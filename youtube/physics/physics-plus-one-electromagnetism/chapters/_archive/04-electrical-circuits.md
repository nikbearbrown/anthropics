# Chapter 4 — Electrical Circuits

# Three Title Options

1. **The Tame and the Wild: How Circuits Make Electrons Behave**
2. **Pushing Charge Through the Wire: The Machinery of Electrical Circuits**
3. **The Path of Least Resistance: Why Circuits Work the Way They Do**

---

**TL;DR:** Electric current is charge in motion, and the resistance you encounter determines how much current flows. Arrange resistors in series and the voltage divides; arrange them in parallel and the resistance shrinks. These two facts explain every circuit from your phone charger to a hydroelectric dam.

---

## Chapter Opening: The Waterfall

Picture the moment when water tumbles over a dam's spillway. The fall turns potential energy into motion—billions of gallons accelerating downward, their energy harvested by turbines at the base. The water's velocity depends on how far it falls. The volume flowing depends on the spillway's width. Together, they determine the power available to extract.

Now imagine electrons at the positive terminal of a battery, compressed together like water behind a dam. The battery's chemical reaction has done work to separate charges, creating an imbalance. When you connect a wire, the electron equivalent of the spillway opens. Electrons flow from high concentration toward low concentration, but their motion is not a free fall. They collide with atoms in the wire—scattering, losing energy, heating the wire itself. The battery supplies new energy to push them forward again.

This chapter teaches you to see circuits as devices that manage three quantities: how much charge moves (the current), the driving force behind it (the voltage), and what slows it down (the resistance). You'll learn that these three quantities are not independent—they're locked together by a remarkably simple law. You'll see what happens when you connect resistors end-to-end versus side-by-side. And you'll understand why a 60-watt lightbulb draws more current than a 40-watt bulb at the same voltage, and why that matters.

### Learning Objectives

By the end of this chapter, you will be able to:

- Define electric current and calculate how much charge flows in a given time.
- Explain Ohm's law and predict current from voltage and resistance.
- Determine the equivalent resistance of resistors in series (they add).
- Determine the equivalent resistance of resistors in parallel (the reciprocals add).
- Calculate the power dissipated in a circuit and explain where that energy goes.

### Prerequisites

You should be comfortable with:
- Algebra and solving for one variable in terms of others.
- The concept of potential energy and energy transfer.
- Basic SI units: volts, amperes, ohms, watts.

### Why This Matters

Circuits are the language of modern life. Every device that runs on electricity—from a hearing aid to a skyscraper's power distribution—rests on the three ideas in this chapter. Understanding them moves you from passively plugging things in to actually predicting what will happen when you do. This is the foundation for electronics, power engineering, and every hybrid technology that bridges the digital and physical worlds.

---

## Concept 1: Current, Voltage, and Ohm's Law

### The Scene: A Thundercloud Gathers

You're standing in a field in 1941, and a storm is building. Clouds have piled up to 40,000 feet. Inside them, ice crystals collide in updrafts, rubbing electrons off one another and leaving themselves positively charged, while the electrons settle toward the cloud base. The charge separation grows until the electrical field inside the cloud reaches catastrophic levels—millions of volts between cloud and ground.

Then, in an instant, the insulation breaks. A leader stroke of electrons races downward at one-third the speed of light. The moment it touches the ground, the main return stroke roars back upward, carrying 20,000 amperes—twenty thousand coulombs per second—in a fraction of a millisecond. That's current. That's what you're witnessing when lightning flashes.

The reason the return stroke is so violent is the price of that charge separation. All those potential volts have been waiting for a path. When the path opens, the difference drives the current. How much current? That depends on the resistance the charge encounters in its path. Air is usually an insulator—hard to push current through. But once the lightning leader ionizes a channel, the air becomes conductive. The resistance drops. The current becomes enormous.

This is the first principle: current is charge in motion, voltage is the push, and resistance is what stands in the way.

### Mechanism: The Definition of Current

Electric current, by definition, is the amount of charge passing a point per unit time. The symbol is $I$, and the equation is:

$$I = \frac{\Delta Q}{\Delta t}$$

Here, $\Delta Q$ is the charge in coulombs that flows past a point, and $\Delta t$ is the time in seconds. A coulomb is a large amount of charge—the amount carried by about $6.24 \times 10^{18}$ electrons. So one ampere (the unit of current) is one coulomb flowing past a point every second.

