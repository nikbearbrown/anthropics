# Chapter 9 — Statics and Torque

*Two conditions, not one — and why the second one surprises everyone.*

---

The Vasco da Gama Bridge outside Lisbon spans the Tagus estuary for about seventeen kilometers. Its main cable-stayed section is $830 \text{ m}$ long, the towers rise $148 \text{ m}$ above the waterline, and the deck supports cars, trucks, and its own enormous weight around the clock. The region experienced a magnitude $8.7$ earthquake in 1755 — the one that flattened Lisbon — and the bridge was designed to handle another one.

For the bridge to do its job, every part of it must stay still. Not approximately still. Still. The deck doesn't translate — no net force in any direction. The deck doesn't rotate — no net torque about any axis. Each cable carries a specific tension, computed during design, that contributes to making both sums vanish at every cross-section. Each tower bears a load distributed across its concrete base so precisely that the structure neither tips, sinks, nor slides.

This is statics: the physics of not moving. It sounds passive. It is not. A bridge standing still under load is doing continuous force-and-torque bookkeeping at every element, all day, indefinitely. The engineer who designed it had to compute every force balance and every torque balance in advance, correctly, for all loading conditions. Get one wrong and something moves — which, in a bridge, means something falls.

What I want you to notice before we write a single equation is that statics requires *two* conditions, not one. Most people, hearing "the bridge isn't moving," instinctively think about forces: the cables pull up, gravity pulls down, it all cancels. That's the first condition. But you could have all forces balanced and the bridge still rotating — if the cables all pulled from the same side of center, there would be no net force (they're still adding to zero) but a net torque, and the deck would spin. The second condition says no rotation either. Both have to be satisfied separately, always.

---

## The first condition: nothing translates

The statement of the first condition is Newton's first law applied to a static case:

$$\sum \mathbf{F}_{\text{external}} = 0.$$

In two dimensions, this gives two equations:

$$\sum F_x = 0, \qquad \sum F_y = 0.$$

The procedure is the same as Chapter 4's free-body diagrams — draw the object, identify every external force, decompose into components, set each axis sum to zero. What's different in statics is that you are not looking for acceleration; you are solving for unknown forces from the requirement that the sums be zero. It's the same tool used backwards.

One subtlety from Chapter 5 reappears: static friction doesn't have a fixed value. It adjusts to whatever the equilibrium requires, up to a maximum of $\mu_s N$. You solve for the friction force from the equilibrium equations, then check that the required value doesn't exceed what the surfaces can provide.

### A sign on two ropes

A $200 \text{ N}$ sign hangs from two ropes attached to a ceiling. Rope 1 makes $30°$ from vertical; Rope 2 makes $45°$ from vertical on the opposite side. Find the tension in each rope.

Three forces on the sign: weight $200 \text{ N}$ downward, tension $T_1$ along Rope 1 (up and to the left), tension $T_2$ along Rope 2 (up and to the right).

Horizontal: $-T_1\sin30° + T_2\sin45° = 0$, so $T_1 = 1.414\,T_2$.

Vertical: $T_1\cos30° + T_2\cos45° = 200$.

Substituting: $0.866(1.414\,T_2) + 0.707\,T_2 = 1.932\,T_2 = 200$, so $T_2 \approx 103.5 \text{ N}$ and $T_1 \approx 146.4 \text{ N}$.

Check: $0.866(146.4) + 0.707(103.5) = 126.8 + 73.2 = 200 \text{ N}$ ✓. The steeper rope — the one closer to vertical — carries more of the load. This makes geometric sense: the more vertical a rope, the more directly it opposes the downward weight.

With two unknowns and two equations, the first condition closes the problem entirely. Many structural problems are like this. Others are not — two equations aren't always enough, and the first condition alone leaves you stuck. That is when you need torque.

---

## The second condition: nothing rotates

