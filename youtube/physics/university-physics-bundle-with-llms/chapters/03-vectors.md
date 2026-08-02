# Chapter 3 — Vectors

## TL;DR
Vectors are quantities with magnitude and direction, represented as arrows in space. You resolve them into components along coordinate axes, add them component-by-component, and combine them using dot products (measuring overlap) and cross products (measuring rotation). Three operations, three different kinds of information.

---

## Cold open: the pilot's calculation

You are sitting in the right-hand seat of a twin-engine airplane at 2,000 feet over water, heading northeast. The airspeed — the plane's speed relative to the air — reads 120 knots. But the air itself is moving. There is a wind from the northwest, 25 knots steady. Below you, the ocean's surface is flowing with the current at 1.5 knots toward the south.

The pilot needs to know the ground track: the actual path the plane is making over the water. That's not northeast at 120 knots. It's something else, because the wind has pushed the plane sideways and the current has pulled the plane downward. The pilot must *add three vectors*: the plane's velocity through the air, the wind velocity, and the current velocity.

Get this wrong and you miss the island.

---

## Learning objectives

By the end of this chapter you will be able to:

- **Represent** a vector in component form using unit vectors $\hat{i}, \hat{j}, \hat{k}$.
- **Calculate** the magnitude of a vector from its components and the angle it makes with a coordinate axis.
- **Add, subtract, and scale** vectors by working component-by-component.
- **Compute** the dot product of two vectors and interpret it geometrically as a projection and physically as work.
- **Compute** the cross product of two vectors and interpret it geometrically and physically (torque, rotational force).
- **Apply** vector operations to problems in kinematics, dynamics, and rotational motion.

## Prerequisites

Trigonometry: sine, cosine, tangent, the inverse functions. Algebra with real numbers and coordinates. Comfort with the idea that a single quantity can live on a 2D or 3D coordinate system.

## Why this chapter matters

Every quantity in mechanics with a direction — displacement, velocity, force, torque — is a vector. You cannot solve a physics problem in two or three dimensions without vector algebra. The methods in this chapter — resolving into components, adding component-by-component, recognizing when the dot product tells you about alignment and when the cross product tells you about twist — are the tools you use for the rest of this course and beyond.

---

## Concept 1 — Vectors, components, and unit vectors

### The geometry: arrows in space

A vector is a quantity with both magnitude and direction. Displacement — the change in position from one place to another — is a vector. Velocity is a vector. Force is a vector. We represent each as an arrow in space: the length of the arrow is the magnitude, the direction the arrow points is the direction of the vector.

In a coordinate system, we write a vector in *component form*: the sum of its projections onto each axis.

### 2D: breaking a vector into $x$ and $y$ components

Imagine a displacement vector $\vec{D}$ that goes 40 meters east and 30 meters north. You could report the vector in terms of its magnitude and direction: "60 meters at 37° north of east." But it's more useful to report it in components:

$$\vec{D} = 40 \text{ m (east)} + 30 \text{ m (north)}$$

To write this compactly, we introduce *unit vectors*: vectors of length 1 that point along the coordinate axes. We use $\hat{i}$ for the unit vector pointing in the +$x$ direction (east) and $\hat{j}$ for the unit vector pointing in the +$y$ direction (north). Then:

$$\vec{D} = 40 \text{ m } \hat{i} + 30 \text{ m } \hat{j}$$

or more briefly:

$$\vec{D} = (40\hat{i} + 30\hat{j}) \text{ m}$$

The coefficients 40 and 30 are the *scalar components* of the vector along the $x$ and $y$ axes. They are numbers, not vectors. The magnitudes $40\hat{i}$ and $30\hat{j}$ are the *vector components* — the actual pieces of the vector along each axis.

To find the magnitude (the length) of this vector, you use the Pythagorean theorem:

$$D = \sqrt{D_x^2 + D_y^2} = \sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50 \text{ m}$$

To find the direction angle $\theta$ (measured counterclockwise from the +$x$ axis):

$$\tan \theta = \frac{D_y}{D_x} = \frac{30}{40} = 0.75 \Rightarrow \theta = \tan^{-1}(0.75) \approx 36.9°$$

This is the specification move: a single vector can be written as an ordered pair of components, and you can move freely between (magnitude, angle) form and (components) form.

### 3D: adding the $z$ component

In three dimensions, you introduce a third unit vector $\hat{k}$ pointing in the +$z$ direction (typically upward). A displacement in 3D space becomes:

$$\vec{D} = D_x\hat{i} + D_y\hat{j} + D_z\hat{k}$$

The magnitude is:

$$D = \sqrt{D_x^2 + D_y^2 + D_z^2}$$

Pythagorean theorem, applied twice: first in the horizontal plane ($\sqrt{D_x^2 + D_y^2}$), then adding the vertical component.

### Converting from magnitude and direction to components

Suppose you know a force vector has magnitude $F = 50$ N and makes an angle $\theta = 35°$ with the horizontal. What are the components?

Use trigonometry. The component along the $x$-axis is the *adjacent* side to the angle:

$$F_x = F \cos \theta = 50 \cos 35° = 50 \times 0.819 = 41 \text{ N}$$

The component along the $y$-axis is the *opposite* side:

$$F_y = F \sin \theta = 50 \sin 35° = 50 \times 0.574 = 29 \text{ N}$$

Check: $\sqrt{41^2 + 29^2} = \sqrt{1681 + 841} = \sqrt{2522} \approx 50$. Yes.

### Worked example — a boat crossing a river

A motorboat can travel at 12 m/s through water. The boat is aimed straight across a river, which flows at 3 m/s downstream. What is the boat's velocity relative to the ground? What angle does its actual path make with the river bank?

*Given:*
- Boat velocity relative to water: $\vec{v}_{\text{boat}} = 12 \text{ m/s } \hat{j}$ (perpendicular to the bank, taking $y$ as the cross-river direction)
- River current: $\vec{v}_{\text{river}} = 3 \text{ m/s } \hat{i}$ (parallel to the bank, taking $x$ as downstream)

*The ground velocity is the vector sum:*

$$\vec{v}_{\text{ground}} = \vec{v}_{\text{boat}} + \vec{v}_{\text{river}} = 3 \hat{i} + 12 \hat{j} \text{ m/s}$$

*Magnitude:*

$$v_{\text{ground}} = \sqrt{3^2 + 12^2} = \sqrt{9 + 144} = \sqrt{153} = 12.4 \text{ m/s}$$

*Direction:*

$$\theta = \tan^{-1}\left(\frac{12}{3}\right) = \tan^{-1}(4) = 76°$$

The boat is moving at 12.4 m/s at an angle 76° to the downstream direction — nearly straight across, but pushed downstream by the current. The boat aimed for the opposite bank and got there, but 10 meters downstream from the point directly across.

### Common misconceptions

**A vector is not the same as a point.** The displacement vector $\vec{D} = 3\hat{i} + 4\hat{j}$ meters and the position vector to the point (3, 4) look the same when written in components, but they mean different things. Displacement is a change in position. Position is a location. The displacement vector can be placed anywhere on the diagram and still mean "3 units east, 4 units north."

**Components are numbers, not vectors.** $D_x = 3$ m is a scalar (a number with a unit). The vector component is $D_x\hat{i} = 3 \text{ m } \hat{i}$, which has both magnitude and direction. Students often mix these up. Be picky: scalar component for the number, vector component for the full object.

---

## Concept 2 — The dot product: measuring alignment

### The definition and its geometry

When two vectors point in similar directions, we say they are *aligned*. The *dot product* (also called the *scalar product*) measures this alignment. It takes two vectors and produces a scalar.

The geometric definition is simple: multiply the magnitudes and the cosine of the angle between them.

$$\vec{A} \cdot \vec{B} = AB \cos \varphi$$

where $\varphi$ is the angle between the vectors, $A$ is the magnitude of $\vec{A}$, and $B$ is the magnitude of $\vec{B}$.

Three cases:
- If $\varphi = 0°$ (pointing the same direction), $\cos 0° = 1$ and $\vec{A} \cdot \vec{B} = AB$ — maximum.
- If $\varphi = 90°$ (perpendicular), $\cos 90° = 0$ and $\vec{A} \cdot \vec{B} = 0$ — no alignment.
- If $\varphi = 180°$ (pointing opposite directions), $\cos 180° = -1$ and $\vec{A} \cdot \vec{B} = -AB$ — they point away.

### Computing the dot product from components

When both vectors are written in component form, the dot product is much simpler to calculate:

$$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$$

In 2D:

$$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y$$

You multiply corresponding components and add. This works because the unit vectors are orthogonal — they form a right angle with each other:

$$\hat{i} \cdot \hat{i} = 1, \quad \hat{j} \cdot \hat{j} = 1, \quad \hat{i} \cdot \hat{j} = 0$$

All the cross terms vanish when you expand the product.

### Geometric interpretation: scalar projection

