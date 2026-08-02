# Chapter 3 — Gauss's Law

*The first of Maxwell's equations, and the fastest tool in electrostatics.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define electric flux $\Phi_E = \oint \vec{E} \cdot d\vec{A}$ and explain its physical meaning as the net "field lines crossing a surface."
2. **(Apply)** Use Gauss's law to compute $\vec{E}$ for distributions with spherical, cylindrical, or planar symmetry.
3. **(Analyze)** Given an unfamiliar charge distribution, decide whether Gauss's law will *help* compute $\vec{E}$ — that is, whether the distribution has exploitable symmetry.
4. **(Apply)** Apply Gauss's law to conductors in electrostatic equilibrium: derive that $\vec{E} = 0$ inside, that net charge resides on the surface, and that the field just outside is $\sigma/\varepsilon_0$.
5. **(Apply)** Build a Gaussian-surface flux visualizer that numerically verifies $\Phi_E = Q_{\text{enc}}/\varepsilon_0$ for user-configurable charges and surfaces.

---

## Opening case: shielded MRI rooms

A modern MRI scanner reads tiny radio-frequency signals from precessing hydrogen nuclei in a patient's body. The signals are in the range of a few microvolts at the receiver coil. In an unshielded room, those signals are buried under cell-phone transmissions, FM radio, fluorescent-lamp electronics, and the room's own electrical wiring — each producing fields hundreds to millions of times stronger than what the MRI machine needs to detect.

So clinical MRI rooms are built as enclosed copper boxes — typically copper sheet or copper mesh embedded in the walls, sealed doors with copper gaskets, copper-screened windows with through-glass mesh. The patient and machine sit inside; the rest of the world is outside. The interior of the room is electromagnetically isolated from external interference to a degree set by the conductivity of the shielding and the wavelengths of the unwanted signals — typically 80–120 dB of attenuation in the MRI band.

The phenomenon making this work is the **Faraday cage**, and its physics is one consequence of Gauss's law. A closed conducting surface, with no charge inside the enclosed volume, has zero electric field in that volume — no matter how violent the field outside. The chapter ahead is the law that says why.

Gauss's law is also the first of Maxwell's four equations. Everything from charge distributions to electromagnetic waves traces back to the relation between flux of $\vec{E}$ through a closed surface and the charge enclosed.

---

## Core concept

### Electric flux

For an electric field $\vec{E}$ and a surface $S$, the **electric flux** through $S$ is

$$\Phi_E = \int_S \vec{E} \cdot d\vec{A}$$

where $d\vec{A}$ is an area element with magnitude $dA$ and direction along the (chosen) outward normal to the surface. The dot product picks out the component of $\vec{E}$ perpendicular to the surface; tangential components contribute nothing.

For a **closed surface**, the convention is that $d\vec{A}$ points outward (away from the enclosed volume). The closed-surface flux is denoted with a circle on the integral:

$$\Phi_E = \oint_S \vec{E} \cdot d\vec{A}$$

Physical meaning: the net number of field lines crossing the surface, signed. Lines emerging from inside count positive; lines entering from outside count negative.

**Units.** $\Phi_E$ has units of $V \cdot m$ (equivalently $N \cdot m^2/C$).

### Gauss's law

The central claim of this chapter:

$$\boxed{\;\oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}\;}$$

The total electric flux through any closed surface equals the total charge enclosed divided by $\varepsilon_0$. Period. Independent of the surface's shape, position, or size — only the enclosed charge matters.

### Why it works (the solid-angle derivation)