![Top-down view of a steering wheel. Two equal and opposite forces applied at diametrically opposed points produce ΣF = 0 (no translation) but Στ ≠ 0 (wheel rotates). A couple. The two equilibrium conditions must each be checked.](../images/09-statics-and-torque-fig-01.png)
*Figure 9.1 — Steering Wheel — Translational and Rotational Equilibrium Are Independent*

Here is the conceptual gap the first condition cannot fill. Imagine two people pulling on opposite ends of a horizontally balanced beam — one pulling up on the left, one pulling down on the right, with equal forces. The net force is zero. The first condition is satisfied. But the beam is rotating — those two equal and opposite forces applied at opposite ends are a *couple*, a pure torque with no net force. If you want the beam to stay still, you need to also require that no such rotational tendency exists. That is the second condition:

$$\sum \tau_{\text{external}} = 0.$$

**Torque** is the rotational analog of force. A force $F$ applied at a distance $r$ from a pivot, at angle $\theta$ between the force vector and the position vector from pivot to application point, produces a torque:

$$\tau = rF\sin\theta.$$

![Wrench applied to a bolt with the force at angle θ from the handle. Three equivalent ways to compute the same torque: full r times full F times sin θ; perpendicular distance r⊥ times full F; full r times perpendicular force...](../images/09-statics-and-torque-fig-02.png)
*Figure 9.2 — Three Equivalent Torque Formulas — τ = rF sin θ = r⊥F = rF⊥*

Three equivalent ways to say the same thing: $\tau = rF\sin\theta = r_\perp F = rF_\perp$, where $r_\perp$ is the perpendicular distance from the pivot to the line of force (the "lever arm"), and $F_\perp$ is the component of force perpendicular to $r$. Use whichever form the geometry makes obvious.

Units are newton-meters ($\text{N·m}$) — same as energy, but torque and energy are not the same thing. The sign convention: counterclockwise is positive, clockwise is negative.

<!-- → [INFOGRAPHIC: three equivalent torque diagrams side by side — (1) τ = rF sinθ with angle θ between r and F labeled, (2) τ = r⊥F showing the perpendicular lever-arm distance from pivot to line of force, (3) τ = rF⊥ showing the perpendicular component of F — all three producing the same numerical result for the same force, to make the geometric equivalence concrete] -->

The critical insight about choosing a pivot: **for a static object, the second condition holds about any point you choose.** The object isn't actually rotating about any particular axis — the requirement of zero net torque holds everywhere simultaneously. This means you can place the pivot wherever you want, and a smart choice is at the location of an unknown force, so that force contributes zero torque (its lever arm is zero) and vanishes from the equation. This is the chief trick of statics problem-solving, and it's the reason torque calculations often look easier than they should.

### A person on a beam

