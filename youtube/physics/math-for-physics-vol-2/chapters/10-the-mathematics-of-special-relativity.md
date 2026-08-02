# The Mathematics of Special Relativity

*Hyperbolic functions and rapidity, the Lorentz transformation as a matrix, four-vectors and the Minkowski metric, invariants, and light-cone geometry — the geometry that makes relativity computable.*

---

## 1. Cold open: the light beam you cannot catch

You are in a spaceship moving at $0.9c$ — nine-tenths the speed of light — chasing a pulse of light that left ahead of you. Common sense says you are closing the gap: the light recedes from you at $c - 0.9c = 0.1c$, a tenth of light speed, and with enough time you might gain on it. You measure the speed of the receding pulse. It is moving away from you at $c$. Not $0.1c$. The full $c$.

Speed up to $0.99c$. Measure again. Still $c$. There is no speed you can reach at which the light slows down relative to you, because the speed of light is the same in *every* inertial frame — that is the experimental fact, confirmed first by Michelson and Morley's failure to detect any "ether wind" in 1887 and a thousand times since. The modern-physics book states the consequences: moving clocks run slow, moving rulers contract, and velocities do not simply add. It writes down the relativistic velocity-addition formula,
$$
u = \frac{v + u'}{1 + vu'/c^2},
$$
and shows that plugging in $u' = c$ gives $u = c$ for *any* $v$ — light's speed is a fixed point. But the formula looks like a patch. Why *that* combination? Why does adding velocities behave like nothing else you add? And why do four separate "relativistic effects" — time dilation, length contraction, velocity addition, $E = mc^2$ — keep showing up together, as if they were one thing?

They are one thing. This chapter shows that a Lorentz boost is a *rotation* — not in space, but in spacetime — and that once you see it that way, the velocity-addition formula is just the rule for adding angles, time dilation and length contraction are just the components of a rotated vector, and the whole confusing list collapses into a single geometric picture preserving a single quantity: the invariant interval.

---

## 2. The tool, named

Volume 1 gave you two things this chapter needs: the trigonometry of rotations in the plane, and the algebra of complex numbers and exponentials. Volume 2's Chapter 4 gave you matrices. The new ingredient is a small one — the **hyperbolic functions** $\cosh$ and $\sinh$ — and the recognition that with them, a change of inertial frame is *the same kind of operation* as a rotation, differing only by a sign in the metric.

The plan:
1. Derive the **Lorentz transformation** from the single requirement that $c$ is invariant.
2. Re-express it as a **hyperbolic rotation**, introducing **rapidity** as the relativistic analogue of an angle.
3. Show that velocity addition is rapidity *addition* — angles add, velocities don't.
4. Introduce the **invariant interval** and the **Minkowski metric**, the "length" that every observer agrees on.
5. Build **four-vectors** and read off $E^2 = (pc)^2 + (mc^2)^2$ and the **light cone**.

A note on convention before we start: we use the metric signature $(-,+,+,+)$, so the squared interval is $\Delta s^2 = -c^2\Delta t^2 + \Delta x^2$. Particle physicists often use the opposite, $(+,-,-,-)$; the physics is identical, only signs of $\Delta s^2$ flip. We will state ours once and hold it.

The deepest difficulty in this material, the one the education research flags over and over, is *not* the algebra. It is **frame bookkeeping** — keeping straight *whose* clock and *whose* ruler measures *which* quantity. A symbolic solver will compute $\gamma$ for you all day; it will not tell you whose clock runs slow. Hold that question — *who measures what?* — in front of every calculation.

---

## 3. Development and derivation

### 3.1 The Lorentz transformation from the invariance of $c$

