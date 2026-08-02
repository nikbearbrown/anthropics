# Chapter 22 — Magnetism

*Electricity seen from a moving train.*

---

Here is the strange thing about magnetism: you probably don't need it.

I mean that precisely. If you know Coulomb's law and you know special relativity, you can derive every magnetic phenomenon in this chapter without ever introducing a separate magnetic force. What we call magnetism turns out to be the relativistic correction to the electric force between moving charges — and the correction is not small. At ordinary current speeds, it produces forces as large as the electric force itself.

Let me show you why.

Take a long wire carrying a current. The wire is electrically neutral: for every drifting electron, there's a stationary positive ion. An electron sitting outside the wire feels no net electric force, because the wire is neutral. Now boost into the frame of the drifting electrons. In this new frame, the electrons are stationary and the positive ions are moving backward. But here's where special relativity bites: moving objects are length-contracted. The positive ions, moving in this frame, are Lorentz-contracted and therefore spaced slightly *closer together* than the stationary electrons. The wire now looks positively charged. The external electron, in this frame, feels a Coulomb attraction toward the wire.

That Coulomb force, transformed back to the lab frame, is exactly what we call the magnetic force. Magnetism is not a new force at all. It is electricity, viewed from a moving frame.

This is one of the most beautiful unifications in physics, and we will not make full use of it here — that requires the machinery of special relativity (Chapter 28). What we will do instead is learn the rules that govern magnetic phenomena: the force law, the field formulas, and the engineering consequences. But keep the deeper picture in mind. Every magnetic force in this chapter has an electric explanation in a moving frame. The two are the same thing.

