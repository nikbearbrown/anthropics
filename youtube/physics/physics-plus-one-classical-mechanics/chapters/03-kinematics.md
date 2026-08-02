# Chapter 3 — Kinematics

*How to describe motion before you ask what causes it.*

---

## A hammer and a feather, August 2, 1971

Astronaut David Scott is standing on the surface of the Moon. It is the final hour of Apollo 15's third moonwalk. He is wearing a white pressure suit, gloves the size of oven mitts, and a boom-mounted camera is trained on his outstretched hands. In one glove he holds a 1.32-kilogram aluminum geological hammer. In the other, a 0.030-kilogram falcon feather donated by the U.S. Air Force Academy.

He looks into the camera and explains the experiment. "In my left hand, I have a feather; in my right hand, a hammer. I guess one of the reasons we got here today was because of a gentleman named Galileo a long time ago, who made a rather significant discovery about falling objects in gravity fields."

He releases them at the same instant. The feather falls. The hammer falls. They strike the lunar regolith together, four-tenths of a second later. Scott shouts: "How about that! Mr. Galileo was correct in his findings."

<!-- → [IMAGE: still frame from the Apollo 15 broadcast showing Scott's outstretched gloves at the moment of release — caption should note the hammer mass (1.32 kg) and feather mass (0.030 kg) and ask the reader to predict which hits first before reading on] -->

The hammer weighs 44 times more than the feather. On Earth, the feather flutters; the hammer plummets. On the Moon, there is no atmosphere worth mentioning. The only force on each object is the Moon's gravity, and the Moon's gravity accelerates every object at the same rate — about $1.62 \text{ m/s}^2$, roughly one-sixth of Earth's. Mass does not matter. Shape does not matter. Whatever you drop falls at the same acceleration.

That four-tenths of a second is the subject of this chapter. By the end, you will be able to write down the equations that predicted the timing of that drop before Scott pressed record — equations that work equally well on the Moon, on Mars, and on a hypothetical asteroid. The same math governs a basketball bouncing in a gym, a 747 braking on a runway, and a rock thrown off a cliff. The single unifying idea is this: if you know where something is, how fast it is moving, and how that speed is changing, you can predict everything that comes next.

Kinematics is the part of physics that describes motion without asking what causes it. That question — what *causes* acceleration — waits for Chapter 4. What we're after here is the vocabulary and the equations. You have to speak the language before you can use it.

---

## Position, displacement, velocity

Start with the simplest question physics asks: *where is the object?*

**Position** is where an object is, measured along some chosen axis from some chosen origin. We write it $x$ for horizontal motion, $y$ for vertical. The choice of origin and the choice of which direction is positive are completely arbitrary — you can put the origin wherever you like and call any direction positive. But once you've chosen, you have to commit. Every number in the calculation has to respect that choice.

**Displacement** is the change in position:

$$\Delta x = x - x_0$$

where $x_0$ is where the object started and $x$ is where it ended up. Displacement has a sign — positive if the object moved in the positive direction, negative if it moved the other way.

**Distance** is the total length of the path traveled, regardless of direction. It is always positive.

These two are not the same, and confusing them is the first mistake students make. A jogger who runs $400 \text{ m}$ down a straight road and then runs $400 \text{ m}$ back has a displacement of zero — she started and ended at the same place — but a distance of $800 \text{ m}$. The distinction matters because some questions are about the net change in position and some are about how much ground was covered. Pick the right one or you'll get the wrong answer.

<!-- → [DIAGRAM: number-line diagram of the jogger's path — origin at start, arrow right to +400 m labeled "leg 1," arrow back left to 0 labeled "leg 2"; annotate total distance (800 m, the sum of both arrows' lengths) and net displacement (0, start = finish); student should see at a glance why the two numbers are different] -->

**Average velocity** is displacement divided by elapsed time:

$$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x - x_0}{t - t_0}$$

The bar marks it as an average. Velocity has units of m/s and carries a sign. Negative velocity doesn't mean slow — it means moving in the negative direction. That jogger's average velocity for the full out-and-back run was zero, even though she was moving the whole time.

