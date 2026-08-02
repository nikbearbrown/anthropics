# Chapter 7 — Circuits and DC Instruments

**Suggested titles**

1. Circuits and DC Instruments
2. Kirchhoff's Two Laws and the RC Time Constant
3. Why Christmas Lights Used to Fail Together (and Now Don't)

**TL;DR.** When resistors and voltage sources are connected in a closed loop, two simple bookkeeping rules — Kirchhoff's voltage and current laws — let you compute every current and voltage in the network. Resistors in series add ($R_\text{eq} = R_1 + R_2$); resistors in parallel combine reciprocally ($1/R_\text{eq} = 1/R_1 + 1/R_2$). Real batteries have **internal resistance** that drops the terminal voltage when current flows. RC circuits charge and discharge with characteristic time constant $\tau = RC$. Voltmeters and ammeters are themselves resistors, with deliberate values to minimize circuit disturbance.

---

## A string of incandescent Christmas lights, mid-1990s

Buy a string of old-style incandescent Christmas lights, the kind that used to disappear when one bulb burned out. Wire them up. Light the tree. A week later, one bulb dies. Half the string goes dark.

The reason: the bulbs were wired in **series** — every bulb in the same loop, current flowing through all of them in sequence. When one bulb's filament breaks, the loop is broken, and current stops everywhere. Cheap to manufacture (one wire run, one switch), painful to debug (which of fifty bulbs is the dead one?).

Modern LED Christmas lights are wired in **parallel** — every bulb has its own short branch off the main wire. When one fails, the others stay lit. Slightly more expensive to make, dramatically nicer to use.

The whole difference is in two equations. Resistors in series add their resistances. Resistors in parallel combine reciprocally. Once you have these two rules and Kirchhoff's two laws (charge conservation at each junction, voltage conservation around each loop), you can analyze any DC circuit. Then we add capacitors, time constants, real batteries with internal resistance, and the meters that measure all of this — and you have the foundation of practical electrical engineering.

**Learning objectives.** By the end of this chapter you should be able to:

1. Compute equivalent resistance for resistors in series ($R_\text{eq} = R_1 + R_2$) and parallel ($1/R_\text{eq} = 1/R_1 + 1/R_2$).
2. Apply Kirchhoff's junction rule (current in = current out) and loop rule (sum of voltage drops = 0) to multi-loop circuits.
3. Account for the **internal resistance** of a battery in computing terminal voltage and circuit current.
4. Compute the time constant $\tau = RC$ for an RC circuit and sketch the charging/discharging curves.
5. Identify and use voltmeters (high resistance, in parallel) and ammeters (low resistance, in series).
6. Reason about safety devices: fuses, circuit breakers, GFCI.

**Prerequisites.** Chapter 19 (capacitors), Chapter 20 (Ohm's law, current, resistance, power). Algebra; comfort with simultaneous equations.

**Why this chapter matters.** Every electronic device — phone, car, refrigerator, MRI machine — is at root a circuit. The two laws and the combination rules in this chapter are the workhorse tools of electrical engineering, used in design and debugging from kindergarten science fair projects to billion-transistor integrated circuits.

---

## Concept 1 — Series and parallel combinations

### Two batteries, two bulbs, four ways to wire them

Take two identical 1.5 V AA batteries and two identical 3-volt incandescent bulbs. There are four obvious ways to connect them:

1. Both batteries in series (3 V total), both bulbs in series.
2. Both batteries in series, both bulbs in parallel.
3. Both batteries in parallel (still 1.5 V total but doubled current capacity), both bulbs in series.
4. Both batteries in parallel, both bulbs in parallel.

In each case the bulbs glow at a different brightness. Configurations 1 and 4 give roughly comparable brightness (similar current per bulb). Configuration 2 makes the bulbs glow brightly (full voltage on each). Configuration 3 makes them dim.

This is a four-line experiment that demonstrates the entire content of Concept 1: how currents, voltages, and powers redistribute when you rearrange the wiring. The math below makes it quantitative.

### The mechanism — combination rules

**Resistors in series** carry the same current; their voltage drops add:

$$R_\text{eq, series} = R_1 + R_2 + R_3 + \dots$$

The equivalent resistance is the simple sum.

**Resistors in parallel** have the same voltage across them; their currents add:

$$\frac{1}{R_\text{eq, parallel}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots$$

The reciprocal of the equivalent resistance is the sum of reciprocals. For just two resistors, this can be rewritten as $R_\text{eq} = R_1 R_2 / (R_1 + R_2)$.

A useful intuition: parallel resistance is always *less* than the smallest individual resistor (more paths for current). Series resistance is always *more* than the largest (current must traverse all of them).

For batteries (or any voltage sources):

- **Series:** voltages add. Two 1.5 V cells in series give 3 V total. Same current capacity as one cell.
- **Parallel:** voltage stays the same. Two 1.5 V cells in parallel still give 1.5 V, but doubled current capacity (twice as much chemical reservoir).

For capacitors, the opposite of resistors:

- **Series capacitors** combine reciprocally: $1/C_\text{eq} = 1/C_1 + 1/C_2$.
- **Parallel capacitors** add: $C_\text{eq} = C_1 + C_2$.

This trips up students who try to apply the same rule to all components. The mnemonic: voltage divides across series resistors but charge stays the same across series capacitors, leading to the opposite combination rule.

### The trade-off

Combination rules trade **complete circuit detail for tractable algebra.** Treating ten resistors as one equivalent resistance lets you get to the answer fast — but you've discarded the individual currents and voltages, which you'll need later. The technique is to combine to find the total current from the source, then "unfold" backwards to recover individual values.

### Worked example — Christmas string analysis

Twenty 5 Ω bulbs are connected (a) in series across 120 V; (b) in parallel across 120 V. Compute the current through each bulb, the power dissipated by each, and the total power for each configuration.

**(a) Series.** Equivalent resistance $R_\text{eq} = 20 \times 5 = 100$ Ω. Total current $I = V/R_\text{eq} = 120/100 = 1.2$ A. Each bulb sees this same 1.2 A. Voltage drop across each bulb: $V_\text{bulb} = IR = 1.2 \times 5 = 6$ V. Power per bulb: $P = I^2 R = (1.2)^2 (5) = 7.2$ W. Total: $20 \times 7.2 = 144$ W.

**(b) Parallel.** Each bulb sees the full 120 V. Current per bulb: $I = V/R = 120/5 = 24$ A. Power per bulb: $P = V^2/R = 120^2/5 = 2880$ W. Total: 20 × 2880 = 57,600 W.

The parallel configuration draws 400 times more power and would instantly burn out both the bulbs and the household wiring. The series configuration is what those old bulbs were actually designed for — each bulb operating at 6 V (not 120 V), drawing reasonable current. The price is that one failure kills the whole string.

**Sanity check.** Modern LED Christmas lights are designed for parallel operation: each LED is a low-voltage device with a small built-in dropping resistor or diode bridge, and the string sees one branch fail without affecting the others. The trade-off (higher manufacturing cost) is small relative to the user-experience improvement.

### Common misconceptions

- *"Adding resistors always increases total resistance."* Adding *in series* does. Adding in parallel always *decreases* it.
- *"Parallel capacitors combine like parallel resistors."* No — parallel capacitors *add*; parallel resistors combine reciprocally. Capacitors and resistors have opposite series/parallel rules.
- *"In a parallel branch, the bulb closer to the battery is brighter."* No — both branches see the full source voltage. Brightness depends on the bulb's resistance.

↳ **Dig Deeper — Why does putting more loads in parallel draw more current from the source?**

*A parallel circuit is the model for household electrical wiring: every appliance gets full line voltage, and adding more devices simply adds more current draw. This sets up the rationale for circuit breakers — which trip when total current exceeds safe wiring capacity.*

**Prompt:**
> Walk me through why adding more parallel loads to a circuit draws more current from the source. Use the household wiring example: a 120 V branch circuit with breakers rated at 15 A. Compute how many simultaneous appliances (toaster 12 A, lamp 1 A, microwave 12 A, hair dryer 12 A) can run on the same circuit before tripping the breaker. Then explain why this is the safety reason for separate circuits in different rooms — and why kitchens, bathrooms, and laundry rooms typically have dedicated 20-A circuits. End with one sentence on what happens electrically when a breaker trips (the circuit opens, current = 0, voltage on the appliance side falls to 0).

**What to do with the output:** Save it. Practical circuit safety design is a direct application of these combination rules, and understanding it makes you safer at home.

---

## Concept 2 — Kirchhoff's laws and EMF

### Gustav Kirchhoff, Königsberg, 1845

Gustav Kirchhoff was 21 years old, a student at the University of Königsberg, when he formulated the two rules that bear his name. The rules are not deep new physics — they are immediate consequences of charge conservation (Kirchhoff's junction rule) and energy conservation (Kirchhoff's loop rule). Their power lies in the systematic procedure they give you for analyzing any electrical network, no matter how complex.

The procedure works on circuits Kirchhoff himself never saw — multi-loop semiconductor circuits, transistor networks with billions of components, quantum-coherent superconducting circuits. The bookkeeping is the same.

### The mechanism — the two laws

**Kirchhoff's junction rule (KCL):** At any junction (node) in a circuit, the total current flowing in equals the total current flowing out:

$$\sum I_\text{in} = \sum I_\text{out}.$$

This is just charge conservation: charge can't accumulate at a junction (in steady state), so what comes in must go out.

**Kirchhoff's loop rule (KVL):** Around any closed loop in a circuit, the sum of voltage drops (and rises) is zero:

$$\sum \Delta V = 0.$$

This is energy conservation: a charge moved around a closed loop returns to where it started, with no net change in potential energy.

A standard sign convention:

- A battery from − to + is a *rise* in potential ($+V$).
- A resistor traversed in the direction of current is a *drop* in potential ($-IR$).
- A resistor traversed opposite to current is a *rise* ($+IR$).

The two laws together let you write a system of equations for any circuit. Variables: the unknown currents in each branch. Equations: KCL at each junction (independent ones), KVL around each independent loop. Solve the system.

### Real batteries: EMF and internal resistance

A battery is not a perfect voltage source. It has an **electromotive force** (EMF, denoted $\varepsilon$) — the open-circuit voltage you would measure if no current were flowing — and an **internal resistance** $r$ that limits how much current the battery can deliver. When current $I$ flows through the battery, the terminal voltage drops by $Ir$:

$$V_\text{terminal} = \varepsilon - Ir.$$

A fresh AA cell might have $\varepsilon = 1.50$ V and $r \approx 0.1$ Ω. Drawing 1 A drops the terminal voltage to 1.40 V. As the battery ages, $r$ grows (chemistry inside changes) and the terminal voltage drops more under load — eventually the cell can no longer deliver useful power even though its open-circuit voltage might still read close to 1.5 V.

### The trade-off

Kirchhoff's laws trade **simple intuition for systematic algebra.** For circuits with two or three loops, you can often guess current directions from physical reasoning. For circuits with many loops, it is faster to write all the KCL and KVL equations and solve them mechanically (often by matrix methods on a computer). The cost: temporarily losing the physical picture in favor of a calculation. The benefit: getting the right answer reliably.

### Worked example — circuit with internal resistance

A 12 V car battery (EMF = 12.0 V, internal resistance $r = 0.05$ Ω) drives a starter motor with resistance $R = 0.20$ Ω during cranking. (a) What is the current through the starter? (b) What is the terminal voltage of the battery during cranking? (c) What is the total power delivered by the battery, and the fraction lost as heat inside the battery?

**(a)** Apply KVL around the loop: $\varepsilon - Ir - IR = 0$, giving $I = \varepsilon/(R + r) = 12/0.25 = 48$ A.

**(b)** Terminal voltage: $V_\text{term} = \varepsilon - Ir = 12 - (48)(0.05) = 12 - 2.4 = 9.6$ V.

**(c)** Power delivered by battery: $P_\text{batt} = \varepsilon I = 12 \times 48 = 576$ W. Power dissipated in internal resistance: $P_r = I^2 r = (48)^2 (0.05) = 115$ W. Fraction lost: $115/576 \approx 20\%$.

About 20% of the cranking energy is wasted heating the battery itself. This is why a car battery gets warm during a long crank, and why low-temperature cranking is harder — cold batteries have higher internal resistance.

**Sanity check.** Car batteries are rated in cold-cranking amps (CCA), typically 500-800 A for a passenger car at $-18$ °C. Our 48 A is normal for a warm engine; the cold-weather case sees much higher current as the engine oil resists motion. The internal-resistance / terminal-voltage / power dissipation analysis is exactly how battery engineers design starting batteries.

### Common misconceptions

- *"A battery's voltage is always the printed value."* No — that's the EMF (open circuit). Under load, the terminal voltage is lower by $Ir$.
- *"Ground is the same potential everywhere."* In an ideal circuit, yes. In a real circuit with finite-resistance grounds, "ground bounce" is a real effect, important in high-frequency electronics.
- *"Kirchhoff's laws only work for simple circuits."* They work for any circuit. SPICE — the standard circuit-simulation software — is essentially an algorithm for applying KCL and KVL to systems with thousands of components.

↳ **Dig Deeper — How a multimeter measures without disturbing the circuit**

*Voltmeters and ammeters are themselves resistors. To measure without changing the thing you're measuring, the voltmeter must have a very high resistance (drawing essentially zero current) and the ammeter must have a very low resistance (causing essentially zero voltage drop). The internal design of these instruments is a careful balance of accuracy vs. circuit disturbance.*

**Prompt:**
> Explain why a voltmeter must have very high internal resistance and an ammeter must have very low internal resistance. Walk through the logic: a voltmeter goes in *parallel* with the component being measured (so its resistance shouldn't divert significant current); an ammeter goes in *series* (so its resistance shouldn't drop significant voltage). Compute typical values: a digital multimeter voltmeter has $R_\text{in} \approx 10$ MΩ; a typical ammeter has $R_\text{in} \approx 0.01$ Ω. Show what error each introduces in measuring a 100 Ω resistor at 10 V. End with one sentence on why high-precision lab work uses techniques (e.g., Wheatstone bridges, lock-in amplifiers) that minimize these effects entirely.

**What to do with the output:** Save it. The voltmeter/ammeter design philosophy applies broadly — every measurement disturbs the system being measured, and good engineering is about making the disturbance negligible.

---

## Concept 3 — RC circuits and time constants

### Charging a capacitor through a resistor

Connect a discharged capacitor $C$ across a battery $\varepsilon$ through a resistor $R$. Initially the capacitor has zero voltage across it, so the full battery voltage drops across $R$, driving current $I_0 = \varepsilon/R$.

As the capacitor charges, its voltage $V_C$ rises, and the voltage available to drive current through $R$ shrinks: $V_R = \varepsilon - V_C$. So the current also shrinks. The capacitor approaches its final voltage $\varepsilon$ asymptotically — never quite reaching it, but getting exponentially close.

The math:

$$V_C(t) = \varepsilon \left(1 - e^{-t/\tau}\right),$$

$$I(t) = \frac{\varepsilon}{R} e^{-t/\tau},$$

where the **time constant** is

$$\tau = RC.$$

After $t = \tau$, the capacitor has reached $1 - 1/e \approx 63\%$ of its final voltage. After $t = 2\tau$, about 86%. After $t = 5\tau$, about 99.3%. Engineers typically treat $5\tau$ as "fully charged."

For a discharging capacitor (battery removed, capacitor discharges through the resistor), the equations flip:

$$V_C(t) = V_0 e^{-t/\tau},$$

$$I(t) = \frac{V_0}{R} e^{-t/\tau}.$$

Same time constant, opposite sign of the exponent.

### The mechanism — why $\tau = RC$

The time constant has units of seconds (Ω × F = (V/A)(C/V) = C/A = s). Physically, it represents the *characteristic timescale* over which the circuit responds. A small $\tau$ means fast response (quick charging or discharging); a large $\tau$ means slow.

Examples:

- Camera flash capacitor: $C \approx 100$ μF, charged through $R \approx 10$ kΩ. $\tau \approx 1$ s. After 5 seconds the flash is ready.
- Defibrillator: $C \approx 100$ μF, discharged through patient $R \approx 50$ Ω. $\tau \approx 5$ ms. The shock is delivered in a few time constants.
- Cardiac pacemaker timing: $\tau \approx 1$ s for the natural cardiac cycle; the pacemaker mimics this timescale with intentionally chosen $R$ and $C$.
- RAM in a DRAM chip: $\tau \approx 50$ ms; that's why DRAM needs to be "refreshed" thousands of times per second to retain data.

### The trade-off

RC time constants trade **circuit simplicity for fixed timescale.** A pure RC circuit has only one characteristic time, set by the product $RC$. To get more complex timing (multiple time constants, oscillation), you need either more components (RLC circuits, oscillators) or active devices (transistor-based timers). For applications where one timescale suffices, RC is the simplest possible solution.

### Worked example — flash camera

A flash capacitor of 100 μF is charged from a 200 V source through a 5 kΩ resistor. (a) Time constant. (b) Time to reach 90% of full charge. (c) Energy stored when fully charged. (d) When the flash fires through a discharge resistance of 5 Ω (the lamp's effective resistance), how long does the flash last?

**(a)** $\tau_\text{charge} = RC = (5000)(10^{-4}) = 0.5$ s.

**(b)** $V_C/\varepsilon = 1 - e^{-t/\tau} = 0.9 \implies t = \tau \ln(10) \approx 2.3 \tau \approx 1.15$ s.

**(c)** $U = \frac{1}{2}CV^2 = \frac{1}{2}(10^{-4})(200)^2 = 2$ J.

**(d)** $\tau_\text{discharge} = (5)(10^{-4}) = 0.5$ ms. The flash effectively ends after $5\tau \approx 2.5$ ms. Bright, fast flash — perfect for stop-action photography.

**Sanity check.** A standard photographic flash is on the order of milliseconds, exactly as our $\tau_\text{discharge}$ predicts. The asymmetry (slow charge, fast discharge) is by design: the same capacitor charges through high resistance (slow but controlled) and discharges through low resistance (fast and intense).

### Common misconceptions

- *"After time $\tau$, the capacitor is fully charged."* No — only 63%. After $5\tau$ it is 99% charged; in practice we treat that as "fully."
- *"Time constant depends on the source voltage."* No — only on $R$ and $C$. Source voltage determines the *final* voltage, not how fast you get there.
- *"In a charging circuit, current is constant until the capacitor is full, then drops to zero."* No — current decreases exponentially throughout. There is no abrupt transition.

↳ **Dig Deeper — How RC filters separate frequencies**

*An RC circuit is the simplest electrical filter. In one configuration, it passes low frequencies and blocks high (low-pass filter). In another, it passes high frequencies and blocks low (high-pass filter). The cutoff frequency is determined by $f_c = 1/(2\pi RC)$, directly related to the time constant. RC filters are the building blocks of every audio system, every radio receiver, and every analog signal-processing chain.*

**Prompt:**
> Explain how an RC circuit can act as a low-pass or high-pass filter. Set up the geometry: a series RC circuit with input voltage applied across the whole series combination, and output voltage taken either across the capacitor (low-pass) or across the resistor (high-pass). Show that the response depends on whether the input frequency is above or below the cutoff $f_c = 1/(2\pi RC)$. Then give one practical example of each: an audio amplifier's bass control as a low-pass filter on the signal; a power supply's DC-blocking capacitor as a high-pass filter. End with one sentence on why this is the simplest possible analog signal-processing element.

**What to do with the output:** Save it. RC filters are everywhere in electronics, and understanding the time-constant / frequency-cutoff connection is the bridge to AC circuits (Chapter 23) and signal processing in any later course.

---

## Synthesis — circuits as bookkeeping with $V$, $I$, $R$, $C$

Step back. Three concepts:

1. **Series and parallel combination rules.** Resistors series add; parallel reciprocate. Capacitors opposite. Reduces complex networks to a single equivalent value.

2. **Kirchhoff's laws.** Junction rule (charge conservation) and loop rule (energy conservation) give a systematic procedure for any circuit. Real batteries have EMF and internal resistance.

3. **RC circuits and time constants.** $\tau = RC$ governs charging and discharging. The same product determines filter cutoff frequencies in AC.

The unifying picture: every circuit is a graph (nodes and branches), every branch has a voltage-current relation (Ohm's law for resistors, $I = C \, dV/dt$ for capacitors), and Kirchhoff's laws are the topology constraints that close the system of equations.

### A worked example combining all three concepts — designing a flashlight

Design a simple LED flashlight: an LED with forward voltage 2.5 V and operating current 20 mA, powered by two AA cells (each 1.5 V EMF, 0.1 Ω internal resistance), through a current-limiting resistor.

**Step 1 — Series battery.** Two AAs in series: $\varepsilon = 3.0$ V, $r_\text{total} = 0.2$ Ω.

**Step 2 — Voltage budget.** LED needs 2.5 V at 20 mA. Available voltage: $\varepsilon - I r = 3.0 - (0.020)(0.2) = 2.996$ V. Voltage that must drop across the limiting resistor: $V_R = 2.996 - 2.5 = 0.496$ V.

**Step 3 — Resistor value.** $R = V_R/I = 0.496/0.020 = 24.8$ Ω. Use a standard 27 Ω resistor (slightly conservative).

**Step 4 — Power dissipated in resistor.** $P_R = I^2 R = (0.020)^2(27) = 0.011$ W. Tiny — any standard 1/4-watt resistor handles this easily.

**Step 5 — Battery life.** Two AAs hold about 2500 mAh combined (in series, 2500 mAh at 3 V; capacity in mAh stays at the per-cell value). Run time: $2500 \text{ mAh}/20 \text{ mA} = 125$ hours.

**Step 6 — Time constant.** No capacitor in this circuit, so $\tau = 0$. Flashlight responds instantly to switch.

**Sanity check.** LED flashlights with two AAs typically last 50–100 hours of continuous use. Our 125 hours is in the right neighborhood (we ignored chemistry voltage droop with discharge, which would shorten real life).

**Scale shift.** The same Kirchhoff bookkeeping, scaled up, governs a house's main breaker panel. The same RC time-constant analysis, scaled down by $10^9$, governs the timing of every transistor in your phone. Three rules at the right level of abstraction.

---

## Exercises

### Warm-up

**21.1** *(LO 1)* Two resistors, 50 Ω and 100 Ω, are connected (a) in series, (b) in parallel. Compute the equivalent resistance for each case.

**21.2** *(LO 2)* A 12 V battery is connected to a 4 Ω resistor. What is the current?

**21.3** *(LO 4)* An RC circuit has $R = 10$ kΩ and $C = 100$ μF. Compute the time constant.

**21.4** *(LO 3)* A battery has EMF 9.0 V and internal resistance 0.5 Ω. It supplies current 1.0 A. What is the terminal voltage?

### Application

**21.5** *(LO 1, 2)* Three resistors of 5 Ω, 10 Ω, and 15 Ω are connected in series across a 12 V battery. Compute the current through each, the voltage drop across each, and the total power dissipated.

**21.6** *(LO 1, 2)* The same three resistors connected in parallel across the same 12 V battery. Compute the current through each, the total current from the battery, and the total power dissipated.

**21.7** *(LO 4)* A 50 μF capacitor is charged through a 5 kΩ resistor from a 9 V battery. (a) Time constant. (b) Voltage on capacitor after 0.5 s. (c) Time to charge to 99% of final.

**21.8** *(LO 5)* A galvanometer has full-scale deflection at 1 mA and internal resistance 50 Ω. Convert it into (a) a 0–5 V voltmeter (what series resistance?), (b) a 0–1 A ammeter (what parallel "shunt" resistance?).

### Synthesis

**21.9** *(LO 1, 2)* A car has its headlights on (each 50 W at 12 V) and is then started. The starter motor has resistance 0.2 Ω; the battery has $\varepsilon = 12$ V, $r = 0.05$ Ω. (a) Compute the headlight current before starting. (b) When the starter engages, what is the terminal voltage of the battery? (c) Why do the headlights dim during starting?

**21.10** *(LO 4, beyond)* A heart pacemaker uses an RC circuit to time its pulses at 60 beats per minute. (a) Compute the required time constant if pulses fire at the time when capacitor reaches 70% of full voltage. (b) If $C = 1$ μF, what should $R$ be?

**21.11** *(LO 1, 2)* Christmas lights designed for series operation have 50 bulbs across 120 V. Each bulb operates at its rated voltage and has 0.1 A current. (a) Voltage rating per bulb. (b) Resistance per bulb. (c) Total power.

### Challenge

**21.12** *(LO 2, beyond)* In a Wheatstone bridge (look it up), four resistors $R_1, R_2, R_3, R_x$ are arranged in a diamond with a galvanometer between two nodes. When balanced (galvanometer reads zero), $R_1 R_x = R_2 R_3$. Use Kirchhoff's laws to derive this balance condition. Why is this a good way to measure an unknown resistance precisely?

**21.13** *(LO 4, beyond)* A camera flash capacitor (200 μF, charged to 300 V) discharges through a flash lamp. The flash lasts about 1 ms. (a) Estimate the lamp's effective resistance during the flash. (b) Estimate the peak power. (c) Estimate the total energy released. (d) The full energy doesn't come out as visible light — it's a mix of visible, infrared, and other wavelengths. Estimate the visible-light efficiency given that a typical flash produces about 50 J of visible-light energy from 200 J stored.

---

## LLM Exercise — Chapter 21: A Multi-Component Circuit in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A circuit analysis of one multi-component system in your anchor phenomenon, with computed currents, voltages, and power dissipations.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 21 (Circuits), I want to identify ONE multi-component circuit relevant to my phenomenon and analyze it.

Please:

1. Identify the circuit. Examples:
   - Bike commute: an e-bike's combined motor + headlight + display circuit.
   - Coffee maker: heating element + thermostat + indicator LED circuit.
   - Marathon: a smartwatch's battery + microcontroller + display circuit.
   - Espresso machine: pump motor + boiler + control electronics.
   - Basketball: the LED scoreboard's row driver circuit.

2. Sketch (verbally) the circuit topology: what's in series, what's in parallel.

3. Compute equivalent resistance.

4. Compute total current from the source.

5. Apply Kirchhoff's laws to find the current through and voltage across each major component.

6. Compute power dissipated in each component.

7. Identify any RC time constants if a capacitor is involved.

8. Connect to Chapter 22 (Magnetism), where currents like the ones you just computed will produce magnetic fields.

Save the output as logbook/chapter-21-circuits.md.
```

### What this produces

Your twenty-first Logbook entry — a multi-component circuit analysis.

### How to adapt this prompt

- *For phenomena with no obvious circuit*: every battery-powered device has at least a series RC or RL circuit; pick a plausible model.
- *For Claude Code:* Use Python (with SymPy) or a free SPICE-like simulator (LTspice, ngspice) to verify your hand calculations.

### Connection to previous chapters

Builds on Chapters 19 and 20 (voltage, current, capacitance). Energy bookkeeping from Chapter 7.

### Preview of next chapter

Chapter 22 introduces magnetism — magnetic forces on moving charges and on currents, and the magnetic field produced by currents themselves (Ørsted's discovery, made operational). The Chapter 22 LLM Exercise will compute a magnetic force or field for your phenomenon.

---

## Chapter summary

Circuits are bookkeeping with voltage, current, resistance, and capacitance. Three commitments:

1. **Series and parallel combination rules.** Resistors in series add; parallel reciprocate. Capacitors are opposite. These reduce networks to single equivalent values.

2. **Kirchhoff's laws.** Junction rule (charge conservation) and loop rule (energy conservation) systematize any circuit analysis.

3. **RC circuits.** $\tau = RC$ is the characteristic timescale for charging/discharging and for AC filter cutoff frequencies.

The one idea that matters most: **circuit analysis is two laws applied systematically, not a collection of special cases.** Once you can write KCL at every node and KVL around every loop, every DC circuit yields to algebra.

The common mistake to watch for: **applying resistor combination rules to capacitors (or vice versa).** They have opposite series/parallel rules, and the mistake is one of the most common in first electrical engineering courses.

---

## What would change my mind

The chapter argues that Kirchhoff's laws plus combination rules suffice for any DC circuit at the introductory level. The argument would need revision if a routine consumer circuit exhibited topology effects (cycles in the graph, multi-loop coupling) that the simple methods couldn't handle. They don't — the laws are general, and apply to circuits with arbitrary topology, just at the cost of more equations to solve simultaneously.

## Still puzzling

The deepest puzzle this chapter raises: *why is energy in an RC discharge always exactly half the initial energy lost as heat in the resistor, regardless of $R$?* This is true: when a capacitor at voltage $V_0$ with energy $\frac{1}{2}CV_0^2$ discharges into a resistor, the resistor dissipates exactly $\frac{1}{2}CV_0^2$ as heat — the full original stored energy. Yet if you charge the capacitor through a resistor, exactly half the input energy is lost as heat in the resistor, regardless of $R$. The half-and-half result has a beautiful information-theoretic interpretation but is one of the most surprising results in elementary electronics.

---

## Connections forward

Chapter 22 introduces **magnetism** — the magnetic field produced by currents (Ørsted, Ampère) and the force felt by moving charges and current-carrying wires (Lorentz). Chapter 23 introduces **electromagnetic induction** — changing magnetic fields create voltages, the basis of generators, transformers, and inductors. Together with this chapter and Chapter 19, these set up the full toolkit for AC circuits, which run the modern world. Chapter 24 unifies everything into electromagnetic waves at the speed of light.

---

**Tags:** circuits, Kirchhoffs-laws, RC-time-constant, internal-resistance, voltmeter-ammeter

---

## AI Wayback Machine

**Gustav Kirchhoff** formulated the two laws of circuit analysis in 1845 — the current law (KCL) and voltage law (KVL) — that still underlie every circuit calculation a hundred and eighty years later. He was 21 at the time.

**Run this:**

```
Who was Gustav Kirchhoff, and how do Kirchhoff's laws connect to circuit analysis we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Gustav Kirchhoff"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to solve one specific multi-loop circuit using Kirchhoff's laws.
- Ask it about Kirchhoff's parallel role in spectroscopy and what his absorption lines proved about the Sun.

What changes? What gets better? What gets worse?
