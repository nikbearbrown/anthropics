# Chapter 3 — Two-Dimensional Kinematics

*Why the coin that goes farther lands at the same time.*

---

There is a demonstration that physics professors love, and the reason they love it is that it keeps working even after students have been warned. You take two identical coins. You balance one on the edge of a desk. The other you place just behind it, on the desk surface, with your finger cocked. One quick flick: the first coin sails out in a horizontal arc. At the same instant — *at the same instant* — the second coin drops straight down from the edge. One travels a meter. One falls straight to the floor. They land at the same time.

Most people hear this and think: surely not. The coin that travelled farther must have been in the air longer. It covered more distance. More distance, more time. That's just obvious.

Try it. Listen for the two clinks. They are simultaneous.

![Strobed top-down view of two coins leaving a desktop: one dropped from rest, one flicked horizontally. Both fall the same vertical distance in the same time. The horizontal flick changes where the coin lands, not when.](../images/03-two-dimensional-kinematics-fig-01.png)
*Figure 3.1 — Two Coins, Same Floor Time — Horizontal and Vertical Are Independent*

What you are hearing is one of the cleanest facts in mechanics: the horizontal motion of an object does not affect its vertical fall. The coin that sailed across the room was also falling — at exactly the same rate as the coin that dropped straight down — from the moment it left the desk until the moment it hit the floor. The horizontal speed changed where it landed. It changed nothing about *when*. Gravity pulled both coins down at $g = 9.80 \text{ m/s}^2$ regardless of what either coin was doing sideways.

Galileo was the first to write this down clearly. Harold Edgerton, the MIT engineer who made strobe photography famous, made it visible. In a famous set of images from 1948, Edgerton photographed two balls falling side by side — one dropped, one thrown horizontally — with a strobe flashing every $\frac{1}{30}$ of a second. The dropped ball left a column of dots, getting farther apart as it accelerated. The thrown ball left a curve of dots. At every single flash, the two balls were at the same height. The horizontal velocities were completely different. The vertical histories were identical.

This is the central fact. Everything else in this chapter is bookkeeping.

<!-- → [IMAGE: Edgerton-style strobe photograph (or a faithful reconstruction) showing two balls falling side by side — one dropped, one thrown horizontally — with position dots at equal time intervals, demonstrating that vertical positions match at every instant] -->

---

## How a quantity gets a direction

Before we can use the independence of vertical and horizontal motion, we need a language for quantities that have direction. Velocity is not just a speed. It is a speed *and* a direction. When the flicked coin left the desk, it had some speed pointing horizontally outward. When it hit the floor, that coin had both a horizontal velocity it had maintained throughout and a downward velocity it had built up under gravity. To say where it was at any moment, you need both.

The word for a quantity that carries magnitude and direction is a *vector*. Temperature is not a vector — $20°$ is $20°$ in every direction. Velocity is a vector. So is acceleration, force, momentum, and displacement. When you say "the wind is blowing at 20 miles per hour," you have given a scalar (a speed). When you say "the wind is blowing at 20 miles per hour due west," you have given a vector.

![Top-down map. Leg 1: 3.5 km at 35° N of E. Leg 2: 2.5 km at 60° N of W. Resultant displacement found by component-wise addition: east-component 1.62 km, north-component 4.18 km, magnitude 4.48 km at 68.8° N of E.](../images/03-two-dimensional-kinematics-fig-03.png)
*Figure 3.3 — Hiker's Two-Leg Walk — Net Displacement by Component Addition*

We draw vectors as arrows. The length represents magnitude; the direction of the arrow is the direction of the vector. This is useful for sketching but useless for calculating. Arrows are hard to add on paper. What saves us is the observation that any arrow in a plane can be decomposed into two perpendicular arrows — one pointing east, one pointing north, say — and those two pieces can be added back into the original by the Pythagorean theorem.

