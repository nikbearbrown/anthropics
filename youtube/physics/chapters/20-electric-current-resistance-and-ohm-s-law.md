# Chapter 20 — Electric Current, Resistance, and Ohm's Law

*Two speeds of electricity, one toaster, and why Georg Ohm lost his job.*

---

Push down the lever on a kitchen toaster. The bread starts heating in milliseconds. The orange glow of the heating element appears essentially instantly. Yet the individual electrons in that heating element wire are drifting along at about $0.0001 \text{ m/s}$ — a tenth of a millimeter per second. At that pace, a single electron would take three hours to crawl from the wall plug to the heating element.

This is one of the genuinely strange facts about electricity. If electrons move so slowly, why does the toaster respond instantly?

![Schematic Drude trajectory: an electron moves freely between collisions with lattice ions (positive cores arranged regularly). Each segment is a small accelerated drift in the field direction; collisions reset the velocity....](../images/20-electric-current-resistance-and-ohm-s-law-fig-04.png)
*Figure 20.4 — Drude Model — Zigzag Through Lattice Ions with Field-Biased Hops*

The answer is that two different things are moving. The *signal* — the electromagnetic field that tells electrons to start drifting — travels at roughly $2 \times 10^8 \text{ m/s}$, close to the speed of light. The *carriers*, the electrons themselves, drift glacially. When you close the switch, the electric field propagates through the wire almost instantly. Every electron in the wire starts drifting simultaneously — they don't have to travel from the switch to the heater, they just have to start moving where they already are. Think of a long pipe packed with marbles: push one marble at one end and a marble pops out the other end almost immediately, even though no individual marble traveled the length of the pipe.

This chapter is about making that precise — what current really is, what resistance really is, what Ohm's law actually claims (and where it fails), and what makes the mathematics of $V = IR$ one of the most useful equations in engineering.

---

## Current: charge in motion

Hans Christian Ørsted, in April 1820, was setting up a lecture demonstration at the University of Copenhagen. Tradition says he was about to show that electricity and magnetism were unrelated. Instead he discovered the opposite: when he aligned a wire parallel to a compass needle and closed the circuit, the needle deflected. Electric current produces a magnetic field.

That discovery launched electromagnetism, but it also gave physicists their first quantitative handle on current. A deflecting compass needle could be used to measure how much current was flowing — before ammeters existed, before any clean definition of the ampere had been written down. Current was not a vague concept; it was a measurable quantity with observable effects.

**Electric current** is the rate of flow of charge:

$$I = \frac{Q}{t},$$

with units $1 \text{ A} = 1 \text{ C/s}$. One **ampere** (named for André-Marie Ampère, who developed the mathematical theory of electromagnetism in the 1820s) is one coulomb of charge passing a given cross-section per second.

A few values to anchor your intuition: a USB charger delivers 1–2 A; a kitchen toaster draws about 12 A; a lightning bolt carries roughly 30,000 A for a millisecond. The range is enormous.

One important convention: **conventional current** flows from the positive terminal of the battery through the external circuit to the negative. This is the direction positive charges would move. Electrons, which carry negative charge, actually flow the other way — from negative to positive. The convention was established by Benjamin Franklin before electrons were discovered, and we keep it because it makes signs work out cleanly in most equations.

### Drift velocity

The current through a wire is related to how fast the carriers are moving by

$$I = n q A v_d,$$

where $n$ is the number density of charge carriers (free electrons per cubic meter), $q$ is the charge per carrier ($e = 1.6 \times 10^{-19} \text{ C}$ for electrons), $A$ is the wire's cross-sectional area, and $v_d$ is the **drift velocity** — the average speed at which carriers move along the wire.

For copper wire carrying 1 A, with cross-section $A = 3 \times 10^{-6} \text{ m}^2$ and free electron density $n \approx 8.5 \times 10^{28} \text{ /m}^3$:

$$v_d = \frac{I}{nqA} = \frac{1}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(3 \times 10^{-6})} \approx 2.5 \times 10^{-5} \text{ m/s}.$$

Twenty-five micrometers per second. About the speed at which fingernails grow. Each individual electron drifts at this pace — yet the toaster heats up in milliseconds, because every electron in the entire wire starts drifting simultaneously when the field arrives.

