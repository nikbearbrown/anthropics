# Chapter 4 — The First Law of Thermodynamics

*Energy conservation, applied. Internal energy is a state function; heat and work are not.*

---

## The thing that never disappears

Start with a question that seems almost too simple: where does the energy go?

You charge a car battery. You leave the car parked in the cold for a week. You come back, turn the key, and the engine turns over sluggishly before catching. The battery is noticeably weaker. Where did the stored energy go? Some left as heat through the battery casing — the chemical reactions inside are slightly exothermic even at rest, and cold temperatures accelerate self-discharge. Some left in tiny currents through the car's electronics, the clock, the alarm system. Nothing disappeared. It all went somewhere. You just have to look in enough places to find all of it.

That is the first law of thermodynamics.

It sounds like an accounting rule, and it is — but accounting rules can be profound. The conservation of energy is one of the most precisely tested principles in all of physics. Every experiment, every reaction, every explosion and implosion and cooling process ever measured has come out with the ledger balanced. Not approximately balanced. Exactly balanced, to whatever precision the measurement allows. If you ever find a system where it seems not to balance, the right response is not "energy is not conserved" — it's "I haven't found where the missing energy went yet."

The first law says:

$$\Delta U = Q - W$$

$\Delta U$ is the change in internal energy of the system. $Q$ is the heat added to the system. $W$ is the work done by the system on its surroundings. The signs matter and are worth stating clearly: $Q > 0$ when the system absorbs heat; $W > 0$ when the system expands and pushes on something. If you compress a gas, you're doing work *on* the system, so $W < 0$ in this convention. Some chemistry books write $\Delta U = Q + W$ with $W$ meaning "work done on the system" — same physics, different bookkeeping. This book uses the physics convention throughout.

What exactly is $U$, the internal energy? It's the total microscopic kinetic and potential energy of all the molecules in the system. For an ideal gas — the model we'll spend most of this chapter and the next working with — it's simpler: no intermolecular forces, so no potential energy between molecules. All the internal energy is kinetic: the translational tumbling of atoms, the rotation of molecules, the vibration of their bonds. For a monatomic ideal gas (helium, neon, argon), each molecule has three translational degrees of freedom, and the equipartition theorem assigns $\tfrac{1}{2}k_BT$ to each:

$$U = \frac{3}{2}Nk_BT = \frac{3}{2}nRT$$

