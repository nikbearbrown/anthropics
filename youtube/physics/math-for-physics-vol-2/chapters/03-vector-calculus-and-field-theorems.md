# Vector Calculus: Gradient, Divergence, Curl, and the Field Theorems

*Electromagnetism is unintelligible without this. Maxwell's four equations are four sentences in the language of $\nabla$.*

## The cold open: the field everywhere, from the charge anywhere

Open an electromagnetism book and you meet Coulomb's law: a point charge $q$ produces an electric field of magnitude $E = q/(4\pi\varepsilon_0 r^2)$ at distance $r$, pointing radially. Fine for one charge. But the book quickly wants the field of a *uniformly charged sphere*, or an infinite charged plane, or a long charged wire, and adding up Coulomb contributions by integration becomes a nightmare of vector components and awkward integrals.

Then the book pulls a rabbit from a hat. It writes **Gauss's law** — the total electric flux out through *any* closed surface equals the enclosed charge divided by $\varepsilon_0$:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0},$$

and for the charged sphere it draws an imaginary spherical surface around the charge, argues that by symmetry $\mathbf{E}$ must be radial and constant in magnitude over that surface, pulls $E$ out of the integral, and gets the field in two lines. The same trick handles the plane and the wire. Later the book writes the *same* law in a completely different-looking form, $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$, and asserts the two are equivalent "via the divergence theorem." It does the analogous thing for the magnetic laws using something called Stokes' theorem, and out of four such equations derives that light is an electromagnetic wave travelling at $c = 1/\sqrt{\mu_0\varepsilon_0}$.

None of this is doable — none of it is even *readable* — without vector calculus: the operator $\nabla$ in its three guises (gradient, divergence, curl), integrals over curves, surfaces, and volumes, and the two great theorems (Gauss's and Stokes') that connect a field inside a region to its behavior on the boundary. This chapter builds that language and then, in the return, converts Maxwell's integral laws into their differential form exactly as the E&M book assumes you can.

## The tool, named

Volume 1 gave you single-variable calculus and basic vector algebra — the dot product, the cross product, components, magnitudes. We assume those. The advanced electromagnetism course (and fluid dynamics, and the Laplacian at the door of quantum mechanics) requires the fusion of the two into **vector calculus**: the idea of a **field** (a number or a vector assigned to every point of space), the differentiation *of* fields by the operator $\nabla$ — appearing as the **gradient** $\nabla f$, the **divergence** $\nabla\cdot\mathbf{F}$, the **curl** $\nabla\times\mathbf{F}$, and the **Laplacian** $\nabla^2 f$ — the integration of fields over **lines, surfaces, and volumes**, and the two integral theorems, the **divergence (Gauss) theorem** and **Stokes' theorem**, that tie a derivative integrated over a region to the field on the region's boundary. The decisive new idea is that $\nabla$ is one object wearing three hats, depending on what it acts on and how. This Gibbs–Heaviside vector calculus — assembled in the 1880s–90s by Josiah Willard Gibbs and, independently, by the self-taught telegraph engineer Oliver Heaviside specifically to make Maxwell's equations tractable — is what the physics books use, so it is what we teach.

## Development and derivation

### Scalar and vector fields

A **scalar field** assigns a number to every point: temperature $T(x,y,z)$ in a room, the electrostatic potential $V(x,y,z)$, air pressure. A **vector field** assigns a vector to every point: the electric field $\mathbf{E}(x,y,z)$, the velocity of a flowing fluid, the gravitational field. Vector calculus is the differential and integral calculus of these fields. Everything reduces to one symbol, the **del** operator,

$$\nabla \equiv \hat{\mathbf{x}}\,\frac{\partial}{\partial x} + \hat{\mathbf{y}}\,\frac{\partial}{\partial y} + \hat{\mathbf{z}}\,\frac{\partial}{\partial z},$$

a vector whose components are differentiation instructions. It does nothing until it is given something to act on, and it can act in three ways.

### The gradient — del acting on a scalar

Let $\nabla$ multiply a scalar field $f$ component by component:

$$\nabla f = \left(\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y},\ \frac{\partial f}{\partial z}\right).$$