Start with a point charge $q$ at the origin. Choose a spherical Gaussian surface of radius $r$ centered on the charge. On this sphere:
- $\vec{E} = (kq/r^2)\hat{r}$ is radial outward
- $d\vec{A} = dA \, \hat{r}$ is radial outward
- $\vec{E} \cdot d\vec{A} = (kq/r^2) \, dA$
- $\int dA = 4\pi r^2$ (sphere's surface area)

Flux: $\Phi_E = (kq/r^2)(4\pi r^2) = 4\pi k q = q/\varepsilon_0$ (using $k = 1/(4\pi\varepsilon_0)$).

Notice $\Phi_E = q/\varepsilon_0$ does *not* depend on $r$. The $1/r^2$ falloff of the field exactly cancels the $r^2$ growth of the sphere's area. This isn't accidental — it's why the inverse-square law gives such a clean global statement.

Now generalize to an *arbitrary* surface enclosing the charge. The key idea is **solid angle**. Each radial direction from $q$ passes through any enclosing surface at exactly one point. The contribution to the flux from a solid-angle element $d\Omega$ is $(kq) \, d\Omega$, *independent of how far away from $q$ the surface is in that direction*. Integrating over the total solid angle ($4\pi$ steradians for any direction):
$$\Phi_E = (kq)(4\pi) = q/\varepsilon_0$$
The result is the same for *any* closed surface enclosing the charge.

For a charge *outside* the surface: every radial direction either misses the surface entirely or enters once and exits once. Each entry-exit pair contributes opposite signs that cancel. Net flux: zero.

Superposition extends this to multiple charges: $\Phi_E = (\sum_i q_i)/\varepsilon_0 = Q_{\text{enc}}/\varepsilon_0$.

The derivation uses only the inverse-square law and superposition. Wherever those hold, Gauss's law holds.

### Using Gauss's law to compute fields

Gauss's law is *always true*. It's *useful for computing $\vec{E}$* only when the charge distribution has enough symmetry that you can pull $|\vec{E}|$ outside the flux integral.

The skill is recognizing the three computationally useful symmetries:

**Spherical symmetry.** Charge distribution depends only on radius from a center. Gaussian surface: sphere of radius $r$ centered on the same point. On the sphere, $\vec{E}$ is radial with constant magnitude.
$$\oint \vec{E} \cdot d\vec{A} = E(r) \cdot 4\pi r^2 = Q_{\text{enc}}/\varepsilon_0 \implies E(r) = \frac{Q_{\text{enc}}}{4\pi\varepsilon_0 r^2}$$

**Cylindrical symmetry.** Distribution depends only on perpendicular distance from an infinite axis. Gaussian surface: cylinder coaxial with the axis, radius $r$, length $L$. On the curved surface, $\vec{E}$ is radial with constant magnitude; on the flat caps, $\vec{E}$ is parallel to the cap and contributes nothing.
$$\oint \vec{E} \cdot d\vec{A} = E(r) \cdot 2\pi r L = \lambda L/\varepsilon_0 \implies E(r) = \frac{\lambda}{2\pi\varepsilon_0 r}$$

**Planar symmetry.** Distribution depends only on perpendicular distance from an infinite plane. Gaussian surface: a "pillbox" (a short cylinder pierced through the plane). On each cap, $\vec{E}$ is perpendicular to the cap with constant magnitude; on the curved side, $\vec{E}$ is parallel to the side and contributes nothing.
$$\oint \vec{E} \cdot d\vec{A} = 2 E A = \sigma A/\varepsilon_0 \implies E = \frac{\sigma}{2\varepsilon_0}$$

In each case, the computational trick is the same: choose a Gaussian surface where the field is *parallel to the normal and constant in magnitude*, then $E$ pulls out of the integral and you do arithmetic.

### Conductors in electrostatic equilibrium

A conductor is a material in which charges are free to move. In **electrostatic equilibrium** — no charges currently moving — four properties follow from Gauss's law and the requirement that mobile charges feel no force.

1. **$\vec{E} = 0$ everywhere inside the conductor.** If $\vec{E}$ were nonzero anywhere inside, mobile charges would feel a force and move; not equilibrium.
2. **Net charge resides only on the surface.** Choose any closed Gaussian surface entirely inside the conductor. Since $\vec{E} = 0$ on it, $\oint \vec{E} \cdot d\vec{A} = 0$, so $Q_{\text{enc}} = 0$. No charge in the interior. Excess charge sits at the surface.
3. **Just outside, $\vec{E}$ is perpendicular to the surface.** Any tangential component would push surface charges along the surface; not equilibrium.
4. **Just outside, $E = \sigma/\varepsilon_0$.** Apply a Gaussian pillbox at the surface: $\vec{E}$ outside contributes $EA$; inside contributes zero; total flux equals $\sigma A/\varepsilon_0$. So $E_{\text{outside}} = \sigma/\varepsilon_0$. (Note: this is twice the "infinite plane" result $\sigma/(2\varepsilon_0)$, because here all the flux is on one side.)

The Faraday cage from the chapter opening follows: a closed conducting shell, no charge inside the cavity, will have $\vec{E} = 0$ inside the cavity (regardless of the external field configuration). External fields induce surface charges on the conductor that exactly cancel them in the interior.

---

## Worked example: a uniformly charged solid sphere

Sphere of radius $R$, total charge $Q$ distributed uniformly (volume density $\rho = Q/((4/3)\pi R^3)$). Find $\vec{E}$ at arbitrary radius $r$.

**Symmetry.** Spherical. Choose Gaussian sphere of radius $r$ centered on the same center.

**Case 1: $r > R$ (outside the sphere).** Gaussian sphere encloses all the charge: $Q_{\text{enc}} = Q$.
$$E(r) \cdot 4\pi r^2 = Q/\varepsilon_0 \implies E(r) = \frac{Q}{4\pi\varepsilon_0 r^2} = \frac{kQ}{r^2}$$
From outside, the sphere looks exactly like a point charge $Q$ at its center.

**Case 2: $r < R$ (inside the sphere).** Gaussian sphere encloses only the fraction of charge within radius $r$:
$$Q_{\text{enc}}(r) = \rho \cdot \frac{4}{3}\pi r^3 = Q \cdot \frac{r^3}{R^3}$$
Apply Gauss:
$$E(r) \cdot 4\pi r^2 = \frac{Q r^3}{\varepsilon_0 R^3} \implies E(r) = \frac{Qr}{4\pi\varepsilon_0 R^3} = \frac{kQr}{R^3}$$
Linear in $r$ inside, zero at center.

**Putting it together.** $E(r)$ rises linearly from zero at the center to a maximum $kQ/R^2$ at the surface, then falls as $1/r^2$ outside. A clean piecewise function.

**The lesson.** Gauss's law collapses what would be a difficult 3D vector integral (the field of a continuous sphere of charge) into a two-line algebraic calculation. The whole trick is choosing the Gaussian surface to match the symmetry.

**The limit.** This works because the source has spherical symmetry. For a *non-uniform* sphere (charge density a function of $r$ only, say $\rho(r) = \rho_0(r/R)$), the symmetry still works — replace $Q_{\text{enc}}(r)$ with the integral $\int_0^r 4\pi r'^2 \rho(r') \, dr'$. But for a sphere with $\rho$ depending on angle, Gauss's law no longer simplifies and you fall back on direct integration.

