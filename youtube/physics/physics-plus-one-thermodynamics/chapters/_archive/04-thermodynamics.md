# Chapter 5 — Thermodynamics

**TL;DR.** Energy is conserved. That's the first law, dressed up in thermodynamic clothing: $\Delta U = Q - W$. The internal energy of a system changes by exactly the heat added minus the work done by the system. What makes this non-trivial is the distinction between state functions and path functions — $U$ depends only on where you are, while $Q$ and $W$ depend on how you got there. Master that distinction and you can work out what happens to any gas in any process: isothermal, adiabatic, isochoric, isobaric. All four follow from the same bookkeeping.

---

## Fire without a match

A diesel engine has no spark plugs. Gasoline engines need a spark to ignite the fuel-air mixture. Diesel engines do not. Instead, they compress the air so rapidly and so forcefully — to about one-twentieth of its original volume — that the air gets hot enough to spontaneously ignite the fuel injected into it. No spark. The compression itself is the ignition source.

How? The piston moves so quickly that essentially no heat has time to flow in or out of the gas during compression. The process is adiabatic — $Q = 0$. And yet the temperature of the compressed air rises to around $700$–$900\text{°C}$, far above diesel fuel's ignition point. Temperature increased dramatically. No heat was added. What happened?

Work was done *on* the gas. The piston pushing inward transferred mechanical energy into the gas. That energy went somewhere — it went into increasing the kinetic energy of the gas molecules, which is to say, it increased the internal energy of the gas, which is to say, it raised the temperature. The energy didn't come from heat. It came from mechanical work. Same result: hot gas.

This is the first law of thermodynamics in its most vivid form. Internal energy can be changed by heat, or by work, or by both. These are two different ways to move energy across the boundary of a system. The first law just says that when you account for both, the books balance exactly.

---

## What internal energy actually is

Before we write down the first law, it's worth being clear about what we're talking about.

Internal energy $U$ is the total microscopic energy of a system. For a gas, that means the kinetic energy of all the molecules zipping around, plus whatever energy is stored in the rotational and vibrational modes of the molecules themselves. For a monatomic gas like helium, there are only three translational degrees of freedom — the molecule can move in $x$, $y$, and $z$ — and the internal energy is $U = \tfrac{3}{2}Nk_BT$. For a diatomic gas like nitrogen or oxygen, which can also rotate around two axes, there are five degrees of freedom and $U = \tfrac{5}{2}Nk_BT$. In both cases, $U$ depends on temperature and nothing else, as long as we're treating the gas as ideal.

That last phrase — "as long as we're treating the gas as ideal" — is doing some work. An ideal gas, by definition, has molecules that don't interact with one another except during brief elastic collisions. There's no potential energy stored between molecules. So there's no way for internal energy to depend on volume: squeezing the molecules closer together doesn't cost anything if they don't interact. All the internal energy is in the molecular motion, and molecular motion is what temperature measures. For an ideal gas, $U$ is purely a function of $T$.

Real gases have intermolecular forces, and for real gases $U$ depends weakly on volume too. But the ideal gas is a remarkable approximation for most situations we care about, and we'll use it throughout this chapter.

---

## The first law

Now we can state the principle. For a closed system — one where no matter crosses the boundary, only energy — the change in internal energy equals the heat added to the system minus the work done by the system:

$$\Delta U = Q - W.$$

The signs deserve a moment. $Q > 0$ means heat is flowing *into* the system from its surroundings. $W > 0$ means the system is doing work *on* its surroundings — expanding against a piston, say. So adding heat increases $U$; doing work decreases $U$. The formula is just a ledger: energy in minus energy out equals change in storage.

Some chemistry textbooks write $\Delta U = Q + W$ instead, where $W$ is defined as work done *on* the system rather than *by* it. Same physics, opposite sign convention for $W$. It's worth knowing both exist so you don't get confused when switching between texts. This chapter uses the physics convention throughout.

Notice what the first law does *not* say. It doesn't say that $Q$ and $W$ individually are determined by the initial and final states of the system. It says only that their difference $Q - W$ is. That asymmetry is the core of the subject, and it's where most of the interesting physics lives.

---

## State functions and path functions: the real content of the first law

Here is a thought experiment. Take a gas in a box at some initial state — call it state A, with a specific temperature, pressure, and volume. You want to bring it to a different final state B with a higher temperature. You have two routes.

Route 1: seal the box rigidly and add heat. The volume stays fixed. All the heat goes directly into raising the internal energy. $W = 0$, so $\Delta U = Q$.

