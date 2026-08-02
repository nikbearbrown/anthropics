# Chapter 3 — Electric Potential and Electric Field

**Suggested titles**

1. Electric Potential and Electric Field
2. Volts, Joules, and the Energy Stored in Empty Space
3. Why a Defibrillator's Capacitor Saves Lives in 1.5 Milliseconds

**TL;DR.** Electric potential — measured in volts — is electric potential energy per unit charge: $V = U/q$. The relation between potential and electric field is $E = -\Delta V/\Delta x$ for parallel-plate geometry. For a point charge, $V = kQ/r$. Capacitors store charge $Q = CV$ and energy $U = \frac{1}{2}CV^2$, with practical applications from camera flashes to AED defibrillators that deliver 200 joules in milliseconds. By the end of the chapter you can compute potentials and energies for simple charge distributions and capacitor configurations.

---

## A 200-joule jolt to a stopped heart

A patient collapses in cardiac arrest in a Boston subway station, 2018. A bystander grabs the wall-mounted AED — automated external defibrillator — opens it, sticks the pads on the patient's chest, and stands back. The device analyzes the heart rhythm, decides shock is warranted, and discharges its capacitor: about 200 joules of electrical energy delivered through the patient's chest in roughly 1.5 milliseconds.

200 joules is not a lot of energy. It is roughly the kinetic energy of a thrown baseball. But delivered in 1.5 ms, it represents an instantaneous power of $200/0.0015 \approx 133$ kW — more than a hundred household microwaves running at once. That brief, focused pulse depolarizes the heart muscle simultaneously, allowing the cardiac sinoatrial node to reassert a normal rhythm. About 70% of cardiac-arrest victims who get defibrillated within five minutes of collapse survive to leave the hospital.

The hardware that makes this possible is a capacitor — a device that stores electric charge on one plate, an equal opposite charge on another plate, with empty space (or insulator) between them. The energy is stored in the *electric field* between the plates. When the discharge button fires, the stored field collapses through the patient's chest, dumping its energy as electric current.

This is what voltage is for. Voltage tells you how much energy you can deliver per unit charge. A 9-volt battery delivers 9 joules per coulomb of charge that flows through it. A defibrillator's capacitor at 2,000 volts delivers 2,000 joules per coulomb. The chapter is about pinning down what voltage means physically, how it relates to electric fields, and how capacitors store the electrical energy that makes a hundred kilowatts of brief power possible from a battery you can carry.

**Learning objectives.** By the end of this chapter you should be able to:

1. Define electric potential energy, electric potential ($V = U/q$), and the volt as J/C.
2. Compute the work done on a charge by an electric field as $W = q\Delta V$, and the kinetic energy gained from an accelerating field.
3. Relate uniform electric field to potential difference: $E = V/d$ for parallel plates separated by $d$.
4. Compute the electric potential at a distance from a point charge: $V = kQ/r$.
5. Sketch and interpret equipotential surfaces, including the property that field lines are perpendicular to equipotentials.
6. Compute the capacitance of a parallel-plate capacitor: $C = \epsilon_0 A/d$, and the energy stored: $U = \frac{1}{2}CV^2$.
7. Combine capacitors in series and in parallel.

**Prerequisites.** Chapter 18 (charge, Coulomb's law, electric field). Chapter 7 (work, energy, conservation). Algebra and basic vector arithmetic.

**Why this chapter matters.** Voltage is the language of practical electricity. Every battery, every wall outlet, every signal in your phone is described by a voltage. Capacitors are everywhere in modern electronics — power supply smoothing, RAM cells, camera flashes, defibrillators, and the gates of every transistor in your computer. The energy-stored-in-fields concept you build here is the foundation for electromagnetic radiation in Chapter 24.

---

## Concept 1 — Electric potential energy and voltage

### Watching a single charge fall through a 1-volt drop

Imagine the simplest possible experiment: an electron sits between two parallel metal plates, the upper plate held at +1 volt relative to the lower plate. The electron, being negatively charged, is attracted upward. Released from rest, it accelerates toward the positive plate, gaining kinetic energy from the electric field's work.

By the time it reaches the upper plate, the electron has gained exactly $1 \text{ eV}$ — one electron-volt — of kinetic energy. That is the energy unit physicists use most often for atomic-scale processes: the energy gained by an electron falling through a one-volt potential difference. In SI units,

$$1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}.$$