![Log ladder of electron speeds in a copper wire. Drift velocity (current carrier average) 10⁻⁴ m/s. Thermal speed (rms at 300 K) 10⁵ m/s. Fermi velocity (typical electron near Fermi surface in copper) 1.6×10⁶ m/s. Signal speed...](../images/20-electric-current-resistance-and-ohm-s-law-fig-01.png)
*Figure 20.1 — Four Speeds of Electricity — Drift, Thermal, Fermi, Signal*

![Two snapshots of electron motion in a wire. No field applied: random thermal velocities, mean velocity zero, no current. Field E applied: same chaotic motion but with a slight bias in the direction opposite E. Centroid of...](../images/20-electric-current-resistance-and-ohm-s-law-fig-03.png)
*Figure 20.3 — Drift Velocity — A Slow Bias Riding on Top of Thermal Chaos*

![An electron accelerated by E gains KE between collisions. At each collision with a lattice ion, the gained KE transfers to lattice vibrations (heat). Total dissipation rate P = I²R = V²/R. Mechanism: drift work converted to...](../images/20-electric-current-resistance-and-ohm-s-law-fig-06.png)
*Figure 20.6 — Joule Heating — Electron KE Transferred to Lattice Vibrations*

The thermal speed of electrons in copper is about $10^6 \text{ m/s}$ — they're already moving extremely fast in random directions. The drift is a tiny directed bias on top of this random motion. The random motion stores thermal energy; the drift carries current. They operate on completely different velocity scales, which is why the toaster signal arrives at light speed while no individual electron makes the journey.

