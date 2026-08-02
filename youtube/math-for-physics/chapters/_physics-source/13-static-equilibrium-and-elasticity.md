# Static Equilibrium and Elasticity

## Three alternative titles

1. Why Bridges Don't Fall — The Two Laws That Keep Structures Standing
2. In Balance: Equilibrium, Deformation, and the Limits of Materials
3. When Things Hold Still — From Rigid Bodies to Bending Beams

## TL;DR

A structure stays upright when two conditions are met: all forces sum to zero *and* all turning forces sum to zero. Once you understand why both matter, you can calculate why a ladder leans at the right angle, where a bridge beam breaks first, and how far a rope stretches.

---

## Part 1: The Opening — A Bridge Under Load

Picture a highway bridge on a clear morning. Beneath it, a structural engineer walks the main span, carrying a worn clipboard and a hundred small concerns. Every beam, every cable, every joint has been calculated to stand. But the calculations rest on a premise so fundamental that it's almost invisible: *each part of the bridge must be in equilibrium*. Not moving. Not rotating.

The main cable doesn't slip at its anchor. The vertical suspender doesn't twist. The steel box-beam spreads the load evenly from top surface to bottom. Each of these facts is true because of two conditions—first stated by Isaac Newton, then refined by generations of engineers—that describe when an object stays still.

Here is the premise: the moment something stops moving, something is true about the forces acting on it.

What we are about to discover is that "something" is actually two things. And getting them both right is the difference between a bridge that stands for a century and one that collapses.

### Learning Objectives

After this chapter:

- You will identify when a system is in static equilibrium and apply both conditions correctly.
- You will draw free-body diagrams that reveal hidden forces.
- You will solve realistic problems: ladders, beams, cable tensions, columns under weight.
- You will understand what happens when materials deform elastically, what limits that deformation, and where plastic flow begins.
- You will interpret material properties (Young's modulus, bulk modulus, shear modulus) not as abstract numbers but as answers to concrete questions: How much load before this rope breaks? How far will this column compress?

### Prerequisites

You need vectors (Chapter 2), Newton's laws (Chapters 5–6), torque and moment of inertia (Chapter 10). You need calculus: the integral definition of moment of inertia, partial derivatives for understanding how strain varies with position. You need to be comfortable with free-body diagrams.

---

## Part 2: The First Condition — Translational Equilibrium

### Concept 2A: $\sum \vec{F} = \vec{0}$ — Why Motion Stops

When you place an object on a table and it stays there, the net force on it is zero. The weight pulling down is balanced by the normal force pushing up. This is the **first equilibrium condition**: the vector sum of all external forces equals zero.

In component form, for an object in equilibrium:

$$\sum F_x = 0 \quad \sum F_y = 0 \quad \sum F_z = 0$$

This condition alone governs translational motion. When it holds, the center of mass of the object does not accelerate. The object either sits still or moves at constant velocity—and since we are interested in static equilibrium, we enforce that it sits still.

**Etymology**: *Equilibrium* comes from Latin *aequus* (equal) and *libra* (balance, as in a balance scale). The word captures the image perfectly: one side equals the other.

#### The Trade-Off: Rigid-Body Assumption

Here is what we are buying and what we are selling:

**What we buy**: The ability to ignore internal stresses in simple problems. A plank in static equilibrium can be treated as a point mass for force balance purposes. This simplifies the math enormously.

**What we sell**: The assumption breaks when stress becomes extreme. A thin rod under enormous compressive load will buckle—will rotate—not because the net force is unbalanced, but because the material has yielded. The rigid-body model stops applying. Real structures require reinforcement and design rules to stay rigid under load.

#### Worked Example: The Pan of Objects

A small pan of mass 42.0 g hangs from two strings angled upward at different angles. One string is 5.0 cm long; the other is 10.0 cm long. They are attached to a ceiling 15 cm apart. Mass is added to the pan until one string snaps. The maximum tension each string can bear is 2.80 N.

Which string breaks first, and how much mass must be added?

**Setup**: The pan and contents have weight $w = (M + m)g$ where $M = 42$ g is the pan and $m$ is the added mass. Three forces act on the pan's attachment point: the two tensions $T_1$ and $T_2$, and the weight $w$ downward.

For this knot to be in equilibrium, the two tension components must balance the weight. The geometry of the strings creates a right triangle. From the 5.0 cm and 10.0 cm strings separated by the ceiling distance, we can compute the angles:

$$\sin \alpha_1 = \frac{2}{\sqrt{5}}, \quad \cos \alpha_1 = \frac{1}{\sqrt{5}}$$
$$\sin \alpha_2 = \frac{1}{\sqrt{5}}, \quad \cos \alpha_2 = \frac{2}{\sqrt{5}}$$

The first equilibrium condition in the horizontal direction gives:
$$T_1 \cos \alpha_1 = T_2 \cos \alpha_2$$
$$T_1 / \sqrt{5} = 2 T_2 / \sqrt{5}$$
$$T_1 = 2 T_2$$

The shorter string carries twice the tension. It will snap first.

In the vertical direction:
$$T_1 \sin \alpha_1 + T_2 \sin \alpha_2 = (M + m)g$$
$$2 T_1 / \sqrt{5} + T_1 / \sqrt{5} = (M + m)g$$
$$2.5 T_1 / \sqrt{5} = (M + m)g$$

Setting $T_1 = 2.80$ N (breaking tension):
$$(M + m) = \frac{2.5 \times 2.80}{\sqrt{5} \times 9.8} = \frac{7.0}{21.95} \approx 0.319 \text{ kg}$$

So $m = 319 - 42 = 277$ g must be added.

#### Common Misconception

"If the net force is zero, nothing happens to the object."

**Reality**: Correct—but "nothing" means the object's linear motion doesn't change. It doesn't mean the object is rigid or undeformed. The first condition addresses translation only. A rope under equal tension at both ends has zero net force but is stretched. A rod pushed from both ends has zero net force but is compressed. To know whether the object rotates or deforms, you need additional information.

---

## Part 3: The Second Condition — Rotational Equilibrium

### Concept 3A: $\sum \vec{\tau} = \vec{0}$ — Why Rotation Stops

Here is what might surprise you: you can satisfy the first equilibrium condition and still have the object spin. Push a door with equal force on opposite sides, at equal distances from the hinge. The net force is zero. The door will not translate. But it will rotate.

The **second equilibrium condition** governs rotation:

$$\sum \vec{\tau} = \vec{0}$$

For an object to be in static equilibrium, the net external torque (taking about any point) must also equal zero. In the plane (the most common case), this becomes:

$$\sum \tau_z = 0$$

where each torque is computed as $\tau = rF \sin \theta$, with $r$ the lever arm, $F$ the force magnitude, and $\theta$ the angle between the force and the lever arm.

Torque, remember, measures rotational effect. A large force near the pivot does little. A small force far from the pivot does much.

**Etymology**: *Torque* comes from Latin *torquere*, to twist. The image of twisting is literal.

#### The Deep Mechanism: Why the Pivot Point Matters

Here is a detail most textbooks gloss over: torque depends on where you measure from. The torque of a force about point A is different from the torque of the same force about point B.

Yet the second equilibrium condition is stated as $\sum \tau = \vec{0}$ without specifying the pivot. This seems to contradict itself. How can all torques sum to zero about one point but not another?

The answer is the hidden assumption: *if the first equilibrium condition holds, then the net torque is zero about any point*.

Here is why. Let's calculate the torque of a force $\vec{F}$ about two different points, separated by vector $\vec{R}$:

$$\tau_A = \vec{r}_A \times \vec{F}$$
$$\tau_B = \vec{r}_B \times \vec{F} = (\vec{r}_A - \vec{R}) \times \vec{F} = \vec{r}_A \times \vec{F} - \vec{R} \times \vec{F}$$

The difference is $\vec{R} \times \vec{F}$. For the net torque to be the same about both points, we need:

$$\sum (\vec{R} \times \vec{F}_k) = \vec{R} \times \sum \vec{F}_k = \vec{0}$$

This is satisfied *exactly when the net force is zero*. So if $\sum \vec{F} = \vec{0}$, then $\sum \tau_A = \sum \tau_B$ for any two points A and B.

**What this means**: Once the first condition is satisfied, you are free to choose any pivot point you like when computing torques. Choose wisely. Choose a point where unknown forces act—they contribute zero torque there—and you reduce the unknowns instantly.

#### Trade-Off: Choice of Pivot

**What we buy**: Enormous simplification. A clever pivot choice can eliminate several unknowns at once, turning a system of three equations into one.

**What we sell**: We must be careful to apply the condition correctly. The pivot point is not special in reality; it's special only in our calculation. We're not saying the object actually pivots there—we're using it as a reference for measuring rotational effect.

#### Worked Example: The Meter Stick on a Fulcrum

A uniform meter stick of mass 150 g is balanced on a fulcrum at the 30 cm mark (so 30 cm on one side, 70 cm on the other). A 50 g mass hangs at the 10 cm mark. A 75 g mass hangs at the 70 cm mark. Where must a third mass $m_3$ be placed at the 100 cm mark (the right end) to balance the system? What is the normal force at the fulcrum?

**Setup**: Let the fulcrum (the pivot) be at 30 cm. Five forces act:

1. Weight of 50 g mass: $w_1 = 0.50$ N downward, lever arm $r_1 = 20$ cm
2. Weight of 75 g mass: $w_2 = 0.75$ N downward, lever arm $r_2 = 40$ cm (to the right of fulcrum)
3. Weight of stick: $w = 1.50$ N downward, lever arm $r = 20$ cm (the stick's center of mass is at 50 cm, which is 20 cm right of fulcrum)
4. Normal force at fulcrum: $N$ upward, lever arm $r_N = 0$ cm
5. Weight of unknown mass: $w_3 = m_3 g$ downward, lever arm $r_3 = 70$ cm (to the right)

For rotational equilibrium about the fulcrum:
$$\tau_1 + \tau_2 + \tau + \tau_3 = 0$$

Taking counterclockwise as positive:
$$(-0.50 \text{ N})(0.20 \text{ m}) + (-0.75 \text{ N})(0.40 \text{ m}) + (-1.50 \text{ N})(0.20 \text{ m}) + (-m_3 g)(0.70 \text{ m}) = 0$$

$$-0.10 - 0.30 - 0.30 = (m_3 \times 9.8)(0.70)$$

$$m_3 = \frac{0.70}{9.8 \times 0.70} = 0.317 \text{ kg} \approx 317 \text{ g}$$

For translational equilibrium:
$$N = w_1 + w_2 + w + w_3 = (0.050 + 0.075 + 0.150 + 0.317) \times 9.8 = 5.8 \text{ N}$$

Notice: The answer does not depend on $g$. The balance condition depends only on ratios of masses and distances, not on the local gravitational field. This is why balance scales work anywhere on Earth—or the Moon.

#### Common Misconception

"If net torque is zero, the object doesn't rotate."

**Reality**: Correct. But that's because we're starting from rest. An object rotating at constant angular velocity with zero net torque will keep rotating. We ensure the object is not rotating by enforcing both that the net torque is zero *and* that the object starts from rest.

---

## Part 4: Problem-Solving Strategy — Putting Both Conditions to Work

### Concept 4A: Free-Body Diagrams and Pivot Selection

Solving a static equilibrium problem is a game of information management. Here are the steps:

1. **Identify the object** and all forces acting on it.
2. **Draw a free-body diagram**. Include every force, its magnitude (if known), and its point of application. Label every unknown.
3. **Choose a coordinate system**. Usually Cartesian; occasionally you'll want to align axes with the object.
4. **Choose a pivot point**. This is your strategic choice. Pick wisely—a point where unknown forces act will zero out their torques.
5. **Write the equilibrium conditions**:
   - Sum of forces in $x$: $\sum F_x = 0$
   - Sum of forces in $y$: $\sum F_y = 0$
   - Sum of torques about the chosen pivot: $\sum \tau = 0$
6. **Solve the system** algebraically. You have three equations and typically three unknowns.

This is mechanical, but it works every time.

#### Worked Example: The Ladder at a Dangerous Angle

A uniform ladder of length $L = 5.0$ m and weight $w = 400$ N leans against a smooth vertical wall (no friction). It rests on a rough floor with coefficient of static friction $\mu_s = 0.38$ (just barely enough). Below what angle with the floor will the ladder slip?

**Setup**: The ladder touches the wall at height $h = L \cos \beta$, where $\beta$ is the angle from the floor. Four forces act:

1. Weight $w = 400$ N downward at the center (2.5 m from either end)
2. Normal force $N$ from the floor, upward
3. Static friction $f$ from the floor, horizontal (toward the wall)
4. Normal force $F_w$ from the wall, horizontal (away from the wall)

Since the wall is frictionless, there is no vertical force from the wall.

**For translational equilibrium**:
- Horizontal: $f = F_w$
- Vertical: $N = w = 400$ N

**For rotational equilibrium**, choose the pivot at the point where the ladder touches the floor (contact with the floor). Then $N$ and $f$ produce zero torque (they act at the pivot):

$$\tau_w + \tau_{weight} = 0$$

The normal force from the wall acts at height $L \cos \beta$ with lever arm $L \sin \beta$:
$$\tau_w = F_w (L \sin \beta)$$

The weight acts at horizontal distance $\frac{L}{2} \sin \beta$ from the pivot:
$$\tau_{weight} = -w \left( \frac{L}{2} \sin \beta \right)$$

(Negative because it tries to rotate the ladder away from the wall.)

Setting the sum to zero:
$$F_w (L \sin \beta) = w \left( \frac{L}{2} \sin \beta \right)$$
$$F_w = \frac{w}{2} = 200 \text{ N}$$

This is independent of $\beta$. So at any angle, the wall must push with 200 N for torque balance.

But friction must be strong enough:
$$f = F_w = 200 \text{ N}$$

The maximum static friction is:
$$f_{\max} = \mu_s N = 0.38 \times 400 = 152 \text{ N}$$

Since the friction required (200 N) exceeds what is available (152 N), the ladder will slip. The angle at which slipping begins is found from:

$$f_{\max} = \mu_s w = \mu_s w$$
$$\tan \beta = \frac{1}{2 \mu_s} = \frac{1}{2 \times 0.38} = 1.32$$
$$\beta = 53°$$

**Below 53°, the ladder is safe. Below 53°, it slips.**

---

## Part 5: From Static to Elastic — Materials Under Load

### Concept 5A: Stress and Strain — Deformation Under Force

Now we shift perspective. Everything so far assumed rigid bodies. But real structures deform. A steel cable under tension stretches slightly. A column under compression squashes. Understanding when deformation is recoverable (elastic) and when it becomes permanent (plastic) is how engineers decide on materials and dimensions.

When a force acts on an object and deforms it, physics names two quantities: **stress** and **strain**.

**Stress** is force per unit area—the intensity of the force doing the deforming:
$$\text{stress} = \frac{F}{A}$$

**Strain** is the fractional change in dimension—the amount of deformation relative to the original size:
$$\text{strain} = \frac{\Delta L}{L_0}$$

Stress has units of pressure (pascals, Pa). Strain is dimensionless—it's a ratio.

#### The Linear Regime: Hooke's Law for Materials

For small stresses, stress and strain are proportional:
$$\text{stress} = E \times \text{strain}$$

The proportionality constant $E$ is the **elastic modulus**. It is a material property—it depends on what the material is made of, not on the size or shape of the sample.

Three types of elastic modulus matter:

**Young's modulus** $Y$ applies when a material is pulled or compressed along one direction:
$$Y = \frac{F/A}{\Delta L / L_0}$$

A high Young's modulus means the material is stiff—you must pull hard to stretch it much. Steel: $Y \approx 200$ GPa. Rubber: $Y \approx 0.01$ GPa. Steel is roughly 20,000 times stiffer.

**Bulk modulus** $B$ applies when a material is squeezed from all sides (as a submarine experiences in the ocean):
$$B = -\frac{\Delta p}{\Delta V / V_0}$$

**Shear modulus** $S$ applies when forces act parallel to a surface, causing layers to slide relative to each other:
$$S = \frac{F/A}{\Delta x / L_0}$$

#### The Trade-Off: Elastic Versus Plastic Behavior

**What we buy**: For stresses below the elastic limit, deformation is recoverable. Remove the force, the material springs back. This allows structures to flex under load without permanent damage.

**What we sell**: Once stress exceeds the elastic limit, the material flows plastically. Deformation becomes permanent. Push further and the material fails—it fractures or tears.

The boundary between elastic and plastic is not sharp. It's a range. Below the **proportionality limit**, Hooke's law holds exactly. Between the proportionality limit and the **elastic limit**, the material is still elastic but the relationship becomes nonlinear. Beyond the elastic limit, the material no longer recovers.

For most engineering problems, we stay well within the elastic regime, where Hooke's law is accurate.

#### Worked Example: A Steel Cable Under Load

A steel cable of length $L_0 = 2.0$ m and cross-sectional area $A = 0.30$ cm² = $3.0 \times 10^{-5}$ m² supports a hanging platform of mass $M = 550$ kg. The weight of the cable itself is negligible.

What is the stress in the cable, and how much does it elongate?

**Stress**:
$$\text{stress} = \frac{F}{A} = \frac{Mg}{A} = \frac{550 \times 9.8}{3.0 \times 10^{-5}} = \frac{5390}{3.0 \times 10^{-5}} = 1.8 \times 10^8 \text{ Pa}$$

This is 180 megapascals—well within the elastic range for steel (which can sustain stresses exceeding 400 MPa).

**Elongation**: Young's modulus for steel is $Y = 2.0 \times 10^{11}$ Pa. From Hooke's law:
$$\text{strain} = \frac{\text{stress}}{Y} = \frac{1.8 \times 10^8}{2.0 \times 10^{11}} = 9 \times 10^{-4}$$

$$\Delta L = \text{strain} \times L_0 = 9 \times 10^{-4} \times 2.0 = 1.8 \times 10^{-3} \text{ m} = 1.8 \text{ mm}$$

The cable stretches by 1.8 mm. Tiny, but real. When the load is removed, the cable returns to its original length.

#### Common Misconception

"Young's modulus tells you how much a material will stretch."

**Reality**: It tells you the *relationship* between stress and strain, not the absolute deformation. A thin wire and a thick wire made of the same material have the same Young's modulus, but the thin wire stretches more under the same force because stress is force per unit area.

---

## Part 6: Material Limits — Where Elastic Becomes Plastic

### Concept 6A: The Stress-Strain Diagram and Failure

If you slowly increase the load on a sample of material and plot stress versus strain, you get a curve characteristic of that material. It tells a story.

For a ductile metal (like steel or aluminum):

1. **Linear elastic region** (from origin to point H): Hooke's law holds. Stress and strain are proportional. The slope is Young's modulus.
2. **Nonlinear elastic region** (H to E): The material still bounces back, but the curve bends. Hooke's law no longer holds exactly.
3. **Plastic region** (E to F): Deformation becomes permanent. The material flows. The stress may even decrease slightly as strain increases—the material is being stretched so far that it's getting thinner, so the stress (force per area) decreases.
4. **Fracture** (at F): The material breaks. On the diagram, this is the end.

The **elastic limit** (point E) is where recovery stops. Beyond this, removing the load leaves the material permanently deformed.

The **breaking stress** (or ultimate stress) is the maximum stress the material can sustain. For steel: roughly 400 MPa. For aluminum: roughly 200 MPa. Aluminum can be pushed to roughly the same strain before breaking, but with a smaller stress. Steel is stronger.

#### Etymology: Why "Elastic"?

*Elastic* comes from the Greek *elastikos*, meaning "driving or pushing back." An elastic material pushes back—it resists deformation and returns to its original shape when released. The name captures the physics perfectly.

#### Scale Shift: From Specimen to Structure

A small steel rod in a laboratory test may stretch 1.8 mm under a load of 5.4 kN. Scale that up to a suspension bridge cable 300 m long carrying the same stress: the cable stretches 270 meters. At that scale, the deformation is visible from miles away. The structure must be designed to accommodate this—that's why long cables are expensive and carefully engineered.

---

## Part 7: Integration and Synthesis — Why Both Equilibrium Conditions Matter

Return to the opening image: the structural engineer walking the bridge.

She is checking equilibrium in two senses.

First, she ensures that no beam rotates uncontrollably. At the point where the suspender cable meets the box-beam, forces must balance—the upward tension from the cable plus the downward weight of the roadway plus the internal shear forces in the beam all sum to zero. This is the first equilibrium condition.

Second, she ensures that no beam twists out of its intended alignment. The cable's tension creates a torque about the beam's center. This torque must be balanced by the resistance of adjacent beams and the support structure. This is the second equilibrium condition.

Without the first condition, the bridge would accelerate. Without the second, it would spin. Both must hold, always.

And the engineer must know something more: how much of the cable's stress margin is consumed by this load, and how much is left in reserve for the next storm, the next earthquake, the next heavy truck convoy. This is where Young's modulus enters—it tells her that at this stress level, the cable is still firmly in the elastic regime, still safe.

Everything together—equilibrium, stress, and elasticity—forms the language of safe design.

---

## Part 8: Graduated Exercises

### Warm-Up

1. A person standing on a beam exerts a downward force of 800 N. The beam is supported by two pillars, one directly beneath the person, the other 3 m away. If the person is 2 m from the first pillar, what is the normal force on each pillar?

2. A rod 1.0 m long and 1.0 cm in diameter is subjected to a tensile stress of 100 MPa. If Young's modulus for the rod's material is 100 GPa, what is the elongation?

### Application

3. A uniform beam of length 4.0 m and weight 600 N is supported at both ends. A 200 N load is placed 1.0 m from the left end. Find the normal forces at each support.

4. A thick copper wire of diameter 2.0 mm and length 3.0 m hangs vertically from a ceiling and stretches 2.0 mm under its own weight plus a 50 kg load at the bottom. What is Young's modulus for copper? (Ignore the wire's weight.)

### Synthesis

5. A uniform ladder 6.0 m long and weighing 500 N leans against a wall at an angle of 60° from the horizontal floor. The wall is frictionless; the floor has friction. A 800 N worker stands 4.0 m up the ladder. Find (a) the normal force on the floor, (b) the friction force required to prevent slipping, and (c) the minimum coefficient of static friction needed.

6. A concrete column 3.0 m tall, with a cross-sectional area of 0.50 m², supports a 500 ton building. Find (a) the compressive stress in the column at the base, (b) the compressive strain, and (c) the compression of the top 1.5 m of the column. Young's modulus for concrete is 30 GPa. Also calculate the compressive stress at 1.5 m depth. Does the stress vary with position? Explain.

### Challenge

7. A uniform rod of length $L$ and mass $M$ is attached at one end to a hinge on a wall. A cable of length $\ell$ is attached to the other end of the rod and runs to a point on the wall directly above the hinge at a distance $h$ above. The rod makes an angle $\theta$ with the horizontal. Find (a) the tension in the cable, (b) the normal force at the hinge, and (c) the angle $\theta$ if the rod and cable make a 90° angle. (This is a classic statics problem with rich geometry.)

---

## Chapter Summary

**Static equilibrium** requires two independent conditions. The first, $\sum \vec{F} = \vec{0}$, ensures the center of mass does not accelerate. The second, $\sum \vec{\tau} = \vec{0}$, ensures the object does not rotate. Both must be satisfied.

When solving equilibrium problems, a free-body diagram is indispensable. It makes visible every force and torque. The choice of pivot point is strategic—pick a point where unknown forces act to zero out their torques and simplify the equations.

**Stress** is force per unit area; **strain** is fractional deformation. In the linear elastic regime, they are proportional, with the proportionality constant called the elastic modulus. For tension or compression, this is Young's modulus $Y$. The modulus is a material property—it's the same whether the sample is tiny or enormous.

**The elastic limit** is where recovery stops. Below it, deformation is temporary. Above it, the material flows plastically and permanent damage occurs. Between the proportionality limit and the elastic limit, the material is still elastic but nonlinear.

Structures are designed to stay within the elastic regime with a safety margin. This margin (the difference between the maximum stress the material can sustain and the stress it actually experiences) is what keeps bridges standing for a century and what determines the minimum cross-sectional area required for a cable, a beam, or a column.

---

## Connections Forward

**Chapter 14: Gravitation** builds on equilibrium by considering gravitational forces and orbits—situations where constant acceleration replaces static equilibrium.

**Chapter 15: Fluid Mechanics** examines pressure (stress in fluids) and its equilibrium consequences: buoyancy, hydrostatic pressure, the stability of submerged objects.

**Advanced mechanics** (not in this volume) uses the stress-strain relationships you've learned here to analyze failures, fatigue, and crack propagation—the limits of engineering.

---

## What Would Change My Mind

If evidence showed that materials do not obey Hooke's law below the elastic limit—if stress and strain were not proportional in the linear regime—then Young's modulus would not be a simple constant, and the design of structures would require much more complicated analysis.

---

## Still Puzzling

I remain uncertain about the microscopic mechanism that causes the plastic flow of metals. The dislocation model (atoms sliding past each other along crystal planes) explains much, but not everything. Under extreme stress, the story becomes more complex.

---

## Tags

static equilibrium; torque and rotation; free-body diagrams; stress and strain; Young's modulus; elastic and plastic deformation; structural engineering; bridge mechanics; material properties; Hooke's law


---

## LLM Exercise — Chapter 13: Equilibrium Solver and Beam Deflection

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A solver for static-equilibrium problems (sum of forces = 0, sum of torques = 0), plus stress-strain calculations for elastic beams.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 13 task in the physics-simulation-toolkit. Static equilibrium
is the engineering problem behind every standing structure. Build the
solver and verify on canonical cases.

In `chapters/ch13_equilibrium/`:

1. `simulations.py`:
   - `class RigidBody2D` — a rigid body in 2D with applied forces and
     applied torques. Each applied force has a position relative to
     a reference point.
   - `solve_equilibrium(body, unknowns)` — given a list of unknown
     forces (with directions specified, magnitudes unknown), solve
     the three 2D equilibrium equations ($\sum F_x = 0$, $\sum F_y = 0$,
     $\sum \tau = 0$) for the unknowns. Use `numpy.linalg.solve`.
   - `stress(force, area)` — $\sigma = F/A$.
   - `strain(delta_length, original_length)` — $\varepsilon = \Delta L / L$.
   - `youngs_modulus(stress, strain)` — $E = \sigma / \varepsilon$.
   - `beam_deflection_simple(length, load, E, I_cross)` — analytical
     deflection $\delta = \frac{FL^3}{48EI}$ for a simply-supported
     beam with central load.
   - `cross_section_inertia(width, height)` — rectangular cross-
     section moment of area, $I = \frac{wh^3}{12}$.

2. `test_simulations.py`:
   - Seesaw: two children of masses $m_1$ and $m_2$ at distances $d_1$
     and $d_2$ from a pivot. Verify the solver returns $m_1 d_1 = m_2 d_2$
     as the balance condition.
   - Ladder against wall: a ladder of length L and mass M leaning at
     angle $\theta$ on a frictional floor and frictionless wall. Solve
     for the minimum $\mu$ that prevents slipping. Verify against the
     analytical answer $\mu_{\min} = \frac{1}{2\tan\theta}$.
   - Cantilever beam: a 1-meter steel beam (E = 200 GPa, rectangular
     cross-section 2 cm × 5 cm) with a 50 kg load at the end. Compute
     the deflection at the tip. Verify against the analytical
     cantilever formula.

3. `benchmarks.py` — for the simply-supported beam, sweep cross-
   section geometries (rectangular, hollow, I-beam approximation).
   Plot stiffness (load/deflection) vs. cross-section material per
   unit length. The I-beam advantage should be clear.

4. `README.md` — decision cards. "Surprising findings": the I-beam
   advantage in stiffness-per-unit-mass; quantify it on your specific
   geometries.

Commit as `ch13: equilibrium solver and beam-deflection
verification`.
```

**What this produces:** An equilibrium solver that handles seesaws, ladders, and trusses; stress-strain calculations; a beam-deflection benchmark that shows the engineering payoff of cross-section choice.

**How to adapt this prompt:**

- *For your own project:* Real structural analysis uses finite-element methods (FEM). This exercise builds intuition for what FEM software is doing under the hood.
- *For ChatGPT / Gemini:* Both work. The ladder problem is a classic; verify the friction-angle relation by hand.
- *For Claude Code:* Native fit. Let it draw the equilibrium free-body diagrams as matplotlib figures.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 6 Force types, Ch 11 moment-of-inertia infrastructure (now applied to cross-sections).

**Preview of next chapter:** Chapter 14 builds orbital mechanics — Kepler's laws verified empirically, two-body simulation, and the geometry of orbits from $F = Gm_1m_2/r^2$.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Sophie Germain** was the 1816 prize-winning theory of vibrating elastic plates — submitted three times to the Paris Academy of Sciences (1811, 1813, 1816), the third entry winning the Prix extraordinaire de mathématiques — and her later work on Fermat's Last Theorem — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Sophie Germain, and how does their work on the theory of vibrating elastic plates and Germain's three submissions to the Paris Academy connect to static equilibrium and the elastic behavior of materials, especially plates and shells? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Sophie Germain"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe Germain's specific 1816 prize-winning argument about vibrating plates and how she derived the governing biharmonic equation
- Ask: "Germain was self-taught, corresponded with Gauss under the male pseudonym Monsieur LeBlanc, and was eventually denied honors (including a Sorbonne degree). What did Gauss say when he learned LeBlanc was Sophie Germain?"
- Add the constraint: "Answer using one piece of mathematics from her plate theory (the biharmonic equation, the fourth-order derivative term) and explain what it physically represents"

What changes? What gets better? What gets worse?
