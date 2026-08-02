# Chapter 19 — Electric Potential and Electric Field

*The energy you can't see, stored in nothing at all.*

---

Here is a question that sounds simple but turns out to be deep: what does a volt actually measure?

You know what a volt is in the way you know what a calorie is — you've seen the number on a label, you know bigger is more of something. A 9-volt battery is stronger than a 1.5-volt battery. A 120-volt wall outlet is dangerous. A 40,000-volt spark from a Van de Graaff generator makes your hair stand up. But *what is a volt, physically?* What is actually different about the space around a 9-volt battery compared to a 1.5-volt battery?

The answer is: **a volt is a joule per coulomb.** It measures energy per unit charge. A 9-volt battery will give 9 joules of energy to every coulomb of charge that flows through it. A 1.5-volt battery gives 1.5 joules per coulomb. That's the whole definition. If you understand it, you can figure out everything else in this chapter.

Let me make it more concrete. Suppose you have a single proton sitting in a region of space where the electric potential is 9 volts. If you let that proton flow through a circuit to a region where the potential is 0 volts — ground — it will gain $9 \text{ V} \times 1.6 \times 10^{-19} \text{ C} = 1.44 \times 10^{-18}$ joules of kinetic energy. Tiny. Now suppose instead you send one mole of protons — $6 \times 10^{23}$ of them — through the same 9-volt drop. Each picks up $1.44 \times 10^{-18}$ J, so together they pick up about 866 joules. Roughly the energy in a quarter-cup of gasoline. This is not magic: it is exactly what a 9-volt battery does when it runs a current.

This is why we define potential. Force on a charge is a vector — it has a direction, it points somewhere. Potential is a scalar — it's just a number at each point in space, like temperature. And it turns out that for calculating energy, which is almost always what engineers and physicists care about, the scalar is far easier to work with than the vector. You add scalar potentials; you have to add vector fields. The price you pay for simplicity is that the scalar doesn't directly tell you which way things will move — you have to take a derivative to get back to the force.

---

## The machinery: work, energy, and the definition of $V$

Start from what you already know about work. The work done on a charge $q$ moving through an electric field is equal to the change in its kinetic energy, by the work-energy theorem. We define the **electric potential energy** $U$ such that the work done by the field equals the decrease in $U$:

$$W_\text{field} = -\Delta U = -(U_\text{final} - U_\text{initial}).$$

