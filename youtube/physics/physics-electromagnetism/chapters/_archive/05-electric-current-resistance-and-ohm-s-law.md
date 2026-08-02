# Chapter 5 — Electric Current, Resistance, and Ohm's Law

**Suggested titles**

1. Electric Current, Resistance, and Ohm's Law
2. Why a Toaster Drops 120 V Across an 11-Ohm Wire
3. Electrons Crawl, Signals Race: The Two Speeds of Electricity

**TL;DR.** Electric current is the rate of charge flow, $I = Q/t$, measured in amperes (1 A = 1 C/s). When a voltage $V$ is applied across a resistive material, current flows according to Ohm's law $V = IR$, where $R$ is the resistance in ohms ($\Omega$). Power dissipated by a resistor is $P = IV = I^2 R = V^2/R$. By the end of the chapter you can compute current, voltage, resistance, and power for any single resistor or wire, distinguish ohmic from nonohmic materials, and reason about why electrical signals travel near the speed of light while individual electrons crawl at millimeters per second.

---

## Two speeds of electricity in one toaster

Push down the lever on a kitchen toaster and the bread starts heating within milliseconds. The orange glow of the heating element comes on essentially instantly. Yet the *individual electrons* in the heating element wire are drifting along at about 0.0001 meters per second — about a tenth of a millimeter per second. At that pace it would take a single electron three hours to crawl from the wall plug to the heating element.

This is one of the great pedagogical puzzles of electricity. If electrons move so slowly, why does the toaster respond so fast?

The answer: the *signal* moves at nearly the speed of light, while the individual *carriers* drift glacially. When you close the switch, the electric field that pushes electrons propagates through the wire at $\sim 2 \times 10^8$ m/s. Every electron in the wire starts drifting almost simultaneously — they don't have to travel from the switch to the heater; they just have to start moving where they already are. Like opening a long pipe of marbles: the marble at the far end pops out essentially at the same instant you push at the near end, even though no individual marble traveled the length of the pipe.

This chapter is about pinning that down — what current really is, what resistance really is, what Ohm's law really claims and where it fails, and what makes a 1500-watt toaster different from a 1500-watt hairdryer at the level of charges flowing through metal.

**Learning objectives.** By the end of this chapter you should be able to:

1. Define electric current $I = Q/t$, units ampere (A) = C/s, and identify the conventional vs. electron flow direction.
2. Compute drift velocity from $I = nqAv_d$ where $n$ is charge carrier density, $A$ is cross-section, $v_d$ is drift velocity.
3. State and apply Ohm's law: $V = IR$ for ohmic materials.
4. Compute resistance from material properties: $R = \rho L/A$, where $\rho$ is resistivity.
5. Identify ohmic vs. nonohmic devices (resistors are ohmic; diodes, semiconductors, light bulb filaments are not).
6. Compute electric power dissipated: $P = IV = I^2R = V^2/R$.
7. Distinguish DC from AC and recognize where each is used.
8. Reason about the temperature dependence of resistance.

**Prerequisites.** Chapter 18 (charge), Chapter 19 (potential, voltage). Algebra.

**Why this chapter matters.** Every electrical device runs on the relationships in this chapter. The wattage of an appliance, the current draw of a phone charger, the resistance of a heating element, the power dissipated as heat — all are computed from $V$, $I$, $R$, and the relations among them. Understanding *why* Ohm's law works (and why some devices break it) sets up everything in semiconductor and electronics engineering.

---

## Concept 1 — Current and drift velocity

### The 1820 Copenhagen lecture demonstration

In April 1820, the Danish physicist Hans Christian Ørsted was preparing a lecture demonstration at the University of Copenhagen. Tradition says he was about to show that current and magnetism were unrelated; the discovery he actually made was the opposite. He aligned a wire parallel to a magnetic compass needle, closed the circuit so that current flowed through the wire, and watched the compass needle deflect. Within hours, the news was traveling across Europe: electric current produces a magnetic field.

