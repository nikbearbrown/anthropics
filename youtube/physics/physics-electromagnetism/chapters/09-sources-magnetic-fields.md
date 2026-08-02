# Chapter 9 — Sources of Magnetic Fields

*Currents make magnetic fields, and the post-2019 ampere is defined by the elementary charge.*

---

A clinical MRI scanner is built around a solenoid roughly a meter long, wound with thousands of turns of superconducting wire carrying hundreds of amperes. The result, inside the bore, is a magnetic field of 1.5 to 7 tesla — up to 140,000 times Earth's surface field. The patient lies inside it. The hydrogen nuclei in their water and fat align with the field, get tipped by a radio-frequency pulse, precess at a frequency proportional to the local field strength, and re-emit detectable RF signals. The machine assembles those signals into an image.

For this to work, the field must be uniform to parts per million across the imaging volume. A real MRI magnet is not one solenoid but several nested coaxial coils with carefully chosen currents, each contributing to the right field profile. But the core physics is this: a solenoid with $n$ turns per meter carrying current $I$ produces a uniform field $B = \mu_0 n I$ inside. If you want 3 T and your winding density is 3000 turns per meter, you need roughly 800 amperes.

This chapter asks how currents make magnetic fields, in the same spirit that earlier chapters asked how charges make electric fields. The structure is parallel. The Biot-Savart law is the magnetic Coulomb's law: field from a current element. Ampère's law is the magnetic Gauss's law: field from any symmetric current configuration. We work through both, applied to the three geometries that actually matter.

---

## The Biot-Savart law

For a current $I$ flowing through a small element $d\vec{\ell}$ (a vector in the direction of current flow), the contribution to the magnetic field at a point displaced $\vec{r}$ from the element is

$$d\vec{B} = \frac{\mu_0}{4\pi} \cdot \frac{I\,d\vec{\ell} \times \hat{r}}{r^2}$$

where $\mu_0 = 4\pi \times 10^{-7}$ T·m/A is the **permeability of free space**.

Compare this to Coulomb's law, $d\vec{E} = (k\,dq/r^2)\hat{r}$. Three differences stand out.

First, the source is current $I\,d\vec{\ell}$ rather than charge $dq$. Second, a cross product appears where Coulomb has a simple $\hat{r}$. The cross product means $d\vec{B}$ is perpendicular to both the current direction and the displacement — the field doesn't point toward or away from the source, it *curls around* it. Third, the constant $\mu_0/4\pi$ is the magnetic analogue of $k = 1/(4\pi\varepsilon_0)$, and the two constants are related: $\mu_0\varepsilon_0 = 1/c^2$. The speed of light hides inside the constants of electrostatics and magnetostatics. This is Chapter 11's punchline.

The right-hand rule handles the cross product geometrically. Point the right thumb along the current direction; the fingers curl in the direction of the magnetic field. For a long wire carrying current upward, the field circles it counterclockwise when viewed from above — the field lines are horizontal rings.

![long straight wire with current I upward — magnetic field lines shown as horizontal circles around the wire, right-hand rule illustrated with thumb pointing up along current and fingers curling counterclockwise, arrow...](../images/09-sources-magnetic-fields-fig-01.png)
*Figure 9.1 — Biot-Savart Law*

<!-- → [IMAGE: long straight wire with current I upward — magnetic field lines shown as horizontal circles around the wire, right-hand rule illustrated with thumb pointing up along current and fingers curling counterclockwise, arrow labels showing the direction of B at several radii] -->

---

## B from a long straight wire

Integrate the Biot-Savart contributions over all elements of an infinitely long straight wire. The integral is a standard one in cylindrical coordinates — every element contributes a field at the same perpendicular distance $r$ from the wire, and the components parallel to the wire cancel by symmetry. The result:

$$B(r) = \frac{\mu_0 I}{2\pi r}$$

The field falls off as $1/r$, not $1/r^2$. The reason: you are integrating over an infinite line of source elements. Even though each element's field falls as $1/r^2$, there are more elements at large angles contributing usefully as you get closer to the wire. The line integral effectively trades one power of $r$ in the denominator for a constant.

