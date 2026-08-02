# Chapter 8 — Magnetism

**Suggested titles**

1. Magnetism
2. Why a Magnetic Compass Doesn't Work in a Spaceship Near Jupiter
3. Lorentz, Ampère, and the Force on Moving Charges

**TL;DR.** Magnetic fields are produced by moving electric charges (currents) and exert forces on other moving charges. The Lorentz force law $\vec{F} = q\vec{v} \times \vec{B}$ governs how charges move in magnetic fields; the right-hand rule keeps signs straight. Currents in wires create fields ($B = \mu_0 I/(2\pi r)$ for a long straight wire) and feel forces in fields ($F = BIL\sin\theta$). The Earth's field, navigation, electric motors, MRI machines, particle accelerators, and the Sun's surface all live inside this chapter.

---

## A magnetic compass that lies near Hudson Bay

A pilot flying a small plane over northern Canada in 1995 notices her magnetic compass slowly rotating, even though the plane is flying straight and level. Half an hour later it has swung 25 degrees off course. She hasn't moved her stick. The compass is wrong.

What she has flown over is the **magnetic anomaly** of the Hudson Bay area — a region where Earth's local magnetic field deviates substantially from the smooth dipole pattern, due to deep crustal magnetization and core convection currents. Pilots in this region know to switch to GPS or true-north navigation; the magnetic compass, the workhorse of navigation since the 11th century, becomes unreliable.

This is one of many places where the magnetic field reveals itself as a real, measurable, and locally variable property of space. The needle's behavior is set by the field's direction and magnitude *at the needle's location*, not anywhere else. And that field is sourced by *moving electric charges* — in this case, the slowly convecting molten iron in Earth's outer core, an electric dynamo running 3,000 km beneath your feet.

The whole subject of magnetism, viewed from the right angle, is a single insight: *moving charges create magnetic fields, and moving charges feel forces in magnetic fields*. Stationary charges create only electric fields and feel only electric forces. The magnetic story unfolds because one observer's electric field is, in a frame moving relative to the source, partially a magnetic field. Magnetism is electricity in motion.

**Learning objectives.** By the end of this chapter you should be able to:

1. Identify magnetic poles and state that magnetic field lines form closed loops (no monopoles).
2. State and apply the Lorentz force law: $\vec{F} = q\vec{v} \times \vec{B}$, with the right-hand rule for direction.
3. Compute the radius of a charged particle's circular motion in a uniform field: $r = mv/(qB)$.
4. Compute the force on a current-carrying wire in a magnetic field: $\vec{F} = I\vec{L} \times \vec{B}$, magnitude $F = BIL\sin\theta$.
5. Compute the magnetic field of a long straight wire: $B = \mu_0 I/(2\pi r)$.
6. Compute the magnetic field of a solenoid: $B = \mu_0 n I$, where $n$ is turns per length.
7. Reason qualitatively about the forces between parallel currents and the operation of an electric motor.

**Prerequisites.** Chapter 18 (electric charge, fields). Chapter 20 (electric current). Vector cross products (or the right-hand rule as the practical alternative).

**Why this chapter matters.** Almost every motor in your life — refrigerator compressor, washing machine, electric vehicle, blender — is an application of the force a magnetic field exerts on a current-carrying wire. MRI machines image your body using magnetic fields stronger than 30,000 times Earth's. Mass spectrometers, particle accelerators, plasma confinement in fusion reactors, the binding of stars in galaxies — all are governed by what you learn here.

---

## Concept 1 — Magnetic fields and the Lorentz force

### A bar magnet, a compass, and Faraday's iron filings

Lay a bar magnet on a sheet of paper. Sprinkle iron filings around it. Tap the sheet gently. The filings organize themselves into curving lines — emerging from one end of the magnet (call it the **north pole**), looping around through space, and entering the other end (the **south pole**). The pattern is unmistakable: the magnetic field has a definite direction at every point in the surrounding space, and the iron filings act as tiny compass needles that align with it.

This is the same picture Michael Faraday traced in the 1830s at the Royal Institution, when he was working out the visual representation of fields. The iron-filing experiment is one of the most elegant demonstrations in physics — instant visualization of an invisible vector field, using a magnet, a sheet of paper, and a few cents' worth of iron.

Two facts the experiment makes obvious:

1. **Magnetic field lines never end.** They loop continuously from north to south *outside* the magnet, and from south to north *inside* the magnet. There are no isolated north or south poles — break a bar magnet in half and you get two new bar magnets, each with both north and south poles.

2. **Like poles repel, unlike poles attract.** This is why a compass needle aligns with the Earth's field: the north end of the needle is attracted to the (geographic) north pole region, which means the geographic north pole is actually a magnetic *south* pole. (The naming convention predates any understanding of why.)

### The mechanism — magnetic field and the Lorentz force

The **magnetic field** $\vec{B}$ at a point is a vector that determines the magnetic force felt by a moving charge at that point. The unit is the **tesla** (T), with $1 \text{ T} = 1 \text{ N}/(\text{C} \cdot \text{m/s}) = 1 \text{ N}/(\text{A} \cdot \text{m})$. A tesla is a large field — Earth's field is about $5 \times 10^{-5}$ T (50 μT), a refrigerator magnet is ~0.005 T, an MRI scanner is 1.5–3 T, and the strongest pulsed laboratory fields reach ~100 T.

The **Lorentz force** on a charge $q$ moving with velocity $\vec{v}$ in field $\vec{B}$ is

$$\vec{F} = q \vec{v} \times \vec{B}.$$

The cross product means three things:

- The force is perpendicular to both $\vec{v}$ and $\vec{B}$.
- The magnitude is $F = qvB \sin\theta$, where $\theta$ is the angle between $\vec{v}$ and $\vec{B}$.
- The direction is given by the **right-hand rule**: point fingers in direction of $\vec{v}$, curl toward $\vec{B}$, thumb points in direction of $\vec{F}$ for positive $q$. Reverse for negative charge.

A consequence: a charge moving *parallel* to $\vec{B}$ feels no magnetic force ($\sin\theta = 0$). A charge moving *perpendicular* to $\vec{B}$ feels maximum force.

A second consequence: the magnetic force is always perpendicular to $\vec{v}$. Therefore the magnetic force does *no work* on the moving charge. It changes the charge's direction but never its speed. This is fundamentally different from electric forces, which do work on charges and change their kinetic energy.

### Circular motion in a uniform field

A charged particle entering a uniform field perpendicular to its velocity moves in a circle, because the magnetic force is always perpendicular to velocity (centripetal). The radius is set by Newton's second law for circular motion:

$$qvB = \frac{mv^2}{r} \implies r = \frac{mv}{qB}.$$

This is the principle of the **mass spectrometer**: ionize a sample, accelerate the ions through a known voltage, send them through a magnetic field perpendicular to their motion, measure the radius of their circular path. From $r$ you get the mass-to-charge ratio. Used routinely in chemistry, biology (proteomics), forensics, and atmospheric science.

The same principle, scaled up, is the **cyclotron** used in particle accelerators (Chapter 31): protons spiraling outward as they're accelerated by alternating electric fields between dee-shaped magnets.

### The trade-off

The Lorentz force law trades **conceptual simplicity for the cross-product complication.** The expression $\vec{F} = q\vec{v} \times \vec{B}$ is compact and beautiful, but the cross product is the most mathematically intricate operation in introductory physics. The right-hand rule is a memorization aid that lets you skip the cross-product algebra. Practiced enough, the rule becomes second nature.

### Worked example — electron in a 1 mT field

An electron moving at $1 \times 10^7$ m/s enters a uniform magnetic field of 1 mT perpendicular to its velocity. (a) Compute the magnetic force. (b) Compute the radius of its circular motion.

**(a)** $F = qvB = (1.602 \times 10^{-19})(10^7)(10^{-3}) = 1.602 \times 10^{-15}$ N. Tiny, as forces go, but on a tiny mass.

**(b)** $r = mv/(qB) = (9.11 \times 10^{-31})(10^7)/[(1.602 \times 10^{-19})(10^{-3})] = (9.11 \times 10^{-24})/(1.602 \times 10^{-22}) \approx 0.057$ m = 5.7 cm.

A 5.7 cm radius — the electron loops in a circle the size of a coffee cup. This is the working scale of cathode-ray tubes, electron microscopes, and old-style oscilloscopes.

**Sanity check.** Period of circulation: $T = 2\pi r/v = 2\pi (0.057)/(10^7) \approx 3.6 \times 10^{-8}$ s. Frequency about 28 MHz — in the radio band, the cyclotron frequency for electrons in a 1 mT field. Standard result.

