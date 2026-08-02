# Chapter 23 — Electromagnetic Induction, AC Circuits, and Electrical Technologies

*Push a magnet through a coil of wire. Watch the needle jump. That's where the electrical grid came from.*

---

In October 1831, Michael Faraday connected a coil of wire to a galvanometer and held a bar magnet near it. The needle read zero. He pushed the magnet into the coil. The needle jumped. He pulled it back out. The needle jumped the other way. He held it still inside the coil. Zero again.

That is the whole discovery. A static magnet does nothing. A *changing* magnetic field through the coil produces a current. The faster the change, the larger the current.

Faraday published in early 1832. Within forty years, his observation had become the theory of light. Within sixty years, it had become the electrical grid. Every power plant on Earth — coal, gas, nuclear, wind, hydroelectric — converts the rotation of a turbine into electricity using Faraday's result. Even a nuclear reactor's role is to boil water, spin a turbine, and spin a coil in a magnetic field, doing what Faraday did in his London laboratory with a bar magnet and a galvanometer, scaled up by a billion.

Faraday's discovery is the inverse of Ørsted's (Chapter 22). Ørsted showed that *currents create magnetic fields*. Faraday showed that *changing magnetic fields create currents*. Together, the two effects close a loop. Mathematically, they imply that electric and magnetic fields can sustain each other through empty space — propagating as a wave at the speed of light. Maxwell worked this out in 1865. Light itself turns out to be an electromagnetic wave, and it follows from Faraday's needle jumping in 1831.

This chapter is about the needle jump and what comes from it.

---

## Faraday's law and Lenz's law

What Faraday observed — that the number of magnetic field lines through the loop changing with time produces a current — became, in Maxwell's hands, a precise mathematical statement:

$$\varepsilon = -\frac{d\Phi_B}{dt}.$$

The induced EMF (voltage) in any closed loop equals the negative rate of change of the magnetic flux through the loop.

**Magnetic flux** $\Phi_B$ is the measure of how much magnetic field is threading the loop:

$$\Phi_B = \int \vec{B} \cdot d\vec{A},$$

with units of **webers** (Wb), where $1 \text{ Wb} = 1 \text{ T}\cdot\text{m}^2$. For a uniform field $B$ perpendicular to a flat loop of area $A$: $\Phi_B = BA$. If the field makes angle $\theta$ with the loop's normal: $\Phi_B = BA\cos\theta$.

![Three panels showing the three independent ways Φ_B = B·A·cos θ can change. Left: magnet moves toward coil (B changes). Middle: coil deforms (A changes). Right: coil rotates in field (θ changes). All produce an EMF.](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-01.png)
*Figure 23.1 — Three Ways to Change Magnetic Flux — B, A, or θ*

The flux can change in three ways: the field strength $B$ can change; the area $A$ of the loop can change; or the angle $\theta$ between them can change. Any of these produces a nonzero $d\Phi_B/dt$ and therefore an EMF.

![Two scenarios. Allowed (Lenz): magnet pushed toward coil, induced current flows to oppose — its B field repels the magnet, requiring work. Forbidden (anti-Lenz): induced current attracts magnet, would create perpetual motion —...](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-02.png)
*Figure 23.2 — Lenz's Law — Induced Current Always Opposes the Flux Change*

The negative sign in Faraday's law is not a bookkeeping annoyance. It encodes a physical law: **Lenz's law**. The induced current flows in the direction that creates a magnetic field *opposing* the change in flux. Push a north pole into a coil — flux increases into the coil — and the induced current flows to create its own field pointing back out, opposing the increase. You feel resistance as you push. You are doing work against that resistance, and that work becomes electrical energy in the circuit.

This is energy conservation stated in electromagnetic language. If the induced current *aided* the change instead of opposing it, the magnet would accelerate into the coil while the coil produced electrical energy out of nothing — perpetual motion. Lenz's law is the universe saying no.

### The moving bar

![Conducting rod of length L slides at velocity v on parallel rails in uniform B (into page). Flux-rule derivation: ε = dΦ/dt = BLv. Lorentz-force derivation: free charges in rod feel qv × B, equivalent to E_motional = vB, EMF =...](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-03.png)
*Figure 23.3 — Motional EMF — Rod on Rails, Two Derivations Agree*

