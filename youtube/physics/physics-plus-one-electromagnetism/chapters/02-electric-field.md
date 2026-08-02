# Chapter 2 — The Electric Field

*From force between charges to field filling space, and the simulation that makes the field visible.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define the electric field operationally as force per unit test charge and identify the units (N/C = V/m).
2. **(Apply)** Compute $\vec{E}$ at any point in space for a point charge and for a small arrangement of point charges using superposition.
3. **(Apply)** Set up and evaluate the integral for $\vec{E}$ on the axis of a uniformly charged ring and on the axis of a uniformly charged disk.
4. **(Analyze)** Distinguish between cases where field lines accurately encode field magnitude (2D) and where they only show direction (3D projected to 2D).
5. **(Apply)** Build a 2D vector-field renderer that draws $\vec{E}$ at every point on a grid for any user-configurable charge arrangement.

---

## Opening case: Faraday's lines of force

In the 1830s, Michael Faraday — who had no formal mathematics training and could not follow Coulomb's equations in their original form — proposed something heretical to the mainstream of physics. The force between charges, he said, is not "action at a distance." It is mediated by something physically real that exists *in the space between* the charges. He called it the **field**, and he pictured it as a set of **lines of force** filling space — lines that emerge from positive charges, end on negative charges, are tangent everywhere to the direction of force, and have a density that signals strength.

Most physicists in 1830 thought this was a quaint visualization for a man who couldn't do math. By 1860 the field concept had become the language of the subject, because James Clerk Maxwell — who *could* do the math — proved that field theory was not just visualization but the right physical framework. By 1864 Maxwell's equations had been written in field form, and by 1888 Hertz had detected actual *waves in the field* propagating through empty space. The field, Faraday's intuition, turned out to be physical. It carries energy. It carries momentum. It propagates at the speed of light.

This chapter teaches the field formulation. It is the same physics as Chapter 1 — the same forces, the same superposition — but expressed in a way that prepares you for Gauss's law (Chapter 3), the wave equation (Chapter 11), and ultimately the realization that light is an oscillation in this very field.

---

## Core concept

### Definition of the electric field

Place a tiny test charge $q_0$ at point $P$. Coulomb's law says it feels a force $\vec{F}$ from all other charges. Define the **electric field** at $P$ as the force per unit test charge:

$$\vec{E}(P) = \lim_{q_0 \to 0} \frac{\vec{F}}{q_0}$$

Units: newton per coulomb (N/C), equivalently volt per meter (V/m). The limit is taken so the test charge is small enough not to disturb the very arrangement that produces the field — a conceptual idealization.

The field is a *property of space*, defined wherever you might place a test charge — and crucially defined whether or not any test charge is actually there. The point charges in your problem are the **sources**; the field is what those sources produce at every point.

### Field of a point charge

For a single point charge $q$ at the origin, the field at position $\vec{r}$ is

$$\vec{E}(\vec{r}) = \frac{kq}{r^2}\,\hat{r}$$

Radially outward if $q > 0$, radially inward if $q < 0$. Magnitude falls as $1/r^2$. The field is undefined *at* the charge itself (it would be infinite) but defined everywhere else.

The relation to Coulomb's law: a second charge $q'$ placed at $\vec{r}$ feels force $\vec{F} = q' \vec{E}(\vec{r})$. The field is the bookkeeping device that lets you describe what one charge does to space without simultaneously specifying what other charge is feeling it.

### Superposition of fields

For multiple source charges $q_i$ at positions $\vec{r}_i$, the total field at $\vec{r}$ is the **vector sum**:

$$\vec{E}(\vec{r}) = \sum_i \frac{k q_i}{|\vec{r} - \vec{r}_i|^3}(\vec{r} - \vec{r}_i)$$

This is the cleaner version of Chapter 1's force superposition. The field at every point is a vector; you compute it once for a given source arrangement, and any subsequent charge feels force $q \vec{E}$ from it. Field superposition is inherited from Maxwell's equations being linear in the sources.

### Field lines: what they show and where they fail

A **field line** is a curve everywhere tangent to $\vec{E}$. Properties:

1. Field lines emerge from positive charges, terminate on negative charges (or extend to infinity).
2. Field lines never cross — at a crossing point, $\vec{E}$ would have to point in two directions at once.
3. The number of lines per unit area perpendicular to the field encodes |$\vec{E}$| — *if* you draw lines proportional to charge and stay in the right dimensional setting.

The last point deserves care. In a 2D textbook diagram of charges in a plane, line density gives a reasonable visual estimate of field magnitude. In actual 3D space, the field's $1/r^2$ falloff comes from the surface area of a sphere growing as $4\pi r^2$ — so a 3D field-line density, computed correctly through a sphere, does encode field strength. But the 2D projection of that 3D structure does not; it discards the third dimension's worth of lines.

For Chapter 2 simulations (2D), treat field-line density as *qualitative* and rely on vector arrows (length proportional to |$\vec{E}$|) for quantitative information.

### Electric dipole

Two equal and opposite charges, $+q$ and $-q$, separated by a small displacement $\vec{d}$ pointing from $-q$ to $+q$, form an **electric dipole**. The dipole moment is

$$\vec{p} = q \vec{d}$$

For a dipole at the origin with $\vec{d}$ small, the field at distance $r$ along the dipole axis (the $+\hat{z}$ direction) is approximately

$$\vec{E}_{\text{axis}}(z) \approx \frac{2k\vec{p}}{z^3}$$

and on the perpendicular bisector (the $\hat{x}$ direction):

$$\vec{E}_{\perp}(x) \approx -\frac{k\vec{p}}{x^3}$$

Both fall as $1/r^3$ — faster than the $1/r^2$ of a single charge. The dipole's two opposite charges nearly cancel at large distances, leaving only the residual asymmetry that scales as $|\vec{d}|/r$ times the point-charge field.

Dipoles are everywhere: water molecules (the H-O-H bond is asymmetric, giving water a permanent dipole moment), antenna radiation patterns, the bound surface charges on dielectrics (Chapter 5), the radiation pattern from accelerating charges (Chapter 12).

### Continuous charge distributions

For a continuous source — a charged rod, a charged disk, a sphere of charge — sum becomes integral. Three densities:

- **Linear** charge density $\lambda$ (C/m): charge per unit length on a 1D object
- **Surface** charge density $\sigma$ (C/m²): charge per unit area on a 2D object
- **Volume** charge density $\rho$ (C/m³): charge per unit volume in a 3D object

The field at point $\vec{r}$ from a distribution:

$$\vec{E}(\vec{r}) = \int \frac{k \, dq}{|\vec{r} - \vec{r}'|^3}(\vec{r} - \vec{r}')$$

where $dq = \lambda \, d\ell$, $\sigma \, dA$, or $\rho \, dV$ depending on the distribution. The integral is over the source distribution's coordinates $\vec{r}'$.

---

## Worked example: field on the axis of a uniformly charged ring

Ring of radius $R$ lying in the $xy$-plane, centered at origin, with total charge $Q$ uniformly distributed (linear density $\lambda = Q/(2\pi R)$). Find $\vec{E}$ at point $(0, 0, z)$ on the axis.

**Symmetry first.** Every element $dq = \lambda \, R \, d\phi$ on the ring contributes a field $d\vec{E}$ to the axial point. By symmetry, the components of $d\vec{E}$ perpendicular to the axis cancel — for every element at angle $\phi$, there's a diametrically opposite element at $\phi + \pi$ contributing an opposite perpendicular component. Only the axial ($\hat{z}$) component survives.

**Distance.** From a ring element at $(\cos\phi, \sin\phi, 0)R$ to the axial point $(0,0,z)$: distance $r = \sqrt{R^2 + z^2}$.

**Axial component.** The element produces $|d\vec{E}| = k \, dq / r^2$, and the projection onto $\hat{z}$ is $\cos\theta = z/r$. So

$$dE_z = \frac{k \, dq}{r^2} \cdot \frac{z}{r} = \frac{k z \, dq}{(R^2 + z^2)^{3/2}}$$

**Integrate over the ring.** $\int dq = Q$, and the integrand is independent of $\phi$, so

$$E_z(z) = \frac{k Q z}{(R^2 + z^2)^{3/2}}$$