Two observers, $S$ and $S'$, with $S'$ moving at speed $v$ along the shared $x$-axis. We want the linear map relating their coordinates $(t,x)$ and $(t',x')$. Linearity is forced by the homogeneity of space and time (no point is special), so write
$$
x' = \gamma\,(x - v t), \qquad t' = \gamma\,(t - \alpha x),
$$
with constants $\gamma, \alpha$ to be fixed. (The $y,z$ coordinates, transverse to the motion, are unchanged: $y'=y$, $z'=z$.) The first equation just says the origin of $S'$, at $x = vt$, sits at $x' = 0$. Now impose the one physical fact: a light pulse leaving the common origin at $t=t'=0$ travels at $c$ in *both* frames, so $x = ct$ in $S$ must correspond to $x' = ct'$ in $S'$.

Substitute $x = ct$ into both equations and demand $x' = ct'$:
$$
\gamma(ct - vt) = c\,\gamma(t - \alpha c t) \;\Longrightarrow\; c - v = c - \alpha c^2 \;\Longrightarrow\; \alpha = \frac{v}{c^2}.
$$
So the time equation is $t' = \gamma(t - vx/c^2)$. To fix $\gamma$, use the **principle of relativity**: the inverse transformation (from $S'$ back to $S$) must have the identical form but with $v \to -v$, since $S$ moves at $-v$ relative to $S'$. Writing the inverse and composing it with the forward map must return the identity. Substituting $x'$ and $t'$ into $x = \gamma(x' + vt')$ and requiring consistency gives
$$
\gamma^2\left(1 - \frac{v^2}{c^2}\right) = 1 \;\Longrightarrow\; \boxed{\;\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.\;}
$$
The **Lorentz factor**. Assembling everything, the **Lorentz boost** along $x$ is
$$
\begin{aligned}
ct' &= \gamma\,(ct - \tfrac{v}{c}\,x),\\
x' &= \gamma\,(x - \tfrac{v}{c}\,ct),
\end{aligned}
\qquad\text{or in matrix form}\qquad
\begin{pmatrix} ct' \\ x' \end{pmatrix}
=
\begin{pmatrix} \gamma & -\gamma\beta \\ -\gamma\beta & \gamma \end{pmatrix}
\begin{pmatrix} ct \\ x \end{pmatrix},
$$
where $\beta \equiv v/c$. We have used $ct$ and $x$ as coordinates so both axes carry the same units (length) and the matrix is symmetric. Notice it required *only* the invariance of $c$ and the principle of relativity. No ether, no patch — the transformation is forced.

### 3.2 The boost is a hyperbolic rotation: rapidity