![Plot of V(x) and |E(x)| along the line connecting two equal positive charges. V is symmetric with a local minimum at midpoint (still high — only relatively low). |E| is zero at midpoint. Common student trap: high V doesn't...](../images/19-electric-potential-and-electric-field-fig-04.png)
*Figure 19.4 — Saddle Point Between Two Equal +q — V High, E Zero*

This is the same bookkeeping as gravitational potential energy: when a ball falls, the field (gravity) does positive work, and the gravitational PE decreases. When a positive charge moves from high potential to low potential, the electric field does positive work, and the electric potential energy decreases.

Now define electric potential $V$ as potential energy per unit charge:

$$\boxed{V = \frac{U}{q}}.$$

The unit is the volt: $1 \text{ V} = 1 \text{ J/C}$.

The work done by the field on charge $q$ moving from point A to point B is

$$W = q(V_A - V_B) = -q\,\Delta V,$$

with $\Delta V = V_B - V_A$.

This has a beautiful consequence for atomic physics. Physicists work constantly with electrons, protons, and other charged particles that move through potential differences. Instead of writing energies in joules — which are always some tiny multiple of $10^{-19}$ — they define the **electron-volt**: the energy gained by an electron (charge $e = 1.6 \times 10^{-19}$ C) falling through a potential difference of one volt.

$$1 \text{ eV} = (1.6 \times 10^{-19} \text{ C})(1 \text{ V}) = 1.6 \times 10^{-19} \text{ J}.$$

One eV is the right scale for atomic processes. The binding energy of hydrogen is 13.6 eV. Visible light photons carry 1.5 to 3 eV. The gap between energy levels in a molecule is a few tenths of an eV. The language of atomic and molecular physics is written in electron-volts.

<!-- → [TABLE: Side-by-side energy scales — column 1: process (hydrogen binding, visible photon, X-ray photon, nuclear fission, AED discharge, car battery), column 2: energy in joules, column 3: energy in eV; student should see that eV is convenient for atomic-scale events, joules for macroscopic] -->

---

## From potential to field: the derivative relation

Now here is the physical picture. Potential is a number that varies through space. The electric field is the *rate of change* of that number — it points in the direction potential decreases fastest, and its magnitude is how fast it decreases.

In one dimension:

$$E = -\frac{dV}{dx}.$$

In three dimensions, the field is the negative gradient of the potential: $\vec{E} = -\nabla V$.

For a uniform field — which is what you get between large parallel plates — this simplifies to

$$E = \frac{V}{d},$$

where $d$ is the separation between the plates. If you put 12 volts across plates 1 mm apart, the field between them is $12/0.001 = 12{,}000$ V/m. The same 12 volts across a 10 cm gap gives only 120 V/m. **Geometry concentrates potential into field.** This is not a coincidence — it is the whole engineering principle behind capacitors, transistor gates, and spark plugs.

For a single point charge $Q$, setting the reference potential to zero at infinity:

$$V = \frac{kQ}{r}.$$

Notice: potential drops as $1/r$, while field drops as $1/r^2$. They have to, because $E = -dV/dr$, and the derivative of $1/r$ is $-1/r^2$.

The superposition principle for potential is wonderfully simple: to find the potential due to many charges, add up the contributions from each as ordinary numbers:

$$V_\text{total} = \sum_i \frac{kQ_i}{r_i}.$$

No vectors. Just addition. This is the main reason we introduce potential at all.

<!-- → [TABLE: Comparison of electric field and electric potential for a point charge — columns: quantity, symbol, formula, how it depends on r, units, vector or scalar; rows: electric field E = kQ/r², potential V = kQ/r; student should see the 1/r vs 1/r² contrast and the scalar/vector distinction side by side] -->

---

## Equipotential surfaces

Imagine drawing all the points in space where $V = 100$ volts. They form a surface — an **equipotential surface**. On this surface, a charge can move freely with no work done by the electric field (since $\Delta V = 0$, $W = q\Delta V = 0$).

Two things follow immediately from the definition:

1. The electric field is *perpendicular* to every equipotential surface. If the field had a component along the surface, it would do work as a charge moved along it — but we just said it doesn't. Contradiction. So the field is purely perpendicular to equipotentials, everywhere.

2. The surface of any conductor in equilibrium is an equipotential. If it weren't, there would be potential differences along the surface, which would drive currents, which would mean it wasn't in equilibrium. Contradiction.

![For a point charge, V = kq/r falls as 1/r; |E| = kq/r² falls as 1/r². Both plotted vs r on the same axes. E is the slope of V: E = -dV/dr. One factor of r separates them.](../images/19-electric-potential-and-electric-field-fig-02.png)
*Figure 19.2 — V vs |E| for a Point Charge — One Power of r Differs*

![Four panels showing equipotential surfaces (lines of constant V) for canonical configurations: single point charge (concentric circles); dipole; two equal +q (saddle topology); parallel plates (evenly spaced straight lines)....](../images/19-electric-potential-and-electric-field-fig-03.png)
*Figure 19.3 — Equipotential Atlas — Concentric Rings, Dipole Curves, Two-+q Saddle, Parallel Lines*

![Three panels. Parallel plates: C = ε₀A/d. Coaxial cylinders (used in cables): C = 2πε₀L/ln(b/a). Concentric spheres: C = 4πε₀ ab/(b−a). All share the same dependence on permittivity and inverse on plate separation.](../images/19-electric-potential-and-electric-field-fig-05.png)
*Figure 19.5 — Three Capacitor Geometries — Parallel Plates, Coaxial, Concentric Spheres*

For a single positive point charge, equipotentials are concentric spheres. Between parallel plates, they are planes parallel to the plates. For a dipole — one positive, one negative charge — the equipotentials curve around both charges in a more complex pattern, always crossing the field lines at right angles.

<!-- → [INFOGRAPHIC: Three-panel diagram — (1) point charge with concentric spherical equipotentials and radial field lines; (2) parallel plates with planar equipotentials and uniform field lines; (3) dipole with curved equipotentials and curved field lines — all demonstrating perpendicularity at every crossing point] -->

Here is an important consequence for lightning rods. A conductor in equilibrium is an equipotential. The surface charge density adjusts to make this so. On a sphere, the charge distributes uniformly, and the field just outside is moderate. But near a sharp point, the surface curves tightly — the field just outside the point becomes very large. Air breaks down at about $3 \times 10^6$ V/m. A sharp rod reaches breakdown voltage at a much lower stored charge than a smooth surface, which is why lightning preferentially strikes pointed objects. Franklin's lightning rod works because it quietly drains the charge from a storm cloud before it accumulates enough to strike.

<!-- → [IMAGE: Close-up photograph or technical illustration of a lightning rod tip showing the sharp point geometry, with field lines crowding around the tip — caption should note that field concentration at a point is why breakdown occurs there first, and that the same geometry problem appears in MOSFET gate edges and high-voltage connector design] -->

---

## A calculation worth doing: ionizing hydrogen

The hydrogen atom is a proton with an electron orbiting at the Bohr radius: $r_0 = 5.29 \times 10^{-11}$ m.

What is the electric potential at the electron's location, due to the proton?

$$V = \frac{ke}{r_0} = \frac{(8.99 \times 10^9)(1.6 \times 10^{-19})}{5.29 \times 10^{-11}} = 27.2 \text{ V}.$$

The potential energy of the electron (charge $-e$) at this potential:

$$U = (-e)(27.2 \text{ V}) = -27.2 \text{ eV}.$$

Negative, which makes sense: the electron is bound; you have to do work to remove it.

To ionize the atom — to move the electron to infinity where $U = 0$ — you need to supply $+27.2$ eV. But wait: the electron isn't stationary. It's moving. In a circular orbit, the kinetic energy turns out to be exactly half the magnitude of the potential energy (this is the virial theorem, which holds for inverse-square force laws the same way it holds for planets). So the electron's kinetic energy is $+13.6$ eV.

Total energy of the atom: $-27.2 + 13.6 = -13.6$ eV.

To ionize, you need to raise the total energy from $-13.6$ eV to $0$. You need $+13.6$ eV.

**The ionization energy of hydrogen is 13.6 eV.** This is one of the most precisely measured numbers in all of physics. The fact that our straightforward calculation — just $V = kQ/r$ and the virial theorem — reproduces it is not a coincidence. It is confirmation that the Coulomb force law is correct, and that quantum mechanics' answer for the orbit radius is right.

A photon with 13.6 eV has wavelength 91 nm — the Lyman limit. Stars go dark at this wavelength because hydrogen in their atmospheres absorbs every photon capable of ionizing it. Astronomers observe this absorption edge in stellar spectra exactly where the calculation says it should be.

<!-- → [CHART: Energy level diagram for hydrogen — y-axis is energy in eV from -14 to 0, horizontal lines at -13.6 eV (n=1), -3.4 eV (n=2), -1.5 eV (n=3), etc., with arrows showing ionization and photon emission; student should see that 13.6 eV is the gap from ground state to continuum] -->

---

## Capacitors: storing energy in a field

Now we get to the device. A capacitor is two conductors separated by an insulator (or vacuum). Connect a battery across them: charge $+Q$ accumulates on one plate, $-Q$ on the other. An electric field builds up between the plates. That field stores energy.

The key relation is

$$Q = CV,$$

where $C$ is the **capacitance**, measured in farads (F), with $1 \text{ F} = 1 \text{ C/V}$. A farad is an enormous capacitance — the capacitors in your phone are measured in picofarads ($10^{-12}$ F) and nanofarads ($10^{-9}$ F).

For a parallel-plate capacitor with plate area $A$, separation $d$, and vacuum between:

$$C = \frac{\epsilon_0 A}{d},$$

where $\epsilon_0 = 8.85 \times 10^{-12}$ F/m is the permittivity of free space. Larger area catches more field lines; smaller separation means a stronger field for the same charge. Both increase capacitance.

If you fill the gap with an insulating material — a dielectric — with relative permittivity $\kappa$, the capacitance scales up:

$$C = \frac{\kappa \epsilon_0 A}{d}.$$

This is how commercial capacitors pack large capacitances into small volumes: ceramic dielectrics with $\kappa$ in the hundreds to thousands.

The energy stored in a charged capacitor is

$$U = \frac{1}{2}CV^2 = \frac{1}{2}\frac{Q^2}{C} = \frac{1}{2}QV.$$

The factor of one-half is not arbitrary. To charge a capacitor, you start with $V = 0$ and push charge onto the plates. As charge accumulates, the voltage rises — which means the next bit of charge has to be pushed against a higher and higher potential. The average voltage during charging is $V/2$, so the average energy cost per coulomb is $V/2$, and the total energy for $Q$ coulombs is $Q \cdot V/2 = \frac{1}{2}QV$.

<!-- → [CHART: Graph of voltage vs. charge during capacitor charging — linear from (0,0) to (Q,V); shaded triangle area below the line equals the stored energy U = ½QV; student should see why the factor of ½ arises geometrically] -->

---

## Where the energy lives

Here is the deep point, and it is easy to miss. The energy of a charged capacitor is not stored on the plates. The plates are just conductors — they hold charge, but charge by itself doesn't have much energy. The energy is stored *in the electric field between the plates* — in what looks, naively, like empty space.

We can make this precise. The energy density of an electric field — energy per unit volume — is

$$u = \frac{1}{2}\epsilon_0 E^2.$$

To derive it: take $U = \frac{1}{2}CV^2$, substitute $C = \epsilon_0 A/d$ and $V = Ed$, and divide by the volume of the gap $Ad$:

$$U = \frac{1}{2}\frac{\epsilon_0 A}{d}(Ed)^2 = \frac{1}{2}\epsilon_0 E^2 (Ad).$$

$$\frac{U}{Ad} = u = \frac{1}{2}\epsilon_0 E^2.$$

This formula holds not just for capacitors. It holds for the electric field of a point charge. It holds for the field of the Earth's surface charge. It holds for the field between a cloud and the ground before a lightning strike. Wherever there is an electric field in space, there is energy, at a density $\frac{1}{2}\epsilon_0 E^2$.

This is a profound shift in how to think about electromagnetism. In Newton's picture, energy lives in particles — in masses, in charges. In Faraday and Maxwell's picture, energy lives in fields. The field is not just a convenient bookkeeping device; it is a physical thing that stores energy, and that energy is real. We will push this idea further in Chapter 24, where electric and magnetic fields oscillate together and carry energy through empty space as light. But the seed is already here, in the charged capacitor: energy, stored in nothing but space with a field in it.

<!-- → [INFOGRAPHIC: Parallel-plate capacitor with the field lines drawn between plates; labels showing: (1) +Q on top plate, -Q on bottom plate; (2) field E between plates; (3) shaded region labeled "energy density u = ½ε₀E²"; caption: "The energy is in the field, not the charge — this idea carries all the way to electromagnetic waves"] -->

---

## The AED: putting it together

![Schematic of an automated external defibrillator: high-voltage battery charges a large capacitor; on trigger, capacitor discharges across the patient via paddles. Stored energy U = ½CV² = 200 J. Delivered in 1.5 ms means peak...](../images/19-electric-potential-and-electric-field-fig-01.png)
*Figure 19.1 — AED Defibrillator — 200 J Stored, Delivered in 1.5 ms = 133 kW Peak*

Return to the defibrillator from the chapter opening. An AED stores about 200 joules and delivers it to a stopped heart. The capacitor is charged to roughly 2,000 volts.

Capacitance from stored energy:

$$C = \frac{2U}{V^2} = \frac{2(200)}{(2000)^2} = \frac{400}{4 \times 10^6} = 10^{-4} \text{ F} = 100 \text{ μF}.$$

Charge stored:

$$Q = CV = (10^{-4})(2000) = 0.2 \text{ C}.$$

Average current during a 1.5 ms discharge:

$$I = \frac{Q}{t} = \frac{0.2}{0.0015} \approx 133 \text{ A}.$$

Field inside the dielectric, assuming a 100 μm thick film:

$$E = \frac{V}{d} = \frac{2000}{10^{-4}} = 2 \times 10^7 \text{ V/m}.$$

![A dielectric slab inserted between capacitor plates polarizes: bound surface charges on top (− next to + plate) and bottom (+ next to − plate). These bound charges partially cancel the free-charge field. Net E inside is...](../images/19-electric-potential-and-electric-field-fig-06.png)
*Figure 19.6 — Dielectric in a Capacitor — Bound Charges Reduce the Internal Field*

The breakdown field of polypropylene film (a common capacitor dielectric) is around $10^8$ V/m, so this design has a safety margin of five times. Good engineering: you don't want your capacitor arcing over inside someone's chest.

The energy density in the dielectric ($\kappa \approx 2$ for polypropylene):

$$u = \frac{1}{2}\kappa\epsilon_0 E^2 = \frac{1}{2}(2)(8.85 \times 10^{-12})(2 \times 10^7)^2 \approx 3{,}540 \text{ J/m}^3.$$

Volume of dielectric needed for 200 J:

$$\text{Vol} = \frac{200}{3540} \approx 0.057 \text{ m}^3.$$

That's 57 liters — obviously too large for a portable device. Real AEDs use higher-$\kappa$ dielectrics (electrolytic or ceramic) to shrink the volume by a factor of hundreds. This is what capacitor engineering actually is: finding materials with higher $\kappa$ and higher breakdown voltage, so you can store the same energy in a smaller box.

Scale that box down by twelve orders of magnitude in capacitance. You're now looking at the gate capacitor of a transistor in a 3 nm semiconductor process: femtofarads of capacitance, picojoules of stored energy, charged and discharged billions of times per second. Same equations. Same physics. Different engineering constraints. The capacitor in an AED and the gate of a transistor in your phone are the same device in two different size regimes.

<!-- → [TABLE: Capacitor comparison across scales — columns: device, capacitance, operating voltage, stored energy, dielectric, approximate physical size; rows: AED capacitor (~100 μF, 2 kV, 200 J), camera flash capacitor (~100 μF, 300 V, 4.5 J), electrolytic bypass cap (~1000 μF, 16 V, 0.13 J), ceramic chip cap (~100 nF, 10 V, 5 nJ), MOSFET gate (~1 fF, 1 V, 0.5 aJ); student should see 15 orders of magnitude in capacitance, same governing equations throughout] -->

---

## Three commitments

**Potential is energy per charge.** $V = U/q$, units J/C = V. Differences in potential drive charge flow; energy gained is $q\Delta V$. The electron-volt is the natural energy unit at atomic scales.

**Potential and field are linked.** $E = -dV/dx$ in general; $E = V/d$ for parallel plates; $V = kQ/r$ for point charges. Equipotential surfaces are perpendicular to field lines. The conductor surface is always an equipotential.

**Capacitors store energy in fields.** $C = \epsilon_0 A/d$; $U = \frac{1}{2}CV^2$. The energy density in the field is $\frac{1}{2}\epsilon_0 E^2$. This energy is as real as kinetic energy — and in Chapter 24, it will travel.

The one idea that matters most here: **the energy in a charged capacitor lives in the electric field between the plates.** Fields carry energy. That is not a metaphor.

---

## Exercises

### Warm-up

**19.1** *(Potential as energy per charge)* A point in a circuit is at $V = 12$ V. A charge of $+3$ μC sits at that point. What is its electric potential energy in joules?

**19.2** *(Work done by a field)* An electron moves from a point at $V = 0$ V to a point at $V = 50$ V. Does the electric field do positive or negative work on the electron? Compute the magnitude of the work in joules and in eV.

**19.3** *(Parallel-plate field)* Two parallel plates are separated by 2 mm and held at a potential difference of 240 V. What is the electric field strength between them? In which direction does it point — from high potential to low, or low to high?

**19.4** *(Capacitor charge and energy)* A 47 μF capacitor is charged to 9 V. Find (a) the charge stored, and (b) the energy stored.

### Application

**19.5** *(Point-charge potential)* A proton ($q = +1.6 \times 10^{-19}$ C) sits at the origin. (a) Compute the electric potential at $r = 0.10$ nm — roughly the scale of a chemical bond. (b) How much work would you need to do to move a second proton from infinity to this distance?

**19.6** *(Superposition of potentials)* Two charges, $+2$ μC at $x = 0$ and $-2$ μC at $x = 4$ cm, sit on the x-axis. Find the electric potential at the midpoint $x = 2$ cm. Then find the electric field at the midpoint. Explain why these two answers have different characters — one zero, one not.

**19.7** *(Parallel-plate capacitor geometry)* A parallel-plate capacitor has square plates of side 8 cm, separated by 1.5 mm of air. (a) Compute the capacitance. (b) If charged to 100 V, how much energy is stored? (c) What is the energy density in the field between the plates?

**19.8** *(Equipotentials and conductors)* A metal sphere of radius 5 cm carries charge $Q = +10$ nC. (a) What is the potential at its surface? (b) What is the potential at a distance of 20 cm from its center? (c) Sketch the equipotential surfaces. At what radius is $V = 500$ V?

### Synthesis

**19.9** *(Accelerating electrons — CRT physics)* An electron starts from rest and is accelerated through a potential difference of 10 kV, the kind used in old CRT displays. (a) What kinetic energy does it gain, in joules and in eV? (b) What speed does it reach? (c) Is a relativistic correction needed? (The rest-mass energy of an electron is $511$ keV — compare.)

**19.10** *(Capacitor engineering)* You need to store 1 J of energy in a capacitor that fits in a cube 2 cm on a side, charged to no more than 100 V. (a) What minimum capacitance is required? (b) If you use a parallel-plate geometry with a dielectric of $\kappa = 500$ (a high-$\kappa$ ceramic), what plate separation is needed to achieve this capacitance with plates of area $(2 \text{ cm})^2$? (c) Check whether the field in the dielectric exceeds a typical ceramic breakdown field of $10^7$ V/m.

**19.11** *(Neuron membrane as a capacitor)* A neuron's cell membrane is about 7 nm thick, has relative permittivity $\kappa \approx 7$, and a patch of membrane has area $\approx 1$ μm². (a) Estimate the capacitance of that patch. (b) The resting potential across the membrane is about 70 mV. How much charge is stored? (c) How many monovalent ions (charge $e$) does this correspond to? Does the number surprise you?

### Challenge

**19.12** *(Energy stored in the field of the Earth)* The Earth's surface carries a surface charge density of about $-1$ nC/m², producing a downward electric field at the surface of roughly 100 V/m. (a) Estimate the total energy stored in the electric field of the Earth, integrating the energy density $u = \frac{1}{2}\epsilon_0 E^2$ from the surface to an altitude of 50 km (the approximate top of the fair-weather atmosphere, where the field drops to near zero). You may assume the field decreases linearly with altitude for this estimate. (b) How does this compare to the energy released by a large thunderstorm (~$10^{14}$ J)?

**19.13** *(Single-electron capacitance)* In a single-electron transistor — a nanoscale device used in quantum computing research — the "island" of metal is so small that adding *one* electron raises its potential by a measurable amount. (a) If one electron raises the island's potential by 25 mV, what is the island's capacitance? (b) A commercial 100 pF capacitor requires how many more electrons to raise its potential by the same 25 mV? (c) Explain in one sentence why classical capacitor design, which assumes charge is continuous, breaks down at the single-electron scale.

---

## Still puzzling

The deepest question this chapter raises but doesn't fully answer: *what is the electric field, really?* We've said it stores energy. We've said it propagates as light. We can calculate everything it does with extraordinary precision. But whether the field is a substance — something that actually exists in empty space — or a mathematical bookkeeping device that happens to work perfectly, is a question that stretches from Maxwell's ether into the vacuum fluctuations of quantum field theory. Physics gives us the machinery. The ontology stays open.

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

## Connections forward

Chapter 20 introduces electric current and Ohm's law: $V = IR$. Chapter 21 builds circuits. Chapter 23 shows that changing magnetic fields generate voltages — the physics of generators and transformers. Chapter 24 reveals that the energy stored in oscillating electric and magnetic fields propagates through space at speed $c$. The volt you defined here, the energy density you computed here, will be in every equation of those chapters.

---

**Tags:** electric-potential, voltage, capacitance, capacitors, energy-storage, Feynman-style