Tiny. But the right scale for atoms — the binding energy of a hydrogen atom is 13.6 eV; the gap between molecular bonding orbitals is a few eV; visible light photons carry 1.5–3 eV. A solar panel works because photons in this energy range can knock electrons across a band gap of a similar size. Voltage and energy talk the same language across the entire periodic table.

### The mechanism — defining potential

Electric potential energy $U$ is the work done against the electric force to move a charge from a reference point to its current position. Like gravitational potential energy, only differences matter; the zero is conventional.

**Electric potential** $V$ — also called *voltage* — is defined as electric potential energy per unit charge:

$$V = \frac{U}{q}.$$

The SI unit is the **volt**, with $1 \text{ V} = 1 \text{ J/C}$.

The crucial bookkeeping fact: the work done by the electric field on a charge moving from point A to point B is

$$W_{A \to B} = q(V_A - V_B) = -q \Delta V,$$

with $\Delta V = V_B - V_A$. A positive charge moving from high potential to low potential gains kinetic energy. A negative charge moving from low potential to high potential gains kinetic energy. (Sign carefully — a negative charge "falls uphill" in voltage.)

By energy conservation, in the absence of friction or other losses, the kinetic energy gained equals the change in electric potential energy:

$$\frac{1}{2} m v^2 = q |\Delta V|.$$

This is how electron guns in old CRT monitors and modern X-ray tubes work — accelerate electrons through a controlled voltage to produce a beam of known kinetic energy.

### The trade-off

Defining potential as energy-per-unit-charge trades **vector force language for scalar energy language.** The electric field is a vector; potential is a scalar. Calculations involving energy are usually simpler than the vector arithmetic of forces, especially for assemblies of many charges. The cost: potential alone doesn't tell you the direction of the field, so you sometimes need to compute $\vec{E}$ directly (next concept).

### Worked example — accelerating an electron through 100 volts

You apply 100 V across a parallel plate setup and release an electron from the negative plate. What is its speed when it reaches the positive plate? (Mass $m_e = 9.11 \times 10^{-31}$ kg.)

**Reasoning.** Energy conservation:

$$\frac{1}{2} m v^2 = e \cdot V \implies v = \sqrt{\frac{2eV}{m_e}}.$$

Plug in:

$$v = \sqrt{\frac{2 (1.602 \times 10^{-19})(100)}{9.11 \times 10^{-31}}} = \sqrt{\frac{3.204 \times 10^{-17}}{9.11 \times 10^{-31}}} = \sqrt{3.52 \times 10^{13}} \approx 5.93 \times 10^6 \text{ m/s}.$$

About 6 million meters per second — 2% of the speed of light. Already, at 100 V, classical mechanics is becoming inaccurate; relativistic corrections matter at higher voltages. This is the speed regime where electrons in old CRT TVs hit the screen.

**Sanity check.** The kinetic energy is $eV = 100$ eV. Converting back: $\frac{1}{2} m v^2 = \frac{1}{2}(9.11 \times 10^{-31})(5.93 \times 10^6)^2 \approx 1.6 \times 10^{-17}$ J = $100$ eV. Consistent.

### Common misconceptions

- *"High voltage always means dangerous."* Voltage alone doesn't kill; current does. A static spark from a doorknob can be 10,000 V but harmless because the available current is microamps. A 12-V car battery can deliver 100+ amps and ignite gasoline. Voltage tells you energy per charge; current tells you charges per second. Both matter.
- *"Potential and potential energy are the same thing."* Potential is energy-*per-unit-charge*. The energy of a specific charge $q$ at potential $V$ is $U = qV$.
- *"Ground is zero potential because it has zero charge."* No — ground is a *reference* point, conventionally chosen because the Earth is so large that adding/removing modest charge barely changes its potential.

