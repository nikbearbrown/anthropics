# Chapter 4 — Electric Potential

*The scalar shortcut to the electric field, and the energy that lives in a difference of volts.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define electric potential $V$ at a point as work per unit charge, distinguish it from potential energy $U = qV$, and explain why only differences $\Delta V$ are physically meaningful.
2. **(Apply)** Compute $V$ for a single point charge ($V = kq/r$) and for a collection of point charges by scalar superposition.
3. **(Apply)** Recover $\vec{E}$ from $V$ via $\vec{E} = -\nabla V$; in particular, get $E_x = -dV/dx$ on a symmetry axis.
4. **(Apply)** Compute the potential of a continuous distribution by $V = \int k\, dq/r$ — worked through for a uniformly charged ring.
5. **(Analyze)** Sketch equipotential surfaces for simple configurations and verify that field lines cross them perpendicularly.
6. **(Apply)** Build a potential-surface visualizer that color-maps $V(x,y)$, overlays equipotential contours, and draws $\vec{E}$ arrows as the numerical gradient.

---

## Opening case: the volt itself

On 20 March 1800, Alessandro Volta wrote a letter to Sir Joseph Banks, the President of the Royal Society in London, describing a device he had built out of alternating discs of zinc, silver, and brine-soaked cardboard. Stack the discs in a tower, touch a wire to the top and another to the bottom, and a steady current flows. No spinning glass globes, no Leyden jars, no rubbing — just chemistry holding the two ends of the stack at different electrical states. The letter was published later that year in the *Philosophical Transactions* ([Volta 1800](https://doi.org/10.1098/rstl.1800.0018)). The device became the **voltaic pile**, the first practical battery, and the start of the electrical revolution that produced the telegraph, the dynamo, and eventually the smartphone in your pocket.

The quantity Volta's pile maintains between its two terminals is the one this chapter is about. Eighty-one years later, at the 1881 International Electrical Congress in Paris, the world's electricians agreed to call its SI unit the **volt** in his honor. A AA battery says "1.5 V" on the label. A wall outlet in the US is "120 V." A defibrillator paddle, "1500 V." A high-voltage power line, "500 kV." The Large Hadron Collider's proton beams sit at the energy a proton would acquire from a potential difference of 6.8 trillion volts, which is why we say each LHC beam runs at 6.8 TeV ([CERN, "LHC Run 3"](https://home.cern/news/news/accelerators/lhc-run-3-physics-record-energy)).

Every one of these numbers names the same physical quantity: **the work the electric field would do per unit charge to move a charge from one point to another.** A 1.5 V battery delivers 1.5 joules of work for every coulomb of charge it pushes through your flashlight bulb. A 6.8 TeV proton has that kinetic energy because it was accelerated across a sequence of potential differences that summed, in effect, to 6.8 trillion volts.

The volt is not new physics. It is a reshaping of the physics we already have. Chapter 3 gave us $\vec{E}$ — a vector at every point. This chapter introduces $V$ — a single number at every point — and shows that the vector field is hiding inside the scalar field as its gradient. The reshaping is dramatic: most problems that look hard in $\vec{E}$ become arithmetic in $V$.

---

## Core concept

### Why a scalar potential exists: the conservative force argument

Take a test charge $q_0$ and move it from point A to point B along some path. The work done by the electric force is

$$W_{A \to B} = q_0 \int_A^B \vec{E} \cdot d\vec{\ell}$$

Here is the load-bearing fact: **for an electrostatic field, this integral does not depend on the path you choose.** Two different routes from A to B give the same work. Equivalently, the work done going around any closed loop is zero. Equivalently, the **curl** of $\vec{E}$ vanishes everywhere:

$$\nabla \times \vec{E} = 0 \quad \text{(electrostatics)}$$

Why is this true? Look at a single point charge $q$ at the origin. Its field is radial: $\vec{E} = (kq/r^2)\hat{r}$. Decompose any path from A to B into tiny radial steps (along $\hat{r}$) and tiny tangential steps (perpendicular to $\hat{r}$). The radial steps contribute $E_r\, dr$; the tangential steps contribute zero because $\vec{E} \cdot d\vec{\ell} = 0$ there. So the integral collapses to a one-dimensional integral over $r$:

$$\int_A^B \vec{E} \cdot d\vec{\ell} = \int_{r_A}^{r_B} \frac{kq}{r^2}\, dr = kq\left(\frac{1}{r_A} - \frac{1}{r_B}\right)$$

Only the endpoints survive. The path between them was irrelevant. By superposition, every static distribution of charges is a sum of point charges, each of which is path-independent, so the whole field is path-independent.

Once a vector field has zero curl on a simply connected region, a theorem of vector calculus says it must be the gradient of a scalar function. We give that scalar a name and a sign:

$$\boxed{\;\vec{E} = -\nabla V\;}$$

The minus sign is convention but it pays off: $V$ becomes potential energy per unit charge, and a positive charge "rolls downhill" in $V$.

A piece of bookkeeping worth flagging. Chapter 3 gave you $\nabla \cdot \vec{E} = \rho/\varepsilon_0$ — the divergence equation. This chapter gives you $\nabla \times \vec{E} = 0$ — the curl equation. These are *independent* facts. Gauss's law tells you where the field comes from; the curl-free condition tells you that field lines never loop back on themselves in electrostatics. You need both to fully specify $\vec{E}$. (In Chapter 10 we will watch the curl-free condition break when magnetic fields change with time — that breakage is Faraday's law. For now, electrostatics, and the gradient relation holds.)

### Defining the potential

The **electric potential difference** between A and B is the work per unit charge to move a test charge from A to B, against the field:

$$V_A - V_B = -\int_A^B \vec{E} \cdot d\vec{\ell}$$

Units: joules per coulomb, given the name **volt**. One volt is one joule of work per coulomb.

To get an absolute $V$ at a point, you need a reference. The convention for isolated finite charge distributions is $V(\infty) = 0$. For circuit problems, "ground" — whatever node you decide to call zero. The reference is a bookkeeping choice; it shifts $V$ everywhere by a constant but changes no observable. If I add a million volts to $V$ everywhere in this room, nothing measurable changes. The fields are the same. The forces are the same. The currents through every wire are the same. **Only differences $\Delta V$ have physical meaning.**

The companion quantity is **electric potential energy**:

$$U = qV$$

$V$ is a property of the field (intensive — joules per coulomb). $U$ is a property of a particular charge sitting in the field (extensive — joules). Confusing the two is the most common student error in this material, and the cure is to write the relation $U = qV$ at the top of every problem until it becomes reflex.

### Potential of a point charge

Pick a point charge $q$ at the origin. Use $V(\infty) = 0$ as reference. Integrate $\vec{E}$ from infinity inward along a radial path:

$$V(r) = -\int_\infty^r \frac{kq}{r'^2}\, dr' = \left[\frac{kq}{r'}\right]_\infty^r = \frac{kq}{r}$$

$$\boxed{\;V(r) = \frac{kq}{r}\;}$$

The potential falls as $1/r$, not $1/r^2$ like the field. The reason is the same as the reason gravitational potential is $-GM/r$ while gravitational field is $-GM/r^2$: integrating an inverse-square law gives an inverse-linear answer. The potential has "one more power of $r$" than the field, by the same algebra as $\int dx/x^2 = -1/x$.

You can run the gradient backwards to check: $-dV/dr = -d(kq/r)/dr = kq/r^2 = E_r$. The field comes back.

### Scalar superposition — the chapter's payoff

For a collection of $N$ point charges $q_i$ at positions $\vec{r}_i$, the potential at field point $\vec{r}$ is

$$V(\vec{r}) = \sum_i \frac{k q_i}{|\vec{r} - \vec{r}_i|}$$

**Each term is a scalar.** No unit vectors. No vector components to track. Compute a distance, do a divide, do a multiply, add. Move to the next charge.

Compare to computing $\vec{E}$ at the same point. For each charge you compute a distance, do a divide, do a multiply, *and* find three components of a unit vector $\hat{r}_i$, *and* multiply through, *and* add as vectors. The vector field route does roughly three times the arithmetic and triple the chances of a sign error.

If you actually need $\vec{E}$, the cheaper route is: compute $V$ (scalars), then differentiate. The vector machinery gets absorbed into one final $\nabla$ at the end instead of being carried through every term.

Concrete check. Two equal positive charges $+q$ sit at $(\pm a, 0)$. At the midpoint between them, $V = 2kq/a$ — just sum two scalars. The field at the midpoint is zero by symmetry. Both facts are correct and not in conflict. $V$ is large; the *gradient* of $V$ at the midpoint is zero because it is a saddle point of the potential landscape. **$V$ at a point and $\vec{E}$ at the same point have no fixed relationship beyond the derivative.**

### Equipotential surfaces

An **equipotential surface** is the locus of points where $V$ has a single value. Topographic maps work this way — the contour lines are level sets of altitude. The same picture applies here.

Three properties drop out immediately:

1. **Moving a charge along an equipotential costs no work.** No $\Delta V$, no $\Delta U$.
2. **Field lines are perpendicular to equipotentials.** The gradient of a scalar always points perpendicular to its level sets — a multivariable calculus fact. Since $\vec{E} = -\nabla V$, the field is perpendicular to constant-$V$ surfaces.
3. **The surface of a conductor in electrostatic equilibrium is an equipotential.** From Chapter 3: $\vec{E} = 0$ inside the conductor, so $V$ is constant throughout. The surface inherits that constant value.

Some geometries to keep in mind:

- **Single point charge:** equipotentials are concentric spheres around the charge. Tighter near the charge (because $V \sim 1/r$ — equal $V$ steps need exponentially closer spheres as $r$ shrinks).
- **Electric dipole** (a $+q$ and $-q$ pair): the plane perpendicular to the dipole axis through the midpoint is the $V = 0$ equipotential. The other equipotentials wrap around each charge, distorted on the side facing the other charge.
- **Parallel plates** with a uniform field: the equipotentials are planes parallel to the plates, evenly spaced ($V$ varies linearly across the gap).
- **Two equal positive charges:** roughly spherical equipotentials far away (the pair looks like a single $2q$); close in, two egg-shaped surfaces around each charge with a saddle point on the line between them.

The simulation at the end of this chapter draws these patterns live. Once you see the equipotential contours and the field arrows on the same canvas — arrows always crossing contours at right angles — the gradient relation stops being abstract.

### Recovering the field by gradient

In Cartesian coordinates:

$$\vec{E} = -\nabla V = -\left(\frac{\partial V}{\partial x}\hat{x} + \frac{\partial V}{\partial y}\hat{y} + \frac{\partial V}{\partial z}\hat{z}\right)$$

In a problem with one-dimensional symmetry (V depends only on $x$, or only on $r$):

$$E_x = -\frac{dV}{dx}, \quad \text{or} \quad E_r = -\frac{dV}{dr}$$

The simulation computes the gradient numerically with central differences:

$$\frac{\partial V}{\partial x}(x, y) \approx \frac{V(x+h, y) - V(x-h, y)}{2h}$$

Accuracy is second-order in $h$. The trade-off: smaller $h$ means lower truncation error but worse cancellation roundoff. For the grid spacing typical in a browser visualization, central differences are accurate enough that the arrows visibly cross the contours at right angles — the visual check on the math.

### Continuous distributions and Poisson's equation

For a charge distribution with density $\rho$ (or $\sigma$, or $\lambda$), the potential at field point $\vec{r}$ is

$$V(\vec{r}) = k \int \frac{dq}{|\vec{r} - \vec{r}'|}$$

A scalar integral. One number per field point. For distributions without enough symmetry for Gauss's law to crack open the field, the potential integral is often the only tractable route — and once you have $V$, the gradient gives $\vec{E}$.

Combining the gradient relation with Gauss's law gives one equation that ties everything together:

$$\nabla \cdot \vec{E} = -\nabla \cdot \nabla V = -\nabla^2 V = \rho/\varepsilon_0$$

$$\boxed{\;\nabla^2 V = -\rho/\varepsilon_0\;}$$

**Poisson's equation.** In a charge-free region ($\rho = 0$), it reduces to $\nabla^2 V = 0$, called **Laplace's equation**. Every electrostatics problem with conductors at specified potentials reduces to solving Laplace's equation with boundary conditions. The mid-level E&M course is largely techniques for this. We name it here, mark its territory, and move on.

### The electron-volt

When the system of interest is one charge crossing a potential difference, the natural energy unit is what you get from a 1 V drop on an electron. Define:

$$1 \text{ eV} = 1.602176634 \times 10^{-19} \text{ J}$$

This is exact: in the 2019 SI redefinition the elementary charge $e$ was *defined* to be $1.602176634 \times 10^{-19}$ C, so the eV is now a defined number ([BIPM 2019](https://www.bipm.org/en/publications/si-brochure)).

The eV is convenient because it spans the energy scales of physics:

| Domain | Energy scale |
|---|---|
| Thermal energy at room temperature ($k_B T$) | $\approx 0.026$ eV |
| Visible photon | 1.8–3.1 eV |
| Hydrogen ionization (Rydberg) | 13.6 eV |
| X-ray photon | $\sim$ keV |
| Nuclear binding per nucleon | $\sim 8$ MeV |
| Proton mass-energy | 938 MeV |
| LHC beam (per proton, 2022 Run 3) | 6.8 TeV |
| Highest cosmic ray ever observed (Amaterasu, 2023) | $\sim 2.4 \times 10^{20}$ eV ([Telescope Array, *Science* 2023](https://doi.org/10.1126/science.abo5095)) |

Twenty-two orders of magnitude in one unit. The Amaterasu particle had macroscopic kinetic energy — about 40 joules, the energy of a baseball thrown by a major-league pitcher — concentrated in a single particle. Where it came from is not yet known.

---

## Worked example: the uniformly charged ring

A ring of radius $R$ carries total charge $Q$ distributed uniformly around its circumference. Find $V$ and $E_x$ at a point on the symmetry axis a distance $x$ from the center.

**Set up.** Place the ring in the $yz$-plane, centered at the origin. The field point is at $(x, 0, 0)$. Pick any element of charge $dq$ on the ring. By the Pythagorean theorem, its distance to the field point is

$$r = \sqrt{x^2 + R^2}$$

— the same value for *every* element on the ring, because every element sits at the same perpendicular distance $R$ from the axis.

**The potential.** Since $r$ does not depend on which $dq$ we pick, the integral is just $r$ pulled outside:

$$V(x) = \int \frac{k\, dq}{r} = \frac{k}{\sqrt{x^2 + R^2}} \int dq = \frac{kQ}{\sqrt{x^2 + R^2}}$$

One line. Done.

**The field.** Differentiate:

$$E_x = -\frac{dV}{dx} = -kQ \cdot \frac{d}{dx}(x^2 + R^2)^{-1/2} = \frac{kQx}{(x^2 + R^2)^{3/2}}$$

The chain rule did the work that vector-component bookkeeping did in Chapter 2.

**Compare with Chapter 2's vector route.** In Chapter 2, we integrated $dE_x = (k\, dq/r^2) \cos\theta$ around the ring, where $\cos\theta = x/r$ projects each element's field onto the axis. The integral was

$$E_x = \int \frac{k\, dq}{r^2} \cdot \frac{x}{r} = \frac{kx}{r^3} Q = \frac{kQx}{(x^2 + R^2)^{3/2}}$$

— the same answer. Two routes. The potential route required a single scalar integral and one derivative; the vector route required carrying the $\cos\theta$ projection through the integration. The potential route does the angular projection automatically — it gets absorbed into the gradient at the end.

**Limits.** At the center ($x = 0$): $V = kQ/R$ and $E_x = 0$ (by symmetry — every charge element pulls toward itself from the field point, and contributions on opposite sides of the ring cancel). At $x \gg R$: $V \to kQ/x$ and $E_x \to kQ/x^2$. The ring looks like a point charge from far away. As it should.

**The lesson.** For distributions where every source point is the same distance from the field point — rings, spherical shells, certain symmetric arcs — the potential integral collapses to a single divide. The vector field integral never does. Even for cases where both routes work, the potential route is usually cheaper.

---

## Common misconceptions

**"High $V$ means high $E$."** No. $\vec{E}$ is the *gradient* of $V$, not $V$ itself. The midpoint between two equal positive charges has high positive $V$ (both charges contribute positively) and zero $\vec{E}$ (saddle point). The plane perpendicular to a dipole axis through the midpoint has $V = 0$ everywhere on it (the two charges contribute equally and opposite) and a large $\vec{E}$ pointing from the $+$ side to the $-$ side. *The value of $V$ at a point tells you nothing about $\vec{E}$ at that point; only the spatial variation does.*

**"$V$ is zero where there is no charge."** $V$ at a point depends on *all* charges everywhere, weighted by distance. The potential a meter from a point charge is nonzero even though there is no charge there. The only place $V$ goes to zero "automatically" is the reference point — and that choice is yours.

**"Equipotential lines and field lines are the same."** They are always perpendicular — never parallel. Field lines run *across* equipotentials, always downhill. The student who confuses the two is one of the most common pedagogical failure modes in this material; the simulation at the end is calibrated to break the confusion visually.

**"$V$ is a vector because $\vec{E}$ is."** $V$ is a *scalar*. One number at each point in space. The vectorness is in $\vec{E} = -\nabla V$, where the gradient operator manufactures three components from one scalar function.

**"If two students get different answers for $V$ at a point, one of them is wrong."** Not necessarily — they may be using different references. Only $\Delta V$ between two points is reference-independent. If one student is using $V(\infty) = 0$ and another is using "the floor of the lab" as ground, their absolute $V$ values differ by a constant, but the $\Delta V$ between any two points is identical. The PER literature (Singh 2006; Pollock & Singh, *Phys. Rev. PER* 2008+) flags reference-point confusion as a persistent stumbling block.

---

## Exercises

**Warm-up (Understand).** Define $V$ in one sentence (use the word "work"). Define $U$ in one sentence. State the relation between them in one symbol. Then explain why a problem can have $V = 1{,}000{,}000$ V at a point without anything dramatic happening to a charge placed there.

**Apply (scalar superposition).** Two charges sit on the x-axis: $+2$ nC at $x = 0$, and $-3$ nC at $x = 4$ cm. Compute $V$ at the point $(2 \text{ cm}, 3 \text{ cm})$. Take $V(\infty) = 0$. Report in volts.

**Apply (gradient).** On the axis of a uniformly charged ring of radius $R = 5$ cm and total charge $Q = 10$ nC, find (a) $V$ at $x = 0$, (b) $V$ at $x = 10$ cm, and (c) $E_x$ at $x = 10$ cm. Use $k = 8.99 \times 10^9$ N·m²/C².

**Apply (electron-volt scale).** An electron is accelerated from rest across a potential difference of 25 kV (a 1960s television tube). (a) What is its kinetic energy in joules? In eV? (b) What is its speed, treating it non-relativistically? Compare to $c$. Should you have used the relativistic formula?

**Apply + Analyze (system energy).** Three charges sit at the vertices of an equilateral triangle of side $a = 10$ cm: $q_1 = +1$ nC, $q_2 = +1$ nC, $q_3 = -1$ nC. (a) Compute the total electrostatic potential energy $U$ of the configuration. (b) If all three charges are released simultaneously, will the configuration fly apart, collapse, or do something more complicated? Argue from your value of $U$ relative to zero, plus the geometry.

**Challenge (Synthesize).** Show that on the axis of a uniformly charged *disk* of radius $R$ and total charge $Q$, the potential is

$$V(x) = \frac{Q}{2\pi\varepsilon_0 R^2}\left(\sqrt{x^2 + R^2} - |x|\right)$$

by treating the disk as a stack of nested rings and integrating the ring result over ring radius from 0 to $R$. Then differentiate to get $E_x$. Verify that as $R \to \infty$ at fixed surface charge density $\sigma = Q/(\pi R^2)$, $E_x \to \sigma/(2\varepsilon_0)$ — the infinite plane result from Chapter 3.

---

## LLM Exercises

### Build the potential-surface visualizer (`04-electric-potential.html`)

> **Show.** Electric potential of point charges: $V(\vec{r}) = \sum_i k q_i / |\vec{r} - \vec{r}_i|$. The electric field is the negative gradient: $\vec{E} = -\nabla V$. Field lines are perpendicular to equipotentials.
>
> **Say.** Build a potential-surface visualizer that color-maps $V(x, y)$, overlays equipotential contour lines, and draws $\vec{E}$ arrows as the numerical gradient of the color map.
>
> **Constrain.** D3 v7. Charge palette: drag-and-drop point charges onto the canvas; per-charge sliders for sign and magnitude (range $\pm 10$ nC). Performance OK for up to 8 simultaneous charges. Render $V(x, y)$ on a grid (~200×200) as a heatmap with red high, blue low; clip extreme values near the singularities to keep the color scale readable. Equipotential contours: use `d3.contours()` to draw level sets of $V$ in green, at evenly spaced levels. Electric field arrows: compute $\vec{E} = -\nabla V$ by central differences on the grid; draw arrows on a coarser sub-grid (e.g., 20×20) with length proportional to $|\vec{E}|$, capped for visual clarity. Toggles: (a) show/hide heatmap, (b) show/hide equipotentials, (c) show/hide field arrows. Filename: `04-electric-potential.html`.
>
> **Verify.** (a) Single $+q$: equipotentials are concentric circles, field arrows radial outward. (b) Single $-q$: equipotentials are concentric circles, field arrows radial inward. (c) Dipole ($+q, -q$): the line equidistant from both charges is a $V = 0$ equipotential; arrows cross it perpendicular to it. (d) Two equal $+q$: there is a saddle point of $V$ on the line between them where $\vec{E} = 0$ (no arrow); the equipotentials form a figure-eight pattern around the saddle. (e) **Critical visual check:** at every grid point, the field arrow should be perpendicular to the local equipotential contour. If they are not perpendicular, the gradient code is wrong.

### Exploration

- Place a single $+10$ nC charge. Sketch by eye where the $V = 100$ V equipotential should be (use $V = kq/r$ → $r = kq/V \approx 0.9$ m for these numbers). Find it on the simulation. Does the spacing of equipotentials get tighter as you approach the charge? Why?
- Place a $+q$ and a $-q$ separated by 10 cm. Find the $V = 0$ equipotential — note that it is *not* the same as the locus of zero $\vec{E}$. Explain in one sentence why.
- Place four equal $+q$ charges at the corners of a square. Identify all the points where $\vec{E} = 0$. How many are there, and which is which kind of critical point (saddle, max, min) of $V$?
- Place two $+q$ side by side. Walk a test point from far away straight toward the midpoint between them. Watch $V$ rise. Now walk perpendicular off the line. Does $V$ rise or fall? What does that tell you about the saddle geometry?

### Extension prompt (chapter bridge)

> **Show.** I've seen the potential-surface visualizer. Now I want to use $V$ to define a new device: a *capacitor*. Two conductors held at different $V$, with the ratio $C = Q/V$ characterizing how much charge sits on the plates per volt of difference.
>
> **Say.** Modify the visualizer to add a "capacitor mode": place two large parallel charged plates ($+\sigma$ and $-\sigma$) and visualize the uniform $\vec{E}$ field between them, the linearly varying $V$, and the planar equipotentials.
>
> **Constrain.** Plates are line segments on the canvas; uniform surface charge density. The $V$ heatmap should show parallel-line equipotentials between the plates. Field arrows should be uniform, perpendicular to the plates. Display a readout: $C = \varepsilon_0 A / d$ for the chosen geometry, $V = E \cdot d$, and stored energy $U = \frac{1}{2}CV^2$.
>
> **Verify.** Equipotentials are evenly spaced lines parallel to the plates. $\vec{E}$ is uniform between them and zero outside (in the idealized limit). The energy readout should equal the energy density $\frac{1}{2}\varepsilon_0 E^2$ multiplied by the volume between the plates.

Save as `04b-capacitor-preview.html`. This is the lead-in to Chapter 5.

---

## What would change my mind

The central claims of this chapter — that the electrostatic field is curl-free, that a scalar potential exists, that $\vec{E} = -\nabla V$, that scalar superposition makes $V$ easier to compute than $\vec{E}$ — rest on the inverse-square law plus the static condition (no time-varying $\vec{B}$). All three are extremely well-tested. Coulomb's $1/r^2$ has been verified to a part in $10^{16}$ ([Williams, Faller & Hill, 1971](https://doi.org/10.1103/PhysRevLett.26.721)). The conservative-force property follows from the radial form, and every laboratory test of energy conservation in electrostatic systems confirms it. A confirmed observation of path-dependent work in a *static* electric field would force a rewrite — but such an observation would also overturn the inverse-square law, and would be the headline of the century. None has been seen.

Time-varying fields are a different story. Chapter 10 (Faraday) shows that $\nabla \times \vec{E} \neq 0$ when $\vec{B}$ changes, and the path-independence of work is genuinely broken. The scalar potential $V$ then needs companions ("vector potential" $\vec{A}$, gauge choices) to keep the framework coherent. For now, electrostatics, and $V$ alone is enough.

## Still puzzling

- *The reference-point convention.* For any isolated finite distribution, $V(\infty) = 0$ is natural. For an infinite line charge, $V \to \infty$ at every infinity, and the convention has to be chosen by hand (pick a finite reference radius). For the full universe — including any background of cosmological charge density — the convention question becomes deep. We assume electrical neutrality at large scales without strong direct evidence; if it failed, the very concept of an absolute $V$ would need rethinking.
- *Why the world is electrically neutral.* The matter in the universe contains roughly equal numbers of protons and electrons. There is no fundamental conservation law that requires this — proton number and electron number are separately conserved (at least at low energies). The near-perfect neutrality is an observational fact, with bounds on net charge imbalance per particle of better than $10^{-21}$ ([Marinelli & Morpurgo, 1984](https://doi.org/10.1016/0370-1573%2884%2990014-1)). If neutrality fails at any level, $V$ from cosmological-scale charges would dominate everything we measure. It doesn't, but we don't fully understand why.
- *Practical PER finding.* Students who execute the gradient calculation correctly still misread the saddle-point geometry of two-positive-charge configurations: they expect $\vec{E} = 0$ to imply $V = 0$, or vice versa. The chapter sketches the counterexamples, but the underlying confusion — that $V$ and $\vec{E}$ have no fixed value-to-value relationship at a point, only a derivative relationship — remains an open teaching problem in the introductory literature.

---

**Tags:** electric potential, voltage, equipotential surface, gradient, electron-volt, Poisson equation, Volta, scalar superposition