This is the **gradient**, a *vector* built from a *scalar*. Its meaning: from the total differential $df = (\partial f/\partial x)dx + (\partial f/\partial y)dy + (\partial f/\partial z)dz = \nabla f\cdot d\mathbf{r}$, the change in $f$ for a small step $d\mathbf{r}$ is the dot product $\nabla f\cdot d\mathbf{r} = |\nabla f|\,|d\mathbf{r}|\cos\theta$. This is largest when $d\mathbf{r}$ points along $\nabla f$, so **the gradient points in the direction of steepest increase of $f$, and its magnitude is that rate of increase.** Steps perpendicular to $\nabla f$ leave $f$ unchanged: the gradient is normal to the level surfaces $f = \text{const}$. In electrostatics the electric field is (minus) the gradient of the potential, $\mathbf{E} = -\nabla V$ — the field points downhill on the potential landscape.

### The divergence — del dotted into a vector

Let $\nabla$ take the dot product with a vector field $\mathbf{F} = (F_x, F_y, F_z)$:

$$\nabla\cdot\mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}.$$

This is the **divergence**, a *scalar* built from a *vector*. Its meaning is **net outflux per unit volume** — the degree to which the field "spreads out from" a point. To see this, take a tiny box of sides $dx, dy, dz$ centered at a point. The flux of $\mathbf{F}$ out of the two faces perpendicular to $x$ is $[F_x(x+\tfrac{dx}{2}) - F_x(x-\tfrac{dx}{2})]\,dy\,dz \approx (\partial F_x/\partial x)\,dx\,dy\,dz$. Adding the analogous contributions from the $y$ and $z$ faces, the total outward flux is $(\nabla\cdot\mathbf{F})\,dV$. So $\nabla\cdot\mathbf{F}$ is the source density: positive where field lines are born (a source), negative where they die (a sink), zero where they merely pass through. This box argument is the seed of the divergence theorem.

A graphical warning the physics-education research stresses: field lines getting *denser* is not the same as field lines *originating*. A field can crowd together (e.g., funneling through a constriction) with zero divergence if nothing is created there. Divergence is about sources, not about density of lines.

### The curl — del crossed into a vector

Let $\nabla$ take the cross product with $\mathbf{F}$:

$$\nabla\times\mathbf{F} = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\[2pt] \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\[4pt] F_x & F_y & F_z \end{vmatrix} = \left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z},\ \frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x},\ \frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right).$$

This is the **curl**, a *vector* built from a *vector*. Its meaning is **circulation per unit area** — the local rotation of the field. If you placed a tiny paddlewheel in the field, the curl points along its axis of spin and its magnitude is twice the angular rate. A field with $\nabla\times\mathbf{F} = 0$ everywhere is **irrotational**; recall from Chapter 2 that this is exactly the field-theoretic form of the exactness test: $(\partial F_y/\partial x) - (\partial F_x/\partial y) = 0$ is one component of $\nabla\times\mathbf{F} = 0$, and on a simply connected domain $\nabla\times\mathbf{F} = 0$ is equivalent to $\mathbf{F}$ being conservative — derivable from a scalar potential, $\mathbf{F} = -\nabla V$. "Conservative $\Leftrightarrow$ curl-free $\Leftrightarrow$ has a potential" is "exact $\Leftrightarrow$ state function exists" translated into fields.

![Two vector-field panels. Left, a field pointing radially outward from a point has positive divergence and is a source. Right, a field circulating around a point has nonzero curl, and a small paddlewheel drawn at its centre would spin.](images/03-vector-calculus-and-field-theorems-fig-01.png)
*Figure 3.1 — Divergence is net outflux per unit volume (a source); curl is circulation per unit area (a rotation). They measure different things.*

Another research-documented trap: not every *curving* field has curl. The field circling a current-carrying wire, $\mathbf{F}\propto \hat{\boldsymbol\phi}/r$, has *zero* curl everywhere outside the wire, despite its circular field lines, because the falloff in magnitude exactly cancels the rotation of direction. Curl is about local spin, not about whether the picture looks like a whirlpool. (An honest aside: curl as a vector is special to three dimensions — it is really an antisymmetric tensor, a "pseudovector," and does not generalize cleanly to other dimensions. The differential-forms framework handles this more gracefully; see *Where it generalizes*.)

### The Laplacian — divergence of the gradient

Compose two of the operations: take the gradient of a scalar, then the divergence of the result:

$$\nabla^2 f \equiv \nabla\cdot(\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}.$$

This is the **Laplacian**, a *scalar* built from a *scalar*. It measures how much the value of $f$ at a point differs from the average of its neighbors: $\nabla^2 f > 0$ where $f$ sits in a valley, $< 0$ on a hill, $=0$ where $f$ equals its surrounding average. It is the single most important second-order operator in physics, governing electrostatic potentials (Laplace's equation $\nabla^2 V = 0$, Poisson's $\nabla^2 V = -\rho/\varepsilon_0$), heat flow, and — with a sign and a constant — the kinetic-energy term of the Schrödinger equation in Chapter 7.

### Three operator identities

Two compositions always vanish, and one does not. **The curl of a gradient is zero**, $\nabla\times(\nabla f) = \mathbf{0}$, because it is built from differences of mixed partials like $\partial^2 f/\partial y\partial z - \partial^2 f/\partial z\partial y$, which cancel by the equality of mixed partials (Chapter 2). **The divergence of a curl is zero**, $\nabla\cdot(\nabla\times\mathbf{F}) = 0$, by the same mixed-partial cancellation. And the one that does not vanish, which we will need for the wave equation:

$$\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F},$$

the "curl of curl" identity, proved by grinding out components and recognizing the gradient-of-divergence and Laplacian pieces. Know this one cold.

### The integrals: line, surface, volume

To state the theorems we need the three integrals of a field over an extended region.

The **line integral** of $\mathbf{F}$ along a curve $C$ accumulates the component of $\mathbf{F}$ along the path: $\int_C \mathbf{F}\cdot d\mathbf{l}$. For a force, this is the work done; around a *closed* loop it is the **circulation** $\oint_C \mathbf{F}\cdot d\mathbf{l}$.

The **surface integral** (flux) of $\mathbf{F}$ through a surface $S$ accumulates the component of $\mathbf{F}$ piercing the surface: $\int_S \mathbf{F}\cdot d\mathbf{A}$, where $d\mathbf{A}$ is an area element times the outward unit normal. Through a *closed* surface this is the net **flux** $\oint_S \mathbf{F}\cdot d\mathbf{A}$. Think of water through a net: flux counts how much fluid crosses per unit time.

The **volume integral** $\int_V f\,dV$ simply sums a scalar density over a region.

### The divergence (Gauss) theorem

Recall that for a tiny box the net outward flux is $(\nabla\cdot\mathbf{F})\,dV$. Now dice a finite region $V$ into many such boxes. The flux out of each box through any *interior* face is exactly cancelled by the flux *into* the neighboring box across that shared face — interior contributions annihilate in pairs. Only the *exterior* faces, which form the boundary surface $S$ of the whole region, survive. Summing the boxes:

$$\sum_{\text{boxes}} (\nabla\cdot\mathbf{F})\,dV = \oint_S \mathbf{F}\cdot d\mathbf{A},$$

and in the limit of infinitely many boxes the sum becomes an integral:

$$\boxed{\;\int_V (\nabla\cdot\mathbf{F})\,dV = \oint_S \mathbf{F}\cdot d\mathbf{A}.\;}$$

This is the **divergence theorem** (Gauss; first general proof by Ostrogradsky in 1826, so "Gauss–Ostrogradsky" is the honest name). In words: *the integral of the divergence over a region equals the flux out through its boundary.* The sum of all the little sources inside is the net flow out across the skin. It is the device that turns Gauss's law from a statement about every surface into a statement at every point.

### Stokes' theorem

The same telescoping argument runs for circulation. Tile a surface $S$ with tiny loops. The circulation around one tiny loop is, by the meaning of curl, $(\nabla\times\mathbf{F})\cdot d\mathbf{A}$ — the curl component along the loop's normal times its area. Adjacent loops share an edge traversed in *opposite* directions, so interior edges cancel in pairs; only the outer edges survive, and they assemble into the boundary curve $C$ of the surface. Summing the loops and passing to the limit:

$$\boxed{\;\int_S (\nabla\times\mathbf{F})\cdot d\mathbf{A} = \oint_C \mathbf{F}\cdot d\mathbf{l}.\;}$$

