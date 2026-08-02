# Chapter 2 — Kinematics

*The geometry of motion, before anyone asks why.*

---

There is a question you probably haven't asked yet, and it's the right one to start with: what does it mean to *describe* motion?

Not explain it. Not cause it. Just describe it — the way a careful observer would write down what they saw, with enough precision that someone who wasn't there could reconstruct every moment of the event from the record.

That's the whole project of this chapter. And it turns out you need fewer ideas than you might expect. Three, really. Position. Velocity. Acceleration. Each one is defined in terms of the one before it, and once you have all three, you can describe — with complete precision — any motion where the acceleration happens to be constant. Which covers a surprising amount of the physical world.

---

## The first idea: position and displacement

Let's start simple. An object is somewhere. You want to say where.

To say where, you need a reference — a place you've agreed to call zero. You also need a direction you've agreed to call positive. Those choices are entirely arbitrary. You pick them, and then you commit to them for the duration of the problem. Nothing physical depends on your choice. The physics is in the relationships between quantities, not in the quantities themselves.

With a reference and a direction fixed, the *position* of an object is just a number with a unit: how far it is from zero, with a sign that tells you which direction. Five meters to the right of the traffic light: $x = +5 \text{ m}$. Two meters to the left: $x = -2 \text{ m}$.

Now the object moves. It was at $x_0$. It's now at $x$. The *displacement* is

$$\Delta x = x - x_0.$$

Delta — $\Delta$ — always means "final minus initial." That's the convention, everywhere in physics, always. Displacement has a sign. Positive means it moved in the positive direction. Negative means the other way.

Here's where the first subtlety lives. Displacement is not the same as distance. *Distance* is the total length of the path the object actually traveled — all of it, regardless of direction. Displacement is the net result: where did you end up, relative to where you started?

![Number-line schematic: jogger leaves home, runs east 5 km, then returns. Total distance traveled = 10 km. Net displacement = 0. The two quantities measure different things.](../images/02-kinematics-fig-02.png)
*Figure 2.2 — Distance vs Displacement — A Jogger Goes Out 5 km and Back*

A runner who goes $400$ meters down the street and then $400$ meters back has traveled a distance of $800$ meters. Her displacement is zero. She's back where she started. These are different numbers because they answer different questions. Distance answers "how much ground did she cover?" Displacement answers "how much did her position change?"

In later problems this distinction will matter a great deal. For now, just hold both definitions clearly, and notice that they agree whenever motion is only in one direction.

<!-- → [FIGURE: Number line showing a runner's path: start at 0, move to +400m, return to 0. Arrow for displacement = 0 labeled in one color, total path distance = 800m labeled differently. Caption: Displacement and distance are the same quantity only when motion never reverses direction.] -->

---

## The second idea: velocity

Motion means position is changing with time. So the natural next question is: how fast?

We define *average velocity* as displacement divided by elapsed time:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x - x_0}{t - t_0}.$$

The bar marks it as an average. Velocity has units of length per time — meters per second in the SI system — and a sign. Positive velocity means motion in the positive direction. Negative velocity means motion in the other direction. "Negative velocity" does not mean slow; it means *direction*.

Now you can see why we bothered distinguishing displacement from distance. If you used distance in the numerator instead of displacement, you'd get *average speed* — how fast the object was moving, without any information about which way. Speed is the magnitude of velocity. For one-directional motion they're the same. The moment motion can reverse, they diverge.

The runner again: in $240$ seconds she ran $800$ meters back to her starting point. Her average speed was $\frac{800}{240} \approx 3.3 \text{ m/s}$. Her average velocity was $\frac{0}{240} = 0$. She went somewhere and came back — net effect on position: nothing.

This is a little strange the first time you see it. Zero average velocity doesn't mean she stood still. It means her motion was symmetric enough that the net displacement was zero. The speed tells you something the velocity doesn't, and vice versa. Both are useful. You pick the one that answers the question you're actually asking.