Now consider two long parallel wires separated by distance $d$, carrying currents $I_1$ and $I_2$. Wire 2 sits in wire 1's magnetic field. The force per unit length on wire 2 is:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}$$

Same-direction currents attract; opposite-direction currents repel. This follows from the cross product $I_2\vec{L} \times \vec{B}_1$: when the currents run the same way, $\vec{B}_1$ at wire 2's location is perpendicular to $\vec{L}$ and the force points toward wire 1.

This formula was historically how the ampere was defined — the constant current in two parallel wires 1 meter apart that produces a force of $2 \times 10^{-7}$ N per meter. I'll return to what replaced that definition.

![two parallel wires side by side — left panel: same-direction currents (both dots or both X marks), force arrows pointing inward (attraction), B field from wire 1 shown at wire 2's location with the cross product I₂L×B...](../images/09-sources-magnetic-fields-fig-02.png)
*Figure 9.2 — Three Geometries*

<!-- → [IMAGE: two parallel wires side by side — left panel: same-direction currents (both dots or both X marks), force arrows pointing inward (attraction), B field from wire 1 shown at wire 2's location with the cross product I₂L×B₁ pointing toward wire 1; right panel: opposite-direction currents, force arrows pointing outward (repulsion) — student should see the cross-product direction flip with the current reversal] -->

---

## B on the axis of a circular loop

A circular loop of radius $R$ in the $xy$-plane carries current $I$ counterclockwise when viewed from $+z$. By symmetry, the field on the axis at height $z$ has only a $z$-component — all transverse contributions from opposite sides of the loop cancel. The Biot-Savart integral over the loop gives:

$$B_z(z) = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}$$

At the center ($z = 0$): $B = \mu_0 I/(2R)$. Far away ($z \gg R$): $B \approx \mu_0 I R^2/(2z^3)$, falling as $1/z^3$.

That $1/z^3$ falloff is the same as an electric dipole field. The current loop *is* a magnetic dipole, with moment

$$\vec{m} = I A \hat{n}$$

where $A = \pi R^2$ is the loop's area and $\hat{n}$ is the normal by the right-hand rule. This is the same quantity that appears in atomic physics when we talk about the magnetic moment of an electron orbit — the fundamental quantum unit of magnetic moment, the **Bohr magneton** $\mu_B = e\hbar/2m_e$, is just this formula for an electron in a circular orbit.

![B_z(z) vs. z for a circular current loop — curve peaking at B = μ₀I/2R at z=0, falling symmetrically on both sides, annotated with the 1/z³ asymptote for z≫R and the value at the center; student should see the field p...](../images/09-sources-magnetic-fields-fig-03.png)
*Figure 9.3 — Ampère's Law*

<!-- → [CHART: B_z(z) vs. z for a circular current loop — curve peaking at B = μ₀I/2R at z=0, falling symmetrically on both sides, annotated with the 1/z³ asymptote for z≫R and the value at the center; student should see the field profile is smooth and peaked, unlike a uniform solenoid] -->

---

## Ampère's law

Ampère's law is to Biot-Savart as Gauss's law is to Coulomb's law. The line integral of $\vec{B}$ around any closed loop equals $\mu_0$ times the current threading the loop:

$$\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}}$$

Always true. Useful for computing $\vec{B}$ when the current configuration has enough symmetry to pull $|\vec{B}|$ out of the integral — the same idea as pulling $E$ out of the Gauss's law flux integral.

**Cylindrical symmetry.** A long straight wire or solid cylinder of current. Choose a circular Amperian loop of radius $r$ centered on the wire. Symmetry forces $\vec{B}$ to be tangential and constant in magnitude on the circle. The line integral collapses: $B \cdot 2\pi r = \mu_0 I_{\text{enc}}$, giving $B = \mu_0 I_{\text{enc}}/(2\pi r)$. Outside the wire, $I_{\text{enc}} = I$ (total current); inside a solid wire of radius $R$, $I_{\text{enc}} = I(r/R)^2$ (only the enclosed fraction). The field inside the wire rises linearly from zero at the center to a maximum at the surface; outside it falls as $1/r$. This is the exact magnetic analogue of the charged solid sphere from Chapter 3.

