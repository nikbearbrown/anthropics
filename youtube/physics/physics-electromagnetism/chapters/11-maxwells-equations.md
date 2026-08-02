# Chapter 11 — Maxwell's Equations and Electromagnetic Waves

*The payoff. Maxwell's addition completes the equations, and light falls out.*

---

In 1862, James Clerk Maxwell was working at King's College London on a mathematical theory of electricity and magnetism. He had taken Faraday's intuitive picture of fields filling space and translated it into equations. Coulomb, Ampère, Faraday — he had them all. And then he found a contradiction.

The pre-Maxwell version of Ampère's law says: the line integral of $\vec{B}$ around any closed loop equals $\mu_0$ times the current passing through that loop. Take a wire charging a capacitor. Draw an Amperian loop around the wire. Now choose two different surfaces bounded by that same loop: a flat disk pierced by the wire, and a bag-shaped surface that slips between the capacitor plates. Both surfaces share the same boundary — the loop — so Ampère's law gives the same left-hand side. But the right-hand sides differ. The flat disk has a real current through it. The bag, which threads through the gap between the plates where no charge moves, has no current through it at all. Same loop, same equation, two different answers.

Maxwell's fix was to add a term. Where pre-Maxwell Ampère saw only current as the source of $\vec{B}$, Maxwell added the *changing electric flux* as an equally valid source:

$$\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt}$$

The extra term is the **displacement current** $I_d = \varepsilon_0\, d\Phi_E/dt$. Between the capacitor plates, the electric flux is growing as charge builds; the displacement current through the bag-shaped surface exactly equals the conduction current through the flat disk. Contradiction resolved.

Then Maxwell did something else. He asked: in a vacuum — no charges, no currents — are there nontrivial solutions to the completed equations? And he found oscillating ones. And those oscillations have a speed:

$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$$

Plugging in the measured values of $\mu_0$ and $\varepsilon_0$, which had been determined from electrostatic and magnetostatic bench experiments with no reference to light:

$$c = \frac{1}{\sqrt{(4\pi \times 10^{-7})(8.854 \times 10^{-12})}} \approx 3 \times 10^8 \text{ m/s}$$

That is the speed of light, measured by Fizeau and Foucault in the 1850s. In 1864, Maxwell wrote: *"We can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena."*

Every equation in the ten preceding chapters was building toward this moment.

---

## The four equations

Here, together for the first time, are Maxwell's equations in integral form. Each one is a chapter you've already read.

$$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0} \tag{1}$$

$$\oint \vec{B} \cdot d\vec{A} = 0 \tag{2}$$

$$\oint \vec{E} \cdot d\vec{\ell} = -\frac{d\Phi_B}{dt} \tag{3}$$

$$\oint \vec{B} \cdot d\vec{\ell} = \mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d\Phi_E}{dt} \tag{4}$$

Equation (1) is Gauss's law from Chapter 3: electric flux through any closed surface equals the enclosed charge divided by $\varepsilon_0$. Equation (2) is Gauss's law for magnetism from Chapter 9: no magnetic monopoles. Equation (3) is Faraday's law from Chapter 10: changing magnetic flux drives circulation of the electric field. Equation (4) is Ampère's law from Chapter 9, plus Maxwell's new term.

The four equations say everything. Every electric and magnetic phenomenon — static fields, circuits, induction, light, radio, X-rays — follows from them. The rest of physics, including quantum mechanics, is a separate subject. But the classical electromagnetic world is entirely encoded here.

<!-- → [TABLE: four Maxwell equations — columns: number, name, integral equation, physical content in plain English, chapter where it was introduced] -->

For students who have seen divergence and curl, the differential forms are:

$$\nabla \cdot \vec{E} = \rho/\varepsilon_0, \qquad \nabla \cdot \vec{B} = 0, \qquad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \qquad \nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$

These are local statements at every point in space — equivalent to the integral forms via Stokes' theorem and the divergence theorem, but more elegant, and the form in which they're typically written in graduate physics.

---

## The displacement current

The added term in equation (4) deserves careful attention, because it is the thing that makes everything else in this chapter possible.

$I_d = \varepsilon_0\, d\Phi_E/dt$ has units of current but is not a flow of charge. It is the magnetic effect of a *changing electric field*. Before Maxwell, the known sources of $\vec{B}$ were: moving charges (steady currents). After Maxwell, the sources are: moving charges *and* changing electric flux.