Ørsted's discovery launched electromagnetism. But for our purposes here, it also nailed down what *current* meant operationally. A magnetic compass deflected near a current-carrying wire told you, quantitatively, how much current was flowing — long before there were ammeters. Current was not a vague concept; it was a measurable physical quantity, with magnetic-needle-deflection as the first observable effect.

The unit named for André-Marie Ampère, who developed the mathematical theory in the 1820s, is the **ampere** (A). One ampere is one coulomb of charge passing a given cross-section per second. A typical USB charger delivers 1–2 A; a kitchen toaster draws about 12 A; a lightning bolt carries roughly 30,000 A for a millisecond.

### The mechanism — current defined

**Electric current** is the rate of flow of charge:

$$I = \frac{Q}{t},$$

with units 1 A = 1 C/s. Current is a scalar in introductory physics (it has a direction along the wire, but the wire constrains it to one degree of freedom).

Two conventions for direction:

**Conventional current** flows from + terminal of the battery through the external circuit to the − terminal. This is the direction *positive* charges would move.

**Electron flow** is opposite — electrons (which carry negative charge) actually move from − to +.

The conventions are equivalent for almost all purposes. Conventional current was established by Franklin before electrons were discovered, and we keep it because it makes signs work out cleanly in most equations. When we write $I$ in formulas, we mean conventional current.

### Drift velocity

The crawl-versus-signal puzzle has a quantitative answer. The current is

$$I = n q A v_d,$$

where $n$ is the number density of charge carriers (carriers per m³), $q$ is the charge per carrier (typically $e$ for electrons), $A$ is the cross-sectional area of the wire, and $v_d$ is the **drift velocity** — the average speed of carriers along the wire.

For copper wire carrying 1 A, with cross-section $A = 3 \times 10^{-6}$ m² (typical 14-gauge wire) and free electron density $n \approx 8.5 \times 10^{28}$ /m³:

$$v_d = \frac{I}{nqA} = \frac{1}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(3 \times 10^{-6})} \approx 2.5 \times 10^{-5} \text{ m/s}.$$

Twenty-five micrometers per second. About the speed at which fingernails grow. Yet the toaster heats up instantly because every electron in the wire is drifting at this rate simultaneously — the signal that says "start drifting" propagates at nearly the speed of light, but the individual carriers crawl.

### The trade-off

Defining current as a scalar flow trades **directional vector information for arithmetic simplicity.** The actual flow of electrons inside a wire is a complicated three-dimensional motion (random thermal motion plus a tiny drift). Treating it as a single scalar quantity $I$ along the wire is a brilliant simplification — exact for steady-state DC in a wire — but it hides the microscopic complexity.

### Worked example — current in a household lamp

A 60 W incandescent bulb runs at 120 V. (a) What current does it draw? (b) How many electrons per second pass through the filament?

**(a)** From $P = IV$, $I = P/V = 60/120 = 0.50$ A.

**(b)** Charge per second = 0.50 C. Number of electrons per second = $0.50/(1.6 \times 10^{-19}) \approx 3.1 \times 10^{18}$.

Three quintillion electrons per second pass through the filament. Each individual electron drifts very slowly, but collectively they carry half a coulomb of charge per second.

**Sanity check.** US household circuits are typically 15-amp breakers; a 60 W bulb at 0.5 A is well within capacity. A typical room with several lamps and a TV draws maybe 5 A total, leaving headroom for a refrigerator or microwave on the same circuit.

### Common misconceptions

- *"Current flows out of the battery and gets used up by the bulb."* No — current flows in a loop. Every electron that enters one terminal of the battery exits the other. Energy is what gets dissipated, not charge.
- *"Higher voltage means more current."* Only if the resistance is fixed. The same 12 V battery applied to a thick wire (low R) drives much more current than across a thin wire (high R).
- *"AC is dangerous and DC is safe."* Both can kill at hospital-cardiac currents. AC is more disruptive to heart rhythm at lower currents (around 50 mA at 60 Hz), but DC of similar magnitude is also lethal.

↳ **Dig Deeper — Why drift velocity is so slow but signals are fast**

*The astonishing slowness of drift velocity in metallic conductors is one of the most counterintuitive facts in physics. The chapter's marble-in-pipe analogy gets the basic idea, but the full picture involves electromagnetic fields propagating at near light speed while individual carriers diffuse and scatter on the order of picoseconds.*