To see this concretely: if 5 nanocoulombs of charge pass through a wire in 1 nanosecond, the current is:

$$I = \frac{5 \times 10^{-9} \text{ C}}{1 \times 10^{-9} \text{ s}} = 5 \text{ A}$$

That's a significant current. Your household outlets deliver 15 to 20 amperes. A lightning strike can carry 20,000 amperes, though only for milliseconds. Your phone's charging circuit draws about 1 ampere.

Now, an important subtlety. In a metal wire, the charge carriers are electrons, which are negatively charged. Electrons move from the negative terminal of a battery toward the positive terminal. But by convention—a historical choice made by Benjamin Franklin in the 1700s, before anyone knew electrons existed—we define *conventional current* as the flow of positive charge. This means conventional current flows in the *opposite* direction to the electrons.

The convention seems backwards, but it persists because it's mathematically equivalent. A positive charge moving right produces the same electromagnetic effects as negative charge moving left. Once you've picked a direction to call positive, the rest of the circuit follows. So in a battery circuit, we draw an arrow pointing from the positive terminal through the circuit to the negative terminal, even though electrons physically move the other way.

There are two types of current: **direct current** (DC) flows in one direction constantly, like from a battery. **Alternating current** (AC) reverses direction periodically. Your household power is AC, switching direction 60 times per second in the U.S. (50 times in Europe). AC allows power transmission over long distances with less energy loss, which is why it powers most of the grid. DC dominates in small electronics—your phone, laptop, car—because batteries produce DC, and many circuits need current in a fixed direction.

### Trade-Off: Convenience vs. Power Loss

The choice between AC and DC involves a crucial trade-off. AC can be transformed up to higher voltages and down to lower voltages using a transformer (a coil of wire wrapped around iron). Higher voltages mean lower currents for the same power, and lower currents mean less heat loss as power travels along wires. That's why your laptop charger converts AC to DC at high voltage, then down to the 19 volts your laptop needs.

But AC requires more complex electronics to switch direction repeatedly, and many devices—LEDs, computers, induction motors in some applications—prefer DC. So modern power systems use AC for transmission and then convert back to DC for electronics. You pay that cost (the charger box) because the benefit (efficient long-distance transmission) is larger.

### Worked Example: Current in a Lightning Stroke

A lightning strike transfers $10^{20}$ electrons from cloud to ground. What is the average current if the stroke lasts 2 milliseconds?

**Given:**
- Number of electrons: $n = 10^{20}$
- Charge per electron: $e = -1.60 \times 10^{-19}$ C
- Duration: $\Delta t = 2 \times 10^{-3}$ s

**Find:** Average current $I$.

**Reasoning:** First, calculate the total charge. Each electron carries $1.60 \times 10^{-19}$ coulombs of negative charge. But for the charge transferred, we count magnitude:

$$\Delta Q = n \cdot |e| = 10^{20} \times 1.60 \times 10^{-19} \text{ C} = 16 \text{ C}$$

Now apply the definition of current:

$$I = \frac{\Delta Q}{\Delta t} = \frac{16 \text{ C}}{2 \times 10^{-3} \text{ s}} = 8000 \text{ A}$$

This is 8 kiloamperes. Lightning typically carries between 5,000 and 20,000 amperes, so 8 kA is realistic. The enormous current is why lightning is dangerous—that much charge flowing through your body would cause immediate cardiac arrest and severe burns.

**Sanity check:** One coulomb per second is one ampere. We had 16 coulombs over 2 milliseconds, which is about 0.016 seconds. So we'd expect current around 16/0.016 = 1000 A. Our 8000 A is higher, which makes sense because the time is shorter (lightning is very brief). The order of magnitude is correct.

**Lesson:** Current is the rate at which charge flows. A small amount of charge in a tiny time interval can produce a huge current. This is why brief, intense events like lightning are more destructive than steady flows.

### Now: Voltage and Ohm's Law

Current alone doesn't explain circuits. You need to know what drives the current. That's voltage—the energy per unit charge available to move the charge around a circuit.

Voltage, measured in volts, is defined as potential energy per coulomb:

$$V = \frac{\text{J}}{\text{C}}$$