Symmetry-seekers will notice what this does: Faraday's law (equation 3) says changing $\vec{B}$ creates circulating $\vec{E}$. Maxwell's addition to equation (4) says changing $\vec{E}$ creates circulating $\vec{B}$. The two fields can create each other. And when they do, the creation is self-sustaining. A changing $\vec{E}$ makes a changing $\vec{B}$; that changing $\vec{B}$ makes a changing $\vec{E}$; which makes a changing $\vec{B}$; and so on, propagating through empty space.

That propagation is light.

![side-by-side panels showing the two cross-creation laws — left: Faraday, a changing B (shown as decreasing flux through a loop) driving circulating E; right: Maxwell, a changing E (growing flux between capacitor plate...](../images/11-maxwells-equations-fig-01.png)
*Figure 11.1 — Maxwell's Paradox*

<!-- → [IMAGE: side-by-side panels showing the two cross-creation laws — left: Faraday, a changing B (shown as decreasing flux through a loop) driving circulating E; right: Maxwell, a changing E (growing flux between capacitor plates) driving circulating B — arrows and labels showing the direction of each induced field] -->

---

## The wave equation

In a source-free vacuum — no charges, no currents — Maxwell's equations become:

$$\nabla \cdot \vec{E} = 0, \qquad \nabla \cdot \vec{B} = 0, \qquad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \qquad \nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$

Take the curl of the third equation:

$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B}) = -\mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

Apply the vector identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$. In source-free vacuum, $\nabla \cdot \vec{E} = 0$, so the first term vanishes:

$$\boxed{\nabla^2 \vec{E} = \mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}}$$

This is the wave equation. Compare it to the standard form $\nabla^2 f = (1/v^2)\,\partial^2 f/\partial t^2$: the wave speed is $v = 1/\sqrt{\mu_0\varepsilon_0} = c$. An identical derivation starting from the fourth equation gives the same wave equation for $\vec{B}$.

The manipulation is clean, but the surprise is not in the algebra. The surprise is that $\mu_0$ and $\varepsilon_0$ were measured independently — one from the force between magnets, one from the force between charges — and their product, when combined here, gives $1/c^2$. Maxwell did not put $c$ into the equations. He found it there.

![diagram of the wave equation derivation — starting from Faraday and Ampère-Maxwell equations at the top, arrow down showing "take curl of Faraday", arrow to "substitute Ampère-Maxwell on the right", arrow to the boxed...](../images/11-maxwells-equations-fig-02.png)
*Figure 11.2 — Maxwell's Four Equations*

<!-- → [IMAGE: diagram of the wave equation derivation — starting from Faraday and Ampère-Maxwell equations at the top, arrow down showing "take curl of Faraday", arrow to "substitute Ampère-Maxwell on the right", arrow to the boxed wave equation, final arrow to "wave speed = 1/√(μ₀ε₀) = c"] -->

---

## Plane wave solutions

The simplest solutions to the wave equation are **plane waves** — fields that depend only on one spatial coordinate and time. For a wave propagating in the $+\hat{x}$ direction:

$$\vec{E}(x, t) = E_0 \cos(kx - \omega t)\,\hat{y}, \qquad \vec{B}(x, t) = B_0 \cos(kx - \omega t)\,\hat{z}$$

Substituting into Maxwell's equations in vacuum yields three constraints that the fields must satisfy:

**Dispersion**: $\omega = ck$, equivalently $\lambda f = c$. The wave's temporal and spatial oscillation rates are tied together by the wave speed.

**Amplitude ratio**: $E_0 = cB_0$. In SI units, $E$ is much larger than $B$ in absolute terms — for sunlight at Earth, $E_0 \approx 870$ V/m while $B_0 \approx 2.9$ µT. The ratio $E_0/B_0 = c \approx 3 \times 10^8$ m/s.

**Transverse geometry**: $\vec{E}$, $\vec{B}$, and the propagation direction are mutually perpendicular. $\vec{E} \times \vec{B}$ points along the propagation direction. Neither $\vec{E}$ nor $\vec{B}$ has a component along the propagation direction. This is not an assumption — it follows from $\nabla \cdot \vec{E} = 0$ in vacuum: the spatial variation of a plane wave along $\hat{x}$ requires the field components perpendicular to $\hat{x}$ to be the wave.

