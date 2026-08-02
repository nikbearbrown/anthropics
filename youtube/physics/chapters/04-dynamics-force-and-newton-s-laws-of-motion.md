# Chapter 4 — Dynamics: Force and Newton's Laws of Motion

*Three sentences that explain nearly everything.*

---

In 1687, Isaac Newton published a book in Latin — *Philosophiæ Naturalis Principia Mathematica* — and in it, buried among the geometry and the propositions, were three sentences. Three sentences about force and motion. They are, by any reasonable measure, the most consequential sentences in the history of science.

Not because they are complicated. Because they are simple, and because they are *right*, and because being right at that level of simplicity means they describe everything from a rolling marble to a falling moon to a rocket in vacuum to a car on a wet road to a swimmer pushing off a wall. The same three sentences, applied to every case. No exceptions in the everyday world — which is to say, in every world humans have built, navigated, or engineered since.

This chapter installs the three sentences. More importantly, it installs the habit of mind that goes with them: identifying forces clearly, summing them correctly, and reading off motion from the result.

---

## Before Newton: what everyone believed

Aristotle, around 350 BC, had a theory. Things at rest stay at rest because rest is natural. Things in motion slow down because slowing down is natural — things want to come to rest. To keep something moving, you have to keep pushing it.

This matched everyday experience. Push a box across a floor and it stops. Roll a ball down the hallway and it slows. The theory held for two thousand years because it agreed with everything anyone casually observed.

It was wrong.

![Three trials of a book sliding on increasingly slippery surfaces — rough table, polished glass, ice. Distance traveled grows. Galileo's leap: in the limit of zero friction, the book never stops. That's the first law.](../images/04-dynamics-force-and-newton-s-laws-of-motion-fig-02.png)
*Figure 4.2 — Galileo's Extrapolation — As Friction Falls, Inertia Reveals Itself*

Galileo was the first to see why. He noticed that a box slides further on a polished floor than on a rough one. Further still on glass. And if you kept smoothing the surface, the box would slide further and further until, extrapolating to a perfectly smooth surface, it wouldn't stop at all. The slowing wasn't what the *box* wanted to do. The slowing was what the *floor* did to the box. Remove the floor's roughness and you remove the slowing.

Newton took this insight and wrote it down precisely.