A 12-volt battery provides 12 joules of energy per coulomb of charge it moves. When that charge flows through a resistor, the resistor extracts that energy and converts it to heat (and light, if it's a lightbulb).

In the 1800s, a German physicist named Georg Simon Ohm conducted experiments on wires and discovered a simple relationship: the current flowing through a conductor is proportional to the voltage applied across it. If you double the voltage, the current doubles. If you halve the voltage, the current halves. The constant of proportionality—the thing that determines the slope of this relationship—is the resistance $R$.

This relationship is **Ohm's law:**

$$V = IR$$

Here, $V$ is the voltage drop (in volts), $I$ is the current (in amperes), and $R$ is the resistance (in ohms, abbreviated $\Omega$). An ohm is one volt per ampere: $1 \, \Omega = 1 \, \text{V/A}$.

To see the relationship intuitively: higher resistance means you need more voltage to push the same current through. A 100-ohm resistor with 10 volts across it carries:

$$I = \frac{V}{R} = \frac{10 \text{ V}}{100 \, \Omega} = 0.1 \text{ A}$$

Double the resistance to 200 ohms, and the current drops to 0.05 amperes. The voltage is still 10 volts—the battery hasn't changed—but the resistance has doubled, so the current halves.

Ohm's law is *empirical*. Ohm didn't derive it from first principles—he measured it. It turns out that most materials obey this relationship over a wide range of voltages and currents. Copper, aluminum, carbon resistors—they're all "ohmic." There are exceptions. Some materials are "nonohmic"—their resistance changes with temperature or current. Lightbulb filaments heat up as current flows, and their resistance increases, so their I-V relationship is not a straight line. But for most resistors and many conductors, Ohm's law holds well enough for practical use.

### Common Misconceptions

**Misconception 1:** "Higher voltage always means more current."

This is true *if* the resistance stays the same. But if you increase voltage while decreasing resistance (by switching to a lower-resistance resistor), the current might not increase. Ohm's law says $I = V/R$. Current depends on both voltage *and* resistance. You have to know both to predict the current.

**Misconception 2:** "Resistance is bad; we should minimize it."

Resistance is essential. Without it, current would be limited only by the battery's internal resistance and the wire's own (tiny) resistance. A 12-volt battery connected to a 0.001-ohm wire would deliver 12,000 amperes, instantly destroying the battery and the wire. Resistance is what allows us to control current. A lightbulb's resistance is what slows the current enough that the heat and light outputs are useful rather than explosively large.

**Misconception 3:** "Voltage is used up as it travels through a circuit."

This is partially true but misleading. Voltage doesn't "travel"—it describes the energy difference between two points. As current flows through a resistor, the voltage *across* the resistor is the amount of energy per coulomb that the resistor extracts from the charge. That voltage "drop" is real—the charge has less energy after passing through. But in the wires connecting the resistor (which have negligible resistance), the voltage stays constant. The energy is lost only where there's resistance.

---

## Concept 2: Series Circuits and Equivalent Resistance

### The Scene: Christmas Lights on a Wire

Before LEDs, Christmas light strings were wired in series—each bulb connected in a line, one after another. If one bulb burned out, the entire string went dark. Why? Because in a series circuit, the current has only one path. Break that path, and current stops everywhere.

This seems like a design flaw, and it is—that's why modern strings use parallel circuits and LEDs. But series circuits have a hidden elegance. Understand how current and voltage divide in series, and you've grasped the fundamental principle of how circuits behave.

### Mechanism: Resistors in Series

Two resistors are in series when they're connected end-to-end, one after the other, in a single path. The current entering the first resistor must exit and immediately enter the second. There's nowhere else for it to go.

This has an immediate consequence: **the same current flows through all resistors in series.**

Now, what about voltage? Each resistor drops some voltage as the current flows through. By Ohm's law, $V = IR$, so a larger resistor drops more voltage. If a current of 1 ampere flows through a 5-ohm resistor, it drops 5 volts. If that same 1 ampere flows through a 10-ohm resistor, it drops 10 volts.

The key insight: the total voltage supplied by the battery must equal the sum of the voltage drops across each resistor. This is because the battery does work to move the charge around the circuit, and that work is dissipated as heat in each resistor. If the battery supplies 12 volts, and one resistor drops 5 volts while the other drops 10 volts, the math works out: 5 + 10 = 15. Wait, that's more than 12. That won't work.

Let me be more careful. Suppose a battery supplies 12 volts to two resistors in series: a 3-ohm resistor and a 9-ohm resistor. The total resistance is 3 + 9 = 12 ohms. By Ohm's law, the current is:

$$I = \frac{V}{R_{\text{total}}} = \frac{12 \text{ V}}{12 \, \Omega} = 1 \text{ A}$$

Now the voltage drops:
- Across the 3-ohm resistor: $V_1 = I \cdot R_1 = 1 \text{ A} \cdot 3 \, \Omega = 3 \text{ V}$
- Across the 9-ohm resistor: $V_2 = I \cdot R_2 = 1 \text{ A} \cdot 9 \, \Omega = 9 \text{ V}$

Total: $V_1 + V_2 = 3 + 9 = 12$ V. It balances.

This leads to the principle for **equivalent resistance in series:**

$$R_{\text{equiv}} = R_1 + R_2 + R_3 + \cdots$$

Resistors in series simply add. A 10-ohm and a 20-ohm resistor in series act like a single 30-ohm resistor.

Why does this matter? Because it lets you simplify circuits. Instead of calculating current through each resistor separately, you replace all the series resistors with their equivalent, find the total current, and then work backwards to find the voltage across each one.

### Trade-Off: Voltage Division

Here's the trade-off in series circuits: voltage divides. If you need to supply 12 volts to a device, but you place another resistor in series with it, some of that 12 volts now drops across the series resistor, and less reaches your device.

This is both a bug and a feature. It's a bug if you want to deliver full voltage to your load—the series resistor (called a "dropping resistor") wastes power. It's a feature if you want to reduce voltage to a sensitive circuit. Before voltage regulators became cheap and small, engineers used dropping resistors to step down voltages.

But there's a cost: power dissipation. The power dissipated in a resistor is $P = I^2 R$. In a series circuit, the same current flows through all resistors, so a larger resistor wastes more power. If your 3-ohm dropping resistor carries 1 ampere, it dissipates 1 watt as heat. If your load resistor (the 9-ohm bulb) carries the same 1 ampere, it dissipates 9 watts. The power divides in proportion to the resistances. The largest resistor gets the most power and dissipates it as heat.

### Worked Example: Three Resistors in Series

A battery supplies 12 volts to three resistors in series: 1 ohm, 6 ohms, and 13 ohms. Find (a) the equivalent resistance, and (b) the current through the circuit. Then verify that the voltage drops add up.

**Given:**
- $V_{\text{battery}} = 12 \text{ V}$
- $R_1 = 1 \, \Omega$, $R_2 = 6 \, \Omega$, $R_3 = 13 \, \Omega$

**Find:** (a) $R_{\text{equiv}}$, (b) $I$, and (c) verify the voltage drops.

**Part (a): Equivalent Resistance**

In series, resistances add:

$$R_{\text{equiv}} = R_1 + R_2 + R_3 = 1 + 6 + 13 = 20 \, \Omega$$

**Part (b): Current**

By Ohm's law:

$$I = \frac{V_{\text{battery}}}{R_{\text{equiv}}} = \frac{12 \text{ V}}{20 \, \Omega} = 0.60 \text{ A}$$

**Part (c): Voltage Drops**

For each resistor:

$$V_1 = I \cdot R_1 = 0.60 \text{ A} \cdot 1 \, \Omega = 0.60 \text{ V}$$
$$V_2 = I \cdot R_2 = 0.60 \text{ A} \cdot 6 \, \Omega = 3.6 \text{ V}$$
$$V_3 = I \cdot R_3 = 0.60 \text{ A} \cdot 13 \, \Omega = 7.8 \text{ V}$$

Sum: $0.60 + 3.6 + 7.8 = 12$ V. Perfect.

**Lesson:** In series, current is the same everywhere, resistances add, and voltage drops add. The pattern is consistent: the larger the resistor, the larger the voltage drop across it (for a given current).

### Common Misconceptions

**Misconception 1:** "All resistors in series have the same voltage drop."

No. The voltage drop across each resistor is proportional to its resistance (given the same current). A 10-ohm resistor carrying 2 amperes drops 20 volts; a 5-ohm resistor carrying the same 2 amperes drops 10 volts. The current is the same; the voltages are different.

**Misconception 2:** "Series is better because resistances add up to a large total, which reduces current."

This is true, but it's not a feature—it's a consequence. Series circuits naturally limit current because resistance adds. In some cases that's useful (protecting sensitive circuits from too much current). In other cases it's a liability (you lose power to the series resistor and the circuit heats up).

---

## Concept 3: Parallel Circuits and Power

### The Scene: Every Outlet in Your Home

Walk into any room and find an outlet. Plug a lamp into the top socket and a phone charger into the bottom. Both work independently. Turn off the lamp—the charger keeps charging. Turn on three lights—they glow at full brightness even as the charger draws current. This is parallel wiring.

In your home, every outlet connects to the same two wires running through the walls: one at 120 volts, one at zero volts (ground). Each device (light, charger, air conditioner) connects across those same two voltages. This is radically different from series. Each device has its own independent path. Add one more device, and the others don't "notice"—they get the same voltage and draw the current they need.

### Mechanism: Resistors in Parallel

Two resistors are in parallel when they connect side-by-side: both have their left ends wired together and their right ends wired together. The voltage across both is identical. The current splits: some goes through the first resistor, some through the second.

By Ohm's law, if both resistors experience the same voltage $V$, the current through each is:

$$I_1 = \frac{V}{R_1}, \quad I_2 = \frac{V}{R_2}$$

The total current from the battery is the sum of these currents (charge is conserved—whatever leaves the battery must enter both paths):

$$I_{\text{total}} = I_1 + I_2 = \frac{V}{R_1} + \frac{V}{R_2} = V \left( \frac{1}{R_1} + \frac{1}{R_2} \right)$$

This can be rewritten as Ohm's law with an equivalent resistance:

$$V = I_{\text{total}} \cdot R_{\text{equiv}}$$

where

$$R_{\text{equiv}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}}$$