There is a concrete version of Faraday's law that shows the mechanics cleanly. A conducting rod of length $L$ moves with velocity $v$ perpendicular to a uniform magnetic field $B$ and perpendicular to its own length. Electrons in the rod feel a Lorentz force $F = evB$ along the rod's length — the same force from Chapter 22. They accumulate at one end until the electric field they build up balances the Lorentz force. The result is a potential difference — an EMF:

$$\varepsilon = BLv.$$

This is **motional EMF**. The rod acts like a battery whose terminal voltage is $BLv$, with no chemistry, no electrodes, just a magnet and a moving conductor.

If the rod slides along two parallel conducting rails connected at one end through a resistor $R$, the EMF drives current $I = BLv/R$ around the circuit. That current, in the magnetic field, feels a Lorentz force opposing the rod's motion (Lenz's law). You must push against this force to keep the rod moving. The mechanical work you do becomes electrical energy dissipated in the resistor. Faraday's law quantifies the exchange rate.

<!-- → [INFOGRAPHIC: motional EMF setup — a conducting rod of length L sliding rightward at velocity v on two parallel rails in a field B pointing out of the page; show the EMF = BLv driving current clockwise through the resistor R at the left end; label the Lorentz force on the rod pointing left (opposing motion), and annotate that the mechanical power input F·v equals the electrical power V²/R — student should see the energy bookkeeping made concrete] -->

---

## Generators: mechanical work becomes AC electricity

Faraday built the first electrical generator in the same year as the coil experiment. A copper disk rotating between the poles of a horseshoe magnet. Charges in the disk moved through the field; Lorentz forces pushed them radially; connecting brushes to the rim and axle extracted a steady current. First generator. No battery, no chemistry. Mechanical rotation, electrical output.

![Schematic of a rotating rectangular coil between magnetic poles. Coil rotates at angular speed ω; flux Φ = NBA cos(ωt). EMF ε = NBA ω sin(ωt) — pure sinusoid. Shown alongside the sinusoidal output waveform.](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-04.png)
*Figure 23.4 — AC Generator — Rotating Coil in B Field Produces ε(t) = NBAω sin(ωt)*

Modern generators refine the geometry: a coil rotates inside a magnetic field, or a magnet rotates inside a coil. Either way, the flux through the coil changes as it rotates. A coil with $N$ turns and area $A$ rotating at angular frequency $\omega$ in a field $B$ has flux

$$\Phi_B = NBA\cos(\omega t).$$

Faraday's law gives the induced EMF:

$$\varepsilon(t) = -\frac{d\Phi_B}{dt} = NAB\omega\sin(\omega t).$$

Sinusoidal AC voltage with peak value $\varepsilon_0 = NAB\omega$. A generator running at 60 rotations per second produces 60 Hz alternating current.

This is why the electrical grid runs at 50 or 60 Hz. Steam turbines at utility-scale power plants run efficiently at 3,000–3,600 rpm. A two-pole generator at 3,600 rpm produces $3{,}600/60 = 60$ cycles per second — 60 Hz. In countries where the grid settled at 50 Hz, turbines run at 3,000 rpm. The choice was made in the late nineteenth century, before AC had won the War of Currents, and it locked in permanently with the infrastructure. You cannot change the grid frequency without replacing every motor, transformer, and timing circuit in the country.

<!-- → [INFOGRAPHIC: cross-section of an AC generator — rotating rectangular coil between two magnetic poles; at four positions in the rotation (0°, 90°, 180°, 270°), show the coil orientation and the corresponding point on the sinusoidal output voltage curve below; label peak EMF = NABω at the 90° position where the coil plane is parallel to the field and flux is changing fastest; label zero EMF at 0° and 180° where flux is at maximum/minimum and changing slowest] -->

The peak EMF formula $\varepsilon_0 = NAB\omega$ tells you how to make a bigger generator: more turns, larger area, stronger field, or faster rotation. Power plants use all four. The rotating coil sits in a carefully engineered magnetic circuit with iron cores to concentrate the flux, water-cooled conductors to handle the heat from the currents, and bearings engineered to last decades at thousands of rpm.

