# Chapter 20 — Electric Current, Resistance, and Ohm's Law

*Two speeds of electricity, one toaster, and why Georg Ohm lost his job.*

---

Push down the lever on a kitchen toaster. The bread starts heating in milliseconds. The orange glow of the heating element appears essentially instantly. Yet the individual electrons in that heating element wire are drifting along at about $0.0001 \text{ m/s}$ — a tenth of a millimeter per second. At that pace, a single electron would take three hours to crawl from the wall plug to the heating element.

This is one of the genuinely strange facts about electricity. If electrons move so slowly, why does the toaster respond instantly?

The answer is that two different things are moving. The *signal* — the electromagnetic field that tells electrons to start drifting — travels at roughly $2 \times 10^8 \text{ m/s}$, close to the speed of light. The *carriers*, the electrons themselves, drift glacially. When you close the switch, the electric field propagates through the wire almost instantly. Every electron in the wire starts drifting simultaneously — they don't have to travel from the switch to the heater, they just have to start moving where they already are. Think of a long pipe packed with marbles: push one marble at one end and a marble pops out the other end almost immediately, even though no individual marble traveled the length of the pipe.

This chapter is about making that precise — what current really is, what resistance really is, what Ohm's law actually claims (and where it fails), and what makes the mathematics of $V = IR$ one of the most useful equations in engineering.

---

## Current: charge in motion

![Two panels. Series: three resistors in a chain, R_total = R₁ + R₂ + R₃ (additive). Parallel: three resistors across the same two nodes, 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ (reciprocal additive). Capacitors follow the opposite pattern.](../images/21-circuits-and-dc-instruments-fig-03.png)
*Figure 21.3 — Series and Parallel Resistors — Two Combination Rules*

![Two curves on the same axes. Charging: q(t) = Q_max(1 − e^(−t/τ)), reaches 63% at t = τ. Discharging: q(t) = Q₀ e^(−t/τ), drops to 37% at t = τ. τ = RC is the time constant.](../images/21-circuits-and-dc-instruments-fig-06.png)
*Figure 21.6 — RC Circuit — Charging and Discharging, τ = RC*

Hans Christian Ørsted, in April 1820, was setting up a lecture demonstration at the University of Copenhagen. Tradition says he was about to show that electricity and magnetism were unrelated. Instead he discovered the opposite: when he aligned a wire parallel to a compass needle and closed the circuit, the needle deflected. Electric current produces a magnetic field.

That discovery launched electromagnetism, but it also gave physicists their first quantitative handle on current. A deflecting compass needle could be used to measure how much current was flowing — before ammeters existed, before any clean definition of the ampere had been written down. Current was not a vague concept; it was a measurable quantity with observable effects.

**Electric current** is the rate of flow of charge:

$$I = \frac{Q}{t},$$

with units $1 \text{ A} = 1 \text{ C/s}$. One **ampere** (named for André-Marie Ampère, who developed the mathematical theory of electromagnetism in the 1820s) is one coulomb of charge passing a given cross-section per second.

A few current values to anchor your intuition: a USB charger delivers 1–2 A; a kitchen toaster draws about 12 A; a lightning bolt carries roughly 30,000 A for a millisecond. The range is enormous.

![Left: KCL at a junction. Three currents flow in (I₁, I₂, I₃ entering), one out (I₄ leaving). Sum: I₁ + I₂ + I₃ = I₄. Right: KVL around a loop. Battery ε pumps energy up; resistors dissipate (V drops). Algebraic sum around any...](../images/21-circuits-and-dc-instruments-fig-02.png)
*Figure 21.2 — Kirchhoff's Laws — KCL = Charge Conservation, KVL = Energy Conservation*

![Two-loop DC circuit with EMFs ε₁ = 12 V and ε₂ = 8 V and resistors R₁ = 4 Ω (left branch), R₂ = 6 Ω (middle), R₃ = 3 Ω (right). Two KVL equations + KCL at central node yield I₁, I₂, I₃ = 1.2, 0.4, 0.8 A.](../images/21-circuits-and-dc-instruments-fig-04.png)
*Figure 21.4 — Two-Loop Worked Example — 12 V + 8 V Sources, R = 4 Ω, 6 Ω, 3 Ω*