Look hard at that matrix. A rotation by angle $\theta$ in the ordinary plane is
$$
\begin{pmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{pmatrix},
$$
which preserves $x^2 + y^2$ and satisfies $\cos^2\theta + \sin^2\theta = 1$. The boost matrix has the same skeleton, but with a crucial sign: from $\gamma^2 - (\gamma\beta)^2 = \gamma^2(1-\beta^2) = 1$, the diagonal and off-diagonal entries satisfy a *difference* of squares equal to 1, not a sum. The functions that satisfy $\cosh^2\phi - \sinh^2\phi = 1$ are the **hyperbolic** ones. So define an angle-like parameter $\phi$, the **rapidity**, by
$$
\boxed{\;\tanh\phi = \beta = \frac{v}{c}.\;}
$$
Then $\gamma = \cosh\phi$ and $\gamma\beta = \sinh\phi$ (check: $\cosh^2 - \sinh^2 = 1$ matches $\gamma^2 - \gamma^2\beta^2 = 1$, and $\tanh\phi = \sinh\phi/\cosh\phi = \gamma\beta/\gamma = \beta$). The boost becomes
$$
\begin{pmatrix} ct' \\ x' \end{pmatrix}
=
\begin{pmatrix} \cosh\phi & -\sinh\phi \\ -\sinh\phi & \cosh\phi \end{pmatrix}
\begin{pmatrix} ct \\ x \end{pmatrix}.
$$
This is a rotation — a **hyperbolic rotation** — through the imaginary-feeling angle $\phi$. Minkowski saw it in 1908; Robb named $\phi$ "rapidity" in 1911. A boost is to spacetime exactly what an ordinary rotation is to the plane, with $\cos\to\cosh$, $\sin\to\sinh$, and a single sign flip in the metric. Every relativistic effect is now a statement about a rotated coordinate frame.

![Spacetime diagram with the unprimed ct and x axes in grey, the boosted primed axes in brown tilting toward the 45 degree light line by the rapidity angle, and red invariant hyperbolas along which an event slides while its interval is preserved](images/10-the-mathematics-of-special-relativity-fig-02.png)
*Figure 10.2 — A Lorentz boost as a hyperbolic rotation: the primed axes tilt symmetrically toward the light line by rapidity φ, and events slide along the invariant hyperbolas −c²t² + x² = const.*

### 3.3 Velocity addition is rapidity addition

Why is the velocity-addition formula so strange? Because velocities are not the natural thing to add — *rapidities* are. Compose two collinear boosts: first by rapidity $\phi_1$, then by $\phi_2$. Multiply the two hyperbolic-rotation matrices. Just as composing two ordinary rotations adds their angles, composing two hyperbolic rotations adds their rapidities (the hyperbolic angle-addition identities are the same as the trig ones):
$$
\begin{pmatrix}\cosh\phi_2 & -\sinh\phi_2\\ -\sinh\phi_2 & \cosh\phi_2\end{pmatrix}
\begin{pmatrix}\cosh\phi_1 & -\sinh\phi_1\\ -\sinh\phi_1 & \cosh\phi_1\end{pmatrix}
=
\begin{pmatrix}\cosh(\phi_1+\phi_2) & -\sinh(\phi_1+\phi_2)\\ -\sinh(\phi_1+\phi_2) & \cosh(\phi_1+\phi_2)\end{pmatrix}.
$$
So $\phi_{\text{total}} = \phi_1 + \phi_2$ — **rapidities add linearly.** Now translate back to velocities using $\beta = \tanh\phi$ and the hyperbolic tangent addition formula:
$$
\beta_{\text{total}} = \tanh(\phi_1 + \phi_2) = \frac{\tanh\phi_1 + \tanh\phi_2}{1 + \tanh\phi_1\tanh\phi_2} = \frac{\beta_1 + \beta_2}{1 + \beta_1\beta_2}.
$$
Multiply through by $c$ and there is the velocity-addition formula, $u = (v + u')/(1 + vu'/c^2)$ — not a patch, but the image of simple addition seen through the $\tanh$ function. And because $\tanh$ saturates at 1 as its argument grows, *no sum of rapidities, however large, ever gives $\beta > 1$.* You can add velocities forever and never reach $c$. That is the resolution of the cold open, in one line of hyperbolic trigonometry.

![A curve of beta equals tanh of rapidity rising linearly near the origin then bending over toward the horizontal red asymptote at beta equals one, with two marked points showing that adding two 0.75c rapidities yields 0.96c](images/10-the-mathematics-of-special-relativity-fig-03.png)
*Figure 10.3 — β = tanh φ: rapidities add linearly under boosts, but tanh saturates at 1, so velocity approaches c without ever reaching it (0.75c "+" 0.75c = 0.96c).*

### 3.4 The invariant interval and the Minkowski metric

A rotation preserves length. What does a hyperbolic rotation preserve? Compute, using the boost equations:
$$
-(ct')^2 + (x')^2 = -\gamma^2(ct - \beta x)^2 + \gamma^2(x - \beta ct)^2.
$$
Expand and collect (the cross terms cancel):
$$
= \gamma^2\big[(1-\beta^2)x^2 - (1-\beta^2)c^2t^2\big] = \gamma^2(1-\beta^2)\big(x^2 - c^2t^2\big) = x^2 - c^2t^2,
$$
since $\gamma^2(1-\beta^2)=1$. So the quantity
$$
\boxed{\;\Delta s^2 = -c^2\Delta t^2 + \Delta x^2 + \Delta y^2 + \Delta z^2\;}
$$
is **invariant** — every inertial observer computes the same $\Delta s^2$ between two events, even though they disagree about $\Delta t$ and $\Delta x$ separately. This is the spacetime "distance," and it is the thing that does not change under a boost the way ordinary distance does not change under a rotation. We can package it with the **Minkowski metric**
$$
\eta_{\mu\nu} = \mathrm{diag}(-1, +1, +1, +1), \qquad \Delta s^2 = \sum_{\mu\nu}\eta_{\mu\nu}\,\Delta x^\mu \Delta x^\nu,
$$
where $x^\mu = (ct, x, y, z)$ is the position **four-vector** (index $\mu = 0,1,2,3$). The Lorentz group is *exactly* the set of linear maps that leave $\Delta s^2$ invariant — boosts and ordinary rotations together. Relativity is the geometry of this metric.

The historically minded should note Minkowski's original trick of writing time as $ict$, which makes $\Delta s^2 = (ict)^2 + x^2$ look like an ordinary Euclidean sum. It is a convenient fiction that hides the genuine *indefiniteness* of the metric (the minus sign is physical — it is why time is different from space) and breaks down in general relativity. We use the real metric with its honest minus sign.

### 3.5 Four-vectors, the energy–momentum relation, and the light cone

Anything that transforms under a boost like $(ct, x, y, z)$ is a **four-vector**, and its "length" $\sum\eta_{\mu\nu}A^\mu A^\nu$ is then automatically invariant. The most important one after position is the **energy–momentum four-vector**:
$$
p^\mu = \left(\frac{E}{c},\; p_x,\; p_y,\; p_z\right).
$$
Its invariant length is the same in every frame, and evaluating it in the rest frame (where $\vec p = 0$ and $E = mc^2$) fixes its value:
$$
-\left(\frac{E}{c}\right)^2 + \vec p^{\,2} = -\left(mc\right)^2 \;\Longrightarrow\; \boxed{\;E^2 = (pc)^2 + (mc^2)^2.\;}
$$
The single most-used relation in particle physics is just the statement *the length of the energy–momentum four-vector is the rest mass.* Set $\vec p = 0$ and recover $E = mc^2$; set $m = 0$ and recover $E = pc$ for light.

Finally, the **light cone**. The sign of $\Delta s^2$ between two events is invariant and classifies their relationship:
- $\Delta s^2 < 0$ (**timelike**): a massive particle can travel between them; their time order is the same for all observers — cause can precede effect.
- $\Delta s^2 = 0$ (**null / lightlike**): only light connects them; they lie *on* the cone.
- $\Delta s^2 > 0$ (**spacelike**): no signal can connect them; their time order is frame-dependent, and no causal influence can pass.

The light cone is the geometric statement of "nothing outruns light": causal influence stays inside the cone. This structure is what relativistic quantum field theory's microcausality is built on.

![A Minkowski spacetime diagram of ct versus x with two 45 degree red null lines forming the light cone, dividing the plane into future and past timelike regions and a spacelike elsewhere, with a vertical stationary worldline and a tilted moving-observer worldline inside the cone](images/10-the-mathematics-of-special-relativity-fig-01.png)
*Figure 10.1 — The light cone in a Minkowski diagram: inside the cone is timelike (causally reachable), outside is spacelike (no signal connects), and massive worldlines always stay inside.*

---

## 4. Worked examples

### Example 1 — The muon that should not reach the ground

Cosmic-ray collisions create muons high in the atmosphere. A muon's rest-frame lifetime is $\tau_0 = 2.2\ \mu\text{s}$; traveling at $0.99c$, in that time it would cover only $ct \approx 0.99 \times (3\times10^8)\times(2.2\times10^{-6}) \approx 650$ m before decaying. Yet muons made at $15$ km altitude reach sea level in abundance. Two descriptions, one invariant.

*Earth frame.* The muon's clock runs slow by $\gamma = 1/\sqrt{1 - 0.99^2} \approx 7.1$. Its lifetime in our frame is $\gamma\tau_0 \approx 15.6\ \mu\text{s}$, in which it travels $0.99c \times 15.6\ \mu\text{s} \approx 4.6$ km — actually we need the full atmospheric depth, and at slightly higher $\gamma$ the muons cover the $15$ km. *Who measures what:* the short lifetime $\tau_0$ is the **proper time**, measured by the muon's own clock; the long $\gamma\tau_0$ is what *we* measure.

*Muon frame.* The muon's clock reads only $\tau_0 = 2.2\ \mu\text{s}$ — but the atmosphere, rushing past at $0.99c$, is **length-contracted** to $15\ \text{km}/\gamma \approx 2.1$ km, which it can cross in its short lifetime. Same survival, different bookkeeping.

The reconciliation is the invariant interval: both observers compute the *same* $\Delta s^2$ between "muon created" and "muon hits ground," and from it the muon's own elapsed (proper) time $\Delta\tau = \sqrt{-\Delta s^2}/c$ comes out the same $2.2\ \mu\text{s}$ for everyone. The proper time belongs to the muon; the interval belongs to all.

### Example 2 — Velocity addition, the easy way

Two spaceships approach Earth from opposite sides, each at $0.75c$ in Earth's frame. How fast does one see the other approach? Naive addition gives $1.5c$ — impossible. Use rapidities: $\beta = 0.75 \Rightarrow \phi = \tanh^{-1}(0.75) \approx 0.973$. The relative rapidity is $\phi_1 + \phi_2 \approx 1.946$, so $\beta_{\text{rel}} = \tanh(1.946) \approx 0.96$. The ships approach each other at $0.96c$ — below $c$, as it must be. The same answer follows from $(0.75+0.75)/(1+0.75^2) = 1.5/1.5625 = 0.96$, but the rapidity route makes *why it stays under $c$* obvious: $\tanh$ can never exceed 1.

### Example 3 — Why $E = mc^2$ is a statement about a four-vector's length

A particle of mass $m$ has total energy $E = \gamma mc^2$ and momentum $p = \gamma mv$. Verify the invariant directly:
$$
E^2 - (pc)^2 = \gamma^2 m^2 c^4 - \gamma^2 m^2 v^2 c^2 = \gamma^2 m^2 c^4\left(1 - \frac{v^2}{c^2}\right) = m^2c^4,
$$
using $\gamma^2(1 - v^2/c^2) = 1$. The frame-dependent $E$ and $p$ conspire so that $E^2 - (pc)^2$ is the *same* $m^2c^4$ in every frame — the rest energy is the length of the four-momentum. This is why colliding-beam experiments quote the invariant mass: it is the one number all observers agree on.

---

## 5. Return to the cold open

You cannot catch the light beam, and now you know why in geometric terms. Chasing the beam means boosting your frame — performing a hyperbolic rotation by some rapidity $\phi$. But the light pulse lives *on the light cone*, where $\Delta s^2 = 0$, and a hyperbolic rotation slides events along the invariant hyperbolas without ever moving a null direction off the cone. The light's worldline makes a $45°$ angle in the spacetime diagram, and no boost — no rapidity, however large — tilts a $45°$ line. In velocity language: your rapidity adds to the light's, but light's "rapidity" is infinite ($\tanh\phi \to 1$), and adding any finite rapidity to it changes nothing. So the pulse recedes at $c$ from every chaser.

The four effects that looked separate are one rotation. Time dilation and length contraction are the time- and space-components of a boosted vector. Velocity addition is rapidity addition pushed through $\tanh$. And $E = mc^2$ is the length of the energy–momentum four-vector. One geometry, one invariant interval, preserved by one kind of rotation — that is the whole of special relativity's mathematics.

---

## 6. Where it generalizes

- **Relativistic electromagnetism.** The electric and magnetic fields are components of one antisymmetric **field tensor** $F^{\mu\nu}$; what one observer calls a pure $\vec E$ field, another (boosted) observer sees as a mix of $\vec E$ and $\vec B$. Maxwell's equations, written with $F^{\mu\nu}$ and the four-gradient $\partial_\mu$, are manifestly the same in every frame. This is *why* the electromagnetism book ultimately needs the metric and four-vectors.
- **Relativistic quantum mechanics.** The Klein–Gordon and Dirac equations are *built* from the requirement of Lorentz invariance; the Minkowski metric and the four-gradient $\partial_\mu$ are their grammar.
- **General relativity.** The flat Minkowski metric here becomes a curved metric $g_{\mu\nu}(x)$; gravity is the curvature of the same spacetime, and the invariant interval becomes the line element of a curved geometry. (This is why we kept the honest minus sign and avoided the $ict$ trick — it does not survive into curved spacetime.)
- **Everyday technology.** GPS satellites carry atomic clocks that must be corrected for time dilation continuously, or navigation errors would accumulate at kilometers per day. The geometry of this chapter is in your phone.

The judgment no solver supplies is the **frame bookkeeping**: deciding which observer measures the proper time, which measures the contracted length, and recognizing that the interval — and only the interval — is shared by all. Compute $\gamma$ with a machine; decide *whose clock it slows* with your head.

---

## Exercises

1. **(The key derivation.)** Derive the Lorentz boost matrix from scratch: assume linearity, impose that a light pulse $x = ct$ maps to $x' = ct'$, and fix $\gamma$ by requiring the inverse transformation to have the same form with $v\to -v$. State explicitly where each physical assumption enters.

2. **(Rapidity.)** Show that $\gamma = \cosh\phi$ and $\gamma\beta = \sinh\phi$ follow from $\tanh\phi = \beta$, and verify $\cosh^2\phi - \sinh^2\phi = 1$ is equivalent to $\gamma^2(1-\beta^2) = 1$. Then derive the velocity-addition formula from $\beta_{\text{tot}} = \tanh(\phi_1 + \phi_2)$.

3. **(Invariance.)** Starting from the boost equations, prove algebraically that $-c^2t^2 + x^2$ is unchanged, i.e. $-c^2t'^2 + x'^2 = -c^2t^2 + x^2$. Then explain in words why this is the spacetime analogue of "a rotation preserves length."

4. **(Four-momentum.)** A pion of mass $m$ decays at rest into two photons. Use conservation of the energy–momentum four-vector and the invariant $E^2 = (pc)^2 + (mc^2)^2$ to find the energy of each photon. (Hint: the total four-momentum before and after is equal in *every* frame.)

5. **(Causality.)** Two events have $\Delta x = 4$ light-seconds and $\Delta t = 3$ seconds. Compute $\Delta s^2$. Are they timelike, spacelike, or null separated? Can one cause the other? Could a different inertial observer see them in the opposite time order?

---

## Sources

- A. Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* 17 (1905) — the Lorentz transformation, time dilation, length contraction, and velocity addition from two postulates.
- H. Minkowski, "Raum und Zeit" ("Space and Time"), Cologne address 1908 (published 1909) — spacetime as a four-dimensional geometry and the boost as a rotation.
- A. A. Robb, *Optical Geometry of Motion* (1911) — coined "rapidity"; É. Borel (1913) developed the hyperbolic kinematic geometry in parallel. [verify Borel citation]
- H. A. Lorentz (1904) and the FitzGerald–Lorentz contraction (1889/1892) — the transformation equations as a pre-Einstein ether hypothesis.
- A. A. Michelson and E. W. Morley (1887) — the null result motivating the invariance of $c$.
- Standard modern treatments for the mathematics: E. F. Taylor and J. A. Wheeler, *Spacetime Physics* (rapidity, invariant interval); W. Rindler, *Introduction to Special Relativity* (four-vectors, the metric); C. W. Misner, K. S. Thorne, and J. A. Wheeler, *Gravitation* (index/metric notation).
- In-series: *Physics — Modern Physics* ch. 01 (Michelson–Morley, time dilation, the muon, GPS corrections; "this is not a trick about signal travel times") and ch. 09 (velocity addition, the spacetime interval, "what is invariant").