This is **Stokes' theorem**: *the integral of the curl over a surface equals the circulation around its bounding curve.* (Its history is tangled: communicated to Stokes by William Thomson in an 1850 letter, set by Stokes as a Cambridge Smith's Prize examination question in 1854 — which Maxwell reportedly sat — and first proved in print by Hankel in 1861.) <!-- FACT-CHECK FLAG: [CONFIRMED] — see factchecks/03-vector-calculus-and-field-theorems-assertions.md (Thomson's July 1850 letter; 1854 Smith's Prize, which Maxwell sat; Hankel's 1861 first printed proof all verified) --> Both theorems are special cases of one generalized statement, $\int_{\partial\Omega}\omega = \int_\Omega d\omega$ — "the integral of a thing over a boundary equals the integral of its derivative over the interior" — the unifying idea we return to at the end.

![Two panels. Left, the divergence theorem: a volume diced into boxes whose shared interior faces cancel, leaving outward flux only on the skin, equal to the integral of the divergence inside. Right, Stokes theorem: a surface tiled by loops whose shared edges cancel, leaving circulation only on the bounding rim, equal to the integral of the curl over the surface.](images/03-vector-calculus-and-field-theorems-fig-02.png)
*Figure 3.2 — Both theorems by the same telescoping argument: interior contributions cancel in pairs, leaving only the boundary — $\int_{\partial\Omega}\omega = \int_\Omega d\omega$.*

## Worked examples

### Example 1 — Gauss's law gives Coulomb's law for a charged sphere

Take total charge $Q$ on a sphere of radius $a$, and find the field outside at radius $r > a$. The symmetry is everything: a sphere looks the same from every direction, so $\mathbf{E}$ can only point radially and can only depend on $r$, i.e. $\mathbf{E} = E(r)\,\hat{\mathbf{r}}$. Choose a *Gaussian surface* — an imaginary sphere of radius $r$ concentric with the charge. On it, $\mathbf{E}$ is everywhere parallel to $d\mathbf{A}$ (both radial) and constant in magnitude, so the flux integral collapses:

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = E(r)\oint_S dA = E(r)\,(4\pi r^2).$$

By Gauss's law this equals $Q_{\text{enc}}/\varepsilon_0 = Q/\varepsilon_0$. Solving,

$$E(r) = \frac{Q}{4\pi\varepsilon_0 r^2},$$

which is Coulomb's law — recovered in three lines, with no integration of contributions, *because symmetry let us pull $E$ out of the flux integral.* That choice — recognizing that a spherical surface makes the integral trivial — is the human judgment a symbolic calculator will not supply.

![A point charge plus Q at the centre of a dashed spherical Gaussian surface of radius r. Equal-length radial electric-field arrows pierce the sphere, constant in magnitude and parallel to the area element. A side box collapses the closed flux integral to E times four pi r squared, sets it equal to Q over epsilon zero, and solves for the Coulomb field.](images/03-vector-calculus-and-field-theorems-fig-03.png)
*Figure 3.3 — A spherical Gaussian surface matched to the symmetry makes $\mathbf{E}$ constant on it, so $\oint\mathbf{E}\cdot d\mathbf{A}=E\,4\pi r^2 = Q/\varepsilon_0$ gives Coulomb's law in three lines.* The same method gives $E\propto 1/r$ for an infinite line of charge (cylindrical Gaussian surface) and $E = $ const for an infinite charged plane (a pillbox).

### Example 2 — From integral Gauss to differential Gauss

Write the enclosed charge as a volume integral of the charge density, $Q_{\text{enc}} = \int_V \rho\,dV$, so Gauss's law reads

$$\oint_S \mathbf{E}\cdot d\mathbf{A} = \frac{1}{\varepsilon_0}\int_V \rho\,dV.$$

Now apply the divergence theorem to the left side: $\oint_S \mathbf{E}\cdot d\mathbf{A} = \int_V (\nabla\cdot\mathbf{E})\,dV$. Therefore

$$\int_V (\nabla\cdot\mathbf{E})\,dV = \int_V \frac{\rho}{\varepsilon_0}\,dV.$$

This holds for *every* region $V$, no matter how small — and two integrals that agree over every region must have equal integrands. Hence the **differential form of Gauss's law**:

$$\boxed{\;\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}.\;}$$

