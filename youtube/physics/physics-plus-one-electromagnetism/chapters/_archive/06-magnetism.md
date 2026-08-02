# Chapter 6 — Magnetism: How Moving Charges Make the World Spin

**TL;DR:** A charge in motion creates a magnetic field. A charge moving through that field experiences a force perpendicular to both its velocity and the field. This symmetry — electricity makes magnetism, magnetism makes electricity — is the machinery behind motors, generators, and the invisible compass that guides every compass needle on Earth.

---

## Chapter Opening: The Problem With Two Halves

Take a bar magnet. Cut it in half. You do not get one piece with only a north pole and one with only a south pole. You get two complete magnets. Each half has its own north and south. You can keep cutting — down to centimeters, down to millimeters, down to the scale of atoms — and every piece still has two poles.

This fact bothered physicists for centuries. Electric charge does not work this way. You can separate a positive charge from a negative charge. But magnetic poles? They refuse to separate. No experiment in human history has ever found a magnetic monopole — a lone north pole or a lone south pole floating by itself. In the cosmos or in the lab. Not once.

That obstinate refusal — that magnets always, *always* come in pairs of opposite poles — tells you something deep about the machinery underneath. Magnetism is not a property of poles. It is a property of motion.

A moving electric charge creates a magnetic field the way a moving car creates a wake. Stop the charge, and the magnetic field disappears. Start it moving, and the field reappears, shaped by the direction and speed of the motion. This is why a compass needle aligns with Earth's magnetic field: deep in the planet's core, molten iron is swirling. That swirl creates our magnetic shield. And this is why a magnet can never be split into isolated poles — because the poles are not the source. The *motion* of electrons inside atoms is the source. Cut the magnet, and you expose new surfaces where billions of moving electrons create new poles. The system rebalances. The two-pole structure persists.

**Learning objectives for this chapter:** You will understand how moving charges generate magnetic fields, how magnetic fields exert forces on moving charges and current-carrying wires, how changing magnetic fields induce currents in conductors, and how these principles build the machinery of electric motors, generators, and transformers — devices that have become as ordinary as the refrigerator magnet and as essential as the power grid.

**Prerequisites:** You should be comfortable with electric current as the flow of charge, with the concept of a force field (gravitational or electric), and with vector notation and the cross product. Familiarity with Newton's second law and basic calculus is helpful.

---

## Concept 1: The Force on a Charge in Motion — and Why It Matters

### The Mechanism: Velocity Meets Field

Picture yourself inside a particle detector — a machine built to watch subatomic collisions. A high-energy proton enters a region where a uniform magnetic field points horizontally across the chamber, say from left to right. The proton is moving downward at 3.0 × 10^6 meters per second — one percent the speed of light. The magnetic field is 2.0 tesla, a field strong enough to be remarkable but not exotic.

What happens to the proton?

The force that acts on it is given by

$$F = qvB\sin\theta,$$

where *q* is the charge (for a proton, 1.60 × 10^−19 coulombs), *v* is the velocity, *B* is the magnetic field strength, and *θ* is the angle between the velocity vector and the field vector. In our case, the proton moves perpendicular to the field, so sin(90°) = 1, and the force is straightforward:

$$F = (1.60 \times 10^{-19}\text{ C})(3.0 \times 10^{6}\text{ m/s})(2.0\text{ T}) = 9.6 \times 10^{-13}\text{ N}.$$

This is a tiny force — about a trillionth of a newton. But the proton has a mass of only 1.67 × 10^−27 kilograms. The acceleration is

$$a = \frac{F}{m} = \frac{9.6 \times 10^{-13}}{1.67 \times 10^{-27}} = 5.7 \times 10^{14}\text{ m/s}^2.$$

This is about ten *thousand billion* times the acceleration of gravity — enough to snap the particle into a sharp curve.