### Common misconceptions

- *"The magnetic force can speed up a charge."* No — magnetic force is always perpendicular to velocity. It changes direction, not speed. Only electric forces do work on charges.
- *"Magnetic poles are like electric charges."* No — a positive charge can exist in isolation, but no monopole has ever been observed. Magnetic field lines always form closed loops; you cannot have a north pole without a south pole somewhere.
- *"A stationary charge feels a magnetic force in a magnetic field."* No — magnetic force requires motion. A still electron in a magnetic field feels no force (only the gravitational force, which is negligible).

↳ **Dig Deeper — Why moving charges experience magnetic forces (the relativity connection)**

*The deepest understanding of magnetism comes from special relativity. What looks like a pure electric field in one reference frame appears as a mixture of electric and magnetic fields in a frame moving relative to the first. Magnetism is, in this sense, a relativistic correction to Coulomb's law — and the size of the "correction" turns out to be huge whenever significant currents flow.*

**Prompt:**
> Explain why magnetism can be derived from special relativity applied to Coulomb's law. Walk me through the standard thought experiment: a wire carrying a current is electrically neutral overall, but in a frame moving with the drifting electrons, length contraction makes the positive ions appear closer together than the electrons, giving a net positive charge density and a Coulomb force on a nearby moving charge. Show that this "Coulomb-from-length-contraction" force is exactly the magnetic force you would compute from the Lorentz law applied to the wire's current. End with one sentence on what this means: magnetism is not separate from electricity but is electricity viewed from a moving frame.

**What to do with the output:** Save it. The relativistic origin of magnetism is one of the most elegant unifications in physics. It also makes the Lorentz force law feel less arbitrary.

---

## Concept 2 — Currents create magnetic fields

### Ørsted's compass, revisited as field source

We met Ørsted in Chapter 20 — his April 1820 demonstration that current in a wire deflected a nearby compass. Now we close the loop. The deflection of the compass tells you that *the wire is producing a magnetic field*, with a definite magnitude and direction that depends on the current and the geometry.

For a long straight wire carrying current $I$, the magnetic field at perpendicular distance $r$ from the wire has magnitude

$$B = \frac{\mu_0 I}{2\pi r},$$

where $\mu_0 = 4\pi \times 10^{-7} \text{ T} \cdot \text{m/A}$ is the **permeability of free space**. The direction is given by the **right-hand rule for currents**: point your right thumb in the direction of current flow, and your fingers curl in the direction of $\vec{B}$ around the wire.

So the field circles the wire, getting weaker with distance ($1/r$, not $1/r^2$ — the geometry of an infinite wire is two-dimensional). At 1 cm from a wire carrying 10 A:

$$B = \frac{(4\pi \times 10^{-7})(10)}{2\pi (0.01)} = 2 \times 10^{-4} \text{ T} = 0.2 \text{ mT}.$$

About four times Earth's surface field. This is why a 10-amp household current can deflect a compass held nearby.

### The mechanism — fields from current configurations

Different geometries give different field expressions:

**Long straight wire:** $B = \mu_0 I/(2\pi r)$. Field circles the wire.

**Circular loop of radius $R$, on its axis at center:** $B = \mu_0 I/(2R)$. Field along the axis. The familiar bar-magnet pattern outside the loop.

**Solenoid** (long tightly-wound coil) of $n$ turns per unit length, near its center: $B = \mu_0 n I$. Field is approximately uniform inside, parallel to the axis. Almost zero outside (for an ideal long solenoid). This is the workhorse geometry for producing controlled, uniform magnetic fields in the lab.

A solenoid wrapped into a closed donut shape becomes a **toroid**, with the field confined entirely inside the torus — used for everything from inductors in power supplies to fusion reactors (tokamaks).

### Forces between parallel currents

Two parallel wires, each carrying current, exert magnetic forces on each other. Wire 1 produces a field at the location of wire 2; wire 2's current carries through that field and feels a force.

If both currents flow in the same direction, the wires *attract*. Opposite directions, they *repel*. The force per unit length:

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}.$$

This phenomenon was, until 2019, the *definition* of the ampere: one ampere is the current that, flowing through two parallel wires 1 meter apart in vacuum, produces a force of exactly $2 \times 10^{-7}$ N per meter of length. Post-2019 SI redefined the ampere via the elementary charge ($e$), but the parallel-wire force is still the conceptual handle.

