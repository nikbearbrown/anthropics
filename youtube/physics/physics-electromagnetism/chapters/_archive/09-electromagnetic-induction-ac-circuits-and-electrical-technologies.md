# Chapter 9 — Electromagnetic Induction, AC Circuits, and Electrical Technologies

**Suggested titles**

1. Electromagnetic Induction, AC Circuits, and Electrical Technologies
2. Faraday's Law and Why a Bicycle Dynamo Lights a Lamp
3. The Hidden Symmetry: Changing Magnetic Fields Make Electric Fields

**TL;DR.** A changing magnetic flux through a loop induces an EMF (voltage) in that loop — Faraday's law: $\varepsilon = -d\Phi_B/dt$. Lenz's law sets the sign: induced currents oppose the change that produced them. This single principle underpins every electric generator, every transformer, every induction motor, every wireless charger, and every modern electrical grid. AC circuits with inductors and capacitors have their own arithmetic of impedance and phase. By the end you can compute induced voltages, transformer ratios, and basic AC circuit responses, and you understand why the electrical grid runs on AC at 60 Hz (or 50 Hz).

---

## A bicycle dynamo on a Berlin street, 1895

In the 1890s, German cyclists started attaching small dynamos to their bicycles — friction wheels that pressed against the spinning tire and turned a small generator inside, lighting a lamp on the handlebars. Pedal faster, the dynamo spins faster, the lamp glows brighter. Stop pedaling, the lamp dims and goes out.

The hardware is laughably simple — a magnet inside a coil, mounted so the wheel's friction spins one or the other. But the physics is one of the most consequential discoveries in human history. Michael Faraday established it in 1831, in a London laboratory, by pushing a bar magnet through a coil of wire and watching a galvanometer needle deflect. *Moving a magnet near a coil produces a current.* No battery. No external power. The kinetic energy of the magnet becomes electrical energy in the coil, mediated by changing magnetic flux.

Faraday's discovery is the inverse of Ørsted's (1820, Chapter 22): Ørsted found that *currents create magnetic fields*; Faraday found that *changing magnetic fields create currents*. Together, the two effects close the loop — and that closed loop, mathematically, predicts that electric and magnetic fields propagate together as waves at the speed of light. The discovery of light as an electromagnetic wave (Maxwell, 1865) is downstream of Faraday's bicycle-dynamo physics.

Closer to home: every power plant on Earth (except direct solar PV) is a Faraday dynamo at scale. Steam turbines spin coils through magnetic fields. Wind turbines spin coils through magnetic fields. Hydroelectric dams spin coils through magnetic fields. Even nuclear reactors — they boil water, the steam spins a turbine, the turbine spins a generator coil. The whole electrical grid runs on Faraday's 1831 discovery.

**Learning objectives.** By the end of this chapter you should be able to:

1. State Faraday's law: $\varepsilon = -d\Phi_B/dt$, with $\Phi_B = \int \vec{B} \cdot d\vec{A}$.
2. Apply Lenz's law to determine the direction of induced currents.
3. Compute the EMF from a moving conductor in a uniform field: $\varepsilon = BLv$.
4. Compute the EMF from a rotating coil (generator): $\varepsilon = NAB\omega \sin(\omega t)$.
5. Compute the turns ratio and voltage transformation in a transformer: $V_s/V_p = N_s/N_p$.
6. Compute inductance and the energy stored in an inductor: $U = \frac{1}{2}LI^2$.
7. Identify the role of inductors and capacitors in AC circuits: reactance, impedance, RLC resonance.
8. Reason about the operation of electrical safety devices and the structure of the modern power grid.

**Prerequisites.** Chapter 19 (capacitors), Chapter 20 (current, power), Chapter 21 (RC circuits), Chapter 22 (magnetic fields, Lorentz force).

**Why this chapter matters.** Every household appliance you plug into the wall, every wireless charger, every car alternator, every guitar pickup, every stove-top induction cooktop, every MRI gradient coil, every credit-card swipe reader — all use electromagnetic induction. This is the chapter that explains why "wall power" exists in the form it does and what it does in the device.

---

## Concept 1 — Faraday's law and Lenz's law

### A magnet, a coil, and a galvanometer needle, October 1831

