# Chapter 9 — Sources of Magnetic Fields

*Currents make magnetic fields, and the post-2019 ampere is defined by the elementary charge.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the Biot-Savart law for the field of a current element and identify it as the magnetic analogue of Coulomb's law.
2. **(Apply)** Compute the magnetic field of a long straight wire, a circular loop on its axis, and an ideal solenoid.
3. **(Apply)** Use Ampère's law to find $\vec{B}$ for current configurations with cylindrical or planar symmetry.
4. **(Understand)** State Gauss's law for magnetism ($\nabla \cdot \vec{B} = 0$) and explain its empirical content: no magnetic monopoles.
5. **(Understand)** Explain the 2019 SI redefinition of the ampere in terms of the fixed elementary charge.
6. **(Apply)** Build a magnetic field-line visualizer for configurable current configurations.

---

## Opening case: the MRI solenoid

A clinical magnetic-resonance imaging scanner is built around a giant **solenoid** — a tightly wound coil, typically a meter long, with thousands of turns of superconducting wire carrying hundreds of amperes. The result is a uniform magnetic field inside the bore: 1.5 tesla, 3 tesla, sometimes 7 tesla for research scanners. That's 30,000 to 140,000 times Earth's surface field.

The patient lies inside this strong, uniform field. Hydrogen nuclei in their body — water and fat are mostly hydrogen — align with $\vec{B}$. RF pulses tip the alignment momentarily; the nuclei precess at the **Larmor frequency** $\omega = \gamma B$ proportional to the field, and re-emit the energy as detectable RF signals. The MRI machine reconstructs an image from these signals.

For this to work, the field must be *extremely* uniform — parts per million across the imaging volume. Real MRI magnets are not just one solenoid; they are several coaxial solenoids with carefully shaped currents producing the right field profile. But the core physics is in this chapter: a solenoid produces a uniform field inside, $B = \mu_0 n I$.

This chapter asks how currents make magnetic fields, the way the previous chapters asked how charges make electric fields. The structure is parallel: Biot-Savart is the magnetic Coulomb's law (field from a source element); Ampère's law is the magnetic Gauss's law (field from symmetric current configurations). We work through both, applied to the three current geometries that matter most.

---

## Core concept

### The Biot-Savart law

For a current $I$ flowing through a small length element $d\vec{\ell}$ (vector along the current direction), the contribution to the magnetic field at a point displaced $\vec{r}$ from the element is

$$d\vec{B} = \frac{\mu_0}{4\pi} \cdot \frac{I \, d\vec{\ell} \times \hat{r}}{r^2}$$

where $\mu_0 = 4\pi \times 10^{-7}$ T·m/A is the **permeability of free space**.

Compare to Coulomb's law: $d\vec{E} = (k\,dq/r^2)\hat{r}$. The differences:
1. The source is *current* $I\,d\vec{\ell}$, not charge.
2. The cross product makes $d\vec{B}$ perpendicular to both $d\vec{\ell}$ and $\hat{r}$. The field *curls around* the current direction.
3. The constant $\mu_0/(4\pi)$ is the magnetic analogue of $k = 1/(4\pi\varepsilon_0)$.

Importantly: $\mu_0$ and $\varepsilon_0$ are related by $\mu_0 \varepsilon_0 = 1/c^2$. The speed of light hides inside the permeability and permittivity of free space; this is Chapter 11's punchline.

**Right-hand rule:** point your right thumb along the current direction. Your fingers curl in the direction of the field. For a long straight wire carrying current upward, $\vec{B}$ is in horizontal circles counterclockwise (viewed looking down along the current).

### Worked: B from a long straight wire

For a long straight wire carrying current $I$, integrate the Biot-Savart contributions over all elements of the wire. The integral is straightforward (a single-variable definite integral in cylindrical coordinates). Result:

$$B(r) = \frac{\mu_0 I}{2\pi r}$$

Direction: circular around the wire, right-hand rule. Falls off as $1/r$ (not $1/r^2$) because the wire is infinite — adding more length adds more contribution from large-angle elements.

For two parallel wires carrying currents $I_1, I_2$ separated by distance $d$ in the same direction, the force per unit length on wire 2 (from $\vec{B}_1$ acting on $I_2\vec{L}$):

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

Same-direction currents *attract*. Opposite-direction currents *repel*. The geometric reason: each wire is in the other's field, and the cross product $\vec{L} \times \vec{B}$ points inward for parallel, outward for antiparallel.

This formula is historically how the **ampere** was defined.

### B on the axis of a circular loop

Loop of radius $R$ in the $xy$-plane, current $I$ counterclockwise viewed from $+z$. By Biot-Savart integration on the axis at distance $z$ from the center, $\vec{B}$ has only a $\hat{z}$ component (symmetry kills the transverse components):