---

## Common misconceptions

**"Gauss's law only works for symmetric distributions."** Gauss's law is *always true*. Symmetry only determines whether it's a useful *computational shortcut* for finding $\vec{E}$. For asymmetric distributions, Gauss's law still tells you the total flux through any closed surface — but knowing the flux doesn't determine $\vec{E}$ point-by-point if you can't pull $E$ out of the integral.

**"The Gaussian surface must be a physical surface."** The Gaussian surface is a mathematical fiction — a region of space bounded by your chosen closed boundary. It doesn't have to coincide with any material object. You draw it on paper (or in code) and apply the law.

**"If a charge is outside the Gaussian surface, its field doesn't reach inside the surface."** False. The external charge produces field everywhere, including on and inside the Gaussian surface. What's zero is the *net flux of its field through the closed surface* — every field line from the external charge enters and exits, contributing canceling signed terms. The field is nonzero; the flux is zero.

**"In a conductor with a cavity, $\vec{E} = 0$ in the cavity always."** Only if there's no charge in the cavity. Put a point charge inside the cavity: the conductor's surface charges rearrange to ensure $\vec{E} = 0$ in the conductor's *material*, but $\vec{E}$ in the cavity is now governed by the cavity charge plus the induced charge on the cavity wall. The cavity field is nonzero.

**"Symmetry recognition is the same as applying the formula."** Recent physics-education research (Singh 2006; Wallace & Chasteen 2010) finds that *recognizing the symmetry* in a problem is harder for students than executing the calculation once the symmetry is identified. Practice symmetry diagnosis explicitly.

---

## Exercises

**Warm-up (Understand).** State Gauss's law in words. Then state in one sentence each: when does it work as a *computational tool* and when is it merely a true statement that doesn't help compute $\vec{E}$?

**Apply.** Symmetry diagnosis (no calculation). For each distribution, name the symmetry (spherical / cylindrical / planar / none) and the Gaussian surface to use:
- (a) A uniformly charged thin spherical shell.
- (b) An infinite straight line of charge.
- (c) Two parallel infinite planes with equal and opposite uniform charge.
- (d) A short, finite straight rod of charge.
- (e) A cube of uniform charge density.
*Answers in order: spherical (sphere); cylindrical (cylinder); planar (pillbox); none (direct integration); none.*

**Apply.** A solid insulating sphere of radius $R = 5$ cm has uniform volume charge density $\rho = +2.0 \, \mu\text{C/m}^3$. Find $|\vec{E}|$ at (a) $r = 3$ cm, (b) $r = 8$ cm. Report each in N/C.

**Apply.** A long coaxial cable has an inner conductor of radius $a$ carrying linear charge $+\lambda$ and an outer conductor of inner radius $b$ carrying linear charge $-\lambda$. Use Gauss's law to find $\vec{E}$ in the three regions: $r < a$, $a < r < b$, $r > b$. (Answers: 0, $\lambda/(2\pi\varepsilon_0 r)$ radially out, 0.)

**Apply + Analyze.** A conducting shell of inner radius $a$, outer radius $b$, has a point charge $+q$ at its center. (a) Find $\vec{E}$ in three regions ($r < a$, $a < r < b$, $r > b$). (b) Find the charge induced on the inner surface (at $r = a$) and on the outer surface (at $r = b$). (c) If the shell carries no net charge, the inner and outer induced charges must sum to zero — check this.