↳ **Dig Deeper — Why voltage and current both matter for electrical safety**

*Electrical injury depends on the current that flows through the body, not just the voltage. The relationship is set by the body's resistance (typically 1 kΩ–100 kΩ depending on dryness, contact area, path through body) and Ohm's law. A 120 V wall outlet through wet skin can drive lethal current; the same voltage through dry callused hands might just startle.*

**Prompt:**
> Explain why electrical safety depends on current, not voltage alone. Use Ohm's law to show how the same voltage can produce vastly different currents through wet vs. dry skin. Then walk through the threshold currents for human physiological effects: <1 mA (imperceptible), 1–5 mA (startle), 10–30 mA (loss of muscle control, "let-go" threshold), 50–150 mA (likely fatal through ventricular fibrillation). End with one sentence on why high-voltage power lines are dangerous primarily because of the current they can drive once contact is made.

**What to do with the output:** Save it. The voltage-vs-current safety distinction is the most important practical implication of this chapter.

---

## Concept 2 — Field, potential, and equipotentials

### A 1.5 V battery and a 1 mm gap

Take a fresh AA battery (1.5 V) and imagine connecting its terminals to two parallel metal plates 1 mm apart. The electric field between the plates is

$$E = \frac{V}{d} = \frac{1.5}{0.001} = 1500 \text{ V/m}.$$

That's a respectable field — enough to noticeably deflect a free electron in the gap. And it came from a humble AA battery and a millimeter of space. Geometry concentrates voltage: the smaller the gap for a given voltage, the stronger the field.

This is why high-precision capacitors use micrometer-scale gaps, why semiconductor MOSFET gates have gate-oxide thickness measured in atoms, and why dust storms on Mars produce locally enormous fields between charged grains.

### The mechanism — relating $E$ and $V$

For a uniform field (parallel plates, ignoring edge effects), the potential difference between the plates separated by distance $d$ is

$$\Delta V = E \cdot d,$$

or equivalently $E = \Delta V / d$. The field points from high potential to low potential.

In the general case, the relation is a derivative: in one dimension,

$$E = -\frac{dV}{dx}.$$

The negative sign captures that $E$ points "downhill" in potential. In three dimensions, $\vec{E} = -\nabla V$ — the field is the negative gradient of the potential. For introductory problems we use $E = V/d$ for parallel plates and $V = kQ/r$ for point charges.

### Potential of a point charge

Setting the reference at infinity ($V = 0$ at $r = \infty$), the potential at distance $r$ from a point charge $Q$ is

$$V = \frac{kQ}{r}.$$

Notice this drops off as $1/r$, not $1/r^2$ like the field. Potential is energy-per-unit-charge, and energy goes as $1/r$ for an inverse-square force (familiar from gravity: gravitational PE goes as $-1/r$).

For multiple point charges, potentials superpose *as scalars* (no vector arithmetic):

$$V_\text{total} = \sum_i \frac{k Q_i}{r_i}.$$

This is one of the major advantages of working with potential rather than field: scalar sums instead of vector sums.

### Equipotential surfaces

An **equipotential surface** is a surface on which $V$ is constant. Key properties:

1. The work done moving a charge along an equipotential is zero (no $\Delta V$).
2. Field lines are everywhere perpendicular to equipotential surfaces (because the field is the gradient of potential, and the gradient is perpendicular to level sets).
3. The surface of any conductor in equilibrium is an equipotential (no $\Delta V$, otherwise charges would flow).

For a single positive point charge, equipotentials are concentric spheres. For parallel plates, equipotentials are planes parallel to the plates, with $V$ varying linearly between them. For a dipole, equipotentials curve around the two charges, perpendicular to the field lines you saw in Chapter 18.

### The trade-off

Working in terms of potential trades **directional information for arithmetic simplicity.** A scalar potential is easier to add and integrate than a vector field. But the field $\vec{E}$ tells you forces directly; you cannot get there from $V$ alone without taking a derivative. In practice, both representations get used, and translating fluently between them is a key skill.