This is the reciprocal formula for parallel resistance. The reciprocals add. For $N$ resistors in parallel:

$$R_{\text{equiv}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_N}}$$

Here's the counterintuitive consequence: **parallel resistance is always smaller than the smallest individual resistor.** If you have a 10-ohm and a 20-ohm resistor in parallel, the equivalent is:

$$R_{\text{equiv}} = \frac{1}{\frac{1}{10} + \frac{1}{20}} = \frac{1}{0.1 + 0.05} = \frac{1}{0.15} = 6.67 \, \Omega$$

Why? Because you've created more paths for current to flow. The current has two routes to get from one point to another, so the overall resistance to current is less.

### Trade-Off: Current Distribution

In parallel circuits, voltage is the same everywhere, but current divides. More current flows through the lower-resistance path. An LED (low resistance, typically a few ohms) in parallel with an incandescent bulb (high resistance, typically 100+ ohms) will get much more current and be much brighter.

This creates a design challenge: if you want multiple devices to operate at the same voltage but draw different currents, you need each to have the right resistance. Parallel is ideal for this. But you also need to protect the circuit. If someone shorts a circuit by connecting a wire (near-zero resistance) across the voltage supply, the current will become enormous and the wire will overheat. That's why homes have fuses and circuit breakers—they detect excessive current and disconnect the circuit before it catches fire.

