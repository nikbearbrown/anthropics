# Chapter 11 — Maxwell's Equations and Electromagnetic Waves

*The payoff. Maxwell's addition completes the equations, and light falls out.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the four Maxwell equations in integral form and identify which preceding chapter each one corresponds to.
2. **(Analyze)** Explain the physical motivation for the displacement current: the charging-capacitor inconsistency in pre-Maxwell Ampère's law.
3. **(Apply)** Derive the wave equation from Maxwell's equations in vacuum and identify the wave speed $c = 1/\sqrt{\mu_0 \varepsilon_0}$.
4. **(Apply)** Use plane-wave solutions: relate $E_0$, $B_0$, $\omega$, $k$, and the transverse geometry.
5. **(Apply)** Compute the Poynting vector, intensity, and radiation pressure for a plane wave.
6. **(Apply)** Build a transverse-EM-wave visualizer showing $\vec{E}$ and $\vec{B}$ oscillating perpendicular to each other and to the direction of propagation.

---

## Opening case: Maxwell's surprise

In 1862, James Clerk Maxwell was working at King's College London on a unified mathematical theory of electricity and magnetism. He had taken Faraday's intuitive picture of fields filling space and translated it into equations. He had taken the experimental relations — Coulomb, Ampère, Faraday — and assembled them into a coherent set. There was one problem.

The pre-Maxwell Ampère's law said that the line integral of $\vec{B}$ around any closed loop equals $\mu_0$ times the current passing through that loop. Maxwell noticed an inconsistency that only shows up in non-steady situations — specifically, a charging capacitor. Apply Ampère's law to an Amperian loop encircling a wire that runs into a capacitor plate. Now choose two different surfaces bounded by that loop: one a flat disk pierced by the wire (encloses the wire's current), the other a bag-shape detoured between the capacitor plates (encloses no wire). Both surfaces are bounded by the *same* loop, so Ampère's law gives the same left-hand side. But the right-hand sides differ. Same equation, two different answers. Contradiction.

Maxwell's fix was a missing term — the **displacement current** — that counts the changing electric flux *as if it were a current*. Adding it, the equation becomes
$$\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}$$
and the contradiction dissolves: the bag-shape surface that encloses no wire still encloses the *changing electric flux* between the plates; the displacement current through that surface exactly equals the conduction current through the disk surface.

Then Maxwell did one more thing. He combined his completed equations and asked: in a vacuum, with no charges or currents, are there nontrivial solutions? Yes — oscillating ones. And those oscillations have a speed:
$$c = 1/\sqrt{\mu_0 \varepsilon_0}$$
Plugging in the measured values of $\mu_0$ and $\varepsilon_0$ (from electrostatic and magnetostatic experiments, which had nothing to do with light):
$$c = 1/\sqrt{(4\pi \times 10^{-7})(8.854 \times 10^{-12})} \approx 3 \times 10^8 \text{ m/s}$$
That is the speed of light, measured by Fizeau, Foucault, and others in the 1850s. Maxwell wrote, in 1864:
> "We can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena."

This is the chapter where everything in Chapters 1–10 pays off. Maxwell's equations unify electricity, magnetism, and light into one framework. Hertz confirmed it experimentally in 1887. Marconi commercialized it as radio in 1901. Every wireless device you use is applied Maxwell. Every photon of sunlight that hits your skin is an oscillation in the very fields you've been building all semester.

---

## Core concept

### Maxwell's four equations (integral form)

| # | Name | Equation | Physical content |
|---|---|---|---|
| 1 | Gauss's law for $\vec{E}$ | $\oint \vec{E} \cdot d\vec{A} = Q_{\text{enc}}/\varepsilon_0$ | Electric flux out of a closed surface = enclosed charge / $\varepsilon_0$ |
| 2 | Gauss's law for $\vec{B}$ | $\oint \vec{B} \cdot d\vec{A} = 0$ | No magnetic monopoles |
| 3 | Faraday's law | $\oint \vec{E} \cdot d\vec{\ell} = -d\Phi_B/dt$ | Changing magnetic flux drives circulation of $\vec{E}$ |
| 4 | Ampère-Maxwell law | $\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}} + \mu_0\varepsilon_0 \, d\Phi_E/dt$ | Current AND changing $\Phi_E$ drive circulation of $\vec{B}$ |