![A vector A at angle θ above horizontal, decomposed into x and y components: A_x = A cos θ (horizontal leg), A_y = A sin θ (vertical leg). The Pythagorean check: A_x² + A_y² = A².](../images/03-two-dimensional-kinematics-fig-02.png)
*Figure 3.2 — Vector Components — A Right Triangle Resolved by Sine and Cosine*

Here is the mechanism. Suppose a vector $\mathbf{A}$ has magnitude $A$ and points at angle $\theta$ above the positive $x$-axis. Draw the right triangle that has $\mathbf{A}$ as its hypotenuse. The horizontal leg is $A_x = A\cos\theta$. The vertical leg is $A_y = A\sin\theta$. These are the **components** of $\mathbf{A}$, and the original vector is exactly recovered from them:

$$A = \sqrt{A_x^2 + A_y^2}, \qquad \theta = \tan^{-1}\!\left(\frac{A_y}{A_x}\right).$$

The power of components is in addition. If you want to add two vectors $\mathbf{A}$ and $\mathbf{B}$ that point in different directions, doing it graphically — placing arrows head to tail, measuring the result — gives you an answer good to maybe a degree or two. Doing it by components gives you the answer to whatever precision your inputs allow:

$$R_x = A_x + B_x, \qquad R_y = A_y + B_y.$$

Components along the same axis add as ordinary numbers. Then you reconstruct the resultant magnitude and direction from $R_x$ and $R_y$ using the Pythagorean theorem and arctangent. This recipe does not change. Every vector-addition problem in this book follows it.

<!-- → [INFOGRAPHIC: three-panel visual — (1) a vector arrow at angle θ with its x and y component projections labeled, (2) the same decomposition expressed as the right-triangle equation Ax = A cosθ, (3) two vectors A and B with their components summed into resultant R — to make the abstract component formulas concrete] -->

One warning about the trig. The equations $A_x = A\cos\theta$ and $A_y = A\sin\theta$ hold when $\theta$ is measured from the $x$-axis. If you measure from the $y$-axis, $\cos$ and $\sin$ swap. The safe habit: draw the right triangle, label which side is adjacent to $\theta$ and which is opposite, then reach for the trig function that matches. Never reach for a formula without drawing the triangle first.

### Adding two displacements

A hiker walks $53.0 \text{ m}$ at $20.0°$ north of east, then $34.0 \text{ m}$ at $63.0°$ north of east. Where does she end up?

Let $x$ be east, $y$ be north. Resolve each leg:

$$A_x = 53.0\cos20.0° = 49.8 \text{ m}, \qquad A_y = 53.0\sin20.0° = 18.1 \text{ m},$$
$$B_x = 34.0\cos63.0° = 15.4 \text{ m}, \qquad B_y = 34.0\sin63.0° = 30.3 \text{ m}.$$

Add:

$$R_x = 49.8 + 15.4 = 65.2 \text{ m}, \qquad R_y = 18.1 + 30.3 = 48.4 \text{ m}.$$

Reconstruct:

$$R = \sqrt{65.2^2 + 48.4^2} = \sqrt{4251 + 2343} \approx 81.2 \text{ m}, \qquad \theta = \tan^{-1}(48.4/65.2) \approx 36.6°.$$

She is $81.2 \text{ m}$ from her starting point, $36.6°$ north of east. Sanity check: she walked $87 \text{ m}$ total; the straight-line distance has to be less, and it is. The angle $36.6°$ sits between $20°$ and $63°$, pulled toward the longer first leg. Both checks pass.

The thing to notice is what the component method did. It turned a geometry problem — adding two arrows at different angles — into two arithmetic problems, each trivially easy, plus a Pythagorean reconstruction. The strategy is to make the bookkeeping so systematic that you can't get confused about directions. From here on, every two-dimensional problem will start the same way: draw the situation, choose axes, resolve everything into components, do arithmetic, reconstruct.

---

## The independence of perpendicular motions

Now we can state the central fact of this chapter properly. A projectile — an object launched into the air and left under gravity alone — obeys two sets of equations simultaneously, and the equations share only one variable.

