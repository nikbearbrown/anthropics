# Chapter 8 — Magnetism and the Magnetic Force

*Moving charges feel a force perpendicular to motion, and circle into geometry without classical analog.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the Lorentz force law $\vec{F} = q\vec{v} \times \vec{B}$ and identify why the magnetic force does no work on a moving charge.
2. **(Apply)** Compute the trajectory of a charged particle in a uniform magnetic field — circular when $\vec{v} \perp \vec{B}$, helical otherwise.
3. **(Apply)** Compute the cyclotron radius $r = mv/|q|B$ and frequency $\omega_c = |q|B/m$ for a given particle and field.
4. **(Apply)** Find the force on a current-carrying conductor in a magnetic field, $\vec{F} = I\vec{L} \times \vec{B}$, and the torque on a current loop, $\vec{\tau} = \vec{m} \times \vec{B}$.
5. **(Analyze)** Use the Hall effect to determine the sign of charge carriers in a conductor.
6. **(Apply)** Build a charged-particle trajectory simulator showing circular and helical motion in configurable fields.

---

## Opening case: the mass spectrometer

A mass spectrometer is a device used in chemistry, biology, and forensic science to identify and weigh molecules. The principle is simple. Ionize the sample so each molecule carries a known charge (typically $+e$). Accelerate the ions through a known potential difference $V$ — they emerge with kinetic energy $\frac{1}{2}mv^2 = qV$, so $v = \sqrt{2qV/m}$. Inject them into a region of uniform magnetic field $\vec{B}$ perpendicular to their motion. They follow circular paths whose radius depends on $m$ and $v$:

$$r = \frac{mv}{qB}$$

Ions of different masses land at different positions on a detector. From the position, you read the mass; from the count, the abundance. A modern time-of-flight or quadrupole instrument can measure molecular masses to parts per million, distinguishing isotopologues, identifying drugs in urine, sequencing peptides.

The whole machine is one equation, $\vec{F} = q\vec{v} \times \vec{B}$, applied to a clean geometry. The chapter ahead is that force law, its consequences for particle trajectories, and the way it generates almost every magnetic device you use — motors, MRI scanners, hard drives, oscilloscopes, particle accelerators.

---

## Core concept

### The Lorentz force

A charge $q$ moving with velocity $\vec{v}$ in a magnetic field $\vec{B}$ feels a force

$$\vec{F} = q \vec{v} \times \vec{B}$$

Three immediate observations:
- **Direction.** $\vec{F}$ is perpendicular to both $\vec{v}$ and $\vec{B}$. Right-hand rule: fingers point along $\vec{v}$, curl toward $\vec{B}$, thumb gives $\vec{v} \times \vec{B}$ (for positive $q$; for negative, reverse).
- **Magnitude.** $|\vec{F}| = |q| v B \sin\theta$ where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$. Zero when $\vec{v} \parallel \vec{B}$; maximum when $\vec{v} \perp \vec{B}$.
- **A charge at rest feels no magnetic force.** Magnetic forces require motion.

Combined with the electric force, the total force on a charge is the **Lorentz force**:
$$\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$$

Units: $\vec{B}$ measured in **tesla** (T) = kg/(A·s²). For scale: Earth's surface field ≈ 25–65 µT. A bar magnet a few cm away: ~0.01 T. A clinical MRI: 1.5–3 T. A research MRI: 7 T. The Large Hadron Collider's bending magnets: 8.3 T.

### The magnetic force does no work

Crucial property. $\vec{F} \cdot \vec{v} = q(\vec{v} \times \vec{B}) \cdot \vec{v} = 0$ (any cross product is perpendicular to either factor). So the rate of work done by the magnetic force on the charge is identically zero:

$$P_{\text{mag}} = \vec{F} \cdot \vec{v} = 0$$

The kinetic energy of a charge in a magnetic field is conserved. The force *deflects* the charge — changes its direction — but never speeds it up or slows it down.

This is the magnetic force's deepest peculiarity. Newtonian intuition wants force to change speed. Magnetic forces only change direction. The work-energy theorem still holds; it's just that the work done by $\vec{F}_{\text{mag}}$ is structurally zero.

(Electric and other forces *can* do work and accelerate the particle; if $\vec{E}$ is also present, $W = \int q\vec{E} \cdot d\vec{r} \neq 0$ in general.)

### Circular motion in a uniform B

Set up: $\vec{B} = B\hat{z}$ uniform. Initial velocity $\vec{v}_0 = v_0 \hat{x}$ in the $xy$-plane. Initial force: $\vec{F} = q\vec{v}_0 \times \vec{B} = qv_0 B (\hat{x} \times \hat{z}) = -q v_0 B \hat{y}$ (for $q > 0$, force is in $-\hat{y}$).