Chapter mappings:
- Equation 1: Chapter 3.
- Equation 2: Chapter 9.
- Equation 3: Chapter 10.
- Equation 4: Chapter 9 (Ampère part); the displacement current term is *new* — Maxwell's contribution.

### The displacement current

The added term in (4) is

$$I_d = \varepsilon_0 \frac{d\Phi_E}{dt}$$

It has units of current but it is not a flow of charge. It is the *magnetic effect of a changing electric field*. In the charging-capacitor scenario from the chapter opening, no charge flows through the space between the plates, but the electric flux between them grows as charge builds on the plates. The displacement current accounts for this and makes the equation consistent with charge conservation.

**Maxwell's claim, more carefully.** Before Maxwell: a steady current creates $\vec{B}$; nothing else does. With Maxwell: either a steady current *or* a changing electric flux creates $\vec{B}$. The second clause is what makes electromagnetic waves possible.

### Maxwell's equations in differential form

For students who have seen the divergence and curl operators:

| # | Equation |
|---|---|
| 1 | $\nabla \cdot \vec{E} = \rho/\varepsilon_0$ |
| 2 | $\nabla \cdot \vec{B} = 0$ |
| 3 | $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$ |
| 4 | $\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \, \partial \vec{E}/\partial t$ |

These are local statements at every point in space, equivalent to the integral forms via Stokes' theorem and the divergence theorem.

### Deriving the wave equation

In a *source-free* region (vacuum, no charges, no currents): $\rho = 0$, $\vec{J} = 0$. Maxwell's equations become:
$$\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$

Take the curl of equation (3):
$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Use the vector identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$. With $\nabla \cdot \vec{E} = 0$:
$$-\nabla^2 \vec{E} = -\mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Or:
$$\boxed{\nabla^2 \vec{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}}$$

This is the **wave equation** for $\vec{E}$. Comparing to the canonical wave equation $\nabla^2 f = (1/v^2)\partial^2 f/\partial t^2$, the wave speed is

$$v = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$$

Plugging in values: $v \approx 2.998 \times 10^8$ m/s = $c$, the measured speed of light.

The same derivation works for $\vec{B}$ (take curl of equation 4, substitute equation 3). Both $\vec{E}$ and $\vec{B}$ satisfy the same wave equation with the same speed.

### Plane wave solutions

The simplest solutions: traveling plane waves. For a wave propagating in $+\hat{x}$:
$$\vec{E}(x, t) = E_0 \cos(kx - \omega t)\,\hat{y}, \qquad \vec{B}(x, t) = B_0 \cos(kx - \omega t)\,\hat{z}$$

Three constraints from Maxwell's equations:
1. **Dispersion**: $\omega = ck$, equivalently $\lambda f = c$.
2. **Amplitude ratio**: $E_0 = c B_0$.
3. **Transverse geometry**: $\vec{E} \perp \vec{B} \perp$ direction of propagation; $\vec{E} \times \vec{B}$ points in the propagation direction.

Why transverse: Gauss's law in source-free vacuum is $\nabla \cdot \vec{E} = 0$, which for a plane wave requires the wave's variation to be perpendicular to the propagation direction.

**Polarization** refers to the direction of $\vec{E}$ in the transverse plane. Linear polarization: $\vec{E}$ oscillates along a fixed direction. Circular: $\vec{E}$ rotates while maintaining magnitude. Elliptical: the general case.

### Energy and the Poynting vector

The energy density of an EM field is
$$u = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2\mu_0} B^2$$

In a plane wave, these two contributions are equal at every instant: $u_E = u_B$. The wave carries equal energy in $\vec{E}$ and $\vec{B}$.

The **Poynting vector** is the energy flux:
$$\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$$