**Horizontal.** Gravity has no horizontal component. Nothing is pushing or pulling the projectile sideways. So horizontal acceleration is zero, and horizontal velocity is constant:

$$x = x_0 + v_{0x}\,t, \qquad v_x = v_{0x} = \text{constant}.$$

**Vertical.** Gravity acts straight down at $g = 9.80 \text{ m/s}^2$. Taking up as positive, this is the same constant-acceleration kinematics from Chapter 2:

$$y = y_0 + v_{0y}\,t - \tfrac{1}{2}\,g\,t^2, \qquad v_y = v_{0y} - g\,t, \qquad v_y^2 = v_{0y}^2 - 2g(y - y_0).$$

The only variable that appears in both sets is $t$ — time. The clock ticks at the same rate for horizontal and vertical motion because it is the same clock. That is the coupling. That is also the key to solving every projectile problem: find $t$ from whichever equation gives it most directly — usually the vertical, because gravity sets the timeline — then substitute that $t$ into the horizontal equation.

Why does this work? Because a horizontal force does not make you fall faster or slower. A vertical force does not make you move sideways faster or slower. They act along perpendicular axes, and perpendicular directions are, by the geometry of flat space, genuinely independent. You can push an object eastward all day without changing how fast it falls. You can push it downward all day without changing how fast it moves east. The forces are orthogonal; their effects are orthogonal; the equations are orthogonal.

This is what Edgerton's photograph shows. The thrown ball had a large horizontal velocity. That velocity carried it sideways. It did not slow the fall. The dropped ball had no horizontal velocity. At every strobe flash, their heights matched.

<!-- → [IMAGE: sketch or reconstructed diagram of an Edgerton-style multi-exposure showing a dropped and a thrown ball side by side, with horizontal dashed lines connecting the two balls at each time step to show matched vertical positions] -->

### A fireworks shell

A fireworks shell is launched at $v_0 = 70.0 \text{ m/s}$ at $75.0°$ above horizontal. The fuse ignites at the peak. How high does it burst? When? How far downrange?

Resolve:

$$v_{0x} = 70.0\cos75.0° = 18.1 \text{ m/s}, \qquad v_{0y} = 70.0\sin75.0° = 67.6 \text{ m/s}.$$

At the peak, $v_y = 0$. From $v_y^2 = v_{0y}^2 - 2gy$:

$$y_{\text{peak}} = \frac{v_{0y}^2}{2g} = \frac{67.6^2}{2(9.80)} = \frac{4570}{19.6} \approx 233 \text{ m}.$$

Time to peak, from $v_y = v_{0y} - gt$:

$$t_{\text{peak}} = \frac{v_{0y}}{g} = \frac{67.6}{9.80} \approx 6.90 \text{ s}.$$

Horizontal distance at that time:

$$x = v_{0x}\,t = 18.1 \times 6.90 \approx 125 \text{ m}.$$

![Five projectile trajectories with the same launch speed at different angles (15°, 30°, 45°, 60°, 75°). 45° produces maximum range. Complementary pairs (15°/75°, 30°/60°) produce equal ranges but very different heights.](../images/03-two-dimensional-kinematics-fig-05.png)
*Figure 3.5 — Range vs Launch Angle — 45° Wins, Complementary Angles Tie*

The shell bursts at $233 \text{ m}$ altitude, $6.90 \text{ s}$ after launch, $125 \text{ m}$ downrange. You can sanity-check this against experience: large professional fireworks typically peak between $200$ and $400$ meters, and their flight times — easily counted between the ground-level *thump* and the burst — are typically five to ten seconds. The numbers agree with observation.

Notice what happened in the calculation. Once the initial velocity was resolved into components, the vertical and horizontal calculations never spoke to each other. The vertical equation produced a time. That time was handed to the horizontal equation. That is the entire algorithm. You will use it dozens of times.