The force is perpendicular to $\vec{v}$ and constant in magnitude (since $|\vec{v}|$ is constant). This is exactly the setup for uniform circular motion. Equating centripetal force to magnetic force:
$$|q|vB = mv^2/r \implies r = \frac{mv}{|q|B}$$

The **cyclotron frequency** at which the charge orbits:
$$\omega_c = v/r = \frac{|q|B}{m}, \qquad f_c = \frac{|q|B}{2\pi m}$$

Notice: the frequency is *independent of $v$*. All charges with the same $q/m$ orbit at the same rate, regardless of how fast they're moving (in the non-relativistic limit). This is why the cyclotron — Lawrence's 1930 invention — works: synchronizing the polarity of an accelerating gap to the cyclotron frequency works for any energy.

### Helical motion: $\vec{v}$ not perpendicular to $\vec{B}$

Decompose the velocity into components parallel and perpendicular to $\vec{B}$: $\vec{v} = \vec{v}_\parallel + \vec{v}_\perp$.

The parallel component feels no force ($\vec{v}_\parallel \times \vec{B} = 0$); it propagates at constant speed along the field line.

The perpendicular component circles at radius $r = mv_\perp/(|q|B)$ and frequency $\omega_c = |q|B/m$.

The combined motion is a **helix** — circular motion superimposed on uniform straight-line motion. Pitch (distance traveled along $\vec{B}$ per revolution): $p = v_\parallel \cdot (2\pi/\omega_c) = 2\pi m v_\parallel/(|q|B)$.

This is how charged particles spiral along Earth's magnetic field lines into the polar atmosphere, producing auroras.

### Mass spectrometer (the worked-example case)

Apply the formulas to the chapter opening. An ion of charge $+e$ accelerated through potential difference $V$ has KE $eV$ and speed $v = \sqrt{2eV/m}$. In a uniform $\vec{B}$ perpendicular to motion, it traces a circle of radius:

$$r = \frac{mv}{eB} = \frac{1}{B}\sqrt{\frac{2mV}{e}}$$

Two ions with the same charge and accelerating voltage but different masses: $r \propto \sqrt{m}$. A 0.1% mass difference produces a 0.05% radius difference; a detector at the right distance separates them spatially. Modern mass spectrometers refine the geometry but the core physics is this.

### The Hall effect

A current-carrying conductor — a thin strip, current $I$ flowing in $+\hat{x}$ — placed in a transverse magnetic field $\vec{B} = B\hat{z}$. The charge carriers (typically electrons in metals) feel a magnetic force perpendicular to their drift velocity. They deflect to one edge of the strip, building up surface charge there. The surface charge produces a transverse electric field that opposes the deflection; in steady state, the electric and magnetic forces balance.

**The transverse Hall voltage** that develops across the strip's width $w$:
$$V_H = \frac{I B}{n q t}$$

where $n$ is the carrier density, $q$ is the carrier charge (with sign), and $t$ is the strip thickness.

The Hall voltage's *sign* tells you the sign of the carriers. In most metals it's negative (electrons), as expected. But in some materials — copper iodide, semiconductors with hole conduction — it's positive, revealing carriers that move as if they had positive charge. This was first explained when band theory (Chapter 12 preview) showed that nearly-full bands can host current carriers that act like positive charges (holes).

Discovery: Edwin Hall, 1879. The quantum-Hall effect, discovered by von Klitzing in 1980 (Nobel 1985), is the deeply nontrivial generalization in 2D electron systems at high fields. Its precision is now used to define the SI ohm.

### Force on a current-carrying conductor

A current is moving charges. A wire of length $L$, carrying current $I$ in direction $\hat{L}$, in a magnetic field $\vec{B}$, feels force:

$$\vec{F} = I \vec{L} \times \vec{B}$$

For a more general wire shape, integrate along the wire: $\vec{F} = \int I \, d\vec{\ell} \times \vec{B}$.

This is the engine that drives electric motors. Run a current through a coil placed in a magnetic field; the resulting force on the wires pushes the coil to rotate. Every electric motor in your house — vacuum cleaner, refrigerator compressor, electric car drive — is this formula at work.

### Torque on a current loop

A rectangular current loop of area $A$ in a uniform field $\vec{B}$ feels no net force (the forces on opposite sides cancel) but a net **torque**:

$$\vec{\tau} = \vec{m} \times \vec{B}$$

where the **magnetic dipole moment** of the loop is

$$\vec{m} = NIA \hat{n}$$

with $N$ the number of turns, $I$ the current, $A$ the area enclosed, and $\hat{n}$ the unit normal to the loop (direction set by right-hand rule from the current circulation).

The loop rotates to align $\vec{m}$ with $\vec{B}$. This is the working principle of every analog ammeter, every electric motor (with commutator switching to keep the torque always in one direction), and every spinning piece of an MRI scanner (atomic magnetic moments precessing in the strong field).