In October 1831, Michael Faraday — by then 40 years old and already famous for his work on electrochemistry and field theory — connected a coil of wire to a galvanometer (a sensitive current detector) and held a bar magnet near the coil. Galvanometer reads zero. Held still, no effect.

Then he *pushed the magnet into the coil*. The needle jumped. He pulled it back out. The needle jumped the other way. He held it still inside the coil. Zero again.

The effect was real, repeatable, and depended on *change*. A static magnet, no matter how strong, produced no current. A *changing* magnetic field through the coil produced a current. The faster the change, the larger the current. Faraday wrote the result up immediately and published it in early 1832 — and electromagnetic induction was born.

Faraday's verbal description of what he was seeing — the *number of magnetic field lines passing through the loop changing with time* — became Maxwell's mathematics a generation later, but it was correct. The number of field lines through a loop is what we now call **magnetic flux**, $\Phi_B$. Faraday's law is the precise statement of his observation:

$$\varepsilon = -\frac{d\Phi_B}{dt}.$$

The induced EMF (voltage) equals the negative rate of change of magnetic flux through the loop.

### The mechanism — flux and Lenz's law

**Magnetic flux** $\Phi_B$ through a surface is defined by

$$\Phi_B = \int \vec{B} \cdot d\vec{A},$$

with units **webers** (Wb), where 1 Wb = 1 T·m². For a uniform field perpendicular to a flat loop of area $A$, simply $\Phi_B = BA$. If the field is tilted by angle $\theta$ from the loop's normal, $\Phi_B = BA\cos\theta$.

The flux can change because:

- $B$ changes (a moving or oscillating magnet, an AC current in a nearby coil).
- $A$ changes (the loop is stretched, compressed, or rotated out of the field).
- $\theta$ changes (the loop rotates relative to the field).

Any of these produces a nonzero $d\Phi_B/dt$ and therefore an EMF.

**Lenz's law** specifies the sign — and physically, the direction — of the induced current. *The induced current flows in whichever direction creates a magnetic field that opposes the change in flux that produced it.*

Push a north pole of a magnet toward a coil: the coil sees increasing flux into itself, and the induced current flows in the direction whose own magnetic field points back outward (opposing the increase). The coil, in effect, presents its own north pole to repel the incoming magnet. You feel a force resisting the motion — you have to do *work* to push the magnet in. That work becomes the electrical energy in the coil.

This is energy conservation in action. If the induced current didn't oppose the change, the magnet would accelerate freely into the coil while the coil produced electrical energy — perpetual motion. Lenz's law forbids this.

### The trade-off

Faraday's law trades **physical specificity for sweeping universality.** It applies to any loop, any field, any geometry of change. It does not tell you how the current is distributed, how the loop's resistance shapes the current, how the geometry of the field affects the magnitude — those are engineering details. The law itself is a single, exact relationship between EMF and rate of flux change.

### Worked example — bar magnet through coil