### The trade-off

Computing fields from currents trades **vector field complexity for use of symmetry-derived formulas.** The general field of an arbitrary current distribution requires the Biot-Savart law (an integral) or Ampère's law (a path integral). For symmetric geometries (long wire, loop, solenoid), the integrals collapse to simple formulas that you memorize. For arbitrary geometries, computer integration takes over.

### Worked example — magnetic field inside an MRI scanner

A clinical MRI scanner uses a superconducting solenoid to produce a uniform field of 1.5 T inside the bore. (a) If the solenoid has 1000 turns per meter, what current must flow through the wire? (b) What field would 1 amp through the same coil produce? (c) Why do MRI machines need superconductors?

**(a)** $B = \mu_0 n I \implies I = B/(\mu_0 n) = 1.5/[(4\pi \times 10^{-7})(1000)] \approx 1194$ A.

**(b)** $B(1 \text{ A}) = (4\pi \times 10^{-7})(1000)(1) = 1.26 \times 10^{-3}$ T = 1.26 mT. Negligible for MRI.

**(c)** A 1200-A current in ordinary copper wire would dissipate enormous power as heat ($P = I^2R$, with $R$ even small enough to be problematic). A superconducting wire has *zero* resistance, so it can carry 1200 A indefinitely with no dissipation, after the initial energy is loaded.

**Sanity check.** Real MRI scanners use kilometer-scale lengths of niobium-titanium superconducting wire wound into coils, kept at 4 K by liquid helium. Once the field is established, the current circulates indefinitely. This is the engineering miracle that makes hospital MRI possible.

### Common misconceptions

- *"A wire's magnetic field is everywhere proportional to $1/r^2$."* No — for a long straight wire, it falls as $1/r$, not $1/r^2$. The infinite-line geometry has $1/r$; only point-source geometries (electric monopole, or short current segment via Biot-Savart) give $1/r^2$.
- *"Solenoid field is the same everywhere inside."* Approximately, near the center of a long solenoid. At the ends, the field weakens substantially.
- *"Parallel currents always attract."* Same direction, attract. Opposite direction, repel. Easy to flip sign by mistake.

↳ **Dig Deeper — How an electric motor works, fundamentally**

*The simplest electric motor is a current loop in a magnetic field, free to rotate. The field exerts a torque on the loop, and the loop spins. Reverse the current twice per rotation (mechanically, with a "commutator") and the loop spins continuously. Every electric motor in your life — from the cooling fan in your computer to the traction motor in a Tesla — is a refinement of this geometry.*

**Prompt:**
> Walk me through how a basic DC motor works. Start with a single rectangular loop of current-carrying wire in a uniform magnetic field. Show that the magnetic forces on the two long sides of the loop are equal and opposite, but offset, producing a torque. Compute the torque magnitude as $\tau = BIA \sin\phi$, where $A$ is the loop area and $\phi$ is the angle between the loop's normal and the field. Then explain the role of the commutator: it reverses the current direction every half-rotation, keeping the torque always in the same rotational sense. End with one sentence on why modern motors use multiple loops at different angles to smooth out the torque ripple.

**What to do with the output:** Save it. Electric motors are one of the most consequential applications of physics in the modern world, and the underlying physics is exactly this chapter.

---

## Concept 3 — Force on current-carrying wires; electromagnets

### A speaker cone driven by a magnetic field

The cone of a loudspeaker is driven by a small coil of wire (the "voice coil") suspended in the field of a permanent magnet. When current flows through the coil, the magnetic force on the current pushes the coil — and the cone attached to it — in or out, depending on current direction. Reverse the current 1000 times per second and the cone vibrates at 1 kHz, pushing air, producing a 1 kHz tone.

This is the same physics in every audio speaker, every set of headphones, every microphone (a microphone is a speaker run backwards: sound waves move the cone, which moves the coil, which generates a small voltage). The force law:

$$\vec{F} = I \vec{L} \times \vec{B},$$

magnitude $F = BIL\sin\theta$, where $L$ is the length of wire in the field and $\theta$ is the angle between current direction and field. The right-hand rule applies as before.

### The mechanism — the wire-in-field force

The Lorentz force on each individual moving charge in the wire is $q\vec{v} \times \vec{B}$. For a wire of length $L$ carrying current $I$ in field $\vec{B}$, summing over all charges in the wire gives the wire-in-field formula above.