![B(r) vs. r for a solid cylindrical current — linear rise from 0 at center to μ₀I/2πR at the surface, then 1/r falloff outside; kink at r=R labeled; student should compare to the E(r) profile of the uniformly charged s...](../images/09-sources-magnetic-fields-fig-04.png)
*Figure 9.4 — Parallel Wires*

<!-- → [CHART: B(r) vs. r for a solid cylindrical current — linear rise from 0 at center to μ₀I/2πR at the surface, then 1/r falloff outside; kink at r=R labeled; student should compare to the E(r) profile of the uniformly charged sphere from Chapter 3] -->

**The solenoid.** The cleanest application of Ampère's law in this chapter. Apply a rectangular Amperian loop with one long side of length $L$ inside the solenoid (parallel to the axis), one long side outside, and two short sides perpendicular to the axis.

- Inside leg: $\vec{B}$ is parallel to $d\vec{\ell}$, contributes $BL$.
- Outside leg: $\vec{B} \approx 0$ for an ideal infinite solenoid, contributes 0.
- Perpendicular legs: $\vec{B} \perp d\vec{\ell}$, contribute 0.

The loop encloses $nL$ turns, each carrying current $I$. So $I_{\text{enc}} = nLI$. Ampère's law gives:

$$BL = \mu_0 n L I \implies B = \mu_0 n I$$

This is a remarkably clean derivation. The uniformity of the field inside follows from the symmetry of the ideal solenoid; the $B \approx 0$ outside follows because the field lines must close, and with the loop field inside large and confined, the return path outside is spread over all of space and is negligible. Real solenoids deviate at the ends — at the geometric end of a long coil, $B$ drops to roughly $\frac{1}{2}\mu_0 n I$ — but near the center the formula is exact.

![cross-section of a solenoid with the rectangular Amperian loop drawn in — inside leg labeled BL (contributing to the integral), outside leg labeled B≈0, perpendicular legs labeled "B⊥dl, no contribution", enclosed tur...](../images/09-sources-magnetic-fields-fig-05.png)
*Figure 9.5 — Gauss's Law for B*

<!-- → [IMAGE: cross-section of a solenoid with the rectangular Amperian loop drawn in — inside leg labeled BL (contributing to the integral), outside leg labeled B≈0, perpendicular legs labeled "B⊥dl, no contribution", enclosed turns labeled nL, the resulting equation B = μ₀nI written beside] -->

---

## Gauss's law for magnetism

For any closed surface, in any configuration, at any time:

$$\oint \vec{B} \cdot d\vec{A} = 0$$

The right-hand side is zero — not $Q_{\text{magnetic}}/\mu_0$, just zero. Because there is no magnetic charge. Every magnetic field line that enters a closed surface must exit it somewhere else. Field lines have no sources and no sinks; they form closed loops.

This is Maxwell's second equation. It is empirical in the same sense that Gauss's law for $\vec{E}$ would be empirical without knowing that electric charges exist — we accept it because it matches every measurement. In 1931, Dirac showed that if a single magnetic monopole existed anywhere in the universe, it would force the quantization of electric charge. The argument is beautiful: a monopole and an electron, interacting quantum-mechanically, produce a phase constraint that requires the product of their charges to be quantized. Since electric charges are quantized (they come in units of $e$), the existence of monopoles would explain why.

Decades of searching have found nothing. The current limits from the LHC's MoEDAL experiment, from IceCube cosmic-ray data, and from dedicated underground detectors are very strong. If monopoles exist, they are either very rare, very heavy, or confined to conditions we haven't accessed. Until one is found, the right-hand side of Gauss's law for $\vec{B}$ is zero, and charge quantization remains an empirical fact without a theoretical explanation.

![side-by-side comparison of Gauss's law for E and Gauss's law for B — left: closed surface with electric field lines diverging outward from a positive charge inside (∮E·dA = Q/ε₀, non-zero RHS), right: closed surface w...](../images/09-sources-magnetic-fields-fig-06.png)
*Figure 9.6 — Inside the MRI*