### Worked Example: Three Resistors in Parallel

A 3-volt battery connects to three resistors in parallel: 10 ohms, 25 ohms, and 15 ohms. Find (a) the equivalent resistance, (b) the total current, and (c) the current through each resistor.

**Given:**
- $V = 3 \text{ V}$
- $R_1 = 10 \, \Omega$, $R_2 = 25 \, \Omega$, $R_3 = 15 \, \Omega$

**Find:** (a) $R_{\text{equiv}}$, (b) $I_{\text{total}}$, (c) $I_1$, $I_2$, $I_3$.

**Part (a): Equivalent Resistance**

$$R_{\text{equiv}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}} = \frac{1}{\frac{1}{10} + \frac{1}{25} + \frac{1}{15}}$$

Convert to a common denominator (150):

$$\frac{1}{10} = \frac{15}{150}, \quad \frac{1}{25} = \frac{6}{150}, \quad \frac{1}{15} = \frac{10}{150}$$

Sum: $\frac{15 + 6 + 10}{150} = \frac{31}{150}$

$$R_{\text{equiv}} = \frac{150}{31} \approx 4.84 \, \Omega$$

**Part (b): Total Current**

$$I_{\text{total}} = \frac{V}{R_{\text{equiv}}} = \frac{3 \text{ V}}{4.84 \, \Omega} \approx 0.62 \text{ A}$$

