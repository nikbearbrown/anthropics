# Vectors and Vector Algebra

*Quantities with direction — and the two operations, alignment and twist, that make them computable.*

## Cold open: the pilot who is not going where the nose points

You are in the right seat of a twin-engine airplane at 2,000 feet, the nose pointed northeast, the airspeed indicator reading 120 knots. But the air itself is moving — a 25-knot wind from the northwest — and the plane flies through that moving air, so its path over the ground is *not* northeast at 120 knots. To find where the plane is actually going, the pilot must combine two quantities that each have a magnitude *and* a direction: the plane's velocity through the air, and the wind's velocity. Adding their magnitudes ($120 + 25$) is meaningless; adding them as arrows is the whole problem.

This is the situation that ordinary numbers cannot handle. A speed is a number; a *velocity* is a number with a direction, and directions do not add like numbers. You need a mathematical object built to carry direction, and a set of operations that respect it. That object is the **vector**, and this chapter builds the algebra that makes vectors computable — including the two operations, the dot product and the cross product, that answer the two questions you will ask of directed quantities for the rest of your studies: *how much do they align?* and *how much do they twist?*

## The tool, named

A **vector** is a quantity with both magnitude and direction, drawn as an arrow. The chapter develops four things:

1. **Components and unit vectors** — writing a vector as a sum of pieces along chosen axes, so that arrows become computable.
2. **Addition and scaling** — combining vectors component by component.
3. **The dot product** — a number measuring how much two vectors *align* (projection).
4. **The cross product** — a vector measuring how much two vectors *twist* (oriented area and rotation), special to three dimensions.

The notation we use — separate dot and cross products, with unit vectors $\hat{\imath}, \hat{\jmath}, \hat{k}$ — was *engineered*, not handed down: it comes from J. Willard Gibbs's Yale lectures, written up by E. B. Wilson in *Vector Analysis* (1901), who split Hamilton's quaternion product into its scalar and vector parts. The deeper meaning of the cross product traces to Hermann Grassmann's *Ausdehnungslehre* (1844), and we will use his insight to explain *why* the cross product behaves as it does.

## Development and derivation

### Components and unit vectors

To compute with arrows, anchor them to axes. Define **unit vectors** — vectors of length exactly 1 — pointing along each axis: $\hat{\imath}$ along $x$, $\hat{\jmath}$ along $y$, $\hat{k}$ along $z$. Any vector is then a sum of scaled unit vectors:

$$\vec{A} = A_x\,\hat{\imath} + A_y\,\hat{\jmath} + A_z\,\hat{k},$$

where the *scalar components* $A_x, A_y, A_z$ are plain numbers — the amount of the vector along each axis. (Components from a magnitude and an angle, $A_x = A\cos\theta$ and $A_y = A\sin\theta$, are exactly the decomposition built in Chapter 3.) The **magnitude** recovers the arrow's length by the Pythagorean theorem, applied twice in 3D:

$$A = |\vec{A}| = \sqrt{A_x^2 + A_y^2 + A_z^2}.$$

The unit vector is the single most difficult concept for students entering this material (Nguyen & Meltzer, 2003), so it is worth stating plainly: $\hat{\imath}$ is not the $x$-axis and not the number 1 — it is *an arrow of length one pointing in the $x$ direction*, a pure carrier of direction. Any vector divided by its own magnitude, $\hat{A} = \vec{A}/|\vec{A}|$, is the unit vector pointing the same way.

### Addition and scaling

Vectors add component by component — which is the algebraic form of the tip-to-tail picture (slide the second arrow's tail to the first arrow's tip; the sum runs from start to finish):

$$\vec{A} + \vec{B} = (A_x + B_x)\hat{\imath} + (A_y + B_y)\hat{\jmath} + (A_z + B_z)\hat{k}.$$

Scaling by a number $c$ stretches every component (and the magnitude) by $c$: $c\vec{A} = cA_x\hat{\imath} + cA_y\hat{\jmath} + cA_z\hat{k}$. Subtraction is addition of the negative, $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$ — a routine source of sign errors, because the difference arrow points *from* the tip of $\vec{B}$ *to* the tip of $\vec{A}$. The discipline that prevents most vector mistakes: keep the arrow picture and the component arithmetic side by side, never one without the other.

### The dot product: deriving the alignment–angle link

The **dot product** of two vectors produces a *number*. From components it is dead simple:

$$\vec{A}\cdot\vec{B} = A_xB_x + A_yB_y + A_zB_z.$$