<!-- → [INFOGRAPHIC: Two-panel thought experiment — (1) lab frame: neutral wire, external electron at rest, no net force; (2) electron's frame: positive ions Lorentz-contracted and crowded together, wire appears positively charged, Coulomb force attracts electron; caption: same physical situation, two frames — what is "magnetic force" in one frame is "Coulomb force" in the other] -->

---

## The field and the force

A magnetic field $\vec{B}$ is a vector field — like the electric field, it has a direction and a magnitude at every point in space. The unit is the **tesla** (T). Some scale: Earth's surface field is about $5 \times 10^{-5}$ T (50 microtesla). A refrigerator magnet is roughly $5 \times 10^{-3}$ T. A clinical MRI scanner runs at 1.5 to 3 T. The strongest continuous laboratory fields reach about 45 T. The surface of a magnetar — a type of neutron star — can hit $10^{11}$ T, enough to distort the shapes of atoms.

The force on a charge $q$ moving with velocity $\vec{v}$ through field $\vec{B}$ is

$$\boxed{\vec{F} = q\vec{v} \times \vec{B}.}$$

![3D vector diagram. Velocity v points right; magnetic field B points up; cross product v × B points out of page. For positive charge, F is along v × B; for negative charge, F is opposite. Magnitude F = qvB sin θ.](../images/22-magnetism-fig-01.png)
*Figure 22.1 — Lorentz Force — F = q v × B by the Right-Hand Rule*

This is the **Lorentz force law**. The cross product makes it geometrically precise: the force is perpendicular to both $\vec{v}$ and $\vec{B}$, with magnitude $F = qvB\sin\theta$ where $\theta$ is the angle between the velocity and the field. The direction follows the **right-hand rule**: point your fingers in the direction of $\vec{v}$, curl them toward $\vec{B}$, and your thumb points in the direction of the force on a positive charge. Negative charge reverses it.

Two consequences follow immediately from the perpendicularity of the force.

First: a charge moving *parallel* to $\vec{B}$ feels no magnetic force at all. The cross product of parallel vectors is zero. This is why cosmic rays spiral along magnetic field lines rather than being stopped by them — the component of velocity along the field is completely unaffected.

Second: the magnetic force *does no work* on a moving charge. Work is force times displacement in the direction of the force. The magnetic force is always perpendicular to the displacement. So the charge's kinetic energy — its speed — never changes because of a magnetic force. Magnetic forces steer; they do not accelerate or decelerate.

![Two panels. Left: v perpendicular to B — circular orbit with radius r = mv/(qB). Right: v has component along B — helix; perpendicular component circles, parallel component drifts steadily. Cyclotron frequency ω_c = qB/m...](../images/22-magnetism-fig-02.png)
*Figure 22.2 — Charged Particle in Uniform B — Circle When v ⊥ B, Helix Otherwise*

This is a profound constraint. It means you cannot build a perpetual-motion machine using magnets alone. It also means that the fascinating trajectories of charged particles in magnetic fields — the spirals in bubble chambers, the auroral curtains above the poles, the beam paths in particle accelerators — are all achieved by *redirecting* kinetic energy, not supplying it.

<!-- → [IMAGE: Bubble chamber photograph showing curved particle tracks — caption: each track is a charged particle spiraling in the chamber's magnetic field; the radius of curvature encodes the particle's momentum; opposite curvatures indicate opposite charges] -->

---

## Circular orbits

If a charge enters a uniform magnetic field with velocity perpendicular to $\vec{B}$, the force is always perpendicular to the velocity, pointing toward a fixed center. The particle moves in a circle. The centripetal force equation gives:

$$qvB = \frac{mv^2}{r} \implies r = \frac{mv}{qB}.$$

The radius is proportional to momentum $mv$ and inversely proportional to the charge and the field strength. Heavier particles curve less; faster particles curve less; stronger fields curve more.

![Schematic: ions accelerated through V₀ enter a uniform B region; perpendicular to B, they circle with r = mv/(qB) = √(2mV₀/q)/B. Three isotope masses produce three radii. Detector array reads m/q from landing position.](../images/22-magnetism-fig-03.png)
*Figure 22.3 — Mass Spectrometer — r ∝ √m Separates Isotopes*

This formula is the foundation of the **mass spectrometer**: ionize a substance, accelerate the ions through a known voltage, send them into a known field, measure the radius. From $r$ and the known $q$, you recover the mass. It is the primary tool of analytical chemistry, proteomics, atmospheric science, isotope geology, and drug testing. Mass spectrometers are in hospital laboratories, airport security scanners, the spacecraft we send to Mars. They work on four lines of algebra.

The same formula governs particle accelerators. At CERN's Large Hadron Collider, protons at 6.5 TeV of kinetic energy are bent around a 27-km ring by superconducting magnets at 8.4 T. Plug in: $r = mv/(qB)$. At relativistic energies, $mv$ is replaced by the relativistic momentum $p$, but the structure of the equation is identical. The size of the machine is set by the strength of magnets humanity can build and the momentum of the particles we want to steer.

<!-- → [TABLE: Circular motion in magnetic fields — columns: particle, mass, charge, speed, field (T), radius (m); rows: electron (1 mT, ~5.7 cm), proton (1 T, ~10 cm), alpha particle (1 T), LHC proton (8.4 T, ~4300 m); student should see how r = mv/qB scales across twelve orders of magnitude in mass] -->

---

## Where fields come from: currents

So far we have treated $\vec{B}$ as given — something you arrange with a magnet or a lab coil. But where do magnetic fields actually come from? The answer is the same answer as for the Lorentz force: moving charges.

![Three panels with B-field geometry. Long straight wire: B = μ₀I/(2πr) in concentric circles. Circular loop: B on axis at center = μ₀I/(2R). Solenoid: B = μ₀nI inside, ≈ 0 outside (uniform).](../images/22-magnetism-fig-04.png)
*Figure 22.4 — Magnetic Field Sources — Long Wire, Loop, Solenoid*

![Bar magnet with field lines emerging from N, looping around, and returning to S. Inside the magnet, lines continue from S to N. Any closed surface encloses zero net flux: ∮ B · dA = 0. There are no isolated magnetic charges.](../images/22-magnetism-fig-06.png)
*Figure 22.6 — Gauss for B = 0 — Field Lines Form Closed Loops, No Monopoles*

Every magnetic field in the universe is sourced by moving electric charges somewhere. The permanent magnet on your refrigerator is magnetized because the electron spins inside the iron lattice are aligned, each spinning electron acting as a tiny current loop. Earth's field comes from slowly convecting liquid iron in the outer core — a natural dynamo 3,000 km below your feet. The field of a straight wire carrying current $I$ has magnitude

$$B = \frac{\mu_0 I}{2\pi r}$$

at distance $r$ from the wire, where $\mu_0 = 4\pi \times 10^{-7}$ T·m/A is the **permeability of free space**. The field circles the wire — use the right-hand rule for currents: point your thumb in the direction of current flow, and your fingers curl in the direction of $\vec{B}$.

Notice that this falls as $1/r$, not $1/r^2$. The field of a point charge falls as $1/r^2$ because the source is a point — all the field spreads out in three dimensions from a single location. The field of an infinite line current falls as $1/r$ because the source is spread along a line — there's only two-dimensional spreading, perpendicular to the wire. Geometry determines the power law.

At 1 cm from a wire carrying 10 A:

$$B = \frac{(4\pi \times 10^{-7})(10)}{2\pi (0.01)} = 2 \times 10^{-4} \text{ T} = 0.2 \text{ mT}.$$

Four times Earth's surface field — enough to deflect a compass held nearby. This is what Ørsted saw in 1820: a current-carrying wire visibly deflecting a compass needle. It was the first experimental evidence that electricity and magnetism were connected.

**The solenoid.** Wind a wire into a long, tight helix — $n$ turns per meter — and pass current $I$ through it. The field inside is

$$B = \mu_0 n I,$$

approximately uniform, parallel to the axis, and almost entirely confined inside the coil. This is one of the most useful field configurations in physics and engineering. An MRI scanner is a solenoid, cooled to 4 K so that the wire becomes superconducting (zero resistance), carrying ~1200 A to produce a 1.5 T uniform field through the bore. The uniformity — better than parts per million across the imaging volume — is what makes the proton resonance signal interpretable as an image.

<!-- → [INFOGRAPHIC: Side-by-side field maps — (1) long straight wire with circular field lines, labeled B = μ₀I/2πr; (2) solenoid with uniform internal field lines, labeled B = μ₀nI; arrows showing right-hand rule for each; caption: field geometry determines the formula — line source gives 1/r, solenoid geometry gives uniform field inside] -->

---

## Forces between wires; the definition of the ampere

If a current creates a magnetic field, and a current in a field feels a force, then two current-carrying wires exert forces on each other. Wire 1 creates a field at wire 2's location; the Lorentz force acts on wire 2's current in that field.

The force per unit length between two parallel wires separated by distance $d$, carrying currents $I_1$ and $I_2$:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}.$$