A bicycle dynamo works on the same principle — a small magnet spinning inside a few hundred turns of wire, driven by friction against the tire. Peak EMF maybe 6 V at cruising speed. Exactly the voltage the headlight needs. Stop pedaling: rotation stops, $\omega = 0$, EMF = 0, light goes out. Faraday's law is the direct line from the formula to the experience.

---

## Transformers: the device that makes the grid possible

On September 4, 1882, Thomas Edison opened Pearl Street Station in Manhattan — the world's first commercial power plant. It supplied DC at 110 V to 80 customers within half a mile. The problem with DC at low voltage: power loss in the transmission line goes as $I^2R$. For fixed power delivered $P = IV$, lower voltage means higher current, means more $I^2R$ waste. Edison's stations had to be within a mile of their customers. The city would need thousands of local generators.

George Westinghouse and Nikola Tesla won the War of Currents by using alternating current and transformers. AC voltage can be stepped up for transmission and back down for use. The device that does the stepping is the **transformer**.

![Iron-core transformer with primary (N₁ turns, V₁) and secondary (N₂ turns, V₂). Mutual flux through both: V₂/V₁ = N₂/N₁ (turns ratio). Power conserved: V₁ I₁ = V₂ I₂ (ideal). Step-up doubles V, halves I.](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-05.png)
*Figure 23.5 — Transformer — Iron Core, Primary + Secondary, Turns Ratio Sets Voltage*

A transformer has two coils wound around a shared iron core. Apply AC to the primary coil ($N_p$ turns) and the changing current creates a changing magnetic flux in the core. Faraday's law says that flux change induces an EMF in any coil threaded by it — including the secondary coil ($N_s$ turns). Because both coils see the same rate of flux change through the same core:

$$\frac{V_s}{V_p} = \frac{N_s}{N_p}.$$

More turns on the secondary than the primary: higher voltage out. Fewer turns: lower voltage. Conservation of energy (for an ideal transformer) requires:

$$V_p I_p = V_s I_s.$$

Step voltage up by a factor of 10 and current drops by a factor of 10. The power is the same on both sides.

Now transmit 1 GW over a 200 km line with $R = 10 \Omega$. At 500 kV: $I = 2{,}000 \text{ A}$, line loss = $(2{,}000)^2 \times 10 = 40 \text{ MW}$ — about 4% of transmitted power. At 11 kV instead: $I = 90{,}900 \text{ A}$, line loss = $(90{,}900)^2 \times 10 \approx 82 \text{ GW}$ — eight times more than you're transmitting. Useless. High voltage is not a safety choice; it is a physics necessity.

The modern grid: generators at 15–25 kV → step up to 115–765 kV for long transmission → step down to 7–35 kV at substations → step down again to 120/240 V at neighborhood transformers. Every step uses a transformer. The transformer is the device that made the electrical grid possible, and Faraday's law is why transformers work.

---

## Inductors and AC circuits

An inductor — any coil of wire — has a property that flows directly from Faraday's law: it resists changes in current. When current through a coil changes, the flux through the coil changes, which induces an EMF opposing the change. Quantitatively:

$$\varepsilon = -L\frac{dI}{dt},$$

where $L$ is the **inductance**, in henries (H). A coil with current changing at 1 A/s induces 1 V of opposing EMF per henry of inductance. The energy stored in the magnetic field of an inductor carrying current $I$ is:

$$U = \frac{1}{2}LI^2.$$

The magnetic analog of $\frac{1}{2}CV^2$ for a capacitor. Energy in the electric field of a capacitor, energy in the magnetic field of an inductor.

In an AC circuit, inductors and capacitors present frequency-dependent resistance — **reactance**. For an inductor at angular frequency $\omega$:

$$X_L = \omega L.$$

For a capacitor:

$$X_C = \frac{1}{\omega C}.$$

Inductors resist high frequencies (reactance increases with $\omega$); capacitors resist low frequencies (reactance decreases with $\omega$). In a series RLC circuit, the total impedance is

$$Z = \sqrt{R^2 + (X_L - X_C)^2}.$$