But its meaning is geometric, and we can derive that meaning. First, the unit vectors: because they are mutually perpendicular and of length 1,

$$\hat{\imath}\cdot\hat{\imath} = 1, \quad \hat{\jmath}\cdot\hat{\jmath} = 1, \quad \hat{\imath}\cdot\hat{\jmath} = 0,$$

(a vector dotted with itself gives its length-squared; perpendicular unit vectors give zero). Now expand $\vec{A}\cdot\vec{B}$ using these and all cross terms vanish, leaving the component formula above — so the component formula is *built from* the geometry, not separate from it.

To connect it to the angle, dot a vector with itself: $\vec{A}\cdot\vec{A} = A_x^2 + A_y^2 + A_z^2 = |\vec{A}|^2$. Then apply the law of cosines (Chapter 3) to the triangle formed by $\vec{A}$, $\vec{B}$, and $\vec{A}-\vec{B}$, whose included angle is $\varphi$:

$$|\vec{A}-\vec{B}|^2 = |\vec{A}|^2 + |\vec{B}|^2 - 2|\vec{A}||\vec{B}|\cos\varphi.$$

Expand the left side as a dot product, $|\vec{A}-\vec{B}|^2 = (\vec{A}-\vec{B})\cdot(\vec{A}-\vec{B}) = |\vec{A}|^2 - 2\,\vec{A}\cdot\vec{B} + |\vec{B}|^2$. Setting the two expressions equal, the $|\vec{A}|^2$ and $|\vec{B}|^2$ cancel, and:

$$\boxed{\,\vec{A}\cdot\vec{B} = |\vec{A}||\vec{B}|\cos\varphi\,.}$$

This is the alignment law. Read it: the dot product is largest when the vectors are parallel ($\cos 0 = 1$), zero when they are perpendicular ($\cos 90° = 0$), negative when they point apart. Geometrically, $|\vec{A}|\cos\varphi$ is the **projection** — the shadow — of $\vec{A}$ onto the direction of $\vec{B}$, so the dot product is "the length of $\vec{B}$ times how much of $\vec{A}$ lies along it." And it gives you the angle between any two vectors for free: $\cos\varphi = (\vec{A}\cdot\vec{B})/(|\vec{A}||\vec{B}|)$.

![Two vectors A and B from a common origin with angle φ; a perpendicular dropped from the tip of A onto the line of B marks the projection |A|cosφ, and a side panel reads the sign of A·B at φ = 0, 90°, and beyond.](images/04-vectors-and-vector-algebra-fig-02.png)
*Figure 4.2 — The dot product is a shadow: A·B = |A||B|cosφ measures how much of A lies along B.*

### The cross product: deriving the area–twist link

The **cross product** $\vec{A}\times\vec{B}$ produces a *vector*. From components it is the determinant

$$\vec{A}\times\vec{B} = \begin{vmatrix}\hat{\imath} & \hat{\jmath} & \hat{k}\\ A_x & A_y & A_z\\ B_x & B_y & B_z\end{vmatrix} = (A_yB_z - A_zB_y)\hat{\imath} + (A_zB_x - A_xB_z)\hat{\jmath} + (A_xB_y - A_yB_x)\hat{k}.$$

Its magnitude is

$$|\vec{A}\times\vec{B}| = |\vec{A}||\vec{B}|\sin\varphi,$$

and here is what that *is*: $|\vec{B}|\sin\varphi$ is the height of the parallelogram spanned by $\vec{A}$ and $\vec{B}$ when $\vec{A}$ is its base, so $|\vec{A}||\vec{B}|\sin\varphi$ is the **area of that parallelogram**. The cross product magnitude is an oriented area. It is largest when the vectors are perpendicular (maximal twist, biggest parallelogram) and zero when they are parallel (no area, no twist). This is Grassmann's insight: the fundamental object is the *oriented area* the two vectors sweep out.