**Average speed** is distance divided by time — unsigned, always positive. For the same jogger, if the whole run took ten minutes ($600 \text{ s}$), her average speed was $800 / 600 \approx 1.3 \text{ m/s}$ and her average velocity was zero. The numerators are different.

**Instantaneous velocity** is the velocity at one specific instant — what your speedometer reads at a single moment. Mathematically, it is the limiting case of average velocity as the time interval shrinks to zero:

$$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}$$

If you know calculus, this is just the derivative $dx/dt$. If you don't know calculus yet, the intuitive picture is enough: as your measurement window gets smaller and smaller, the average velocity over that window converges to a definite number. That number is the velocity *right now*.

The vocabulary trade is simple: everyday speech treats "speed" and "velocity" as synonyms, and everyday speech gets away with it because most everyday motion doesn't change direction. Physics makes them distinct because the equations require the distinction. The cost is small. The benefit is that every later calculation actually works.

---

## Acceleration and the kinematic equations

Now add the second layer: velocity can change.

**Average acceleration** is how fast velocity is changing:

$$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v - v_0}{t - t_0}$$

Units are m/s² — velocity per time. Like velocity, acceleration is signed. Negative acceleration means velocity is becoming more negative. If the object is already moving in the negative direction, negative acceleration speeds it up. If it's moving in the positive direction, negative acceleration slows it down. The relationship between sign of $a$ and sign of $v$ is what tells you whether the object is speeding up or slowing down — the sign of $a$ alone doesn't.

For most of this chapter we make one simplifying assumption: *acceleration is constant.* Many real situations satisfy this well enough (free fall over short distances; a car braking at a steady rate; a ball rolling down a ramp). For situations where acceleration varies, we break the motion into segments, each approximately constant. With this assumption, four equations connect all the kinematic quantities. Setting $t_0 = 0$ so that $\Delta t = t$, and using subscript $0$ for initial values:

**Equation 1 — average velocity for constant acceleration:**

$$\bar{v} = \frac{v_0 + v}{2}$$

When velocity changes linearly in time, the average is simply the mean of the endpoints.

**Equation 2 — position from average velocity:**

$$x = x_0 + \bar{v} \, t$$

The definition of average velocity, solved for position. If you know how fast you went on average and for how long, you know how far you got.

**Equation 3 — final velocity from acceleration:**

$$v = v_0 + a t$$

Direct from the definition of acceleration. After time $t$ at constant acceleration $a$, your velocity has changed by $at$.

**Equation 4 — position from initial velocity and acceleration:**

$$x = x_0 + v_0 t + \tfrac{1}{2} a t^2$$

This combines Equations 2 and 3. The first two terms describe motion at constant velocity $v_0$; the third term is the additional displacement contributed by acceleration. The factor of $\tfrac{1}{2}$ is not arbitrary — it is the area of a triangle under the velocity-time graph, the geometric signature of linearly changing velocity.

A fifth equation eliminates $t$ when you have initial and final velocities and want displacement:

**Equation 5 — final velocity from displacement:**

$$v^2 = v_0^2 + 2a(x - x_0)$$

Memorize these. Better — understand what each one solves for, so you can pick the right one for any problem.

<!-- → [TABLE: five-row reference table of the kinematic equations — columns: equation number, formula, what it solves for, what it requires (knowns), what it omits (e.g., Eq. 5 has no t); last column: one real-world example for each. Student should be able to use this table as a decision tree at the start of any problem] -->

Here is the method in practice. A Boeing 747 lands at $v_0 = 70.0 \text{ m/s}$ and decelerates at $a = -1.50 \text{ m/s}^2$ — every second, its speed drops by $1.5 \text{ m/s}$.

*How long until it stops?* Set $v = 0$ in Equation 3:

$$0 = 70.0 + (-1.50) t \implies t = \frac{70.0}{1.50} \approx 46.7 \text{ s}$$

*How far does it travel?* Apply Equation 5 with $v = 0$ and $x_0 = 0$:

$$0 = (70.0)^2 + 2(-1.50) x \implies x = \frac{4900}{3.00} \approx 1{,}633 \text{ m}$$