Potential energy of the loop in the field: $U = -\vec{m} \cdot \vec{B}$. Minimum when $\vec{m}$ aligns with $\vec{B}$.

---

## Worked example: a proton in Earth's magnetic field

A solar-wind proton enters Earth's magnetosphere with $v = 4 \times 10^5$ m/s perpendicular to $\vec{B}$. Earth's field at the relevant altitude: $B \approx 3 \times 10^{-5}$ T. Find the cyclotron radius and period.

Proton mass $m_p = 1.67 \times 10^{-27}$ kg; charge $+e = 1.6 \times 10^{-19}$ C.

**Radius:**
$$r = \frac{mv}{|q|B} = \frac{(1.67 \times 10^{-27})(4 \times 10^5)}{(1.6 \times 10^{-19})(3 \times 10^{-5})} \approx 1.4 \times 10^5 \text{ m} = 140 \text{ km}$$

So a solar-wind proton circles in Earth's field on the scale of 100s of kilometers.

**Period:**
$$T = \frac{2\pi m}{|q| B} = \frac{2\pi (1.67 \times 10^{-27})}{(1.6 \times 10^{-19})(3 \times 10^{-5})} \approx 2.2 \text{ ms}$$

One revolution in a couple of milliseconds.

**The lesson.** Same formulas as the mass spectrometer; vastly different scales. The cyclotron radius and frequency tell you whether a charged particle's motion can be approximated as straight-line (if $r \gg$ system size) or as tightly curved (if $r \ll$ system size). For solar-wind protons in Earth's field: $r = 140$ km is small compared to Earth's diameter ($\sim 12{,}000$ km), so the protons follow field lines rather than crossing them — leading to the auroral pattern at the magnetic poles where field lines dip into the atmosphere.

**The limit.** This is non-relativistic. For very high-energy cosmic-ray protons ($v$ approaching $c$), the cyclotron radius is $\gamma m v/(|q|B)$ where $\gamma$ is the Lorentz factor — the trajectory bends less. For ultra-high-energy cosmic rays at $10^{20}$ eV, the cyclotron radius exceeds the size of our galaxy, so they aren't confined.

---

## Common misconceptions

**"Magnetic forces do work on moving charges."** They don't. $\vec{F} \perp \vec{v}$ always implies $W = 0$. The kinetic energy of a charge in a magnetic field is conserved. (If you observe acceleration, there's an electric field or another force at work — not the magnetic force alone.)

**"A current-carrying wire feels a force *because it's charged*."** It's not net-charged. The wire is electrically neutral; positive ions and electron sea cancel. The force is on the *moving charges* (the electrons), which then transfer momentum to the lattice through scattering. The macroscopic wire experiences the force.

**"Magnetic field lines start on north poles and end on south poles."** They form *closed loops*. The north and south poles are where the field lines emerge from / enter the material; the lines continue through the material's interior connecting them. There are no magnetic monopoles in the source equation (Chapter 9).

**"The cyclotron frequency depends on the particle's speed."** It doesn't (non-relativistically). $\omega_c = |q|B/m$. Faster particles trace bigger circles in the same time. This is why a fixed-frequency electric field can accelerate particles continuously in a cyclotron.

**"The Hall effect shows that current is positive in 'positive-Hall-coefficient' materials."** The current direction is the conventional positive-charge flow direction; it's a sign convention, not a physical fact. What the Hall effect tells you is the *sign of the actual charge carriers* — electrons in most metals (negative Hall coefficient), but holes in some semiconductors (positive Hall coefficient).

---

## Exercises

**Warm-up (Apply).** A proton enters a 0.5 T field at $10^6$ m/s perpendicular to $\vec{B}$. Compute the cyclotron radius and period.

**Apply.** Mass spectrometer geometry: ions of charge $+e$ accelerated through $V = 1000$ V enter a magnetic field $B = 0.2$ T perpendicular to motion. Find the radius for (a) singly-ionized $^{12}$C ($m = 12 \cdot 1.66 \times 10^{-27}$ kg = $2 \times 10^{-26}$ kg), (b) singly-ionized $^{13}$C. By how much do the radii differ?

**Apply.** A horizontal wire of length 1 m carries a current of 10 A through a uniform magnetic field of 0.5 T directed perpendicular to the wire. Find the force on the wire (magnitude and direction).

**Apply + Analyze.** Two ions, with the same kinetic energy but different masses, enter a uniform magnetic field perpendicular to motion. Show that the ratio of their cyclotron radii is $r_1/r_2 = \sqrt{m_1/m_2}$. Why doesn't the heavier one travel slower with a smaller radius?