![Schematic of a real battery: ideal EMF source ε in series with internal resistance r. When current I flows, the terminal voltage drops by Ir below the EMF. Plot of V_terminal vs I shows linear droop with slope −r.](../images/21-circuits-and-dc-instruments-fig-05.png)
*Figure 21.5 — Real Battery — EMF Plus Internal Resistance, V_terminal = ε − I r*

One important convention: **conventional current** flows from the positive terminal of the battery through the external circuit to the negative. This is the direction positive charges would move. Electrons, which carry negative charge, actually flow the other way — from negative to positive. The convention was established by Benjamin Franklin before electrons were discovered, and we keep it because it makes signs work out cleanly in most equations. When you write $I$ in a formula, you mean conventional current.

### Drift velocity

Now the quantitative version of the marble-pipe puzzle. The current through a wire is related to how fast the carriers are drifting by

$$I = n q A v_d,$$

where $n$ is the number density of charge carriers (free electrons per cubic meter), $q$ is the charge per carrier ($= e = 1.6 \times 10^{-19} \text{ C}$ for electrons), $A$ is the wire's cross-sectional area, and $v_d$ is the **drift velocity** — the average speed at which carriers move along the wire.

For copper wire carrying 1 A, with a typical cross-section $A = 3 \times 10^{-6} \text{ m}^2$ and free electron density $n \approx 8.5 \times 10^{28} \text{ /m}^3$:

$$v_d = \frac{I}{nqA} = \frac{1}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(3 \times 10^{-6})} \approx 2.5 \times 10^{-5} \text{ m/s}.$$

Twenty-five micrometers per second. About the speed at which fingernails grow. Each individual electron drifts at this pace — yet the toaster heats up in milliseconds, because every electron in the entire wire starts drifting simultaneously when the field arrives.