The idealization here is that there is no air resistance. This is fine for the purposes of learning the kinematics, and it is surprisingly good for short, dense projectiles (a thrown rock, a basketball over a rim). It is poor for anything light enough or slow enough that drag significantly changes the trajectory — a badminton shuttlecock, a ping-pong ball, an arrow at long range, a large artillery shell on a long arc. In those cases, numerical simulation is needed. The clean equations you are learning now are the foundation; knowing when they fail is part of knowing them well.

<!-- → [CHART: parabolic trajectory for the fireworks shell example — x-axis horizontal distance (0–250 m), y-axis altitude (0–250 m), curve from launch at 75° through peak at (125 m, 233 m) to implied landing beyond; annotate the peak coordinates, launch angle, and component velocity vectors at launch (v_x = 18.1 m/s horizontal, v_y = 67.6 m/s vertical) and at the peak (v_x = 18.1 m/s horizontal, v_y = 0) — student should see that the horizontal component is unchanged at the peak] -->

---

## Motion relative to motion

There is a third idea in this chapter, and it uses the same vector machinery.

A canoe on a river. You point the bow directly across the water and paddle steadily. You expect to arrive at the far bank directly opposite your launch point. Instead, you arrive downstream. The current was carrying you the whole time you were paddling. Your velocity *through the water* pointed across. The water's velocity *over the ground* pointed downstream. Your velocity *over the ground* — which is what actually determines where you end up — was the vector sum of both.

This sounds simple, but it trips people up because everyday language does not flag which frame a velocity is measured in. "How fast is the boat going?" relative to *what*? The water, which is carrying it? The shore, which is standing still? A fish swimming alongside? The answer to each question is a different number, and conflating them is the source of every relative-velocity error.

The fix is a bookkeeping rule. Write every velocity with two subscripts: the object (O), the medium it moves through (M), and the ground frame (G). The rule is:

$$\mathbf{v}_{\text{O,G}} = \mathbf{v}_{\text{O,M}} + \mathbf{v}_{\text{M,G}}.$$

The object's velocity relative to the ground equals its velocity relative to the medium, plus the medium's velocity relative to the ground. The subscripts cancel diagonally — O,M then M,G leaves O,G — which is a useful check that you've combined the right vectors. The addition itself is the same component recipe as before.

### A boat in a current

