# Chapter 5 — Capacitance and Dielectrics

*The bridge from electrostatics to circuits, and the energy that lives in the field.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define capacitance $C = Q/V$ as a geometric property of a pair of conductors and identify the units.
2. **(Apply)** Derive the capacitance of parallel plates, coaxial cylinders, and concentric spheres from Gauss's law and the potential definition.
3. **(Apply)** Compute energy stored in a capacitor using $U = Q^2/2C = \frac{1}{2}CV^2$ and interpret the result as energy density $u_E = \frac{1}{2}\varepsilon_0 E^2$ in the field.
4. **(Apply)** Use the series and parallel combination rules — series capacitors add reciprocally, parallel capacitors add directly — and explain why the direction is opposite to resistor combinations.
5. **(Analyze)** Explain qualitatively how a dielectric increases capacitance and quantitatively use $C_{\text{die}} = \kappa C_0$.
6. **(Apply)** Build a charging/discharging RC-circuit simulator that makes the time constant $\tau = RC$ visible.

---

## Opening case: the camera flash

A modern compact camera flash fires for about a millisecond and delivers somewhere around 7 joules of light energy in that pulse. The flash bulb draws something like 7000 watts during the discharge — many times what the small lithium battery in the camera can deliver continuously. The battery would die in seconds if it had to power the flash directly.

The trick is a capacitor. The battery slowly charges a small electrolytic capacitor — typically 150 microfarads — to about 300 volts. Stored energy: $U = \frac{1}{2} C V^2 = \frac{1}{2}(150 \times 10^{-6})(300)^2 \approx 6.75$ J. When the photographer presses the shutter, a switch discharges the capacitor through the xenon flash tube in about a millisecond. Average power during discharge: 6.75 J / 0.001 s = 6750 W. The battery accumulates energy slowly; the capacitor delivers it fast.

This pattern — a slow source charging a capacitor, then a quick controlled discharge through a load — is everywhere in modern electronics. Defibrillators deliver 150 joules in a few milliseconds through paddles to a patient's chest. Camera flashes do 7 J. Particle accelerators store gigajoules in capacitor banks for pulsed magnetic experiments. Every smartphone power supply has dozens of capacitors handling momentary current spikes the battery cannot.

The chapter ahead is the physics that makes capacitors work: a geometric property called capacitance, energy stored in the electric field between conductors, and the dynamics of charging through a resistor.

---

## Core concept

### Capacitance

Two conductors carrying equal and opposite charges $+Q$ and $-Q$ — call them the "plates" of a capacitor — sit at potentials $V_+$ and $V_-$. The potential difference between them is $V = V_+ - V_-$.

The **capacitance** is the ratio:

$$C = \frac{Q}{V}$$

Units: farad (F) = coulomb/volt. The farad is a large unit; practical capacitors range from picofarads ($10^{-12}$ F) to thousands of farads (supercapacitors).

The key conceptual point: $C$ depends only on the geometry of the conductors and on the material between them. *Not on $Q$ or $V$*. Double the charge on the plates and the voltage doubles; their ratio is fixed by the geometry.

### Three canonical geometries

**Parallel plates.** Area $A$, separation $d$ (with $d \ll \sqrt{A}$ to ignore edge effects). Apply Gauss's law inside, between the plates: surface charge $\sigma = Q/A$ on each plate; field $E = \sigma/\varepsilon_0$ between them. Potential difference: $V = E \cdot d = Qd/(\varepsilon_0 A)$. Capacitance:

$$C_{\text{parallel plates}} = \frac{\varepsilon_0 A}{d}$$

**Cylindrical (coaxial).** Inner conductor radius $a$, outer conductor inner radius $b > a$, length $L$ (with $L \gg b$ to ignore end effects). By Gauss's law in cylindrical symmetry, field between the cylinders is $E(r) = \lambda/(2\pi\varepsilon_0 r)$ where $\lambda = Q/L$. Integrate to get $V = (\lambda/(2\pi\varepsilon_0)) \ln(b/a) = (Q/(2\pi\varepsilon_0 L)) \ln(b/a)$. Capacitance:

$$C_{\text{cylindrical}} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}$$

**Spherical (concentric).** Inner sphere radius $a$, outer sphere inner radius $b > a$. By Gauss's law in spherical symmetry, field between them is $E(r) = kQ/r^2$. Integrate: $V = kQ(1/a - 1/b) = kQ(b - a)/(ab)$. Capacitance:

$$C_{\text{spherical}} = \frac{4\pi\varepsilon_0 ab}{b - a}$$

In the limit $b \to \infty$ (an isolated sphere): $C = 4\pi\varepsilon_0 a$.

In each derivation, the recipe is: (1) compute $\vec{E}$ between the conductors using Gauss's law; (2) integrate $-\vec{E} \cdot d\vec{\ell}$ to get the potential difference; (3) divide $Q$ by $V$. Gauss's law (Chapter 3) is doing the heavy lifting.

### Energy stored

Build up charge on a capacitor gradually. At intermediate stage $q$, the voltage is $q/C$ and the work to move the next increment $dq$ from one plate to the other is $dW = (q/C) \, dq$. Total work to go from 0 to $Q$:

$$U = \int_0^Q \frac{q}{C} \, dq = \frac{Q^2}{2C} = \frac{1}{2} C V^2 = \frac{1}{2} Q V$$

Three equivalent expressions for the same energy.

**Where is the energy?** Rewrite for parallel plates using $C = \varepsilon_0 A/d$ and $V = Ed$:

$$U = \frac{1}{2}(\varepsilon_0 A/d)(Ed)^2 = \frac{1}{2}\varepsilon_0 E^2 \cdot (Ad)$$

The volume between the plates is $A \cdot d$. So the energy per unit volume — the **energy density** of the field — is

$$u_E = \frac{1}{2}\varepsilon_0 E^2$$

This generalizes. Anywhere in space where there is an electric field, there is energy density $\frac{1}{2}\varepsilon_0 E^2$. The energy is *in the field*, not on the plates. The plates are just the physical setup that creates the field; the field is where the energy lives.

This insight — that fields themselves carry energy — was Maxwell's. By Chapter 11 the field carries energy in propagating waves; by Chapter 12 those waves are light, and the same $u_E$ tells you how much energy is in sunlight crossing a square meter of your back yard.

### Combinations

**Parallel capacitors share the voltage.** Two capacitors $C_1, C_2$ connected in parallel both feel the same $V$ across them. Charge on each: $Q_1 = C_1 V$, $Q_2 = C_2 V$. Total: $Q = (C_1 + C_2) V$. Equivalent capacitance:

$$C_{\text{eq, parallel}} = C_1 + C_2 + \cdots$$

Parallel capacitances add directly.

**Series capacitors share the charge.** Two capacitors $C_1, C_2$ in series get the same $Q$ on each (the charge that flowed through the series path). Voltage across each: $V_1 = Q/C_1$, $V_2 = Q/C_2$. Total voltage: $V = V_1 + V_2 = Q(1/C_1 + 1/C_2)$. Equivalent capacitance:

$$\frac{1}{C_{\text{eq, series}}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$$

Series capacitances add reciprocally.

**Resistors are the opposite.** Series resistors add directly; parallel resistors add reciprocally. The inversion catches students who have just memorized the resistor rules from a circuits course. The physical reason: capacitance is "ease of storing charge"; resistance is "obstruction to current." Putting more storage paths in parallel adds storage capacity directly; putting more obstruction paths in parallel reduces total obstruction.

### Dielectrics

Insert an insulating slab between the plates of a capacitor. Two atomic-scale things happen:

1. **Induced dipoles.** In each atom or molecule, the electron cloud shifts slightly opposite to the external field; the nucleus shifts slightly with it. Each atom becomes a tiny dipole.
2. **Permanent dipoles align** in polar materials (water, plastics with permanent dipoles). Random thermal motion partially overcomes the field's alignment torque; the population of aligned dipoles exceeds the anti-aligned.

Both effects produce **bound surface charges** on the dielectric: positive on the face nearer the negative plate, negative on the face nearer the positive plate. The bound charges produce a field *opposing* the external field. Inside the dielectric, the field is reduced:

$$E_{\text{in dielectric}} = E_0 / \kappa$$

where $\kappa$ is the **dielectric constant** (or relative permittivity). Common values: vacuum $\kappa = 1$ (by definition), air $\kappa \approx 1.0006$, paper $\kappa \approx 3.7$, glass $\kappa \approx 5$–10, water $\kappa \approx 80$, strontium titanate $\kappa \approx 310$.

With the dielectric, for fixed $Q$ on the plates, $V$ drops by $\kappa$. So $C = Q/V$ increases by $\kappa$:

$$C_{\text{die}} = \kappa C_0$$

Practical benefit: smaller capacitor, more capacitance, higher breakdown voltage for the same physical size. Modern ceramic capacitors with $\kappa$ in the thousands fit microfarads into millimeter-scale packages.

### RC dynamics

Connect a capacitor through a resistor $R$ to a battery of EMF $\varepsilon$. Kirchhoff's voltage law:
$$\varepsilon = IR + Q/C$$

With $I = dQ/dt$:
$$\frac{dQ}{dt} = \frac{\varepsilon}{R} - \frac{Q}{RC}$$

First-order linear ODE. With $Q(0) = 0$, solution:
$$Q(t) = C\varepsilon \left(1 - e^{-t/RC}\right)$$

Current decays exponentially:
$$I(t) = \frac{\varepsilon}{R} e^{-t/RC}$$

The **time constant** is

$$\tau = RC$$

After one $\tau$: $Q = C\varepsilon(1 - 1/e) \approx 0.632 \, C\varepsilon$ — 63% charged. After $5\tau$: 99.3% charged. The same $\tau$ governs *discharging* (battery disconnected, capacitor shorted through $R$): $Q(t) = Q_0 e^{-t/RC}$.

**An energy puzzle.** Total energy delivered by the battery during full charging: $W_{\text{battery}} = \varepsilon Q_{\text{final}} = \varepsilon \cdot C\varepsilon = C\varepsilon^2$. Energy stored in the capacitor at $t = \infty$: $U_C = \frac{1}{2} C \varepsilon^2$. The other half: $W_R = \frac{1}{2} C \varepsilon^2$ — dissipated as heat in the resistor.

*Exactly half the battery's energy is dissipated in the resistor during charging, regardless of $R$.* You cannot charge a capacitor through a resistor without losing half the energy to heat. This is one of the cleaner counterintuitive results in elementary E&M.

---

## Worked example: a capacitor with a dielectric

A parallel-plate capacitor with $A = 1.0$ cm² and $d = 0.1$ mm in air. (a) Capacitance? (b) If connected to a 12 V battery, how much charge accumulates? (c) Disconnect the battery; slide a mica sheet ($\kappa = 7$) into the gap. What happens to $Q$, $V$, $E$, and $U$?

**(a) Capacitance.** $C_0 = \varepsilon_0 A / d = (8.85 \times 10^{-12})(10^{-4})/(10^{-4}) = 8.85 \times 10^{-12}$ F = 8.85 pF.

**(b) Charge.** $Q = C_0 V = (8.85 \times 10^{-12})(12) = 1.06 \times 10^{-10}$ C ≈ 0.11 nC. About $6.6 \times 10^8$ electrons.

**(c) Insert mica with battery disconnected.** Now the *charge* on the plates is fixed (no path to flow). But $C$ jumps to $\kappa C_0 = 7 \times 8.85$ pF = 62 pF.
- $Q$ stays at 0.11 nC.
- $V = Q/C = 1.06 \times 10^{-10} / (62 \times 10^{-12}) = 1.7$ V. The voltage drops by $\kappa$.
- $E = V/d = 17,000$ V/m, also dropped by $\kappa$ from the original $1.2 \times 10^5$ V/m.
- $U = Q^2/(2C) = (1.06 \times 10^{-10})^2 / (2 \cdot 62 \times 10^{-12}) = 9 \times 10^{-11}$ J. The stored energy *dropped* by $\kappa$ as well.

Where did the energy go? Into the work done by the capacitor's field *pulling the dielectric into the gap*. The dielectric is attracted into the region of strong field; the system loses electrostatic energy as the slab slides in. If you removed the dielectric, you'd have to do work *against* this force — that work goes back into the stored field energy.

**The lesson.** Inserting a dielectric with the battery disconnected lowers $E$, $V$, and $U$. Inserting it with the battery *connected* keeps $V$ fixed and instead increases $Q$ and $U$ (the battery pumps in extra charge).

**The limit.** The formulas $C_{\text{die}} = \kappa C_0$ and $E = E_0/\kappa$ assume the dielectric *uniformly fills* the gap. Partial fillings (half-thickness dielectric, dielectric slab not extending to the edges) require the series/parallel-combination reasoning.

---

## Common misconceptions

**"A capacitor stores charge."** It stores *equal and opposite* charges — net zero charge in the device as a whole. What it stores is *energy*, in the field between the plates.

**"The energy is on the plates."** The energy is in the electric field. Energy density: $u_E = \frac{1}{2}\varepsilon_0 E^2$, distributed throughout the volume where the field is nonzero. Empty plates with no field between them store no energy regardless of how big they are.

**"Series capacitors add."** Parallel capacitors add; series capacitors add *reciprocally*. The inverse of resistors. Easy to get wrong.

**"Larger capacitance means larger voltage rating."** Independent properties. A 100 µF / 6.3 V capacitor and a 100 µF / 50 V capacitor are different parts. The voltage rating is set by dielectric strength × thickness, not by the capacitance value.

**"You can charge a capacitor through a resistor with arbitrarily small energy loss if you use a small enough resistor."** No. Half of the battery's energy is dissipated in the resistor regardless of $R$. To avoid the loss, you'd need to charge through an inductor (which introduces oscillation; energy bounces between $L$ and $C$).

---

## Exercises

**Warm-up (Apply).** A parallel-plate capacitor has $C_0 = 100$ pF in vacuum. (a) If the gap is filled with a material of $\kappa = 4$, what is $C$? (b) The capacitor is charged to 100 V (in vacuum) and the battery is removed. The dielectric is inserted. Find $Q$, $V$, $E$, and $U$ before and after.

**Apply.** Two capacitors $C_1 = 10$ µF and $C_2 = 20$ µF. Find $C_{\text{eq}}$ for (a) series, (b) parallel connections. For each combination connected to a 12 V battery, find the charge on each capacitor.

**Apply.** A 100 µF capacitor is charged to 250 V. (a) How much energy is stored? (b) If the capacitor discharges through a 50 Ω resistor, what is the time constant? (c) After how long is the energy stored reduced to half the initial value?

**Apply + Analyze.** A parallel-plate capacitor has plates of area $A = 50$ cm², separation $d = 1$ mm. The space is half-filled with a dielectric slab of $\kappa = 4$ extending across half the gap (so $d/2$ of vacuum and $d/2$ of dielectric, in series). Find $C$. (Hint: treat the two halves as capacitors in series with their respective dielectrics.)

**Challenge (Synthesize).** Show that for any RC charging from 0 to $Q_{\text{final}} = C\varepsilon$, the energy delivered by the battery is $C\varepsilon^2$ and exactly half is dissipated in the resistor. Independent of the value of $R$. (Hint: $W_R = \int_0^\infty I^2 R \, dt$ with $I(t) = (\varepsilon/R) e^{-t/RC}$.)

---

## LLM Exercises

### Build the RC charge/discharge simulator (`05-capacitor-rc.html`)

> **Show.** RC charging: $Q(t) = C\varepsilon(1 - e^{-t/RC})$. RC discharging: $Q(t) = Q_0 e^{-t/RC}$. Time constant $\tau = RC$.
>
> **Say.** Build an interactive RC-circuit charging/discharging visualizer with parallel dielectric demonstration.
>
> **Constrain.** D3 v7. Panel 1: schematic circuit with battery $\varepsilon$, resistor $R$, capacitor $C$. Sliders for $R$ (1 Ω to 1 kΩ), $C$ (1 µF to 1000 µF), $\varepsilon$ (1 V to 20 V). Toggle: charge / discharge mode. Live plots of $Q(t)$, $V_C(t)$, $I(t)$, and $U(t)$ updating in real time. Show $\tau = RC$ as a vertical reference line on the time axis. Animate orange dots flowing along wires to represent current; speed proportional to $|I|$. Panel 2: parallel-plate capacitor with dielectric slider $\kappa \in [1, 100]$. Show: $E$ between plates (color-mapped), $C$ readout, $U$ readout. Filename: `05-capacitor-rc.html`.
>
> **Verify.** (a) Charging from zero: $Q$ rises toward $C\varepsilon$, reaching $\approx 63\%$ at $t = \tau$. (b) Doubling $R$ doubles $\tau$ (curves stretch out by factor 2). (c) Inserting dielectric (Panel 2) with battery disconnected: $E$ drops by $\kappa$, $V$ drops by $\kappa$. (d) The energy dissipated in the resistor during charging equals the energy stored in the capacitor at the end.

### Exploration

- Charge a 100 µF capacitor through a 100 Ω resistor with $\varepsilon = 10$ V. Measure $\tau$ from the curve. (Should be 10 ms.)
- Reduce $R$ by a factor of 10. Does charging speed up by a factor of 10? Does the *energy lost in the resistor* change?
- In the dielectric panel: insert a $\kappa = 80$ dielectric (water-like). What happens to the stored energy if the battery is connected? Disconnected?

### Extension prompt (chapter bridge)

> **Show.** I've seen capacitors store and discharge energy through resistors. Now I want to see what happens when the charge flows — what current and voltage do in more complex circuits.
>
> **Say.** Build a DC circuit analyzer: drag-and-drop resistors and batteries onto a grid, automatically solve for branch currents and node voltages.
>
> **Constrain.** Use nodal analysis (Kirchhoff's laws). Display branch currents as animated orange arrows. Display node voltages as labels. Show power dissipated in each resistor.
>
> **Verify.** A simple series circuit: current is the same through every resistor. A simple parallel circuit: voltage is the same across each.

Save as `05b-dc-circuits-preview.html`. This is the lead-in to Chapter 7.

---

## What would change my mind

The central claims of this chapter — capacitance as a geometric property, energy density $\frac{1}{2}\varepsilon_0 E^2$ in the field, $\kappa$ as the dielectric's response to an external field — are mature physics. The energy-density expression is what gets imported, with magnetic equivalent $u_B = B^2/(2\mu_0)$, into Maxwell's wave-propagation calculations in Chapter 11. If $u_E = \frac{1}{2}\varepsilon_0 E^2$ were wrong, electromagnetic radiation would carry the wrong amount of energy, and a century of antenna and radio engineering would show systematic error. It doesn't. The dielectric constant's microscopic theory (Clausius-Mossotti, Onsager corrections) is well-established at the level needed. At very high frequencies or in exotic materials, $\kappa$ becomes complex (frequency-dependent loss); the chapter ignores this.

## Still puzzling

- *The half-energy-lost result for RC charging.* Independent of $R$. There is no way to charge a capacitor through a passive resistor without losing exactly half. The only ways around it: (a) charge through an inductor instead, accepting LC oscillation; (b) use a switching converter that approximates near-lossless charging in the limit of infinite switching frequency. Both are taught in advanced electronics; the chapter mentions but doesn't develop them.
- *Frequency-dependent $\kappa$.* In an AC circuit, the dielectric's response varies with frequency. Capacitors aren't quite the same component at 1 kHz as at 1 GHz. Intro treatment uses $\kappa$ as a constant; reality is more complicated.
- *Supercapacitor energy density.* As of 2026, modern supercapacitors store 10–20 Wh/kg, an order of magnitude below lithium-ion batteries but with much higher power density. Research into materials with higher $\kappa$ — dipole glasses, layered ceramics, ionic-liquid double layers — continues. The energy-density-vs-power-density tradeoff frontier is moving.

---

**Tags:** capacitance, dielectric, energy density, RC circuit, time constant, supercapacitor, polarization, Leyden jar