<!-- → [TABLE: Two-column comparison — Speed vs. Velocity. Rows: definition, sign behavior, formula, what it answers, runner example value. Caption: Speed and velocity diverge the moment motion can reverse direction. Choosing the wrong one gives the wrong answer.] -->

There's one more concept here that's worth naming now: *instantaneous velocity*. Your car's speedometer doesn't show you an average over the last hour; it shows you how fast you're going *right now*. Formally, instantaneous velocity is the limit of average velocity as the time interval shrinks toward zero:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}.$$

If you know calculus, this is just the derivative of position with respect to time: $v = dx/dt$. If you don't yet, the intuition is enough: as you shrink the window of time you're averaging over, the average velocity converges to a definite value — the velocity at that instant. Later in the course you'll see this same structure everywhere. It's how you turn an accumulated quantity into a rate.

<!-- → [FIGURE: Sequence of three x-t graphs showing progressively smaller Δt intervals around the same point on a curve. Each panel draws the secant line between two points; as the interval shrinks, the secant approaches the tangent. Caption: Instantaneous velocity is the slope of the tangent to the position-time curve — the limit of the secant slope as the time window collapses to zero.] -->

---

## The third idea: acceleration

Velocity tells you how fast position is changing. But velocity can change too. *Acceleration* is how fast velocity is changing.

Average acceleration is defined the same way average velocity is:

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v - v_0}{t - t_0}.$$

Units: meters per second per second — $\text{m/s}^2$. Signed, just like velocity.

Here's where students often get the signs tangled. A negative acceleration doesn't mean the object is slowing down. It means the acceleration points in the negative direction. Whether the object is speeding up or slowing down depends on whether the velocity and the acceleration point in the same direction or opposite directions.

An object moving in the positive direction ($v > 0$) with a negative acceleration ($a < 0$) is slowing down — the acceleration is fighting the motion. But an object moving in the negative direction ($v < 0$) with a negative acceleration ($a < 0$) is *speeding up* — the acceleration and the motion agree. The sign of $a$ alone tells you nothing about whether the object is speeding up or slowing down. You need both signs.

The word "deceleration" is used sometimes to mean "the magnitude of a negative acceleration." It's a convenience, not a new concept. I'll mostly avoid it because it tends to make students sloppy about signs.

<!-- → [TABLE: Four combinations of v and a sign, with column for "speeding up or slowing down" and a brief physical example for each. Caption: Sign of acceleration alone does not determine whether an object is speeding up. You need the relative signs of v and a.] -->

---

![Three labeled scales using the same constant-acceleration kinematic equations: Apollo 11 ascent (a few m/s², minutes); Voyager 2 cruise (essentially zero acceleration, decades); video game projectile (10 m/s², milliseconds)....](../images/02-kinematics-fig-06.png)
*Figure 2.6 — Same Equations, Many Scales — Apollo, Voyager, Game Engine*

## The kinematic equations: what you get when acceleration is constant

Now comes the payoff. Suppose the acceleration is constant — doesn't change with time. This is a special case, not the general rule. But it's an enormously useful special case: free fall, cars braking uniformly, objects on frictionless inclined planes. A large fraction of introductory physics problems live here.

With constant acceleration, you can write down five equations relating position, velocity, acceleration, and time. They all follow from the definitions above; none of them is new physics. Let's derive the important ones.

Start with the definition of average acceleration, rearranged:

$$v = v_0 + at. \tag{1}$$

If you know your initial velocity, the acceleration, and how long it's been acting, you know your current velocity. That's it. One line.

For constant acceleration, the velocity changes linearly from $v_0$ to $v$. The average velocity over the interval is just the midpoint:

$$\bar{v} = \frac{v_0 + v}{2}. \tag{2}$$

(This is only true for constant acceleration. If $a$ varies, the average is not the arithmetic mean.)

Combine the definition of average velocity with equation (2):

$$x = x_0 + \bar{v}\, t = x_0 + \frac{v_0 + v}{2}\, t. \tag{3}$$

Substitute equation (1) for $v$:

$$x = x_0 + v_0 t + \frac{1}{2}at^2. \tag{4}$$

This is the one with the $\frac{1}{2}$ that always looks mysterious. It isn't. The first term ($v_0 t$) is where you'd be if you'd kept moving at constant velocity $v_0$. The second term ($\frac{1}{2}at^2$) is the *extra* displacement from the acceleration. The factor of $\frac{1}{2}$ comes from the fact that the velocity ramps up linearly — it starts at $v_0$ and builds to $v_0 + at$, so the average contribution from the acceleration is half its final value.

![Velocity vs time graph: 747 lands at 70 m/s and decelerates uniformly to 0 in 46.7 seconds (a ≈ -1.5 m/s²). The triangular area under the line equals the stopping distance = 1633 m.](../images/02-kinematics-fig-03.png)
*Figure 2.3 — 747 Landing — v vs t, Area = Stopping Distance*

If you draw the $v$-vs-$t$ graph, the displacement is the area under the curve. The acceleration adds a triangular region — base $t$, height $at$, area $\frac{1}{2}at^2$. The $\frac{1}{2}$ is just the area of a triangle.

<!-- → [FIGURE: v-t graph for constant acceleration. Horizontal axis: time. Vertical axis: velocity. Line starts at v0, rises linearly to v = v0 + at. Rectangle of area v0·t shaded one color; triangle of area ½at² shaded another. Caption: The total displacement is the area under the v-t line — rectangle plus triangle gives equation (4).] -->

Finally, eliminate $t$ between equations (1) and (4) — solve (1) for $t$, substitute into (4), simplify:

$$v^2 = v_0^2 + 2a\,(x - x_0). \tag{5}$$

This one is for when you don't know the time. It connects initial velocity, final velocity, acceleration, and displacement without any $t$ in sight.

So: five equations, four variables ($v_0$, $v$, $a$, $t$, and $x - x_0$ — actually five quantities, any four of which determine the fifth). In any constant-acceleration problem, you know three things and want a fourth. Pick the equation that has your three knowns on the right and your unknown on the left. One line of algebra, and you're done.