For a wire perpendicular to a uniform field, the force per unit length is

$$\frac{F}{L} = BI.$$

A wire 1 meter long, carrying 5 A, perpendicular to a 0.1 T field, feels a force of 0.5 N — about the weight of a small apple. Substantial.

### Electromagnets

A coil of wire wrapped around an iron core makes an **electromagnet**: switch on the current and the iron core becomes magnetized, producing a strong field near its surface; switch off, the field collapses. Used in junkyard cranes (lift cars), MRI machines (focus the field), particle accelerators (steer beams), and the read-write heads of every hard disk drive ever built.

The magnetic susceptibility of iron amplifies the solenoid's $B$ field by a factor of hundreds to thousands. Soft iron loses its magnetization when the current is removed (good for switching applications); hardened steel retains some magnetization (used for permanent magnets).

### The trade-off

Practical electromagnetic devices trade **complex 3D geometries for the simplicity of $F = BIL$.** Real motors, speakers, and electromagnets have curved field lines, varying current densities, and saturated cores at high fields. The simple wire-in-field formula gets the order of magnitude right; finite-element simulation handles the rest. In introductory physics we use the simple formula and trust the engineering literature for the details.

### Worked example — torque on a square coil

A square coil 10 cm on a side, with 100 turns of wire, lies in a uniform magnetic field of 0.5 T. The coil carries 2 A. (a) What is the maximum torque? (b) At what orientation is the torque maximum?

**(a)** Maximum torque on a coil: $\tau_\text{max} = BIAN$, where $N$ is the number of turns and $A$ is the loop area. $\tau_\text{max} = (0.5)(2)(0.01)(100) = 1.0$ N·m.

**(b)** Torque is maximum when the plane of the coil is *parallel* to $\vec{B}$ (i.e., the coil's normal vector is perpendicular to $\vec{B}$). Torque is zero when the coil's normal aligns with $\vec{B}$.

**Sanity check.** A 1 N·m torque on a 10-cm-radius lever arm gives 10 N of force — about 1 kg-weight. Substantial. This is why a small electric drill can generate enough torque to drive a screw into wood.

### Common misconceptions

- *"All wires feel a force in any magnetic field."* Only current-carrying wires feel force, and the force depends on the angle. A wire carrying current parallel to $\vec{B}$ feels zero force.
- *"Permanent magnets work without any current."* They work with *internal* currents — the orbital and spin motions of electrons in the magnet's atoms. Permanent magnetization is the alignment of these atomic-scale current loops.
- *"Iron is the only magnetic material."* No — nickel, cobalt, neodymium-iron-boron, and many alloys are also magnetic. The element-level explanation involves unpaired electron spins and quantum mechanics (Chapter 30).

↳ **Dig Deeper — How a hard disk drive reads and writes bits with electromagnetism**

*The hard disk drive (HDD), invented at IBM in 1956 and refined for decades, stores data as small magnetic regions on a spinning platter. Reading and writing each bit requires an electromagnet (the "head") flying nanometers above the platter. The physics of this device is a textbook combination of magnetic-field generation, ferromagnetic materials, and Lorentz forces.*

**Prompt:**
> Explain how a hard disk drive reads and writes bits magnetically. For writing: the head is a tiny electromagnet, and the current direction determines the magnetization direction of a small region on the platter (north-up = "1", south-up = "0", or some convention). For reading: as a magnetized region passes under the head, the changing magnetic flux through the head's coil induces a voltage (Faraday's law, Chapter 23 preview). Mention that modern drives use giant magnetoresistance (GMR) read heads instead of induction, with sensitivity that earned the 2007 Nobel Prize. End with one sentence on why physical HDDs are being displaced by SSDs (no moving parts, faster).

**What to do with the output:** Save it. The HDD is one of the most beautiful real-world applications of magnetism, and understanding it ties together everything in this chapter and the next.

---

## Synthesis — moving charges, fields, forces

Step back. Three concepts:

1. **Moving charges feel magnetic forces.** $\vec{F} = q\vec{v} \times \vec{B}$. Magnetic force is perpendicular to velocity; does no work. Charged particles move in circles in uniform fields.

2. **Currents create magnetic fields.** $B = \mu_0 I/(2\pi r)$ for a long wire; $B = \mu_0 n I$ for a solenoid. Geometry determines the formula; symmetry collapses the integral.