The *direction* of $\vec{A}\times\vec{B}$ is perpendicular to both, given by the **right-hand rule**: fingers point along $\vec{A}$, curl toward $\vec{B}$, thumb gives the result. And here is the honest subtlety that the mnemonic hides: the right-hand rule is a *choice of orientation*, a convention about how we encode an area as a perpendicular arrow — not a law of nature. (The result is technically a *pseudovector*, and the trick of representing an oriented area by a perpendicular vector only works in three dimensions; in Grassmann's framework the area is the real object and lives in any dimension.) `[contested — see pantry]` This is why the cross product is *anticommutative*:

$$\vec{B}\times\vec{A} = -(\vec{A}\times\vec{B}),$$

curling the other way flips the thumb. The unit vectors obey a cyclic pattern, $\hat{\imath}\times\hat{\jmath} = \hat{k}$, $\hat{\jmath}\times\hat{k} = \hat{\imath}$, $\hat{k}\times\hat{\imath} = \hat{\jmath}$, and any unit vector crossed with itself is zero.

![Two vectors A and B spanning a shaded parallelogram of area |A||B|sinφ, with height |B|sinφ marked and the cross product A×B drawn as an arrow out of the plane by the right-hand rule; a panel notes B×A = −(A×B).](images/04-vectors-and-vector-algebra-fig-03.png)
*Figure 4.3 — The cross product magnitude is the oriented area the two vectors span; the right-hand rule is a convention for encoding that area as a perpendicular arrow.*

The pair is the whole chapter: **dot = alignment (a number), cross = twist/oriented area (a vector).** Choosing which one a problem needs is the skill.

## Worked examples

### Example 1 — Work as a dot product

Push a box with a force $\vec{F}$ of 50 N directed $20°$ above the horizontal, while it slides 10 m horizontally ($\vec{d}$). The work done is the dot product — *only the part of the force along the motion counts*:

$$W = \vec{F}\cdot\vec{d} = |\vec{F}||\vec{d}|\cos\varphi = (50)(10)\cos 20° = 470\ \text{J}.$$

Read the geometry: if you pushed straight *up* ($\varphi = 90°$), then $\cos 90° = 0$ and $W = 0$ — no work, because none of the force lies along the motion. This is exactly why a centripetal force, always perpendicular to the velocity, does no work and cannot change a body's speed. The dot product makes "how much of this force acts along the motion" into a single computable number.

### Example 2 — Torque as a cross product

Tighten a nut with a wrench. Your hand is at position $\vec{r} = 0.25\,\hat{\jmath}$ m from the nut and pulls with force $\vec{F} = 50\,\hat{\imath}$ N. The turning effect is the torque, a cross product:

$$\vec{\tau} = \vec{r}\times\vec{F} = (0.25\,\hat{\jmath})\times(50\,\hat{\imath}) = 0.25\cdot 50\,(\hat{\jmath}\times\hat{\imath}) = 12.5\,(-\hat{k})\ \text{N·m}.$$

The magnitude $12.5$ N·m is the area of the parallelogram spanned by lever arm and force; the $-\hat{k}$ direction (into the page, by the right-hand rule) says the nut turns clockwise. Note that torque is *largest when force is perpendicular to the lever arm* (full $\sin 90°$) and *zero when you pull straight along the wrench* (no twist) — the twist interpretation made physical.

### Example 3 — Finding the angle between two forces

Two dogs pull a rope with forces $\vec{F}_1 = (10\hat{\imath} - 20\hat{\jmath})$ N and $\vec{F}_2 = (-15\hat{\imath} - 6\hat{\jmath})$ N. What angle separates their pulls? Use the dot product as the angle-finder:

$$\vec{F}_1\cdot\vec{F}_2 = (10)(-15) + (-20)(-6) = -150 + 120 = -30,$$
$$|\vec{F}_1| = \sqrt{10^2 + 20^2} = 22.4, \quad |\vec{F}_2| = \sqrt{15^2 + 6^2} = 16.2,$$
$$\cos\varphi = \frac{-30}{(22.4)(16.2)} = -0.083 \;\Rightarrow\; \varphi = \cos^{-1}(-0.083) \approx 95°.$$

The slightly negative dot product tells you at a glance — before computing the angle — that the forces are *just past perpendicular*, pulling in nearly independent directions. Reading the sign of the dot product is faster than computing the angle and often all you need.

## Return to the cold open

The pilot's problem is pure vector addition. Set up axes (east $= \hat{\imath}$, north $= \hat{\jmath}$). The plane's airspeed of 120 knots toward the northeast ($45°$) resolves into components $120\cos45°\,\hat{\imath} + 120\sin45°\,\hat{\jmath} \approx 84.9\,\hat{\imath} + 84.9\,\hat{\jmath}$. A wind *from* the northwest blows *toward* the southeast, i.e. toward $(+\hat{\imath}, -\hat{\jmath})$ at $25$ knots: $25\cos(-45°)\hat{\imath} + 25\sin(-45°)\hat{\jmath} \approx 17.7\,\hat{\imath} - 17.7\,\hat{\jmath}$. Add component by component:

$$\vec{v}_{\text{ground}} \approx (84.9 + 17.7)\hat{\imath} + (84.9 - 17.7)\hat{\jmath} = 102.6\,\hat{\imath} + 67.2\,\hat{\jmath}\ \text{knots}.$$

The ground speed is $|\vec{v}_{\text{ground}}| = \sqrt{102.6^2 + 67.2^2} \approx 123$ knots, at heading $\tan^{-1}(67.2/102.6) \approx 33°$ north of east — *not* the northeast ($45°$) the nose points, and *not* 120 knots.

![Tip-to-tail vector addition on east-north axes: the plane's airspeed vector (NE) plus the wind vector (toward SE) gives a ground velocity of about 123 knots at roughly 33° north of east.](images/04-vectors-and-vector-algebra-fig-01.png)
*Figure 4.1 — Velocities add as arrows, component by component; the wind pushes the plane south of its heading and slightly speeds it up.* The wind has pushed the plane south of its heading and slightly sped it up. You could only get this by treating the velocities as arrows and adding their components — the exact operation ordinary numbers cannot perform. Miss it, and you miss the island.

## Where it generalizes

The dot product is everywhere a notion of *alignment* matters. In machine learning, "cosine similarity" between two data vectors is literally the normalized dot product $\cos\varphi = \vec{A}\cdot\vec{B}/(|\vec{A}||\vec{B}|)$ — the same formula derived above, repurposed to ask how similar two documents or images are. In graphics it decides how brightly a surface is lit (the dot product of light direction and surface normal). The cross product governs every rotation, every magnetic force ($\vec{F} = q\vec{v}\times\vec{B}$), every angular momentum ($\vec{L} = \vec{r}\times\vec{p}$); Kepler's law that a planet sweeps equal areas in equal times is the statement that $\tfrac{1}{2}|\vec{r}\times\vec{v}|$ is constant — the area interpretation made into a conservation law.

A solver will compute a dot or cross product instantly and even draw the arrows. So what is left for you? *Choosing the right operation* — is this an alignment question or a twist question? — *choosing the coordinate frame*, and *reading the geometric meaning*: a near-zero dot product means "nearly perpendicular"; a large cross product means "strongly twisting." That interpretation is the transferable skill, and it is exactly what the computation does not supply. The right-hand rule is the clean cautionary tale: a student who memorizes it as a rule misses that the cross product secretly encodes an oriented area and only *looks* like a vector because we live in three dimensions. Learn the meaning, not the mnemonic. (Vectors are the heart of Part II's calculus: in Chapter 7 you will differentiate vector-valued functions to get velocity and acceleration, and the full vector calculus — gradient, divergence, curl, and the integral theorems electromagnetism needs — is the project of **Volume 2**.)

## Exercises

1. **(Components)** A displacement is $\vec{D} = 8\hat{\imath} + 6\hat{\jmath}$ m. Find its magnitude and the angle it makes with the $x$-axis.

2. **(Add)** Find $\vec{F}_1 + \vec{F}_2$ for $\vec{F}_1 = 10\hat{\imath} + 5\hat{\jmath}$ N and $\vec{F}_2 = -3\hat{\imath} + 7\hat{\jmath}$ N, and give the magnitude of the resultant.

3. **(Dot vs. cross)** For $\vec{A} = 3\hat{\imath} + 4\hat{\jmath}$ and $\vec{B} = 4\hat{\imath} - 3\hat{\jmath}$, compute $\vec{A}\cdot\vec{B}$ and $|\vec{A}\times\vec{B}|$. What does each result tell you about the angle between them?

4. **(Derivation)** Derive $\vec{A}\cdot\vec{B} = |\vec{A}||\vec{B}|\cos\varphi$ from the law of cosines, showing every cancellation. Then explain in one sentence why this makes the dot product the natural tool for finding work.

5. **(Cross product as area)** Two vectors have magnitudes $|\vec{A}| = 4$ and $|\vec{B}| = 7$ with a $30°$ angle between them. Find the area of the parallelogram they span, and state the magnitude of $\vec{A}\times\vec{B}$. Why are these the same number?

## Sources

- E. B. Wilson, *Vector Analysis* (1901), founded on the lectures of J. Willard Gibbs.
- Hermann Grassmann, *Die lineale Ausdehnungslehre* (1844) — the exterior/wedge product (oriented area).
- W. R. Hamilton, quaternions (1843); M. J. Crowe, *A History of Vector Analysis* (1967).
- Oliver Heaviside, vector reformulation of Maxwell's equations (1880s).
- T. Nguyen & D. E. Meltzer, "Initial understanding of vector concepts among students in introductory physics courses," *American Journal of Physics* 71, 630 (2003).