**Check limits.**
- At $z = 0$: $E_z = 0$. By symmetry, the center of the ring has zero field. ✓
- At $z \gg R$: $E_z \to kQ/z^2$. From far away, the ring looks like a point charge. ✓
- At $z = R$ (a natural scale): $E_z = kQ/(R^2 \cdot 2^{3/2}) = kQ/(2\sqrt{2} R^2)$. About $0.354 \, kQ/R^2$. Maximum field on the axis turns out to be at $z = R/\sqrt{2}$ (find this by taking $dE_z/dz = 0$).

**The lesson.** Symmetry reduces a 2D integral over a ring to a 1D weighted sum that vanishes by inspection in transverse directions. Always look for symmetry *before* setting up the integral.

**The limit.** This works on the axis. *Off* the axis, the perpendicular components no longer cancel and the integral is harder. For a point in the plane of the ring but not at center, the field requires elliptic integrals. Gauss's law (Chapter 3) won't help either — the ring has neither spherical, cylindrical, nor planar symmetry. The lesson: not every problem yields to elegance.

---

## Common misconceptions

**"Field lines show the path a charge would follow."** They show the *direction* of the force at every instant. A particle moving in the field has inertia; it follows a curved trajectory determined by Newton's second law, not by the field lines. Only in the special case of zero initial velocity and a strictly uniform field do path and field line coincide.

**"Where there's no charge, there's no field."** False. The field is a property of space at every point. A point in empty space between two charges has a perfectly well-defined field — that's why a test charge placed there feels a force. The field exists everywhere the sources can influence; the sources don't have to be local to the field.

**"Field lines and equipotentials are the same thing."** They are everywhere *perpendicular* — see Chapter 4. They are different objects. Field lines follow $\vec{E}$; equipotentials trace surfaces of constant potential $V$.

**"In two dimensions, the field of a point charge falls as $1/r$, not $1/r^2$."** Tricky. A "point charge" in *true* 2D physics (a 2D world) does have a field falling as $1/r$, because Gauss's law in 2D uses a circumference $2\pi r$ rather than a surface $4\pi r^2$. But in our 3D world rendered onto a 2D *cross-section*, the field of a 3D point charge still falls as $1/r^2$, and the 2D image is just a slice. Confusion arises because an *infinite line charge* viewed in cross-section gives a 2D-looking field that does fall as $1/r$ — but that's because the source is genuinely a line, not a point.

---

## Exercises

**Warm-up (Apply).** Compute $\vec{E}$ at the origin from a single charge $q = +1$ µC located at position $(0, 0, 0.1)$ m. Express in N/C and identify the direction.

**Apply.** Two charges, $+q$ at $(+a, 0)$ and $-q$ at $(-a, 0)$, form a dipole. Compute $\vec{E}$ at points (a) on the $x$-axis at $x = 2a$, (b) on the $y$-axis at $y = 2a$. Verify the $1/r^3$ scaling for $r \gg a$.

**Apply.** Two charges $+q$ at $(+a, 0)$ and $+q$ at $(-a, 0)$ (both positive). Compute $\vec{E}$ at $(0, y)$ for arbitrary $y > 0$. Where does $|\vec{E}|$ have its maximum on the $y$-axis? Where does $\vec{E} = 0$? (Hint: on the $y$-axis itself, but only for special $y$.)

**Apply + Analyze.** A uniformly charged disk of radius $R$ and surface charge density $\sigma$ lies in the $xy$-plane. (a) Set up the integral for $E_z(z)$ on the disk's axis using the result for a ring. (b) Carry out the integral. Result: $E_z = (\sigma/2\varepsilon_0)[1 - z/\sqrt{R^2 + z^2}]$. (c) Take the limit $R \to \infty$ (infinite plane): $E_z = \sigma/(2\varepsilon_0)$. The field of an infinite plane is *uniform* — same magnitude at every distance. Compare to a point charge's $1/r^2$ falloff.