**Part (c): Current Through Each Resistor**

Each resistor has the full 3 volts across it:

$$I_1 = \frac{V}{R_1} = \frac{3}{10} = 0.30 \text{ A}$$
$$I_2 = \frac{V}{R_2} = \frac{3}{25} = 0.12 \text{ A}$$
$$I_3 = \frac{V}{R_3} = \frac{3}{15} = 0.20 \text{ A}$$

Sum: $0.30 + 0.12 + 0.20 = 0.62$ A. This matches $I_{\text{total}}$, confirming charge conservation.

**Lesson:** In parallel, voltage is constant across all branches, current divides inversely with resistance (smaller resistance gets more current), and the equivalent resistance is smaller than any individual resistor. Notice that the 10-ohm resistor (smallest) carries the most current (0.30 A), and the 25-ohm resistor (largest) carries the least (0.12 A).

### Common Misconceptions

**Misconception 1:** "Parallel resistors all carry the same current."

No. They have the same voltage across them, so by Ohm's law, current depends on resistance. Lower resistance means higher current. Only if all resistors are identical will they carry the same current.

**Misconception 2:** "Adding another resistor in parallel increases the total resistance."

The opposite is true. Adding another path decreases resistance. Adding a resistor in parallel always decreases the equivalent resistance (until you've added infinitely many zero-ohm paths, which is not physical). This is why adding electrical outlets to a wall—which are parallel branches—can overload a circuit. You're decreasing the total resistance, increasing total current, and potentially exceeding the circuit breaker's limit.

---

## Integration: Power and the Complete Circuit

You've learned how current, voltage, and resistance relate (Ohm's law), how they behave in series (resistances add, current is constant, voltage divides), and how they behave in parallel (voltage is constant, current divides, reciprocal resistances add). Now comes the practical question: where does the energy go?

Electric power is the rate at which energy is transferred. The SI unit is the watt, which is one joule per second. The power delivered by a voltage source to a circuit is:

$$P = IV$$

This is because voltage is energy per coulomb ($V = \text{J/C}$) and current is coulombs per second ($I = \text{C/s}$). Multiply them: $\text{J/C} \times \text{C/s} = \text{J/s} = \text{W}$.

In a circuit with a resistor, that power is dissipated as heat. By substituting Ohm's law ($V = IR$), you can express power in two other ways:

$$P = IV = I(IR) = I^2 R$$

or

$$P = IV = \left( \frac{V}{R} \right) V = \frac{V^2}{R}$$

A 100-ohm resistor with 10 volts across it dissipates:

$$P = \frac{V^2}{R} = \frac{100}{100} = 1 \text{ W}$$

A 100-watt incandescent lightbulb operating at 120 volts draws a current of:

$$I = \frac{P}{V} = \frac{100 \text{ W}}{120 \text{ V}} \approx 0.83 \text{ A}$$

and has a resistance of:

$$R = \frac{V}{I} = \frac{120}{0.83} \approx 144 \, \Omega$$

**Putting it together:** A circuit with a battery, resistors in series and parallel, and a load device is really a system for transferring energy. The battery does chemical work to move charge. That charge carries potential energy as it flows through the circuit. The resistors extract that energy and convert it to heat. The total power delivered equals the total power dissipated—energy is conserved.

In your home, a circuit breaker trips when the total current exceeds its rating (typically 15 or 20 amperes) because that's when the total power dissipation would exceed the safe limit and wires could overheat.

---

## Exercises

### Warm-Up (Concept Check)

1. **Current Definition.** A phone charger draws 2 amperes. How many coulombs of charge pass through it in one minute? (Hint: use $I = \Delta Q / \Delta t$.)

2. **Ohm's Law Direct.** A resistor has 5 volts across it and carries 0.5 amperes. What is its resistance?

3. **Series Recognition.** In a circuit diagram, you see a battery connected to two resistors one after the other. Are they in series or parallel? How do you know?

### Application (Extending the Concepts)