**Polarization** is the direction of $\vec{E}$ in the transverse plane. Linear polarization: $\vec{E}$ oscillates back and forth along a fixed direction. Circular: $\vec{E}$ rotates while maintaining constant magnitude. Elliptical: the general case. Sunlight is unpolarized — a superposition of all polarization orientations; a polarizing filter selects one.

![3D perspective diagram of a plane EM wave propagating along +x̂ — E field shown as orange arrows oscillating along ŷ, B field as purple arrows oscillating along ẑ, propagation direction along x̂, the three vectors lab...](../images/11-maxwells-equations-fig-03.png)
*Figure 11.3 — Plane Electromagnetic Wave*

<!-- → [IMAGE: 3D perspective diagram of a plane EM wave propagating along +x̂ — E field shown as orange arrows oscillating along ŷ, B field as purple arrows oscillating along ẑ, propagation direction along x̂, the three vectors labeled and shown perpendicular to each other, a few wavelengths of the wave shown along x] -->

---

## Energy and the Poynting vector

Where is the energy in an electromagnetic wave?

The energy density of an EM field is

$$u = \frac{1}{2}\varepsilon_0 E^2 + \frac{B^2}{2\mu_0}$$

The first term is the electric energy density from Chapter 5. The second is the magnetic energy density. In a plane wave, they are equal at every instant: $u_E = u_B$. You can verify this from $E_0 = cB_0$ and $c = 1/\sqrt{\mu_0\varepsilon_0}$ — the numbers work out exactly.

The energy flux — power per unit area carried by the wave — is described by the **Poynting vector**:

$$\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$$

The direction is along propagation (since $\vec{E} \times \vec{B}$ points that way). The magnitude $|\vec{S}|$ is the instantaneous power per unit area passing through a surface perpendicular to the propagation direction. For a plane wave, $\vec{S}$ oscillates in time; the time-averaged intensity is:

$$I = \langle|\vec{S}|\rangle = \frac{E_0^2}{2\mu_0 c} = \frac{c\varepsilon_0 E_0^2}{2}$$

For sunlight at Earth's surface: $I \approx 1000$ W/m². Plug in to find the peak fields: $E_0 \approx 870$ V/m, $B_0 \approx 2.9$ µT.

This is also the result Feynman found strange enough to spend several lectures on. In a simple DC circuit, the energy does not flow through the wires — it flows through the electromagnetic field surrounding the wires, described by exactly this Poynting vector. The wires guide the field; the field carries the energy. The result surprised many when it was first understood, and it should surprise you too.

EM waves also carry momentum. For a wave with intensity $I$ hitting a surface:

$$P_{\text{rad}} = I/c \text{ (absorbed)}, \qquad P_{\text{rad}} = 2I/c \text{ (perfectly reflected)}$$

Solar radiation pressure at Earth: roughly $9 \times 10^{-6}$ N/m² — small enough to ignore for most purposes, but real enough to matter for spacecraft trajectory planning and to provide the thrust for solar sails. JAXA's IKAROS spacecraft, launched in 2010, was the first to demonstrate interplanetary propulsion by photon pressure alone.

![radiation pressure diagram — a plane wave (labeled intensity I) incident on two surfaces side by side: left surface labeled "absorber, P_rad = I/c" with a single arrow showing force in propagation direction; right sur...](../images/11-maxwells-equations-fig-04.png)
*Figure 11.4 — Electromagnetic Spectrum*

<!-- → [IMAGE: radiation pressure diagram — a plane wave (labeled intensity I) incident on two surfaces side by side: left surface labeled "absorber, P_rad = I/c" with a single arrow showing force in propagation direction; right surface labeled "perfect reflector, P_rad = 2I/c" with wave bouncing back and a double arrow — student should see the factor-of-2 comes from momentum reversal] -->

![Poynting vector diagram — plane wave propagating along +x̂ with E along ŷ and B along ẑ, the cross product E×B shown pointing along +x̂ labeled as S (energy flux), with a flat surface perpendicular to propagation show...](../images/11-maxwells-equations-fig-05.png)
*Figure 11.5 — Poynting Vector*