**Challenge.** A charged rod of length $L$ has total charge $Q$ uniformly distributed along it. Find $\vec{E}$ at a point on the axis of the rod, at distance $d$ beyond one end. (Hint: line element $dq = (Q/L) \, dx$, integrate from rod's near end to far end.)

---

## LLM Exercises

### Build the field visualizer (`02-electric-field.html`)

> **Show.** Field of a point charge: $\vec{E} = kq\hat{r}/r^2$. Superposition for multiple charges.
>
> **Say.** Build a 2D electric-field visualizer with drag-and-drop charges and an animated vector-field background.
>
> **Constrain.** D3 v7. Up to 8 charges, drag-and-drop with sliders for magnitude (positive or negative). Compute $\vec{E}$ at each point on a 20×15 grid by summing over all charges. Draw arrows at each grid point: direction = $\vec{E}$ direction; length scaled by $\log(1 + |\vec{E}|)$ for visual readability; color map blue (weak) to red (strong) via D3's interpolateRdBu. Toggle button: show/hide field lines (computed by RK4 integration from starting points near each charge). Filename: `02-electric-field.html`.
>
> **Verify.** (a) Single positive charge: arrows radiate outward; magnitudes fall with distance. (b) Equal opposite charges (dipole): field lines connect them; on the perpendicular bisector $\vec{E}$ points from $+q$ to $-q$; on the axis, far away, $|\vec{E}| \sim 1/r^3$. (c) Two equal positive charges: a null point appears on the midline.

### Exploration

- Build a quadrupole (two dipoles head-to-tail). What does the field look like far away? Does it fall as $1/r^3$, $1/r^4$, or something else? (Answer: $1/r^4$. The leading dipole moments cancel; only the quadrupole moment survives.)
- Toggle between vector-arrow view and field-line view for the same configuration. Where do they agree visually? Where do they mislead?
- Drag charges into a perfect square configuration with alternating signs. Sketch the expected field pattern before the simulation renders.

### Extension prompt (chapter bridge)

> **Show.** I now have a visualizer that draws $\vec{E}$ from any charge arrangement. I want to add a Gaussian surface — a closed curve in 2D — and measure the flux through it.
>
> **Say.** Add a draggable, resizable closed curve (a circle, representing a Gaussian sphere in 2D cross-section). Compute the flux numerically: $\Phi_E \approx \sum_i \vec{E}_i \cdot \hat{n}_i \, \Delta\ell_i$ around the boundary.
>
> **Constrain.** The Gaussian surface should be visually distinct (yellow dashed). Display the computed flux $\Phi_E$ alongside the theoretical value $Q_{\text{enc}}/\varepsilon_0$. Update both in real time as the user moves the surface or adds charges.
>
> **Verify.** Surface enclosing no charges: $\Phi_E \approx 0$. Surface enclosing one positive charge: $\Phi_E = q/\varepsilon_0$ regardless of surface size. Surface enclosing a $+q$ and a $-q$: $\Phi_E \approx 0$.

Save as `02b-gaussian-surface-preview.html`. This is the lead-in to Chapter 3.

---

## What would change my mind

The field concept's central claim is that all of electromagnetism can be cast in terms of fields rather than direct action at a distance. The two formulations are mathematically equivalent at the level of force on a test charge — Coulomb's law and "Coulomb's law via field" give the same force. The deep claim — that the field itself is physical, carrying energy and momentum — is supported by (a) the fact that EM waves propagate through empty space at finite speed $c$, demonstrably carrying energy detectable in distant receivers, and (b) the fact that radiation pressure has been measured directly (Lebedev 1900, Nichols & Hull 1901). A confirmed observation that EM influence is instantaneous (faster-than-light) or that "field energy" is not conserved when it should be would force a reconsideration. No such observation exists.

## Still puzzling

- *What "is" the field?* In classical physics it's a function from spacetime points to vectors. In quantum field theory it's an operator-valued field whose excitations are photons. The classical-to-quantum transition is exactly where Chapter 12's photoelectric effect lives.
- *Why does the field-line picture sometimes mislead?* The line-density convention is a specific encoding choice; in some renderings (2D projection of 3D, near singularities) it breaks down. The convention is useful, not fundamental. The vector formulation is.
- *Can charges be smaller than the field?* Point charges as infinitesimal objects produce divergent fields at their location. Classical EM does not fully resolve this; quantum electrodynamics does, by replacing the point charge with a renormalized cloud. Beyond intro scope.

---

**Tags:** electric field, superposition, field lines, dipole, continuous charge distribution, Faraday, vector field