A bar magnet with surface field 0.5 T (perpendicular to the magnet's pole face) is pushed through a 100-turn coil of area $5 \times 10^{-4}$ m² in 0.1 s. Estimate the average induced EMF.

**Reasoning.** Initially the magnet is far from the coil; flux ≈ 0. With the magnet inside (assume its full pole face passes through), flux per turn $\approx B \cdot A = (0.5)(5 \times 10^{-4}) = 2.5 \times 10^{-4}$ Wb. Total flux linkage (with $N = 100$ turns): $N\Phi_B = 0.025$ Wb-turns.

Average EMF: $\varepsilon_\text{avg} = \Delta(N\Phi_B)/\Delta t = 0.025/0.1 = 0.25$ V.

A quarter of a volt. Modest but measurable — this is roughly the regime of a good galvanometer demonstration.

**Sanity check.** Real bicycle dynamos generate 6 V at moderate speed for a 3-watt headlight bulb (need to deliver 0.5 A through 12 Ω). That requires more turns, faster motion, higher field. The orders of magnitude work out.

### Common misconceptions

- *"A static magnetic field produces an EMF in a coil at rest."* No — the field must be *changing*, or the coil must be *moving* (so the flux through it changes). A static magnet next to a static coil produces nothing.
- *"Faraday's law and Ohm's law are the same kind of statement."* No. Ohm's law is about a single component; Faraday's law is a fundamental field equation. Ohm's law has exceptions (semiconductors); Faraday's law is exact.
- *"Lenz's law is a separate principle from energy conservation."* It *is* energy conservation, expressed in electromagnetic language. They cannot disagree.

↳ **Dig Deeper — Why eddy currents brake without contact**

*A conducting plate moving through a magnetic field develops circulating currents (eddy currents) that, by Lenz's law, oppose its motion. This is the principle behind regenerative braking in electric vehicles, the smooth braking of roller-coasters, and the resistance you feel when waving a sheet of aluminum near a strong magnet.*

**Prompt:**
> Explain how eddy-current braking works. Walk me through the geometry: a conducting plate (e.g., aluminum) moving through a region of magnetic field perpendicular to the plate's motion. Show how the changing flux through different parts of the plate induces circulating currents (eddies), and how those currents — in the field — feel a Lorentz force that opposes the plate's motion. Connect this to (a) regenerative braking in electric vehicles (EMF in the motor coils when the vehicle decelerates), (b) the smooth braking on amusement-park free-fall rides, (c) why a metal pan won't sit still on an induction cooktop. End with one sentence on why eddy current braking is contactless and wears nothing out — the great advantage over friction brakes.

**What to do with the output:** Save it. Eddy current physics is one of the most useful engineering applications of Faraday's law.

---

## Concept 2 — Generators and motional EMF

### Faraday's disk generator, 1831

In the same year (1831) as his coil-and-magnet experiments, Faraday built the first electrical generator: a copper disk rotating between the poles of a horseshoe magnet. As the disk rotated, charges in it moved through the magnetic field; the Lorentz force on the moving charges pushed them outward (or inward, depending on rotation direction). Connecting brushes to the rim and the axle, Faraday extracted a steady DC current.

This was the first **electrical generator** — converting mechanical rotation to electrical current. Modern generators have refined the geometry (rotating coils between fixed magnets, or rotating magnets inside fixed coils, with iron cores to focus the flux), but the principle is identical. Mechanical work in, electrical work out, mediated by Faraday's law.

### The mechanism — motional EMF

Consider a straight rod of length $L$ moving with velocity $v$ perpendicular to a magnetic field $B$ (and perpendicular to its own length). Each electron in the rod feels a Lorentz force $F = ev \times B = evB$ along the rod. This force drives charges to one end of the rod, building up a potential difference until the buildup balances the Lorentz force:

$$\varepsilon = BLv.$$

This is **motional EMF**. The rod acts like a battery with EMF $BLv$, with no battery chemistry — just a magnet, a moving conductor, and the Lorentz force.

If the rod is part of a closed loop (e.g., the rod sliding along two parallel rails connected at one end), the EMF drives a current $I = BLv/R$ through the loop, where $R$ is the loop's total resistance. The current carrying through field experiences a Lorentz force that opposes the motion of the rod (Lenz's law again) — so you have to push the rod against this force, doing work that becomes the electrical energy in the loop.

### Generator EMF — rotating coil

A coil rotating in a uniform magnetic field has flux

$$\Phi_B = NBA\cos(\omega t),$$

where $N$ is the number of turns, $A$ is the coil area, $B$ is the field magnitude, and $\omega$ is the angular frequency of rotation. Faraday's law gives

$$\varepsilon(t) = -\frac{d\Phi_B}{dt} = NAB\omega \sin(\omega t).$$

This is sinusoidal AC voltage, with peak value $\varepsilon_0 = NAB\omega$. A generator running at 60 Hz angular frequency $\omega = 2\pi \times 60 \approx 377$ rad/s produces 60 Hz AC.

This is why the world's electrical grid runs at 50 or 60 Hz: those frequencies are convenient mechanical rotation speeds for steam turbines (3,600 rpm = 60 Hz with two-pole generators; 3,000 rpm = 50 Hz; sub-multiples for multi-pole machines). The choice of frequency was made early in the 20th century and locked in by the installed base.

### The trade-off

Generators trade **direct mechanical power for AC electrical convenience.** A generator produces sinusoidal AC by virtue of its rotational geometry. Direct-current generators require a commutator (mechanical switch) that wears out and produces sparks. Modern utility-scale generators produce three-phase AC, which is more efficient to transmit and easier to convert to mechanical work in motors.

### Worked example — bicycle dynamo output

A bicycle dynamo has a coil with 200 turns, area $2 \times 10^{-4}$ m², in a field of 0.3 T, rotating at 1500 rpm.