Direction: along propagation. Magnitude: power per unit area (W/m²). For a plane wave, the time-averaged magnitude (intensity) is
$$I = \langle |\vec{S}|\rangle = \frac{E_0^2}{2\mu_0 c} = \frac{c \varepsilon_0}{2} E_0^2$$

For sunlight at Earth's surface: $I \approx 1000$ W/m². Peak $E_0 \approx 870$ V/m. Peak $B_0 \approx 2.9$ µT.

### Radiation pressure

EM waves carry momentum. For a wave with intensity $I$ absorbed by a surface:
$$P_{\text{rad}} = I/c \text{ (absorber)}, \quad P_{\text{rad}} = 2I/c \text{ (perfect reflector)}$$

Solar radiation pressure at Earth: $\sim 9 \times 10^{-6}$ N/m² for an absorber. Small but cumulative — the basis of solar-sail propulsion (JAXA's IKAROS, 2010, was the first interplanetary demonstration).

### The electromagnetic spectrum

All EM waves obey the same equation. They differ only in frequency (and wavelength: $\lambda = c/f$).

| Region | Frequency (Hz) | Wavelength | Photon energy | Examples |
|---|---|---|---|---|
| Radio | $< 10^9$ | $> 30$ cm | $< 4$ µeV | FM, AM, mobile |
| Microwave | $10^9$ to $10^{12}$ | 30 cm to 0.3 mm | 4 µeV to 4 meV | WiFi, GPS, radar, ovens |
| Infrared | $10^{12}$ to $4\times10^{14}$ | 0.3 mm to 700 nm | 4 meV to 1.7 eV | Heat, fiber optics |
| Visible | $4\times10^{14}$ to $8\times10^{14}$ | 700 to 400 nm | 1.7 to 3.1 eV | Sight |
| UV | $8\times10^{14}$ to $10^{16}$ | 400 to 10 nm | 3.1 to 124 eV | Sunburn |
| X-ray | $10^{16}$ to $10^{19}$ | 10 nm to 0.01 nm | 124 eV to 124 keV | Medical imaging |
| Gamma | $> 10^{19}$ | $< 0.01$ nm | $> 124$ keV | Nuclear, cosmic |

Radio waves and gamma rays are the same wave at frequencies separated by $10^{14}$. Their physics is one chapter's worth of equations.

### Hertz's confirmation

In 1887, Heinrich Hertz at the Technische Hochschule Karlsruhe built the first device to deliberately *generate and detect* EM waves. A spark-gap oscillator (a capacitor discharging through an inductor) produced oscillations near 100 MHz. A small wire loop placed across the lab developed sparks when the oscillator fired, even with the receiver shielded from the transmitter's light. Hertz confirmed:
1. Waves propagate at speed $c$ (measured by reflection and standing-wave techniques).
2. Waves can be reflected, refracted, polarized — same as light.
3. Waves are transverse (polarization filters work).

Maxwell's 1864 prediction became experimental fact in 1887. Hertz himself dismissed the practical utility ("it's of no use whatsoever..."). Marconi (1895–1901) commercialized it as radio. Within a century, radio engineering had reshaped human communication.

---

## Worked example: a charging capacitor

A parallel-plate capacitor, plate area $A$, separation $d$, is charging at rate $dV/dt = 10^6$ V/s. Show that the displacement current between the plates equals the conduction current in the wire.

**Setup.** As the capacitor charges, $Q = CV = (\varepsilon_0 A/d) V$. Conduction current in the wire: $I_c = dQ/dt = (\varepsilon_0 A/d)(dV/dt)$.

**Electric field between the plates** (treating plates as infinite, ignoring fringing): $E = V/d$. Electric flux through a surface placed between the plates: $\Phi_E = EA = (V/d)A$.

**Displacement current** through that same surface:
$$I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \varepsilon_0 \frac{A}{d} \frac{dV}{dt} = \frac{\varepsilon_0 A}{d}\frac{dV}{dt}$$

Compare to $I_c = (\varepsilon_0 A/d)(dV/dt)$. They're identical.

The bag-shape surface (Maxwell's worry) and the flat disk give the same answer for the Ampère-Maxwell integral. The displacement current term is the bridge that connects "current piercing the disk" to "changing flux through the bag."

**Numerical check.** Take $A = 1$ cm² = $10^{-4}$ m², $d = 1$ mm, $dV/dt = 10^6$ V/s. Then $I_c = I_d = (8.85 \times 10^{-12} \cdot 10^{-4}/10^{-3})(10^6) = 8.85 \times 10^{-7}$ A = 0.9 µA. A small but real current.

**The lesson.** Charge conservation requires Maxwell's added term. The displacement current is not a flow of charge; it's the magnetic effect of a changing $\vec{E}$. Without it, the equations contradict each other in non-steady situations.

**The limit.** The derivation treats the capacitor's geometry idealized (infinite plates, neglected fringing). For real, finite capacitors, $\vec{E}$ leaks out the edges and the displacement-current argument requires more care — but the fundamental result, that $I_c + I_d$ is the right driving term, is correct.

---

## Common misconceptions

**"Maxwell invented the displacement current to save his equations from inconsistency."** Backwards. The physical issue is *charge conservation*: charge has to be conserved at every point, every instant. Maxwell noticed Ampère's law violated this at a charging capacitor. The added term restores conservation. The mathematical consistency of the equations falls out.

**"The displacement current is a real flow of charge between the capacitor plates."** No. There is no charge moving between the plates in a vacuum gap. The displacement current is a term in Ampère's law that captures the magnetic effect of a changing electric field. It has units of current but is not a current.

**"Light is different from radio waves."** Both are EM waves obeying the same wave equation with the same speed. Their only difference is frequency.

**"The speed of light is constant everywhere."** It is constant in vacuum. In a material with dielectric constant $\kappa$ and relative permeability $\mu_r$, the wave speed is $v = c/\sqrt{\kappa \mu_r}$ — slower. In glass, light moves at about $2 \times 10^8$ m/s.

**"$\vec{E}$ and $\vec{B}$ are independent fields."** They're not. They are components of one electromagnetic field; what is "electric" to one observer is partly "magnetic" to another moving observer. Chapter 12 returns to this Lorentz-mixing.

---

## Exercises

**Warm-up (Apply).** State the four Maxwell equations in integral form. For each, identify (a) which preceding chapter it comes from, (b) whether it relates a *flux* or a *circulation* of $\vec{E}$ or $\vec{B}$ to its source.

**Apply.** Compute the speed of EM waves from $\mu_0 = 4\pi \times 10^{-7}$ and $\varepsilon_0 = 8.854 \times 10^{-12}$. Show the units work out to m/s.

**Apply.** A plane EM wave in vacuum has electric-field amplitude $E_0 = 200$ V/m, frequency $f = 10^{12}$ Hz (infrared). Find: (a) wavelength, (b) magnetic-field amplitude, (c) average intensity, (d) radiation pressure on a perfect absorber.

**Apply.** A capacitor with circular plates of radius 5 cm and separation 1 mm is charging at $dV/dt = 10^4$ V/s. (a) Find the conduction current in the wire. (b) Find the displacement current between the plates. (c) Verify they're equal.

**Apply + Analyze.** Show that for a plane EM wave, the magnetic energy density equals the electric energy density at every instant. Start from $E_0 = cB_0$ and the expressions $u_E = \frac{1}{2}\varepsilon_0 E^2$ and $u_B = B^2/(2\mu_0)$.

**Challenge (Synthesize).** Derive the wave equation for $\vec{E}$ from Maxwell's equations starting from $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$. Show each step: take curl, apply the identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$, use Gauss's law to set $\nabla \cdot \vec{E} = 0$ in vacuum, substitute Maxwell's 4th equation. Identify the wave speed.

---

## LLM Exercises

### Build the transverse EM wave visualizer (`11-em-wave.html`)

> **Show.** A plane EM wave in vacuum has $\vec{E}$ and $\vec{B}$ oscillating perpendicular to each other and to the propagation direction, with $\vec{E} \times \vec{B} \propto \hat{k}$.
>
> **Say.** Build a transverse EM wave visualizer.
>
> **Constrain.** D3 v7. Render a 3D-perspective view of a plane wave propagating along $+\hat{x}$. $\vec{E}$ oscillates along $\hat{y}$ (orange, per `DESIGN.md`); $\vec{B}$ oscillates along $\hat{z}$ (purple). Both as sine curves with the same period and phase. Sliders: amplitude (0 to 200 V/m), frequency (radio to visible to X-ray spectrum, log scale), polarization angle. Display: wavelength, frequency, period, Poynting vector magnitude. Animate by updating phase via `requestAnimationFrame`. Filename: `11-em-wave.html`.
>
> **Verify.** (a) Doubling frequency halves wavelength (since $\lambda = c/f$). (b) $E_0/B_0 = c$ (display this ratio as a check). (c) The energy density $u_E = \frac{1}{2}\varepsilon_0 E^2$ and $u_B = B^2/(2\mu_0)$ are equal at every instant.

### Exploration

- Set the frequency to FM radio (~100 MHz). Wavelength should be ~3 m.
- Set to visible green light (~$5 \times 10^{14}$ Hz). Wavelength ~600 nm.
- Vary the polarization angle. Observe how $\vec{E}$ rotates in the transverse plane.
- Verify the Poynting vector: at peak field, $|\vec{S}| = E_0 B_0 / \mu_0$. Compute and compare to the displayed value.

### Extension prompt (chapter bridge)

> **Show.** I've built a single plane wave. Now: when two plane waves with the same frequency meet, what happens?
>
> **Say.** Build a two-slit interference visualizer.
>
> **Constrain.** Two coherent point sources separated by distance $d$, emitting waves of wavelength $\lambda$. Compute the resulting intensity pattern on a screen at distance $L$. Show the wave fronts from each source, the interference pattern, and the predicted fringe spacing $\Delta y = \lambda L/d$.
>
> **Verify.** Fringe spacing matches the formula. Doubling $d$ halves the fringe spacing. Doubling $\lambda$ doubles it.

Save as `11b-two-slit-preview.html`. This is the lead-in to Chapter 12.

---

## What would change my mind

Maxwell's equations are mature, exact, and confirmed at every scale where classical EM applies. The displacement current is needed for self-consistency; without it, the equations contradict charge conservation. A confirmed deviation — a measurable phenomenon Maxwell's equations cannot explain in their domain — would force a rewrite. None has been observed. At very small scales, quantum electrodynamics (QED) supersedes classical Maxwell; the classical equations are the appropriate-limit description, not the deepest one. At cosmic scales, general relativity provides curvature corrections; for laboratory experiments these are utterly negligible.

The 1887 Hertz experiment showed that the predicted EM waves *exist* and propagate at $c$. A century of antennas, broadcast radios, microwave links, optical fibers, lasers, and wireless networks have engineered Maxwell to spec, with no failure.

## Still puzzling

- *Why is $\mu_0 \varepsilon_0 = 1/c^2$?* In SI units, this looks like a coincidence. In natural units (where $c = 1$), it's a tautology. The deeper structure (Maxwell's equations are Lorentz-covariant; $\vec{E}$ and $\vec{B}$ are components of a single tensor) shows the unification.
- *The displacement current and the photon.* In QED, the displacement current corresponds to virtual-photon exchange between charges. The classical picture is the smooth-limit version of a quantum process. The chapter ignores this; for intro purposes, the classical picture suffices.
- *What if no monopoles exist?* If they're not out there, $\nabla \cdot \vec{B} = 0$ stands. The symmetry between $\vec{E}$ and $\vec{B}$ remains asymmetric — only $\vec{E}$ has explicit sources (charges). The asymmetry is uncomfortable but empirical.

---

**Tags:** Maxwell's equations, displacement current, wave equation, electromagnetic wave, Poynting vector, EM spectrum, Hertz, light

