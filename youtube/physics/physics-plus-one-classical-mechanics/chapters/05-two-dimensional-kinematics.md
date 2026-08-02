# Chapter 5 — Two-Dimensional Kinematics

*How two straight-line problems, running in parallel, become a curve.*

---

## A coin flicked off a desk, a coin nudged off the edge

A physics professor stands at the front of a lecture hall with two identical coins on the corner of her desk. She puts one finger on the first coin and a second finger on the second. With one quick motion, she flicks the first coin horizontally — it sails out in a graceful arc, lands a meter away with a clear *clink*. At the same instant, she nudges the second coin off the edge — it falls straight down and lands directly below the desk corner with its own *clink*.

Two clinks. One arrived a meter out. The other arrived directly below. They sounded at the same time.

Most students hear it but don't believe it. Surely the coin that traveled farther took longer? It went farther through the air; more air, more time. Try it yourself with a coin and a ruler on the edge of a table: flick one coin, push the other off at the same moment. Listen.

The clinks are simultaneous because horizontal motion does not affect vertical fall. Each coin falls under gravity at the same rate — $g = 9.80 \text{ m/s}^2$ — regardless of how fast it is also moving sideways. The flicked coin had a horizontal velocity. That changed *where* it landed, not *when*. Sideways speed and downward fall do not negotiate with each other.

<!-- → [IMAGE: strobe-style illustration of the two-coin experiment — show both coins at the same five or six instants during the fall; the flicked coin moves rightward at each step while both coins descend to the same vertical positions in lockstep; caption should ask the reader to confirm that every row is level before reading on] -->

This is the most important fact in two-dimensional kinematics, and Galileo was the first to write it down clearly. Once you have it, every projectile problem in this book — a fireworks shell, an arrow loosed at a target, a basketball arcing toward the rim — collapses into two one-dimensional problems running in parallel. You already know how to solve those.

---

## Vectors and components

Before we can use the independence of perpendicular motions, we need a language for motion that has direction. That language is vectors.

A **scalar** is a quantity with a magnitude only: mass, time, temperature, energy. A **vector** is a quantity with both magnitude and direction: position, displacement, velocity, acceleration, force. Every vector in this chapter lives in a plane, and any such vector can be drawn as an arrow — the length encodes the magnitude, the direction of the arrow encodes the direction.

The central trick is this. Any two-dimensional vector $\mathbf{A}$ can be split into two perpendicular pieces, one pointing along the $x$-axis and one along the $y$-axis:

$$\mathbf{A} = \mathbf{A}_x + \mathbf{A}_y.$$

These are the **components** of $\mathbf{A}$. If $\mathbf{A}$ has magnitude $A$ and points at angle $\theta$ above the $x$-axis, the right-triangle geometry gives:

$$A_x = A\cos\theta, \qquad A_y = A\sin\theta.$$

Going the other way — from components back to magnitude and angle — is the Pythagorean theorem:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \theta = \tan^{-1}\!\left(\frac{A_y}{A_x}\right).$$