**Step 1 — Angular frequency.** $\omega = 2\pi (1500/60) = 2\pi (25) \approx 157$ rad/s.

**Step 2 — Peak EMF.** $\varepsilon_0 = NAB\omega = (200)(2 \times 10^{-4})(0.3)(157) \approx 1.88$ V. RMS = peak/$\sqrt{2}$ ≈ 1.33 V.

That seems low for a 6-V bike light. Real bike dynamos use higher fields, more turns, and step up via the bike-light driver electronics. Our calculation is the right order of magnitude for a bare unloaded coil.

**Sanity check.** Pedal harder → faster rotation → higher $\omega$ → higher EMF → brighter bulb. Stop pedaling → $\omega = 0$ → no EMF → no light. The formula matches direct experience.

### Common misconceptions

- *"A motor and a generator are different devices."* They are the same hardware, run in opposite directions. Apply voltage and the rotor turns (motor); turn the rotor and a voltage appears (generator). Modern hybrid car alternators do both.
- *"DC generators don't use Faraday's law."* They do — but use a commutator (mechanical switch) to flip the polarity each half-rotation, producing pulsed DC instead of AC.
- *"Faster rotation always means more power."* More EMF, yes. More power requires more current too, which depends on the load. A generator spinning at twice the speed into the same load delivers four times the power; into an open circuit, no power despite higher voltage.

↳ **Dig Deeper — How a transformer steps voltage up or down**

*A transformer is two coils wound around a common iron core. Apply AC to one (the primary); the changing magnetic flux passes through the iron to the other (the secondary), inducing an AC voltage. The voltage ratio is the turns ratio: $V_s/V_p = N_s/N_p$. This is the technology that makes the electrical grid possible — high-voltage transmission, low-voltage distribution.*

**Prompt:**
> Explain how a transformer steps AC voltage up or down. Walk me through the physics: an AC current in the primary coil produces a changing magnetic flux in the iron core; the same flux passes through the secondary coil; Faraday's law gives the secondary EMF as $\varepsilon_s = N_s d\Phi/dt$, while the primary's back-EMF (which equals the applied voltage in an ideal transformer) is $\varepsilon_p = N_p d\Phi/dt$. The ratio is the turns ratio. Then explain power conservation: in an ideal transformer, $V_p I_p = V_s I_s$, so stepping voltage up steps current down. End with one sentence on why this is exactly what's needed for long-distance power transmission (high V to reduce $I^2R$ losses, then step back down at the customer end).

**What to do with the output:** Save it. The transformer is one of the most consequential inventions in human history; the electrical grid would not exist without it.

---

## Concept 3 — Inductors, AC circuits, and the grid

### A neon sign and a starter ballast

In an old neon sign or fluorescent tube, the gas inside doesn't conduct electricity until you apply a high-voltage spike to ionize it. Once ionized, it conducts well — too well, in fact; the resistance drops nearly to zero, and without something to limit the current, the tube would burn out instantly.

The trick: an **inductor** in series. An inductor is a coil of wire that resists changes in current — passing DC freely, but presenting a frequency-dependent "reactance" to AC. When the gas first ionizes and current spikes, the inductor's back-EMF holds the current in check. After the transient settles, the inductor passes the steady AC operating current with little voltage drop. This is the "ballast" inside every old fluorescent fixture (modern LEDs don't need it).

The same physics — coils that resist change in current — is the heart of every transformer, every wireless charger, every audio crossover network in your speakers. Inductors are the third basic circuit element after resistors and capacitors, and the chapter closes with what they do.

### The mechanism — inductance

An **inductor** is any device whose EMF depends on the rate of change of current through it:

$$\varepsilon = -L \frac{dI}{dt},$$

where $L$ is the **inductance**, units **henries** (H), with $1 \text{ H} = 1 \text{ V} \cdot \text{s/A}$.

The negative sign is Lenz's law — the inductor "fights" changes in the current. A 1-H inductor with current changing at 1 A/s produces 1 V of opposing EMF.

For a long solenoid of $N$ turns, length $\ell$, cross-section $A$:

$$L = \frac{\mu_0 N^2 A}{\ell}.$$

Practical inductors range from nanohenries (ferrite-bead RF chokes) to henries (large power-supply chokes).