<!-- → [INFOGRAPHIC: two-panel diagram contrasting the two speeds — left panel shows a wire cross-section with electrons doing random zigzag motion (thermal ~10⁶ m/s) plus a tiny net rightward drift arrow (v_d ~10⁻⁵ m/s); right panel shows a timeline: signal from switch reaches heater in nanoseconds, an individual electron would take hours; student should see that current flow doesn't require electrons to travel from switch to heater] -->

A 60 W incandescent bulb at 120 V draws $I = P/V = 60/120 = 0.50 \text{ A}$, which means about $3 \times 10^{18}$ electrons pass through the filament every second. Three quintillion electrons per second, each moving at the speed of a growing fingernail. Collectively they carry half a coulomb of charge per second. That is current.

---

## Resistance and Ohm's law

In 1825, Georg Simon Ohm — a high-school physics teacher in Cologne, working with homemade equipment — began a four-year experimental program. He took wires of different lengths and thicknesses, applied controlled voltages, and measured currents with a magnetic-needle galvanometer built on Ørsted's discovery. His instruments were primitive but his patience was not.

The pattern he published in 1827:

$$V = IR,$$

where $V$ is the voltage across the conductor, $I$ is the current, and $R$ is the **resistance**, measured in **ohms** ($\Omega$, with $1 \Omega = 1 \text{ V/A}$). For a wide range of metallic conductors, current is proportional to applied voltage. Double the voltage, double the current.

Ohm's 1827 book was poorly received in Germany — too empirical for the dominant idealistic philosophy of the time. He resigned his teaching position and spent six years doing menial work before being recognized with a professorship and, eventually, a law named after him. It now governs every electrical engineering textbook ever written.

### Where resistance comes from

Resistance depends on both geometry and material:

$$R = \frac{\rho L}{A},$$

where $L$ is the conductor's length, $A$ is its cross-section, and $\rho$ is the **resistivity** of the material in units of $\Omega\cdot\text{m}$.

| Material | Resistivity ($\Omega\cdot\text{m}$) at 20°C |
|---|---|
| Silver | $1.59 \times 10^{-8}$ |
| Copper | $1.72 \times 10^{-8}$ |
| Aluminum | $2.65 \times 10^{-8}$ |
| Iron | $9.71 \times 10^{-8}$ |
| Nichrome (heating element) | $1.0 \times 10^{-6}$ |
| Carbon | $\sim 3.5 \times 10^{-5}$ |
| Silicon (pure) | $640$ |
| Glass | $10^{10}$ to $10^{14}$ |
| Quartz | $\sim 7.5 \times 10^{17}$ |

![Log bar chart of electrical resistivity ρ (Ω·m) for diverse materials: silver 1.6×10⁻⁸, copper 1.7×10⁻⁸, aluminum 2.7×10⁻⁸, steel 1×10⁻⁷, nichrome 1.5×10⁻⁶, carbon 3.5×10⁻⁵, germanium 0.5, silicon 640, glass 10¹², fused quartz...](../images/20-electric-current-resistance-and-ohm-s-law-fig-02.png)
*Figure 20.2 — Resistivity Ladder — Silver to Fused Quartz Spans 10²⁶*

That table spans about 26 orders of magnitude — from quartz to silver. The choice of conductor or insulator is, at root, a choice of $\rho$. Copper is the standard for household wiring because it is the second-best conductor (after silver, which is too expensive) and ductile enough to draw into wire. Nichrome — a nickel-chromium alloy — is used for heating elements precisely because its resistivity is high enough to dissipate substantial power at line voltages.

The formula $R = \rho L/A$ has a clean physical meaning: longer wires have higher resistance (more scattering events for the electrons); thicker wires have lower resistance (more parallel paths). Same logic as water flow through a pipe.

### Temperature dependence

Resistance of metals increases with temperature:

$$R = R_0[1 + \alpha(T - T_0)],$$

where $\alpha \approx 4 \times 10^{-3}/°\text{C}$ for copper. At higher temperature, lattice atoms vibrate more energetically, scattering electrons more frequently and reducing drift velocity. A toaster's nichrome element, glowing red-hot at around $1{,}100°\text{C}$, has about three times the resistance it had cold.

Semiconductors go the other way: resistance *decreases* with temperature, because heating creates more free charge carriers, overcoming the lattice-scattering increase. This is why transistors can thermally run away — higher temperature means lower resistance, which means higher current, which means higher temperature.

### Ohmic and nonohmic

Materials that obey $V = IR$ with constant $R$ are **ohmic**. Most metallic resistors at constant temperature.

![Four I-V curves on one set of axes. Ohmic resistor: straight line through origin, slope 1/R. Filament: sublinear (R rises with T as current heats it). Diode: zero current below threshold, then exponential. Thermistor (NTC):...](../images/20-electric-current-resistance-and-ohm-s-law-fig-05.png)
*Figure 20.5 — I vs V — Linear (Ohmic) and Three Flavors of Non-Ohmic*

Materials whose $V$-versus-$I$ curve is nonlinear are **nonohmic**. Diodes pass current in one direction only; their current-voltage relationship is exponential. Semiconductor transistors have gate-voltage-dependent resistance — the nonlinearity is exactly what makes amplification and digital switching possible. An incandescent bulb filament starts cold ($\sim 10 \Omega$) and heats to $\sim 100 \Omega$ under current; the resistance triples between switch-on and steady-state. The cold surge of current — twelve times the steady-state value — lasts only a few milliseconds while the filament heats up. This repeated cold-surge stress is why bulbs most often fail at the moment of switching on, not during steady burning.

For every introductory problem, treat resistors as ohmic unless explicitly told otherwise.

### The toaster heating element, quantified

A 1500 W toaster runs at 120 V. Operating current: $I = P/V = 1500/120 = 12.5 \text{ A}$. Resistance: $R = V/I = 120/12.5 = 9.6 \Omega$. The element is nichrome wire with cross-section $A = 5 \times 10^{-7} \text{ m}^2$. Length:

$$L = \frac{RA}{\rho} = \frac{(9.6)(5 \times 10^{-7})}{1.0 \times 10^{-6}} = 4.8 \text{ m}.$$

Almost five meters of nichrome wire, coiled to fit inside a box you hold in your hand. Look down into the toaster slots and you can see the tightly wound element — exactly what $4.8 \text{ m}$ looks like when coiled compactly.

<!-- → [INFOGRAPHIC: resistivity scale bar — horizontal log-scale bar from 10⁻⁸ to 10¹⁸ Ω·m; mark positions of silver (1.59×10⁻⁸), copper (1.72×10⁻⁸), nichrome (1.0×10⁻⁶), carbon (3.5×10⁻⁵), silicon (640), glass (10¹²), quartz (7.5×10¹⁷); color the left (conductor) end in orange and the right (insulator) end in blue; annotate that the 26-order-of-magnitude span from quartz to silver is larger than the span from the size of a proton to the size of the solar system; student should see that the choice of conductor vs. insulator is simply a choice of ρ on this scale] -->

---

## Power, AC, and the grid

When current $I$ flows through a resistor $R$ under voltage $V$, energy is dissipated as heat. The **power** dissipated:

$$P = IV = I^2R = \frac{V^2}{R}.$$

Use whichever form has the variables you know. For the toaster, all three give 1500 W — as they must, since they are the same equation written three ways.

The energy dissipated in time $t$: $E = Pt$. A 1500 W toaster running for an hour uses 1.5 kWh, which at \$0.15/kWh costs 22 cents.

### AC and the grid

On September 4, 1882, Thomas Edison opened Pearl Street Station in Manhattan — the world's first commercial power station. DC at 110 V, 80 customers, half a square mile. The problem: DC at low voltage cannot be transmitted efficiently over long distances. Power loss in a transmission line goes as $I^2R$. For fixed delivered power $P = IV$, lower voltage means higher current means more $I^2R$ waste. Edison's stations had to be within a mile of their customers.

George Westinghouse and Nikola Tesla championed alternating current because AC voltages can be stepped up by transformers for transmission and back down for use. The War of Currents ended with AC dominant. Every wall outlet is AC at 60 Hz (North America) or 50 Hz (most of the world).

For power calculations, AC uses the **root-mean-square** (RMS) voltage. AC voltage varies as $V(t) = V_0 \sin(2\pi ft)$. The time-average power in a resistor is

$$\bar{P} = \frac{V_\text{RMS}^2}{R}, \quad \text{where} \quad V_\text{RMS} = \frac{V_0}{\sqrt{2}}.$$

The "120 V" on every US appliance is the RMS value. Peak is $120\sqrt{2} \approx 170 \text{ V}$. The RMS convention makes AC and DC power formulas look identical: a 1500 W AC toaster dissipates the same average power as a 1500 W DC heater of the same resistance.

The modern grid uses 115–765 kV for transmission. A 200 km line with $R = 10 \Omega$ carrying 1 GW at 500 kV: $I = 2{,}000 \text{ A}$, line loss = $(2{,}000)^2 \times 10 = 40 \text{ MW}$ — about 4%. Transmit the same 1 GW at 11 kV: $I = 90{,}900 \text{ A}$, line loss exceeds the power you're transmitting. High voltage is not primarily about safety or insulation. It is about minimizing waste.

### Electrical safety

The same $V = IR$ governs what current flows through a person who touches a live wire. Skin resistance depends on moisture and contact area:

Dry skin, light contact: $\sim 10^5 \Omega$. At 120 V, $I = 1.2 \text{ mA}$ — perceptible but not dangerous. Wet skin, firm contact: $\sim 10^3 \Omega$. The same 120 V drives $\sim 120 \text{ mA}$ — into the range of ventricular fibrillation. Submerged: as low as $\sim 100 \Omega$. Lethal currents at ordinary voltages.

The voltage is the same. The resistance — set by skin condition and contact area — determines whether you live or die. This is why bathroom outlets require GFCI protection, which cuts power within milliseconds if current leaks through an unexpected path.

---

## Everything from two equations

Current, resistance, and power all flow from two equations:

$$V = IR \quad \text{(Ohm's law)}$$
$$P = IV.$$

From these two, by substitution, you get every relationship in the chapter. The marble-pipe metaphor that opened the chapter captures the signal-versus-carrier split: the electromagnetic field that propagates at near light speed is what actually carries the instruction to "start drifting"; the carriers themselves crawl at $v_d$. Both facts live in $I = nqAv_d$ — $v_d$ is the crawl, and the speed at which the field sets up that uniform drift is the light-speed signal.

A USB-C charger delivers 5 V at 3 A: $P = IV = 15 \text{ W}$ to your phone. At the wall (120 V AC, 90% efficient): $P_\text{in} = 15/0.90 \approx 16.7 \text{ W}$, $I = 16.7/120 \approx 0.14 \text{ A}$. The current on the phone side (3 A) is twenty times larger than on the wall side (0.14 A) because $P = IV$ requires current to be inversely proportional to voltage at fixed power. The heavier USB-C cable on the phone side handles 3 A; the thin wall-outlet wiring handles 0.14 A comfortably.

Scale that up by $10^{10}$ and you have the grid: 1 GW at 500 kV, $I = 2{,}000 \text{ A}$ in the transmission line; delivering the same 1 GW at 120 V would require $I = 8.3 \times 10^6 \text{ A}$ — a current no cable could carry. The entire electrical grid is an application of $P = IV$.

---

## Exercises

### Warm-up

**20.1** *(LO 1)* A current of $3.0 \text{ A}$ flows through a wire for $45 \text{ s}$. (a) How much charge passes a given cross-section? (b) How many electrons does that represent?

**20.2** *(LO 3)* A resistor has $R = 22 \Omega$. (a) What current flows when $11 \text{ V}$ is applied? (b) What voltage produces a current of $0.75 \text{ A}$ through the same resistor?

**20.3** *(LO 4)* A copper wire ($\rho = 1.72 \times 10^{-8} \text{ Ω·m}$) is $6.0 \text{ m}$ long with cross-sectional area $1.5 \times 10^{-6} \text{ m}^2$. (a) Compute its resistance. (b) If the wire's length were doubled and its diameter halved (area quartered), what is the new resistance?

**20.4** *(LO 6)* An 80 W light bulb runs at 120 V. Compute: (a) current drawn; (b) resistance; (c) energy used in 10 hours; (d) cost at \$0.15/kWh.

### Application

**20.5** *(LO 2)* A copper wire ($n = 8.5 \times 10^{28} \text{ /m}^3$) with cross-section $A = 4.0 \times 10^{-6} \text{ m}^2$ carries $8.0 \text{ A}$. (a) Compute the drift velocity. (b) How long would it take one electron to travel $1.5 \text{ m}$ along this wire at the drift velocity? (c) Compare to the time for the signal to travel the same $1.5 \text{ m}$ at $2 \times 10^8 \text{ m/s}$.

**20.6** *(LO 4, 8)* A nichrome heating coil has cold resistance $R_0 = 25 \Omega$ at $20°\text{C}$. The temperature coefficient $\alpha_\text{Ni} \approx 4.0 \times 10^{-4}/°\text{C}$. When glowing at $1{,}000°\text{C}$: (a) what is the hot resistance? (b) If powered by 120 V, compare the startup current (cold) to the operating current (hot). (c) What is the startup power vs. operating power?

**20.7** *(LO 3, 6)* A hair dryer is rated at $1{,}875 \text{ W}$ at 120 V. (a) What current does it draw? (b) What is its operating resistance? (c) Will it trip a 15-A breaker? (d) Can you run it simultaneously with a 1500 W toaster on the same 15-A circuit?

**20.8** *(LO 6, 7)* A US wall outlet provides $V_\text{RMS} = 120 \text{ V}$ AC. (a) What is the peak voltage $V_0$? (b) A toaster draws $I_\text{RMS} = 12.5 \text{ A}$. Find the peak instantaneous power and the average power. (c) What DC voltage would deliver the same average power to the same resistance?

### Synthesis

**20.9** *(LO 4, 8)* A 1500 W toaster designed for 120 V US outlets is plugged into a 240 V outlet in Europe without a voltage converter. (a) Compute the current it draws. (b) Compute the power it dissipates. (c) Why is this dangerous? (d) What resistance would a 240 V toaster with the same 1500 W rating need?

**20.10** *(LO 6, 7)* A power transmission line carries 800 MW over 250 km at 400 kV (RMS). The line has total resistance $12 \Omega$. (a) Compute the current. (b) Compute the power lost as heat. (c) Express the loss as a percentage of transmitted power. (d) If the same power were transmitted at 40 kV instead, by what factor does the line loss change?

**20.11** *(LO 3, 5)* A silicon diode at room temperature follows $I = I_0(e^{V/V_T} - 1)$ with $I_0 = 10^{-12} \text{ A}$ and $V_T = 0.026 \text{ V}$. (a) Compute the current at $V = 0.3$, $0.5$, $0.7 \text{ V}$. (b) Is the diode ohmic? (c) Compute the effective resistance $R = V/I$ at each voltage and comment on how it changes.

### Challenge

**20.12** *(LO 4, 5, beyond chapter)* When you turn on an incandescent lamp, the filament starts at room temperature (resistance $\sim 10 \Omega$) and heats to operating temperature (resistance $\sim 100 \Omega$) in about $0.10 \text{ s}$. (a) Compute the initial current and power at 120 V. (b) Compute the steady-state current and power. (c) Estimate the energy deposited in the filament during the $0.10 \text{ s}$ surge (use the average of initial and final power). (d) The tungsten filament has mass $\sim 0.1 \text{ g}$ and specific heat $\sim 130 \text{ J/(kg·K)}$. Estimate the temperature rise from this energy. (e) Why does the surge not destroy the filament?

**20.13** *(LO 1, 2, beyond chapter)* A copper wire of length $2.0 \text{ m}$ and diameter $1.0 \text{ mm}$ is used as an extension cord for a $1{,}200 \text{ W}$ appliance at 120 V. (a) Compute the wire's resistance. (b) Compute the voltage drop across the cord at operating current. (c) What fraction of the 120 V supply is lost? (d) What power is dissipated in the cord as heat? (e) At what cord length would the voltage drop reach 5% of the supply voltage?

---



By the end of this chapter you should be able to:

1. Define electric current $I = Q/t$ and identify conventional vs. electron flow direction.
2. Compute drift velocity from $I = nqAv_d$ and explain why it is so small despite fast signal propagation.
3. State and apply Ohm's law $V = IR$ for ohmic materials.
4. Compute resistance from $R = \rho L/A$ and use the temperature-dependence formula $R = R_0[1 + \alpha(T - T_0)]$.
5. Distinguish ohmic from nonohmic devices and give examples of each.
6. Compute power using $P = IV = I^2R = V^2/R$ and convert between watts, kilowatt-hours, and joules.
7. Explain why AC transmission at high voltage minimizes $I^2R$ losses, and apply RMS voltage for AC power calculations.

**Prerequisites.** Chapter 18 (electric charge). Chapter 19 (voltage and potential). Algebra.

**Why this chapter matters.** Every electrical device you use runs on the relationships in this chapter. The wattage of an appliance, the current draw of a charger, the resistance of a heating element, the reason the grid runs at hundreds of kilovolts — all follow from $V = IR$ and $P = IV$.

---

## ↳ Dig Deeper — Why drift velocity is slow but signals are fast

*The marble-pipe analogy is useful but imprecise. The actual mechanism involves electromagnetic fields propagating at near-light-speed along the surface of the conductor, while individual electrons scatter on picosecond timescales and accumulate tiny average drift velocities.*

**Prompt:**
> Explain the gap between drift velocity (~10⁻⁵ m/s) and signal speed (~2×10⁸ m/s) in electrical conductors. Walk through: (1) the random thermal speed of free electrons in copper (~10⁶ m/s), (2) the mean free path and collision frequency, (3) how an electric field produces a small drift on top of this random motion, (4) how the field itself propagates as a transverse electromagnetic wave guided by the conductor, adjusting surface charges along the entire wire essentially simultaneously. End with one sentence on why this is the conceptual foundation for transmission lines and high-frequency electronics.

**What to do with the output:** Save it. The signal-vs-carrier distinction is the key to antennas, transmission lines, and every high-frequency electronic system.

---

## ↳ Dig Deeper — Superconductivity: resistance exactly zero

*Some materials, cooled below a critical temperature, have literally zero resistance — not just very low, but exactly zero. Discovered by Heike Kamerlingh Onnes in mercury at 4.2 K in 1911, this is a quantum-mechanical effect with no classical analog, and it is the basis of MRI machines and particle accelerator magnets.*

**Prompt:**
> Explain superconductivity: below a critical temperature $T_c$, some materials have *exactly* zero resistance. Walk through the history (Kamerlingh Onnes, 1911), the BCS theory (electron pairs coupled by lattice phonons, forming Cooper pairs that move without scattering), and the existence of "high-temperature" superconductors (cuprates, $T_c$ up to ~135 K). End with one sentence on practical applications: MRI machines, maglev trains, particle accelerators, and the ongoing search for room-temperature superconductors.

**What to do with the output:** Save it. Superconductivity is one of the most beautiful connections between quantum mechanics and a macroscopic, engineering-scale property of matter.

---

## ↳ Dig Deeper — Why high-voltage transmission and the transformer

*The reason you get electricity from a power plant 100 km away instead of from a local generator is the transformer. Transformers step AC voltage up for transmission (minimizing $I^2R$ losses) and back down for safe use. This only works because the current is alternating.*

**Prompt:**
> Explain why long-distance electrical transmission uses high voltage. Compute power loss $P_\text{loss} = I^2R$ for a fixed delivered power $P = IV$ at two different transmission voltages — 110 kV and 500 kV — over a 200 km line with 10 Ω resistance. Show numerically how the losses differ. Then explain why transformers make this possible for AC but not for DC — and add one sentence on why high-voltage DC (HVDC) has become viable in recent decades for specific applications.

**What to do with the output:** Save it. The transformer/transmission story is the engineering reason the modern electrical grid exists as it does. It sets up Chapter 23's electromagnetic induction.

---

## LLM Exercise — Chapter 20: Current and Power in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A current and power calculation for one electrical component of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 20 (Current, Resistance, Ohm's Law), I want to identify ONE current-carrying component of my phenomenon.

Please:

1. Identify the current. Examples:
   - Bike commute: e-bike motor current draw, or current through brake-light LEDs.
   - Coffee maker: current through the heating element when brewing.
   - Marathon: current through a GPS smartwatch chip.
   - Espresso machine: current draw of the pump motor.
   - Basketball: current through scoreboard LEDs.

2. Identify or estimate:
   (a) Voltage applied (V).
   (b) Current drawn (A).
   (c) Resistance (Ω) — compute from R = V/I or look up.
   (d) Power dissipated (W) — compute from P = IV.
   (e) Energy consumed per use (J or kWh).

3. State your inputs, sources, and uncertainty.

4. Sanity check: does the power match the rated wattage of the device?

5. Estimate the cost of running this component for one hour at $0.15/kWh.

6. Connect to Chapter 21 (Circuits), where multiple resistors and voltage sources are combined.

Save the output as logbook/chapter-20-current.md.
```

### What this produces

Your twentieth Logbook entry — a current-and-power analysis of your phenomenon.

### How to adapt this prompt

- *For phenomena with no obvious current:* every electronic device involves current; if your phenomenon is non-electrical, pick a peripheral aspect (lights, sensors, monitors).
- *For Claude Code:* if you have a power-monitor reading, plot power vs. time and integrate to get total energy.

### Connection to previous chapters

Builds on Chapter 19's voltage and potential. Energy bookkeeping from Chapter 7 reappears in the kilowatt-hour calculation.

### Preview of next chapter

Chapter 21 combines resistors, voltage sources, and capacitors into circuits using Kirchhoff's laws. The Chapter 21 LLM Exercise will analyze a multi-component circuit in your phenomenon.

---

## What would change my mind

The chapter argues that Ohm's law and the power formulas cover essentially all introductory current problems. The argument would need revision if a routine consumer-electronics problem were so dominated by nonlinear semiconductor behavior that the linear formulas gave wrong answers for average power — they don't, for time-averaged power balance, though instantaneous behavior in switching power supplies is genuinely complex.

## Still puzzling

The deepest puzzle: *why is Ohm's law so linear over such an enormous range of metallic materials?* The microscopic story involves electrons scattering off phonons at a rate roughly proportional to temperature, with a mean free path roughly independent of field strength — a combination that gives $V \propto I$ when derived from the Drude model. But the quality of the approximation, across so many metals and current densities, is remarkable. The deviations — in semiconductors, in superconductors, at very high fields — are where the interesting physics lives.

---

## AI Wayback Machine

**Georg Simon Ohm** published the law bearing his name in 1827 — establishing that current is proportional to voltage for metallic conductors. The book was so poorly received in Germany that he resigned his teaching position. His name is now on the unit of resistance.

**Run this:**

```
Who was Georg Simon Ohm, and how does Ohm's law connect to the current and resistance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Georg Ohm"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Ohm's original experiments demonstrating $V = IR$.
- Ask it about why Ohm's 1827 book was poorly received — and what changed.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 21 builds circuits by combining resistors, batteries, and capacitors with Kirchhoff's voltage and current laws. Chapter 22 introduces magnetism — the field produced by currents and felt by moving charges — which is where Ørsted's 1820 observation finally gets its mathematical treatment. Chapter 23 introduces electromagnetic induction, the heart of generators, motors, and transformers, and explains why the grid runs on AC. Chapter 24 reveals that electric and magnetic fields propagate together as waves at speed $c$. Every later chapter on electricity rests on the $V$, $I$, $R$, $P$ relationships installed here.

---

**Tags:** electric-current, Ohms-law, resistance, power, drift-velocity