For a diatomic gas at moderate temperatures (nitrogen, oxygen, the air you're breathing now), rotation contributes two more degrees of freedom:

$$U = \frac{5}{2}nRT$$

In either case, $U$ depends only on the temperature. That's the crucial fact about ideal gases: if the temperature doesn't change, the internal energy doesn't change. This will simplify every calculation in the chapter.

<!-- → [FIGURE: Side-by-side molecular diagrams — monatomic gas (single sphere, 3 translational arrows) vs. diatomic gas (dumbbell shape, 3 translational + 2 rotational arrows). Caption: "Degrees of freedom determine U. Each mode holds ½k_BT. Count the arrows, multiply by N, get the internal energy."] -->

---

## What "state function" actually means

Here is the thing that trips people up, and it's worth getting exactly right before anything else.

Suppose I tell you that a gas is currently at temperature $T = 300$ K, pressure $P = 2$ atm, and volume $V = 10$ L. Those three numbers completely describe the state of the gas. From them you can compute the internal energy $U$, the enthalpy $H$, the entropy $S$ — everything thermodynamics cares about. These quantities are *state functions*: they depend only on where the gas is right now, not on the path it took to get there.

Heat and work are not like that.

Imagine taking that same gas from state A (300 K, 2 atm, 10 L) to state B (600 K, 4 atm, 10 L) by two different paths. Path 1: heat it at constant volume. Path 2: compress it first, then heat it, then let it expand. Both paths start at A and end at B. The internal energy change $\Delta U$ is the same on both paths — it depends only on the endpoints. But the amount of heat $Q$ absorbed, and the amount of work $W$ done, are different on the two paths. There is no way to talk about "the heat contained in the gas at state B." Heat is energy in transit, not energy stored. The moment the gas stops exchanging energy with its surroundings, there is no longer any heat — only internal energy.

This is not a semantic distinction. It has real consequences. If $Q$ were a state function, you could extract unlimited energy from a gas by cycling it through the right sequence of processes, since the "heat content" would reset each cycle. The fact that $Q$ is path-dependent is exactly what prevents perpetual-motion machines from working. The second law of thermodynamics will make this precise, but it begins here.

<!-- → [DIAGRAM: PV diagram showing two paths from state A to state B. Path 1: vertical line (isochoric) then horizontal (isobaric). Path 2: smooth diagonal curve. Shaded area under each path shown in different colors — student should see that the areas (= work done) differ, so Q must differ too, even though ΔU is the same.] -->

---

## The four basic processes

Thermodynamics is, in part, the study of what happens when you constrain a gas and then poke it. The four constraints you can impose are: fix the temperature (isothermal), fix the pressure (isobaric), fix the volume (isochoric), or insulate the system so no heat can flow (adiabatic). Each constraint simplifies the first law in a different way.

**Isothermal.** Fix $T$. Since $U$ depends only on $T$ for an ideal gas, $\Delta U = 0$. The first law immediately tells you $Q = W$: every joule of heat the gas absorbs goes directly into work it does on its surroundings. This is, perhaps, the hardest case to build intuition for — the gas is absorbing heat and its temperature isn't changing? Yes, because it's expanding at the same time. The energy flows in as heat and flows right back out as mechanical work. Temperature is a measure of internal energy per degree of freedom; if internal energy isn't accumulating, temperature isn't rising.

Work done in an isothermal process, for $n$ moles of ideal gas expanding from $V_1$ to $V_2$ at temperature $T$:

$$W = nRT \ln\frac{V_2}{V_1}$$

This comes from integrating $P \, dV$ with $P = nRT/V$ substituted in. The logarithm appears because $P$ drops as $V$ increases — you're integrating a hyperbola.

**Isochoric.** Fix $V$. No volume change means no $PdV$ work: $W = 0$. The first law reduces to $\Delta U = Q$. Every joule of heat you add raises the internal energy directly; none is "lost" to mechanical work. This is the simplest case to understand. Heating a gas in a rigid sealed container: all the heat stays as internal energy, temperature rises, pressure rises (by the ideal gas law), and that's it.

**Isobaric.** Fix $P$. The gas can expand, so it does work $W = P \Delta V$. The first law gives $Q = \Delta U + P\Delta V$. Using $\Delta U = nC_V \Delta T$ and the ideal gas law $P\Delta V = nR\Delta T$:

$$Q = n(C_V + R)\Delta T = nC_P\Delta T$$

This defines the molar heat capacity at constant pressure, $C_P = C_V + R$. The fact that $C_P > C_V$ has a clean physical meaning: at constant pressure, some of the heat you add goes into doing work on the expanding surroundings, so you need *more* heat to achieve the same temperature rise than you would at constant volume.

**Adiabatic.** No heat exchange: $Q = 0$. The first law gives $\Delta U = -W$. If the gas expands, it does positive work, so $\Delta U < 0$ — the internal energy drops and the temperature falls. If it's compressed, work is done on it, $\Delta U > 0$, and the temperature rises.

The adiabatic case is the one with the most striking physical consequences, so it's worth pausing on. A diesel engine has no spark plug. It ignites its fuel by compression alone: air is drawn in and compressed to roughly $\tfrac{1}{20}$ of its original volume in a fraction of a second. That process is fast enough to be nearly adiabatic. The temperature of the air, starting around 300 K, climbs to over 800 K — hot enough to ignite diesel fuel on injection. The work done compressing the air converts entirely into internal energy, which means heat. The piston is, in a sense, a heat pump — but there's no heat flowing anywhere. The temperature rises because work is being done on the gas, not because anything is being added.

The same physics in reverse: an adiabatic expansion cools a gas. This is how a bicycle pump gets warm when you inflate a tire (compression, not quite adiabatic but close), and how the air feels cold rushing out of a pressurized container (expansion, roughly adiabatic). It's also the physical basis for atmospheric temperature gradients — air that rises adiabatically cools, which is why mountain peaks are cold even when the lowlands are warm.

<!-- → [TABLE: Summary of the four processes — columns: process, constraint held fixed, W, Q, ΔU, physical example. Rows: isothermal (ΔU=0, Q=W), isochoric (W=0, ΔU=Q), isobaric (W=PΔV, Q=nCpΔT), adiabatic (Q=0, ΔU=-W). Physical examples: isothermal expansion of a gas in a heat bath; sealed rigid container; piston free to move at atmospheric pressure; diesel engine compression.] -->

---

## Worked example: same endpoints, different paths, different heat

Here is the calculation that makes the path-dependence of $Q$ and $W$ concrete.

Take $n = 2$ mol of diatomic ideal gas (air, approximately). Initial state: $T_1 = 300$ K, $P_1 = 1$ atm. Final state: $T_2 = 400$ K. Two ways to get there.

**Path A — sealed cylinder (isochoric).**

Rigid walls, no piston. $W = 0$ before we compute anything else.

$$\Delta U = nC_V \Delta T = 2 \cdot \frac{5}{2}(8.314)(100) = 4157 \text{ J}$$

Since $W = 0$: $Q = \Delta U = 4157$ J.

The gas absorbs 4157 J of heat. All of it goes into internal energy. Temperature rises from 300 K to 400 K, pressure rises proportionally (from 1 atm to $\tfrac{400}{300} \approx 1.33$ atm), volume stays fixed.

**Path B — frictionless piston (isobaric, $P = 1$ atm).**

The piston moves. Using the ideal gas law, initial volume $V_1 = nRT_1/P_1 \approx 0.049$ m³, final volume $V_2 = nRT_2/P_2 \approx 0.066$ m³.

$$W = P\Delta V = (101{,}325)(0.066 - 0.049) \approx 1665 \text{ J}$$

Internal energy change: same as before, because $\Delta U$ depends only on the temperature endpoints:

$$\Delta U = 4157 \text{ J}$$

Heat required: $Q = \Delta U + W = 4157 + 1665 = 5822$ J.

**Comparison.**

Both paths start at 300 K and end at 400 K. $\Delta U$ is identical: 4157 J either way — the gas doesn't remember how it got from one temperature to the other. But Path B required nearly 40% more heat input (5822 J vs. 4157 J), because 1665 J of it went into doing work on the piston rather than raising the temperature.

This is the physical content of $C_P > C_V$. To raise a gas's temperature by 100 K at constant volume, you supply $nC_V \Delta T$ of heat. To raise it by the same 100 K at constant pressure, you supply $nC_P \Delta T$ — more, because you also have to pay for the expansion work.

The "extra" heat is not wasted. It's the 1665 J that moved the piston — mechanical energy, available to do work on something else. The first law just tells you where it came from.

<!-- → [INFOGRAPHIC: Two-column energy-flow diagram. Left column (Path A): one arrow Q = 4157 J entering a box labeled "internal energy ΔU = 4157 J"; W = 0. Right column (Path B): one arrow Q = 5822 J entering, splitting inside the box into ΔU = 4157 J stored and W = 1665 J exiting as work on piston. Student should see: the ΔU box is the same size in both columns; Path B needs a larger Q to also fund W.] -->

---

## Enthalpy: a useful fiction for chemists

The calculation above hints at something. At constant pressure, heat absorbed equals $\Delta U + P\Delta V$. That combination comes up so often — in chemistry, in engineering flow problems, anywhere processes happen at constant atmospheric pressure — that it gets its own name:

$$H = U + PV$$

$H$ is the **enthalpy**. It's a state function (since $U$, $P$, and $V$ are all state functions). For a process at constant pressure:

$$\Delta H = \Delta U + P\Delta V = Q$$

So $\Delta H$ is the heat absorbed at constant pressure. Chemists tabulate $\Delta H$ for reactions (the "heat of reaction") because most chemistry happens in open beakers at atmospheric pressure, not in sealed containers. When you dissolve a salt and the solution gets cold, the dissolution is endothermic: $\Delta H > 0$. When you burn methane, $\Delta H < 0$ — heat is released. The enthalpy bookkeeping keeps track of the $P\Delta V$ work automatically, so you never have to think about it separately.

For an ideal gas:

$$\Delta H = n C_P \Delta T$$

with $C_P = C_V + R$ — the Mayer relation, which you can derive directly from $H = U + PV$ combined with the ideal gas law. The derivation is worth doing once: differentiate $H = U + PV$ with respect to $T$ at constant $P$, substitute $PV = nRT$, and you get $C_P - C_V = R$. The difference is exactly $R$ per mole — the work done per kelvin per mole of expansion against constant pressure.

One thing enthalpy is not: it's not a more fundamental quantity than internal energy. It's a convenience, defined to absorb the $P\Delta V$ work term for constant-pressure processes. In situations where pressure is not constant, or where you're tracking the system's microscopic energy directly, $U$ is what you want. Enthalpy is a tool, not a truth.

---

## What the first law rules out

The first law prohibits a particular kind of fantasy: a machine that produces more energy than it consumes. A *perpetual-motion machine of the first kind* — one that produces net work output with no energy input — would require $\Delta U < 0$ and $Q = W = 0$: internal energy decreasing while nothing flows in or out. The first law says this is impossible. The internal energy of an isolated system is constant.

Notice that the first law does *not* prohibit taking heat from a hot reservoir and converting it entirely into work. That's allowed by the first law as long as the bookkeeping balances. What prohibits it is the *second* law — the constraint on the *direction* of energy flow, not just its quantity. The second law is Chapter 6.

What the first law does rule out, precisely, is this: you cannot build a device that, over a complete cycle (returning to its original state after each cycle), produces net work without any heat input. If the device returns to its original state, $\Delta U = 0$ over the cycle, so $Q = W$: net work output requires net heat input. No net heat, no net work. Period.

---

## What's hidden in the ideal-gas assumption

Everything in this chapter assumes ideal gas behavior: $U = nC_VT$, $PV = nRT$, no intermolecular forces. Real gases deviate from this in two regimes.

At high pressure, molecules are close enough that repulsive forces raise $U$ above the ideal value. At low temperature, attractive forces pull molecules together and lower $U$. The van der Waals equation (Chapter 3) accounts for these corrections. For the processes we've been computing — near atmospheric pressure, moderate temperatures — the ideal-gas approximation is excellent.

But the moment a gas condenses into a liquid, or a solid melts, the ideal-gas framework breaks down completely. Phase transitions involve large changes in $U$ (the latent heat) with *no* change in temperature. The first law still holds — $\Delta U = Q - W$ is exact for real systems — but $\Delta U = nC_V\Delta T$ does not. A real treatment of steam engines, refrigerators, and atmospheric thermodynamics requires tracking internal energy through phase changes, which we'll return to in Chapter 8.

---

## Still puzzling

*Why does $U$ depend only on $T$ for an ideal gas?* Because there are, by definition, no forces between ideal-gas molecules. Potential energy requires forces. With no intermolecular forces, the only energy is kinetic — translation, rotation, vibration — and kinetic energy is a function of $T$ alone through the equipartition theorem. Real gases have intermolecular forces, so $U$ depends on both $T$ and $V$.

*What about open systems?* The first law as stated — $\Delta U = Q - W$ — is for closed systems: no matter crosses the boundary. Open systems, where fluid flows in and out (a turbine, a jet engine, your lungs), require an additional term for the energy carried by the flowing matter itself. That additional term is the flow work $PV$, which is why enthalpy $H = U + PV$ is the natural variable for steady-flow engineering analysis. The steady-flow energy equation is the first law for open systems. Chapter 9 takes this up.

*Is the first law exactly true, or just very well confirmed?* In classical physics, exactly true by definition: it follows from the assumption that energy is conserved, which is a consequence of time-translation symmetry (Noether's theorem). In quantum mechanics, energy-time uncertainty allows brief violations at the quantum level — but these average out over measurable timescales. For any macroscopic thermodynamic process, the first law holds to the precision of the best available measurements.

---

## Exercises

### Warm-up

**W1.** A gas absorbs 800 J of heat from its surroundings and simultaneously does 300 J of work by expanding against a piston. Find $\Delta U$. State whether the gas became warmer or cooler.

*Tests: direct application of $\Delta U = Q - W$ with explicit sign conventions. Difficulty: low.*

**W2.** One mole of monatomic ideal gas ($C_V = \tfrac{3}{2}R$) is heated at constant volume from $T_1 = 250$ K to $T_2 = 450$ K. Find $W$, $\Delta U$, and $Q$.

*Tests: isochoric process — recognizing $W = 0$ immediately collapses the first law to $\Delta U = Q$. Difficulty: low.*

**W3.** The same 1 mol of monatomic ideal gas is heated at constant pressure of 1.5 atm from 250 K to 450 K. Find $\Delta V$, $W$, $\Delta U$, and $Q$. Why is $Q$ larger here than in W2?

*Tests: isobaric process and the physical meaning of $C_P > C_V$. Difficulty: low.*

---

### Application

**A1.** Two moles of diatomic ideal gas ($C_V = \tfrac{5}{2}R$) expand isothermally at $T = 350$ K from $V_1 = 8.0$ L to $V_2 = 24.0$ L. Find $W$, $\Delta U$, and $Q$. Explain in one sentence why $\Delta U = 0$ even though the gas absorbed heat.

*Tests: isothermal process — distinguishing temperature from internal energy, applying the logarithmic work formula. Difficulty: medium.*

**A2.** A monatomic ideal gas undergoes adiabatic compression. Initial state: $T_1 = 300$ K, $V_1 = 12$ L. It is compressed to $V_2 = 3$ L. Using $TV^{\gamma-1} = \text{const}$ with $\gamma = 5/3$, find $T_2$. Then compute $\Delta U$ and $W$. Verify that $\Delta U = -W$.

*Tests: adiabatic process — using the adiabatic relation, connecting work to internal energy change with no heat term. Difficulty: medium.*

**A3.** A gas is taken from state A ($P = 1$ atm, $V = 5$ L, $T = 300$ K) to state B ($P = 1$ atm, $V = 10$ L, $T = 600$ K) by two paths. Path 1: isobaric expansion directly from A to B. Path 2: isochoric heating from A to intermediate state C ($P = 2$ atm, $V = 5$ L, $T = 600$ K), then isothermal expansion from C to B. Treat the gas as 0.20 mol of diatomic ideal gas. For each path compute $W$, $\Delta U$, and $Q$. Confirm that $\Delta U$ is the same on both paths and that $Q$ and $W$ differ.

*Tests: path-dependence of $Q$ and $W$ — the central conceptual result of the chapter, made numerical. Difficulty: medium-high.*

**A4.** Derive Mayer's relation $C_P - C_V = R$ for an ideal gas. Start from $H = U + PV$, use $PV = nRT$, and differentiate with respect to $T$ at constant pressure. Identify at each step what you are differentiating and why.

*Tests: algebraic reasoning about state functions — connecting $H$, $U$, and $PV$ through differentiation rather than memorization. Difficulty: medium.*

---

### Synthesis

**S1.** A sealed rigid container holds 3 mol of monatomic ideal gas at 400 K. A heating coil inside does 2,000 J of electrical work on the gas. Simultaneously, 500 J of heat leaks out through the walls. Find the final temperature. (Treat electrical work done on the system as $W = -2{,}000$ J in the physics convention; the heat leak is $Q = -500$ J.)

*Tests: first law with both $Q$ and $W$ nonzero and negative — requires careful sign-convention tracking in a non-standard setup. Difficulty: medium.*

**S2.** An engineer claims a cyclic engine that, per cycle, absorbs 1,200 J of heat from a hot reservoir, exhausts 400 J to a cold reservoir, and produces 900 J of net mechanical work. Evaluate this claim using only the first law. Is it possible? If not, what is the maximum net work the first law permits for these heat exchanges?

*Tests: applying the first law to a complete cycle ($\Delta U = 0$) to constrain engine output — directly sets up the efficiency questions of Chapter 6. Difficulty: medium.*

---

### Challenge

**C1.** Show that an ideal gas undergoing a reversible adiabatic process satisfies $PV^\gamma = \text{const}$, where $\gamma = C_P/C_V$. Start from $dU = -P\,dV$ (since $Q = 0$), substitute $dU = nC_V\,dT$ and the ideal gas law to eliminate $dT$, and integrate. Do not look up the result — derive it step by step, naming what you are eliminating at each stage.

*Tests: deriving the adiabatic relation from the first law — requires combining differential forms, substitution, and integration. Difficulty: high.*

---

## LLM Exercises

### Build the first-law visualizer (`04-first-law.html`)

> **Show.** First law: $\Delta U = Q - W$. For ideal gas: $\Delta U = nC_V \Delta T$. Process-specific formulas: isothermal $W = nRT \ln(V_f/V_i)$; adiabatic $W = -\Delta U$; isochoric $W = 0$; isobaric $W = P\Delta V$.
>
> **Say.** Build an interactive first-law energy-balance visualizer.
>
> **Constrain.** D3 v7. Controls: process type (isothermal / adiabatic / isochoric / isobaric), $n$ (mol), gas type (monatomic / diatomic — sets $\gamma$ and $C_V$), initial $T_0$, $P_0$, $V_0$, and a slider for the final-state parameter (final $T$, $V$, or $P$ depending on process type). Compute $\Delta U$, $Q$, $W$ for the process. Display: animated energy bar chart showing $U_\text{initial}$, $U_\text{final}$, and $Q$, $W$ as arrows in/out of the system. The first law $\Delta U = Q - W$ displayed with numerical values, verifying that the equation holds. Filename: `04-first-law.html`.
>
> **Verify.** Isothermal: $\Delta U = 0$, $Q = W$. Adiabatic: $Q = 0$, $\Delta U = -W$. Isochoric: $W = 0$, $\Delta U = Q$. Isobaric: $Q - W = \Delta U$.

### Exploration

- Run an adiabatic expansion of a monatomic gas from $T_1 = 600$ K to $V_2 = 2V_1$. Find $T_2$ and verify $TV^{\gamma-1} = \text{const}$.
- Compare isothermal and adiabatic expansions of the same gas with the same initial state to the same final volume. Which absorbs more heat? Which does more work? Why?
- Verify Mayer's relation $C_P - C_V = R$ in the simulation by comparing $Q$ for isobaric and isochoric processes that produce the same $\Delta T$.

### Extension prompt (chapter bridge)

> **Show.** I've computed $\Delta U$, $Q$, $W$ for individual processes. Now I want to visualize them on a PV diagram and chain multiple processes into a thermodynamic cycle.
>
> **Say.** Build an animated PV diagram showing process curves and computing work as area under the curve.
>
> **Constrain.** Plot the gas's state point on the PV diagram. Animate the process from initial to final state. The work $W = \int P\,dV$ should be shown as the shaded area under the curve. Cycle mode: chain 4 processes returning to the initial state; net work = enclosed area.
>
> **Verify.** Isothermal expansion: hyperbolic curve, positive work. Adiabatic expansion: steeper hyperbola, less work for the same $\Delta V$. Isochoric: vertical line, $W = 0$. Cycle: enclosed area = net work.

Save as `04b-pv-cycle-preview.html`. Bridge to Chapter 5.

---

**Tags:** first law of thermodynamics, internal energy, heat, work, state function, path function, ideal gas, enthalpy, Mayer's relation, sign conventions