$$B_z(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$$

At the center ($z = 0$): $B = \mu_0 I/(2R)$. Far away ($z \gg R$): $B \approx \mu_0 I R^2/(2z^3)$ — a $1/r^3$ falloff like the electric dipole. The current loop is a *magnetic dipole* with moment $\vec{m} = I\pi R^2 \hat{n}$.

### The ideal solenoid

A tightly wound coil with $n$ turns per unit length, carrying current $I$, in the limit of infinite length (or short length but inside many turns from each end), produces a uniform field along the axis inside:

$$B = \mu_0 n I$$

Outside the solenoid (still in the infinite-length limit): $B \approx 0$.

To derive this, apply **Ampère's law** (see next subsection) to a rectangular Amperian loop with one long side inside the solenoid (length $L$ along the axis), one long side outside, and two perpendicular sides connecting them. The line integral collapses:
- Inside leg: $\vec{B} \parallel \vec{L}$, contributes $BL$.
- Outside leg: $\vec{B} \approx 0$, contributes 0.
- Perpendicular legs: $\vec{B} \perp \vec{L}$, contribute 0.

Total: $BL = \mu_0 (nLI)$, since $nL$ turns pass through the loop. So $B = \mu_0 n I$.

This is the relevant result for the MRI scanner of the chapter opening. Plug in: a 3 T MRI bore with $n = 3000$ turns/m needs current $I = B/(\mu_0 n) = 3/(4\pi \times 10^{-7} \cdot 3000) \approx 800$ A. (Real MRIs run currents in this range, typically using superconducting wire.)

### Ampère's law

The magnetic analogue of Gauss's law. The line integral of $\vec{B}$ around any closed loop equals $\mu_0$ times the current piercing the loop:

$$\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}$$

Always true. Useful for computing $\vec{B}$ when the current configuration has enough symmetry to pull $|\vec{B}|$ out of the integral.

The three computationally useful symmetries (same logic as Gauss for $\vec{E}$):
- **Cylindrical**: long straight wires, infinite cylinders of current → circular Amperian loops coaxial with the wire/cylinder.
- **Planar** (less common): infinite sheets of current → rectangular Amperian loops with two sides parallel to the sheet.
- **Solenoid/toroidal**: as set up above.

Like Gauss for $\vec{E}$, the chapter's hardest skill is recognizing when Ampère's law gives you $\vec{B}$ efficiently, versus when direct Biot-Savart integration is required.

### Gauss's law for magnetism: no monopoles

For any closed surface:

$$\oint \vec{B} \cdot d\vec{A} = 0$$

Equivalently in differential form: $\nabla \cdot \vec{B} = 0$. The empirical content: there are no isolated magnetic charges. Magnetic field lines have no "source" or "sink"; they always form closed loops.

Dirac (1931) showed that *if* a magnetic monopole existed, it would explain why electric charge is quantized (in terms of fundamental units of $e$). The hypothesis remains theoretically attractive in some grand unified theories. Experimental searches — MoEDAL at the LHC, IceCube cosmic-ray monitor, dedicated underground searches — have not detected a magnetic monopole at any energy. The current limits are very strong; if monopoles exist they are either very rare, very heavy, or very localized.

Until further notice: $\nabla \cdot \vec{B} = 0$ is one of Maxwell's equations, with the right-hand side identically zero.

### The 2019 SI redefinition of the ampere

Before 2019, the ampere was defined operationally:
> "The ampere is the constant current that, when maintained in two straight parallel conductors of infinite length, of negligible circular cross-section, and placed 1 meter apart in vacuum, would produce between these conductors a force equal to $2 \times 10^{-7}$ newton per metre of length."

This is exactly the $F/L = \mu_0 I_1 I_2/(2\pi d)$ formula with $I_1 = I_2 = 1$ A and $d = 1$ m. Inverting: $\mu_0 = 4\pi \times 10^{-7}$ T·m/A *exactly*, by definition of the ampere.

In May 2019, the SI was reorganized. The ampere was redefined by fixing the **elementary charge**:

$$e = 1.602\,176\,634 \times 10^{-19} \text{ C \quad (exact, by definition)}$$

The ampere is now derived: 1 A = 1 C/s = $(1/e)$ elementary charges per second ≈ $6.241 \times 10^{18}$ charges/s. As a consequence, $\mu_0$ is no longer exact; it is measured, with $\mu_0 \approx 4\pi \times 10^{-7}$ T·m/A to extremely high precision but no longer by definition.