The energy stored in an inductor is

$$U = \frac{1}{2} L I^2.$$

This energy lives in the magnetic field inside (and around) the coil — the magnetic analog of the electric energy stored in a capacitor's field.

### AC circuit elements — reactance and impedance

In an AC circuit at frequency $\omega = 2\pi f$:

- **Resistor:** $V_R$ in phase with $I$; "resistance" $R$.
- **Inductor:** $V_L$ leads $I$ by 90°; "inductive reactance" $X_L = \omega L$.
- **Capacitor:** $V_C$ lags $I$ by 90°; "capacitive reactance" $X_C = 1/(\omega C)$.

For a series RLC circuit driven at angular frequency $\omega$, the total impedance is

$$Z = \sqrt{R^2 + (X_L - X_C)^2}.$$

The current is $I = V/Z$. Notice the inductive and capacitive reactances *subtract* — they are 180° out of phase with each other. At one specific frequency they cancel exactly:

$$\omega_0 = \frac{1}{\sqrt{LC}},$$

the **resonant frequency** of the circuit. At resonance, $Z = R$ (smallest possible), current is maximum for a given driving voltage. This is how radio receivers tune to specific stations: an LC circuit resonant at the station's frequency picks out that signal from the chaos of all radio waves bombarding the antenna.

### The trade-off

AC circuit analysis trades **DC simplicity for frequency-dependent complexity.** AC introduces phase relationships, reactance, complex impedance — concepts not present in DC. The reward: you can transmit power efficiently over long distances, design filters and resonant circuits, and access the entire engineering tradition of signal processing.

### The electrical grid

Every commercial power plant in the world (except solar PV and certain small generators) produces three-phase AC at 50 or 60 Hz via Faraday-law generators. The voltage is then stepped up by transformers to hundreds of kilovolts for long-distance transmission, stepped back down at substations to 7–35 kV for local distribution, and stepped down again at neighborhood transformers to 240 V or 120 V for customers.

The grid is enormous — the eastern North American interconnection covers over a million square miles, with all generators synchronized to the same 60 Hz frequency. The synchronization is accomplished by Lenz's law: any generator that drifts off frequency feels a torque pushing it back into sync.

Wireless chargers, induction cooktops, MRI gradient coils, electric guitar pickups, RFID readers — all are applications of changing magnetic flux producing voltage in a nearby coil. Faraday's 1831 discovery is everywhere.

### Worked example — transformer for a phone charger

A phone charger plugs into 120 V AC and delivers 5 V DC at 2 A. Inside is a step-down transformer, then a rectifier and filter (we ignore those here). The transformer's primary has 1000 turns. (a) How many turns does the secondary have? (b) What is the primary current (assuming an ideal transformer)?

**(a)** $V_s/V_p = N_s/N_p \implies N_s = N_p (V_s/V_p) = 1000 \times (5/120) \approx 42$ turns.

**(b)** Power conservation: $V_p I_p = V_s I_s \implies I_p = (V_s I_s)/V_p = (5)(2)/120 \approx 0.083$ A = 83 mA.

The wall outlet sees a small current at 120 V; the phone sees a large current at 5 V. Same power ($\sim 10$ W) on both sides. This is why phone chargers warm up — even at 90%+ efficiency, the dissipated few percent of 10 W heats the charger.

**Sanity check.** Modern USB-C chargers use switching power supplies (faster, smaller, more efficient than 60 Hz transformers), but the underlying voltage-step logic is identical. Switching supplies use a small high-frequency transformer instead of a large 60-Hz one, leveraging the fact that transformer size scales inversely with frequency.

### Common misconceptions

- *"AC and DC are interchangeable for any application."* Not quite. Some loads (motors, transformers, wireless chargers) require AC. Others (electronics, batteries) require DC. Conversion has efficiency cost.
- *"Inductors block DC and pass AC."* Backwards. Inductors have *zero* reactance at DC ($X_L = \omega L = 0$ when $\omega = 0$) and increasing reactance at higher frequencies. They pass DC and resist high-frequency AC.
- *"Transformer turns ratio determines power output."* No — turns ratio determines voltage ratio. Power output is set by the load.

↳ **Dig Deeper — Why we use 60 Hz (and 50 Hz) instead of some other frequency**