The reactances subtract because inductors and capacitors are 180° out of phase. At the one frequency where $X_L = X_C$:

$$\omega_0 = \frac{1}{\sqrt{LC}},$$

the impedance reduces to just $R$, and current through the circuit is maximum. This is **resonance**. A radio receiver is a tunable RLC circuit. Adjusting the variable capacitor shifts $\omega_0$ to match the broadcast frequency you want to hear. At resonance, the current response from that frequency is maximum; all other frequencies see the full impedance $Z > R$ and are attenuated. The selectivity of a radio dial is the selectivity of an LC circuit at resonance.

<!-- → [CHART: impedance Z vs. frequency for a series RLC circuit — x-axis from 0.1ω₀ to 10ω₀ on a log scale, y-axis from R to 10R; the curve has a sharp minimum of Z = R at ω₀, rising steeply on both sides; show three curves for different Q factors (sharp resonance for high Q, broad for low Q) and annotate ω₀ = 1/√LC; student should see that the RLC circuit selects one frequency and rejects others, and that higher Q = sharper selectivity] -->

---

## Everything from one observation

Pull back to where we started: Faraday pushing a bar magnet through a coil, watching a galvanometer needle jump.

That needle jump is:

- Every electrical generator ever built (mechanical rotation → changing flux → EMF → current).
- Every transformer in the grid (AC current in primary → changing flux in core → EMF in secondary → stepped voltage).
- Every inductor in every AC circuit (current change → flux change → opposing EMF → reactance).
- Every wireless charger (AC current in pad coil → changing field → induced EMF in phone coil).
- Every induction cooktop (AC coil in the element → eddy currents in the iron pan → ohmic heating).
- Every regenerative brake in an electric car (coils decelerating through a field → opposing force → electrical energy back to the battery).
- Every MRI gradient coil. Every guitar pickup. Every electric motor run backward.

![Two panels. RC: τ_RC = RC, bigger R makes the circuit slower (longer to charge). RL: τ_RL = L/R, bigger R makes the circuit faster (current settles sooner). Mirror inversion in R.](../images/23-electromagnetic-induction-ac-circuits-and-electrical-technologies-fig-06.png)
*Figure 23.6 — RC vs RL — Two Time Constants, Opposite Dependence on R*

And, once Maxwell added the final missing term in 1865 — that changing *electric* fields also create magnetic fields — the electromagnetic wave is predicted. Set the wave speed equal to $1/\sqrt{\mu_0\epsilon_0}$, plug in the measured values of the constants, and the answer is $3 \times 10^8 \text{ m/s}$. The speed of light. Light is Faraday's needle jump, propagating through empty space at the speed allowed by the constants of nature.

The scale shift: Faraday's coil experiment happened at a few centimeters, a few volts, a few milliamps. The grid operates at thousands of kilometers, hundreds of kilovolts, thousands of amperes. An MRI gradient coil switches at 1 kHz and images millimeter-scale structures inside the human body. An FM antenna radiates at 100 MHz, and the wave that carries the radio program travels at the speed of light. One law, thirty orders of magnitude in frequency, everything from the bicycle dynamo to the structure of the observable universe.

---

## Exercises

### Warm-up

**23.1** *(LO 1)* A 50-turn coil of area $0.020 \text{ m}^2$ sits in a magnetic field that increases uniformly from $0$ to $0.40 \text{ T}$ in $0.080 \text{ s}$. (a) Compute the average induced EMF. (b) If the coil has resistance $5.0 \Omega$, what current flows?

**23.2** *(LO 3)* A conducting rod $0.60 \text{ m}$ long moves at $3.0 \text{ m/s}$ perpendicular to a $0.25 \text{ T}$ magnetic field. (a) Compute the motional EMF. (b) If the rod is part of a closed loop with total resistance $2.0 \Omega$, what current flows and what force opposes the rod's motion?

**23.3** *(LO 5)* A transformer has $N_p = 800$ turns and $N_s = 40$ turns. The primary is connected to 120 V AC. (a) What is the secondary voltage? (b) If the secondary delivers $3.0 \text{ A}$, what current flows in the primary (ideal transformer)?