<!-- → [IMAGE: Poynting vector diagram — plane wave propagating along +x̂ with E along ŷ and B along ẑ, the cross product E×B shown pointing along +x̂ labeled as S (energy flux), with a flat surface perpendicular to propagation showing "I watts per square meter flowing through this surface"] -->

---

## The electromagnetic spectrum

All electromagnetic waves obey the same wave equation and travel at the same speed $c$ in vacuum. They differ only in frequency — and therefore in wavelength ($\lambda = c/f$) and in photon energy ($E = hf$, though that's Chapter 13's quantum story).

Radio waves and gamma rays are not different phenomena that happen to share a name. They are literally the same wave — Maxwell's oscillating fields — separated by fourteen orders of magnitude in frequency. That their effects are so different (you can hear a radio wave's effect through a speaker; a gamma ray's effect is ionizing radiation that damages DNA) is a consequence of how much energy each photon carries and how matter responds to fields at different frequencies. The underlying wave is one thing.

<!-- → [TABLE: electromagnetic spectrum — columns: region name, approximate frequency range, approximate wavelength, photon energy range, representative applications — rows from radio through gamma] -->

The span from radio to gamma is not the full story. Below radio, there are extremely-low-frequency (ELF) waves used to communicate with submerged submarines; above gamma, there is no known upper limit. The entire range is one family.

---

## Hertz's confirmation

Maxwell predicted EM waves in 1864. In 1887, Heinrich Hertz at Karlsruhe deliberately generated and detected them for the first time.

His apparatus: a spark-gap oscillator, essentially a capacitor discharging rapidly through an inductor, producing oscillations near 100 MHz. His detector: a small wire loop across the lab, sized to be resonant at the same frequency. When the oscillator fired, sparks appeared in the detector loop — even when the detector was shielded from the oscillator's light.

Hertz then did exactly what a physicist should do: he measured. He showed the waves propagate at $c$ by reflecting them off a metal wall and producing standing waves whose spacing he measured. He showed they could be reflected, refracted, and polarized — all properties of Maxwell's predicted transverse oscillations. His experiments were definitive.

Hertz reportedly dismissed the practical implications: *"It's of no use whatsoever... this is just an experiment that proves Maestro Maxwell was right."* Marconi began commercial radio telegraphy between England and Newfoundland in 1901, fourteen years after Hertz's experiment, four years after Hertz's death. Every wireless device in the world runs on the physics Hertz confirmed.