3. **Currents in fields feel forces.** $F = BIL\sin\theta$. Two parallel currents attract or repel; this is the force in every electric motor and speaker.

The unifying picture: magnetism and electricity are two faces of the same phenomenon, related by motion (and by special relativity). A static electric charge sources only $\vec{E}$; once it moves, it sources $\vec{B}$ as well, and feels forces from any other moving charge's field.

### A worked example combining all three concepts — particle in a beam-line magnet

A proton beam at 50 MeV (kinetic energy) enters a region of uniform 1.5 T magnetic field perpendicular to the beam. (a) What is the radius of the proton's circular motion? (b) How long does it take to complete one revolution? (c) If the magnet has length 3 m along the beam direction, by what angle is the beam deflected?

**Step 1 — Proton speed.** At 50 MeV, the proton is mildly relativistic. For a back-of-envelope, $KE \approx \frac{1}{2}m v^2 \implies v \approx \sqrt{2 KE/m}$. With $KE = 50 \times 10^6 \times 1.602 \times 10^{-19} = 8 \times 10^{-12}$ J and $m_p = 1.67 \times 10^{-27}$ kg: $v \approx \sqrt{2(8 \times 10^{-12})/(1.67 \times 10^{-27})} = \sqrt{9.58 \times 10^{15}} \approx 9.8 \times 10^7$ m/s = $0.33c$. Mildly relativistic — full relativistic treatment would give $\sim 9.5 \times 10^7$ m/s, close enough for our purposes.

**Step 2 — Radius.** $r = mv/(qB) = (1.67 \times 10^{-27})(9.8 \times 10^7)/[(1.602 \times 10^{-19})(1.5)] = (1.64 \times 10^{-19})/(2.40 \times 10^{-19}) \approx 0.68$ m = 68 cm.

**Step 3 — Period.** $T = 2\pi r/v = 2\pi(0.68)/(9.8 \times 10^7) \approx 4.4 \times 10^{-8}$ s. Frequency $\sim 23$ MHz.

**Step 4 — Deflection angle.** In a 3 m magnet, the proton traces an arc of length 3 m on a circle of radius 0.68 m. Arc/radius = angle in radians: $\theta = 3/0.68 \approx 4.4$ rad — but that's more than $\pi$, meaning the proton would actually circle multiple times in such a long magnet at this radius. Realistically, the magnet would be much shorter or the field stronger. For a 30 cm magnet: $\theta = 0.30/0.68 \approx 0.44$ rad ≈ 25°.

**Scale shift.** Same equations: at the LHC at CERN, 6.5 TeV protons (10⁵× more energy) circulate in a ring 27 km around — using superconducting magnets at 8.4 T to bend them. Magnetism is the steering wheel of high-energy physics.

---

## Exercises

### Warm-up

**22.1** *(LO 2)* A proton moves at $1 \times 10^6$ m/s perpendicular to a 0.1 T magnetic field. Compute the magnetic force.

**22.2** *(LO 3)* What is the radius of the proton's circular motion in 22.1?

**22.3** *(LO 5)* What magnetic field does a long straight wire carrying 5 A produce at 5 cm distance?

**22.4** *(LO 6)* A solenoid has 200 turns over 0.10 m. Current is 2 A. What is the field inside?

### Application

**22.5** *(LO 4)* A 1 m long wire carries 10 A perpendicular to a 0.5 T magnetic field. Compute the force on the wire.

**22.6** *(LO 5)* Two long parallel wires 5 cm apart carry currents 10 A in the same direction. Compute the force per meter on each.

**22.7** *(LO 3, 6)* In a mass spectrometer, an ion of charge $+e$ and unknown mass is accelerated through 2000 V, then enters a 0.3 T field perpendicular to its velocity. The radius of its circular path is 12 cm. Compute the mass.

**22.8** *(LO 7)* A square coil 5 cm on a side, with 50 turns, carries 1 A in a 0.4 T field. Compute the maximum torque.

### Synthesis

**22.9** *(LO 1, 2)* Earth's magnetic field is about 50 μT pointing approximately north (and slightly down in the northern hemisphere). A 100 m long horizontal east-west power line carries 500 A. Compute the magnetic force per meter and per total length.