<!-- → [INFOGRAPHIC: two-panel diagram contrasting the two speeds of electricity — left panel: a long copper wire with random zigzag electron paths (thermal velocity ~10⁶ m/s) and a tiny net rightward drift arrow (v_d ~ 10⁻⁵ m/s) labeled "drift velocity"; right panel: the same wire with an electromagnetic wave propagating along it at ~2×10⁸ m/s labeled "signal speed"; below both: a timeline showing that the signal reaches the far end in nanoseconds while an individual electron would take hours — student should see that the two speeds are wildly different and that current flow doesn't require electrons to travel the length of the wire] -->

The thermal speed of electrons in copper is about $10^6 \text{ m/s}$ — they are already moving extremely fast in random directions. The drift is a tiny directed bias on top of this random motion, like a slow current in a river of fast-moving molecules. The random motion is what stores thermal energy; the drift is what carries current. They are on completely different velocity scales.

A 60 W incandescent bulb at 120 V draws $I = P/V = 60/120 = 0.50 \text{ A}$, which means about $0.50/( 1.6 \times 10^{-19}) \approx 3 \times 10^{18}$ electrons pass through the filament every second. Three quintillion electrons per second, each moving at the speed of a growing fingernail. Collectively, they carry half a coulomb of charge per second. That is current.

---

## Resistance and Ohm's law

In 1825, Georg Simon Ohm — a high-school physics teacher in Cologne, working with homemade equipment — began a four-year experimental program. He took wires of different lengths and thicknesses, applied controlled voltages, and measured the resulting currents with a magnetic-needle galvanometer based on Ørsted's discovery. His measuring instruments were primitive, but his patience was not.

The pattern he published in 1827:

$$V = IR,$$

where $V$ is the voltage across the conductor, $I$ is the current, and $R$ is the **resistance**, measured in **ohms** ($\Omega$, with $1 \Omega = 1 \text{ V/A}$). For a wide range of metallic conductors, current is proportional to applied voltage. Double the voltage, double the current. The constant of proportionality is the resistance.

Ohm's 1827 book was poorly received in Germany — too empirical for the dominant idealistic philosophy of the era. He resigned his teaching position and spent six years doing menial work before being recognized with a professorship and, eventually, a law named for him. It now governs every electrical engineering textbook ever written.

### Where resistance comes from

Resistance depends on both geometry and material:

$$R = \frac{\rho L}{A},$$

where $L$ is the conductor's length, $A$ is its cross-section, and $\rho$ is the **resistivity** of the material, in units of $\Omega \cdot \text{m}$.

<!-- → [TABLE: resistivity of representative materials at 20°C — columns: material, resistivity (Ω·m); rows: silver (1.59×10⁻⁸), copper (1.72×10⁻⁸), aluminum (2.65×10⁻⁸), iron (9.71×10⁻⁸), nichrome heating element (1.0×10⁻⁶), carbon (~3.5×10⁻⁵), pure silicon (640), glass (10¹⁰ to 10¹⁴), quartz (~7.5×10¹⁷); student should see the 26-order-of-magnitude span from best conductor to best insulator] -->

That table spans about 26 orders of magnitude — from quartz to silver. The choice of conductor or insulator is, at root, a choice of $\rho$. Copper is the standard for household wiring because it is the second-best conductor (after silver, which is too expensive) and ductile enough to draw into wire. Nichrome — a nickel-chromium alloy — is used for heating elements precisely because its resistivity is high enough to dissipate substantial power at line voltages.

The formula $R = \rho L/A$ has a clean physical meaning: longer wires have higher resistance (electrons must make more collisions); thicker wires have lower resistance (more parallel paths for current). Same logic as water flowing through a pipe: longer pipe, narrower pipe = more resistance to flow.

### Temperature dependence

Resistance of metals increases with temperature:

$$R = R_0[1 + \alpha(T - T_0)],$$

where $\alpha \approx 4 \times 10^{-3}/°\text{C}$ for copper. At higher temperature, lattice atoms vibrate more energetically, scattering electrons more frequently and reducing drift velocity for the same applied field. A toaster's nichrome heating element, glowing red-hot at around $1{,}100°\text{C}$, has about three times the resistance it had cold.

Semiconductors go the other way: resistance *decreases* with temperature, because heating creates more free charge carriers (overcoming the valence band gap), and this increase in carrier density dominates the scattering effect. This is why transistors can thermally run away — higher temperature means lower resistance, which means higher current, which means higher temperature.

### Ohmic and nonohmic

Materials that obey $V = IR$ with constant $R$ are **ohmic**. Most metallic conductors at constant temperature qualify.

Materials whose $V$-versus-$I$ curve is nonlinear are **nonohmic**:

Diodes pass current in one direction only — the current through a diode does not simply scale with voltage; it has a threshold and then rises exponentially. A semiconductor transistor is a three-terminal device that controls current flowing through it with a gate voltage — the control is nonlinear and that nonlinearity is exactly what makes amplification and digital switching possible.

![Two panels. Top: series wiring — battery, bulbs in a single chain; one burnout breaks the loop, all bulbs go dark. Bottom: parallel wiring — each bulb across the source; one burnout removes only that branch, others stay lit.](../images/21-circuits-and-dc-instruments-fig-01.png)
*Figure 21.1 — Christmas Lights — Why Old Strings Died Together (Series), New Ones Don't (Parallel)*

An incandescent bulb filament is interesting: it starts cold (resistance $\sim 10 \Omega$) and heats up dramatically under current, reaching resistance $\sim 100 \Omega$ when glowing. The cold surge of current (twelve times the steady-state value) lasts only until the filament heats up, typically a few milliseconds. This is why incandescent bulbs often fail at the moment of switching on — the cold-surge stress, repeated over thousands of switch cycles, eventually fractures the filament.

For every introductory problem in this chapter, treat resistors as ohmic unless explicitly told otherwise. The nonlinear world is real and important; it is just not the starting point.

### The toaster heating element

A 1500 W toaster runs at 120 V. The operating current: $I = P/V = 1500/120 = 12.5 \text{ A}$. The resistance: $R = V/I = 120/12.5 = 9.6 \Omega$. The element is nichrome wire with cross-section $A = 5 \times 10^{-7} \text{ m}^2$. How long is it?

$$L = \frac{RA}{\rho} = \frac{(9.6)(5 \times 10^{-7})}{1.0 \times 10^{-6}} = 4.8 \text{ m}.$$

Almost five meters of nichrome wire, coiled to fit inside a box you hold in your hand. You can verify this by looking down into the toaster slots: the tightly coiled element is exactly what $4.8 \text{ m}$ looks like when wound into a compact form.

---

## Power, AC, and the practical grid

When current $I$ flows through a resistor $R$ under voltage $V$, energy is dissipated as heat. The **power** dissipated is:

$$P = IV.$$

Substituting Ohm's law gives two equivalent forms:

$$P = I^2 R = \frac{V^2}{R}.$$

Use whichever form has the variables you know. For the toaster: $P = IV = (12.5)(120) = 1500 \text{ W}$; $P = I^2R = (12.5)^2(9.6) = 1500 \text{ W}$; $P = V^2/R = 120^2/9.6 = 1500 \text{ W}$. All consistent — this is just energy conservation restated in rate form.

The energy dissipated in time $t$ is $E = Pt$. A 1500 W toaster running for one hour uses $1.5 \text{ kWh}$ — which at \$0.15/kWh costs 22 cents.

### AC and the grid

On September 4, 1882, Thomas Edison threw the switch at Pearl Street Station in lower Manhattan — the world's first commercial power station. It supplied DC at 110 V to about 80 customers within half a mile. The problem: DC cannot be efficiently transmitted over long distances.

Power loss in a transmission line goes as $I^2 R$. To deliver a fixed power $P = IV$ over long distances, you want to minimize $I$ — which means maximizing $V$. But DC voltage at the time could not be stepped up or down. Edison's stations had to be within a mile of their customers.

George Westinghouse and Nikola Tesla championed alternating current (AC) instead, because AC voltages can be stepped up by transformers (Chapter 23) for transmission and stepped back down for use. The "War of Currents" of the 1880s ended with AC dominant. Every wall outlet in your home is AC at 60 Hz (North America) or 50 Hz (most of the rest of the world).

For power calculations, AC uses the **root-mean-square** (RMS) voltage and current. AC voltage varies sinusoidally: $V(t) = V_0 \sin(2\pi f t)$. The time-average power in a resistor is

$$\bar{P} = \frac{V_\text{RMS}^2}{R}, \quad \text{where} \quad V_\text{RMS} = \frac{V_0}{\sqrt{2}}.$$

The "120 V" printed on every US appliance is the RMS value. The peak is $120\sqrt{2} \approx 170 \text{ V}$. The RMS convention is a mathematical device that makes AC and DC power formulas look identical: a 1500 W AC toaster dissipates exactly the same average power as a 1500 W DC heater of the same resistance.

### Why high voltage?

The modern grid uses transmission voltages of 115 kV to 765 kV. The reason is $I^2R$. A 200 km line with resistance $10 \Omega$ carrying 1 GW of power at 110 kV requires current $I = P/V = 10^9/1.1 \times 10^5 \approx 9{,}100 \text{ A}$. Power lost as heat in the line: $I^2R = (9{,}100)^2 \times 10 \approx 828 \text{ MW}$ — 83% of the power delivered, gone as line heat. Transmit the same 1 GW at 500 kV: $I = 2{,}000 \text{ A}$, line loss = $(2{,}000)^2 \times 10 = 40 \text{ MW}$ — about 4%. High voltage is not primarily about safety or insulation; it is about minimizing waste in transmission.

<!-- → [INFOGRAPHIC: power transmission efficiency comparison — two scenarios side by side, both delivering 1 GW over 200 km with 10 Ω line resistance: (1) transmission at 110 kV: I = 9,100 A, line loss 828 MW (83% wasted); (2) transmission at 500 kV: I = 2,000 A, line loss 40 MW (4% wasted); student should see that doubling voltage quadruples efficiency improvement because loss goes as I² = (P/V)²] -->

### Safety

The power formula also governs what happens to a person who touches a live wire. Human skin resistance varies enormously with moisture and contact:

Dry skin, light contact: $\sim 10^5 \Omega$. A 120 V outlet drives $I = 120/10^5 = 1.2 \text{ mA}$ — perceptible but not dangerous.

Wet skin, firm contact: $\sim 10^3 \Omega$. The same outlet drives $\sim 120 \text{ mA}$ — lethal. Ventricular fibrillation can occur at 50–100 mA.

Submerged in water: as low as $\sim 100 \Omega$. Lethal currents at ordinary voltages.

The voltage is the same. The resistance — set by skin moisture and contact area — determines whether you live or die. This is why bathroom outlets require GFCI (ground fault circuit interrupter) protection, which cuts power within milliseconds if current leaks through an unexpected path.

---

## The three ideas as one equation

Current, resistance, and power all flow from two equations:

$$V = IR \quad \text{(Ohm's law)}$$
$$P = IV.$$

From these, substituting one into the other, you get every relationship in this chapter. Current $I = V/R$. Power $P = V^2/R = I^2R$. Energy $E = Pt$. Resistance $R = \rho L/A$ links those macroscopic quantities to the material and geometry.

The marble-pipe metaphor that opened the chapter is one face of this. The signal moves at near the speed of light because an electromagnetic wave propagating along the wire surface adjusts the field at every point essentially simultaneously. The individual electrons drift at millimeters per second because each one collides with the lattice roughly $10^{14}$ times per second and can only accumulate a tiny net velocity in the field direction between collisions. Both are captured in $I = nqAv_d$ — the signal speed shows up in how fast the field is established; the drift velocity shows up in $v_d$.

A USB-C charger delivering 5 V at 3 A provides $P = IV = 15 \text{ W}$ to your phone. At the wall (120 V AC), that same 15 W of output (assuming 90% efficiency) requires $P_\text{in} = 15/0.90 \approx 16.7 \text{ W}$, drawing $I = 16.7/120 \approx 0.14 \text{ A}$ from the outlet. The current inside the phone (3 A at 5 V) is twenty times larger than the current at the wall outlet (0.14 A at 120 V), because $P = IV$ requires current to be inversely proportional to voltage at fixed power. The high-voltage/low-current side has thin wires; the low-voltage/high-current side needs the heavier cable. Same equation, different regimes of the same network.

Scale that up by $10^{10}$ and you have the grid: 1 GW at 500 kV, $I = 2{,}000 \text{ A}$ in the transmission line; 1 GW delivered at 120 V to end users would require $I = 8.3 \times 10^6 \text{ A}$ — a current impossible to carry in any cable. The engineering of the entire electrical grid is an application of $P = IV$.

---

## Exercises

### Warm-up

**20.1** *(LO 1)* A current of $3.0 \text{ A}$ flows through a wire for $45 \text{ s}$. (a) How much charge passes a given cross-section? (b) How many electrons does that represent?

**20.2** *(LO 3)* A resistor has $R = 15 \Omega$. (a) What current flows when $9.0 \text{ V}$ is applied? (b) What voltage would drive $0.50 \text{ A}$ through the same resistor?

**20.3** *(LO 4)* A copper wire ($\rho = 1.72 \times 10^{-8} \Omega\cdot\text{m}$) is $8.0 \text{ m}$ long with cross-section $2.0 \times 10^{-6} \text{ m}^2$. (a) Compute its resistance. (b) If the wire were twice as long and half as thick, what would the resistance be?

**20.4** *(LO 6)* A 75 W light bulb runs at 120 V. Compute: (a) current drawn; (b) resistance; (c) energy used in 8 hours; (d) cost at \$0.15/kWh.

### Application

**20.5** *(LO 3, 6)* A hair dryer is rated at 1{,}875 W at 120 V. (a) What current does it draw? (b) What is its resistance when operating? (c) Will it trip a 15-A circuit breaker?

**20.6** *(LO 2)* A copper wire ($n = 8.5 \times 10^{28}/\text{m}^3$) with cross-section $A = 5.0 \times 10^{-6} \text{ m}^2$ carries $5.0 \text{ A}$. (a) Compute the drift velocity. (b) At this drift velocity, how long would it take one electron to travel $1.0 \text{ m}$? (c) In contrast, at what fraction of the speed of light does the signal travel?

**20.7** *(LO 4, 5)* A nichrome heating element has cold resistance $R_0 = 20 \Omega$ at $20°\text{C}$. $\alpha_\text{Ni} \approx 4 \times 10^{-4}/°\text{C}$. When operating at $900°\text{C}$: (a) what is the hot resistance? (b) If powered by 120 V, what current flows at cold start vs. at operating temperature? (c) What does the ratio tell you about the startup surge?

**20.8** *(LO 6, 7)* A US wall outlet is rated at $V_\text{RMS} = 120 \text{ V}$ AC. (a) What is the peak voltage? (b) A $60 \Omega$ resistor is connected. Compute: peak current, RMS current, average power, and peak instantaneous power. (c) What would the DC voltage need to be to produce the same average power?

### Synthesis

**20.9** *(LO 4, 6)* The same 1{,}500 W toaster designed for 120 V US outlets is plugged into a 240 V outlet in Europe without an adapter. (a) What current flows? (b) What power is dissipated? (c) What happens to the toaster? (d) What resistance would the toaster need to operate at its rated power on 240 V?

**20.10** *(LO 6, 7)* A power transmission line carries 500 MW of power over 300 km at 345 kV. The line has resistance $0.05 \Omega/\text{km}$. (a) Compute the current in the line. (b) Compute the total resistance of the line. (c) Compute the power lost as heat. (d) What fraction of the transmitted power is lost? (e) How would the loss change if the same power were transmitted at 138 kV?

**20.11** *(LO 3, 5)* The $V$-$I$ characteristic of a diode is approximately $I = I_0(e^{V/V_T} - 1)$ where $I_0 = 10^{-12} \text{ A}$ and $V_T = 0.026 \text{ V}$ at room temperature. (a) Compute the current at $V = 0.3 \text{ V}$, $0.5 \text{ V}$, $0.7 \text{ V}$. (b) Plot (by computing three points) the $V$-$I$ curve and comment on whether it is ohmic. (c) What is the "effective resistance" $V/I$ at each voltage? Is it constant?

### Challenge

**20.12** *(LO 4, 5, beyond chapter)* When you flip a light switch, explain why the bulb doesn't immediately burn out from the cold-filament current surge. Given cold resistance $\sim 10 \Omega$ and hot resistance $\sim 100 \Omega$ at 120 V: (a) compute the cold-start current and power; (b) compute the steady-state current and power; (c) the surge lasts roughly $0.1 \text{ s}$ — estimate the energy deposited in that time; (d) explain why this energy is survivable (hint: consider the thermal mass of the filament and its temperature rise).

**20.13** *(LO 4, beyond chapter)* A 10 m long, 14-gauge copper wire (diameter $1.63 \text{ mm}$, so $A = \pi(0.815 \times 10^{-3})^2 \approx 2.08 \times 10^{-6} \text{ m}^2$, $\rho_{Cu} = 1.72 \times 10^{-8} \Omega\cdot\text{m}$) is used as an extension cord. (a) Compute its resistance. (b) If a 1{,}500 W toaster is plugged in (drawing 12.5 A), compute the voltage drop across the cord. (c) What fraction of the 120 V supply is lost in the cord? (d) What power is dissipated as heat in the cord? (e) At what length would the cord drop more than 5% of the supply voltage?

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

**Why this chapter matters.** Every electrical device in your life runs on the relationships in this chapter. The wattage of an appliance, the current draw of a charger, the resistance of a heating element, the reason the grid runs at hundreds of kilovolts — all follow from $V = IR$ and $P = IV$.

---

## ↳ Dig Deeper — Why drift velocity is slow but signals are fast

*The marble-pipe analogy is useful but imprecise. The actual mechanism involves electromagnetic fields propagating at near-light-speed along the surface of the conductor, while individual electrons scatter on picosecond timescales and accumulate tiny average drift velocities.*

**Prompt:**
> Explain the gap between drift velocity (~10⁻⁵ m/s) and signal speed (~2×10⁸ m/s) in electrical conductors. Walk through: (1) the random thermal speed of free electrons in copper (~10⁶ m/s), (2) the mean free path and collision frequency, (3) how an electric field produces a small drift on top of this random motion, (4) how the field itself propagates as a transverse electromagnetic wave guided by the conductor, adjusting surface charges along the entire wire essentially simultaneously. End with one sentence on why this is the conceptual foundation for understanding transmission lines and high-frequency electronics.

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
> Explain why long-distance electrical transmission uses high voltage. Compute power loss $P_\text{loss} = I^2R$ for a fixed delivered power $P = IV$ at two different transmission voltages — say 110 kV and 500 kV — over a 200 km line with 10 Ω resistance. Show numerically how the losses differ. Then explain why transformers make this possible for AC but not for DC — and add one sentence on why high-voltage DC (HVDC) has become viable in recent decades for specific applications (long undersea cables, asynchronous grid connections).

**What to do with the output:** Save it. The transformer/transmission story is the engineering reason the modern electrical grid exists in its current form. It sets up Chapter 23's electromagnetic induction.

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