![Top-down view: a boat heads straight across a river at 4 m/s relative to water. The river flows downstream at 3 m/s. The boat's velocity relative to ground is the vector sum: 5 m/s at 36.9° downstream of straight-across.](../images/03-two-dimensional-kinematics-fig-06.png)
*Figure 3.6 — Relative Velocity — Boat Across a Flowing River*

The bow points due north (across the river). Speed relative to the water: $0.750 \text{ m/s}$ north. The river flows east at $1.20 \text{ m/s}$. What is the boat's velocity relative to shore?

Let $x$ be east, $y$ be north.

Boat relative to water: $v_x = 0$, $v_y = 0.750 \text{ m/s}$.
Water relative to shore: $v_x = 1.20 \text{ m/s}$, $v_y = 0$.

Add:

$$v_{\text{tot},x} = 1.20 \text{ m/s}, \qquad v_{\text{tot},y} = 0.750 \text{ m/s}.$$

Reconstruct:

$$v = \sqrt{1.20^2 + 0.750^2} = \sqrt{1.44 + 0.5625} \approx 1.42 \text{ m/s}, \qquad \theta = \tan^{-1}(0.750/1.20) \approx 32.0°.$$

The boat moves at $1.42 \text{ m/s}$ at $32°$ east of north — meaning it is heading mostly downstream rather than straight across. Sanity check: the river flows faster than the boat can paddle ($1.20 > 0.750$), so the boat should drift more downstream than sideways. A $32°$ angle from north — which is $58°$ from east — confirms the downstream component dominates. The answer is in the right direction.

The common error here is adding speeds: $1.20 + 0.750 = 1.95 \text{ m/s}$. This would be correct only if both velocities pointed in the same direction. They are perpendicular; their sum is found by the Pythagorean theorem, not by addition. The numbers obey the geometry of the situation, not the convenience of having only one number to add.

<!-- → [INFOGRAPHIC: vector diagram for the boat-in-current problem — showing v(boat/water) pointing north, v(water/shore) pointing east, and the resultant v(boat/shore) as the diagonal, with magnitude 1.42 m/s and angle 32° labeled — to make the vector addition rule geometrically concrete] -->

The same machinery scales to airplanes and crosswinds, to swimmers in tidal currents, to satellites released from moving spacecraft. The only difference is which direction the medium is moving and how much faster than the object it is. The subscript rule forces you to be honest about the framing, and the component arithmetic gives you the answer.

---

## The three ideas as one idea

Step back. You have three concepts from this chapter: vectors and their components; the independence of perpendicular motions; the addition of velocities in different frames. They are not three separate tools. They are one tool seen from three different angles.

The tool is this: motion in two dimensions is just two one-dimensional motions happening simultaneously, coupled only through time. Split any 2D motion into components. Each component obeys ordinary 1D kinematics. Find $t$ from one direction and use it in the other. Add vectors by components, not by magnitudes. Keep track of which frame you're in.

This is why the coin demonstration works. The coin that flies across the room has a nonzero $v_x$. The coin that drops has $v_x = 0$. But both have $v_{y,0} = 0$ at the moment they leave the desk, and both accelerate vertically at the same rate. Their vertical histories are identical. The horizontal histories are unrelated. The clinks are simultaneous.

<!-- → [INFOGRAPHIC: side-by-side comparison of the two-coin demonstration with labels — dropped coin shows only y-axis fall, flicked coin shows x-axis travel with identical y-axis fall, with matching vertical positions marked at equal time intervals to reinforce the independence of axes] -->

![Parabolic trajectory of a fireworks shell. v₀ = 70 m/s at 75°. v₀x = 18.1 m/s, v₀y = 67.6 m/s. Apex height ~233 m at t = 6.9 s; range ~250 m at t = 13.8 s. Velocity vectors decomposed at three points.](../images/03-two-dimensional-kinematics-fig-04.png)
*Figure 3.4 — Fireworks Shell — Launched at 70 m/s, 75° Above Horizontal*

![Three scales: tossed pencil (cm, milliseconds), thrown rock (meters, seconds), satellite orbit (kilometers, hours). The same component decomposition and kinematic equations describe all three.](../images/03-two-dimensional-kinematics-fig-07.png)
*Figure 3.7 — Same 2D Equations at Wildly Different Scales*

This framework scales farther than you might expect. A long jumper leaves the ground at some angle and speed; their horizontal distance is governed by the same equations as the fireworks shell, with $g = 9.80 \text{ m/s}^2$ and a few meters of height change. An artillery shell follows a parabolic arc over a few kilometers — same equations, and the approximations hold well. A cannonball fired fast enough to follow the curvature of the Earth doesn't come down at all: it is in orbit. That is what orbit is — a projectile falling so fast that the ground curves away beneath it as fast as it falls. The equations of this chapter do not describe that regime (you would need to account for varying $g$ and the curved geometry of the Earth's surface), but the spirit is identical. Every projectile, at every scale, is a two-component kinematics problem. The only question is which idealizations hold.

---

## Exercises

### Warm-up

**3.1** *(LO 1)* A vector has magnitude $25.0 \text{ m}$ and points $40.0°$ north of east. Compute its east ($x$) and north ($y$) components. Then verify your answer by reconstructing the magnitude and angle from the components.

**3.2** *(LO 1)* A vector has components $A_x = -3.0 \text{ m}$ and $A_y = +4.0 \text{ m}$. What is its magnitude and direction? Draw a sketch before computing — which quadrant should the angle land in?

**3.3** *(LO 3)* A ball is thrown horizontally at $8.0 \text{ m/s}$ from a height of $1.5 \text{ m}$. Without writing a single equation yet, estimate: roughly how long until it hits the ground, and roughly how far horizontally? Then compute both values exactly.