### Worked example — escape speed of an electron from a hydrogen atom

A hydrogen atom is a single proton with an electron orbiting at the Bohr radius $r = 5.29 \times 10^{-11}$ m. What kinetic energy must we give the electron for it to escape to infinity (ionization)?

**Reasoning.** The potential at the electron's position, due to the proton:

$$V = \frac{ke}{r} = \frac{(8.99 \times 10^9)(1.602 \times 10^{-19})}{5.29 \times 10^{-11}} \approx 27.2 \text{ V}.$$

The potential energy of the electron (charge $-e$) at this potential:

$$U = -eV = -(1.602 \times 10^{-19})(27.2) = -4.36 \times 10^{-18} \text{ J} = -27.2 \text{ eV}.$$

To escape (where $U = 0$), the electron needs kinetic energy $+27.2$ eV. But classical mechanics says the electron also has kinetic energy in its current orbit equal to half the magnitude of the potential energy (virial theorem) — about $13.6$ eV. So the *additional* energy needed is $27.2 - 13.6 = 13.6$ eV.

That number — 13.6 eV — is the **Rydberg energy**, the ionization energy of hydrogen. It is one of the most measured numbers in atomic physics, agreeing with theory to many decimal places. Our back-of-envelope reasoning has reproduced it.

**Sanity check.** A 13.6 eV photon has wavelength ~91 nm — far ultraviolet, the Lyman-limit edge. UV photons above this energy ionize hydrogen; photons below cannot. This wavelength is observed exactly where predicted in stellar spectra.

### Common misconceptions

- *"Field equals potential divided by distance."* Only for *uniform* fields and parallel geometry. For point charges, $E = kQ/r^2$ and $V = kQ/r$ — different powers of $r$.
- *"Equipotential surfaces are just visual aids."* They are visual aids and they are real surfaces in space. In a metal, every point of the surface is at the same potential — you can demonstrate this with a voltmeter.
- *"A negative charge can do work on you, since it has negative potential energy."* Be careful with signs. The work done depends on $\Delta V$ and the sign of $q$, not just one.

↳ **Dig Deeper — The Van de Graaff generator and breakdown voltage**

*A Van de Graaff generator can sustain hundreds of thousands of volts on a polished metal sphere — but only up to a limit set by the breakdown voltage of air (~3 MV/m). Beyond that field strength, air molecules ionize and the charge leaks away as a corona discharge or spark. This sets practical limits on every high-voltage device.*

**Prompt:**
> Explain how a Van de Graaff generator works: the rubber belt physically transports charge from a small electrode to a large sphere, building up potential. Compute the maximum voltage a Van de Graaff sphere of radius $r$ can sustain in air, given the breakdown field of air ($E_\text{max} \approx 3 \times 10^6$ V/m). Solve $E_\text{max} = kQ/r^2$ for the maximum charge, then substitute into $V = kQ/r$ to express maximum voltage purely as $V_\text{max} = E_\text{max} \cdot r$. End with one sentence on why this scaling explains why physics demonstrations use large spheres (~30 cm radius can sustain ~1 MV) and why power transmission lines use elaborate insulator strings.

**What to do with the output:** Save it. Breakdown voltage limits show up everywhere — capacitor design, transmission line design, MOSFET gate-oxide thickness, lightning physics.

---

## Concept 3 — Capacitors and stored energy

### A defibrillator on a defibrillator-pad cart

A typical hospital crash-cart defibrillator has a capacitor rated at about 32 microfarads (32 μF) and charges to about 5,000 volts before discharge. The energy stored:

$$U = \frac{1}{2} C V^2 = \frac{1}{2} (32 \times 10^{-6})(5000)^2 = \frac{1}{2} (32 \times 10^{-6})(2.5 \times 10^7) = 400 \text{ J}.$$

400 joules. That number, the same kinetic energy as an apple falling 200 meters, sits stored in a small device the size of a deck of cards, in the electric field between two thin plates of metal separated by an insulating film. When the operator presses the discharge button, the stored field collapses through the patient's chest in a few milliseconds — peak power on the order of $400/0.005 = 80$ kW.