Currents in the *same* direction attract. Currents in *opposite* directions repel. (This is opposite to what you might expect if you think of the charges: two parallel positive currents would repel each other electrostatically if the wire weren't neutral. The magnetic attraction overwhelms the — perfectly cancelled — electric force. Another view of how magnetism is larger than the relativistic "correction" suggests.)

![Two panels. Left: parallel currents in the same direction attract. Right: antiparallel currents repel. Force per length F/L = μ₀ I₁ I₂ / (2π d). This was the basis of the SI ampere definition (1948–2019).](../images/22-magnetism-fig-05.png)
*Figure 22.5 — Parallel Wires — Same Direction Attract, Opposite Repel*

This force was, until 2019, the *definition* of the ampere: one ampere is the current that, flowing through two parallel wires one meter apart in vacuum, produces a force of exactly $2 \times 10^{-7}$ N per meter. The SI system redefined the ampere in 2019 by fixing the numerical value of the elementary charge — cleaner, more fundamental — but the conceptual definition is still the picture to have in your head.

<!-- → [TABLE: Two parallel wires force summary — columns: current directions, force direction (attract/repel), force per meter formula, numerical example (I₁=I₂=10 A, d=1 cm); rows: same direction, opposite direction; then a second sub-table showing the 2019 SI redefinition: old definition (parallel-wire force), new definition (fixed value of e = 1.602×10⁻¹⁹ C), why the change (eliminates circularity in defining A via N via kg)] -->

---

## Force on a current-carrying wire

A current is just many charges moving together. Apply the Lorentz force to each charge in a wire segment and sum up, and you get:

$$\vec{F} = I\vec{L} \times \vec{B},$$

magnitude $F = BIL\sin\theta$, where $L$ is the length of wire in the field and $\theta$ is the angle between the current direction and the field. For wire perpendicular to field: $F = BIL$.

This is the force in every electric motor, every loudspeaker, every galvanometer ever built.

A loudspeaker works like this: a small coil of wire (the "voice coil") sits in the gap of a permanent magnet. Current through the coil — representing an audio signal — creates a force on the coil, pushing it in or out, driving the attached paper cone, pushing air, making sound. Reverse the current and the force reverses. Drive it at 440 Hz and the cone oscillates at 440 Hz, producing an A4 note. The physics is exactly $F = BIL$, executing a thousand times per second.

A motor generalizes this: instead of a wire moving linearly in a field, you have a coil free to rotate. The field exerts a torque on the coil. The coil turns. Reverse the current every half-rotation (using a mechanical commutator) and the torque is always in the same rotational direction. The coil spins continuously. Every electric motor in your life — refrigerator compressor, washing machine drum, EV traction drive, cooling fan in your laptop — is this geometry, refined.

The torque on a flat coil of area $A$, $N$ turns, carrying current $I$ in field $B$:

$$\tau = BIAN\sin\phi,$$

where $\phi$ is the angle between the coil's normal and the field. Maximum torque when the coil is parallel to the field; zero torque when the coil is perpendicular to it (the equilibrium position that motors must commutate through).

<!-- → [IMAGE: Cutaway photograph or technical diagram of a loudspeaker voice coil assembly — labels pointing to: permanent magnet, gap where field is concentrated, voice coil winding, cone attachment point; caption: the voice coil sits in a ~1 T radial field in the gap; current through it produces a force F = BIL along the cone axis, proportional to the audio signal current] -->

<!-- → [INFOGRAPHIC: DC motor operating sequence — three panels showing (1) coil parallel to B, maximum torque labeled τ = BIAN; (2) coil at 45°, intermediate torque; (3) coil perpendicular to B, zero torque, commutator fires to reverse current; arrows showing rotation direction throughout; caption: the commutator reverses current at zero-torque position, keeping the coil spinning rather than oscillating] -->

---

## A calculation worth doing: the MRI solenoid

A clinical 1.5 T MRI scanner uses a solenoid with approximately 1000 turns per meter. What current must flow?

$$I = \frac{B}{\mu_0 n} = \frac{1.5}{(4\pi \times 10^{-7})(1000)} \approx 1{,}194 \text{ A}.$$

1,200 amperes. In ordinary copper wire, the resistive heating at that current would be enormous — $P = I^2 R$, and even a wire with small resistance would dissipate kilowatts. The only practical solution is a superconducting wire, which has exactly zero resistance below its critical temperature.

MRI solenoids use niobium-titanium wire, wound into coils and cooled to 4 K by liquid helium. At 4 K, the resistance drops to zero. The 1,200 A, once loaded, circulates indefinitely without a power source — the current is sustained by the wire's own inductance (Chapter 23). The liquid helium holds the wire at 4 K for years between refills.

The field uniformity required is extraordinary: the resonance frequency of proton spins depends on the local field strength, and spatial variation across the imaging volume would blur the image. Field homogeneity is maintained to better than 1 part per million over the imaging volume — achieved by adding small "shim" coils around the bore whose fields precisely cancel residual variations.

That level of engineering — 1 ppm field uniformity, zero-resistance 1,200 A currents, sustained for years — is resting on four lines of physics: $B = \mu_0 n I$, the definition of the tesla, Ohm's law run to its limit, and quantum mechanics of superconductivity.

<!-- → [TABLE: MRI scanner specifications bridged to physics — columns: engineering spec, physical meaning, governing equation; rows: field strength 1.5 T (force on proton spins, B = μ₀nI), homogeneity <1 ppm (frequency resolution of proton resonance, δf/f = δB/B), current ~1200 A (solenoid field formula), temperature 4 K (superconducting transition, below T_c resistance = 0), liquid helium consumption (cooling power vs. heat leak through cryostat walls)] -->

---

## Putting it all together: a proton in a bending magnet

Particle accelerators steer beams using bending magnets — precisely calibrated regions of uniform field that deflect the beam by a controlled angle. Here is how to think about one.

A proton beam at 50 MeV kinetic energy enters a region of 1.5 T field perpendicular to the beam direction. What is the radius of curvature?

The proton's speed: $\frac{1}{2}mv^2 \approx 50 \text{ MeV} = 8.0 \times 10^{-12}$ J, giving $v \approx 9.8 \times 10^7$ m/s (about $0.33c$ — mildly relativistic; a full treatment gives a similar number).

Radius: $r = mv/(qB) = (1.67 \times 10^{-27})(9.8 \times 10^7)/[(1.602 \times 10^{-19})(1.5)] \approx 0.68$ m.

A bending magnet 30 cm long deflects the beam through an angle $\theta = L/r = 0.30/0.68 \approx 0.44$ radians, or about 25 degrees. Accelerator designers chain together dozens of such magnets to steer the beam around a ring.

The physics is three equations: $r = mv/(qB)$, geometry, and $\frac{1}{2}mv^2 = eV_\text{acc}$. From those three equations, and the constraint that the machine must fit on a given site, you derive the required field strength and the size of the ring. The LHC at 6.5 TeV per proton and 27 km circumference is the same calculation, extended to relativistic energies and confronting the limits of superconducting magnet technology.

---

## Three commitments

**Moving charges feel magnetic forces.** $\vec{F} = q\vec{v} \times \vec{B}$. The force is perpendicular to velocity; magnetic forces steer, they do not accelerate. Particles in uniform fields follow circular paths of radius $r = mv/(qB)$.

**Currents create magnetic fields.** $B = \mu_0 I/(2\pi r)$ for a long wire; $B = \mu_0 nI$ for a solenoid. The right-hand rule gives direction. Field geometry determines the $r$-dependence.

**Currents in fields feel forces.** $F = BIL\sin\theta$. This torque drives every electric motor and every speaker. Parallel currents attract; antiparallel repel.

The one idea that matters most: **magnetism and electricity are the same phenomenon.** A moving charge sources both $\vec{E}$ and $\vec{B}$. What looks like a pure magnetic force in one frame is a Coulomb force in another. The unification is not a convenience — it is a statement about the structure of spacetime.

---

## Exercises

### Warm-up

**22.1** *(Lorentz force magnitude)* A proton moves at $2 \times 10^6$ m/s perpendicular to a uniform magnetic field of 0.5 T. Compute the magnetic force on it. In which direction does the force point relative to the velocity?

**22.2** *(No work done)* An electron enters a region of uniform $\vec{B}$ with speed $3 \times 10^6$ m/s. After traveling through the field, it exits with a different direction but the same speed. Explain in one sentence why the magnetic force cannot change the electron's speed, using the definition of work.

**22.3** *(Field of a long wire)* A long straight wire carries 8 A. What is the magnetic field strength 4 cm from the wire? How does this compare to Earth's surface field (~50 μT)?

**22.4** *(Solenoid field)* A solenoid is 20 cm long and wound with 400 turns of wire. Current through it is 3 A. What is the magnetic field inside, near the center?

### Application

**22.5** *(Circular orbit radius)* An alpha particle (mass $6.64 \times 10^{-27}$ kg, charge $+2e$) moves at $5 \times 10^6$ m/s perpendicular to a 0.8 T field. Compute the radius of its circular path. How does this compare to the electron radius in Example 22 at 1 mT?

**22.6** *(Mass spectrometer)* An ion of unknown mass and charge $+e$ is accelerated through 3{,}000 V, then enters a 0.25 T field perpendicular to its velocity. The radius of its circular path is 18 cm. (a) Find the ion's speed just before entering the field (use energy conservation: $eV = \frac{1}{2}mv^2$). (b) Find its mass. (c) What element is it likely to be?

**22.7** *(Force on a current-carrying wire)* A horizontal wire 50 cm long carries 12 A and sits perpendicular to a uniform horizontal magnetic field of 0.3 T. (a) Compute the force on the wire. (b) If the wire has mass 5 g, does the magnetic force exceed the gravitational force on it?

**22.8** *(Motor torque)* A rectangular coil 6 cm × 10 cm has 80 turns and carries 0.5 A in a 0.6 T uniform field. (a) Compute the maximum torque. (b) At what orientation of the coil relative to $\vec{B}$ is the torque maximum? At what orientation is it zero?

### Synthesis

**22.9** *(Forces between parallel wires)* Two long parallel wires 8 cm apart carry currents of 15 A and 20 A in the same direction. (a) Compute the force per meter on each wire. (b) Is the force attractive or repulsive? (c) If the currents were in opposite directions, how would your answers change?

**22.10** *(Cyclotron frequency)* Show that the period of a charged particle's circular orbit in a uniform magnetic field is $T = 2\pi m/(qB)$ — independent of the particle's speed. This is the cyclotron principle. Compute the cyclotron frequency $f = 1/T$ for a proton in a 1.5 T field. In what part of the electromagnetic spectrum does this frequency fall?

**22.11** *(Bending magnet design)* You are designing a beam-line for protons accelerated to 100 MeV kinetic energy, and need to deflect the beam by 45° using a single bending magnet. (a) Compute the proton speed. (b) Compute the required radius of curvature $r$. (c) If the maximum achievable field is 1.8 T, what length must the magnet be?

### Challenge

**22.12** *(Relativistic bending)* At the LHC, protons are accelerated to 6.5 TeV. In the ultra-relativistic limit, momentum $p \approx E/c$ where $E$ is the total energy. The bending radius is $r = p/(qB)$. With $B = 8.4$ T and the ring circumference 26.7 km, verify that the bending magnet radius is consistent with the ring geometry. (The ring is not all bending magnet — roughly 70% of the circumference is bending magnets; account for this.)

**22.13** *(Earth as a magnet)* Earth's magnetic dipole moment is approximately $8 \times 10^{22}$ A·m². The field of a magnetic dipole at distance $r$ along its axis is $B = \mu_0 m/(2\pi r^3)$, where $m$ is the dipole moment. (a) Estimate Earth's field at the surface ($r \approx 6.4 \times 10^6$ m) along the magnetic axis. Compare to the measured value of ~60 μT at the poles. (b) A geomagnetic storm can compress Earth's magnetosphere from its normal 10 Earth-radii standoff to 6 Earth-radii. By what factor does the field at that standoff distance increase? (c) Why does this matter for satellites in low Earth orbit?

---

## Still puzzling

The deepest asymmetry in this chapter: *why are there no magnetic monopoles?* Electric monopoles — isolated charges — are everywhere. But break a bar magnet in half and you get two magnets, each with both poles. Magnetic field lines always close on themselves; there is no source point and no sink point. Maxwell's equations have a perfect symmetry between $\vec{E}$ and $\vec{B}$ except for this one asymmetry: $\nabla \cdot \vec{B} = 0$, but $\nabla \cdot \vec{E} = \rho/\epsilon_0$. Paul Dirac showed in 1931 that even a single monopole in the universe would explain why electric charge comes in discrete units. No monopole has ever been detected, despite decades of searching. The asymmetry remains unexplained.

---

## LLM Exercise — Chapter 22: Magnetic Fields and Forces in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A magnetic-field or magnetic-force estimate for one component of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 22 (Magnetism), I want to identify ONE magnetic component of my phenomenon.

Please:

1. Identify the magnetic element. Examples:
   - Bike commute: any motors (e-bike, headlight dynamo); the steel frame's response to Earth's field.
   - Coffee maker: thermostat solenoid valve.
   - Marathon: the speaker in your music headphones.
   - Espresso machine: the pump motor's rotor.
   - Basketball: nothing magnetic in the ball; consider the locker room magnetic strip.

2. Estimate or compute:
   (a) The magnetic field strength involved (T).
   (b) The current that produces or interacts with the field (A).
   (c) The geometry (long wire, loop, solenoid?).
   (d) The force or torque produced.

3. State your inputs and uncertainty.

4. Sanity check against published numbers (small motors typically ~0.1-0.5 T at gap; speakers ~1 T at voice coil).

5. Connect to Chapter 23 (Electromagnetic Induction), where moving magnets and changing currents will produce voltages.

Save the output as logbook/chapter-22-magnetism.md.
```

### What this produces

Your twenty-second Logbook entry — a magnetic-field or force calculation.

### How to adapt this prompt

- *For phenomena with no obvious magnetism*: every electronic device contains at least an inductor or magnetic shield; pick one. Or compute Earth's field at your location.
- *For Claude Code:* Use COMSOL or a free FEMM (Finite Element Method Magnetics) simulation to verify your hand calculations for non-trivial geometries.

### Connection to previous chapters

Builds on Chapters 18 (electric force), 20 (current). The Lorentz force applies to a charge; moving charges = currents; currents create fields → Chapter 22's central loop.

### Preview of next chapter

Chapter 23 closes the loop: changing magnetic fields produce voltages (Faraday's law), making generators, transformers, and the electrical grid possible. The Chapter 23 LLM Exercise will compute an induced voltage relevant to your phenomenon.

---

## Connections forward

Chapter 23 introduces **electromagnetic induction**: Faraday's discovery that *changing* magnetic fields produce electric fields. This closes the symmetry — changing $\vec{E}$ produces $\vec{B}$ (Chapter 19's displacement current), changing $\vec{B}$ produces $\vec{E}$. Chapter 24 shows that these two fields sustain each other in oscillation, propagating at speed $c$ as electromagnetic waves. The steering forces you computed here are one half of a story; the generating forces of Chapter 23 are the other half.

---

**Tags:** magnetism, Lorentz-force, magnetic-field, electric-motor, solenoid, Feynman-style