The plane needs about $1.6 \text{ km}$ of runway. Real 747 landing data puts the ground roll in the range of $1.5$–$2 \text{ km}$ under normal conditions. The calculation lands inside that range. That's the sanity check: does the answer match what we know, roughly, from the real world?

<!-- → [CHART: velocity-time graph for the 747 braking from 70.0 m/s to 0 over 46.7 s — straight line with negative slope, area under the line shaded and labeled "displacement = 1,633 m"; caption should note that the area of the triangle is ½ × base × height = ½ × 46.7 × 70.0, confirming Equation 4 geometrically] -->

The selection logic is always the same. *What do I know? What do I want?* Find the equation that has your knowns on the right side and your unknown on the left. For constant-acceleration problems in one dimension, at least one of the five equations gives the answer in one algebraic step.

Notice what's happening with the sign on $a$. The 747 is moving in the positive direction (forward) and decelerating, so $a$ is negative. The answer $x \approx 1{,}633 \text{ m}$ came out positive, which is correct — the plane moved forward. The sign structure is doing real work. Pick a positive direction at the start of every problem and don't switch. A negative answer isn't a mistake; it means "in the negative direction."

---

## Free fall

Everything we have just done is fully general for constant acceleration. The most important special case — the one Galileo worked out, the one David Scott demonstrated on the Moon — is when the only force on an object is gravity and there is no air.

In a vacuum, every object falls at the same acceleration:

$$g = 9.80 \text{ m/s}^2 \text{ on Earth's surface, directed downward.}$$

Strictly, $g$ varies a little — from $9.78 \text{ m/s}^2$ at the equator to $9.83 \text{ m/s}^2$ at the poles, with smaller corrections for altitude. We use $9.80$ unless told otherwise. On the Moon, $g_\text{Moon} \approx 1.62 \text{ m/s}^2$. On Mars, $g_\text{Mars} \approx 3.71 \text{ m/s}^2$.

This is not obvious. It is one of the stranger facts in physics when you first encounter it. Why should the Moon's gravity treat a 1.32-kilogram hammer the same as a 0.030-kilogram feather? The short answer is that gravity exerts more force on the heavier object, but the heavier object also requires more force to accelerate by the same amount — and the two effects exactly cancel. Newton's law of gravitation says force is proportional to mass; Newton's second law says acceleration equals force divided by mass. The mass appears in both equations and cancels. What remains is an acceleration that depends only on where you are (which determines $g$), not on what you are. Einstein elevated this cancellation from a numerical accident to a foundational principle — the equivalence principle — that we will not reach until Chapter 28. For now, accept the fact and use it.

Set up the coordinate system. Take *up* as positive. Then the gravitational acceleration is *down*, which is negative in our convention: $a = -g = -9.80 \text{ m/s}^2$. The kinematic equations become:

<!-- → [DIAGRAM: vertical axis with up labeled positive, a downward arrow labeled g = 9.80 m/s² pointing in the negative direction; show the same axis relabeled with down positive to demonstrate both valid conventions side by side; the point is that the physics is identical — only the sign of g in the equations changes] -->

$$v = v_0 - gt$$

$$y = y_0 + v_0 t - \tfrac{1}{2} g t^2$$

$$v^2 = v_0^2 - 2g(y - y_0)$$

These are not new equations. They are Equations 3, 4, and 5 with $a = -g$ substituted in. Free fall is a special case of constant-acceleration kinematics, not a separate subject. The reason it gets its own section is that it comes up constantly, and it's worth practicing until the substitution is automatic.

One more thing about sign conventions before the worked example. If you take *down* as positive — which is equally valid, just a different choice — then $a = +g$ and all the signs flip. Either convention gives the same physical answer. What breaks problems is inconsistency: starting with up-positive, then drifting mid-calculation to treating a downward displacement as positive. Pick one. Stick to it.

A worked example. A person standing on the edge of a cliff throws a rock straight up with $v_0 = 13.0 \text{ m/s}$. The rock misses the cliff edge on the way down and continues falling. Taking up as positive, with $y_0 = 0$ at the throwing point:

*Where is the rock at $t = 1.00 \text{ s}$, $2.00 \text{ s}$, $3.00 \text{ s}$?*

$$y_1 = (13.0)(1.00) - \tfrac{1}{2}(9.80)(1.00)^2 = 13.0 - 4.90 = 8.10 \text{ m}$$

$$y_2 = (13.0)(2.00) - \tfrac{1}{2}(9.80)(2.00)^2 = 26.0 - 19.6 = 6.40 \text{ m}$$

$$y_3 = (13.0)(3.00) - \tfrac{1}{2}(9.80)(3.00)^2 = 39.0 - 44.1 = -5.10 \text{ m}$$

At $t = 1$ second, the rock is $8.10 \text{ m}$ above the throwing point, still rising. At $t = 2$ seconds, $6.40 \text{ m}$ above — it has turned around, peaked somewhere between $t = 1$ and $t = 2$, and is now heading back down. At $t = 3$ seconds, $-5.10 \text{ m}$ — it is $5.10 \text{ m}$ below the throwing point, past the cliff edge, still falling.

<!-- → [CHART: two-panel figure — left: position-time graph (parabola) for the rock from t=0 to t=3 s, with the three computed points plotted and the peak at t=1.33 s marked; right: velocity-time graph (straight line from +13.0 m/s to –16.4 m/s) crossing zero at t=1.33 s; caption should note that the slope of the v-t line is constant at –9.80 m/s² throughout, including at the peak] -->

*When did it reach the peak?*

At the peak, $v = 0$. Set $v = v_0 - gt = 0$:

$$t_\text{peak} = \frac{v_0}{g} = \frac{13.0}{9.80} \approx 1.33 \text{ s}$$

Consistent with the position snapshot: the peak occurs between $t = 1$ and $t = 2$, closer to $t = 1$. The calculation and the snapshot agree.

Now the misconception worth naming explicitly: at the peak, the rock's velocity is zero, but its acceleration is not. Acceleration is still $-9.80 \text{ m/s}^2$ at the peak — gravity has not turned off. The rock is accelerating downward even at the instant it is momentarily at rest. That is *why* it starts falling immediately: the acceleration is what changes the velocity from zero to negative. Velocity zero and acceleration zero are not the same condition.

The Apollo 15 hammer-and-feather drop, revisited. The hammer fell from about $1.50 \text{ m}$ above the lunar surface. With $y_0 = 1.50$, $v_0 = 0$, $a = -g_\text{Moon} = -1.62 \text{ m/s}^2$, solve for the time to reach $y = 0$:

$$0 = 1.50 + 0 - \tfrac{1}{2}(1.62) t^2 \implies t = \sqrt{\frac{2 \times 1.50}{1.62}} \approx 1.36 \text{ s}$$

Scott said they hit together "four-tenths of a second later," which would mean he was holding them much lower than chest height — closer to $0.13 \text{ m}$ above the surface. (Check: $t = \sqrt{2 \times 0.13 / 1.62} \approx 0.40 \text{ s}$, which works.) Either way, the equations produce the timing. The math was written before the mission; the mission confirmed the math.

---

## What connects the three ideas

Position, velocity, acceleration are not three independent concepts. They are one idea, layered.

Velocity is the rate of change of position. Acceleration is the rate of change of velocity. Position accumulates from velocity; velocity accumulates from acceleration. The kinematic equations are the expressions of that layered structure for the special case where the bottom layer — acceleration — is constant. Once you fix acceleration, the whole structure of the motion is determined, forward in time, by nothing more than algebra.

This is the *descriptive* side of mechanics. It tells you what the motion looks like. It says nothing about why. Why does the 747 decelerate at $1.50 \text{ m/s}^2$ rather than $3.00$ or $0.50$? Why is $g$ on Earth $9.80 \text{ m/s}^2$ rather than $5$ or $20$? Kinematics cannot answer those questions — the answers require Newton's laws, which require the concept of *force*, which is Chapter 4.

The deliberate separation is one of the best design decisions in the pedagogy of physics. You learn to describe motion first, precisely and completely, without the complication of explaining it. Then, when the explanation arrives, you already have the language to receive it. Every kinematic equation you've seen in this chapter will reappear in Chapter 4, but on the right side of $F = ma$ rather than standing alone. They are vocabulary waiting for a sentence.

There is something deeper here worth noticing. The constant-acceleration assumption is exact only in ideal cases. Real accelerations change. A falling skydiver is pulled down by gravity and pushed up by air drag; drag grows with speed, so the net downward acceleration decreases as the diver falls faster, until drag balances gravity and acceleration drops to zero — that is terminal velocity, roughly $55 \text{ m/s}$ for a spread-eagled human, at which point the skydiver is moving fast but no longer accelerating. The kinematic equations of this chapter cannot handle that case exactly.

But here is the key: over any short enough time interval, *any* smoothly changing acceleration is approximately constant. The same five equations, applied piecewise over small time intervals, become the basis of every numerical simulation of motion ever written. Every video game physics engine, every flight simulator, every orbital mechanics code is doing this: divide time into tiny steps; at each step, pretend acceleration is constant; advance position and velocity by one step; repeat. The equations you memorized this chapter are, scaled up by computer power and reduced to millisecond intervals, the equations that run simulations of the solar system. From David Scott's four-tenths of a second to the orbit of Voyager 2, kinematics is the single language.

<!-- → [INFOGRAPHIC: three-panel scale comparison — left: Scott's 0.40-second hammer drop on the Moon (height ~0.13 m); center: a skydiver's 60-second free fall (~1.8 km altitude drop, showing terminal velocity curve as acceleration decreases); right: Voyager 2's trajectory schematic (decades of travel, piecewise gravity from multiple planets); caption: "The same five equations, applied at different scales and time-step sizes, describe all three" — student should feel the range of applicability] -->

---

## Exercises

### Warm-up

**3.1** A swimmer in a $50 \text{ m}$ pool swims one full lap (down and back) in $42 \text{ s}$. Compute (a) total distance, (b) net displacement, (c) average speed, (d) average velocity.

**3.2** A car accelerates from rest to $25 \text{ m/s}$ in $8.0 \text{ s}$. What is its average acceleration?

**3.3** A bicyclist initially traveling at $4.0 \text{ m/s}$ accelerates at $0.50 \text{ m/s}^2$ for $6.0 \text{ s}$. What is her final velocity?

**3.4** Drop a small dense object from rest. How far does it fall in $0.50$ seconds, ignoring air resistance? In $1.0$ seconds?

### Application

**3.5** A car traveling at $30.0 \text{ m/s}$ decelerates at $5.0 \text{ m/s}^2$. (a) How far does it travel before stopping? (b) How long does the deceleration take?

**3.6** You throw a baseball straight up with initial velocity $20.0 \text{ m/s}$. Compute (a) the time to reach peak height, (b) the peak height, (c) the time at which the ball returns to your hand.

**3.7** On the Moon, where $g_\text{Moon} = 1.62 \text{ m/s}^2$, a hammer is dropped from $1.50 \text{ m}$ above the surface. (a) How long does it take to hit the ground? (b) On Earth (no air), how long would the same drop take? (c) Scott's footage suggests a drop time of about $0.40 \text{ s}$ — reconcile this with your calculation in part (a) by estimating the actual drop height.

**3.8** The position of a particle is given by $x(t) = 2t^2 - 5t + 3$ (meters, $t$ in seconds). Compute its velocity and acceleration at $t = 2 \text{ s}$. If you know calculus, take derivatives. If not, compute average velocities over $\Delta t = 0.001 \text{ s}$ centered on $t = 2$.

### Synthesis

**3.9** You drop a stone into a vertical well and hear it splash $2.5 \text{ s}$ later. (a) Estimate the depth of the well, ignoring the travel time of sound. (b) Estimate how much the answer changes if you account for the speed of sound ($340 \text{ m/s}$) returning from the bottom.

**3.10** Sketch position-vs-time, velocity-vs-time, and acceleration-vs-time graphs for a ball thrown straight up with initial velocity $10 \text{ m/s}$, caught at the same height $2 \text{ s}$ later. Draw all three on the same time axis. Mark the peak on each.

**3.11** Two balls are dropped simultaneously from the same height — one a bowling ball, one a Styrofoam ball, both in air. Which hits the ground first in practice, roughly by how much, and why does this contradict free-fall theory? Explain using one sentence about air resistance and one about the magnitudes involved.

### Challenge

**3.12** A rocket fires its engine for the first $30 \text{ s}$ of vertical flight, producing constant acceleration $a = +20 \text{ m/s}^2$. After $30 \text{ s}$, the engine cuts out and the rocket is in free fall. Compute (a) velocity and altitude at engine cutoff, (b) additional altitude gained after cutoff before the rocket peaks, (c) total flight time from launch back to launch altitude. Treat as two constant-acceleration segments.

**3.13** Explain in your own words why the four constant-acceleration equations would not correctly describe a freely falling skydiver over a long fall. What physical effect breaks the constant-$a$ assumption, roughly at what point in the fall does it become significant, and what is the mathematical tool you would reach for to handle it properly?

---

## LLM Exercise — Chapter 3: Kinematics of Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** A kinematic property of your anchor phenomenon — one motion-related quantity (a speed, an acceleration, a stopping distance, a free-fall time) — calculated from inputs and reported with proper units and uncertainty.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste the 1-sentence description from your Chapter 1 entry].

For Chapter 3, I want to apply kinematics — position, velocity, acceleration, the equations of constant acceleration, free fall — to one motion-related question about my phenomenon.

Please:

1. Identify ONE motion-related question I can ask about my phenomenon that uses Chapter 3 physics. Be specific. Examples: for a bike commute — what's the average acceleration during a stop at a traffic light? for an espresso machine — at what velocity does water emerge from the portafilter? for a basketball shot — what's the ball's velocity when it leaves my hand?

2. Walk me through which kinematic equation(s) apply. Identify the assumptions (constant acceleration? one dimension? free fall? air resistance ignored?) and flag where each assumption might fail for my real phenomenon.

3. Give me input numbers (sourced or measured). For each: where to get the value, what uncertainty to expect.

4. Solve the equation. Report the answer with proper units and uncertainty (use the percent-addition rule from Chapter 1).

5. One Fermi-style sanity check.

6. One sentence on how this entry will connect to Chapter 4 (forces) when we meet it.

Save the output as logbook/chapter-03-kinematics.md.
```

### What this produces

A third Logbook entry, building on Chapter 1's anchor quantity. By the end of Chapter 3 your Logbook has one foundation document and three physics entries.

### How to adapt this prompt

- *For phenomena involving rotation* (a spinning fan, a record player): replace "kinematics in 1D" with "wait for Chapter 10 — angular kinematics is the better tool." But you can still ask about linear motion of a point on the rotating object as a Chapter 3 exercise.
- *For phenomena involving fluids* (water flow, blood flow): the kinematics equations apply to the fluid speed, but the constant-acceleration assumption usually fails. Use them for an idealized "as-if" calculation and note the gap.
- *For ChatGPT or Gemini:* Identical, with the usual interface substitutions.

### Connection to previous chapters

Builds directly on Chapter 1's anchor quantity. The uncertainty propagation rule from Chapter 1 is applied here.

### Preview of next chapter

Chapter 4 extends kinematics to two dimensions — projectile motion, vectors, components. The Chapter 4 LLM Exercise will ask you to find a 2D motion in your phenomenon (an angled trajectory, a curving path) and analyze it using vector decomposition.

---

## AI Wayback Machine

**Galileo Galilei** worked out the kinematics of falling bodies in the late 16th century — showing that distance scales with the square of time, independent of mass. He performed experiments by rolling balls down inclined planes when free-fall was too fast to measure directly.

**Run this:**

```
Who was Galileo Galilei, and how does his work on kinematics connect to what we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Galileo Galilei"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Galileo's inclined-plane experiment and the math he extracted from it.
- Ask it about Galileo's house arrest after his 1633 trial, and what he wrote during it.

What changes? What gets better? What gets worse?