A capacitor is the canonical device for storing electrical energy in a field. Camera flashes, defibrillators, signal-filtering circuits, the RAM in your computer — all use capacitors. This concept gives you the equations.

### The mechanism — capacitance defined

A **capacitor** is two conductors separated by an insulator (or vacuum). When you connect a battery across them, charge $+Q$ accumulates on one conductor and $-Q$ on the other. The relation between charge stored and voltage across is

$$Q = CV,$$

where $C$ is the **capacitance**. The SI unit is the **farad** (F), with $1 \text{ F} = 1 \text{ C/V}$. A farad is enormous; practical capacitors are typically picofarads (pF, $10^{-12}$ F) to millifarads (mF). The 1-farad supercapacitors sold at electronics stores are remarkable specifically because of how rare a full farad is in a small package.

Capacitance depends on geometry. For a parallel-plate capacitor with plate area $A$ and separation $d$, with vacuum between:

$$C = \frac{\epsilon_0 A}{d},$$

where $\epsilon_0 = 8.85 \times 10^{-12} \text{ F/m}$ is the **permittivity of free space**. Larger area = more charge stored at given voltage. Smaller gap = stronger field at given charge = more charge needed to reach given voltage = larger $C$.

If you fill the gap with an **insulator** (a "dielectric") of relative permittivity $\kappa$ (kappa), capacitance scales by $\kappa$:

$$C = \frac{\kappa \epsilon_0 A}{d}.$$

Common dielectrics: paper ($\kappa \approx 3$), plastic films ($\kappa \approx 3$), tantalum oxide ($\kappa \approx 25$), ceramic ($\kappa \approx 100$–$10{,}000$). Modern commercial capacitors squeeze enormous capacitance into small volumes by using high-$\kappa$ dielectrics and very thin layers.

### Energy stored

The work done to charge a capacitor from 0 to $Q$ is the integral of $V \, dq$, which works out to

$$U = \frac{1}{2} \frac{Q^2}{C} = \frac{1}{2} CV^2 = \frac{1}{2} QV.$$

The half-factor is geometric — as the capacitor charges, its voltage rises linearly from 0 to $V$, so the average voltage during charging is $V/2$.

### Capacitors in series and parallel

Two capacitors in **parallel** (same voltage, charges add):

$$C_\text{parallel} = C_1 + C_2.$$

Two capacitors in **series** (same charge, voltages add):

$$\frac{1}{C_\text{series}} = \frac{1}{C_1} + \frac{1}{C_2}.$$

Series capacitance is always *smaller* than the smallest individual capacitor. Parallel capacitance is always *larger* than the largest individual capacitor.

### The trade-off

Practical capacitor design trades **energy density for breakdown safety.** Higher energy density (more $U$ per unit volume) requires either thinner dielectric (smaller $d$, larger $C$) or higher voltage — but both push you toward the dielectric breakdown limit. Every commercial capacitor is a balance: maximum stored energy that won't fail under normal operating conditions.

### Worked example — energy in an AED capacitor

An AED stores 200 J at 2,000 V. Find (a) the capacitance, (b) the charge stored, (c) the average current during a 1.5 ms discharge.

**(a)** $U = \frac{1}{2} CV^2 \implies C = 2U/V^2 = 2(200)/(2000)^2 = 400/(4 \times 10^6) = 10^{-4}$ F = 100 μF.

**(b)** $Q = CV = (10^{-4})(2000) = 0.2$ C.

**(c)** Average current $I = Q/t = 0.2/0.0015 \approx 133$ A.

**Sanity check.** A typical defibrillator delivers ~30–40 A peak through the patient (resistance ~50 Ω at the chest). Our 133 A averaged over 1.5 ms is consistent with peak currents in the right range — actual discharge profiles have a fast spike and decay, not a uniform pulse.

### Common misconceptions