**23.4** *(LO 6)* An inductor of $L = 80 \text{ mH}$ carries a steady current of $2.0 \text{ A}$. (a) How much energy is stored? (b) An LC circuit has $L = 80 \text{ mH}$ and $C = 5.0 \text{ μF}$. What is the resonant frequency?

### Application

**23.5** *(LO 1, 2)* A bar magnet is dropped down a vertical copper tube. (a) Explain in words, using Lenz's law, why the magnet falls slower than free fall. (b) Does the magnet ever reach terminal velocity inside the tube? What determines that speed? (c) Would the effect be stronger or weaker in a tube made of plastic? Explain.

**23.6** *(LO 4)* An AC generator has $N = 200$ turns, coil area $A = 0.030 \text{ m}^2$, field $B = 0.50 \text{ T}$, and rotates at $60 \text{ Hz}$. (a) Compute the peak EMF. (b) Compute the RMS voltage. (c) If connected to a $120 \Omega$ resistive load, what is the RMS current and average power delivered?

**23.7** *(LO 5)* A step-up transformer at a power plant output steps 25 kV up to 500 kV for transmission. (a) What is the turns ratio? (b) The plant generates 500 MW. Compute the current in the primary and secondary windings. (c) If the transmission line has resistance $8 \Omega$, what fraction of the transmitted power is lost as heat?

**23.8** *(LO 6, 7)* A series RLC circuit has $R = 20 \Omega$, $L = 0.10 \text{ H}$, $C = 50 \text{ μF}$, driven by $V_\text{RMS} = 120 \text{ V}$ AC. (a) Find the resonant frequency. (b) At resonance, find the impedance, current, and power. (c) At $f = 2f_0$, find $X_L$, $X_C$, $Z$, and compare the current to the resonant case.

### Synthesis

**23.9** *(LO 1, 3)* A square coil of side $0.20 \text{ m}$ and 100 turns moves at $2.0 \text{ m/s}$ out of a uniform $0.50 \text{ T}$ magnetic field region (the field fills only part of space). As the coil exits, one side of length $0.20 \text{ m}$ is still in the field. (a) Compute the motional EMF from that side. (b) If the coil has resistance $4.0 \Omega$, compute the current and the braking force on the coil. (c) What power is dissipated in the coil, and where does it come from?

**23.10** *(LO 4, 5)* A power plant produces electricity at 20 kV. The power is transmitted at 230 kV. (a) What is the step-up transformer turns ratio? (b) At the customer end, a second transformer steps from 230 kV to 240 V. What is that turns ratio? (c) A customer draws 10 kW. Trace the current through each part of the chain: through the generator, through the transmission line, through the neighborhood transformer primary, and through the customer's breaker panel.

**23.11** *(LO 6)* An FM radio receiver tunes to 100 MHz using a variable capacitor in an LC circuit. The inductor is $L = 0.30 \text{ μH}$. (a) What capacitance is needed for 100 MHz resonance? (b) To tune from 88 MHz to 108 MHz, over what range must the capacitance vary? (c) Sketch qualitatively how the impedance curve shifts as the capacitor is adjusted.

### Challenge

**23.12** *(LO 1, beyond chapter)* An MRI gradient coil switches its magnetic field gradient from $-30 \text{ mT/m}$ to $+30 \text{ mT/m}$ across a patient (50 cm extent) in $200 \text{ μs}$. (a) Estimate the average rate of change of $B$ at the patient's location. (b) Estimate the EMF induced in a conducting loop of area $\sim 0.05 \text{ m}^2$ (roughly the cross-section of a body segment). (c) Comment on whether this could cause sensations and why MRI safety protocols limit gradient switching rates.

**23.13** *(LO 3, 4, beyond chapter)* A rail gun accelerates a conductive projectile of mass $50 \text{ g}$ and length $L = 0.10 \text{ m}$ along rails $0.10 \text{ m}$ apart in a field $B = 2.0 \text{ T}$. A current of $10{,}000 \text{ A}$ flows through the projectile. (a) Compute the Lorentz force on the projectile. (b) If the rails are $1.0 \text{ m}$ long, what is the projectile's exit velocity (assuming constant force from rest)? (c) Compute the back-EMF when the projectile is moving at that exit velocity. What does this imply about the actual current during acceleration?