**3.4** *(LO 5)* A boat heads due east at $6.00 \text{ m/s}$ relative to the water. The water flows due north at $2.00 \text{ m/s}$. What is the boat's speed and direction relative to the shore?

### Application

**3.5** *(LO 2)* A hiker walks $4.0 \text{ km}$ east, then $3.0 \text{ km}$ north. (a) What total distance did she walk? (b) What is her displacement — magnitude and direction — from start to finish? (c) Why are the two answers different?

**3.6** *(LO 4)* A projectile is launched at $50.0 \text{ m/s}$ at $30.0°$ above horizontal on level ground. Find: (a) the components of the initial velocity; (b) the time of flight; (c) the range; (d) the maximum height.

**3.7** *(LO 4)* A ball is thrown horizontally from the top of a $60.0 \text{ m}$ building and lands $100 \text{ m}$ from the base. Find: (a) the time in the air; (b) the initial horizontal speed; (c) the velocity — magnitude and direction — just before impact.

**3.8** *(LO 5)* An airplane heads due north at $200 \text{ km/h}$ relative to the air. A wind blows from the west at $50.0 \text{ km/h}$. What is the plane's velocity relative to the ground? If the pilot wants to travel due north over the ground, in which direction should she point the nose, and what will her ground speed be?

### Synthesis

**3.9** *(LO 1, 2, 4)* A motorcycle leaves a $32°$ ramp at $40.0 \text{ m/s}$. The takeoff and landing are at the same height. (a) What is the range? (b) What is the peak height? (c) If buses $20.0 \text{ m}$ long are parked end-to-end below the jump, how many can the rider clear?

**3.10** *(LO 3, 4)* Return to the coin demonstration from the chapter opening. The desk is $0.80 \text{ m}$ tall. One coin is flicked horizontally at $2.0 \text{ m/s}$; the other drops straight down. (a) Compute when each coin hits the floor. (b) Compute where each lands relative to the desk edge. (c) Show numerically that the landing times are identical, and explain physically why this had to be true.

**3.11** *(LO 4, 5)* A river is $300 \text{ m}$ wide. A canoe can maintain $0.750 \text{ m/s}$ relative to the water; the river flows at $1.20 \text{ m/s}$ downstream. (a) If the paddler aims straight across (perpendicular to the bank), how far downstream does she land, and how long does the crossing take? (b) At what angle upstream should she aim the bow to land directly across? (c) At that angle, how long does the crossing take? (d) Which crossing strategy takes less time — straight across or aimed to land directly opposite?

### Challenge

**3.12** *(LO 4, beyond chapter)* A cannon fires a shell with muzzle velocity $560 \text{ m/s}$ at the maximum-range angle. (a) Compute the range, ignoring air drag and Earth's curvature. (b) Compute the peak altitude. (c) Look up Earth's radius and estimate by how much the curvature changes the answer in (a). (d) Comment qualitatively on whether air resistance makes the actual range larger or smaller than the vacuum calculation.

**3.13** *(LO 3, 4, beyond chapter)* Derive the range equation $R = v_0^2 \sin(2\theta_0)/g$ from the kinematic equations. Show every step: write the vertical equation for landing, solve for total flight time $t$, substitute into the horizontal equation. State explicitly which physical assumption about the launch and landing height makes the derivation clean. Then use the result to find the two launch angles that give the same range for a given $v_0$ — and explain physically why they exist.

---



By the end of this chapter you should be able to:

1. Resolve a two-dimensional vector into perpendicular components using $A_x = A\cos\theta$ and $A_y = A\sin\theta$, and reconstruct a vector from its components using the Pythagorean theorem.
2. Add vectors analytically by summing components axis by axis, then reconstructing the resultant.
3. Apply the independence of horizontal and vertical motion to set up projectile problems: resolve initial velocity, write separate 1D equations for each axis, use time as the coupling variable.
4. Solve full projectile problems for range, peak height, flight time, and impact velocity at any launch angle.
5. Add velocities using vector components to handle relative motion — a boat in a current, a plane in a crosswind.

