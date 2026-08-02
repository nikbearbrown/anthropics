# Chapter 7 — DC Circuits

*Kirchhoff's two laws and the systematic analysis of any DC circuit.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State Kirchhoff's current law (KCL) and voltage law (KVL) and identify them as conservation of charge and energy respectively.
2. **(Apply)** Compute equivalent resistance for resistors in series and parallel and combine them in mixed networks.
3. **(Apply)** Set up and solve nodal-analysis equations for a multi-loop circuit using KCL and KVL.
4. **(Analyze)** Account for internal resistance of real batteries and the loading effect of voltmeters and ammeters.
5. **(Apply)** Build an interactive circuit simulator that solves circuits as the user assembles them on a grid.

---

## Opening case: the room with no working lamp

A student has three lamps connected to a power strip, all using the same kind of bulb. One day the third lamp stops working — but only when she plugs in her laptop charger at the same socket. Unplug the laptop, the lamp works. Plug in the laptop, the lamp stops. The bulb is new. The wiring looks fine.

What's happening is that the power-strip's circuit has a small internal resistance — call it 0.5 Ω. The laptop charger draws perhaps 8 A on startup; the lamps draw 0.5 A each. With the laptop drawing 8 A through 0.5 Ω, the voltage drop across the wiring is 4 V — bringing the lamp's terminal voltage from 120 V to 116 V. For most lamps that's invisible. But the third lamp has an aging filament that won't strike at 116 V; it needs 119 V or more to light. So the lamp doesn't work, *not because the lamp is broken*, but because the laptop is loading the same power strip and dropping the voltage seen at the lamp.

This is the **loading effect**, and it is a real thing every electrical engineer knows about. To analyze it, you need to model the wiring as a circuit element with finite resistance, the source as a battery with finite internal resistance, and apply two universal laws — KCL and KVL — to figure out what voltage and current actually appear at the lamp.

This chapter develops those tools systematically. By the end, the laptop-vs-lamp puzzle is a one-line application. So is essentially every multi-loop DC circuit you will meet.

---

## Core concept

### Kirchhoff's two laws

**Kirchhoff's Current Law (KCL).** At any node (junction where wires meet), the total current flowing in equals the total current flowing out.

$$\sum I_{\text{in}} = \sum I_{\text{out}}$$

KCL is **conservation of charge**. Charge cannot pile up at a node (it would build a runaway potential); it flows through.

**Kirchhoff's Voltage Law (KVL).** Around any closed loop, the algebraic sum of voltage changes is zero.

$$\sum_{\text{loop}} \Delta V = 0$$

Walking around any loop and adding up the voltage gains (across batteries from − to +) and drops (across resistors in the direction of current flow), you end up where you started. Same potential. KVL is **conservation of energy**: a charge carried around a loop returns to its starting potential, so net work done on it equals zero.

These two laws plus Ohm's law ($V = IR$) are sufficient to solve any DC circuit. The skill is setting up the equations systematically.

### Resistors in series and parallel

**Series:** resistors $R_1, R_2$ in a chain, same current flows through both. Total voltage drop: $V = IR_1 + IR_2 = I(R_1 + R_2)$. Equivalent resistance:

$$R_{\text{eq, series}} = R_1 + R_2 + \cdots$$

**Parallel:** resistors $R_1, R_2$ between the same two nodes, same voltage across both. Total current: $I = V/R_1 + V/R_2 = V(1/R_1 + 1/R_2)$. Equivalent resistance:

$$\frac{1}{R_{\text{eq, parallel}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots$$

Note the inversion compared to capacitors (Ch 5): resistors add in series; capacitors add in parallel. Easy to confuse; worth memorizing both pairs.

For two resistors in parallel: $R_{\text{eq}} = R_1 R_2 / (R_1 + R_2)$. Two equal $R$'s in parallel give $R/2$.

### Voltage divider and current divider

Two resistors $R_1, R_2$ in series across $V_{\text{in}}$, output taken across $R_2$:
$$V_{\text{out}} = V_{\text{in}} \cdot \frac{R_2}{R_1 + R_2}$$

This is the voltage divider. It's everywhere: setting a reference voltage, biasing transistors, building potentiometer-controlled controls.

Two resistors in parallel sharing current $I$:
$$I_1 = I \cdot \frac{R_2}{R_1 + R_2}, \quad I_2 = I \cdot \frac{R_1}{R_1 + R_2}$$

Current divider. The *larger* resistor gets the *smaller* current — opposite of voltage divider's intuition.

### Multi-loop analysis: nodal method

For a circuit with $N$ nodes:
1. Label every node with a variable: $V_0$ (ground, set to 0), $V_1$, $V_2$, etc.
2. Write KCL at each non-ground node: sum of currents into the node = 0.
3. Use Ohm's law to express each branch current in terms of node voltages: $I_{\text{branch}} = (V_{\text{node A}} - V_{\text{node B}})/R_{\text{branch}}$.
4. Solve the resulting system of linear equations.

For a two-node circuit (besides ground), the result is a single equation in one unknown — straightforward. For more nodes, the system grows; numerical software (or Cramer's rule, or Gauss elimination) handles it.

### Real batteries: EMF and internal resistance

An *ideal* battery delivers constant voltage $\varepsilon$ regardless of current. A *real* battery is modeled as an ideal EMF $\varepsilon$ in series with an **internal resistance** $r$. Terminal voltage:

$$V_{\text{terminal}} = \varepsilon - Ir$$

At zero current (open circuit), $V_{\text{terminal}} = \varepsilon$. At nonzero current, the terminal voltage drops by $Ir$.

A car battery has $r \sim 0.01$ Ω; supplies a starting motor at 200 A → terminal drops by $\sim 2$ V from its 12.6 V open-circuit value. A small AA battery has $r \sim 0.15$ Ω; supplies 0.5 A → drops by 0.075 V from its 1.5 V open-circuit. The internal resistance limits the *maximum* current the battery can deliver: short-circuit current is $I_{\max} = \varepsilon/r$.

The laptop-charger-vs-lamp puzzle is exactly this physics, applied to wiring instead of the battery.

### Voltmeters and ammeters

A real **voltmeter** is a high-resistance ammeter in parallel with the element being measured. To not perturb the circuit, it must have $R$ much larger than the element's resistance. A 10 MΩ digital multimeter measuring across a 1 kΩ resistor barely disturbs the circuit. The same multimeter measuring across a 50 MΩ resistor is in trouble.

A real **ammeter** is a low-resistance voltmeter inserted in series with the branch being measured. To not perturb the circuit, it must have $R$ much smaller than other branch resistances. An ideal ammeter has zero resistance; a real one has milliohms.

**The loading effect:** any meter changes the circuit by being there. Engineering practice is to verify your meter's resistance doesn't matter for your problem.

### Power dissipation

Power delivered to a resistor is the rate at which the electric field does work on moving charges:

$$P = IV = I^2 R = V^2/R$$

All three forms are equivalent via Ohm's law; pick the one that matches what you have. Power dissipated appears as heat — Joule heating.

Total power delivered by a battery: $P_{\text{source}} = \varepsilon I$. Of this, $P_{\text{external}} = (\varepsilon - Ir) I$ is delivered to the external circuit and $P_{\text{internal}} = I^2 r$ is dissipated as heat inside the battery itself.

**Maximum power transfer theorem.** The external circuit absorbs maximum power from a battery when its resistance equals the battery's internal resistance ($R_{\text{ext}} = r$). At this match: half the source power is delivered externally; half is dissipated internally. Pushed by radio engineering, taken seriously for low-power signal sources, less relevant for big power supplies where efficiency matters more than power transfer.

---

## Worked example: a two-loop circuit

Two batteries and three resistors. Battery 1 ($\varepsilon_1 = 12$ V) drives current $I_1$ through $R_1 = 4$ Ω. Battery 2 ($\varepsilon_2 = 8$ V) drives current $I_2$ through $R_2 = 6$ Ω. Both circuits share a middle resistor $R_3 = 3$ Ω with current $I_3$. Find $I_1, I_2, I_3$.

**Nodal analysis.** Let the bottom node be ground ($V = 0$), and let $V$ be the voltage at the top node (where all three resistors meet).

**Branch currents in terms of $V$:**
- $I_1 = (\varepsilon_1 - V)/R_1 = (12 - V)/4$ (flowing into the top node from battery 1)
- $I_2 = (\varepsilon_2 - V)/R_2 = (8 - V)/6$ (flowing into the top node from battery 2)
- $I_3 = V/R_3 = V/3$ (flowing out of the top node through $R_3$ to ground)

**KCL at the top node:**
$$\frac{12 - V}{4} + \frac{8 - V}{6} = \frac{V}{3}$$

Multiply through by 12:
$$3(12 - V) + 2(8 - V) = 4V$$
$$36 - 3V + 16 - 2V = 4V$$
$$52 = 9V$$
$$V = 52/9 \approx 5.78 \text{ V}$$

**Back out branch currents:**
- $I_1 = (12 - 5.78)/4 = 1.56$ A
- $I_2 = (8 - 5.78)/6 = 0.37$ A
- $I_3 = 5.78/3 = 1.93$ A

**Check KCL.** $I_1 + I_2 = 1.93 = I_3$. ✓

**Check KVL** (loop 1, going around: battery 1 + → top node → through $R_1$ back to battery 1 −):
$\varepsilon_1 - I_1 R_1 = 12 - 1.56 \cdot 4 = 12 - 6.24 = 5.76$ V (= $V$, the top-node potential). ✓

**The lesson.** Pick a node, write one KCL equation, solve. Done. The nodal method scales: $N$ nodes → $N-1$ equations in $N-1$ unknowns.

**The limit.** This works for purely resistive DC circuits. Add capacitors or inductors, and the equations become differential. Add nonlinear elements (diodes, transistors), and the equations are nonlinear. Both are doable but beyond this chapter.

---

## Common misconceptions

**"Current gets used up by a resistor."** Current (charge per second) is conserved at every node and through every series branch. What gets dissipated is *energy*: power $I^2 R$ becomes heat. The current that emerges from a resistor equals the current that entered.

**"A voltmeter measures the voltage across the wire it's attached to."** It measures the voltage *between two nodes*. Wires (treated as ideal) have zero voltage drop along their length.

**"A battery always delivers its rated voltage."** Only at zero current (open circuit). Under load: terminal voltage drops by $Ir$. The drop is the *loading effect* and it's a real engineering concern.

**"Adding resistors in parallel adds resistance."** It *reduces* total resistance. More parallel paths = more current capacity = less obstruction. Opposite of series.

**"KVL only works for single-loop circuits."** It works for any closed loop in any circuit, no matter how many branches. The challenge in multi-loop circuits is picking enough independent loops to determine all the currents.

---

## Exercises

**Warm-up (Apply).** Three resistors: 10 Ω, 20 Ω, 30 Ω. Find the equivalent resistance for (a) all in series, (b) all in parallel, (c) 10 Ω in series with the parallel combination of 20 and 30.

**Apply.** A 9 V battery (internal resistance 0.5 Ω) drives a 100 Ω load. Find (a) terminal voltage, (b) current through the load, (c) power dissipated in the load, (d) power dissipated in the internal resistance.

**Apply.** A two-loop circuit: $\varepsilon_1 = 6$ V, $R_1 = 2$ Ω in the left loop; $\varepsilon_2 = 12$ V, $R_2 = 4$ Ω in the right loop; shared $R_3 = 3$ Ω in the middle. Use nodal analysis to find the current through $R_3$. Watch for sign conventions.

**Apply + Analyze.** A 12 V battery is connected to a 10 Ω resistor in series with a 100 Ω resistor. A digital voltmeter with internal resistance 10 MΩ measures the voltage across the 100 Ω resistor. (a) What voltage *should* appear across the 100 Ω resistor, ignoring the meter? (b) What does the voltmeter actually read, accounting for its 10 MΩ in parallel with the 100 Ω? (c) Now repeat for a meter with only 10 kΩ internal resistance.

**Challenge (Synthesize).** Show that for maximum power transfer from a source $\varepsilon, r$ to a variable external resistor $R$, the power delivered to $R$ is maximized at $R = r$, with $P_{\max} = \varepsilon^2/(4r)$. (Hint: take $dP_{\text{ext}}/dR = 0$.)

---

## LLM Exercises

### Build the interactive DC circuit simulator (`07-dc-circuits.html`)

> **Show.** Kirchhoff's laws: KCL at every node, KVL around every loop. Ohm's law: $V = IR$.
>
> **Say.** Build an interactive DC circuit simulator. Users drag resistors and batteries onto a grid; the simulator automatically solves the resulting circuit and displays currents and node voltages in real time.
>
> **Constrain.** D3 v7 for graphics. Components: resistor (with slider for $R$), ideal battery (with slider for $\varepsilon$), wire, ground. Snap-to-grid placement. As components are connected, automatically build the nodal-analysis matrix and solve via Gaussian elimination. Display: branch currents as animated orange arrows (length proportional to $|I|$, direction set by sign of $I$); node voltages as labeled values. Voltmeter and ammeter tools (drag onto the circuit, get a readout). Reset button. Filename: `07-dc-circuits.html`.
>
> **Verify.** (a) Simple series circuit (battery + 2 resistors in a single loop): current is the same through every resistor; voltages add correctly. (b) Simple parallel circuit: voltage is the same across each parallel branch; currents add correctly. (c) Multi-loop circuit (two batteries, three resistors, the worked example above): node voltage $\approx 5.78$ V and branch currents match.

### Exploration

- Build the worked-example two-loop circuit. Verify against your hand calculation.
- Build a Wheatstone bridge: four resistors in a diamond pattern with a battery across one diagonal and a galvanometer (very-high-resistance voltmeter) across the other. Find the balance condition where the galvanometer reads zero. Predict the condition algebraically before simulating.
- Add internal resistance to a battery and verify the loading effect: terminal voltage drops as you add load resistors in parallel.
- Build a voltage divider with $R_1 = R_2$ and an ideal voltmeter across $R_2$. Then attach a 10 kΩ load resistor in parallel with the voltmeter and watch the divider output change.

### Extension prompt (chapter bridge)

> **Show.** I've solved DC circuits. Now: what does a magnetic field do to a moving charge?
>
> **Say.** Modify or add a new simulator: a charged particle moves through a region with a configurable magnetic field. Show the trajectory.
>
> **Constrain.** A 2D canvas. Charge $q$ with slider (positive or negative). Initial velocity vector (sliders for $v_x, v_y$). Magnetic field $\vec{B} = B\hat{z}$ (out of the page) with slider for $B$. Solve Newton's second law $m\,d\vec{v}/dt = q\vec{v} \times \vec{B}$ numerically using RK4. Trace the trajectory.
>
> **Verify.** Charged particle with $\vec{v} \perp \vec{B}$: circular motion. Reversing the sign of $q$ reverses the direction of circulation. Doubling $B$ halves the radius.

Save as `07b-particle-in-magnetic-field-preview.html`. This is the lead-in to Chapter 8.

---

## What would change my mind

Kirchhoff's laws are not derived; they are statements of charge and energy conservation applied to circuits. Conservation of charge has been tested to extraordinary precision in particle physics; if charge were not conserved, KCL would fail. Conservation of energy is essentially axiomatic in macroscopic physics; KVL falls out as a corollary. A confirmed violation of either conservation law would force a deep rewrite — not just of this chapter, but of physics.

In real circuits, *parasitic effects* (capacitance between wires, inductance of leads, skin effect at high frequency) cause measured behavior to deviate from idealized DC analysis. These deviations don't invalidate KCL or KVL; they require modeling more circuit elements.

## Still puzzling

- *Where does the energy actually flow in a circuit?* Surprisingly subtle. The energy from a battery to a resistor flows not *through the wires* but *through the electromagnetic field surrounding the wires* (Poynting vector, Ch 11). The wires guide the energy; they don't carry it inside themselves. This is true and almost never taught at intro level.
- *Nonlinear elements.* Diodes, transistors, MOSFETs — most modern electronics depends on nonlinear elements. KCL and KVL still apply; Ohm's law does not. Industrial circuit simulators (SPICE) solve nonlinear systems iteratively.
- *Active devices add energy.* Op-amps, voltage sources, transistors — these don't merely pass energy along; they amplify. Active-circuit analysis goes beyond passive KVL/KCL but builds on it.

---

**Tags:** Kirchhoff's laws, resistors, series, parallel, nodal analysis, voltage divider, internal resistance, loading effect, Wheatstone bridge