---



By the end of this chapter you should be able to:

1. State Faraday's law ($\varepsilon = -d\Phi_B/dt$) and apply it to compute induced EMFs from changing flux.
2. Apply Lenz's law to determine the direction of induced currents and explain why it enforces energy conservation.
3. Compute the motional EMF of a conductor moving in a field: $\varepsilon = BLv$.
4. Compute the EMF from a rotating coil (AC generator): $\varepsilon = NAB\omega\sin(\omega t)$.
5. Apply the transformer turns ratio and power conservation: $V_s/V_p = N_s/N_p$, $V_pI_p = V_sI_s$.
6. Compute energy stored in an inductor ($U = \frac{1}{2}LI^2$) and the resonant frequency of an LC circuit ($\omega_0 = 1/\sqrt{LC}$).
7. Explain why the electrical grid uses AC and why high-voltage transmission minimizes line losses.

**Prerequisites.** Chapter 22 (magnetic fields, Lorentz force). Chapter 20–21 (current, resistance, AC power, circuits). Chapter 19 (capacitors).

**Why this chapter matters.** Every power plant on Earth uses Faraday's law. Every transformer. Every wireless charger. Every regenerative brake. This is the chapter that explains where wall power comes from and why the world's electrical grid is built the way it is.

---

## ↳ Dig Deeper — Why eddy currents brake without contact

*A conducting plate moving through a magnetic field develops circulating eddy currents that, by Lenz's law, oppose its motion. This is regenerative braking in electric vehicles, the smooth deceleration of roller-coasters, and why a metal pan heats on an induction cooktop.*

**Prompt:**
> Explain eddy-current braking: a conducting plate (aluminum or copper) moving through a region of magnetic field perpendicular to its motion. Show how the changing flux through different parts of the plate induces circulating eddy currents, and how those currents in the field feel a Lorentz force opposing the plate's motion. Connect to (a) regenerative braking in EVs, (b) free-fall deceleration on amusement rides, (c) induction cooktop heating of iron pans. End with one sentence on why eddy-current braking is contactless and wears nothing out — the main advantage over friction brakes.

**What to do with the output:** Save it. Eddy-current physics is one of the most useful engineering applications of Faraday's law and appears in every serious electromagnetic engineering course.

---

## ↳ Dig Deeper — How a transformer steps voltage up or down

*A transformer is two coils around a shared iron core. AC in the primary → changing flux in the core → induced EMF in the secondary. The voltage ratio is the turns ratio. This is the technology that makes the electrical grid possible.*

**Prompt:**
> Explain transformer physics from Faraday's law. Walk through: AC current in the primary produces changing flux in the iron core; the same $d\Phi/dt$ passes through the secondary; Faraday's law gives $V_s = N_s(d\Phi/dt)$ and $V_p = N_p(d\Phi/dt)$, so $V_s/V_p = N_s/N_p$. Then apply power conservation ($V_pI_p = V_sI_s$) and show numerically why high-voltage transmission reduces $I^2R$ losses. End with one sentence on why this only works for AC and how HVDC (high-voltage DC) transmission has become competitive using modern power electronics.

**What to do with the output:** Save it. The transformer story is the engineering reason the electrical grid exists as it does, and it directly sets up Chapter 24 (electromagnetic waves).

---

## ↳ Dig Deeper — Why 60 Hz (and 50 Hz)?

*The choice of 60 Hz in North America and 50 Hz in most of the world was made in the late 19th century. The choice was not arbitrary — it balanced rotating-machine speed, transformer efficiency, and lighting flicker — and it locked in permanently with the infrastructure.*

**Prompt:**
> Explain why the world's electrical grids use 50 or 60 Hz rather than some other frequency. Walk through the trade-offs: (a) lighting flicker — lamps below ~40 Hz visibly flicker; (b) transformer efficiency — higher frequency allows smaller cores but more iron loss; (c) rotating-machine speeds — 60 Hz with 2-pole generators gives 3,600 rpm; (d) skin effect — higher frequencies concentrate current near the wire surface; (e) infrastructure lock-in — once the frequency is chosen, switching requires replacing every machine. End with one sentence on where HVDC is returning to DC for specific modern applications.