![Hertz experiment schematic — left: spark-gap oscillator (inductor + capacitor, sparking electrode) labeled "transmitter, ~100 MHz"; right: small resonant wire loop with gap labeled "receiver — sparks appear when trans...](../images/11-maxwells-equations-fig-06.png)
*Figure 11.6 — Hertz's 1887 Spark-Gap Experiment*

<!-- → [IMAGE: Hertz experiment schematic — left: spark-gap oscillator (inductor + capacitor, sparking electrode) labeled "transmitter, ~100 MHz"; right: small resonant wire loop with gap labeled "receiver — sparks appear when transmitter fires"; between them: wavy lines representing the EM wave; a metal wall shown to the right of the receiver labeled "reflecting wall used to create standing waves and measure λ"] -->

---

## Worked example: the displacement current in a charging capacitor

A parallel-plate capacitor with plate area $A$ and separation $d$ is charging at rate $dV/dt$. Show that the displacement current between the plates equals the conduction current in the wire.

**Conduction current.** The charge on the plates is $Q = CV = (\varepsilon_0 A/d)V$. The current in the wire is $I_c = dQ/dt = (\varepsilon_0 A/d)(dV/dt)$.

**Electric flux between the plates.** The field between (parallel-plate approximation) is $E = V/d$. The flux through a surface placed between the plates is $\Phi_E = EA = VA/d$.

**Displacement current through that surface:**

$$I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \varepsilon_0 \cdot \frac{A}{d} \cdot \frac{dV}{dt}$$

This equals $I_c$ exactly. The flat disk surface (real current) and the bag-shaped surface (no real current, only growing flux) give the same answer for the Ampère-Maxwell integral. The added term is not an approximation or a patch — it is required by charge conservation.

**Numbers.** With $A = 10^{-4}$ m², $d = 10^{-3}$ m, $dV/dt = 10^6$ V/s:

$$I_c = I_d = \frac{(8.85 \times 10^{-12})(10^{-4})}{10^{-3}} \times 10^6 \approx 0.9 \text{ µA}$$

Small, but measurable. And the magnetic field this displacement current creates between the plates is the same as if a wire had carried 0.9 µA through the gap. Maxwell's term is physically real.

---

## Common misconceptions

**"Maxwell invented the displacement current to make his equations consistent."** The displacement current is required by charge conservation, not by mathematical aesthetics. At a charging capacitor, the pre-Maxwell equations violate charge conservation in non-steady situations. The fix restores conservation; mathematical consistency is a consequence.

**"The displacement current is a real flow of charge between the plates."** No. In a vacuum gap, no charge moves. The displacement current is the magnetic effect of a changing electric field. It has the units and the magnetic consequences of a current, but it is not a movement of charge.

**"Light is a different phenomenon from radio waves."** Same wave, different frequency. One equation, one speed, fourteen decades of frequency.

**"Light travels at $c$ everywhere."** In vacuum. In a dielectric with constant $\kappa$ and relative permeability $\mu_r$, the wave speed is $c/\sqrt{\kappa\mu_r}$. In glass, roughly $2 \times 10^8$ m/s. This slowing is the basis of refraction and of fiber-optic dispersion management.

---

## Exercises

**Warm-up 1.** *(Maxwell's equations — tests: matching equations to physical content)* State the four Maxwell equations in integral form. For each one: (a) identify which earlier chapter first introduced it, (b) state in one plain-English sentence what it says, (c) identify whether it involves a flux integral or a circulation integral of $\vec{E}$ or $\vec{B}$.

**Warm-up 2.** *(Wave speed — tests: computing $c$ from $\mu_0$ and $\varepsilon_0$)* Using $\mu_0 = 4\pi \times 10^{-7}$ T·m/A and $\varepsilon_0 = 8.854 \times 10^{-12}$ C²/(N·m²), compute $c = 1/\sqrt{\mu_0\varepsilon_0}$. Show explicitly that the units of $1/\sqrt{\mu_0\varepsilon_0}$ reduce to m/s.

**Warm-up 3.** *(Plane wave properties — tests: three constraints from Maxwell's equations)* A plane EM wave in vacuum has electric field amplitude $E_0 = 300$ V/m and frequency $f = 2.4 \times 10^9$ Hz (WiFi band). Find: (a) wavelength $\lambda$, (b) wavenumber $k = 2\pi/\lambda$, (c) magnetic field amplitude $B_0$, (d) the direction of $\vec{B}$ if $\vec{E}$ points along $\hat{y}$ and the wave propagates along $+\hat{z}$.

**Application 1.** *(Displacement current — tests: $I_d = \varepsilon_0\, d\Phi_E/dt$ and equality with conduction current)* A parallel-plate capacitor has circular plates of radius $r = 6$ cm and plate separation $d = 2$ mm. It is charging at $dV/dt = 5 \times 10^4$ V/s. (a) Find the conduction current in the wire. (b) Find the electric field between the plates as a function of $V$. (c) Find the displacement current through a surface placed between the plates. (d) Verify (a) and (c) are equal. (e) What is the magnetic field at the rim of the plates ($r = 6$ cm) due to the displacement current?

**Application 2.** *(Intensity and Poynting vector — tests: $I = c\varepsilon_0 E_0^2/2$, field amplitudes from intensity)* A laser pointer delivers $P = 5$ mW through a circular beam of diameter 2 mm. (a) Find the intensity $I$ in W/m². (b) Find the peak electric field $E_0$. (c) Find the peak magnetic field $B_0$. (d) Compare $E_0$ to the electric field 1 cm from a 1 µC point charge in vacuum. (e) Compare $B_0$ to Earth's surface magnetic field (~$5 \times 10^{-5}$ T).

**Application 3.** *(Radiation pressure — tests: $P_\text{rad} = I/c$ and $2I/c$, force on an area)* A solar sail has area $A = 196$ m² (14 m × 14 m, like IKAROS). Solar intensity at Earth is $I \approx 1360$ W/m². (a) Find the radiation force on the sail, assuming it is a perfect reflector. (b) Find the acceleration if the sail plus spacecraft has mass 310 kg. (c) Express the force in comparison to 1 µN (about the thrust of an ion engine at minimum). (d) After one year of continuous thrust, what velocity would the spacecraft accumulate from this force alone? Comment on whether solar sails are practical.

**Synthesis 1.** *(Equal energy densities — tests: $u_E = u_B$ in a plane wave)* For a plane wave with $E_0 = 500$ V/m: (a) Find $B_0$. (b) Compute $u_E = \frac{1}{2}\varepsilon_0 E_0^2$ and $u_B = B_0^2/(2\mu_0)$ at the instant both fields are at their peak amplitude. (c) Verify they are equal by substituting $B_0 = E_0/c$ and using $c^2 = 1/(\mu_0\varepsilon_0)$. (d) The time-averaged intensity is $I = c\varepsilon_0 E_0^2/2$ — explain in one sentence why there is a factor of $\frac{1}{2}$ compared to the peak energy density times $c$.

**Synthesis 2.** *(Spectrum and wave properties — tests: $\lambda = c/f$, recognizing the span)* For each of the following, find the wavelength and classify the wave as radio, microwave, infrared, visible, UV, X-ray, or gamma: (a) $f = 87.9$ MHz (an FM radio station), (b) $f = 2.45$ GHz (microwave oven), (c) $f = 6 \times 10^{14}$ Hz (orange light), (d) $f = 3 \times 10^{17}$ Hz (medical X-ray), (e) $f = 10^{20}$ Hz (cosmic gamma ray). For (c), find $E_0$ from the intensity of sunlight ($I \approx 1000$ W/m²).

**Challenge.** *(Wave equation from Maxwell's equations)* Starting from Faraday's law in differential form $\nabla \times \vec{E} = -\partial \vec{B}/\partial t$ and the Ampère-Maxwell law in vacuum $\nabla \times \vec{B} = \mu_0\varepsilon_0\,\partial \vec{E}/\partial t$, derive the wave equation for $\vec{E}$ in the following steps: (a) take the curl of both sides of Faraday's law; (b) apply the vector identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$; (c) use Gauss's law in vacuum ($\nabla \cdot \vec{E} = 0$) to simplify; (d) substitute the Ampère-Maxwell law for $\nabla \times \vec{B}$; (e) identify the wave speed. Then repeat the analogous steps starting from the Ampère-Maxwell law to obtain the wave equation for $\vec{B}$.

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

Maxwell's equations are exact in the classical domain. A confirmed deviation at any scale where classical EM currently works would force a rewrite — none has been found. At very small scales, quantum electrodynamics supersedes them; the classical equations are the appropriate limit. At cosmological scales, general relativity provides corrections; for laboratory work these are immeasurable.

Hertz's 1887 experiment confirmed the predicted waves exist and propagate at $c$. The century-plus of engineering that followed — radio, radar, television, fiber optics, mobile phones, GPS — has been continuous engineering validation. When Maxwell's equations predict the gain of an antenna, the cutoff frequency of a waveguide, or the dispersion of a pulse in optical fiber, they are right.

## Still puzzling

*Why is $\mu_0\varepsilon_0 = 1/c^2$?* In SI units this looks like a numerical coincidence. In natural units where $c = 1$, it's a tautology. The deeper structure is that Maxwell's equations are Lorentz-covariant — $\vec{E}$ and $\vec{B}$ are components of a single antisymmetric tensor, mixed into each other by changes of reference frame. The "coincidence" is the covariance; the speed of light is not a property of light specifically but of the geometry of spacetime.

*The displacement current and the photon.* In quantum electrodynamics, what classical theory calls a displacement current corresponds to virtual-photon exchange. The oscillating field that carries the wave is quantized into photons. The classical picture is the smooth limit of a quantum process.

*The asymmetry between $\vec{E}$ and $\vec{B}$.* Equation (1) has a source on the right-hand side: charge. Equation (2) has zero. If magnetic monopoles existed, equation (2) would acquire a source term, and the full symmetry between $\vec{E}$ and $\vec{B}$ in Maxwell's equations would be restored. Without them, the equations are asymmetric in a way that has no deep theoretical explanation — only the empirical fact that no monopole has ever been found.

---

**Tags:** Maxwell's equations, displacement current, wave equation, electromagnetic wave, Poynting vector, EM spectrum, Hertz, light, plane wave
![Radiation Pressure](../images/11-maxwells-equations-fig-07.png)
*Figure 11.7 — Radiation Pressure*