**22.10** *(LO 5, 6, beyond)* A long solenoid of length 1 m, radius 5 cm, with 1000 turns, carries 1 A. (a) Compute the field inside. (b) An electron at the center of the solenoid moves perpendicular to the axis at $10^6$ m/s. Compute the radius of its motion.

**22.11** *(LO 4, beyond)* An electric motor's torque depends on the field strength, current, and number of turns of wire on the rotating coil. Discuss the design trade-offs: (a) why don't motor designers just keep increasing $N$ to get more torque? (b) Why do high-power motors typically use stronger permanent magnets (rare-earth Nd-Fe-B)?

### Challenge

**22.12** *(LO 3, beyond)* A particle accelerator produces 100 GeV electrons. Compute the radius of their circular motion in a 1 T field. (Hint: at this energy, electrons are highly relativistic; use $r = pc/(qBc) = E/(qBc)$ for ultra-relativistic case.)

**22.13** *(LO 5, 7, beyond)* Estimate the magnetic field strength in the gap of a typical refrigerator door magnet. Assume the magnet is ferrite with surface magnetization producing ~0.05 T at the surface. (a) What force does it exert on a 1 cm² piece of soft iron at the door? (b) Why does a refrigerator magnet stick to a steel fridge but not to an aluminum one?

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

## Chapter summary

Magnetism is the physics of moving charges and currents. Three commitments:

1. **Magnetic field $\vec{B}$ exerts force on moving charges via Lorentz law $\vec{F} = q\vec{v} \times \vec{B}$.** Force is perpendicular to velocity; magnetic force does no work; charged particles in uniform fields move in circles of radius $r = mv/(qB)$.

2. **Currents create magnetic fields.** $B = \mu_0 I/(2\pi r)$ for a long wire; $B = \mu_0 nI$ for a solenoid. Right-hand rule gives directions.

3. **Currents in fields feel forces.** $F = BIL\sin\theta$. Parallel currents attract; antiparallel repel. This is the force in every electric motor.

The one idea that matters most: **electricity and magnetism are two manifestations of the same phenomenon, unified by motion.** A static charge sources $\vec{E}$; a moving charge sources $\vec{E}$ and $\vec{B}$. From a moving frame, "your" electric field is "their" mix of electric and magnetic. The unification is complete in special relativity (Chapter 28).

The common mistake to watch for: **using the wrong right-hand rule.** There are two: one for the Lorentz force ($\vec{v} \times \vec{B}$, gives force on a charge), one for the field around a current-carrying wire (thumb along current, fingers curl around wire). Practice both.

---

## What would change my mind

The chapter argues that the Lorentz force law and current-carrying-wire formulas suffice for any introductory magnetic problem. The argument would need revision if a class of routine engineering problems (say, magnetic design at the saturation limit of soft iron, or near-field interactions in MRI antennas) were intractable with the simple formulas. They aren't, for back-of-envelope work; finite-element simulation handles the precision.

## Still puzzling

The deepest puzzle this chapter raises and partially resolves: *why are there no magnetic monopoles?* Maxwell's equations are perfectly symmetric except for this asymmetry — electric monopoles (charges) exist, magnetic monopoles don't. Dirac (1931) and 't Hooft (1974) showed that even one monopole in the universe would explain charge quantization, but no monopole has been observed despite extensive searching. The fact remains unexplained at the deepest level.

---

## Connections forward

Chapter 23 introduces **electromagnetic induction** — the discovery (Faraday 1831) that *changing magnetic fields produce electric fields*. This is the most consequential law in this part of physics: it makes generators, transformers, induction motors, wireless charging, and the entire electrical grid possible. Chapter 24 unifies $\vec{E}$ and $\vec{B}$ in Maxwell's equations and predicts that they propagate together as electromagnetic waves at speed $c$ — light. Magnetism is the bridge.

---

**Tags:** magnetism, Lorentz-force, magnetic-field, electric-motor, solenoid

---

## AI Wayback Machine

**Hans Christian Ørsted** discovered the connection between electricity and magnetism in 1820 — noticing that a compass needle deflected when a nearby wire carried current. The accidental observation founded electromagnetism.

**Run this:**

```
Who was Hans Christian Ørsted, and how does his discovery connect to the magnetism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hans Christian Ørsted"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what Ørsted observed in his 1820 lecture demonstration — and what made him take the deflection seriously.
- Ask it about Ørsted's parallel work as a writer and Friend of Hans Christian Andersen.

What changes? What gets better? What gets worse?