**What to do with the output:** Save it. The 50/60 Hz story is one of the best case studies in how physics constraints interact with engineering choices that then become permanently locked in.

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
   - Bike commute: bike dynamo lighting the headlight; regenerative braking on an e-bike.
   - Coffee maker: the relay coil switching the heating element.
   - Marathon: kinetic-energy harvesting in a self-powered watch.
   - Espresso machine: AC induction motor in the pump.
   - Basketball: inductive sensor in sports tracking equipment.

2. Estimate or compute:
   (a) Geometry: turns, area, field, frequency.
   (b) Induced EMF (V).
   (c) Current and power transferred.

3. State inputs and uncertainty.

4. Identify whether the device works by motional EMF, changing field (transformer), or both.

5. Sanity check against published specs.

6. Connect to Chapter 24 (Electromagnetic Waves) — changing fields propagate through empty space as light.

Save the output as logbook/chapter-23-induction.md.
```

### What this produces

Your twenty-third Logbook entry — an induction-related calculation anchored to your phenomenon.

### How to adapt this prompt

- *For phenomena with no obvious inductive element:* every appliance plugged into the wall passes through transformers. Pick the wall-power chain.
- *For Claude Code:* if you have an oscilloscope trace of an AC waveform, fit the amplitude, frequency, and phase and analyze the impedance.

### Connection to previous chapters

Builds on Chapter 22 (magnetic fields, Lorentz force) and Chapter 20–21 (current, circuits). Energy bookkeeping from Chapter 7 reappears: mechanical work in, electrical work out.

### Preview of next chapter

Chapter 24 closes the electromagnetic arc. Maxwell's addition to Faraday's law predicts that electric and magnetic fields can propagate through empty space at speed $c$ — and that prediction turns out to be light.

---

## What would change my mind

The chapter argues that Faraday's law and standard AC machinery are sufficient for all practical electromagnetic-induction problems at the introductory level. The argument would need revision if a routine engineering problem required the full Maxwell treatment or relativistic field corrections — they do for radio antennas (Chapter 24) and high-energy physics (Chapter 28), but not for any utility-grid or consumer-electronics application.

## Still puzzling

The deepest puzzle this chapter raises and does not resolve: *why are electric and magnetic fields linked at all?* Faraday's law says changing $B$ creates $E$; Maxwell's addition says changing $E$ creates $B$; together they allow fields to propagate through empty space. The wave speed is $1/\sqrt{\mu_0\epsilon_0}$, which equals $c$. This identification of light as an electromagnetic wave is one of the most consequential predictions in the history of physics. Why the universe arranges its fields to sustain each other in this particular way — that question pushes into the deepest structure of quantum field theory and general relativity, and it remains, at some level, open.

---

## AI Wayback Machine

**Nikola Tesla** developed the polyphase AC induction motor and AC power distribution in the 1880s — the technology that made the modern electrical grid possible. His system displaced Edison's DC despite an extraordinarily fierce public-relations campaign.

![Nikola Tesla](../images/nikola-tesla-22z.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Nikola Tesla, and how does his AC power work connect to electromagnetic induction we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Nikola Tesla"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain why AC, not DC, makes long-distance power transmission practical — using the transformer physics from this chapter.
- Ask it about the mythologized Tesla figure vs. the historical record: what's accurate, what's overblown.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 24 closes the electromagnetic story: Maxwell shows that the electric and magnetic fields described in Chapters 18–23 can propagate through empty space as waves at speed $c$ — and those waves are light. The same equations that govern your wireless charger at 200 kHz govern visible light at $5 \times 10^{14}$ Hz, X-rays at $10^{18}$ Hz, and beyond. Faraday's needle jump in 1831 is the starting point; Maxwell's prediction of light in 1865 is the destination; and quantum electrodynamics — a future chapter — is what comes after that.

---

**Tags:** electromagnetic-induction, Faradays-law, transformers, AC-circuits, generators