<!-- → [IMAGE: side-by-side comparison of Gauss's law for E and Gauss's law for B — left: closed surface with electric field lines diverging outward from a positive charge inside (∮E·dA = Q/ε₀, non-zero RHS), right: closed surface with magnetic field lines forming closed loops passing through — every line that enters also exits (∮B·dA = 0, zero RHS) — annotations explaining "electric charges exist" vs. "no magnetic charges observed"] -->

---

## The 2019 SI redefinition of the ampere

Before 2019, the ampere had a definition that reads like a physics problem:

> "The ampere is the constant current which, when maintained in two straight parallel conductors of infinite length, of negligible circular cross-section, and placed 1 metre apart in vacuum, would produce between these conductors a force of exactly $2 \times 10^{-7}$ newton per metre of length."

This definition is exactly the formula $F/L = \mu_0 I_1 I_2/(2\pi d)$ inverted: with $I_1 = I_2 = 1$ A and $d = 1$ m, the force is $2 \times 10^{-7}$ N/m if and only if $\mu_0 = 4\pi \times 10^{-7}$ T·m/A. So the old definition made $\mu_0$ exact by fiat, while making the ampere depend on an unrealizable mechanical experiment (infinite wires of zero cross-section).

In May 2019, the entire SI was reorganized around fixed values of fundamental constants. The ampere was redefined by pinning the elementary charge:

$$e = 1.602\,176\,634 \times 10^{-19} \text{ C} \quad \text{(exact, by definition)}$$

One ampere is now the flow of exactly $1/e \approx 6.241 \times 10^{18}$ elementary charges per second. The practical consequence: $\mu_0$ is no longer exact. It is now a measured quantity, with experimental value very close to $4\pi \times 10^{-7}$ T·m/A but with a small uncertainty. For this course, we use $\mu_0 = 4\pi \times 10^{-7}$ T·m/A with no loss of accuracy.

The conceptual move is the interesting part. Every SI base unit — the kilogram, the second, the meter, the ampere, the kelvin, the mole, the candela — is now defined by fixing one or more fundamental constants of nature. The units become consequences of the constants rather than the constants being consequences of the units. This is a philosophical improvement: the same definitions would be understood by any civilization that had measured the same physical constants, regardless of its history or location.

<!-- → [TABLE: old vs. new ampere definition — rows: basis, what is exact, what is measured, practical consequence; columns: pre-2019 and post-2019] -->

---

## Worked example: two parallel wires

Two long parallel wires, separation $d = 5$ cm, carrying currents $I_1 = 10$ A and $I_2 = 5$ A in the same direction. Find (a) the field at the midpoint between them and (b) the force per unit length on wire 2.

**(a) Field at the midpoint.** The midpoint is at distance $d/2 = 2.5$ cm from each wire.

Wire 1 produces $B_1 = \mu_0 I_1/(2\pi \cdot d/2) = (4\pi \times 10^{-7})(10)/(2\pi \times 0.025) = 8.0 \times 10^{-5}$ T.

Wire 2 produces $B_2 = \mu_0 I_2/(2\pi \cdot d/2) = 4.0 \times 10^{-5}$ T.

Now the directions. At the midpoint, wire 1 (to the left, say) produces a field pointing downward; wire 2 (to the right) produces a field pointing upward — opposite directions. Both currents run the same way, so both fields curl the same way around their respective wires, but at the midpoint they point in opposite directions. The net field:

$$B_{\text{net}} = B_1 - B_2 = 8.0 \times 10^{-5} - 4.0 \times 10^{-5} = 4.0 \times 10^{-5} \text{ T}$$

in the direction set by the stronger wire.

**(b) Force per unit length on wire 2.** Wire 2 sits in wire 1's field at distance $d = 5$ cm:

$$B_1(d) = \frac{\mu_0 I_1}{2\pi d} = \frac{(4\pi \times 10^{-7})(10)}{2\pi(0.05)} = 4.0 \times 10^{-5} \text{ T}$$

Force per unit length: $F/L = I_2 B_1 = (5)(4.0 \times 10^{-5}) = 2.0 \times 10^{-4}$ N/m, directed toward wire 1. Same-direction currents attract.