- *"Adding more capacitors in series increases capacitance."* No — series *decreases* it. Parallel increases it. Opposite of how resistors combine.
- *"Capacitors store charge, not energy."* They store both. The charge is what you can move; the energy is in the field between the plates.
- *"Once charged, a capacitor is a battery."* Not really — a capacitor's voltage drops as charge leaves; a battery maintains its voltage by chemistry. A capacitor delivers a fast brief pulse; a battery delivers steady current for a long time.

↳ **Dig Deeper — Where the energy "lives" in a charged capacitor**

*A surprising and deep claim: the energy in a charged capacitor isn't on the plates or in the wires. It's in the electric field between the plates. The energy density is $u = \frac{1}{2} \epsilon_0 E^2$ — a property of empty space wherever there's an electric field. This is the conceptual leap from particles-and-forces to fields-as-physical-objects, and it sets up the energy-carrying electromagnetic waves of Chapter 24.*

**Prompt:**
> Explain why we say the energy of a charged capacitor lives in the electric field between the plates, not on the plates themselves. Derive the volumetric energy density $u = \frac{1}{2}\epsilon_0 E^2$ for a parallel-plate capacitor with vacuum between the plates: start from $U = \frac{1}{2}CV^2$, substitute $C = \epsilon_0 A/d$ and $V = Ed$, simplify, divide by volume $Ad$. Then explain that this same formula applies to electric fields anywhere — including the field of a point charge, the field around the Earth, the field in the empty space between you and a static-charged balloon. End with one sentence on how this prepares for the realization that EM waves carry energy in their fields as they propagate.

**What to do with the output:** Save it. The "energy lives in the field" idea is the conceptual bridge to electromagnetic radiation, where the field carries energy *without* any source charge nearby.

---

## Synthesis — voltage, field, and stored energy

Step back. Three concepts:

1. **Electric potential.** $V = U/q$. The volt is J/C. Differences in voltage drive charges; energy gained by a charge crossing $\Delta V$ is $q\Delta V$.

2. **Field-potential relation.** $E = -dV/dx$ in one dimension; $E = V/d$ for parallel plates. Equipotentials are surfaces of constant $V$, perpendicular to field lines.

3. **Capacitors store energy in fields.** $C = \epsilon_0 A/d$ (or $\kappa\epsilon_0 A/d$ with dielectric). $U = \frac{1}{2}CV^2$. Series and parallel rules opposite to resistors.

The unifying picture: charges create fields; fields can be described by a scalar potential; potential differences mean energy can be extracted by moving charges; capacitors are devices that deliberately store the energy in a controlled geometry.

### A worked example combining all three concepts — the AED redo

Reconsider the defibrillator from the chapter opener: 200 J of stored energy, ~2000 V across the capacitor.

**Charge stored** (Concept 1 + Concept 3): $Q = 2U/V = 400/2000 = 0.2$ C.

**Capacitance** (Concept 3): $C = Q/V = 0.2/2000 = 10^{-4}$ F = 100 μF.

**Field strength inside** (Concept 2): If the dielectric is 100 μm thick (a typical commercial film), $E = V/d = 2000/10^{-4} = 2 \times 10^7$ V/m. That is below the breakdown field of typical capacitor dielectrics (~$10^8$ V/m for polypropylene), so the design is safe.

**Energy density in the field** (Dig Deeper): $u = \frac{1}{2}\epsilon_0\kappa E^2$. With $\kappa \approx 2$ for polypropylene, $u = \frac{1}{2}(8.85 \times 10^{-12})(2)(2 \times 10^7)^2 \approx 3.5 \times 10^3$ J/m³.

**Volume of capacitor** (sanity check): With 200 J stored at 3500 J/m³, the dielectric volume must be $V \geq 200/3500 \approx 0.057$ m³ = 57 L. That is large for a portable AED — meaning real AEDs use much higher-$\kappa$ dielectrics (electrolytics, ceramics) to shrink the package. This is the standard trade-off in capacitor engineering.

**Scale shift.** The same equations, scaled down by ~$10^{12}$ in capacitance, govern the gate of a transistor in your phone — femtofarads of capacitance, picojoules of stored energy, switched billions of times per second. The hardware is different by twenty orders of magnitude in energy. The physics is identical.