**Challenge.** Earnshaw's theorem. Prove that no arrangement of static point charges can produce stable equilibrium for a fourth test charge in empty space. (Hint: stability requires the divergence of force to be negative at the equilibrium point. But in empty space, $\nabla \cdot \vec{E} = 0$ by Gauss's law with $\rho = 0$. So the force on a test charge has zero divergence everywhere in empty space — which forbids stability in all three directions simultaneously.)

---

## LLM Exercises

### Build the Gaussian-surface flux visualizer (`03-gauss-law.html`)

> **Show.** Gauss's law: $\oint \vec{E} \cdot d\vec{A} = Q_{\text{enc}}/\varepsilon_0$. I want to drop a Gaussian surface (a circle in 2D) into a field, move and resize it, and watch the numerical flux match the analytical prediction.
>
> **Say.** Build a Gaussian-surface flux visualizer.
>
> **Constrain.** D3 v7. Charge palette: place point charges anywhere on the canvas, set magnitude and sign via sliders. Field-line view (computed by RK4) overlaid. A draggable, resizable circle represents the Gaussian surface (a 2D cross-section of a sphere). Compute the line integral $\oint \vec{E} \cdot \hat{n} \, d\ell$ around the boundary numerically (sample 200 points). Display the result alongside the theoretical $Q_{\text{enc}}/\varepsilon_0$ for comparison. Arrow vectors at sample points on the surface, colored by their dot-product sign (red = outward flux, blue = inward). Filename: `03-gauss-law.html`.
>
> **Verify.** (a) Surface enclosing only $+q$: $\Phi_E = q/\varepsilon_0$ regardless of surface size. (b) Surface enclosing $+q$ and $-q$: $\Phi_E \approx 0$. (c) Surface enclosing no charges (charges outside the surface): $\Phi_E \approx 0$ within numerical noise.

### Exploration

- Place a single positive charge. Move the Gaussian surface around. Does the flux ever change? When does it jump?
- Put two equal positive charges side by side. Position the Gaussian surface to enclose just one of them. What flux do you measure?
- Place a $+q$ at the center of the surface and add a $-q$ far away (still inside the surface). The flux should be zero — verify.

### Extension prompt (chapter bridge)

> **Show.** Gauss's law gives me $\vec{E}$ from symmetric distributions. Now I want a scalar quantity that's even easier to compute — the electric potential $V$, where $\vec{E} = -\nabla V$.
>
> **Say.** Modify the visualizer to show $V(x, y)$ as a color-mapped background and equipotential contour lines.
>
> **Constrain.** Compute $V(x,y) = \sum_i k q_i / r_i$ at each grid point. Render as a heatmap (red = high, blue = low) with green dashed equipotential contours via `d3.contours()`. Verify that the existing electric-field arrows point from high-$V$ regions to low-$V$ regions and are perpendicular to the equipotential contours.
>
> **Verify.** Visual check: $\vec{E}$ arrows are perpendicular to equipotentials everywhere; flow runs downhill from red regions to blue regions.

Save as `03b-potential-preview.html`. This is the lead-in to Chapter 4.

---

## What would change my mind

Gauss's law as derived here rests on (a) the inverse-square law (Coulomb), (b) superposition, and (c) the geometric fact that solid angles sum to $4\pi$ around any interior point. All three are extremely well-tested. The exponent in the inverse-square law has been verified to be 2 within a part in $10^{16}$ in laboratory tests (Williams, Faller & Hill, 1971; subsequent improvements). A confirmed deviation from inverse-square at any scale where Coulomb's law currently holds would force a rewriting of this chapter. None has been observed. Some theories propose tiny deviations at sub-millimeter scales (related to extra spatial dimensions); experimental searches have placed strong bounds.

## Still puzzling

- *Magnetic monopoles.* Gauss's law for $\vec{B}$ (Chapter 9, then Maxwell's equations in Chapter 11) reads $\oint \vec{B} \cdot d\vec{A} = 0$ for any closed surface — the magnetic analogue with the right-hand side identically zero, *because no magnetic charges have been observed*. Dirac (1931) showed that a single magnetic monopole, if it existed, would explain the quantization of electric charge. None has been detected.
- *Symmetry recognition pedagogy.* The 2023 PER literature suggests intro students can execute Gauss-law calculations once symmetry is identified, but struggle to recognize symmetry independently. The chapter has an exercise on this but the gap remains an open teaching problem.
- *Gauss's law in non-Euclidean geometries.* In curved spacetime (general relativity), the surface-integral form has to be generalized. The Maxwell-equations chapter doesn't take us there; the formulation is more involved but the spirit survives.

---

**Tags:** Gauss's law, flux, Gaussian surface, conductor, Faraday cage, Earnshaw's theorem, symmetry, Maxwell equation #1