*The choice of 60 Hz in North America (and 50 Hz in most of the world) was made in the late 19th century during the war of currents. The choice was not arbitrary, but was set by competing constraints: rotating machine speeds, transformer efficiency, lighting flicker, and infrastructure compatibility.*

**Prompt:**
> Explain why the world's electrical grids settled on 50 or 60 Hz rather than higher or lower frequencies. Walk through the trade-offs: (a) lighting flicker — incandescent and arc lamps below ~40 Hz visibly flicker; (b) transformer efficiency — higher frequency means smaller cores but more iron loss; (c) machine speeds — 60 Hz with 2-pole generators gives 3600 rpm, a convenient steam-turbine speed; (d) skin effect in transmission — higher frequency means current concentrates near conductor surface, raising effective resistance; (e) historical infrastructure — once a frequency is chosen, switching is enormously expensive. End with one sentence on the modern HVDC (high-voltage DC) trend and why specific applications (long undersea cables, asynchronous grid interconnects) are returning to DC where conversion losses can be tolerated.

**What to do with the output:** Save it. The 50/60 Hz story is a beautiful case study in how engineering constraints shape technology choices that then become locked in for generations.

---

## Synthesis — Faraday's law as the bridge

Step back. Three concepts:

1. **Faraday's law.** $\varepsilon = -d\Phi_B/dt$. Lenz's law gives the sign. Changing flux through a loop induces an EMF.

2. **Generators and motional EMF.** $\varepsilon = BLv$ for a moving conductor; $\varepsilon = NAB\omega \sin(\omega t)$ for a rotating coil. Mechanical → electrical.

3. **Inductors and AC circuits.** $\varepsilon = -L(dI/dt)$, $U = \frac{1}{2}LI^2$. AC circuits use reactance and impedance; LC circuits resonate at $\omega_0 = 1/\sqrt{LC}$. The grid runs on transformed AC.