The dot product has a beautiful geometric meaning. The quantity $A \cos \varphi$ is the *projection* of vector $\vec{A}$ onto the direction of $\vec{B}$. Imagine shining a light perpendicular to $\vec{B}$; the shadow $\vec{A}$ casts has length $A \cos \varphi$. Then:

$$\vec{A} \cdot \vec{B} = B \times (\text{projection of } \vec{A} \text{ onto } \vec{B})$$

This projection idea appears everywhere in physics: it's how we find the component of a force that does work, the component of a displacement that counts for a given direction, the component of a field that couples to a particle.

### Physical application: work

Work — the energy transferred by a force — is defined as the dot product of force and displacement:

$$W = \vec{F} \cdot \vec{d} = Fd \cos \varphi$$

If you push a box across the floor with a force of 50 N at an angle 20° above horizontal, and the box moves 10 meters horizontally:

$$F = 50 \text{ N}, \quad d = 10 \text{ m}, \quad \varphi = 20°$$

$$W = 50 \times 10 \times \cos 20° = 500 \times 0.94 = 470 \text{ J}$$

The full force doesn't do work. Only the component of the force parallel to the displacement does. If you pushed straight up (90°), $W = 0$ — no work, because the force is perpendicular to the motion.

### Worked example — finding the angle between two forces

Two dogs pull on a rope. The first pulls with force $\vec{F}_1 = (10\hat{i} - 20\hat{j}) \text{ N}$. The second pulls with force $\vec{F}_2 = (-15\hat{i} - 6\hat{j}) \text{ N}$. What is the angle between the forces?

*Step 1: Calculate the dot product from components.*

$$\vec{F}_1 \cdot \vec{F}_2 = (10)(-15) + (-20)(-6) = -150 + 120 = -30 \text{ N}^2$$

*Step 2: Calculate the magnitudes.*

$$F_1 = \sqrt{10^2 + (-20)^2} = \sqrt{100 + 400} = \sqrt{500} = 22.4 \text{ N}$$

$$F_2 = \sqrt{(-15)^2 + (-6)^2} = \sqrt{225 + 36} = \sqrt{261} = 16.2 \text{ N}$$

*Step 3: Use the geometric formula to find the angle.*

$$\cos \varphi = \frac{\vec{F}_1 \cdot \vec{F}_2}{F_1 F_2} = \frac{-30}{(22.4)(16.2)} = \frac{-30}{363} = -0.083$$

$$\varphi = \cos^{-1}(-0.083) = 95°$$

The forces are nearly perpendicular (which would be 90°). They're pulling in nearly independent directions.

### Common misconceptions

**The dot product is not vector subtraction.** $\vec{A} \cdot \vec{B}$ is a scalar. $\vec{A} - \vec{B}$ is a vector. They answer different questions.

**Perpendicularity means zero, not orthogonal-in-some-abstract-sense.** If $\vec{A} \cdot \vec{B} = 0$, then $\vec{A}$ and $\vec{B}$ are at right angles. Period. No alignment, no shared direction.

---

## Concept 3 — The cross product: measuring rotation

### The definition and the right-hand rule

The *cross product* (or *vector product*) of two vectors produces a third vector. Unlike the dot product, which measures how much two vectors point in the same direction, the cross product measures how much they *twist* relative to each other. It appears whenever rotation enters the picture: torque, angular momentum, the magnetic force on a moving charge.

The magnitude of the cross product is:

$$|\vec{A} \times \vec{B}| = AB \sin \varphi$$

where $\varphi$ is the angle between the vectors. The result is largest when the vectors are perpendicular ($\sin 90° = 1$) and zero when they're parallel or antiparallel ($\sin 0° = \sin 180° = 0$).

The direction of $\vec{A} \times \vec{B}$ is perpendicular to both $\vec{A}$ and $\vec{B}$, determined by the *right-hand rule*: point your right hand's fingers in the direction of $\vec{A}$, curl them toward $\vec{B}$, and your thumb points in the direction of $\vec{A} \times \vec{B}$.

Important: **the cross product is anticommutative**. Reversing the order reverses the sign:

$$\vec{B} \times \vec{A} = -(\vec{A} \times \vec{B})$$

### Computing the cross product from components

When vectors are given in component form, use the determinant formula:

$$\vec{A} \times \vec{B} = (A_yB_z - A_zB_y)\hat{i} + (A_zB_x - A_xB_z)\hat{j} + (A_xB_y - A_yB_x)\hat{k}$$

This is easier to remember as a determinant:

$$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$$

Expand along the first row.

### Cyclic order of the unit vectors

The cross products of the unit vectors follow a cyclic pattern:

$$\hat{i} \times \hat{j} = \hat{k}, \quad \hat{j} \times \hat{k} = \hat{i}, \quad \hat{k} \times \hat{i} = \hat{j}$$

Reverse the order and you get the negative:

$$\hat{j} \times \hat{i} = -\hat{k}, \quad \hat{k} \times \hat{j} = -\hat{i}, \quad \hat{i} \times \hat{k} = -\hat{j}$$

Any unit vector crossed with itself is zero: $\hat{i} \times \hat{i} = 0$.

### Physical application: torque

Torque is the rotational analogue of force. When a force $\vec{F}$ is applied at a distance $\vec{r}$ from a pivot point, the torque is:

$$\vec{\tau} = \vec{r} \times \vec{F}$$

The magnitude is $\tau = rF \sin \varphi$, where $\varphi$ is the angle between the position vector and the force vector. Maximum torque occurs when the force is perpendicular to the lever arm ($\sin 90° = 1$). The direction tells you which way the object will spin.

For a wrench tightening a nut: if the position vector from the nut to your hand is $\vec{r} = 0.25 \text{ m } \hat{j}$ and you pull with a force $\vec{F} = 50 \text{ N } \hat{i}$ (perpendicular to the handle), then:

$$\vec{\tau} = (0.25 \text{ m } \hat{j}) \times (50 \text{ N } \hat{i}) = 0.25 \times 50 \times (\hat{j} \times \hat{i}) = 12.5 \text{ N·m } (-\hat{k})$$

The negative sign indicates the nut rotates clockwise (when viewed from above). The magnitude, 12.5 N·m, is how much rotational effort you apply.

### Worked example — magnetic force on a moving charge

A charged particle moves through a magnetic field. The magnetic force is $\vec{F} = q\vec{v} \times \vec{B}$, where $q$ is the charge, $\vec{v}$ is the velocity, and $\vec{B}$ is the magnetic field. A proton moving east at 5.0 × 10⁶ m/s enters a magnetic field pointing upward at 1.5 T. What is the magnitude and direction of the force? (For a proton, $q = 1.6 \times 10^{-19}$ C.)

*Step 1: Set up the vectors.*

Taking east as $+\hat{i}$ and up as $+\hat{k}$:

$$\vec{v} = (5.0 \times 10^6) \hat{i} \text{ m/s}$$

$$\vec{B} = 1.5 \hat{k} \text{ T}$$

*Step 2: Calculate the cross product.*

$$\vec{v} \times \vec{B} = (5.0 \times 10^6 \hat{i}) \times (1.5 \hat{k}) = 5.0 \times 10^6 \times 1.5 \times (\hat{i} \times \hat{k})$$

Using the cyclic rule: $\hat{i} \times \hat{k} = -\hat{j}$.

$$\vec{v} \times \vec{B} = 7.5 \times 10^6 \times (-\hat{j}) = -7.5 \times 10^6 \hat{j} \text{ m/(s·T)}$$

*Step 3: Calculate the force.*

$$\vec{F} = q(\vec{v} \times \vec{B}) = (1.6 \times 10^{-19}) \times (-7.5 \times 10^6 \hat{j}) = -1.2 \times 10^{-12} \hat{j} \text{ N}$$

The magnitude is $1.2 \times 10^{-12}$ N and the direction is southward (negative $\hat{j}$). The particle curves to the south.

### Common misconceptions

**The cross product is not commutative.** $\vec{A} \times \vec{B} \neq \vec{B} \times \vec{A}$. They differ by a sign. This matters for torque and angular momentum, where the sign tells you the direction of rotation.

**Parallel vectors give zero, not undefined.** If $\vec{A} \parallel \vec{B}$, then $\vec{A} \times \vec{B} = 0$. There's no rotation. This is different from the dot product of orthogonal vectors (also zero), so don't confuse them.

---

## Integration and synthesis

You now have three tools for combining vectors:

1. **Vector addition** (component-by-component): combines displacements, velocities, forces. Tells you the net effect in each direction.

2. **Dot product** (magnitude times cosine of angle): measures overlap or alignment. Used for work, power, projections. Always gives a scalar.

3. **Cross product** (magnitude times sine of angle, with direction from right-hand rule): measures rotation. Used for torque, angular momentum, magnetic force. Always gives a vector perpendicular to both inputs.