**Prerequisites.** Chapter 1 (units, sig figs, uncertainty). Chapter 2 (kinematic equations in 1D, free fall). Right-triangle trigonometry ($\sin$, $\cos$, $\tan$, $\tan^{-1}$, Pythagorean theorem).

**Why this chapter matters.** Real motion is not a straight line. Projectiles arc; boats drift; planes are blown off course. Every later chapter involving motion in more than one dimension — circular motion, orbits, magnetic forces on moving charges — uses the vector decomposition installed here. If Chapter 2 was kinematics in one direction, this chapter is kinematics in the world as it actually is.

---

## ↳ Dig Deeper — Why the component decomposition is unique

*The chapter asserts that any 2D vector splits into perpendicular components in exactly one way, once the axes are fixed. This is not obvious, and the argument has consequences for everything from force decomposition on inclined planes to electric field calculations.*

**Prompt:**
> Explain why the decomposition of a 2D vector into perpendicular components along a chosen pair of axes is unique. What changes if the axes are not perpendicular (oblique components)? Walk through one worked example showing a vector decomposed along non-perpendicular axes, and explain why the formulas $A_x = A\cos\theta$, $A_y = A\sin\theta$ no longer apply. End with one sentence on why physicists almost always choose perpendicular axes.

**What to do with the output:** Save it. The same uniqueness argument appears when decomposing forces on inclined planes (Chapter 5) and fields along arbitrary axes (Chapter 18).

---

## ↳ Dig Deeper — The range equation and why 45° wins

*From the kinematic equations you can derive a closed-form expression for projectile range on level ground: $R = v_0^2 \sin(2\theta_0)/g$. The result is famous; the derivation is short; the claim that $45°$ maximizes range deserves a careful look at when it actually holds.*

**Prompt:**
> Derive the range equation $R = v_0^2\sin(2\theta_0)/g$ from the kinematic equations for level-ground launch and landing. Then explain (a) why $\theta_0 = 45°$ maximizes range, (b) why the optimal angle drops to about $38°$ when air resistance is included, and (c) why a shot-putter releasing from above ground level optimizes below $45°$ even with no air. End with one sentence on which athletic events the $45°$ result actually predicts well.

**What to do with the output:** Save it. The pattern — clean theory, modified by realistic conditions — recurs whenever physics meets engineering. The same shape of correction appears in aerospace launch-angle optimization.

---

## ↳ Dig Deeper — Galilean relativity and the limits of velocity addition

*The velocity-addition rule in this chapter is exact at everyday speeds. At speeds approaching the speed of light, it fails, and the correct rule from special relativity is one of the foundations of modern physics.*

**Prompt:**
> Explain the classical (Galilean) velocity addition rule used in this chapter, then state the relativistic formula: $u' = (u + v)/(1 + uv/c^2)$. Compute one example: an object moving at $0.5c$ relative to a frame that moves at $0.5c$ relative to a third frame. The classical rule gives $1.0c$; what does the relativistic rule give, and why does the difference matter? End with one sentence on at what speeds the classical rule starts to fail measurably.

**What to do with the output:** Save it. Special relativity (Chapter 28) revisits this in depth. Velocity addition is one of the cleanest places to feel the difference between classical and relativistic kinematics.

---

## LLM Exercise — Chapter 3: 2D Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A 2D-motion analysis of one element of your anchor phenomenon — a curving path, an angled trajectory, a relative-velocity calculation — using vector decomposition.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste the 1-sentence description from earlier chapters].

For Chapter 3, I want to apply two-dimensional kinematics — vectors, components, projectile motion, and relative velocity — to one element of my phenomenon that involves motion in more than one direction.

Please:

1. Identify ONE 2D-motion question in my phenomenon. Examples:
   - Bike commute: what's my velocity relative to the road when there's a crosswind, and how does it change my heading?
   - Coffee maker: what is the trajectory of a drip falling from the showerhead onto the grounds?
   - Basketball shot: what release angle maximizes my chance of making a free throw given my release height and speed?
   - Marathon: how does a 10 km/h crosswind change effective pace if I'm running due north at 4 m/s?

2. Set up the problem with explicit axes (x and y), state the components of every vector involved, and identify which 1D kinematic equation applies to each axis.

3. Walk through the calculation. Report the answer with proper units, sig figs, and an uncertainty estimate using percent-addition from Chapter 1.

4. Sanity-check the result using a Fermi estimate.

5. Identify which assumption (no air drag, constant g, level launch/land) is most likely to affect this calculation, and estimate by what fraction the real answer probably differs.

6. One sentence on how this connects to Chapter 4 (forces).

Save the output as logbook/chapter-03-two-dimensional-kinematics.md.
```

### What this produces

A third Logbook entry: a worked 2D motion problem applied to your anchor phenomenon, with explicit accounting of which idealizations are carrying the load.

### How to adapt this prompt

- *For phenomena that are mostly 1D:* introduce a hypothetical 2D element (a crosswind, a curved component) so you exercise the chapter's machinery even if the real phenomenon is mostly straight.
- *For ChatGPT or Gemini:* identical, with the usual interface substitutions.
- *For Claude Code:* if you have GPS data, video frames, or any time-series involving 2D motion, paste it and ask Claude to fit a parabola or compute angles directly.

### Connection to previous chapters

Builds directly on Chapter 2's 1D kinematics — a second axis is added, and the two axes are coupled through time. The uncertainty propagation rule from Chapter 1 still applies; in 2D problems with multiple trig steps, the percent-addition rule accumulates more terms.

### Preview of next chapter

Chapter 4 introduces Newton's laws — finally answering *why* the projectile follows the arc it does. The Chapter 4 LLM Exercise will identify the forces in your phenomenon and apply $F = ma$ to compute one of them.

---

## What would change my mind

The chapter argues that the no-air-resistance treatment captures the essential kinematics for short, dense projectiles, with caveats for lighter or faster objects. The argument would need revision if students systematically developed incorrect intuitions from the vacuum model that caused predictable errors in later work — in standard practice, the caveats taught alongside the equations prevent this.

## Still puzzling

The deepest question this chapter raises and does not resolve: **why is space Euclidean enough, at human scales, for vector decomposition to work?** Perpendicular directions are independent because flat space allows them to be. In curved spacetime — near a black hole, on the surface of a neutron star — this stops being exactly true. We will not encounter that until Chapter 33. Until then, the flatness is a gift we are not yet required to explain.

---

## AI Wayback Machine

**Niccolò Tartaglia** worked out projectile motion in the 1530s — the first systematic mathematical treatment of how a cannonball travels through the air. He developed the theory while consulting for Italian artillery commanders, and later regretted helping make war more deadly.

**Run this:**

```
Who was Niccolò Tartaglia, and how does his projectile motion work connect to the two-dimensional kinematics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Niccolò Fontana Tartaglia"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Tartaglia's account of projectile motion — what was right, what was wrong, what Galileo later corrected.
- Ask it about Tartaglia's famous mathematical contest with Cardano over solving cubic equations.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 4 introduces Newton's laws of motion — finally telling you *why* objects accelerate as they do. Force is a vector; decomposing forces on inclined planes uses exactly the component machinery from this chapter. Chapter 5 takes that into surfaces and friction. Chapter 6 curls projectile motion into a circle: uniform circular motion is what happens when a projectile falls toward a center at constant speed. Chapter 8 applies vector addition to collisions in two dimensions. Chapter 22 uses it for magnetic forces on moving charges. Vectors are the spine of the rest of the book.

---

**Tags:** vectors, projectile-motion, components, relative-velocity, independence-of-axes