The unifying picture: changing electric currents create magnetic fields (Chapter 22); changing magnetic fields create electric fields (this chapter, Faraday's law). Together — and crucially, with one extra term Maxwell added in 1865 — these laws form Maxwell's equations and predict that electric and magnetic fields can travel through empty space as **electromagnetic waves at speed $c$**. Light is the wave that carries the electric and magnetic fields when they couple through empty space.

### A worked example combining all three concepts — wireless charging a phone

A wireless phone charger uses inductive coupling: an AC current in a primary coil in the charging pad creates a changing magnetic flux that passes through a secondary coil in the phone. The phone's coil sees an induced EMF, which is then rectified and stored in the phone's battery.

**Setup.** Charger pad coil: 50 turns, area $5 \times 10^{-4}$ m², driven at 200 kHz with peak current 2 A.

**Step 1 — Field at the phone coil.** Treating the pad coil as a small solenoid, $B \approx \mu_0 NI/\ell$. With $\ell$ ≈ 1 cm: $B \approx (4\pi \times 10^{-7})(50)(2)/0.01 \approx 0.013$ T. (Real geometry is more complex; this is a back-of-envelope.)

**Step 2 — Flux through phone coil.** Phone coil also $\sim 50$ turns, area $\sim 5 \times 10^{-4}$ m². Flux per turn (assuming good coupling): $\Phi = BA \approx (0.013)(5 \times 10^{-4}) \approx 6.5 \times 10^{-6}$ Wb.

**Step 3 — Induced EMF.** Driving frequency 200 kHz means $\omega = 2\pi \times 2 \times 10^5 \approx 1.26 \times 10^6$ rad/s. Peak EMF in phone coil: $\varepsilon_0 = N \omega \Phi = (50)(1.26 \times 10^6)(6.5 \times 10^{-6}) \approx 410$ V.

That seems high — and in fact real wireless chargers carefully tune the system for safer voltages. The point of using high frequency (200 kHz instead of 60 Hz) is exactly that $\omega$ is in the EMF formula; higher $\omega$ means more EMF for the same flux. The system is efficient at this frequency because that's where the inductive coupling resonance is engineered.

**Step 4 — Power transfer.** Real wireless chargers deliver 5–15 W to the phone, with efficiency around 70–80%. The energy comes from the AC source through changing magnetic flux through empty space — no wires, no contacts.

**Scale shift.** Same physics, scaled up by $10^6$ in frequency: an MRI gradient coil switches at 1 kHz to image patient tissue. Same physics, scaled up by $10^{10}$: an FM radio antenna at 100 MHz radiates electromagnetic waves carried by changing fields through truly empty space (Ch 24). One law, three orders of magnitude apart, all from Faraday.

---

## Exercises

### Warm-up

**23.1** *(LO 1)* A 50-turn coil of area 0.020 m² is in a field that increases from 0 to 0.30 T in 0.10 s. Compute the average induced EMF.

**23.2** *(LO 3)* A 0.50 m long rod moves at 4.0 m/s perpendicular to a 0.20 T field. Compute the motional EMF.

**23.3** *(LO 5)* A transformer has 1000 primary turns and 50 secondary turns. Primary AC voltage is 240 V. Compute the secondary voltage.

**23.4** *(LO 6)* An inductor of 50 mH carries current 0.5 A. How much energy is stored?

### Application

**23.5** *(LO 1, 2)* A bar magnet is dropped through a vertical conducting tube. Describe what happens — does it fall freely, or does it slow? Explain in terms of induced currents and Lenz's law.

**23.6** *(LO 4)* A generator has a 200-turn rectangular coil 30 cm × 20 cm, rotating at 60 Hz in a 0.50 T field. Compute the peak EMF.

**23.7** *(LO 5)* A long-distance transmission line carries 1 GW at 500 kV. (a) Compute the current. (b) If the line resistance is 10 Ω, compute the power loss as heat. (c) Now repeat for the same power transmitted at 50 kV instead of 500 kV. By what factor does the loss change?

**23.8** *(LO 7)* A series RLC circuit has $R = 10$ Ω, $L = 100$ mH, $C = 10$ μF. (a) Compute the resonant frequency. (b) At resonance, what is the impedance? (c) For a 10 V driving voltage at resonance, what is the current?

### Synthesis

**23.9** *(LO 1, 2, 3)* A 0.50 m horizontal conducting bar moves at 5.0 m/s on horizontal rails through Earth's magnetic field (50 μT, vertical component). The rails are 0.30 m apart and connect to a resistor of 1.0 Ω. (a) Compute the EMF. (b) Compute the current. (c) What force resists the bar's motion? (d) What mechanical power must be supplied to keep it moving?

**23.10** *(LO 4, 5)* A 1 GW power plant generates 25 kV from its generator. The voltage is stepped up by a transformer for transmission, then stepped down to 240 V for customers. (a) Compute the turns ratio of each transformer. (b) Why is intermediate voltage (e.g., 7.2 kV at the neighborhood) used between the substation and the home transformer?

**23.11** *(LO 7, 8)* Draw the modern household electrical chain: 120 V wall outlet → phone charger → phone battery → phone circuit. Identify which components are AC, which DC, and where the conversions happen.

### Challenge

**23.12** *(LO 1, beyond)* An MRI gradient coil produces a magnetic field that varies from −30 mT/m to +30 mT/m, switching in 200 μs. The patient is 50 cm long. Estimate the EMF induced in a 0.5 m long, 0.05 m wide loop of conducting tissue (a piece of skin). Comment on whether this could induce currents large enough to be felt.

**23.13** *(LO 3, beyond)* A unipolar generator (a Faraday disk) of radius 10 cm rotates at 100 rpm in a uniform 1 T field perpendicular to the disk. Estimate the EMF between the rim and the axle. (Hint: the EMF is generated by the radial Lorentz force on charges in the rotating disk; integrate $\varepsilon = \int (v \times B) \cdot dr$ from axle to rim.)

---

## LLM Exercise — Chapter 23: Induction in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An induced-EMF or transformer-related calculation for one component of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 23 (Electromagnetic Induction), I want to identify ONE inductive component of my phenomenon.

Please:

1. Identify the inductive element. Examples:
   - Bike commute: bike dynamo lighting the headlight; regenerative brake on an e-bike.
   - Coffee maker: the relay coil that switches on the heating element.
   - Marathon: the small generator inside a self-powered watch (kinetic-energy harvester).
   - Espresso machine: the AC induction motor in the pump.
   - Basketball: the inductive sensor in some sports tracking equipment.

2. Estimate or compute:
   (a) The geometry: turns, area, field, frequency.
   (b) The induced EMF (V).
   (c) The current and power transferred.

3. State your inputs and uncertainty.

4. Identify whether the device works because of motion (motional EMF), changing field (transformer), or both.

5. Sanity check against published specs.

6. Connect to Chapter 24 (Electromagnetic Waves), where we'll see that changing fields propagate through empty space as light.

Save the output as logbook/chapter-23-induction.md.
```

### What this produces

Your twenty-third Logbook entry — an induction-related calculation.

### How to adapt this prompt

- *For phenomena with no obvious inductive element*: every appliance plugged into the wall passes through transformers. Pick the wall power chain.
- *For Claude Code:* If you have an oscilloscope trace of an AC waveform, fit it to extract amplitude, frequency, and phase, and analyze the impedance.

### Connection to previous chapters

Builds on Chapter 22's magnetic field and Chapter 21's circuits. The energy bookkeeping from Chapter 7 reappears (mechanical → electrical work).

### Preview of next chapter

Chapter 24 closes the EM arc: the discovery (Maxwell, 1865) that electric and magnetic fields can propagate together through empty space as waves at the speed of light. The Chapter 24 LLM Exercise will identify electromagnetic radiation in your phenomenon.

---

## Chapter summary

Electromagnetic induction is the law that completes the symmetry between electric and magnetic fields: changing flux makes EMF. Three commitments:

1. **Faraday's law.** $\varepsilon = -d\Phi_B/dt$. Any change in magnetic flux through a loop produces an EMF. Lenz's law sets the sign by energy conservation.

2. **Generators convert mechanical to electrical work.** $\varepsilon = BLv$ for a moving conductor; $\varepsilon = NAB\omega\sin(\omega t)$ for a rotating coil. The world's grid runs on rotating coils in fields, producing 50/60 Hz AC.

3. **Inductors and transformers run AC circuits and the grid.** Inductors resist current changes; transformers step voltage up or down via flux through a shared core. AC circuits use reactance and impedance; LC circuits resonate.

The one idea that matters most: **changing fields create voltages, and that fact runs the modern world.** Every power plant, every transformer, every motor, every wireless charger, every MRI scanner uses Faraday's law in some form.

The common mistake to watch for: **forgetting Lenz's law.** Induced currents always oppose the change that created them. If you get the wrong sign, the system would violate energy conservation.

---

## What would change my mind

The chapter argues that Faraday's law and the standard AC circuit machinery suffice for nearly all practical electromagnetic-induction problems at the introductory level. The argument would need revision if a class of routine engineering problems required full Maxwell's equations or relativistic field treatments. They don't, for any utility-grid or consumer-electronics application — those become important in radio antennas (Ch 24) and high-energy physics (Ch 28).

## Still puzzling

The deepest puzzle this chapter raises and prepares: *why are electric and magnetic fields linked at all?* Faraday's law (changing $B$ creates $E$) plus Maxwell's later addition (changing $E$ creates $B$) means that the two fields can sustain each other in empty space, propagating as a wave. The wave's speed turns out to be exactly $c$, the speed of light. This identification — light is an electromagnetic wave — is the most consequential prediction in 19th-century physics. Why the universe arranges its fundamental forces this way is a question that pushes into the foundational structure of physics itself.

---

## Connections forward

Chapter 24 unifies electric and magnetic fields into **electromagnetic waves** — light. The same equations that govern your wireless charger at 200 kHz govern visible light at $5 \times 10^{14}$ Hz, X-rays at $10^{18}$ Hz, and gamma rays beyond. Chapter 25 onward treats light as both a wave and (eventually, in Chapter 29) as a stream of photons. The closing of the EM loop in this chapter — Faraday completing what Ørsted started — is the bridge to all of optics, modern communications, and quantum electrodynamics.

---

**Tags:** electromagnetic-induction, Faradays-law, transformers, AC-circuits, generators

---

## AI Wayback Machine

**Nikola Tesla** developed the polyphase AC induction motor and AC power distribution in the 1880s — the technology that enabled modern electrification. His system displaced Edison's DC despite a fierce public-relations war.

**Run this:**

```
Who was Nikola Tesla, and how does his AC power work connect to electromagnetic induction we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Nikola Tesla"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain why AC, not DC, makes long-distance power transmission practical.
- Ask it about the mythologized Tesla figure vs. the historical record — what's true, what's overblown.

What changes? What gets better? What gets worse?