<!-- → [INFOGRAPHIC: Timeline from Aristotle (~350 BC) through Galileo (~1600) to Newton (1687). Key claim at each node: Aristotle — "motion requires sustained cause"; Galileo — "friction causes slowing, not natural tendency to stop"; Newton — "constant velocity is the natural state." Caption: Two thousand years separated the wrong theory from the right one. The gap wasn't lack of intelligence — it was lack of friction-free experiments.] -->

---

## The first law: the natural state is motion, not rest

A body at rest remains at rest. A body in motion remains in motion at constant velocity. *Unless acted upon by a net external force.*

This is Newton's first law, and it directly contradicts Aristotle. The natural state is *constant velocity* — which includes zero velocity as a special case. Rest is not privileged. An object moving at $10 \text{ m/s}$ to the right in the absence of all forces will continue at $10 \text{ m/s}$ to the right indefinitely. Not because something is pushing it. Because *nothing is stopping it*.

Two phrases in the law need precision. *External* means the force comes from outside the system you're analyzing. If you punch yourself in the arm, your fist pushes your arm and your arm pushes your fist — those are internal forces, and they don't change where you as a whole are going. *Net* means the vector sum of all external forces. Two forces equal in magnitude and opposite in direction sum to zero. The object doesn't change its velocity even though forces are acting. The net is what matters.

This is where Aristotle's everyday experiments were missing forces. The box sliding to a stop on the floor was not slowing because motion requires a cause. It was slowing because friction — an external force — was continuously acting against it. When you stopped pushing, the forward force went to zero, but friction didn't. The net force was now backward, and the box decelerated. Once you count *all* the forces, the first law holds perfectly.

The property of matter that this law is really about has a name: **inertia**. Inertia is resistance to changes in velocity. A heavy object is harder to start and harder to stop than a light one — not because it wants to stay put, but because it has more inertia. The quantitative measure of inertia is mass, in kilograms. We'll meet mass again in a moment.

<!-- → [FIGURE: Two panels. Left: box on rough floor, friction arrow opposing motion, object decelerates and stops. Right: same box on frictionless surface, no friction arrow, object continues at constant velocity. Caption: The box doesn't stop because motion ends naturally. It stops because friction acts. Remove friction and the first law prevails.] -->

A satellite in orbit is the cleanest large-scale demonstration. Once the engines cut out, there is no forward thrust. The satellite continues moving — not because something is pushing it, but because nothing is stopping it. (Gravity is continuously changing its *direction*, which is what keeps it in orbit rather than flying off in a straight line — that's Chapter 6. But nothing is maintaining its *speed*.)

<!-- → [FIGURE: Overhead view of satellite orbit. Tangent arrow showing "direction satellite would travel without gravity." Curved arrow showing actual orbit. Caption: The satellite's speed is maintained by inertia — the first law. Gravity changes the direction, not the speed. Both effects together produce the orbit.] -->

---

## The second law: $F = ma$

The first law tells you what happens when there's no net force. The second law tells you what happens when there is.

$$\mathbf{F}_{\text{net}} = m \mathbf{a}.$$

Three symbols. The **net force** on the left is the vector sum of all external forces on the system, in newtons. The **mass** $m$ is the system's inertia, in kilograms — a scalar, always positive. The **acceleration** $\mathbf{a}$ on the right is the resulting change in velocity, in $\text{m/s}^2$, pointing in the same direction as the net force.

What the equation says: if you push something, it accelerates in the direction you push, by an amount proportional to your push and inversely proportional to how much mass there is. Push harder: bigger acceleration. More mass: smaller acceleration. The proportionality is exact.

In components along chosen axes:

$$F_{\text{net},x} = m a_x, \qquad F_{\text{net},y} = m a_y.$$

This is what makes Chapter 3's vector work so important. Every two-dimensional force problem decomposes into two independent one-dimensional second-law problems.

### Mass and weight are not the same thing

Near Earth's surface, gravity pulls every object downward with a force proportional to its mass:

$$\mathbf{W} = m \mathbf{g},$$

where $g \approx 9.80 \text{ m/s}^2$ downward. This force $\mathbf{W}$ is the **weight**. It is measured in newtons. It is not the same as mass.

Mass is what the object *is* — a property of the matter, fixed regardless of location, measured in kilograms. Weight is what gravity *does* to that mass in a particular place — a force, measured in newtons. A $5 \text{ kg}$ object has a weight of $5 \times 9.80 = 49 \text{ N}$ on Earth and $5 \times 1.62 = 8.1 \text{ N}$ on the Moon. Same mass. Different weight. The factor of $g$ converts between them.

The confusion between mass and weight runs deep — even NASA engineers say "how much does the probe weigh" when they mean mass. In physics, the distinction is not cosmetic. Use the wrong one and your calculation is off by a factor of $g$.

<!-- → [TABLE: Mass vs. Weight comparison. Columns: property, mass, weight. Rows: what it measures, SI unit, depends on location, formula, numerical example (5 kg object on Earth vs. Moon). Caption: Mass is a property of matter. Weight is a force that gravity exerts on that mass. They are related by W = mg but are not the same thing.] -->

### Free-body diagrams: the bookkeeping

Before you write $\mathbf{F}_{\text{net}} = m\mathbf{a}$ for any specific problem, draw a **free-body diagram**. Reduce the object to a point. Draw an arrow for every external force on it — and only external forces. Label each one. Choose axes. Sum forces along each axis. Then apply the second law.

This is the algorithm. The hard part is identifying all the forces. The most common errors are omitting a real force (forgetting the normal force from the floor; forgetting the tension in a rope) or inventing an imaginary one ("the force of motion" does not exist; neither does "centrifugal force" — that's Chapter 6). Free-body diagrams enforce discipline.

<!-- → [FIGURE: Free-body diagram of a box being pushed horizontally across a floor. Forces shown: applied push (right), friction (left), weight (down), normal force (up). Each arrow labeled. Caption: Every external force gets an arrow. Only external forces. The diagram makes the second-law calculation mechanical.] -->

### A worked example

You push a stalled $1{,}500 \text{ kg}$ car along a flat road with $400 \text{ N}$ of horizontal force. Rolling friction opposes the motion at $200 \text{ N}$.

![A stalled car being pushed. Four forces drawn from the car's center: applied push F_app (forward), friction f_friction (backward), normal N (up), weight W (down). Vertical pair cancels; horizontal net = 200 N forward.](../images/04-dynamics-force-and-newton-s-laws-of-motion-fig-03.png)
*Figure 4.3 — Stalled Car — Free-Body Diagram with Four Forces*

Free-body diagram: applied push ($+400 \text{ N}$, horizontal forward), friction ($-200 \text{ N}$, horizontal backward), weight ($1{,}500 \times 9.80 = 14{,}700 \text{ N}$ down), normal force ($14{,}700 \text{ N}$ up).

Vertical axis: $N - W = 14{,}700 - 14{,}700 = 0$. Car is not accelerating into or out of the road. Good — if this weren't zero, something would be wrong.

Horizontal axis: $F_{\text{net},x} = 400 - 200 = 200 \text{ N}$.

$$a = \frac{F_{\text{net}}}{m} = \frac{200}{1{,}500} \approx 0.13 \text{ m/s}^2.$$

Four hundred newtons is roughly 90 pounds of force — a hard but plausible human push. An acceleration of $0.13 \text{ m/s}^2$ means the car gains about $1.3 \text{ m/s}$ of speed in ten seconds. That matches what happens when you shove a stalled car on a flat road.

Notice the vertical-axis check. You could say "obviously the car doesn't accelerate vertically." But working it explicitly tells you the normal force ($14{,}700 \text{ N}$), which you'll need when friction is a function of $N$ (Chapter 5). The "trivial" check is not trivial.

<!-- → [FIGURE: Free-body diagram of the stalled car example. Object shown as rectangle. Four arrows: F_push (right, 400 N), f_friction (left, 200 N), W (down, 14700 N), N (up, 14700 N). Coordinate axes shown. Net horizontal force = 200 N labeled separately. Caption: The vertical forces cancel; the horizontal forces do not. The net is what produces the acceleration.] -->

---

## The third law: you can't push without being pushed

A swimmer at the wall pushes her feet against the tile — and shoots forward into the pool. Her muscles exerted force on the wall. What exerted force on *her*?

The wall did. When her feet pressed against the wall, the wall pressed back against her feet, with exactly the same magnitude of force, in exactly the opposite direction. That's the force that accelerated her into the water. Without the wall pushing back, there would be nothing to push off against.

Newton's third law: *whenever one body exerts a force on a second body, the second body exerts a force on the first that is equal in magnitude and opposite in direction.*

If A exerts force $\mathbf{F}$ on B, then B exerts force $-\mathbf{F}$ on A. Same magnitude. Opposite direction. Always. No exceptions.

The critical word is *on a different object*. The force pair always acts on two different objects. This is why the forces in a third-law pair never cancel in a free-body diagram: you draw the free-body diagram for one object, and only one force from each pair appears on it.

### Why things accelerate despite equal and opposite forces

This is the misconception that needs to die early. "If every action has an equal and opposite reaction, doesn't everything cancel out and nothing moves?"

No — because the two forces act on different objects. The swimmer's feet push the wall with $500 \text{ N}$; the wall pushes the swimmer with $500 \text{ N}$. The $500 \text{ N}$ on the wall would accelerate the wall — but the wall is part of the pool, which is part of the Earth, whose total mass is $6 \times 10^{24} \text{ kg}$, giving it an acceleration of $\sim 10^{-22} \text{ m/s}^2$. Effectively zero. The $500 \text{ N}$ on the swimmer accelerates her — and her mass is $60 \text{ kg}$, giving an acceleration of roughly $8 \text{ m/s}^2$. Same force pair. Same force magnitude. Wildly different accelerations, because the masses are wildly different.

![Stylized high-speed snapshot of a baseball bat shattering at the moment of contact with a ball. Force pair: bat pushes ball (F_bat→ball) right; ball pushes bat (F_ball→bat) left. Equal magnitudes, opposite directions,...](../images/04-dynamics-force-and-newton-s-laws-of-motion-fig-01.png)
*Figure 4.1 — Rivera's Cutter — Bat-Ball Contact, Equal and Opposite Forces*

The bat shattering on a Mariano Rivera cutter is the same story. During contact, the bat applies a force to the ball and the ball applies an equal and opposite force to the bat. A Rivera cutter contacts the bat a few inches from the handle — off the sweet spot, close to the grip, where the geometry concentrates the ball's reaction force into a small cross-section of wood. The wood couldn't transmit that force without failing. The bat broke not because the hitter swung too hard, but because the ball pushed back with precisely the force the bat applied, in the wrong place along the lever.

<!-- → [FIGURE: Two-object diagram showing swimmer and wall. Arrow from swimmer's feet to wall labeled "swimmer pushes wall." Arrow from wall to swimmer labeled "wall pushes swimmer." Both arrows same length, opposite direction. Caption: Third-law force pairs always act on different objects. The swimmer's acceleration comes from the wall's push on her, not from her own push on the wall.] -->

<!-- → [FIGURE: Bat-ball contact diagram. Two separate free-body diagrams side by side: one for the ball (single arrow: bat pushes ball, forward), one for the bat (single arrow: ball pushes bat, backward). Both arrows labeled with same magnitude F. Caption: Each object gets its own free-body diagram. The third-law partner forces appear on different diagrams — never on the same one.] -->

### Identifying pairs

The method for spotting a third-law pair: reverse the subject and object. "The Earth pulls the Moon" → "the Moon pulls the Earth." Both true, same magnitude, opposite direction: a pair. "The table pushes up on the book" → "the book pushes down on the table." Pair.

![Book resting on a table. The book experiences gravity (W_Earth→book down) and normal force (N_table→book up); they cancel because the book is in equilibrium. The third-law partners live on different objects: book pulls Earth...](../images/04-dynamics-force-and-newton-s-laws-of-motion-fig-04.png)
*Figure 4.4 — Book on Table — Four Forces, Two Third-Law Pairs (Not the Same as Equilibrium)*

What is *not* a pair: gravity (Earth on book) and normal force (table on book). Both forces act on the book — so they can appear on the same free-body diagram, and they do happen to cancel there when the book is in equilibrium. But they are not each other's third-law partners. The partner of "gravity Earth-on-book" is "gravity book-on-Earth." The partner of "normal table-on-book" is "normal book-on-table." Different pairings entirely.

<!-- → [TABLE: Third-law pair identification. Four rows: (1) Earth pulls person down — person pulls Earth up. (2) Bat pushes ball forward — ball pushes bat backward. (3) Tire pushes road backward — road pushes tire forward. (4) Gravity Earth-on-book (NOT paired with normal force table-on-book). Caption: Each pair involves the same interaction viewed from two ends. Both forces belong to different objects, always.] -->

---

## What the three laws actually say, together

Step back. The three laws form a single machinery.

**First:** constant velocity is the natural state. Change requires a net external force.

**Second:** net external force equals mass times acceleration. $\mathbf{F}_{\text{net}} = m\mathbf{a}$. Once you have the forces, you have the motion.

**Third:** every force is half of a pair. When you write down a force on your object, the partner force exists on something else.

The laws don't tell you where forces come from. For that, you need force laws — gravity (Chapter 6), friction (Chapter 5), springs, electric fields, and ultimately the four fundamental forces of nature. What Newton's laws do is tell you what to *do* with a force once you have one: sum all the external ones on your object, divide by mass, get acceleration. Then use Chapter 2's kinematics to go from acceleration to velocity to position.

That's the complete algorithm for classical mechanics. Identify the object. Draw the free-body diagram. Sum the forces. Divide by mass. Integrate kinematically. Repeat.

<!-- → [INFOGRAPHIC: Flowchart of the Newton's-laws algorithm. Boxes in sequence: "Identify the system" → "Draw free-body diagram (external forces only)" → "Choose coordinate axes" → "Sum forces along each axis" → "Apply F_net = ma along each axis" → "Solve for unknown" → "Use kinematics (Ch. 2) to get position and velocity." Caption: Every Newton's-laws problem in the next ten chapters follows this algorithm. The steps don't change; only the force law filling in F changes.] -->

### A worked example using all three laws

Two tugboats push a $5.0 \times 10^6 \text{ kg}$ barge. Tugboat 1 applies $2.7 \times 10^5 \text{ N}$ in the $+x$ direction. Tugboat 2 applies $3.6 \times 10^5 \text{ N}$ in the $+y$ direction. The barge accelerates at $7.5 \times 10^{-2} \text{ m/s}^2$ in the direction of the combined push. Find the drag force from the water.

**First law framing.** The barge is accelerating, so the net force is not zero. Drag is opposing the motion, reducing the net force below the applied. We need to find how much.

**Second law calculation.** Combined tugboat force:

$$F_{\text{app}} = \sqrt{(2.7 \times 10^5)^2 + (3.6 \times 10^5)^2} = 4.5 \times 10^5 \text{ N.}$$

Required net force for the observed acceleration:

$$F_{\text{net}} = ma = (5.0 \times 10^6)(7.5 \times 10^{-2}) = 3.75 \times 10^5 \text{ N.}$$

Drag is the difference:

$$F_{\text{drag}} = 4.5 \times 10^5 - 3.75 \times 10^5 = 7.5 \times 10^4 \text{ N.}$$

**Third law interpretation.** The drag force on the barge is the water's reaction to the barge being pushed through it. The barge pushes water aside (action); the water pushes back on the barge (reaction). Drag is one end of that pair.

**Sanity check.** Drag is about $17\%$ of the applied force — plausible for a slow-moving flat-bottomed barge in water. The acceleration ($7.5 \text{ cm/s}^2$) is low, as expected for a multi-million kilogram vessel.

<!-- → [FIGURE: Top-down diagram of barge with two tugboat force vectors: F1 pointing right (+x, 2.7×10⁵ N), F2 pointing up (+y, 3.6×10⁵ N). Resultant vector F_app shown at 53° above +x axis. Drag vector shown opposing resultant. Net force vector (shorter than F_app) shown in same direction as F_app. Caption: The two tugboat forces combine as vectors. Drag opposes the resultant. The difference between F_app and F_drag is the net force that produces the observed acceleration.] -->

---

## The scale shift

I want you to feel one thing before closing this chapter.

![Five labeled examples on a logarithmic force-axis: bat-ball collision (8000 N, 0.7 ms); person walking (~100 N); car accelerating (~2000 N); planet orbiting (Earth-Sun gravitational force ~3.5×10²² N). The equation F=ma works...](../images/04-dynamics-force-and-newton-s-laws-of-motion-fig-05.png)
*Figure 4.5 — F = ma at Five Scales — Bat-Ball to Earth-Sun*

The same three sentences — first law, $F = ma$, third law — govern a baseball bat shattering under $5{,}000 \text{ N}$ over a millisecond. They govern a person walking at a few newtons of net force over seconds. They govern a car cruising at zero net force over hours. They govern the Moon orbiting Earth under $2 \times 10^{20} \text{ N}$ of gravitational pull over billions of years.

Across more than 30 orders of magnitude in mass. At least as many in time. No modifications to the three sentences. No new terms. No fine print.

That's not obvious. It's extraordinary. And it's the reason Newton's laws sit at the foundation of everything mechanics builds on from here.

<!-- → [CHART: Log-scale chart showing mass range of objects governed by Newton's laws. X-axis: log₁₀(mass in kg), from -30 (electron, shown as limit) to +30 (large asteroid). Labeled points: baseball (0.145 kg), person (70 kg), car (1500 kg), Boeing 747 (4×10⁵ kg), Moon (7×10²² kg). Annotation: "Same three laws apply across all labeled points." Caption: Newton's laws hold across at least 25 orders of magnitude in mass with no corrections needed. The laws of quantum mechanics and general relativity become important only at the extremes not shown.] -->

---

## Exercises

### Warm-up

**4.1** *(LO 1)* A puck slides across a frictionless rink at constant velocity. (a) What is the net force on it? (b) Are there any forces on it at all — if so, list them.

**4.2** *(LO 3)* A $2.0 \text{ kg}$ object experiences a net force of $10 \text{ N}$. What is its acceleration?

**4.3** *(LO 5)* What is the weight (in newtons) of a $65 \text{ kg}$ student on Earth? On the Moon ($g_{\text{Moon}} = 1.62 \text{ m/s}^2$)? What is her mass in each location?

**4.4** *(LO 4)* Identify the third-law partner of each force: (a) Earth's gravity pulling down on you. (b) Your hand pushing on a door. (c) A horse pulling a cart forward.

### Application

**4.5** *(LO 2, 3)* A $1{,}200 \text{ kg}$ car accelerates from rest to $25 \text{ m/s}$ in $8.0 \text{ s}$. (a) What is its acceleration? (b) What is the net force during the acceleration? (c) If air drag and rolling friction sum to $400 \text{ N}$, what forward force must the engine-and-tires produce?

**4.6** *(LO 2, 3)* A $50 \text{ kg}$ skydiver falls at terminal velocity. (a) What is her acceleration? (b) What is the net force on her? (c) What is the magnitude of the air drag?

**4.7** *(LO 5)* A $20 \text{ kg}$ box hangs from two ropes attached to the ceiling, each making $30°$ with the vertical. Find the tension in each rope.

**4.8** *(LO 2, 3)* A horizontal force of $30 \text{ N}$ is applied to a $5.0 \text{ kg}$ block on a frictionless surface. (a) What is the block's acceleration? (b) What normal force does the surface exert?

### Synthesis

**4.9** *(LO 2, 3, 4)* Two ice skaters of masses $50 \text{ kg}$ and $80 \text{ kg}$ push off each other on a frictionless rink. The push lasts $0.50 \text{ s}$; the lighter skater experiences $200 \text{ N}$ during contact. (a) What force does the heavier skater experience? (b) What are their respective accelerations? (c) What are their velocities after the push?

**4.10** *(LO 3, 5)* A $100 \text{ kg}$ crate on a frictionless $30°$ ramp. (a) Component of gravity along the ramp. (b) Normal force from the ramp. (c) Acceleration down the ramp.

**4.11** *(LO 2, 4)* A $1{,}500 \text{ kg}$ truck tows a $500 \text{ kg}$ trailer on level road, accelerating at $1.0 \text{ m/s}^2$. Rolling friction on the trailer is $50 \text{ N}$. (a) Net force on the system. (b) Tension in the tow hitch. (c) Three Newton's-third-law force pairs in this scenario.

### Challenge

**4.12** *(beyond chapter)* A $0.145 \text{ kg}$ baseball changes velocity from $-40 \text{ m/s}$ to $+45 \text{ m/s}$ during $1.5 \text{ ms}$ of bat contact. (a) Average acceleration during contact. (b) Average force on the ball. (c) Average force on the bat. (d) Estimated peak force, given that real force-time curves typically peak at roughly twice the average.

**4.13** *(beyond chapter)* A rocket of initial mass $1{,}000 \text{ kg}$ (including $800 \text{ kg}$ of fuel) burns fuel at $4 \text{ kg/s}$, expelling exhaust at $2{,}500 \text{ m/s}$ relative to the rocket. (a) Thrust force. (b) Acceleration immediately after launch. (c) Acceleration just before all fuel is exhausted. (d) Why does the answer to (c) matter for real rocket design?

---

## LLM Exercise — Chapter 4: Forces in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A free-body diagram of a key element of your anchor phenomenon, with all forces identified, $F = ma$ applied, and at least one Newton's-third-law pair named explicitly.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 4, I want to apply Newton's three laws to my phenomenon. Please:

1. Pick ONE moment in my phenomenon where forces are interesting. Examples:
   - Bike commute: the moment of pushing off from a stop sign — what forces accelerate me?
   - Coffee maker: the moment when water column weight pushes down through the basket and grounds resist — what's the force balance during brewing?
   - Basketball shot: the moment of release — what forces does the player exert and feel?
   - Marathon: a steady-state stride at race pace — what forces are balanced, and what produces forward motion?
   - Espresso: the puck during extraction at 9 bar — what forces act on the coffee, and what balances them?

2. Draw (in ASCII or describe in text) the free-body diagram for the chosen object. List every external force with magnitude (estimated or computed) and direction.

3. Apply F = ma along each axis. Solve for any unknown (the acceleration, an unknown force, or a needed coefficient).

4. Identify at least one Newton's-third-law action-reaction pair in the scene. Name both forces, both objects, and explain why the pair doesn't "cancel."

5. Sanity check the result with one Fermi-style estimate.

6. Identify which fundamental force (gravity, electromagnetic, etc.) ultimately underlies each contact force you listed.

7. One sentence on how friction (Chapter 5) will modify this analysis.

Save the output as logbook/chapter-04-newtons-laws.md.
```

### What this produces

A fourth Logbook entry: a force analysis of your phenomenon with the action-reaction structure made explicit. By Chapter 4 you have foundation + 1D kinematics + 2D kinematics + force analysis — most of Newtonian mechanics in skeleton form for your phenomenon.

### How to adapt this prompt

- *For phenomena where motion is mostly steady-state* (a coffee maker reaching equilibrium, a marathon at constant pace): emphasize the balanced-force analysis (first law) rather than the accelerating analysis. Both are exercises of Newton's laws.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have force data (e.g., a pressure curve from an espresso machine, a wattmeter reading from a stationary bike), paste it and ask for a force-vs-time fit.

### Connection to previous chapters

Builds directly on Chapter 3's vector decomposition (forces are vectors; we resolve them along axes the same way we resolved velocities). The kinematics from Chapter 2 returns: once you have $a$ from Newton's second law, you can predict velocity and position from the kinematic equations.

### Preview of next chapter

Chapter 5 specializes Newton's laws to friction, drag, and elasticity — three force laws that fill in the "where do contact forces come from?" gap. The Chapter 5 LLM Exercise will ask you to compute friction or drag explicitly for your phenomenon.

---

**Tags:** Newtons-laws, force, free-body-diagram, third-law, inertia