The integral law (a statement about whole surfaces) and the differential law (a statement at every point) are the same physics, bridged by the divergence theorem. This is precisely the equivalence the E&M book asserts and assumes you can verify.

### Example 3 — The electromagnetic wave equation from the operator identities

In source-free vacuum, Maxwell's equations (derived below) read $\nabla\cdot\mathbf{E} = 0$, $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$, and $\nabla\times\mathbf{B} = \mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$. Take the curl of Faraday's law:

$$\nabla\times(\nabla\times\mathbf{E}) = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B}) = -\mu_0\varepsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2}.$$

Now use the curl-of-curl identity on the left, $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$, and drop $\nabla\cdot\mathbf{E} = 0$:

$$-\nabla^2\mathbf{E} = -\mu_0\varepsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2} \;\Longrightarrow\; \boxed{\;\nabla^2\mathbf{E} = \mu_0\varepsilon_0\,\frac{\partial^2\mathbf{E}}{\partial t^2}.\;}$$

This is a wave equation. Comparing to the standard form $\nabla^2\mathbf{E} = (1/c^2)\,\partial^2\mathbf{E}/\partial t^2$ identifies the wave speed as $c = 1/\sqrt{\mu_0\varepsilon_0}$ — which, plugging in measured $\mu_0$ and $\varepsilon_0$, comes out to the speed of light. Light is an electromagnetic wave, and the derivation is *nothing but* the operator identities of this chapter. The single identity $\nabla\times(\nabla\times\mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$ did the decisive work.

## Return to the cold open: Maxwell's equations, integral to differential

We can now convert all four of Maxwell's laws from the integral form the *Treatise* and the E&M book state to the differential form the local physics lives in.

**Gauss for $\mathbf{E}$:** done above — $\oint_S\mathbf{E}\cdot d\mathbf{A} = Q_{\text{enc}}/\varepsilon_0$ becomes $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$ by the divergence theorem.

**Gauss for $\mathbf{B}$:** there are no magnetic charges, so the flux of $\mathbf{B}$ out of any closed surface is zero, $\oint_S\mathbf{B}\cdot d\mathbf{A} = 0$. The divergence theorem turns this into $\int_V(\nabla\cdot\mathbf{B})\,dV = 0$ for every region, hence $\nabla\cdot\mathbf{B} = 0$.

**Faraday's law:** the circulation of $\mathbf{E}$ around a loop equals minus the rate of change of magnetic flux through it, $\oint_C\mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int_S\mathbf{B}\cdot d\mathbf{A}$. Apply Stokes' theorem to the left side: $\oint_C\mathbf{E}\cdot d\mathbf{l} = \int_S(\nabla\times\mathbf{E})\cdot d\mathbf{A}$. Matching integrands over every surface,

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}.$$

**Ampère–Maxwell law:** the circulation of $\mathbf{B}$ around a loop equals $\mu_0$ times the enclosed current plus the displacement-current term, $\oint_C\mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}} + \mu_0\varepsilon_0\frac{d}{dt}\int_S\mathbf{E}\cdot d\mathbf{A}$. Stokes' theorem on the left and $I_{\text{enc}} = \int_S\mathbf{J}\cdot d\mathbf{A}$ on the right give, by the same matching-integrands argument,

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\,\frac{\partial\mathbf{E}}{\partial t}.$$

There they are, the four differential Maxwell equations:

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}, \quad \nabla\cdot\mathbf{B} = 0, \quad \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}, \quad \nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t},$$

each one obtained from its integral cousin by exactly one of the two theorems. (A bonus the operators give for free: take the divergence of the Ampère–Maxwell law. Since $\nabla\cdot(\nabla\times\mathbf{B}) = 0$ identically, the right side must vanish too, which forces $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$, the **continuity equation** expressing charge conservation. The displacement-current term $\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t$ is *required* for consistency — without it the divergence of a curl would not vanish.) The four equations are now four readable sentences: the divergence of $\mathbf{E}$ is the charge density, the divergence of $\mathbf{B}$ is zero, the curl of $\mathbf{E}$ is minus the changing $\mathbf{B}$, the curl of $\mathbf{B}$ is the current plus the changing $\mathbf{E}$. The student who owns $\nabla$ and the two theorems reads electromagnetism; the one who does not sees decoration.

## Where it generalizes