![Horizontal 4 m beam supported by two posts (left edge and right edge). Person of weight 700 N stands at x = 1 m from left. Beam's own weight 300 N at center. Pick the pivot at the right support: F_left × 4 = 300 × 2 + 700 × 3...](../images/09-statics-and-torque-fig-03.png)
*Figure 9.3 — Beam with a Person — Pick the Pivot to Kill Unknowns*

A uniform $50 \text{ kg}$ beam, $4.0 \text{ m}$ long, is supported at both ends. A $100 \text{ kg}$ person stands $1.0 \text{ m}$ from the left support. Find the support forces.

Forces: beam weight $490 \text{ N}$ at center ($2.0 \text{ m}$ from each end); person's weight $980 \text{ N}$ at $1.0 \text{ m}$ from left; left support $F_L$ upward; right support $F_R$ upward.

Vertical equilibrium: $F_L + F_R = 490 + 980 = 1470 \text{ N}$.

Torque about the left support (so $F_L$ drops out): counterclockwise positive.

$$+4.0\,F_R - 2.0(490) - 1.0(980) = 0 \implies F_R = \frac{980 + 980}{4.0} = 490 \text{ N}.$$

Then $F_L = 1470 - 490 = 980 \text{ N}$.

The left support carries twice the right support load — because the person is standing much closer to the left end ($1.0 \text{ m}$) than the right ($3.0 \text{ m}$). The torque equation distributed the load according to relative proximity. This is the mathematical expression of what your intuition would say about which side of a see-saw is heavier.

### A ladder that might slip

A $5.0 \text{ m}$ uniform $20 \text{ kg}$ ladder leans against a frictionless wall at $60°$ from the ground. The floor has $\mu_s = 0.40$. Will it slip?

![5 m ladder leaning at 60° against a smooth wall, friction only at the floor. Forces: weight W at center, normal N_floor, friction f_floor, normal N_wall. Equilibrium gives N_wall = W cot θ / 2; slip when μ_s < cot θ / 2.](../images/09-statics-and-torque-fig-05.png)
*Figure 9.5 — Ladder Leaning at 60° — Free-Body Diagram and Slip Condition*

Three forces: weight $196 \text{ N}$ at the midpoint ($2.5 \text{ m}$ along the ladder); normal force from wall $N_w$ horizontal at the top; normal force from floor $N_f$ upward; friction from floor $f$ horizontal (toward the wall) at the base.

Vertical: $N_f = 196 \text{ N}$.

Horizontal: $f = N_w$.

Torque about the base (so $N_f$ and $f$ drop out):

$$N_w \times (5.0\sin60°) - 196 \times (2.5\cos60°) = 0.$$
$$N_w \times 4.33 = 196 \times 1.25 = 245 \implies N_w \approx 56.6 \text{ N}.$$

Required friction: $f = 56.6 \text{ N}$. Maximum available: $\mu_s N_f = 0.40 \times 196 = 78.4 \text{ N}$.

Since $56.6 < 78.4$, the ladder holds. If the floor were oilier — say $\mu_s = 0.25$, giving a maximum of only $49 \text{ N}$ — the ladder would slip.

Notice the geometry: as the ladder is laid down more shallowly (smaller angle from horizontal), $N_w$ increases and $N_f$ stays the same. At some critical angle, the required friction hits the available maximum and the ladder slips. Builders' rules of thumb about ladder angles are just this calculation expressed as a single number.

<!-- → [INFOGRAPHIC: free-body diagram for the ladder problem — ladder at 60° with labeled force arrows: weight at midpoint (down), N_w at top (horizontal, away from wall), N_f at base (up), friction f at base (toward wall); show the perpendicular lever arms used in the torque equation as dashed lines to the line of each force, to make the geometry of torque visible] -->

---

## Mechanical advantage and the body as a structure

The two equilibrium conditions together let you do something powerful: calculate the internal forces in a mechanism or a body, not just the external reactions. This reveals numbers that consistently surprise people.

Consider a lever. One of the oldest simple machines. The principle: apply a force on the long end of a rigid bar balanced on a fulcrum, and a larger force appears on the short end. The mechanical advantage is:

$$MA = \frac{F_{\text{output}}}{F_{\text{input}}} = \frac{r_{\text{input}}}{r_{\text{output}}}.$$

A crowbar with input arm $0.8 \text{ m}$ and output arm $0.04 \text{ m}$ has $MA = 20$: a $100 \text{ N}$ push produces $2{,}000 \text{ N}$ at the nail. The energy balance still holds: the input end moves $20\times$ as far as the output end, so work in equals work out. You don't get energy for free — you trade distance for force.

Now apply the same analysis to your own body. The biceps muscle attaches to the forearm bone about $5 \text{ cm}$ from the elbow joint. A book in your hand sits about $30 \text{ cm}$ from the elbow. Torque balance about the elbow:

$$F_{\text{biceps}} \times 0.05 = W_{\text{book}} \times 0.30 \implies F_{\text{biceps}} = 6\,W_{\text{book}}.$$

![Side-view sketch of a forearm holding a load. Elbow is pivot. Biceps attaches 5 cm from elbow. Hand holds load 30 cm from elbow. Lever arm ratio 6:1 means biceps tension must be 6× the load weight. Trade: muscles are short and...](../images/09-statics-and-torque-fig-04.png)
*Figure 9.4 — Forearm — Biceps 5 cm From Elbow Lifts a Load 30 cm Away*

To hold a $5 \text{ kg}$ book ($49 \text{ N}$), the biceps must pull with about $294 \text{ N}$ — six times the book's weight, roughly $30 \text{ kg}$ of muscle force to hold a $5 \text{ kg}$ book. The mechanical advantage of the forearm lever is $1/6$, not 6. The body trades *force* for *speed and range of motion*: the muscle moves a tiny distance and the hand sweeps through a wide arc. That's the design — speed over force, paid for by enormous internal muscle loads.

<!-- → [INFOGRAPHIC: forearm-as-lever diagram — elbow as pivot (circle), biceps attachment point 5 cm from elbow (small arrow up labeled F_biceps), hand 30 cm from elbow (large arrow down labeled W_book = 49 N); show the torque balance equation numerically; annotate the mechanical advantage = 1/6; student should see that the muscle force is much larger than the load it's balancing] -->

The numbers get even more striking at the shoulder. A person hanging from a bar by one arm has the full body weight ($\sim 700 \text{ N}$ for $70 \text{ kg}$) pulling down through the hand, which is about $40 \text{ cm}$ from the shoulder joint. The deltoid muscle attaches only $10 \text{ cm}$ from the joint, at about $15°$ from the bone. The effective lever arm of the deltoid is $0.10 \times \sin15° \approx 0.026 \text{ m}$. Torque balance:

$$F_{\text{deltoid}} \times 0.026 = 700 \times 0.40 \implies F_{\text{deltoid}} \approx 10{,}700 \text{ N}.$$

Over a ton of force in the deltoid to hold up a $70 \text{ kg}$ body. The tendon that transmits this to the bone is carrying loads that would snap a steel cable of the same diameter — except that tendons are extraordinarily tough biological composites optimized over millions of years for exactly this regime.

The general message from the body calculations: internal forces in real structures are almost always much larger than the external loads, because internal elements typically have short lever arms. A muscle, a tendon, a cable anchor, a beam cross-section — all transmit loads that are multiplied from the external forces by an often surprising geometric factor. Getting these wrong in design means things fail.

---

## Stability: when equilibrium isn't enough

![Three side-by-side panels: ball in a bowl (stable, restoring torque on displacement), ball on hill (unstable, torque amplifies displacement), ball on flat (neutral, no torque). Criterion: project the center of mass through the...](../images/09-statics-and-torque-fig-06.png)
*Figure 9.6 — Three Stability Conditions — Stable, Unstable, Neutral*

Equilibrium — both conditions satisfied — is necessary for a structure to be at rest. But it is not sufficient for the structure to *stay* at rest under perturbation. That is the question of stability.

Balance a pencil on its tip. It is, for an instant, in equilibrium: the normal force from the table exactly supports the weight, and the torques balance (by symmetry, assuming perfect balance). But any small tilt — a vibration, a breath — moves the center of mass to the side. Now gravity's line of action falls *outside* the base of support (the pencil's tip), and gravity exerts a torque that tilts the pencil further. The perturbation grows. This is unstable equilibrium.

Now set the same pencil on its eraser end. Tilt it slightly. The center of mass is still over the base (the eraser is larger, and the pencil is short relative to its tilt angle). Gravity pulls the center of mass back down. The perturbation damps. This is stable equilibrium.

The geometric criterion: **an object is in stable equilibrium if, after a small perturbation, its center of mass is still directly above some point within its base of support.** This is why wide-base, low-center-of-mass designs are stable, and why tall narrow structures are not. A tall bookcase (narrow base, high center of mass) tips easily; a coffee table (wide base, low center of mass) almost never does.

<!-- → [INFOGRAPHIC: three stability cases side by side — (1) stable: a rounded object in a bowl, showing that a small tilt raises the center of mass and gravity pulls it back; (2) unstable: a ball balanced on a hill, showing that a small tilt lowers the center of mass and gravity pulls it further; (3) neutral: a ball on a flat surface, center of mass stays at constant height; label the center of mass position and the base of support in each, to make the geometric criterion concrete] -->

This same criterion explains why a semi-truck is prone to rollover in tight turns. The centripetal acceleration during a turn is equivalent (from the truck's frame) to a lateral force, which effectively tilts the gravity vector sideways. The truck's center of mass — about $1.5 \text{ m}$ above the road on a loaded trailer — swings outside the wheelbase ($\sim 2.6 \text{ m}$ track width) when the lateral acceleration exceeds $g \times (1.3/1.5) \approx 0.87g$. A passenger car, with a center of mass $0.5 \text{ m}$ up and a $1.6 \text{ m}$ track, requires $g \times (0.8/0.5) = 1.6g$ to tip — well above what any road turn produces. The truck is geometrically closer to the tipping threshold by design and load constraints.

---

## Two conditions, as one framework

Pull it together. Statics has two conditions:

**$\sum F = 0$** — nothing translates. Gives one equation per direction ($x$, $y$, and $z$ in 3D). Solved for unknown force magnitudes.

**$\sum \tau = 0$** — nothing rotates. Gives one equation per pivot choice (though only one independent one per 2D problem). Pivot chosen strategically to eliminate an unknown.

Together, three equations in 2D. Three unknowns: typically two force components and one torque condition. For most structural problems — the beam, the ladder, the sign on ropes — this is exactly enough.

The same two conditions describe the kitchen table, the Vasco da Gama Bridge, the bones of your skeleton under standing load, and every bolt holding a machine together. The scales differ by many orders of magnitude. The conditions don't change.

<!-- → [INFOGRAPHIC: summary diagram showing the two equilibrium conditions side by side — left panel: force diagram with vector arrows summing to zero (translational equilibrium), right panel: torque diagram showing clockwise and counterclockwise torques of equal magnitude about a pivot (rotational equilibrium); label the three equations that emerge in 2D and note the strategic pivot choice that eliminates one unknown] -->

What changes when you move from statics (Chapter 9) to dynamics (Chapter 10) is not the framework but the right-hand side. In statics, $\sum F = 0$ and $\sum \tau = 0$. In dynamics, $\sum F = ma$ and $\sum \tau = I\alpha$. The same balance equations, with inertia and acceleration reinstated. Statics is the limiting case where both accelerations are zero. The two conditions that had to be satisfied simultaneously in this chapter become the two *equations of motion* in the next.

---

## Exercises

### Warm-up

**9.1** *(LO 1)* A $5.0 \text{ kg}$ box sits motionless on a level floor. (a) What is the normal force? (b) You press down on the box with an additional $20 \text{ N}$. Now what is the normal force?

**9.2** *(LO 2)* A $40 \text{ N}$ force is applied perpendicular to the end of a wrench $0.25 \text{ m}$ long. (a) What torque does this produce about the bolt? (b) If the same force is applied at $30°$ from perpendicular (i.e., $60°$ from the wrench handle), what torque results?

**9.3** *(LO 1, 2)* A $200 \text{ N}$ sign hangs from a single rope tied to the ceiling. The rope makes $20°$ from vertical. A horizontal wire is also attached to the wall to keep the sign from swinging. Find the tension in the rope and the tension in the horizontal wire.

**9.4** *(LO 4)* Identify each as stable, unstable, or neutral equilibrium, and explain using the center-of-mass criterion: (a) a marble at the bottom of a spherical bowl; (b) a marble at the top of a hill; (c) a marble resting on a flat table; (d) a pencil balanced upright on its tip.

### Application

**9.5** *(LO 1, 2, 3)* A uniform $30 \text{ kg}$ plank $4.0 \text{ m}$ long is supported at both ends. A $60 \text{ kg}$ person stands $1.0 \text{ m}$ from the left end. (a) Find the support force at each end. (b) Where would the person have to stand for both supports to carry equal loads?

**9.6** *(LO 1, 2, 3)* A $5.0 \text{ m}$ uniform $15 \text{ kg}$ ladder leans against a frictionless wall at $70°$ from the ground. (a) Find the normal force from the wall. (b) Find the required friction force at the base. (c) What minimum coefficient of static friction keeps the ladder from slipping?

**9.7** *(LO 5)* A lever has an input arm of $1.2 \text{ m}$ and an output arm of $0.15 \text{ m}$. (a) What is the mechanical advantage? (b) A $60 \text{ N}$ input force produces what output force? (c) If the input end moves $0.60 \text{ m}$, how far does the output move? (d) Verify that the input work equals the output work.

**9.8** *(LO 1, 2, 3)* A horizontal uniform beam of length $3.0 \text{ m}$ and mass $12 \text{ kg}$ is attached to a wall by a hinge at its left end and supported by a cable attached to the wall at $40°$ above horizontal at the right end. A $25 \text{ kg}$ lamp hangs from the right end. Find the cable tension and the force the hinge exerts on the beam (magnitude and direction).

### Synthesis

**9.9** *(LO 1, 2, 3)* A $5{,}000 \text{ kg}$ bridge $30 \text{ m}$ long is supported at both ends. A $1{,}000 \text{ kg}$ truck is parked with its center of mass $10 \text{ m}$ from the left support. Find the support force at each end.

**9.10** *(LO 2, 5)* Model the forearm as a uniform $1.5 \text{ kg}$ lever $38 \text{ cm}$ long, pivoted at the elbow. The biceps attaches $4 \text{ cm}$ from the elbow; a $4.0 \text{ kg}$ weight is held in the hand. (a) What torque does the held weight produce about the elbow? (b) What torque does the forearm's own weight produce (acting at its center, $19 \text{ cm}$ from elbow)? (c) What biceps force is required to hold the arm horizontal? (d) What is the mechanical advantage of the forearm lever?

**9.11** *(LO 4)* A loaded delivery truck has its center of mass $1.4 \text{ m}$ above the road and a track width of $2.4 \text{ m}$. (a) On what sideways tilt angle will it tip (ignoring centripetal effects — just geometric tipping)? (b) At what lateral acceleration (as a fraction of $g$) will it roll over in a turn? (c) Compare to an SUV with center of mass $0.7 \text{ m}$ up and track width $1.6 \text{ m}$.

### Challenge

**9.12** *(LO 1, 2, beyond chapter)* A uniform door of mass $25 \text{ kg}$, height $2.0 \text{ m}$, and width $0.90 \text{ m}$ hangs from two hinges — one $0.25 \text{ m}$ from the top, one $0.25 \text{ m}$ from the bottom. Find the horizontal and vertical force components at each hinge. (Hint: assume the top hinge carries the horizontal load; use both force and torque equations to find all four components.)

**9.13** *(LO 2, 5, beyond chapter)* A person does a one-arm hang from a pull-up bar. Their mass is $72 \text{ kg}$, and the hand grips the bar $42 \text{ cm}$ from the shoulder joint. The rotator-cuff muscle group attaches $8 \text{ cm}$ from the shoulder at $20°$ from the upper-arm bone. (a) Find the rotator-cuff force required. (b) What is the mechanical advantage of this muscle group for this task? (c) The shoulder joint itself must also exert a force to close the force balance. Find its magnitude and direction.

---



By the end of this chapter you should be able to:

1. State the two conditions for static equilibrium ($\sum \mathbf{F} = 0$ and $\sum \tau = 0$) and apply both to the same problem.
2. Compute torque ($\tau = rF\sin\theta = r_\perp F = rF_\perp$) about any chosen pivot, with correct sign.
3. Solve for unknown forces in static structures by choosing a strategic pivot to eliminate an unknown from the torque equation.
4. Distinguish stable, unstable, and neutral equilibrium using the center-of-mass-over-base-of-support criterion.
5. Compute mechanical advantage of a lever and verify the force-distance trade-off with energy conservation.

**Prerequisites.** Chapter 4 (Newton's laws). Chapter 5 (friction, normal forces). Chapter 7 (work and energy, for mechanical advantage). Chapter 3 (vector decomposition).

**Why this chapter matters.** Statics underlies every standing structure: bridges, buildings, scaffolding, prosthetics, bones. It is the most-used branch of mechanics in civil and mechanical engineering. And it is the limiting case of the rotational dynamics in Chapter 10 — every concept here generalizes directly when things start moving.

---

## ↳ Dig Deeper — Statically determinate vs. indeterminate

*A statically determinate structure has as many equilibrium equations as unknown forces — solvable by statics alone. A statically indeterminate structure has more unknowns than equations and requires knowing how the material deforms (Hooke's law from Chapter 5) to solve. Understanding the distinction is the entry to structural engineering.*

**Prompt:**
> Explain the distinction between statically determinate and statically indeterminate structures. Give one example of each: (a) a beam supported at two points (determinate — 3 equilibrium equations, 3 unknown reaction forces), (b) a beam supported at three points (indeterminate — 3 equations, 4 unknowns). For the indeterminate case, explain what additional information (material stiffness via Hooke's law) is needed to solve. End with one sentence on why most engineered structures are designed to be statically determinate or only mildly indeterminate.

**What to do with the output:** Save it. The determinate/indeterminate distinction is foundational to structural engineering and explains why simple beam problems are tractable while complex frames require finite-element analysis.

---

## ↳ Dig Deeper — Why "any pivot" works

*The chapter says you can choose any point as pivot for the torque equation and it always gives the correct equilibrium condition. This is non-trivial — it's what justifies the strategic pivot choice.*

**Prompt:**
> Explain why, for an object in static equilibrium, $\sum \tau = 0$ holds about *any* chosen pivot point. Walk through the algebra: show that if $\sum \mathbf{F} = 0$ and $\sum \tau = 0$ about one point, then $\sum \tau = 0$ about any other point. (Hint: shifting the pivot adds $-\mathbf{r}_{\text{shift}} \times \mathbf{F}_{\text{net}}$ to every torque, and this sum is zero because $\mathbf{F}_{\text{net}} = 0$.) End with one sentence on why this is the key to choosing a clever pivot to simplify the algebra.

**What to do with the output:** Save it. The "any pivot works" result is the heart of strategic statics problem-solving and the reason the beam and ladder calculations in this chapter work out so cleanly.

---

## ↳ Dig Deeper — Center of mass and stability

*An object's stability is tied to whether its center of mass falls within its base of support. If tilting moves the center of mass outside the base, the object tips. This explains rollover in trucks, the lean of runners carrying loads, and the geometry of every standing structure.*

**Prompt:**
> Explain the geometric criterion: an object is stable if the vertical line through its center of mass falls within its base of support. Apply it to: (a) a person standing upright, (b) a person carrying a heavy backpack and leaning forward to compensate, (c) a loaded tractor-trailer in a tight turn (where lateral acceleration effectively tilts the gravity vector). End with one sentence on why a wider base or a lower center of mass increases stability.

**What to do with the output:** Save it. The center-of-mass-over-base-of-support criterion is the most useful intuitive rule in statics and explains a large fraction of everyday stability behavior.

---

## LLM Exercise — Chapter 9: Statics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A static-equilibrium analysis of one stationary element of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 9, I want to apply the two conditions of static equilibrium (ΣF = 0, Στ = 0) to one stationary element of my phenomenon. Please:

1. Identify ONE stationary structural element. Examples:
   - Bike commute: bike at rest leaning against a wall — what friction at the floor, what normal force from the wall?
   - Coffee maker: brewing chamber gasket under pressure load — what static force balance keeps it sealed?
   - Basketball: a basketball balanced on a fingertip — what center-of-mass condition?
   - Marathon: a runner standing still at the start line — what muscles are active to maintain posture?
   - Espresso: portafilter handle locked into the group head — what torque balance holds it in place under 9 bar?

2. Draw (in ASCII or describe) the free-body diagram. Identify all external forces and where they act.

3. Apply ΣF = 0 along each axis. Apply Στ = 0 about a strategic pivot.

4. Solve for the unknown forces. Report with units, sig figs, and percent uncertainty.

5. Sanity-check: does the magnitude of the muscle/cable/contact force surprise you?

6. Identify stability (stable, unstable, neutral) and the geometric criterion (does the center of mass fall within the base of support?).

7. One sentence connecting to Chapter 10 (rotational dynamics) — when torques don't balance, the object accelerates rotationally.

Save the output as logbook/chapter-09-statics.md.
```

### What this produces

A ninth Logbook entry: an equilibrium analysis revealing the often-surprising forces in stationary structures — muscle forces are almost always much larger than expected.

### How to adapt this prompt

- *For phenomena that are always moving:* focus on a moment when the system is briefly at rest (a basketball at its arc apex, a runner at the moment of foot plant, a bike at a traffic light).
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have measurements or a CAD sketch, paste the dimensions.

### Connection to previous chapters

Builds on Chapter 4 (force balance, Newton's first law). Adds torque and rotational equilibrium. Uses vector decomposition (Chapter 3) and friction (Chapter 5). The mechanical-advantage results here connect directly to work and energy conservation (Chapter 7).

### Preview of next chapter

Chapter 10 generalizes everything here to moving rotational systems. Where statics has $\sum \tau = 0$, dynamics has $\sum \tau = I\alpha$ — the rotational analog of $F = ma$. The same framework, with non-zero right-hand sides.

---

## What would change my mind

The chapter argues that the two equilibrium conditions are exact in classical mechanics for any rigid body at rest. The argument would need revision if a problem required more than three independent equations in 2D — which signals a statically indeterminate structure, requiring deformation analysis. This isn't a refutation of the framework; it's the extension into elasticity (Chapter 5) and finite-element analysis. The conditions themselves are exact; only the question of whether they're *sufficient* to close the problem depends on the structure.

## Still puzzling

The deepest question this chapter raises: **why is the rigid-body assumption ever accurate?** All real materials deform under load (Hooke's law, Chapter 5). Yet treating a beam as perfectly rigid for calculating support reactions almost always gives the right answer for the *reactions*, even when the deformations are real and measurable. Why? Because the typical strains are small compared to the overall geometry — the beam's shape barely changes, so the lever arms barely change, so the torque equations barely change. The approximation is self-consistent. But understanding *when* it breaks down — in slender structures, at dynamic loading rates, near material limits — is the entire subject of structural mechanics, and it lies beyond what this chapter can resolve.

---

## AI Wayback Machine

**Archimedes of Syracuse** worked out the law of the lever and the basics of static equilibrium in the 3rd century BCE. The famous line — "Give me a place to stand, and I will move the Earth" — was a demonstration of mechanical advantage, not rhetoric. His treatises on mechanics established statics as a quantitative science two thousand years before Newton.

![Archimedes of Syracuse](../images/archimedes-6oo.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Archimedes, and how does his work connect to the statics and torque we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Archimedes"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Archimedes's geometric proof of the law of the lever.
- Ask it about the Archimedes Palimpsest — how his lost writings were recovered from a medieval parchment.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 10 takes the two equilibrium conditions and removes the requirement of zero acceleration. Where $\sum F = 0$ becomes $\sum F = ma$, $\sum \tau = 0$ becomes $\sum \tau = I\alpha$, where $I$ is the moment of inertia (the rotational analog of mass) and $\alpha$ is the angular acceleration. Every statics problem you solved here is a special case of a dynamics problem with $a = 0$ and $\alpha = 0$. Chapter 11 (fluid statics) applies the same balance framework to fluids — pressure is the fluid analog of contact force, and the same two conditions of balance determine pressure at every depth. The pattern persists: equilibrium, in any branch of physics, means whatever could change is balanced so that it doesn't.

---

**Tags:** statics, torque, equilibrium, mechanical-advantage, free-body-diagram