Route 2: let the gas expand against a piston at constant pressure while you heat it. The gas does work on the piston as it expands. To reach the same final temperature as Route 1, you have to add *more* heat — some of it goes into the work of expansion.

Both routes end at the same state B — same temperature, and for an ideal gas, same internal energy. The internal energy change $\Delta U$ is identical for both paths. But the heat $Q$ is larger for Route 2, and the work $W$ is zero for Route 1 but positive for Route 2.

$\Delta U$ is a *state function*: it depends only on the endpoints A and B, not on how you traveled between them. $Q$ and $W$ are *path functions*: they depend on the specific process followed.

This distinction is worth sitting with, because it's subtle and it matters. Think of it in terms of altitude. If you hike from sea level to the top of a mountain, your change in altitude is determined entirely by where you started and where you ended. But the total distance walked depends on whether you took the direct trail or the winding switchbacks. Altitude is a state function; distance walked is a path function. $U$ is altitude; $Q$ and $W$ are like distance walked along different routes.

The mathematical statement is that $dU$ is an exact differential — it can be integrated without knowing the path — while $\delta Q$ and $\delta W$ are inexact differentials, their integrals are path-dependent. This is not a technical detail. It's the whole point.

Other state functions include temperature $T$, pressure $P$, volume $V$, and — a concept we'll develop later — entropy $S$. These all describe the *current condition* of a system, independent of history. Path functions like $Q$ and $W$ describe *processes*, not states. You can't say a gas "contains" $500\text{ J}$ of heat; you can only say $500\text{ J}$ of heat *flowed into* the gas along some particular path.

---

## Work done by a gas

Before going through specific processes, we need the formula for the work a gas does when it expands.

If a gas pushes against a piston with pressure $P$, and the piston moves by a small amount $dV$, the work done is $P\,dV$. For a finite process:

$$W = \int_{V_1}^{V_2} P\,dV.$$

This is the area under the curve on a pressure-volume diagram. Draw $P$ on the vertical axis and $V$ on the horizontal axis; the work done in any process is the area swept out between the initial and final states. Different paths between the same two states sweep out different areas — that's why $W$ is path-dependent.

For specific ideal-gas processes, the integral has closed forms. Isothermal expansion (constant temperature, so $P = nRT/V$): $W = nRT\ln(V_2/V_1)$. Isobaric expansion (constant pressure): $W = P(V_2 - V_1)$. Isochoric (constant volume): $W = 0$, trivially. Adiabatic: $W = -\Delta U = -nC_V(T_2 - T_1)$, since no heat flows.

---

## The four processes

With $\Delta U = Q - W$ and $\Delta U = nC_V\Delta T$ for an ideal gas, each of the standard processes is just a specific constraint applied to the first law.

**Isothermal.** Temperature is held constant, so $\Delta T = 0$ and therefore $\Delta U = 0$. The first law becomes $Q = W$: every joule of heat absorbed is converted to work. The gas expands, pushing the piston out, and heat flows in from the reservoir at exactly the rate needed to keep temperature constant. The gas is not storing any of that energy — it's a pure transducer, turning heat into mechanical work. This is why isothermal processes are important in the theory of heat engines.

**Adiabatic.** The system is thermally insulated — or the process happens too quickly for heat to flow. $Q = 0$. The first law becomes $\Delta U = -W$: work done by the gas comes entirely at the expense of internal energy, and temperature drops. Conversely, work done *on* the gas (compression) raises its temperature, with no heat involved. This is the diesel engine. Rapid expansion cools, rapid compression heats, and no heat crosses the boundary in either case. Adiabatic processes are steeper on a PV diagram than isothermal processes — for a given volume change, the pressure falls faster, because temperature is also falling.

**Isochoric.** Volume is held constant — a rigid sealed container. $W = 0$. The first law becomes $\Delta U = Q$: all the heat added goes directly into internal energy. Temperature rises. No work is done because no displacement occurs. The pressure rises proportionally with temperature. This is also called a constant-volume or isovolumetric process, and it's a good approximation for heating something in a sealed container.

**Isobaric.** Pressure is held constant — a gas in a cylinder with a freely moving, frictionless piston exposed to a constant external pressure. As the gas is heated, it expands, maintaining pressure. Work is done on the piston. The heat required is *more* than for the isochoric case that produces the same temperature rise, because some of the heat goes into the work of expansion. Quantitatively, $Q = \Delta U + W = nC_V\Delta T + P\Delta V = nC_V\Delta T + nR\Delta T = n(C_V + R)\Delta T = nC_P\Delta T$. This is why $C_P > C_V$: at constant pressure, heating costs more because the gas has to do expansion work as well as warm up.