Here is what makes this force peculiar: it is *always perpendicular* to both the velocity and the magnetic field. Use the right-hand rule. Point your fingers in the direction of the velocity. Curl them toward the direction of the magnetic field. Your thumb points in the direction of the force. If the velocity is downward and the field points rightward, the force points into the page — perpendicular to both.

A force perpendicular to velocity does not change the speed of an object; it only changes the direction. The proton does not slow down. It curves. In fact, it curves in a circle, a perfect circle, tracing a path with radius

$$r = \frac{mv}{qB} = \frac{(1.67 \times 10^{-27})(3.0 \times 10^{6})}{(1.60 \times 10^{-19})(2.0)} = 1.6\text{ cm}.$$

The proton spirals through the detector in a circle of radius just over one centimeter. The magnetic field does no work on the proton — the force is perpendicular to the motion — but it sculpts the trajectory with geometric precision. This is how particle detectors work. By measuring the radius of curvature, physicists can deduce the momentum of particles they cannot see directly.

### The Trade-Off

The magnetic force is a *perpendicular* force. This is its power and its limitation. It can bend a path. It cannot accelerate a particle along its direction of motion. A magnetic field alone cannot add or remove energy from a charged particle. It can only redirect.

This is why magnets in a particle accelerator must be paired with electric fields. The electric field does the real work — speeding the particle up or slowing it down. The magnetic field provides the steering. Electric fields accelerate. Magnetic fields direct. Together they choreograph the particle's dance.

### Worked Example: A Charge in the Lab

An electron (charge −1.60 × 10^−19 C, mass 9.11 × 10^−31 kg) enters a region with a perpendicular magnetic field of 0.50 T, moving at 2.0 × 10^6 m/s. What is the radius of its circular path?

Using r = mv/(qB):

$$r = \frac{(9.11 \times 10^{-31})(2.0 \times 10^{6})}{(1.60 \times 10^{-19})(0.50)} = 2.3 \times 10^{-2}\text{ m} = 2.3\text{ cm}.$$

Notice that the electron follows the same size circle as the proton, even though it is 2,000 times lighter. Why? Because its charge is the same, and its velocity is the same. The lighter mass would normally lead to smaller radius (weaker inertia), but the radius formula shows that mass and charge scale equally in the numerator and denominator.

### Common Misconceptions

**Misconception:** A magnetic field always deflects a moving charge.

*Reality:* A magnetic field deflects a charge *only if* the charge is moving. A stationary charge in a magnetic field experiences zero force. Furthermore, a charge moving *parallel* to the magnetic field experiences zero force — the sin(θ) term vanishes when θ = 0°. The charge must be moving at an angle to the field.

**Misconception:** The magnetic force speeds up or slows down a charged particle.

*Reality:* The magnetic force is always perpendicular to the velocity, so it does no work on the particle. The speed remains constant; only the direction changes. An electric field can speed a particle up or down, but a magnetic field cannot.

---

## Concept 2: Currents Create Magnetic Fields — and Reveal a Symmetry

### The Mechanism: From Wire to Field

In 1821, a Danish physicist named Hans Christian Oersted performed an experiment that startled the scientific community. He ran a current through a wire and brought a compass needle near it. The needle deflected. The compass pointed away from the wire instead of toward the North Pole.

At that instant, the invisible wall between electricity and magnetism cracked. Electric charges in motion — currents — make magnetic fields. The universe does not give you electricity and magnetism as separate phenomena. It gives you electricity and magnetism as two faces of a single phenomenon: *electromagnetism*.

The magnetic field created by a long straight current-carrying wire forms concentric circles around the wire. Imagine looking at the wire end-on. The field circles it like tree rings. The direction is given by the right-hand rule: point your right thumb in the direction of the current, and your fingers curl in the direction of the magnetic field.

The strength of the field at distance *r* from the wire is

$$B = \frac{\mu_0 I}{2\pi r},$$

where *I* is the current in amperes and μ₀ is a fundamental constant called the permeability of free space:

$$\mu_0 = 4\pi \times 10^{-7}\text{ T} \cdot \text{m/A}.$$

This equation tells you something important: the field is strongest near the wire and weakens as 1/*r*. At twice the distance, the field is half as strong. At ten times the distance, the field is one-tenth as strong.

Now coil the wire into a solenoid — a cylindrical coil like a compressed spring. Run current through it. The magnetic fields from each loop add up inside the coil, creating a field that points along the axis of the solenoid, from one end to the other. The field looks nearly identical to that of a bar magnet. In fact, there is no essential difference. A bar magnet and a solenoid are the same thing, except that a magnet's field is generated by the spin and orbital motion of electrons inside atoms, while a solenoid's field is generated by the macroscopic flow of current through wire loops.

The field strength inside a solenoid is

$$B = \mu_0 \frac{NI}{\ell},$$

where *N* is the number of loops and *ℓ* is the length of the solenoid. More loops, stronger field. Longer solenoid, weaker field. Tighter coil, stronger field. This is the basis of the electromagnet — a device that can be switched on and off by controlling the current.

### The Trade-Off

An electromagnet is powerful, but it requires current. A permanent magnet requires no current — the atomic-scale electron motion that generates its field is "free," powered by the quantum structure of matter. But a permanent magnet cannot be turned off. An electromagnet can be turned off, adjusted, even reversed by reversing the current. The trade-off is clear: a permanent magnet costs nothing to run but is rigid. An electromagnet costs power to run but is flexible. Most practical machines use electromagnets because flexibility matters more than permanence.

### Worked Example: Field at a Distance

A long straight wire carries 1.5 amperes of current. What is the magnetic field strength 5.0 centimeters away from the wire?

$$B = \frac{\mu_0 I}{2\pi r} = \frac{(4\pi \times 10^{-7})(1.5)}{2\pi(0.050)} = \frac{(4 \times 10^{-7})(1.5)}{2(0.050)} = 6.0 \times 10^{-6}\text{ T}.$$

This is about 1/10,000th of the field strength of a typical bar magnet, but strong enough to deflect a compass needle noticeably.

### Common Misconceptions

**Misconception:** A current-carrying wire has a magnetic field everywhere around it.

*Reality:* Yes. Every current-carrying conductor generates a magnetic field. There is no such thing as a "silent" wire. The field weakens with distance, but it never truly reaches zero — it extends to infinity, getting fainter and fainter.

**Misconception:** The magnetic field inside a solenoid is uniform.

*Reality:* It is approximately uniform in the *center* of the solenoid, but near the ends the field is weaker and spreads out. The longer the solenoid relative to its diameter, the more uniform the field in the middle.

---

## Concept 3: Changing Flux Makes Current — Faraday's Asymmetrical Gift

### The Mechanism: The Induction Dance

Michael Faraday wanted to know: if current makes magnetic fields, does a magnetic field make current? In 1831, he moved a bar magnet through a wire coil and measured the current. Nothing when the magnet was stationary. Current when the magnet moved. Stop the motion, current stops. Reverse the magnet's direction, current reverses.

The key insight is this: it is not the presence of the magnetic field that matters. It is the *change* in the field.

Faraday quantified this with a concept called magnetic flux — the amount of magnetic field passing through a surface:

$$\Phi = BA\cos\theta,$$

where *B* is the field strength, *A* is the area, and *θ* is the angle between the field direction and a perpendicular to the area. When the field points straight through the area, θ = 0°, cos(0°) = 1, and flux is maximized. When the field is parallel to the surface, θ = 90°, cos(90°) = 0, and flux is zero — no field lines pass through.

The induced electromotive force (emf) — the voltage that drives current — is proportional to the rate of change of flux:

$$\varepsilon = -N\frac{\Delta\Phi}{\Delta t},$$

where *N* is the number of loops in the coil and the negative sign expresses Lenz's law, which we will examine in a moment. The SI unit of magnetic flux is the weber (Wb), and 1 weber per second equals 1 volt.

Here is what makes this remarkable: if the magnetic field doubles in strength while the coil stays fixed, the emf doubles. If the coil expands while the field stays fixed, the emf depends on how fast the area grows. If the coil rotates so the angle changes, the emf depends on the rate of rotation. Any change in the product B × A × cos(θ) will induce an emf.

*Lenz's law* is the physical insight beneath the negative sign. It states: the induced current flows in a direction such that its magnetic field *opposes the change that caused it*. If the external magnetic field is increasing, the induced current creates a field in the opposite direction. If the external field is decreasing, the induced current creates a field in the same direction, trying to keep the flux constant.

This is not merely a mathematical rule. It is a consequence of energy conservation. If the induced current always helped the external field grow (by creating a field in the same direction), you could harvest infinite energy from the growing field. That would violate conservation of energy. Instead, the induced current fights the change, making work necessary to push the magnet through the coil.

### Worked Example: A Coil in a Changing Field

A circular coil has 16 loops and a diameter of 2.0 centimeters. A uniform magnetic field passes through it perpendicular to the plane of the coil. The field strength drops from 0.020 tesla to 0.010 tesla over 34 seconds. What current is induced in the coil if the resistance is 0.10 ohm?

First, calculate the flux change. The area is

$$A = \pi r^2 = \pi(0.010)^2 = 3.14 \times 10^{-4}\text{ m}^2.$$

The change in flux is

$$\Delta\Phi = \Delta B \cdot A = (0.010 - 0.020)(3.14 \times 10^{-4}) = -3.14 \times 10^{-6}\text{ Wb}.$$

The induced emf is

$$\varepsilon = -N\frac{\Delta\Phi}{\Delta t} = -16 \times \frac{-3.14 \times 10^{-6}}{34} = 1.48 \times 10^{-6}\text{ V}.$$

Using Ohm's law, the current is

$$I = \frac{\varepsilon}{R} = \frac{1.48 \times 10^{-6}}{0.10} = 1.5 \times 10^{-5}\text{ A} = 15\text{ μA}.$$

The current is small — 15 millionths of an ampere — but it is real, measurable, and flows in the direction predicted by Lenz's law: opposing the decrease in flux by creating an upward-pointing magnetic field inside the coil.

### The Trade-Off

Induction is powerful but slow. You cannot induce a large current with a stationary magnet. You must *change* the field. The faster you change it, the larger the induced emf. This is why generators spin: spinning maximizes the rate of change of flux. And this is also why transformers require AC (alternating current) to work; DC (direct current) creates a static field, and a static field induces no current in the secondary coil.

### Common Misconceptions

**Misconception:** A magnetic field creates a current in any conductor.

*Reality:* A *static* magnetic field creates no current. Only a *changing* magnetic field induces current. A conductor at rest in a steady magnetic field will have charges in it that experience a magnetic force, but that force is perpendicular to the charges' velocity, so they cannot accelerate along the wire to create sustained current. Induction requires change.

**Misconception:** Lenz's law means the induced current always opposes the external field.

*Reality:* Lenz's law says the induced current opposes the *change* in flux. If the external field is increasing and pointing upward, the induced current creates a downward field to oppose the increase. But if the external field is already strong and pointing upward, and then weakens, the induced current creates an upward field to oppose the *decrease*. The current's job is to keep flux constant, not to cancel the external field.

---

## Integration: How These Three Concepts Build the World's Machines

Concept 1 tells you: a moving charge in a magnetic field experiences a force perpendicular to its motion. Use this at scale — put many charges in a wire loop, run current through it, place it in a magnetic field — and the whole loop experiences a torque. It wants to rotate.

This is how electric motors work. A coil of wire in a magnetic field, with current flowing through it, rotates. To keep it rotating in the same direction (rather than oscillating back and forth), you reverse the current every half rotation using automatic switches called brushes. The current reversal keeps the torque pointing the same way. The coil spins. Attach a shaft to it, and you have converted electrical energy into mechanical motion. This principle powers every electric motor on Earth — from the tiny motors in cell phones to the industrial motors that drive manufacturing.

Concept 2 tells you: a moving charge creates a magnetic field. Reverse the motor: make the shaft turn by hand (or by wind, water, or steam). The coil rotates in the magnetic field. The charges in the wire move through the field. They experience a magnetic force perpendicular to their motion (from Concept 1), and that force has a component along the wire, pushing charges forward. This builds up a potential difference — an emf. Current flows. You have converted mechanical energy into electrical energy.

This is how electric generators work. It is the same machinery as the motor, but in reverse. This principle powers every grid-scale power plant: hydroelectric dams spin turbines by falling water; coal and nuclear plants use steam to spin turbines; wind turbines use wind. All of them use rotating coils in magnetic fields to convert motion into electricity.

Concept 3 tells you: a changing magnetic field induces an emf in a conductor. Take two coils, side by side but not touching. Run an alternating current through the first coil — the primary. The current creates a changing magnetic field. That changing field passes through the second coil — the secondary. An emf is induced in the secondary. No moving parts. No mechanical connection. Just the invisible action of changing flux.

This is how transformers work. They step voltages up (for long-distance transmission) or down (for household use). Without transformers, the power grid as we know it could not exist. You cannot transmit electricity efficiently at low voltage; the resistance in the wires dissipates too much energy as heat. You must step up the voltage before transmission, which simultaneously steps down the current (P = IV, so if power is fixed and voltage rises, current falls). Lower current means lower resistive losses.

When the power arrives near your home, a step-down transformer brings the voltage back down to 120 or 240 volts. Again, no moving parts. Just Faraday's law at work.

---

## Graduated Exercises

**Warm-up (check understanding):**

1. A proton moves northward at 2.0 × 10^6 m/s through a magnetic field pointing westward. Using the right-hand rule, in which direction is the magnetic force on the proton?

2. A wire carrying current downward is placed in a magnetic field pointing to the right. Using the right-hand rule for F = IℓB, determine the direction of the force on the wire.

3. A bar magnet is moved toward a wire coil. Does the induced current in the coil create a magnetic field that attracts or repels the approaching magnet? (Hint: Lenz's law.)

**Application (extend the mechanism):**

4. A rectangular loop of wire is in a uniform magnetic field pointing out of the page. The loop rotates about a horizontal axis. At the moment shown, the plane of the loop is perpendicular to the page. Is the flux through the loop at a maximum, a minimum, or somewhere in between? What is the value of θ in Φ = BA cos(θ)?

5. A solenoid with 500 turns, each of area 0.010 m², carries 2.0 amperes of current. Calculate the magnetic field strength inside the solenoid if the solenoid is 0.25 meters long. (Use B = μ₀NI/ℓ.)

6. An electron enters a magnetic field of 0.30 T, moving perpendicular to the field at 1.5 × 10^6 m/s. Calculate the radius of its circular path. (Use r = mv/qB. Electron mass: 9.11 × 10^−31 kg. Electron charge magnitude: 1.60 × 10^−19 C.)

**Synthesis (combine concepts):**

7. A generator coil rotates at 60 Hz (60 revolutions per second) in a magnetic field of 0.50 T. The coil has 100 turns, each with area 0.020 m². What is the peak emf induced in the coil? (Hint: for a rotating coil, the emf oscillates as ε = ε₀ sin(ωt), where ω = 2πf and ε₀ = NABω.)

8. A copper rod slides across two parallel rails in a magnetic field of 0.25 T, perpendicular to both the rails and the rod. The rails are separated by 0.10 m. The rod moves at 2.0 m/s. What emf is induced across the rod? If the circuit has a total resistance of 50 ohms, what current flows?

**Challenge (push deeper):**

9. In the generator example above (Exercise 7), the coil rotates through a complete cycle (360°) in 1/60 second. At which moments in the cycle is the induced emf zero? At which moments is it at maximum? Why? (Hint: emf depends on dΦ/dt, the rate of change of flux, not the flux itself.)

10. A superconducting loop (zero resistance) hangs in a region of magnetic field. A magnet approaches the loop from above. By Lenz's law, the loop will generate a current to oppose the change in flux. For a superconductor, once a current starts, it persists forever without any external emf. Will the magnet eventually fall through the loop, or will it be repelled? What does this tell you about the relationship between induced currents and magnetic forces?

---

## Chapter Summary

Magnetism emerges from moving charges. A charge moving through a magnetic field experiences a force perpendicular to both its velocity and the field — a force that bends paths but does no work. A charge in motion creates a magnetic field around itself, forming concentric circles in the case of a straight wire or an axis-aligned field in the case of a coil. A changing magnetic field induces an emf in a conductor, driving current in a direction that opposes the change — Lenz's law. These three principles are the machinery of electromagnetism.

They explain why a compass needle points north (Earth's rotating core generates a magnetic field). They explain why you cannot pull the poles of a magnet apart (every piece of moving charge creates a dipole). And they power the technologies that have become invisible to us: the motors in our devices, the generators that create the electricity flowing into our homes, the transformers that step it up and down so it can be delivered to us.

The deeper insight is symmetry. Electricity makes magnetism. Magnetism makes electricity. They are not separate forces. They are two manifestations of one force, revealed when charges move. This fusion of electricity and magnetism into a single framework — electromagnetism — was one of the great unifications of physics, and it opened the door to understanding light itself. Light, it turns out, is a propagating electromagnetic wave: a self-sustaining oscillation of electric and magnetic fields, speeding through space at the one universal constant speed. But that is a chapter ahead.

---

## Connections Forward

In the next chapter, we examine electromagnetic waves — oscillating electric and magnetic fields that can travel through empty space. You will see how Faraday's law and Ampere's law (the symmetrical partner to Faraday's law, showing that changing electric fields create magnetic fields) combine to create the wave equation. Light, radio, X-rays, and all other electromagnetic radiation emerge from this framework. The patterns you see here — the perpendicularity of forces and fields, the symmetry between electric and magnetic phenomena, the centrality of changing flux — will reappear there.

You will also encounter the deep question: are electric and magnetic fields real, existing independently in space, or are they just mathematical conveniences for calculating forces? Maxwell's equations answer this question decisively. The fields are real. They carry energy. They can propagate. And in their oscillation, they create the light that lets you see the world.

---

**What would change my mind:** If experiments showed that magnetic monopoles exist — single poles of magnetic charge that could be isolated — the entire framework would need revision. But despite intensive searches at the largest particle accelerators and in the most sensitive experiments, no monopole has ever been found. This absence itself is evidence that the framework is correct: magnetic dipoles are inevitable whenever you have moving charges.

**Still puzzling:** I do not fully understand the *microscopic origin* of ferromagnetism — why some materials like iron exhibit such strong magnetic effects compared to others. The standard explanation invokes electron spin and orbital angular momentum within atoms, with exchange interactions favoring aligned spins. But the full story involves subtle quantum mechanics and condensed-matter physics that extends beyond this chapter. It works, but the machinery underneath remains opaque to me at the level of detailed first principles.

---

**Tags:** magnetism, electromagnetic induction, Faraday's law, Lenz's law, electric motors, generators, transformers, magnetic flux, permeability

**Byline:** Nik Bear Brown
---

## LLM Exercise — Chapter 20: Magnetism (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the electromagnet from a nail + the iron-filings field-pattern visualization + an induction demonstration.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 20 demo. Notebook in this Claude Project. Chapter 20
taught: magnetic field; force on a moving charge (F = qv × B);
current-carrying wires create magnetic fields (Ampère's law);
electromagnetic induction (changing magnetic flux induces an EMF
— Faraday's law); generators and transformers as applied
electromagnetism.

Two short demos.

**Demo A — Simple Electromagnet**

Materials:
- A long iron nail (3-4 inches; magnetic — test with a magnet
  before starting).
- A battery (9V or AA).
- Insulated wire (3-5 meters of thin gauge; magnet wire ideal,
  insulated multi-strand also fine).
- Small steel objects: paper clips, staples, small screws.

Procedure:
1. Wrap the wire around the nail tightly: 50-100 turns. Leave
   ~10 cm of wire free at each end. Strip insulation off both
   ends.
2. Connect the wire ends to the battery (briefly! the wire and
   battery will get hot).
3. Test: the nail should now attract paper clips. Count how
   many.
4. Disconnect. The magnetic field is gone; the paper clips drop.

Variations:
- Try with more turns of wire — magnetic strength increases.
- Try with a stronger battery (9V instead of AA) — strength
  increases.
- Try without the iron nail (just air-core coil) — much weaker
  magnetism.

The physics: current in the coil produces a magnetic field
(Ampère's law); the iron core concentrates and amplifies the
field (high magnetic permeability of iron).

**Demo B — Induction (Faraday's Law)**

Materials:
- A coil of wire (the same one from Demo A works; remove the
  nail).
- A multimeter set to read low-voltage AC or DC.
- A magnet (a refrigerator magnet works; a stronger neodymium
  magnet works much better).

Procedure:
1. Connect the coil's wire ends to the multimeter.
2. Move the magnet rapidly TOWARD the coil. The multimeter
   should briefly read a small voltage.
3. Move the magnet AWAY rapidly. Voltage swings the OTHER
   direction (sign reverses).
4. Move slowly. Voltage is much smaller (induction depends on
   rate of change of flux, dΦ/dt).

The physics: changing magnetic field through the coil induces
an EMF (voltage). The faster the change, the larger the EMF.
This is how generators work.

**Use Claude as a thinking partner:**
- Before A: "Predict the magnetic field strength of a 100-turn
  coil carrying 1 amp around a 10-cm iron nail."
- After B: "Why does moving the magnet AWAY produce voltage in
  the OPPOSITE direction from moving it TOWARD?"

**Notebook entry should include:**
- Photos of both demos.
- For A: max paper clips lifted; effect of more turns.
- For B: voltage readings for fast vs. slow motion; sign
  difference for approach vs. retreat.
- One real-world application: every electric motor uses Demo
  A's principle; every electric generator uses Demo B's
  principle.

End with: a transformer changes voltage but conserves power
(P = VI). If a transformer steps voltage up by 10×, what
happens to current? Why does this matter for power transmission
across long distances?
```

---

**What this produces:** A demo entry with a working electromagnet and a working induction generator. The connection between the two — both are aspects of the same electromagnetic field — is one of physics's deepest unifications (Maxwell's contribution).

**How to adapt this prompt:**

- *For your own project:* Magnet wire (insulated, single-strand) is best for the coil because it's thin and lets you fit many turns. Available cheaply.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional for plotting voltage-vs-time if you can sample the multimeter.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 18's stationary charges and Ch 19's flowing charges culminate in Ch 20's magnetic phenomena. Faraday's law connects Chs 18-20 into one electromagnetic story.

**Preview of next chapter:** Chapter 21 is the quantum nature of light. You'll do an LED-threshold-voltage demo — different colors of LEDs light up at different battery voltages, demonstrating that photon energy depends on frequency (E = hf).


---

## AI Wayback Machine

**Hans Christian Ørsted** discovered electromagnetism in 1820 by noticing a compass deflection near a current-carrying wire.

**Run this:**

```
Who is Hans Christian Ørsted, and how does their work connect to magnetism we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hans Christian Ørsted"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Hans Christian Ørsted's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Hans Christian Ørsted's framework."

What changes? What gets better? What gets worse?