In the airplane problem from the opening: you use vector addition to find the ground velocity. You'd use the dot product to find how much of the plane's velocity is directed toward the airport. You'd use the cross product to find the torque if the plane's propellers were spinning — or the magnetic force if the plane flew near a pulsar's intense magnetic field.

The trade-off across these operations: addition is straightforward but requires working in components; dot product tells you alignment instantly but loses directional information by producing a scalar; cross product tells you the axis of rotation but only works in 3D.

---

## Worked examples and exercises

### Warm-up exercises

1. A displacement vector has components $\vec{D} = (8\hat{i} + 6\hat{j})$ m. What is the magnitude of this displacement? At what angle from the +$x$ axis does it point?

2. Two force vectors are $\vec{F}_1 = (10\hat{i} + 5\hat{j})$ N and $\vec{F}_2 = (-3\hat{i} + 7\hat{j})$ N. Add them to find the net force $\vec{F}_{\text{net}}$. What is the magnitude of the net force?

3. A velocity vector is $\vec{v} = (3\hat{i} + 4\hat{j} + 12\hat{k})$ m/s. What is the magnitude?

### Application exercises

4. A sailboat is heading due north at 4 m/s through the water. A current flows due east at 2 m/s. What is the actual velocity relative to the ground? In what direction is the boat actually moving?

5. A force of 100 N is applied at an angle 30° above the horizontal to a box. The box is displaced 5 m horizontally. How much work is done by the force?

6. A wrench is 0.40 m long. A force of 60 N is applied perpendicular to the wrench handle at the end. What is the magnitude of the torque applied to the bolt?

### Synthesis exercises

7. Three displacement vectors are $\vec{A} = (5\hat{i})$ m, $\vec{B} = (3\hat{j})$ m, and $\vec{C} = (4\hat{k})$ m. Find $\vec{A} \cdot \vec{B}$, $\vec{B} \cdot \vec{C}$, and $\vec{A} \times \vec{B}$.

8. A particle has velocity $\vec{v} = (2\hat{i} + 3\hat{j})$ m/s and is subject to a force $\vec{F} = (10\hat{i} - 5\hat{j})$ N. What is the component of the force in the direction of motion? What is the power (rate of work) delivered to the particle?

### Challenge exercises

9. Two vectors have magnitude $A = 5$ and $B = 7$. The angle between them is 60°. (a) Find the dot product $\vec{A} \cdot \vec{B}$. (b) If you resolve both vectors onto a common direction, what is the sum of their projections?

10. A cross product $\vec{A} \times \vec{B}$ produces a vector of magnitude 10. If $|\vec{A}| = 4$, what is $|\vec{B}|$ and at what angle $\varphi$ are they oriented?

---

## Chapter summary

Vectors are quantities with magnitude and direction, represented as arrows in coordinate space. In component form, a vector is a sum of scalar multiples of unit vectors along each axis: $\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$.

Vector addition works component-by-component: $\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} + (A_z + B_z)\hat{k}$. This combines displacements, velocities, and forces.

The dot product $\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$ measures alignment: positive when vectors point the same way, zero when perpendicular, negative when opposite. Geometrically, $\vec{A} \cdot \vec{B} = AB \cos \varphi$. It produces a scalar and appears in work ($W = \vec{F} \cdot \vec{d}$) and power ($P = \vec{F} \cdot \vec{v}$).

The cross product $\vec{A} \times \vec{B} = (A_yB_z - A_zB_y)\hat{i} + (A_zB_x - A_xB_z)\hat{j} + (A_xB_y - A_yB_x)\hat{k}$ measures rotation: magnitude $AB \sin \varphi$, direction perpendicular to both vectors, determined by the right-hand rule. It produces a vector and appears in torque ($\vec{\tau} = \vec{r} \times \vec{F}$) and magnetic force ($\vec{F} = q\vec{v} \times \vec{B}$).

Etymology: *vector* from Latin *vehere*, to carry; *scalar* from Latin *scalaris*, of a scale or ladder. Vectors carry direction as well as magnitude.

---

## Connections forward

Chapter 4 applies vectors to one-dimensional motion, where all quantities point along a single line. Chapter 5 extends this to two and three dimensions, where vectors reveal their full power: projectile motion cannot be solved without resolving motion into horizontal and vertical components. Newton's laws in Chapter 6 are stated in vector form. The dot product reappears in work and energy (Chapter 8), the cross product in torque and rotational motion (Chapter 10). Every chapter that follows depends on these tools.

---

## What would change my mind