---

## The same endpoint, different journeys

The isochoric and isobaric examples make the path-dependence concrete. Start with $2\text{ mol}$ of a diatomic ideal gas at $T_1 = 300\text{ K}$. Heat to $T_2 = 400\text{ K}$. In both cases, $\Delta U = nC_V\Delta T = 2 \cdot \tfrac{5}{2}(8.314)(100) = 4{,}157\text{ J}$. Same endpoints, same $\Delta U$.

In the isochoric case: $W = 0$, so $Q = 4{,}157\text{ J}$.

In the isobaric case: the gas expands. $W = P\Delta V = nR\Delta T = 2(8.314)(100) = 1{,}665\text{ J}$. So $Q = 4{,}157 + 1{,}665 = 5{,}822\text{ J}$.

To achieve the same temperature rise — the same final state — the isobaric path required nearly $1.4\times$ as much heat as the isochoric path, because $1{,}665\text{ J}$ had to be paid out as work on the piston. The extra heat didn't "disappear" — it became mechanical energy in the piston. The books balance.

This is why there are two heat capacities for a gas: $C_V$, the heat capacity at constant volume, measures how much heat is needed to raise the temperature by one degree when no work is done; $C_P$, the heat capacity at constant pressure, measures how much is needed when the gas is free to expand and do work. For ideal gases, $C_P = C_V + R$. The $R$ is the extra heat that goes into work at constant pressure. This is called Mayer's relation, and it falls directly out of the first law.

---

## Enthalpy: the chemist's state function

Chemists usually work at constant atmospheric pressure, not constant volume. Most chemical reactions happen in open beakers or flasks, not sealed rigid containers. For their purposes, the natural quantity to track is not $U$ but $H = U + PV$, called enthalpy.

Why $U + PV$? Because at constant pressure, $\Delta H = \Delta U + P\Delta V = \Delta U + W = Q$. That is: the change in enthalpy equals the heat exchanged at constant pressure. If a reaction absorbs heat at atmospheric pressure, $\Delta H > 0$ (endothermic). If it releases heat, $\Delta H < 0$ (exothermic). The sign of $\Delta H$ at constant pressure tells you directly whether you need to put energy in or whether you get energy out. That's useful.

$H$ is a state function, just like $U$. For an ideal gas, $PV = nRT$, so $H = U + nRT$ and $\Delta H = \Delta U + nR\Delta T = nC_V\Delta T + nR\Delta T = nC_P\Delta T$. The connection to $C_P$ rather than $C_V$ is not an accident — enthalpy is the natural energy variable for constant-pressure processes, just as internal energy is natural for constant-volume ones.

In chemistry, enthalpy shows up in Hess's law, heats of formation, and reaction enthalpy tables. The underlying reason it works is just that it's a state function: you can add or subtract $\Delta H$ values for different reactions and chain them together, because the answer depends only on endpoints. Path-independence is the gift that keeps giving.

---

## What the framework hides

The first law is energy conservation, and energy conservation is one of the deepest principles in physics — connected, via Noether's theorem, to the time-translation symmetry of physical laws. It's not going to be wrong. But the version stated here makes several assumptions worth naming.

The first is the ideal gas approximation. Real gases have intermolecular forces, so $U$ depends on volume as well as temperature. Near a phase transition — when a gas liquefies or a liquid freezes — $\Delta U$ can be large even when $\Delta T = 0$, because energy goes into changing the intermolecular potential rather than the kinetic energy. The first law still holds exactly; $\Delta U = nC_V\Delta T$ does not.

The second is the quasi-static assumption behind $W = \int P\,dV$. This formula assumes the process is slow enough that the gas is always in a well-defined equilibrium state with a uniform pressure. Real processes — explosions, shockwaves, rapid expansions — are not quasi-static. The work done in an irreversible process is always less than the reversible (quasi-static) maximum. The first law still holds, but the work integral no longer gives the right answer; you have to account for friction, turbulence, and other dissipative effects.

The third is what the first law doesn't tell you: the *direction* of processes. Energy conservation allows heat to flow from cold to hot — it doesn't violate $\Delta U = Q - W$ — but we know from experience that it never does spontaneously. The first law is silent on this. The second law, which we'll reach next chapter, supplies the missing constraint: not all processes that conserve energy actually occur. Only the ones that increase entropy do. The first law says *how much*. The second law says *which way*.