<!-- → [TABLE: The five kinematic equations. Columns: equation, what it solves for, which variable is absent. Rows: each of the five equations labeled (1)-(5). Caption: For any constant-acceleration problem, identify what you know and what you want, then pick the equation where the absent variable is the one you don't need.] -->

---

## Free fall: the universal experiment

The most important application of constant-acceleration kinematics is *free fall* — motion under gravity alone, ignoring air resistance.

![Stylized lunar surface with David Scott's hammer and feather released simultaneously. Both reach the surface at the same time because the Moon has no atmosphere. Galileo's prediction confirmed on television, ~1.6 m/s² gravity.](../images/02-kinematics-fig-01.png)
*Figure 2.1 — Apollo 15, Aug 2, 1971 — David Scott Drops a Hammer and a Feather*

On August 2, 1971, astronaut David Scott stood on the surface of the Moon. In one gloved hand: a 1.32-kilogram geological hammer. In the other: a 0.030-kilogram falcon feather. He released them simultaneously. They hit the lunar surface together.

This is what Galileo argued must be true, and what air resistance on Earth usually prevents you from seeing clearly. In vacuum, the only force is gravity, and gravity accelerates every object at the same rate, regardless of mass. On the Moon, that rate is $g_{\text{Moon}} \approx 1.62 \text{ m/s}^2$. On Earth, $g \approx 9.80 \text{ m/s}^2$. On Mars, $3.71 \text{ m/s}^2$. These are properties of the local gravitational field. The mass of the falling object is irrelevant.

<!-- → [TABLE: Surface gravity on Earth, Moon, Mars, and Jupiter. Columns: body, g (m/s²), g relative to Earth. Caption: The free-fall acceleration is a property of the gravitational field, not the falling object. The same rock dropped on each body falls at a different rate.] -->

Why mass cancels out is a deep question — one that Einstein eventually made into a foundational principle of general relativity. For now, it's an empirical fact: in vacuum, everything falls the same way. A coin and a crumpled piece of paper dropped from the same height will hit the ground at almost the same time on Earth, because both are dense enough that air resistance is small compared to gravity over a short fall. In vacuum, there's no "almost" — it's exact.

![Vertical y-axis with up labeled positive. Acceleration of gravity points down with magnitude 9.80 m/s² near Earth's surface, so g = -9.80 m/s² with this convention. Diagram shows a thrown object on its way up (v positive, a...](../images/02-kinematics-fig-04.png)
*Figure 2.4 — Free-Fall Sign Convention — Up Is Positive, g = −9.80 m/s²*

To apply the kinematic equations to free fall, choose a coordinate axis (usually $y$ for vertical), pick a positive direction (usually upward), and set the acceleration:

$$a = -g = -9.80 \text{ m/s}^2.$$

The minus sign is because gravity points downward, and we chose up as positive. That's all. The five equations become:

$$v = v_0 - gt,$$

$$y = y_0 + v_0 t - \tfrac{1}{2}gt^2,$$

$$v^2 = v_0^2 - 2g\,(y - y_0).$$

Not new equations — just equations (1), (4), (5) with $a = -g$ plugged in.

Let me work through a problem in detail, because the details are where students go wrong.

![A rock thrown upward at v₀ = 13.0 m/s from a 5.0 m cliff. Snapshots at t = 1, 2, 3 s show position above ground (13.1, 6.4, −10.7 m) and velocity (3.2, −6.6, −16.4 m/s). The rock reaches apex around t = 1.33 s, then falls past...](../images/02-kinematics-fig-05.png)
*Figure 2.5 — Rock Thrown Upward from a Cliff — Position and Velocity at t = 1, 2, 3 s*

**A rock thrown upward.** You throw a rock straight up with initial velocity $v_0 = 13.0 \text{ m/s}$ from a cliff edge. It clears the edge on the way down and continues falling below your position. Where is it, and how fast is it going, at $t = 1.0$, $2.0$, and $3.0$ seconds?

Set $y_0 = 0$ at the throwing point. Up is positive. $a = -9.80 \text{ m/s}^2$.

At $t = 1.0$ s:
$$y = (13.0)(1.0) - \tfrac{1}{2}(9.80)(1.0)^2 = 13.0 - 4.9 = 8.1 \text{ m}.$$
$$v = 13.0 - (9.80)(1.0) = 3.2 \text{ m/s}.$$
Still moving upward. Slowing down.

At $t = 2.0$ s:
$$y = (13.0)(2.0) - \tfrac{1}{2}(9.80)(2.0)^2 = 26.0 - 19.6 = 6.4 \text{ m}.$$
$$v = 13.0 - (9.80)(2.0) = -6.6 \text{ m/s}.$$
Now moving downward. It peaked somewhere between $t = 1$ and $t = 2$.

At $t = 3.0$ s:
$$y = (13.0)(3.0) - \tfrac{1}{2}(9.80)(3.0)^2 = 39.0 - 44.1 = -5.1 \text{ m}.$$
$$v = 13.0 - (9.80)(3.0) = -16.4 \text{ m/s}.$$
Now below the cliff edge, moving downward and accelerating.

When did it reach the peak? At the peak, $v = 0$:
$$0 = 13.0 - (9.80)t_{\text{peak}} \implies t_{\text{peak}} = \frac{13.0}{9.80} \approx 1.33 \text{ s}.$$

Consistent with the snapshots: it peaked between $t = 1$ and $t = 2$, right where we expected.

Now the misconception I want you to notice and correct permanently: at the peak, the velocity is zero but the acceleration is not. The acceleration is $-9.80 \text{ m/s}^2$ at the peak, just like everywhere else. Gravity doesn't pause because the rock isn't moving. The rock's velocity is zero for an instant; the rate of change of that velocity — the acceleration — is $9.80 \text{ m/s}^2$ downward, continuously. That's exactly why the velocity immediately becomes negative after the peak. Zero velocity plus downward acceleration equals a rock that's about to move downward. There's no mystery once you keep velocity and acceleration separate.

<!-- → [FIGURE: Three-panel graph. Panel 1: y-vs-t — parabola opening downward, starts at 0, peaks at ~1.33 s, crosses below 0 near t=2.6 s. Panel 2: v-vs-t — straight line with negative slope, starts at +13.0, crosses zero at 1.33 s, continues negative. Panel 3: a-vs-t — flat horizontal line at -9.80 for all t. Caption: Position, velocity, and acceleration for the rock problem. Notice that acceleration is constant throughout — including at the peak, where velocity happens to be zero.] -->

---

## What this chapter actually taught you

Kinematics is the *language* of motion. Position tells you where. Velocity tells you how fast and in which direction position is changing. Acceleration tells you how fast and in which direction velocity is changing. Each quantity is the rate of change of the previous one — that nested structure repeats throughout physics.

The constant-acceleration equations are a closed toolkit. With five equations connecting five kinematic quantities, any problem that fits the "constant $a$" assumption can be solved in one or two lines of algebra. The free-fall case applies those equations with $a = g$ downward — and reveals something deep: in vacuum, mass doesn't matter. Every object falls the same way.

Chapter 3 extends this to two dimensions — projectile motion, where the horizontal and vertical directions decouple into two independent one-dimensional kinematic problems. Chapter 4 finally answers the question this chapter carefully avoided: *why* is there acceleration at all? Newton's laws explain what causes the quantities kinematics only describes.

But notice what we accomplished without asking why. We can predict, with precision, where any freely falling object will be at any future moment — given its initial position and velocity. Galileo could do this. Newton could do this. Apollo 15's mission planners could do this. You now can too.

---

## Exercises

### Warm-up

**2.1** *(LO 1)* A swimmer completes one full lap of a 50-meter pool in 42 seconds. Compute (a) total distance, (b) net displacement, (c) average speed, (d) average velocity. Explain in one sentence why (b) and (d) are zero even though the swimmer was moving the whole time.

**2.2** *(LO 2)* A car accelerates from rest to 25 m/s in 8.0 s. What is its average acceleration?

**2.3** *(LO 3)* A bicyclist moving at 4.0 m/s accelerates at $0.50 \text{ m/s}^2$ for 6.0 s. What is her final velocity? How far did she travel?

**2.4** *(LO 4)* Drop a dense small object from rest. How far does it fall in 0.50 s? In 1.0 s? (Ignore air resistance.) Show that the second distance is not twice the first, and explain geometrically why.

### Application

**2.5** *(LO 3)* A car traveling at 30.0 m/s decelerates uniformly at $5.0 \text{ m/s}^2$. (a) How long until it stops? (b) How far does it travel while stopping?

**2.6** *(LO 4)* You throw a baseball straight up at 20.0 m/s. (a) When does it reach its peak? (b) How high is the peak? (c) When does it return to your hand? (d) What is its velocity the instant before it returns?

**2.7** *(LO 4)* On the Moon ($g_{\text{Moon}} = 1.62 \text{ m/s}^2$), you drop a hammer from 1.50 m. (a) How long does it take to hit the ground? (b) Repeat for Earth (no air). (c) David Scott's hammer-and-feather drop took about 1.4 seconds. Does your Moon calculation agree? Show the arithmetic.

**2.8** *(LO 5)* A particle's position is given by $x(t) = 2t^2 - 5t + 3$ (meters, with $t$ in seconds). Compute its velocity and acceleration at $t = 2$ s. (Use the derivative if you know calculus; otherwise, compute average velocities over very small intervals centered on $t = 2$.)

### Synthesis

**2.9** *(LO 3, LO 4)* You drop a stone into a well and hear the splash 2.5 s later. (a) Estimate the depth, ignoring the travel time of sound. (b) The speed of sound in air is 340 m/s. Estimate the correction: how much shallower is the well than your part-(a) answer suggests? Does the correction matter for practical purposes?

**2.10** *(LO 3, LO 5)* Sketch position-vs-time, velocity-vs-time, and acceleration-vs-time graphs for a ball thrown straight up at 10 m/s, caught at the same height 2.0 s later. Put all three on the same time axis. Mark the peak on each graph. Explain why the acceleration graph is a horizontal line even though the position and velocity graphs are curved.

**2.11** *(LO 3, LO 4)* Two balls are released simultaneously from the same height — a bowling ball and a Styrofoam ball — in air at room temperature. In everyday experience, which lands first, and roughly by how much? Explain the discrepancy with ideal free-fall theory using one sentence about drag force and one about why the discrepancy is larger for some objects than others.

### Challenge

**2.12** *(beyond chapter)* A rocket fires for 30 s with constant upward acceleration $a = +20 \text{ m/s}^2$, then the engine cuts out. (a) What are the rocket's velocity and altitude at engine cutoff? (b) How much higher does it coast before reaching its peak? (c) What is the total time from launch until the rocket returns to launch altitude? Work in two segments, each with its own constant acceleration.

**2.13** *(beyond chapter)* Explain in your own words why the constant-acceleration kinematic equations would give increasingly wrong answers for a dense object falling from very high altitude (say, 10 km) through air, even though they work well for short drops. What physical effect breaks the constant-$a$ assumption, and at roughly what speed does it become significant?

---

## LLM Exercise — Chapter 2: Kinematics of Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A kinematic property of your anchor phenomenon — one motion-related quantity (a speed, an acceleration, a stopping distance, a free-fall time) — calculated from inputs and reported with proper units and uncertainty.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste the 1-sentence description from your Chapter 00 / Chapter 1 entry].

For Chapter 2, I want to apply kinematics — position, velocity, acceleration, the equations of constant acceleration, free fall — to one motion-related question about my phenomenon.

Please:

1. Identify ONE motion-related question I can ask about my phenomenon that uses Chapter 2 physics. Be specific. Examples: for a bike commute — what's the average acceleration during a stop at a traffic light? for an espresso machine — at what velocity does water emerge from the portafilter? for a basketball shot — what's the ball's velocity when it leaves my hand?

2. Walk me through which kinematic equation(s) apply. Identify the assumptions (constant acceleration? one dimension? free fall? air resistance ignored?) and flag where each assumption might fail for my real phenomenon.

3. Give me input numbers (sourced or measured). For each: where to get the value, what uncertainty to expect.

4. Solve the equation. Report the answer with proper units and uncertainty (use the percent-addition rule from Chapter 1).

5. One Fermi-style sanity check.

6. One sentence on how this entry will connect to Chapter 4 (forces) when we meet it.

Save the output as logbook/chapter-02-kinematics.md.
```

### What this produces

A second Logbook entry, building on Chapter 1's anchor quantity. By the end of Chapter 2 your Logbook has one foundation document and two physics entries.

### How to adapt this prompt

- *For phenomena involving rotation* (a spinning fan, a record player): replace "kinematics in 1D" with "wait for Chapter 10 — angular kinematics is the better tool." But you can still ask about linear motion of a point on the rotating object as a Chapter 2 exercise.
- *For phenomena involving fluids* (water flow, blood flow): the kinematics equations apply to the fluid speed, but the constant-acceleration assumption usually fails. Use them for an idealized "as-if" calculation and note the gap.
- *For ChatGPT or Gemini:* Identical, with the usual interface substitutions.

### Connection to previous chapters

Builds directly on Chapter 1's anchor quantity. The uncertainty propagation rule from Chapter 1 is applied here.

### Preview of next chapter

Chapter 3 extends kinematics to two dimensions — projectile motion, vectors, components. The Chapter 3 LLM Exercise will ask you to find a 2D motion in your phenomenon (an angled trajectory, a curving path) and analyze it using vector decomposition.

---

**Tags:** kinematics, free-fall, constant-acceleration, position-velocity-acceleration, Apollo-15