**What this reveals.** Superposition for $\vec{B}$ works exactly as for $\vec{E}$: compute the field from each source, take the vector sum. The direction check is the place mistakes happen — working through the right-hand rule explicitly at each step is not optional.

**The limit.** The infinite-wire formula $B = \mu_0 I/(2\pi r)$ is exact only for infinite wires. For a finite wire of length $\ell$, the field at perpendicular distance $r$ from the midpoint is $B = (\mu_0 I/4\pi r)(\sin\theta_1 + \sin\theta_2)$ where $\theta_1$ and $\theta_2$ are the half-angles subtended by the wire's ends. As $\ell \to \infty$, both $\theta \to \pi/2$ and the formula recovers $\mu_0 I/(2\pi r)$.

---

## Common misconceptions

**"Magnetic field lines start on north poles and end on south poles."** They form closed loops everywhere. Inside a bar magnet, the field lines continue from south to north, completing the loop. The poles are where the lines emerge into the space outside the magnet — not sources or sinks, just places where the closed loops cross the boundary.

**"Ampère's law only works for symmetric configurations."** It is always true. Symmetry determines whether it's a useful computational shortcut, exactly as with Gauss's law for $\vec{E}$.

**"The solenoid field is uniform throughout the interior."** For an infinite solenoid. At the ends of a real finite solenoid, the field drops. At the geometric end face, $B \approx \frac{1}{2}\mu_0 n I$ — half the interior value. Do not apply $B = \mu_0 nI$ at the ends.

**"Since the magnetic force does no work, it can't accelerate a charged particle."** The magnetic force $q\vec{v} \times \vec{B}$ is always perpendicular to $\vec{v}$, so it does no work on the particle and doesn't change its speed. But it does change the direction of $\vec{v}$ — that's what bending a charged particle in a cyclotron or in Earth's field is. Deflection, not acceleration in the energy sense.

---

## Exercises

**Warm-up 1.** *(Biot-Savart for a long wire — tests: $B = \mu_0 I / 2\pi r$ with direction)* A long straight wire carries $I = 8$ A in the $+\hat{z}$ direction. Find $|\vec{B}|$ and its direction at perpendicular distances (a) $r = 2$ cm and (b) $r = 8$ cm from the wire. By what factor does the field change between the two points? Verify this matches the $1/r$ dependence.

**Warm-up 2.** *(Circular loop on axis — tests: $B_z(z)$ formula and center value)* A circular loop of radius $R = 4$ cm carries $I = 3$ A. Find $\vec{B}$ (a) at the center of the loop and (b) on the axis at $z = R = 4$ cm. For (b), evaluate the formula numerically. Then estimate what you'd expect from the $1/z^3$ far-field approximation at $z = 4$ cm and explain why the approximation is poor at this distance.

**Warm-up 3.** *(Solenoid — tests: $B = \mu_0 n I$, inverting for required current)* A solenoid is 20 cm long with 1200 total turns, carrying $I = 2.5$ A. (a) Find $n$ in turns/meter. (b) Find $B$ at the center. (c) What current would be needed to double the field? (d) What is the approximate field at the end face of the solenoid?

**Application 1.** *(Parallel wires, superposition — tests: vector sum of fields from two sources)* Two long parallel wires are 8 cm apart. Wire 1 carries 6 A to the right; wire 2 carries 4 A to the right. Find the magnetic field magnitude and direction at (a) the midpoint between them, (b) a point 4 cm to the left of wire 1 (on the far side from wire 2), (c) a point 4 cm to the right of wire 2. For each, draw a quick sketch confirming the direction.