---

## Exercises

### Warm-up

**19.1** *(LO 1)* What is the electric potential energy of a $+2 \mu$C charge at a point where $V = 100$ V?

**19.2** *(LO 1, 2)* An electron is accelerated through a potential difference of 10 V. What is its kinetic energy in joules and in eV?

**19.3** *(LO 3)* A parallel-plate capacitor has plates 2 mm apart with 12 V across them. What is the field strength?

**19.4** *(LO 6)* A 5 μF capacitor is charged to 9 V. How much energy is stored?

### Application

**19.5** *(LO 4)* What is the electric potential 30 cm from a $+5 \mu$C point charge?

**19.6** *(LO 6)* A parallel-plate capacitor has plates 10 cm × 10 cm separated by 1 mm of air. What is its capacitance? If it's charged to 100 V, how much charge is stored?

**19.7** *(LO 6, 7)* Two capacitors, $C_1 = 10$ μF and $C_2 = 20$ μF, are connected (a) in parallel, (b) in series. Compute the equivalent capacitance for each.

**19.8** *(LO 4)* Two charges, $+q$ at $x = 0$ and $+q$ at $x = a$. Compute the potential at the midpoint. Compute the field at the midpoint. Why is the potential nonzero but the field zero?

### Synthesis

**19.9** *(LO 1, 2, 3)* In an old CRT TV, electrons are accelerated through 25 kV. (a) What is the kinetic energy gained by each electron? (b) What is the speed reached? (c) Treating the screen as a parallel plate at distance 30 cm from the electron gun, what is the average field?

**19.10** *(LO 4, 5)* Compute and sketch the equipotential surfaces for (a) an isolated point charge $+Q$, (b) two point charges $+Q$ and $-Q$ separated by distance $a$, (c) two point charges $+Q$ and $+Q$.

**19.11** *(LO 6)* The membrane of a neuron acts approximately as a parallel-plate capacitor with $A \approx 10^{-9}$ m², $d \approx 7$ nm, and $\kappa \approx 7$ (lipid bilayer). (a) Compute the membrane capacitance. (b) The resting potential is about 70 mV. Compute the charge on each side of the membrane. (c) How many ions does this correspond to?

### Challenge

**19.12** *(LO 6, beyond chapter)* A "supercapacitor" rated at 1 farad, 5 V, the size of a stack of coins, can be bought commercially. (a) Compute the energy stored. (b) Compute the average current if it discharges fully in 0.1 s. (c) Compare the energy to a 9-V alkaline battery (~5000 J of chemical energy). Why don't supercapacitors replace batteries in most applications?

**19.13** *(LO 6, beyond chapter)* The quantum capacitance of a single-electron transistor — a nanoscale device — is so small that adding *one* electron raises its potential by tens of millivolts. (a) Estimate the capacitance required to raise potential by 30 mV with one electron. (b) Compare to the capacitance of a typical commercial 100 pF capacitor. (c) What does this imply about why classical capacitor design breaks down at the single-electron level?

---

## LLM Exercise — Chapter 19: Voltage in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A voltage and energy estimate for one electrical component of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 19 (Electric Potential), I want to identify ONE voltage and energy related component of my phenomenon.

Please:

1. Identify the voltage. Examples:
   - Bike commute: voltage of e-bike battery, typical drop across LED safety lights.
   - Coffee maker: 120V wall outlet, switch contacts.
   - Marathon: action potential of motor neurons (~100 mV peak).
   - Espresso machine: voltage and capacitance of pump's start capacitor.
   - Basketball: static voltage when the ball strikes the floor.

2. Compute (or look up):
   (a) The voltage in volts.
   (b) The charge involved (if a capacitor or static system).
   (c) The energy stored or transferred per cycle (in joules).

3. State your inputs and uncertainty.

4. Sanity check against the energy budget — does this voltage/energy make sense given the system's overall power consumption?

5. If a capacitor is involved, compute its capacitance and time constant if known.