**Apply (Hall).** A copper strip carries 10 A current in the $+\hat{x}$ direction. The strip is 1 mm thick, 1 cm wide. A 0.5 T field is applied in $+\hat{z}$. Calculate the Hall voltage. (Copper carrier density $n \approx 8.5 \times 10^{28}$ m$^{-3}$.)

**Challenge.** A square current loop of side $a$ and current $I$ in a uniform magnetic field $\vec{B}$ (perpendicular to the loop's normal) feels a torque that rotates it toward alignment. Show that the torque is $\tau = IAB$ where $A = a^2$. Find the equilibrium orientation. Find the maximum potential energy difference.

---

## LLM Exercises

### Build the charged-particle trajectory simulator (`08-particle-trajectory.html`)

> **Show.** Lorentz force: $\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$. In a uniform $\vec{B}$ alone, a charge moves in a circle (if $\vec{v} \perp \vec{B}$) or helix (otherwise).
>
> **Say.** Build a 3D trajectory simulator for a charged particle in configurable $\vec{E}$ and $\vec{B}$ fields.
>
> **Constrain.** D3 v7 for visualization (project 3D to 2D). Sliders: charge $q$ (positive/negative), mass $m$, initial velocity vector $(v_x, v_y, v_z)$, magnetic field $(B_x, B_y, B_z)$, electric field $(E_x, E_y, E_z)$. Integrate Newton's second law $m\,d\vec{v}/dt = q(\vec{E} + \vec{v} \times \vec{B})$ using RK4 with timestep $\Delta t = T_c/100$ where $T_c$ is the cyclotron period. Draw the trail of recent positions. Display cyclotron radius and frequency as readouts. Filename: `08-particle-trajectory.html`.
>
> **Verify.** (a) $\vec{v} \perp \vec{B}$, no $\vec{E}$: circular motion at the predicted radius. (b) $\vec{v}$ at angle to $\vec{B}$: helix. (c) Add $\vec{E}$ perpendicular to both $\vec{B}$ and $\vec{v}$: a drift (E×B drift) appears.

### Exploration

- Vary the magnetic field strength. Verify $r \propto 1/B$ and $\omega \propto B$.
- Set up the mass-spectrometer geometry: $V_{\text{accel}}$ → $v = \sqrt{2qV/m}$ → uniform $\vec{B}$ → radius. Try two ions of different masses but same charge. Match your hand calculation.
- Set up a crossed-field drift: $\vec{E}$ and $\vec{B}$ perpendicular. The particle drifts at velocity $\vec{v}_{\text{drift}} = \vec{E} \times \vec{B}/B^2$ on top of its circular motion. Verify.

### Extension prompt (chapter bridge)

> **Show.** Now I know what a magnetic field does to a moving charge. But: where do magnetic fields come from?
>
> **Say.** Build a magnetic field-line visualizer for various current configurations: straight wire, circular loop, solenoid cross-section.
>
> **Constrain.** Apply the Biot-Savart law to compute $\vec{B}$ at every grid point. Draw field lines by RK4 integration. Color the current with orange arrows; field lines in purple. Filename: `08b-field-from-currents-preview.html`.
>
> **Verify.** Straight wire: circular field lines around the wire. Two parallel wires, same direction: lines bunch between them. Opposite direction: lines spread out between them.

This is the lead-in to Chapter 9.

---

## What would change my mind

The Lorentz force law is exact in classical EM. It has been confirmed countless times in particle accelerators, mass spectrometers, cyclotrons, and every-day electric motors. A confirmed deviation at any scale where classical EM applies would require rewriting this chapter and Chapter 11. At relativistic speeds, the *formula* doesn't change (mass becomes $\gamma m$ in $r = mv/qB$); only the kinematic interpretation. At quantum scales, the Lorentz force emerges from the more fundamental QED interaction; its classical form remains correct in the appropriate limit.

## Still puzzling

- *No magnetic monopoles.* Chapter 9 will state this empirically. If a single magnetic monopole were ever detected, the magnetic force law would expand to include a "magnetic Coulomb" term, and the symmetry between $\vec{E}$ and $\vec{B}$ would become complete.
- *Magnetic forces don't do work — but motors do work.* Resolved by noticing that motors involve currents (so the electrons in the wire are accelerated by the magnetic force, which then transfer momentum to the lattice through scattering — and the *electric field* of the source does work on the electrons). The macroscopic motor's work comes from the source, not directly from the magnetic force on the wire. Subtle but correct.
- *Hall effect with anomalous signs.* Some materials have Hall coefficients with the "wrong" sign — explained only by band theory's holes. Quantum-Hall and anomalous-Hall effects are active research topics in condensed-matter physics.

---

**Tags:** Lorentz force, magnetic field, tesla, cyclotron, mass spectrometer, Hall effect, magnetic dipole moment, torque