If an experiment showed that force and displacement don't combine additively — that the work done by two simultaneous forces is not the sum of the individual works — this chapter's framework would need revision. We have never observed this.

## Still puzzling

Why does the cross product only work in three dimensions (and technically two)? The mathematical reason involves the geometry of rotations, but the physical intuition remains elusive to me.


---

## LLM Exercise — Chapter 3: The Vector Library

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A reusable vector library — dot product, cross product, projection, decomposition — with empirical verification of algebraic identities. Every later chapter imports this.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 3 task in the physics-simulation-toolkit. Build the vector
library every later chapter will import.

In `chapters/ch03_vectors/`:

1. `simulations.py` — implement a `Vec3` class (or use numpy arrays with
   utility functions; pick the cleaner approach for the toolkit). Provide:
   - Addition, scalar multiplication, negation
   - `dot(a, b)` — dot product
   - `cross(a, b)` — cross product
   - `magnitude(v)`, `unit(v)` — Euclidean norm and normalization
   - `angle_between(a, b)` — uses `acos(dot/magprod)` with safe clipping
     to [-1, 1] for numerical edge cases
   - `project_onto(a, b)` — projection of a onto b
   - `decompose(v, basis)` — decompose v into components along an
     orthonormal basis

   Carry units through using the Chapter 2 `Units` module — vectors of
   positions, velocities, forces should all have correct units.

2. `test_simulations.py` — verify the algebraic identities empirically
   on random vectors (use `hypothesis` if available):
   - `dot(a, b) == dot(b, a)` (commutativity)
   - `cross(a, b) == -cross(b, a)` (anti-commutativity)
   - `dot(a, cross(b, c)) == dot(b, cross(c, a)) == dot(c, cross(a, b))`
     (scalar triple product)
   - `cross(a, cross(b, c)) == b * dot(a, c) - c * dot(a, b)` (BAC-CAB)
   - `|a + b|^2 == |a|^2 + 2*dot(a,b) + |b|^2` (cosine rule)

   For each, generate 1000 random vector triples and verify the
   identity holds within floating-point tolerance.

3. `benchmarks.py` — compare your implementation to direct `numpy`
   operations. The unit-carrying overhead should be modest (<2x) for
   typical 3-component vectors.

4. `README.md` — populate with the vector library's interface, a
   one-paragraph statement of why algebraic identities matter
   (they're the structural facts every later chapter assumes), and
   the worked example: verify the right-hand rule for cross products
   on the standard basis vectors $\hat{i} \times \hat{j} = \hat{k}$.

Commit as `ch03: vector library with verified algebraic identities`.
```

**What this produces:** A unit-aware `Vec3` interface, five algebraic identity tests verified on random inputs, a benchmark, and a README with the right-hand rule worked out. Every later chapter imports this.

**How to adapt this prompt:**

- *For your own project:* If you prefer numpy arrays over a custom class, the trade-off is unit-tracking — `pint` plays better with simple wrappers than with numpy. Choose deliberately.
- *For ChatGPT / Gemini:* Both work for the math. Verify cross-product implementations with hand-checked cases.
- *For Claude Code:* Native fit. Let it run the property tests on 1000 random samples.
- *For Cowork:* Useful if you want the test outputs saved to a markdown report.

**Connection to previous chapters:** Imports `Units` from Chapter 2.

**Preview of next chapter:** Chapter 4 implements 1D kinematics with proper numerical integration — RK4 versus Euler — and verifies the constant-acceleration kinematics equations empirically against numerical solutions.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Josiah Willard Gibbs** was the development of modern vector analysis — his Yale lecture notes *Elements of Vector Analysis* (1881–1884) gave us the dot product, the cross product, and the vector calculus every later chapter of this book uses — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Josiah Willard Gibbs, and how does their work on the development of modern vector calculus as distinct from Hamilton's quaternions connect to vectors and the algebra of physical quantities with direction? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Josiah Willard Gibbs"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to compare Gibbs's vector calculus to Hamilton's quaternions — what was the same, what was different, and why Gibbs's notation won
- Ask: "Gibbs spent his entire career at Yale, refused offers from Johns Hopkins, and published in obscure journals. How did his ideas spread internationally despite that?"
- Add the constraint: "Answer using one specific identity (e.g., $\vec{a} \times (\vec{b} \times \vec{c}) = \vec{b}(\vec{a}\cdot\vec{c}) - \vec{c}(\vec{a}\cdot\vec{b})$) and trace how Gibbs's notation made it computable"

What changes? What gets better? What gets worse?