There is something deeper here that the formalism obscures. The distinction between $Q$ and $W$ — both just energy crossing a boundary — is actually somewhat arbitrary. Both are forms of energy transfer. The difference is one of organization: work involves coherent, macroscopic motion (a piston moving in one direction), while heat involves disordered, microscopic motion (random molecular collisions). At the molecular level, there is no fundamental difference between them. The distinction emerges from our coarse-grained, macroscopic description. When we say heat is "disordered" and work is "ordered," we are already approaching entropy — which is the quantitative measure of that disorder. That's next.

---

## LLM Exercises

### Build the first-law visualizer (`04-first-law.html`)

> **Show.** First law: $\Delta U = Q - W$. For ideal gas: $\Delta U = nC_V \Delta T$. Process-specific formulas: isothermal $W = nRT \ln(V_f/V_i)$; adiabatic $W = -\Delta U$; isochoric $W = 0$; isobaric $W = P\Delta V$.
>
> **Say.** Build an interactive first-law energy-balance visualizer.
>
> **Constrain.** D3 v7. Controls: process type (isothermal/adiabatic/isochoric/isobaric), $n$ (mol), gas type (monatomic/diatomic — sets $\gamma$ and $C_V$), initial $T_0$, $P_0$, $V_0$, and a slider for the final-state parameter (final $T$, $V$, or $P$ depending on process type). Compute $\Delta U$, $Q$, $W$ for the process. Display: animated energy bar chart showing $U_{\text{initial}}$, $U_{\text{final}}$, and $Q$, $W$ as arrows in/out of the system. The first law $\Delta U = Q - W$ displayed with numerical values, verifying that the equation holds. Filename: `04-first-law.html`.
>
> **Verify.** Isothermal: $\Delta U = 0$, $Q = W$. Adiabatic: $Q = 0$, $\Delta U = -W$. Isochoric: $W = 0$, $\Delta U = Q$. Isobaric: $Q - W = \Delta U$.

### Exploration

- Run an adiabatic expansion of a monatomic gas, going from $T_1 = 600\text{ K}$ to $V_2 = 2V_1$. Find $T_2$ and verify $TV^{\gamma-1} = \text{const}$.
- Compare isothermal and adiabatic expansions of the same gas with the same initial state to the same final volume. Which one absorbs more heat? Which one does more work? Why?
- Verify Mayer's relation: $C_P - C_V = R$ by comparing $Q$ for isobaric and isochoric processes that produce the same $\Delta T$.

### Extension prompt (chapter bridge)

> **Show.** I've computed $\Delta U$, $Q$, $W$ for individual processes. Now I want to visualize them on a PV diagram and chain multiple processes into a thermodynamic cycle.
>
> **Say.** Build an animated PV diagram showing process curves and computing work as area under the curve.
>
> **Constrain.** Plot the gas's state point on the PV diagram. Animate the process from initial to final state. The work $W = \int P\,dV$ should be shown as the shaded area under the curve. Cycle mode: chain 4 processes returning to the initial state; net work = enclosed area.
>
> **Verify.** Isothermal expansion: hyperbolic curve, positive work. Adiabatic expansion: steeper hyperbola, less work for the same $\Delta V$. Isochoric: vertical line, $W = 0$. Cycle: enclosed area = net work.

Save as `04b-pv-cycle-preview.html`. Bridge to Chapter 6.

---

## AI Wayback Machine

**James Prescott Joule** — a Manchester brewer's son with no university position — spent years in the 1840s meticulously measuring the mechanical equivalent of heat: how many joules of work correspond to one calorie of heat. His paddle-wheel experiments, where falling weights drove paddles through water and raised the water's temperature, established that heat is a form of energy, not a separate fluid called caloric. He measured the conversion to within about 1% of the modern value using equipment no more sophisticated than a thermometer and a pulley.

**Run this:**

```
Who was James Prescott Joule, and how did his experiments establish that heat is a form of energy rather than a fluid? Keep it to three paragraphs. End with the single most surprising thing about his career or methods.
```

→ Search **"James Prescott Joule"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain what the "caloric theory" of heat was, why it seemed plausible, and what experiments killed it.
- Ask it to describe the argument between Joule and the scientific establishment, and why his lack of academic credentials made it hard to get his work accepted.

What changes? What gets better? What gets worse?

---

**Tags:** first-law, thermodynamics, internal-energy, heat, work, state-function, path-function, ideal-gas, enthalpy, Mayer's-relation, adiabatic, isothermal, isochoric, isobaric