<!-- → [DIAGRAM: right-triangle decomposition — draw vector A as a diagonal arrow from the origin, with Ax as the horizontal leg labeled A cosθ, Ay as the vertical leg labeled A sinθ, the angle θ marked at the origin; add a second panel showing the 3-4-5 counterexample (Ax=3, Ay=4, A=5, not 7) to illustrate why magnitudes don't add; caption: "the components add as vectors, not as numbers"] -->

A common mistake: $A_x + A_y \neq A$. The components don't add numerically to the magnitude. If $A_x = 3$ and $A_y = 4$, the magnitude is $\sqrt{9 + 16} = 5$, not $7$. The components add as *vectors* — tip-to-tail arrows — and the magnitude of their sum is recovered by the Pythagorean theorem, not arithmetic.

The reason components matter is that vector addition becomes trivial once you decompose. Adding two vectors $\mathbf{A}$ and $\mathbf{B}$ that point in different directions looks hard in arrow-and-protractor mode. Once decomposed:

$$R_x = A_x + B_x, \qquad R_y = A_y + B_y.$$

Components along the same axis add as ordinary numbers. Reconstruct the resultant from $R = \sqrt{R_x^2 + R_y^2}$ and $\theta = \tan^{-1}(R_y / R_x)$. Every vector addition problem in this book follows exactly this recipe.

Here it is in practice. A hiker walks $53.0 \text{ m}$ at $20.0°$ north of east, then $34.0 \text{ m}$ at $63.0°$ north of east. Let $x$ be east, $y$ be north.

First leg:
$$A_x = (53.0)\cos(20.0°) = 49.8 \text{ m}, \qquad A_y = (53.0)\sin(20.0°) = 18.1 \text{ m}.$$

Second leg:
$$B_x = (34.0)\cos(63.0°) = 15.4 \text{ m}, \qquad B_y = (34.0)\sin(63.0°) = 30.3 \text{ m}.$$

Resultant:
$$R_x = 49.8 + 15.4 = 65.2 \text{ m}, \qquad R_y = 18.1 + 30.3 = 48.4 \text{ m}.$$

$$R = \sqrt{(65.2)^2 + (48.4)^2} = \sqrt{6594} \approx 81.2 \text{ m}, \qquad \theta = \tan^{-1}(48.4/65.2) \approx 36.6°.$$

She ends up $81.2 \text{ m}$ from her start, $36.6°$ north of east. The answer passes the obvious sanity checks: it is less than her total path ($87 \text{ m}$), and the direction falls between the angles of her two legs ($20°$ and $63°$), weighted toward the longer first leg.

<!-- → [DIAGRAM: top-down map of the hiker's two-leg path — draw leg A (53 m at 20° NE) as an arrow, then leg B (34 m at 63° NE) tip-to-tail, then the resultant R (81.2 m at 36.6° NE) as a dashed arrow from start to finish; annotate each leg with its length and angle; caption should note that the resultant is shorter than the path total and ask the reader why it must be] -->

One more trap with components. The formula $A_x = A\cos\theta$ and $A_y = A\sin\theta$ is correct only when $\theta$ is measured from the $x$-axis. If you measure from the $y$-axis, the sine and cosine swap. This is not something to memorize — it is something to draw. Sketch the vector, draw the right triangle, label the sides, and read off which function you need. Every time.

---

## The independence of perpendicular motions

In 1948, Harold Edgerton — the MIT engineer who made strobe photography famous — captured two billiard balls falling side by side. One was released from rest. The other was thrown horizontally at the same instant from the same height. The strobe flashed every $1/30$ of a second; the image shows both balls as a sequence of frozen positions.

At every flash, the two balls were at the same height. The thrown ball was farther to the side, but always level with the dropped ball. The horizontal velocity did not touch the vertical fall.

This is the experimental proof of what the desk-coin demonstration shows in a lecture hall: **horizontal and vertical motions under gravity are independent.** They share a clock, but each runs by its own rules. Gravity pulls downward; there is no horizontal component of gravity to disturb horizontal motion, and there is no horizontal component of velocity to disturb the vertical fall.

The consequence is algorithmic. Take any object moving in two dimensions under gravity alone. Resolve its initial velocity into components:

$$v_{0x} = v_0\cos\theta_0, \qquad v_{0y} = v_0\sin\theta_0.$$

Then write the kinematic equations — from Chapter 3 — separately for each axis.

**Horizontal** ($a_x = 0$, no horizontal gravity):
$$x = x_0 + v_{0x}\, t, \qquad v_x = v_{0x} = \text{constant}.$$

**Vertical** ($a_y = -g$, taking up as positive):
$$y = y_0 + v_{0y}\, t - \tfrac{1}{2}g t^2, \qquad v_y = v_{0y} - gt, \qquad v_y^2 = v_{0y}^2 - 2g(y - y_0).$$

The two systems share only $t$. Find $t$ from whichever axis gives you a condition — usually vertical, since gravity sets the flight time — and substitute into the other. That is the complete algorithm for projectile motion.

Notice that the horizontal velocity is constant throughout. At the peak of the arc, when the vertical velocity is momentarily zero, the horizontal velocity is still exactly $v_{0x}$. The ball at its apex is not hovering; it is moving sideways at full speed while being, for an instant, neither going up nor going down. The arc is the trace of those two simultaneous motions.

A worked example that makes this concrete. A fireworks shell is launched at $v_0 = 70.0 \text{ m/s}$ at $75.0°$ above horizontal. Where does it peak, and when?

**Resolve:**
$$v_{0x} = (70.0)\cos(75.0°) = 18.1 \text{ m/s}, \qquad v_{0y} = (70.0)\sin(75.0°) = 67.6 \text{ m/s}.$$

**Time to peak** (where $v_y = 0$):
$$t_\text{peak} = \frac{v_{0y}}{g} = \frac{67.6}{9.80} \approx 6.90 \text{ s}.$$

**Height at peak:**
$$y = \frac{v_{0y}^2}{2g} = \frac{(67.6)^2}{2(9.80)} \approx 233 \text{ m}.$$

**Horizontal distance at that time:**
$$x = v_{0x}\, t_\text{peak} = (18.1)(6.90) \approx 125 \text{ m}.$$

The shell explodes about $233 \text{ m}$ up, $125 \text{ m}$ downrange, $6.90 \text{ s}$ after launch. Professional display shells peak between $200$ and $400 \text{ m}$; at any fireworks show, count the seconds between the launch thump and the burst — you will typically count six to eight. The numbers are in range.

<!-- → [CHART: parabolic trajectory of the fireworks shell — x-axis: horizontal distance (0 to ~125 m), y-axis: height (0 to ~233 m); mark the launch point, the peak (125 m, 233 m), and note the time labels at t=0, t=3.45 s (halfway), t=6.90 s (peak); show the horizontal velocity vector as a constant-length arrow at several points along the arc to make the constancy of vx visible; the parabola should look steep, reflecting the 75° launch angle] -->

This treatment ignores air resistance. For a fireworks shell that is essentially a burning canister moving through air, drag is real. But the vacuum calculation gives the right order of magnitude and captures every qualitative feature of the trajectory. The parabolic arc, the symmetry between ascent and descent, the independence of horizontal and vertical — these are all exact in vacuum and approximately true in air for dense, compact objects over reasonable distances.

Two misconceptions worth naming, because they come up constantly.

First: at the peak, gravity has not switched off. The vertical velocity is zero; the vertical *acceleration* is still $-9.80 \text{ m/s}^2$. Gravity does not care that the ball is momentarily not moving vertically — it pulls down regardless. The instant after the peak, velocity is small and negative; an instant later, it is more negative; gravity has been acting throughout. Velocity zero and acceleration zero are not the same condition.

Second: launching steeper does not always increase range. The range on level ground is:

$$R = \frac{v_0^2 \sin(2\theta_0)}{g}.$$

This is maximized when $\sin(2\theta_0) = 1$, which occurs at $\theta_0 = 45°$. A shell at $75°$ is trading horizontal reach for altitude — it goes high, not far. A shell at $45°$ travels the same speed but divides it more evenly between horizontal and vertical, maximizing the product of flight time and horizontal velocity. The $75°$ angle is correct for fireworks, where height matters and downrange distance is a safety consideration. For a thrown ball or a long jump, $45°$ is the theoretical optimum — and real long jumpers hit $42°$–$43°$ because their legs can generate more speed at shallower angles.

<!-- → [CHART: family of projectile trajectories from the same launch speed at five angles (15°, 30°, 45°, 60°, 75°) — overlay all five parabolas on one set of axes; draw a dotted envelope curve connecting the peaks; annotate 45° as the maximum-range trajectory and 75°/15° as the symmetric pair with the same range but different heights; caption: "complementary angles (θ and 90°−θ) give the same range but different peak heights"] -->

---

## Adding velocities: motion relative to motion

A canoe is launched from the east bank of a river. The paddler aims the bow due west and paddles steadily, keeping the nose pointed straight across. The expectation: arrive directly opposite. The reality: arrive downstream, somewhere.

This is not a paddling error. The canoe's velocity relative to the water is westward. The water's velocity relative to the ground is downstream. The canoe's velocity relative to the ground — which is what determines where you land — is the vector sum. There is no orientation of the bow that eliminates the current's contribution; it adds no matter what.

The rule is:

$$\mathbf{v}_\text{object/ground} = \mathbf{v}_\text{object/medium} + \mathbf{v}_\text{medium/ground}.$$

The subscripts cancel diagonally, which is a useful mnemonic: object/ground on the left, object/medium and medium/ground on the right. In components, you decompose each velocity onto a common pair of axes, add component by component, and reconstruct.

A boat points perpendicular to the bank at $v_y = 0.750 \text{ m/s}$ relative to the water. The river flows downstream at $v_x = 1.20 \text{ m/s}$ relative to the shore. Let $x$ be downstream, $y$ be across.

$$v_\text{tot,x} = 0 + 1.20 = 1.20 \text{ m/s}, \qquad v_\text{tot,y} = 0.750 + 0 = 0.750 \text{ m/s}.$$

$$v_\text{tot} = \sqrt{(1.20)^2 + (0.750)^2} \approx 1.42 \text{ m/s}, \qquad \theta = \tan^{-1}(0.750/1.20) \approx 32.0°.$$

The boat moves at $1.42 \text{ m/s}$ relative to shore, $32°$ from downstream. The river is faster than the paddler ($1.20 > 0.750$), so the downstream component dominates — the angle is less than $45°$, meaning the boat is being swept more parallel to the bank than across it.

<!-- → [DIAGRAM: top-down river view — draw the boat's velocity relative to water as an arrow pointing straight across (v=0.750 m/s), the river current as an arrow pointing downstream (v=1.20 m/s), and the resultant ground-track velocity as a diagonal arrow (1.42 m/s at 32° from downstream); annotate all three vectors with their labels and magnitudes; show the actual ground track as a dashed diagonal line from launch point to landing point on the far bank, well downstream of the intended straight-across crossing] -->

The same structure governs an airplane in a crosswind. The plane heads north at $200 \text{ km/h}$ relative to the air; a west wind pushes the air eastward at $50 \text{ km/h}$ relative to the ground. The plane's ground track is the vector sum: $200 \text{ km/h}$ north plus $50 \text{ km/h}$ east, giving $\sqrt{200^2 + 50^2} \approx 206 \text{ km/h}$ at about $14°$ east of north. The pilot has to aim into the wind — slightly west of north — if the intention is to track due north over the ground.

The common error is adding speeds: $200 + 50 = 250 \text{ km/h}$. That would only be correct if the plane were going downwind. The velocities are perpendicular, so they add by the Pythagorean theorem, and the result is less than the arithmetic sum.

The deeper point about frames is worth pausing on. Every velocity is a velocity *relative to some frame*. The question "how fast is the boat going?" has no answer until you specify: relative to the water, or relative to the shore? Physicists are punctilious about this because the calculation breaks if you mix frames. The two-subscript notation makes the bookkeeping honest — if both subscripts in each velocity term are labeled, you cannot accidentally mix a water-relative speed with a ground-relative speed without the algebra flagging the inconsistency. This habit, established here, will matter again in Chapter 28 when we reach special relativity, where velocity addition is more subtle and the stakes of getting frames wrong are higher.

---

## What connects the three ideas

Vectors and components. The independence of perpendicular motions. Velocity addition. These are not three separate topics assembled by convention into one chapter. They are the same idea at three levels of application.

The core claim is this: two-dimensional motion under a force that points in only one direction — gravity — separates cleanly into two one-dimensional problems along perpendicular axes. The force acts on one axis only. The other axis runs free. The two axes share time, and time is the variable that couples them. Everything else about the solution follows from this structure: resolve, solve separately, recombine if needed.

What changes as you scale the problem is not the structure but the approximations.

A coin falling off a desk: air resistance negligible, $g$ constant, dimensions measured in centimeters. The vacuum equations are exact to any precision you can measure.

A basketball shot: air resistance small, $g$ effectively constant over a few meters of arc. The vacuum equations give the right trajectory to within the ball's own diameter.

A long jump: same. Athletes peak at $42°$–$43°$ rather than $45°$ because their legs can generate more speed at shallower angles — an optimization the equations predict once you allow $v_0$ to vary with $\theta_0$.

An artillery shell: air resistance becomes significant at long range. The vacuum equations give order-of-magnitude answers; accurate fire-control tables require computer integration of equations including drag.

A ballistic missile: the curvature of the Earth matters. "Level ground" is an approximation that fails over thousands of kilometers. The same vector decomposition applies, but in a rotating coordinate system attached to a sphere.

A satellite: the projectile keeps missing the ground. That's what an orbit is — a projectile in perpetual free fall, where the ground curves away beneath it at exactly the rate the projectile falls. The kinematic structure is identical; the geometry of the falling surface is not flat.

The same five kinematic equations from Chapter 3, decomposed by the component method of this chapter, describe the coin, the cannonball, and, with appropriate coordinate systems, the satellite. From a desk corner to low Earth orbit, the language does not change. The approximations negotiated at each scale is what physics is largely about.

<!-- → [INFOGRAPHIC: vertical scale ladder from "desk (cm)" to "orbit (km)" — six rungs: coin off desk (~0.5 m fall), basketball shot (~3 m arc), long jump (~8 m horizontal), artillery shell (~10 km range), ballistic missile (~1,000 km), satellite orbit (~400 km altitude); for each rung, annotate which approximation breaks first (air, flat-Earth, constant-g, Newtonian gravity); caption: "the equations stay the same — only the fine print changes"] -->

---

## Exercises

### Warm-up

**5.1** A hiker walks $4.0 \text{ km}$ east, then $3.0 \text{ km}$ north. (a) What is her total walking distance? (b) What is her displacement (magnitude and direction from start)?

**5.2** A vector has magnitude $25.0 \text{ m}$ and points $40°$ north of east. Compute its east ($x$) and north ($y$) components.

**5.3** A vector has $A_x = -3.0 \text{ m}$ and $A_y = +4.0 \text{ m}$. What is its magnitude and direction (angle from the $+x$-axis)?

**5.4** A ball is thrown horizontally at $8.0 \text{ m/s}$ from a height of $1.5 \text{ m}$. Ignoring air resistance, how long until it hits the ground, and how far does it travel horizontally?

### Application

**5.5** A boat heads east at $6.00 \text{ m/s}$ relative to the water. The water flows north at $2.00 \text{ m/s}$. (a) What is the boat's velocity relative to the shore (magnitude and direction)? (b) If the river is $300 \text{ m}$ wide (east–west), how long does it take to cross?

**5.6** A projectile is launched at $50.0 \text{ m/s}$ at an angle of $30.0°$ above horizontal on level ground. (a) What are the components of the initial velocity? (b) What is the time of flight? (c) What is the range? (d) What is the maximum height?

**5.7** A ball is thrown horizontally from the top of a $60.0 \text{ m}$ building and lands $100 \text{ m}$ from the base. Find: (a) the time in the air, (b) the initial horizontal velocity, (c) the velocity (magnitude and direction) just before impact.

**5.8** An airplane heads due north at $200 \text{ km/h}$ relative to the air. A wind blows from the west at $50 \text{ km/h}$. What is the plane's velocity relative to the ground (magnitude and direction)?

### Synthesis

**5.9** A daredevil drives a motorcycle off a $32°$ ramp at $40.0 \text{ m/s}$. The takeoff and landing are at the same height. (a) How far does he travel horizontally? (b) If buses parked end-to-end below are $20.0 \text{ m}$ each, how many can he clear?

**5.10** The free-throw line in basketball is $4.57 \text{ m}$ from the basket; the rim is $3.05 \text{ m}$ above the floor. A player releases the ball at $2.44 \text{ m}$ above the floor with an initial speed of $8.15 \text{ m/s}$. At what release angle does the ball pass through the rim?

**5.11** Drop one coin off a desk while flicking another horizontally at $2.0 \text{ m/s}$. The desk is $0.80 \text{ m}$ tall. (a) Compute when each coin hits the floor. (b) Compute where each coin lands relative to the edge. (c) Comment on whether the two clinks should be simultaneous.

### Challenge

**5.12** A cannon fires a shell with muzzle velocity $560 \text{ m/s}$ at the maximum-range angle. (a) Compute the range, ignoring air drag and Earth's curvature. (b) Compute the peak altitude. (c) Estimate by how much the curvature of the Earth changes the answer in (a), given Earth's radius is about $6{,}370 \text{ km}$. (d) Comment qualitatively on whether air resistance makes the actual range larger or smaller than the calculated value.

**5.13** Derive the range equation $R = v_0^2 \sin(2\theta_0) / g$ from the kinematic equations. Work step by step: write the vertical equation for landing, solve for $t$, substitute into the horizontal equation. State explicitly the assumption that launch and landing are at the same height.

---

## LLM Exercise — Chapter 5: 2D Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** A 2D-motion analysis of one element of your anchor phenomenon — a curving path, an angled trajectory, a relative-velocity calculation — using vector decomposition.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste the 1-sentence description from earlier chapters].

For Chapter 5, I want to apply two-dimensional kinematics — vectors, components, projectile motion, and relative velocity — to one element of my phenomenon that involves motion in more than one direction.

Please:

1. Identify ONE 2D-motion question in my phenomenon. Examples:
   - Bike commute: what's my velocity relative to the road when there's a crosswind, and how does it change my heading?
   - Coffee maker: what is the trajectory of a drip falling from the showerhead onto the grounds, given the showerhead spacing?
   - Basketball shot: what release angle maximizes my chance of making a free throw given my release height and speed?
   - Marathon: how does a 10 km/h crosswind change effective pace if I'm running due north at 4 m/s?
   - Espresso: what arc does a stream of water make exiting the portafilter at a typical extraction velocity?

2. Set up the problem with explicit axes (x and y), state the components of every vector involved, and identify which 1D kinematic equation applies to each axis.

3. Walk through the calculation. Report the answer with proper units, sig figs, and an uncertainty estimate (using percent-addition from Chapter 1).

4. Sanity-check the result using a Fermi estimate.

5. Identify which assumption (no air drag, constant g, level launch/land, etc.) is most likely to affect this calculation, and estimate by what fraction the real answer probably differs.

6. One sentence on how this connects to Chapter 6 (Newton's laws and forces) when we meet it.

Save the output as logbook/chapter-05-two-dimensional-kinematics.md.
```

### What this produces

A fifth Logbook entry: a worked 2D motion problem applied to your anchor phenomenon, with an honest accounting of which idealizations are doing the heavy lifting.

### How to adapt this prompt

- *For phenomena that are mostly 1D* (a vertical pour, a straight-line commute on a windless day): introduce a hypothetical 2D element (what would happen with a crosswind, or with a curved component) so you still exercise the chapter's machinery.
- *For ChatGPT or Gemini:* identical, with the usual interface substitutions.
- *For Claude Code:* if you have GPS data from your bike commute, video frames of a basketball shot, or any time-series, paste it and ask Claude to fit a parabola or compute angles directly.

### Connection to previous chapters

Builds on Chapter 3's 1D kinematics by adding a perpendicular axis. The uncertainty propagation rule from Chapter 1 still applies — and in 2D problems, where you multiply trig functions by speeds and times, the percent-addition rule has more terms to track.

### Preview of next chapter

Chapter 6 introduces Newton's three laws — finally answering *why* the projectile follows the path it does. Force is a vector; force decomposition uses exactly the component machinery installed here. The Chapter 6 LLM Exercise will ask you to identify the forces at work in your phenomenon and apply $F = ma$ to compute one of them.

---

## AI Wayback Machine

**Niccolò Tartaglia** worked out projectile motion in the 1530s — the first systematic mathematical treatment of how a cannonball travels through the air. He developed the theory while consulting for Italian artillery commanders and later regretted helping make war more deadly.

**Run this:**

```
Who was Niccolò Tartaglia, and how does his projectile motion work connect to the two-dimensional kinematics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Niccolò Fontana Tartaglia"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Tartaglia's account of projectile motion — what was right, what was wrong, what Galileo later corrected.
- Ask it about Tartaglia's famous mathematical contest with Cardano over solving cubic equations.

What changes? What gets better? What gets worse?