4. **Series Voltage Division.** A 9-volt battery connects to a 2-ohm resistor in series with a 4-ohm resistor. Without calculating the total current first, explain why the 4-ohm resistor must have twice the voltage drop of the 2-ohm resistor.

5. **Parallel Current Distribution.** A 12-volt battery connects to a 6-ohm resistor in parallel with a 12-ohm resistor. Which resistor carries more current? By what factor? (Use Ohm's law; you don't need the equivalent resistance.)

6. **Power in a Lightbulb.** A 60-watt lightbulb operates at 120 volts. Find its resistance and the current it draws. Then verify: does $I^2 R$ equal 60 watts?

### Synthesis (Combining Concepts)

7. **Series-Parallel Mix.** A circuit has two 20-ohm resistors in series, and this combination in parallel with a 10-ohm resistor. Find the equivalent resistance of the entire combination. (Hint: start with the series part, then treat it as a parallel branch.)

8. **Energy Flow.** A 12-volt battery delivers 0.5 amperes to a circuit. How much energy does the battery supply in 1 hour? Where does this energy go in the circuit? (Hint: use $P = IV$ and then $E = Pt$.)

### Challenge (Extension and Critique)

9. **Why Circuits Fail.** Some older Christmas light strings went dark if one bulb burned out (series circuit). Modern strings stay lit (parallel circuit). Why? What's the trade-off in each design?

10. **Real-World Resistance.** The copper wires in your home have some resistance, though we usually treat them as ideal (zero resistance) in circuit diagrams. If the wires from your circuit breaker to a wall outlet have a combined resistance of 0.1 ohm, and a 15-ampere circuit draws full current, how much voltage is "lost" in the wires? What happens to this energy?

---

## Summary

Electric current is the flow of charge through a circuit, measured in amperes. Voltage is the energy per coulomb driving that charge, and resistance opposes the flow.

Ohm's law ties these together: $V = IR$. This simple relationship—validated by countless experiments and observations—lets you predict how a circuit will behave.

Resistors in series add; they limit current by increasing total resistance and divide voltage among themselves. Resistors in parallel allow current to split and always provide a smaller total resistance than any single path. Both configurations appear in every circuit design from power grids to phone chargers.

Power is energy per unit time, and in a circuit, it flows from the source (battery) into the resistances, where it becomes heat. Understanding power lets you predict heating (good for a stove, bad for a short circuit) and energy consumption (important for your electricity bill and your device's battery life).

The most important lesson: these three concepts—series, parallel, and power—are not separate ideas. They're different facets of the same principle. Current, voltage, and resistance are interdependent. When you change one, you must think through how it affects the others.

---

## Connections Forward

This chapter completes the electrical fundamentals. The next chapter introduces capacitors—devices that store charge rather than dissipate it. You'll learn that capacitors behave like "open circuits" to steady current (charge can't flow indefinitely into a capacitor; it fills up) but like conductors to changing current. This lets you design circuits that filter out unwanted signal variations, store brief pulses of energy, and build timing circuits.

After that come inductors, which do the opposite: they resist changes in current. Together, capacitors and inductors let you design oscillators and filters—the building blocks of radios, audio equipment, and signal processing. But they only work because of the Ohm's law, series, and parallel principles you've learned here. You now understand the machinery. Everything else is a variation on this theme.

The deeper pattern you should notice: the world of electricity organizes around a few fundamental ideas—conservation of energy, conservation of charge, and the empirical fact that current is proportional to voltage. These aren't mysterious axioms. They follow from the motion of electrons and the forces they experience. But the mathematics works out so neatly that you can build entire technologies on top without needing to think about individual electrons every time. That's the power of a well-chosen abstraction.

---

**What would change my mind:** If an experiment showed that a material's resistance changed with the direction of applied voltage—that $V = IR$ predicted current in one polarity but a completely different current in the reverse polarity—I would have to reconsider whether Ohm's law is as universal as it appears to be in introductory physics.

**Still puzzling:** I don't fully understand why electrons scatter so readily from atomic nuclei and impurities in a conductor. The quantum mechanics of electron-ion collisions is complex, and I've simplified it here to "electrons bump into atoms and lose energy." The actual interaction involves quantum tunneling and wave-particle duality. That's a deeper physics problem.

---