**Application 2.** *(Ampère's law, solid cylinder — tests: $I_\text{enc}$ at interior vs. exterior points)* A solid copper wire of radius $R = 2$ mm carries a total current $I = 10$ A uniformly distributed through its cross-section. Use Ampère's law to find $\vec{B}$ at (a) $r = 1$ mm (inside), (b) $r = 2$ mm (at the surface), (c) $r = 4$ mm (outside). Sketch $B(r)$ for $0 \leq r \leq 8$ mm, labeling the kink at $r = R$.

**Application 3.** *(Force between wires — tests: $F/L$ formula with sign)* Two long parallel wires are 3 cm apart. Wire 1 carries 5 A; wire 2 carries 10 A in the opposite direction. (a) Find the force per unit length on each wire. (b) Is the force attractive or repulsive? (c) If $I_2$ is reversed to be in the same direction as $I_1$, how does the force change in magnitude and direction?

**Synthesis 1.** *(Helmholtz coils — tests: superposition of two loops)* Two identical circular loops of radius $R$, each carrying current $I$ in the same sense, are placed coaxially a distance $R$ apart (the Helmholtz configuration). The field at the midpoint between them is the sum of the two loops' on-axis fields evaluated at $z = R/2$ from each loop center. (a) Write the expression for the field at the midpoint. (b) Compute numerically for $R = 5$ cm and $I = 2$ A. (c) The Helmholtz configuration is chosen because the field is unusually uniform near the midpoint — show that $dB/dz = 0$ at the midpoint by computing the derivative of the total field there.

**Synthesis 2.** *(MRI back-calculation — tests: $B = \mu_0 n I$ inverted with realistic numbers)* A clinical 3 T MRI solenoid is 1.2 m long with 4200 total turns of superconducting wire. (a) Find $n$. (b) What current is required to produce $B = 3$ T? (c) Superconducting wire has essentially zero resistance; compute the power dissipated compared to copper wire with resistivity $\rho = 1.7 \times 10^{-8}$ Ω·m and cross-sectional area $A = 1$ mm² at the same current. Why does MRI require superconductors?

**Challenge.** *(Earth's magnetic dipole)* Earth's magnetic dipole moment is approximately $m = 8 \times 10^{22}$ A·m². (a) Model Earth's field as a magnetic dipole. Compute the predicted field magnitude at Earth's magnetic pole (on the surface, directly above the dipole, at distance $r = 6.4 \times 10^6$ m). Use the on-axis dipole formula $B = \mu_0 m/(2\pi r^3)$. Compare to the measured value of roughly $6 \times 10^{-5}$ T. (b) If this dipole moment were generated by a single circular current loop at Earth's outer-core radius ($r_{\text{core}} \approx 3.5 \times 10^6$ m), what current would the loop carry? Express as a multiple of a typical lightning bolt current (30 kA).

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

The Biot-Savart law and Ampère's law are exact in magnetostatics. No discrepancy between prediction and measurement has been observed. The 2019 SI redefinition reorganized which quantities are exact by definition, not what the physics predicts.

The claim that there are no magnetic monopoles is empirical and provisional. A confirmed detection would modify the right-hand side of Gauss's law for $\vec{B}$ to $\mu_0 Q_{\text{m,enc}}$, and the full duality between $\vec{E}$ and $\vec{B}$ in Maxwell's equations would be restored. The community keeps looking. The absence of detection over decades does not prove monopoles don't exist — it sets bounds on their abundance and mass.

## Still puzzling

*Why is electric charge quantized?* Every free particle carries a charge that is an integer multiple of $e$. We have no derivation of this from first principles — only Dirac's argument, which says "if monopoles exist, then charge quantization follows." Monopoles have not been found, and charge is quantized. The logical chain runs the wrong direction for that to be the explanation.

*Ferromagnetic permeability.* For iron, nickel, cobalt, and their alloys, $\mu_r \gg 1$ and is strongly nonlinear — the material's magnetization depends on its history (hysteresis). Transformer cores and inductor cores use these materials to confine flux. The simple $B = \mu_0 H$ relation that underlies this chapter's formulas does not apply there.

*Magnetic monopole searches.* MoEDAL at the LHC, IceCube, and dedicated underground detectors continue operating. Each year without detection tightens the bound. If we eventually find one, it will be the most important discovery in physics since the Higgs. If we never find one, we will not understand why charge is quantized.

---

**Tags:** Biot-Savart law, Ampère's law, solenoid, permeability, magnetic flux, magnetic monopole, ampere, SI redefinition, parallel wires