**Prompt:**
> Explain the dramatic gap between drift velocity ($\sim 10^{-5}$ m/s in typical copper wires) and signal speed ($\sim 2 \times 10^8$ m/s). Walk me through: (1) the random thermal motion of free electrons in copper at $\sim 10^6$ m/s, (2) the much smaller drift in response to an applied field, (3) the mechanism by which an electric field set up at one end of a wire propagates through the wire at near-light-speed (it propagates as a transverse electromagnetic wave outside the conductor, with the conductor's surface charges adjusting to maintain the field at every interior point). End with one sentence on why this is a textbook example of how a "macroscopic" property (current flow) emerges from very different microscopic dynamics.

**What to do with the output:** Save it. The signal-vs-carrier distinction is the conceptual key to understanding transmission lines, antennas, and high-frequency electronics.

---

## Concept 2 — Resistance and Ohm's law

### Georg Ohm's wire experiments, Cologne 1825

In 1825, Georg Simon Ohm — a high-school physics teacher in Cologne, working with homemade equipment — set up an experiment that would consume four years and earn him a doctorate. He took wires of different lengths and thicknesses, applied controlled voltages from a Volta-pile battery, and measured the resulting current. His instruments were primitive (he used the deflection of a magnetic-needle galvanometer based on Ørsted's discovery), but his patience was extraordinary.

The pattern he found, eventually published in 1827:

$$I = \frac{V}{R},$$

usually written

$$V = IR.$$

For a wide range of metallic conductors, current is *proportional* to applied voltage. The constant of proportionality, $1/R$, characterizes the wire. $R$ is the **resistance**, units **ohms** ($\Omega$, with $1 \text{ }\Omega = 1 \text{ V/A}$).

Ohm's discovery was poorly received in Germany — too empirical for the dominant idealistic philosophy of the time — and he spent six years doing menial teaching jobs before being recognized. His name is on the law that runs every electrical engineering textbook today.

### The mechanism — resistance from material properties

Resistance depends on geometry and material:

$$R = \frac{\rho L}{A},$$

where $L$ is the length of the conductor, $A$ is its cross-section, and $\rho$ is the **resistivity** of the material (units Ω·m). A short table:

| Material | Resistivity (Ω·m) at 20 °C |
|---|---|
| Silver | $1.59 \times 10^{-8}$ |
| Copper | $1.72 \times 10^{-8}$ |
| Aluminum | $2.65 \times 10^{-8}$ |
| Iron | $9.71 \times 10^{-8}$ |
| Constantan (alloy) | $4.9 \times 10^{-7}$ |
| Nichrome (heating element) | $1.0 \times 10^{-6}$ |
| Carbon | $\sim 3.5 \times 10^{-5}$ |
| Silicon (pure) | $640$ |
| Glass | $10^{10}$ to $10^{14}$ |
| Quartz | $\sim 7.5 \times 10^{17}$ |

Notice the stunning range — 26 orders of magnitude from quartz to silver. The choice of conductor or insulator is, at root, a choice of $\rho$.

Wires used in household wiring are copper because it's the second-best conductor (silver is better but much more expensive). Heating elements are nichrome (an alloy of nickel and chromium) because its resistivity is high enough to dissipate substantial power at line voltages. Insulators are typically rubber, plastic, or glass, with resistivities high enough that essentially no current leaks across them.

### Temperature dependence

Resistance of metals *increases* with temperature:

$$R = R_0 [1 + \alpha (T - T_0)],$$

where $\alpha$ is the temperature coefficient of resistance (about $4 \times 10^{-3}$ per °C for copper). At higher temperature, lattice atoms vibrate more, scattering electrons more often and reducing drift velocity for the same field. A toaster's nichrome wire, when red-hot at ~1100 °C, has resistance about three times its room-temperature value.

Semiconductors *decrease* in resistance with temperature (heat creates more free charge carriers, dominating the lattice-scattering effect). This is why transistors run hotter as they pass more current — and why they can thermally run away if not properly cooled.

### Ohmic vs. nonohmic

Materials that obey $V = IR$ with constant $R$ over the operating range are **ohmic**. Most metallic resistors at constant temperature.

Materials whose $V$-vs-$I$ curve is nonlinear are **nonohmic**:

- Diodes pass current in one direction only; nonlinear in both regions.
- Semiconductors generally have temperature-dependent and field-dependent resistance.
- Incandescent bulb filaments heat up dramatically when current flows; their resistance triples between cold and hot, so the cold-resistance is a poor predictor of operating current.
- Neon tubes and gas-discharge lamps have a striking voltage threshold below which no current flows.

For any introductory problem, treat resistors as ohmic unless explicitly told otherwise.

### The trade-off

Ohm's law trades **range of validity for linear simplicity.** The law holds over an enormous range of metallic materials at near-room temperature, but breaks for semiconductors, high-frequency AC in conductors (skin effect), nonlinear devices (diodes), and at extreme fields. The simplification is essential pedagogically and predictively for the regimes where it works.

### Worked example — toaster heating element

A 1500 W toaster runs at 120 V. (a) Compute the operating current. (b) Compute the resistance. (c) The element is nichrome wire with cross-section $A = 5 \times 10^{-7}$ m² (about 0.4 mm²). How long is the wire?

**(a)** $I = P/V = 1500/120 = 12.5$ A.

**(b)** $R = V/I = 120/12.5 = 9.6$ Ω.

**(c)** $L = RA/\rho = (9.6)(5 \times 10^{-7})/(1.0 \times 10^{-6}) = 4.8$ m.

About 5 meters of nichrome wire, coiled to fit inside the toaster body. This matches the visible coiled element you see when you look down into a slot.

**Sanity check.** Household toasters are typically 800–1800 W. Our 1500 W is in the middle of that range. The 12.5 A draw is below a 15-A breaker but close enough that you can't run a toaster and microwave on the same circuit without tripping it.

### Common misconceptions

- *"All materials follow Ohm's law."* No — semiconductors and nonlinear devices don't. Ohm's law is excellent for metals at constant temperature.
- *"Higher resistance always means hotter."* It depends on whether the resistor is in series or parallel with other components. In parallel with constant voltage, lower R means higher current means higher dissipated power.
- *"Resistance is determined entirely by the material."* Geometry matters too — long wires have higher R, thicker wires have lower R, even of the same material.

↳ **Dig Deeper — Superconductivity, the limit case where R → 0**

*Some materials, when cooled below a critical temperature $T_c$, have *exactly* zero resistance. They are superconductors. Discovered by Heike Kamerlingh Onnes in 1911 in mercury at 4.2 K, this is a quantum-mechanical effect with no classical analog. It is now the basis of MRI machines, particle accelerator magnets, and quantum computers.*

**Prompt:**
> Explain superconductivity: that some materials below a critical temperature $T_c$ have *exactly* zero resistance. Walk through the historical discovery (Heike Kamerlingh Onnes, mercury at 4.2 K, 1911), then briefly outline the BCS theory (electrons pair via lattice phonon interactions, forming Cooper pairs that move without scattering). Note the existence of "high-temperature" superconductors (cuprates, $T_c$ up to ~135 K at ambient pressure; recently up to ~250 K under high pressure for hydrogen-rich compounds). End with one sentence on the practical implications: MRI machines, maglev trains, particle accelerators, the dream of room-temperature superconductors.

**What to do with the output:** Save it. Superconductivity is one of the most beautiful applications of quantum mechanics to a macroscopic system. You will revisit it in any condensed-matter or materials-science course.

---

## Concept 3 — Power, AC vs DC, and practical electricity

### Edison's 1882 Pearl Street station

On September 4, 1882, Thomas Edison threw the switch at Pearl Street Station in lower Manhattan — the world's first commercial electric power station. It supplied direct current (DC) at 110 V to about 80 customers in a roughly half-square-mile area, lighting up office buildings and the New York Times newspaper offices. By 1886, Edison's company had similar stations in dozens of cities.

The catch: DC at low voltage cannot be efficiently transmitted over long distances, because power loss in the wires goes as $I^2 R$, and reducing $I$ requires raising $V$, but DC voltage cannot easily be transformed up or down. Edison's stations had to be located within about a mile of their customers.

George Westinghouse, working with Nikola Tesla, championed alternating current (AC) instead, because AC voltages can be stepped up by transformers (Chapter 23) for transmission and stepped back down for use. The "war of currents" of the 1880s ended with AC dominant — by 1900, virtually all new power stations were AC. Today, every wall outlet in your house is AC at 60 Hz (in North America) or 50 Hz (most of the rest of the world).

For our purposes here, the equations of power and energy work essentially the same for both — with the caveat that for AC we typically use the *root-mean-square* (RMS) voltage and current, which give the right average power.

### The mechanism — power dissipated in a resistor

The power dissipated when current $I$ flows through a resistor $R$ across voltage $V$ is

$$P = IV.$$

Substituting Ohm's law gives two equivalent forms:

$$P = I^2 R = \frac{V^2}{R}.$$

Use whichever form has the variables you know.

For a 1500 W toaster at 120 V drawing 12.5 A: $P = IV = 12.5 \times 120 = 1500$ W. Or: $P = I^2 R = (12.5)^2 (9.6) = 1500$ W. Or: $P = V^2/R = 120^2/9.6 = 1500$ W. All consistent.

The energy dissipated as heat in time $t$ is

$$E = Pt.$$

Your electricity bill measures cumulative energy in kilowatt-hours (kWh): 1 kWh = 3.6 MJ. A 1500 W toaster running for one hour uses 1.5 kWh. At about $0.15/kWh, that's 22 cents per hour of toasting.

### AC and RMS values

AC voltage varies sinusoidally:

$$V(t) = V_0 \sin(2\pi f t),$$

where $V_0$ is the peak amplitude and $f$ is the frequency (60 Hz in US). Current through a pure resistor follows the same sine wave.

The instantaneous power $P(t) = V(t) I(t) = V_0^2 \sin^2(2\pi f t) / R$ varies in time. Its time-average is

$$\bar{P} = \frac{V_0^2}{2R} = \frac{V_\text{RMS}^2}{R},$$

where $V_\text{RMS} = V_0/\sqrt{2}$ is the **root-mean-square** voltage. When you read "120 V" on a US wall outlet, that's the RMS value; the peak is $120 \sqrt{2} \approx 170$ V.

This convention exists so that AC and DC formulas look identical: a 1500 W AC heater dissipates the same average power as a 1500 W DC heater of the same resistance. The RMS value is a mathematical convenience that lets you ignore the underlying sinusoidal time dependence for power calculations.

### Practical electricity hazards

The combination of $V$, $I$, and $R$ governs what current flows through a person who touches a live wire. Skin resistance varies enormously with moisture and contact area:

- Dry skin, light contact: ~$10^5$ Ω. A 120 V wall outlet drives current $I = V/R \approx 1$ mA — perceptible but not dangerous.
- Wet skin, firm contact: ~$10^3$ Ω. The same 120 V drives $\sim 100$ mA — into the lethal range (ventricular fibrillation).
- Submerged in water: as low as $\sim 100$ Ω. Lethal currents at much lower voltage.

This is why bathrooms have GFCI (ground fault circuit interrupter) outlets and why "don't use the toaster while standing in the tub" is more than a cliché. The voltage is the same; the path through the body changes.

### The trade-off

Practical electrical engineering trades **safety and efficiency through high-voltage transmission and low-voltage distribution.** Long-distance transmission at hundreds of kilovolts minimizes $I^2 R$ losses; local distribution steps down to 240 V or 120 V for human-safe consumption. Every step requires transformers (Chapter 23) and creates a small efficiency loss — about 5% of generated electricity is lost in transmission and distribution combined.

### Worked example — running cost of a refrigerator

A typical household refrigerator runs on 120 V, draws 1.5 A average current (cycling on and off through the day, but averaging this over time), and runs continuously. (a) Average power. (b) Annual energy use in kWh. (c) Annual cost at $0.15/kWh.

**(a)** $P = IV = 1.5 \times 120 = 180$ W.

**(b)** Annual energy: $180 \text{ W} \times 8760 \text{ h/yr} = 1.58 \times 10^6 \text{ Wh} \approx 1580 \text{ kWh}$.

**(c)** Annual cost: $1580 \times 0.15 = $237.

That is about right for an older refrigerator. New ENERGY STAR units can use ~400 kWh/yr (about $60/yr).

**Sanity check.** US households average about 10,000 kWh/yr in electricity. A refrigerator at 1500 kWh/yr is about 15% of that — consistent with published energy audits.

### Common misconceptions

- *"AC is more dangerous than DC."* AC at 60 Hz is more disruptive to heart rhythm at low currents (~50 mA), but DC at higher currents is also lethal. AC is also easier to step up and down, which is why we use it; it's not categorically more dangerous.
- *"A bigger wire is always safer."* It's safer for *current capacity*, but a long thin wire carrying small current is fine. Ampacity (max safe current) depends on geometry and cooling, not just material.
- *"Power and energy are the same thing."* Power is rate of energy use ($W = J/s$). Energy is the cumulative quantity ($J$ or $kWh$). A 100 W bulb running for 10 hours uses the same energy as a 1000 W toaster running for 1 hour — both 1 kWh.

↳ **Dig Deeper — The transformer and why long-distance power transmission requires high voltage**

*The reason your house gets electricity from a power plant 100 km away — instead of needing a power plant in your neighborhood like Edison's original system — is the transformer. Transformers can step AC voltage up or down with very high efficiency, and this lets the grid use 500-kilovolt transmission lines while delivering 240 V to your house.*

**Prompt:**
> Explain why long-distance electrical power transmission uses high voltage. Compute the power loss in a transmission line as $P_\text{loss} = I^2 R$, then show how, for delivering a fixed power $P = IV$ to the customer, raising $V$ allows reducing $I$ — which reduces $I^2 R$ losses dramatically. Use a sample calculation: 1 GW delivered over a 200 km line with resistance ~10 Ω, comparing transmission at 110 kV vs. 500 kV. Then briefly explain how transformers make the high-low voltage stepping possible, and why this only works for AC (not DC). End with one sentence on why high-voltage DC (HVDC) transmission has become competitive in the past 30 years (long undersea cables, asynchronous grid interconnects).

**What to do with the output:** Save it. The transformer / transmission story is the engineering reason the modern electrical grid exists in its current form, and it sets up Chapter 23.

---

## Synthesis — current, resistance, power, all from $V = IR$

Step back. Three concepts:

1. **Current is rate of charge flow.** $I = Q/t$, units A. Drift velocity is glacial; signals travel at near light speed.

2. **Ohm's law and resistance.** $V = IR$ for ohmic materials. Resistance from material properties: $R = \rho L/A$. Some materials (semiconductors, diodes) are nonohmic.

3. **Power dissipated in a resistor.** $P = IV = I^2R = V^2/R$. AC uses RMS values for power calculations. The grid distributes high voltage to minimize $I^2R$ losses, then steps down for safe use.

### A worked example combining all three concepts — a phone charger

A standard USB-C phone charger delivers 5 V at up to 3 A. (a) What is the equivalent resistance of the phone (treating it as ohmic, average load)? (b) What is the power delivered? (c) If the wall outlet is 120 V AC, what current does the *charger* draw from the wall, assuming the charger is 90% efficient at AC-to-DC conversion?

**(a)** $R_\text{phone} = V/I = 5/3 \approx 1.67$ Ω.

**(b)** $P_\text{out} = IV = 3 \times 5 = 15$ W.

**(c)** Power drawn from wall: $P_\text{in} = P_\text{out}/\eta = 15/0.90 \approx 16.7$ W. Current: $I = P/V = 16.7/120 \approx 0.14$ A = 140 mA.

The current flowing into the back of your phone (3 A at 5 V) is much larger than the current flowing into the charger from the wall (0.14 A at 120 V). Both deliver about 15 W, by $P = IV$. The high-voltage / low-current side has small wires; the low-voltage / high-current side needs the heavier USB-C cable to handle 3 A safely.

**Scale shift.** The same $P = IV$ relation, scaled up, governs a transmission line carrying 1 GW at 500 kV (current = 2 kA) vs. delivering the same power at 120 V (current = 8.3 MA — impossible to handle in a wire). The grid is engineered around exactly this scaling.

---

## Exercises

### Warm-up

**20.1** *(LO 1)* A current of 2.0 A flows through a wire for 30 s. How much charge passes a given cross-section?

**20.2** *(LO 3)* A wire has resistance 24 Ω. What current flows when 12 V is applied?

**20.3** *(LO 4)* A copper wire 5.0 m long has cross-section $1.0 \times 10^{-6}$ m². Compute its resistance. ($\rho_{Cu} = 1.72 \times 10^{-8}$ Ω·m.)

**20.4** *(LO 6)* A 100 W bulb runs at 120 V. Compute current, resistance, and energy used in 1 hour.

### Application

**20.5** *(LO 6)* A hair dryer rated at 1875 W runs at 120 V. (a) What current does it draw? (b) Will it trip a 15-A breaker?

**20.6** *(LO 1, 6)* The Tesla Model S has a battery rated at 100 kWh, with a typical operating voltage of 400 V. (a) Convert kWh to joules. (b) Estimate the total charge (in coulombs) that the battery can deliver at 400 V before depletion. (c) If you draw 100 kW (about 130 hp) for highway driving, how long before you need a charge?

**20.7** *(LO 4, 8)* A nichrome heating element has resistance 30 Ω at 20 °C. When operating, it reaches 800 °C. Estimate its hot resistance, given $\alpha_{Ni} \approx 4 \times 10^{-4}$ per °C.

**20.8** *(LO 6, 7)* A US AC wall outlet provides $V_\text{RMS} = 120$ V. (a) What is the peak voltage? (b) An incandescent bulb draws $I_\text{RMS} = 0.50$ A. Compute the peak power dissipated and the average power dissipated.

### Synthesis

**20.9** *(LO 4, 8)* The same 1500 W toaster gets used in a country with 240 V mains instead of 120 V. (a) What current would it draw if the resistance were unchanged? (b) What power would it dissipate? (c) Would this be safe?

**20.10** *(LO 1, 2)* In a copper wire, $n \approx 8.5 \times 10^{28}$ free electrons/m³, cross-section $5 \times 10^{-6}$ m², carrying 2 A current. Compute the drift velocity. Comment on its small magnitude.

**20.11** *(LO 6, beyond chapter)* Power loss in a transmission line: a 200 km line carries 1 GW at 500 kV (RMS). Total resistance of the line is ~10 Ω. (a) Compute the current. (b) Compute the power lost as heat. (c) Compute the percentage loss.

### Challenge

**20.12** *(LO 8, beyond chapter)* When you flip a light switch, why doesn't the light bulb explode in the first instant from the surge of current through its cold (low-resistance) filament? Compute, using approximate numbers: filament cold resistance 10 Ω; hot resistance 100 Ω. (a) Initial current at 120 V. (b) Initial power dissipated. (c) Why doesn't this damage the bulb? (Hint: how long does the surge last?)

**20.13** *(LO 4, 5, beyond chapter)* The resistivity of pure silicon ($\sim 640$ Ω·m) is enormous compared to a metal, but pure silicon is the basis of every semiconductor in your phone. Explain why this is not a contradiction — what does *doping* (introducing trace amounts of phosphorus or boron) do to the resistivity, and how does it allow silicon to function as a controllable conductor?

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
   - Coffee maker: current through the heating element when the carafe is on.
   - Marathon: current through a smartwatch chip.
   - Espresso machine: current draw of the pump motor.
   - Basketball: current through scoreboard LEDs.

2. Identify or estimate:
   (a) Voltage applied (V).
   (b) Current drawn (A).
   (c) Resistance (Ω) — compute via $R = V/I$ or look up.
   (d) Power dissipated (W) — compute via $P = IV$.
   (e) Energy consumed per use (J or kWh).

3. State your inputs, sources, and uncertainty.

4. Sanity check: does the power match the rated wattage of the device?

5. Estimate the cost of running this component for one hour, using $0.15/kWh.

6. Connect to Chapter 21 (Circuits), where we'll combine multiple resistors and voltage sources.

Save the output as logbook/chapter-20-current.md.
```

### What this produces

Your twentieth Logbook entry — a quantified current-and-power analysis.

### How to adapt this prompt

- *For phenomena with no obvious current*: every electronic device involves some current; if your phenomenon is non-electrical, pick a peripheral electrical aspect (lights, sensors, monitors).
- *For Claude Code:* If you have a power-monitor reading, plot power vs. time and integrate to get total energy.

### Connection to previous chapters

Builds on Chapter 19's voltage. Energy bookkeeping from Chapter 7 reappears.

### Preview of next chapter

Chapter 21 combines resistors, voltage sources, and capacitors into circuits with Kirchhoff's laws. The Chapter 21 LLM Exercise will analyze a multi-component circuit relevant to your phenomenon.

---

## Chapter summary

Electric current is the rate of charge flow; resistance limits it; power is the product of voltage and current. Three commitments:

1. **Current $I = Q/t$, ampere = C/s.** Drift velocity of carriers is millimeters per second; signal speed is near $c$.

2. **Ohm's law $V = IR$ for ohmic materials.** Resistance from $R = \rho L/A$. Resistivity spans 26 orders of magnitude across materials.

3. **Power dissipated $P = IV = I^2R = V^2/R$.** AC uses RMS values; the grid uses high voltage to minimize $I^2R$ transmission losses.

The one idea that matters most: **electrical signals travel near the speed of light, but the individual charges crawl.** This resolves the paradox of fast electrical response despite slow drift, and is the foundation of how transmission lines, antennas, and high-frequency electronics work.

The common mistake to watch for: **forgetting that Ohm's law assumes constant resistance.** Filaments, semiconductors, and diodes are not ohmic, and their $V$-$I$ curves require care.

---

## What would change my mind

The chapter argues that Ohm's law and the simple power formulas cover essentially all introductory current problems. The argument would need revision if a routine consumer-electronics problem (say, the current through a USB charger's switching power supply) were so dominated by nonlinear semiconductor behavior that the simple linear formulas gave wrong answers. They don't, for the average-power question; instantaneous behavior of switching supplies is genuinely complex but the time-averaged power balance still uses $P = IV$.

## Still puzzling

The deepest puzzle this chapter raises and partially resolves: *why is Ohm's law approximately linear over such a huge range of metallic materials?* The microscopic explanation involves electrons scattering off lattice vibrations (phonons) at a rate roughly proportional to temperature, with a mean free path roughly independent of field strength. This combination, derived in solid-state physics courses, gives $V$ proportional to $I$. But the quality of the approximation across so many materials and current ranges is genuinely impressive, and the deviations (in semiconductors, in superconductors, at very high fields) all signal physics beyond the simple Drude model.

---

## Connections forward

Chapter 21 builds **circuits** by combining resistors and capacitors with batteries, using Kirchhoff's voltage and current laws. Chapter 22 introduces **magnetism** — the magnetic field produced by currents and felt by moving charges. Chapter 23 introduces **electromagnetic induction**, the heart of generators, motors, and transformers — and explains why the electrical grid runs on AC. Chapter 24 reveals that electric and magnetic fields together propagate as waves at speed $c$. Every later chapter on electricity rests on the relationships between $V$, $I$, $R$, and $P$ you installed here.

---

**Tags:** electric-current, Ohms-law, resistance, power, drift-velocity

---

## AI Wayback Machine

**Georg Simon Ohm** published the law bearing his name in 1827 — establishing that current is proportional to voltage for ohmic materials. The book was so poorly received that he resigned his teaching position and only later was vindicated.

**Run this:**

```
Who was Georg Simon Ohm, and how does Ohm's law connect to the electric current and resistance we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Georg Ohm"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Ohm's original experiments demonstrating V = IR.
- Ask it about why Ohm's 1827 book was poorly received — and what changed.

What changes? What gets better? What gets worse?