**Tags:** electric-circuits, Ohm's-law, series-parallel, current-voltage-resistance, power-dissipation

---

## LLM Exercise — Chapter 19: Electrical Circuits (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** a real working circuit with battery + bulb(s) + wires, comparing series vs. parallel and measuring voltage/current.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 19 demo. Notebook in this Claude Project. Chapter 19
taught: current (charge flow per second; A = C/s); voltage
(potential difference, V); resistance (V = IR — Ohm's law);
series circuits (R_total = R1 + R2, current same throughout);
parallel circuits (1/R_total = 1/R1 + 1/R2, voltage same
across); power dissipation (P = VI = I²R = V²/R).

**The Demo:** Build real circuits with a battery and bulbs.
Compare series vs. parallel. Measure voltage and current with
a multimeter.

**Materials:**
- Two or three identical small light bulbs (LED is OK; 1.5V or
  3V flashlight bulbs work too).
- A 9V battery + battery clip, OR two AA batteries in series in
  a battery holder.
- Wires (multi-strand or solid; insulated; alligator clips help).
- A multimeter (~$15 at hardware store; or borrow one).
- Optional: switches, resistors of known value.

**Procedure A: Series circuit**

1. Connect: battery → bulb 1 → bulb 2 → bulb 3 → back to battery.
2. Observe: all bulbs light, but DIMLY (each gets ~1/3 the
   voltage if all bulbs are identical).
3. Measure: voltage across each bulb. Should be ~equal (e.g.,
   3V across each if total is 9V).
4. Measure: current through the circuit (one point only — same
   everywhere in series). Note the current.
5. Unscrew one bulb. The whole circuit goes DARK. Series
   circuits fail completely if one element fails.

**Procedure B: Parallel circuit**

1. Connect: battery to a junction; from the junction, three
   parallel branches each with one bulb; all reconverge at a
   second junction; back to battery.
2. Observe: all bulbs light at FULL brightness (each gets the
   full battery voltage).
3. Measure: voltage across each bulb. Should equal the battery
   voltage (~9V each).
4. Measure: current through each branch. Sum of branch currents
   should equal the current from the battery.
5. Unscrew one bulb. The other bulbs stay lit (just lose one
   branch).

**Procedure C: Verify Ohm's law**

1. With one bulb in a circuit, measure the voltage across it (V)
   and the current through it (I).
2. Compute resistance R = V/I.
3. Repeat with a different battery voltage (single AA vs. 9V).
4. The resistance should be ~constant (within bulb's heating
   effects).

**Use Claude as a thinking partner:**
- Before: "Predict the brightness comparison of one bulb on 9V
  vs. three identical bulbs in series on 9V."
- After: "I measured Va = X, Ia = Y across each series bulb.
  Computed bulb resistance: Z. Does this match my parallel
  measurement of voltage and current?"

**Notebook entry should include:**
- Photos of both circuits in action.
- Schematic diagrams (sketched or generated).
- Voltage and current measurements for each bulb in each
  configuration.
- Computed resistance.
- The series-vs-parallel observations: which bulbs were
  dimmer, which failed when one was unscrewed.

End with: house wiring is typically parallel, not series. Why?
What would happen if your house's outlets were wired in series?
```

---

**What this produces:** A demo entry with measured voltages, currents, and resistances for both series and parallel configurations. The "house wiring is parallel" question is one of the chapter's most important real-world lessons.

**How to adapt this prompt:**

- *For your own project:* Multimeters are widely available cheap. If you can't get one, the brightness-comparison observations alone tell most of the story.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* For circuit-schematic generation, Claude Code can produce ASCII or LaTeX-style diagrams.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 18's electrical concepts get applied to flowing charge (current) instead of static charge.

**Preview of next chapter:** Chapter 20 is magnetism. You'll build a simple electromagnet by wrapping wire around a nail and powering it with a battery. Iron filings (or a homemade compass) reveal the field structure.


---

## AI Wayback Machine

**Gustav Kirchhoff** formulated the two circuit laws bearing his name in 1845, at age 21.

**Run this:**

```
Who is Gustav Kirchhoff, and how does their work connect to electrical circuits we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Gustav Kirchhoff"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Gustav Kirchhoff's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Gustav Kirchhoff's framework."

What changes? What gets better? What gets worse?