6. Connect to Chapter 20 (Current and Resistance), where we'll compute the current that flows when this voltage is applied.

Save the output as logbook/chapter-19-electric-potential.md.
```

### What this produces

Your nineteenth Logbook entry — a voltage and energy estimate.

### How to adapt this prompt

- *For phenomena with no obvious voltage*: use the static-electric voltage from movement or friction; ~1000 V is typical for shoe-on-carpet contact.
- *For Claude Code:* If you have an oscilloscope trace or measurement of voltage vs. time, fit it to extract the time constant of any RC discharge.

### Connection to previous chapters

Builds on Chapter 18's electric force and field. Energy bookkeeping is from Chapter 7.

### Preview of next chapter

Chapter 20 introduces electric current — the rate of charge flow when a voltage is applied across a conductor. Ohm's law $V = IR$ ties potential, current, and resistance together. The Chapter 20 LLM Exercise will compute currents and powers for the same component.

---

## Chapter summary

Electric potential is energy per unit charge; voltages drive charges through fields and devices. Three commitments:

1. **Electric potential $V = U/q$, units J/C = volts.** Work done on a charge moving through $\Delta V$ is $q\Delta V$. The eV is the natural energy unit at atomic scales.

2. **Potential and field are linked: $E = V/d$ for parallel plates, $V = kQ/r$ for point charges.** Equipotential surfaces are perpendicular to field lines.

3. **Capacitors store energy in fields.** $C = \epsilon_0 A/d$ for parallel plates; $U = \frac{1}{2}CV^2$. Modern capacitors use dielectrics with $\kappa \gg 1$ to pack large $C$ into small volumes.

The one idea that matters most: **the energy in a charged capacitor lives in the field between the plates, not on the conductors.** This conceptual leap — fields as carriers of real energy — sets up everything in electromagnetism that follows.

The common mistake to watch for: **confusing potential ($V$) with potential energy ($U$).** They differ by a factor of $q$. A point of high potential has zero potential energy until you put a charge there.

---

## What would change my mind

The chapter argues that the parallel-plate capacitor formula and field-potential relationship cover essentially every introductory voltage problem. The argument would need revision if quantum effects (single-electron capacitance, tunneling currents) were dominant in a class of problems we treat classically. They aren't, for any device larger than a few nanometers, but at extreme miniaturization (transistor gates in 3 nm process nodes) the classical formulas break down.

## Still puzzling

The deepest puzzle this chapter raises and partially resolves: *where does the energy actually live in an electric field?* We assert it lives in the field, with energy density $\frac{1}{2}\epsilon_0 E^2$. This is exactly correct mathematically and consistent with all observations. But the conceptual claim — that empty space, in the presence of a field, contains real energy — is a profound idealization. We will use it again and again. Whether the field is truly a substance or just a useful mathematical fiction is, at the deepest level, a question about ontology that physics gives us precise machinery for and only fragmentary philosophical answers about.

---

## Connections forward

Chapter 20 introduces **electric current** — the flow of charge through conductors when a voltage is applied — and Ohm's law $V = IR$. Chapter 21 builds circuits from resistors, capacitors, and batteries. Chapter 22 introduces magnetism. Chapter 23 introduces electromagnetic induction, where changing magnetic fields generate voltages — the physics of generators, transformers, and the entire electrical grid. Chapter 24 reveals that electric and magnetic fields together propagate as waves at speed $c$ — light. The voltage you computed for an AED here is a small piece of the physics that runs the world.

---

**Tags:** electric-potential, voltage, capacitance, capacitors, energy-storage

---

## AI Wayback Machine

**Alessandro Volta** invented the voltaic pile in 1800 — the first chemical battery, capable of producing a continuous current rather than the brief discharges of static-electric experiments. The unit of electric potential bears his name.

**Run this:**

```
Who was Alessandro Volta, and how does his battery work connect to the electric potential we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Alessandro Volta"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a voltaic pile produces a potential difference from chemical reactions.
- Ask it about Volta's dispute with Luigi Galvani over animal electricity, and what each got right.

What changes? What gets better? What gets worse?