The same operator language runs every field theory. In fluid dynamics the divergence of the velocity field measures compression and the curl is the vorticity; the continuity equation $\nabla\cdot\mathbf{J} + \partial\rho/\partial t = 0$ expresses conservation of mass exactly as it expressed conservation of charge above, and reappears yet again in quantum mechanics as the conservation of probability. In heat flow, Fourier's law makes the heat current proportional to $-\nabla T$, and conservation gives the heat equation with the Laplacian $\nabla^2 T$ — the same Laplacian that, in Chapter 7, separates the Schrödinger equation into the special functions of the hydrogen atom. And the deepest generalization unifies the chapter's two theorems into one. The divergence theorem and Stokes' theorem are both instances of the **generalized Stokes theorem**

$$\int_{\partial\Omega}\omega = \int_\Omega d\omega,$$

the statement that integrating a quantity over the boundary of a region equals integrating its derivative over the interior. In that language — the calculus of *differential forms* — gradient, divergence, and curl are three faces of one operation $d$, and the cluster of theorems collapses to a single line that generalizes to any number of dimensions and is the natural setting for relativity and gauge theory. Physics still teaches the Gibbs–Heaviside vectors because they are concrete and because Maxwell's equations were tamed in them; but the unification is real, and worth knowing exists. One operator language, every field; and behind it, one theorem.

## Exercises

1. **(Computing the operators.)** For the field $\mathbf{F} = (x^2,\ xy,\ 0)$, compute $\nabla\cdot\mathbf{F}$ and $\nabla\times\mathbf{F}$ at the point $(1,1,0)$. For the scalar field $f = x^2 + y^2 + z^2$, compute $\nabla f$ and $\nabla^2 f$.

2. **(Graphical meaning.)** For each field, state by inspection whether the divergence and the curl are zero or nonzero, and justify in one phrase: (a) $\mathbf{F} = (x, y, z)$ (radial outward); (b) $\mathbf{F} = (-y, x, 0)$ (rigid rotation); (c) $\mathbf{F} = (-y, x, 0)/(x^2+y^2)$ (field circling a wire, $r\neq 0$). For (c), compute the curl explicitly and comment on the trap it illustrates.

3. **(Derivation — required.)** State the divergence theorem. Then use it to convert the integral form of Gauss's law, $\oint_S\mathbf{E}\cdot d\mathbf{A} = \frac{1}{\varepsilon_0}\int_V\rho\,dV$, into the differential form $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$, justifying carefully the step where you match integrands.

4. **(Gauss's law, symmetry.)** Use Gauss's law with an appropriate Gaussian surface to find the electric field of an infinite line charge with linear charge density $\lambda$. State explicitly which symmetry argument lets you pull $E$ out of the flux integral.

5. **(Operator identity to wave equation.)** Prove the identity $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$ for the $x$-component by direct computation. Then explain in two or three sentences how this identity, together with $\nabla\cdot\mathbf{E} = 0$, produces the electromagnetic wave equation from Maxwell's curl equations.

## Sources

- J. Willard Gibbs and E. B. Wilson, *Vector Analysis: A Text-Book for the Use of Students of Mathematics and Physics, Founded upon the Lectures of J. Willard Gibbs* (New Haven: Yale University Press, 1901).
- Oliver Heaviside, *Electromagnetic Theory*, Vol. 1 (London: The Electrician, 1893); *Electrical Papers* (1892).
- James Clerk Maxwell, *A Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873).
- C. F. Gauss (1813); M. Ostrogradsky, first general proof of the divergence theorem (presented to the Paris Academy 1826; published St. Petersburg 1831).
- George Green, *An Essay on the Application of Mathematical Analysis to the Theories of Electricity and Magnetism* (Nottingham, 1828); G. G. Stokes, Smith's Prize examination, Cambridge (1854), theorem communicated by W. Thomson in a letter of July 1850; first printed proof by H. Hankel (1861). [provenance confirmed 2026-05-30]
- M. J. Crowe, *A History of Vector Analysis* (1967) — secondary, for the notation history.
- L. Bollen, P. van Kampen, and M. De Cock, "Students' difficulties with vector calculus in electrodynamics," *Physical Review Special Topics — Physics Education Research* 11, 020129 (2015) (arXiv:1502.02830).