The change is largely cosmetic — at intro-physics precision, $\mu_0 = 4\pi \times 10^{-7}$ is still the working value. But the conceptual move is interesting: the SI base unit is no longer pinned to an unrealized mechanical thought experiment (infinite parallel wires in vacuum) but to a fundamental quantum constant.

---

## Worked example: field from two parallel wires

Two long parallel wires, separation $d = 5$ cm, carrying currents $I_1 = 10$ A and $I_2 = 5$ A in the same direction. (a) Find the field at the midpoint between them. (b) Find the force per unit length on wire 2.

**(a) Field at midpoint.** Each wire produces a field at the midpoint at distance $d/2 = 2.5$ cm. Wire 1 produces $B_1 = \mu_0 I_1/(2\pi (d/2)) = (4\pi \times 10^{-7})(10)/(2\pi \cdot 0.025) = 8.0 \times 10^{-5}$ T. Wire 2 produces $B_2 = \mu_0 I_2/(2\pi (d/2)) = 4.0 \times 10^{-5}$ T.

Direction: by the right-hand rule, both fields point in *opposite directions* at the midpoint (one wire pushes its field clockwise around itself; the other does the same but they're on opposite sides). So:
$$B_{\text{net}} = B_1 - B_2 = 4.0 \times 10^{-5} \text{ T}$$
in the direction set by the larger wire.

**(b) Force per unit length on wire 2.** Wire 2 sits in wire 1's field at distance $d$: $B_1 = \mu_0 I_1/(2\pi d) = 4.0 \times 10^{-5}$ T. Force per unit length on wire 2:
$$F/L = I_2 B_1 = (5)(4.0 \times 10^{-5}) = 2.0 \times 10^{-4} \text{ N/m}$$

Direction: same-direction currents attract, so the force on wire 2 points toward wire 1.

**The lesson.** Superposition for $\vec{B}$ works exactly like for $\vec{E}$. Field from each source, vector sum. Force on a current is $I L \times B$ from the *other* source's field.

**The limit.** This is for "long" wires — long enough that finite-length corrections are negligible. For short wires, the integration of Biot-Savart over a finite length gives a different result; the field of a finite wire of length $L$ at perpendicular distance $r$ from its midpoint is $B = (\mu_0 I/4\pi r)(\sin\theta_1 + \sin\theta_2)$ where $\theta_1, \theta_2$ are the angles subtended.

---

## Common misconceptions

**"Magnetic field lines start on north poles and end on south poles."** They form closed loops everywhere. The "poles" of a bar magnet are where the field lines emerge into the surrounding space; inside the magnet, the same field lines continue, connecting the poles. No source, no sink.

**"Ampère's law only works for infinite symmetric currents."** It is always true; symmetry just determines computational usefulness, exactly like Gauss for $\vec{E}$.

**"The solenoid field is uniform everywhere inside."** Only for an *infinite* solenoid (or near the center of a long but finite one). At the ends of a real solenoid, the field drops; at the geometric end of a long coil, $B \approx \frac{1}{2}\mu_0 n I$ — half the interior value. This factor-of-two error catches students who use the formula at the ends.

**"Magnetic forces don't do work, so how does a motor do work?"** The wire feels a force; the force does no work on the *electrons* (the magnetic force is perpendicular to their velocity). But the magnetic force on the moving electrons gets transferred through scattering to the lattice — the wire as a whole accelerates. The electrons' kinetic energy comes from the *source's electric field* (the battery). Subtle but correct.

**"Magnetic monopoles must exist by symmetry."** They might. Dirac's argument is suggestive but not conclusive. Experimentally: no detection, ever. ∇·B = 0 with the right-hand side zero is the current best understanding.

---

## Exercises

**Warm-up (Apply).** A long straight wire carries 10 A. Find $\vec{B}$ at perpendicular distance (a) 1 cm, (b) 10 cm. Report magnitude and indicate direction (e.g., "circular around the wire, counterclockwise viewed looking along $+\hat{I}$").

**Apply.** A circular loop of radius 5 cm carries 2 A. Find $\vec{B}$ (a) at the center, (b) on the axis at $z = 10$ cm.

**Apply.** A solenoid with 800 turns per meter carries 3 A. Find the field inside the solenoid in tesla. How much current would be needed to produce $B = 1$ T?

**Apply + Analyze.** Two parallel wires 5 cm apart carry currents $I_1 = 4$ A in $+\hat{x}$ and $I_2 = 6$ A in $-\hat{x}$ (opposite directions). (a) Find the force per unit length on each wire. Is it attractive or repulsive? (b) Find the magnetic field at the midpoint between them. (c) Find a point along the line connecting them where $\vec{B} = 0$.

**Apply (Hall + Ampère).** A copper wire of radius 1 mm carries 5 A uniformly through its cross-section. Use Ampère's law to find $\vec{B}$ (a) at $r = 0.5$ mm (inside the wire), (b) at $r = 1$ mm (at the surface), (c) at $r = 2$ mm (outside).

**Challenge.** Earth's magnetic dipole moment is about $8 \times 10^{22}$ A·m². If you modeled this as a single circular current loop with radius equal to Earth's outer-core radius ($\sim 3500$ km), what current would the loop need to carry to produce this dipole moment? Compare to a typical lightning bolt's current (~30 kA). (Hint: $m = I A$ → $I = m/A$.)

---

## LLM Exercises

### Build the magnetic field-line visualizer (`09-magnetic-field-sources.html`)

> **Show.** Biot-Savart: $d\vec{B} = (\mu_0/4\pi)(I\,d\vec{\ell} \times \hat{r})/r^2$. For a long straight wire: $B = \mu_0 I/(2\pi r)$, circular around the wire.
>
> **Say.** Build an interactive magnetic field-line visualizer for several current configurations.
>
> **Constrain.** D3 v7. Selectable configurations: (1) single long straight wire, (2) two parallel wires (same or opposite direction), (3) circular current loop, (4) solenoid cross-section. Sliders for current magnitude(s). For each configuration, compute $\vec{B}(x, y)$ analytically at every grid point; draw field lines by RK4. Field lines purple (per `DESIGN.md`). Currents shown as orange dots (out of page) or X marks (into page). Filename: `09-magnetic-field-sources.html`.
>
> **Verify.** (a) Single wire: circular field lines, density decreasing with distance. (b) Two parallel wires, same direction: lines bunch between them. Opposite direction: lines spread out between them. (c) Solenoid: nearly uniform field lines parallel to the axis inside; lines fan out at the ends.

### Exploration

- Build the two-parallel-wires case. Set currents equal and same-direction. Predict the field at the midpoint (should be zero by symmetry). Verify.
- Build a solenoid cross-section. Compare the field inside (uniform) to the field outside (nearly zero). What happens near the ends?
- For a single wire: increase $I$ by factor of 2. Does the field strength double? (Yes; the formula $B = \mu_0 I/(2\pi r)$ is linear in $I$.)

### Extension prompt (chapter bridge)

> **Show.** Currents make $\vec{B}$. Now, what about a *changing* magnetic flux through a loop? Does it create a current in the loop?
>
> **Say.** Build a Faraday induction simulator: a moving bar magnet near a stationary coil.
>
> **Constrain.** Bar magnet (dipole approximation) with adjustable speed (slider). Show field lines from the magnet. Compute the flux $\Phi_B$ through a fixed circular coil; numerically differentiate to get $d\Phi_B/dt$ and hence the induced EMF. Display $\Phi_B(t)$, $\varepsilon(t)$, and the resulting induced current $I(t)$ in real time. Reverse the motion to see the EMF reverse.
>
> **Verify.** Faster motion gives larger EMF. Reversed motion gives reversed EMF (Lenz's law).

Save as `09b-faraday-preview.html`. This is the lead-in to Chapter 10.

---

## What would change my mind

The Biot-Savart law and Ampère's law are exact in magnetostatics (steady currents). A discrepancy between predicted and measured fields would force revision. None has been observed at intro-physics precision. The 2019 SI redefinition of the ampere is a unit redefinition, not a physics change; it doesn't alter what the formulas predict, only how we describe them.

The claim that there are no magnetic monopoles is empirical. A confirmed detection would force adding a magnetic charge term to Gauss's law for $\vec{B}$: $\oint \vec{B} \cdot d\vec{A} = \mu_0 Q_{\text{m}}$. The Maxwell equations would gain a fourth source term and the full symmetry between $\vec{E}$ and $\vec{B}$ would be restored. The community continues to search. Until detection, the right-hand side is zero.

## Still puzzling

- *Why is electric charge quantized?* Dirac's monopole argument is one of the few we have. If monopoles exist, charge quantization follows. If they don't, charge quantization is empirically true but theoretically unexplained.
- *Frequency-dependent permeability.* For ferromagnetic materials, $\mu_r$ is complicated and frequency-dependent. The chapter treats most materials as $\mu \approx \mu_0$. Industrial transformer cores and inductor cores use high-$\mu_r$ ferromagnetic materials; the simple formulas modify.
- *Magnetic monopole searches.* MoEDAL at the LHC continues to look. IceCube monitors cosmic rays. Underground searches use giant solenoidal detectors. Each year that passes without detection tightens the bound on monopole abundance and mass. If we never find them, we will not know why charge is quantized.

---

**Tags:** Biot-Savart law, Ampère's law, solenoid, permeability, magnetic flux, magnetic monopole, ampere, SI redefinition, parallel wires

