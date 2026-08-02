# Chapter 7 — Thermodynamics

*The engine, the refrigerator, and the one-way arrow.*

---

## The Guinea Pig in the Ice

In the winter of 1782, Antoine Lavoisier built a contraption in a Paris laboratory that looked like a nested set of metal buckets. The inner bucket held a guinea pig, surrounded by ice. As the animal's body heat melted the ice, water dripped out. Lavoisier measured the water. The mass of melted ice times the latent heat of fusion told him exactly how many calories the animal had released.

Then he burned the same mass of the same food in pure oxygen and measured the heat released by combustion. The two numbers agreed.

The animal wasn't a magical heat source. It was a slow-burning piece of food. The chemical energy of the food, oxidized by breathing, came out as heat at exactly the rate the chemistry predicted. Lavoisier had stumbled into the first law of thermodynamics half a century before anyone named it: energy in equals energy out.

But here's what Lavoisier's calorimeter couldn't tell him — and what took another seventy years to work out. The animal wasn't converting all its food energy into useful work. Neither is your car engine, your power plant, or any heat engine ever built. There is a ceiling on how much of any heat input can be turned into work, and that ceiling is set not by engineering but by the laws of nature. It was computed in 1824 by a 28-year-old French military engineer named Sadi Carnot, and it is one of the strangest results in all of physics.

This chapter is the story of why that ceiling exists, what sets it, and what it means.

---

## The First Law: The Ledger

Start with the bookkeeping.

The **first law of thermodynamics** is energy conservation dressed in thermal language. The change in the internal energy of a system equals the heat that flowed in minus the work the system did on its surroundings:

$$\Delta E_{\text{int}} = Q - W.$$

$Q$ is positive when heat flows in. $W$ is positive when the system does work on something else. Internal energy goes up when you add heat; it goes down when the system does work. This is the ledger. Every joule is accounted for.

**Internal energy** is the sum of all the kinetic and potential energies of every molecule inside the system. For an ideal gas, it depends only on temperature: $E_{\text{int}} = \frac{3}{2}Nk_BT$ for a monatomic gas. That's it — temperature is just molecular kinetic energy, and internal energy is the total of it.

The first law applies to everything: a gas in a piston, a battery discharging, a person climbing stairs, a star radiating into space. It says nothing about direction. It doesn't tell you whether heat will flow from hot to cold or cold to hot. It doesn't say what fraction of heat can become work. It's a conservation law — input minus output equals change in storage — and it's satisfied by processes that never happen just as well as by processes that do.

That's a feature, not a bug. The first law's universality is why it's the first law. The question of direction belongs to the second.

---

## The PV Diagram: Drawing the Engine

To think about heat engines, we need a picture. The right picture is a plot of pressure versus volume — the PV diagram.

A gas at any instant has a pressure $P$ and a volume $V$. Plot those as a point. Change the gas slowly — compress it, heat it, let it expand — and the point moves along a curve. That curve is a process. Close the curve back on itself and you have a cycle. The gas returns to its starting state and the whole thing repeats.

The reason PV diagrams are useful is this: the work done by the gas during any quasi-static process is the area under the curve,

$$W = \int P\,dV.$$

Expansion to the right: positive work, the gas pushes out on whatever is containing it. Compression to the left: negative work, something is pushing in on the gas. For a complete cycle, the net work is the area *enclosed* by the loop.

Four processes come up constantly, each defined by what stays constant:

**Isobaric** — pressure constant. Horizontal line on the PV diagram. Work is simply $W = P\Delta V$.

**Isochoric** — volume constant. Vertical line. No displacement, so $W = 0$. All the heat goes into changing the internal energy.

**Isothermal** — temperature constant. For an ideal gas, $PV = nRT$ is constant, so the path is a hyperbola. Since temperature doesn't change, neither does internal energy, so all the heat input comes back out as work: $Q = W$.

**Adiabatic** — no heat exchange. Common when a process is fast, so heat doesn't have time to flow. By the first law, $W = -\Delta E_{\text{int}}$: the work done comes entirely from the gas's internal energy. An adiabatic expansion cools the gas; an adiabatic compression heats it. This is why a bicycle pump gets warm when you compress air quickly — fast enough that the heat can't escape — and why the air from an aerosol can feels cold when it expands.

A heat engine is a device that runs a gas around a closed loop on the PV diagram: heat flows in at high temperature, the gas expands and does work, the gas is compressed back to its starting state, heat flows out at low temperature. The net work per cycle is the enclosed area. The **efficiency** is how much of the heat input becomes useful work:

$$\eta = \frac{W}{Q_H} = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H},$$

where $Q_H$ is the heat absorbed from the hot reservoir and $Q_C$ is the heat dumped to the cold reservoir.

---

## The Cyclist on the Hill

Let me work through the first-law bookkeeping with a specific case before we move to the second law.

A 70 kg cyclist climbs a hill, gaining 100 m of elevation in 30 minutes. Her body converts chemical energy to mechanical work at about 25% efficiency. How much food energy did she burn? How much heat did her body release?

Useful work done against gravity: $W = mgh = (70)(9.80)(100) = 68{,}600 \text{ J} \approx 68.6 \text{ kJ}$.

If that's 25% of the total chemical energy burned: $E_{\text{chem}} = W/0.25 = 274 \text{ kJ}$.

The other 75% became heat: $Q_{\text{heat}} = 274 - 68.6 = 205 \text{ kJ}$, released over 1800 seconds, giving a heat output rate of about 114 W — which is why you sweat on a hill climb.

Sanity check: 274 kJ is about 65 food kilocalories, roughly a small banana. A short uphill commute costs about a banana. That matches published metabolic estimates for recreational cycling.

Now the first law says nothing about the 25% figure. Why isn't it 80%? Or 100%? That's the second law's domain.

---

## The Second Law: Direction and the Ceiling

Drop a drop of black ink into a glass of still water. Watch. In ten minutes the ink disperses into a uniform haze. Now wait a year. The ink will not spontaneously regroup into a drop.

The molecular collisions that mixed the ink are still happening — every individual collision is microscopically reversible, consistent with Newtonian mechanics running forwards or backwards. The first law is satisfied either way. But the bulk un-mixing never occurs.

This is the second law.

It's been stated three ways, all equivalent:

**Kelvin-Planck:** No cyclic device can convert heat from a single reservoir entirely into work. There must always be a cold reservoir to dump some heat into.

**Clausius:** Heat does not spontaneously flow from a cold body to a hot one. It can be made to flow that way — a refrigerator does it — but only with work input.

**Entropy:** In any spontaneous process, the total entropy of an isolated system increases or stays the same. $\Delta S \geq 0$, always, for the universe as a whole.

These are the same statement wearing different clothes. Pick whichever framing helps for the problem at hand.

---

## The Carnot Bound

Carnot's question was sharp: among all possible engines operating between a hot reservoir at temperature $T_H$ and a cold reservoir at temperature $T_C$, which is the most efficient? And what is that efficiency?

His answer: build an engine made entirely of reversible steps. A **reversible** process is one that could, in principle, be run backwards without leaving any net change in the universe — no friction, no heat conduction across finite temperature differences, everything infinitely slow and quasi-static. An idealization, but a useful one as an upper bound.

The Carnot cycle has four legs: isothermal expansion at $T_H$ (heat $Q_H$ flows in), adiabatic expansion (temperature drops from $T_H$ to $T_C$, no heat flows), isothermal compression at $T_C$ (heat $Q_C$ flows out), adiabatic compression (temperature rises back to $T_H$, no heat flows). On the PV diagram it looks like a lens: two hyperbolic isotherms connected by two adiabats.

The efficiency of this engine:

$$\eta_C = 1 - \frac{T_C}{T_H}.$$

Temperatures in kelvin — absolute temperatures, not Celsius. At $T_H = 600$ K and $T_C = 300$ K: $\eta_C = 50\%$.

Now Carnot's theorem: *no engine operating between the same two reservoirs can exceed this efficiency*. The proof is a proof by contradiction. Suppose a super-Carnot engine exists with $\eta > \eta_C$. Use its work output to run a Carnot refrigerator between the same reservoirs. Tune the sizes so the refrigerator returns exactly as much heat to the hot reservoir as the engine took. Net result: the cold reservoir loses heat, the hot reservoir is unchanged, and no work was consumed. Heat has flowed spontaneously from cold to hot. That violates Clausius.

Since Clausius has never been violated in two centuries of physics, the super-Carnot engine cannot exist.

A corollary equally striking: all reversible engines operating between the same two reservoirs have the same efficiency. The working substance is irrelevant. Carnot showed this using steam; it would have been identical for ideal gas, liquid sodium, or a rubber band. This is deep — it means the Carnot efficiency isn't a property of any material, it's a property of the temperature difference alone. This is why we can define the kelvin temperature scale purely thermodynamically, without reference to any particular material's properties.

---

## What the Carnot Bound Actually Means

A modern coal-fired power plant burns fuel at around $T_H = 870$ K and rejects heat to a condenser at $T_C = 320$ K:

$$\eta_C = 1 - \frac{320}{870} \approx 63\%.$$

Real coal plants achieve about 40%. The gap is irreversibilities: heat exchangers running across finite temperature differences, turbine friction, pumping losses. Every departure from reversibility costs efficiency.

A gasoline car engine is worse. Peak combustion temperature around 2000 K, exhaust at 400 K:

$$\eta_C = 1 - \frac{400}{2000} = 80\%.$$

Real gasoline engines: 25–35%. The actual thermodynamic cycle used in a gasoline engine — the Otto cycle — isn't the Carnot cycle, so even a frictionless, perfectly quasi-static Otto engine would fall short of 80%. The rest of the gap is mechanical loss, heat conduction through cylinder walls, and finite combustion time.

The point worth emphasizing: the Carnot bound has nothing to do with friction. Remove all friction from an engine and it still can't exceed $\eta_C$. The limit is more fundamental — it follows from the impossibility of converting heat entirely into work in a cyclic process. That's a statement about the nature of heat and temperature, not about mechanical design.

---

## Refrigerators and Heat Pumps

Run the Carnot engine backwards. Instead of extracting work from a temperature difference, you put work in and pump heat from cold to hot. That's a refrigerator.

The figure of merit for a refrigerator is the coefficient of performance:

$$\text{COP}_{\text{ref}} = \frac{Q_C}{W},$$

how much heat you remove from the cold side per joule of work input. The Carnot bound:

$$\text{COP}_{\text{Carnot, ref}} = \frac{T_C}{T_H - T_C}.$$

For a freezer at $-18^\circ\text{C} = 255$ K in a kitchen at $22^\circ\text{C} = 295$ K: $\text{COP}_{\text{Carnot}} = 255/40 = 6.4$. Ideally, one joule of work removes 6.4 joules of heat from the freezer. Real refrigerators achieve COPs of 2–4.

A heat pump uses the same device but the goal is the heat delivered to the warm side, not the cold extracted:

$$\text{COP}_{\text{HP}} = \frac{Q_H}{W} = \text{COP}_{\text{ref}} + 1.$$

The Carnot bound for a heat pump between 0°C outside and 20°C inside (273 K and 293 K): $293/20 \approx 14.7$. Even a real heat pump achieving a quarter of this — COP of 3.6 — delivers 3.6 joules of heat for every joule of electricity. A resistance heater delivers exactly 1 joule per joule. The heat pump wins because most of the heat it delivers came from the cold outdoor air for free; the work just drives the transfer.

---

## Entropy

For a reversible heat transfer of $Q$ at absolute temperature $T$, the entropy change is:

$$\Delta S = \frac{Q}{T}.$$

Suppose 1000 J of heat flows reversibly from a reservoir at 600 K to one at 300 K. The hot reservoir loses entropy: $\Delta S_H = -1000/600 = -1.67$ J/K. The cold reservoir gains entropy: $\Delta S_C = +1000/300 = +3.33$ J/K. Total: $\Delta S_{\text{universe}} = +1.67$ J/K. Heat flows spontaneously from hot to cold, and the universe's entropy increases. This is the second law computed in joules per kelvin.

For a Carnot engine, by construction, the entropy changes cancel: the entropy lost by the hot reservoir at $T_H$ exactly equals the entropy gained by the cold reservoir at $T_C$. Net entropy change: zero. That's what it means to be reversible.

For any real engine falling short of Carnot, the entropy generated by irreversibilities is extra heat dumped to the cold reservoir — entropy that doesn't contribute to useful work. The closer you run to Carnot, the less entropy you generate per cycle.

The deeper picture, due to Boltzmann, connects entropy to counting. Define $\Omega$ as the number of microscopic arrangements (microstates) consistent with the macroscopic state you observe. Then:

$$S = k_B \ln \Omega,$$

where $k_B = 1.38 \times 10^{-23}$ J/K is Boltzmann's constant. The second law is true because there are astronomically more disordered arrangements than ordered ones. The ink disperses into the water not because spreading is *forced* by any microscopic law — every individual molecular collision is reversible — but because the spread-out configurations so vastly outnumber the concentrated ones that the system will almost certainly be found in a spread-out state. The second law is, at bottom, a statement about probability and counting.

---

## A Worked Example: The Coal Plant

A 1 GW coal plant burns coal at $T_H = 800$ K and exhausts to $T_C = 300$ K. It delivers electricity at 35% thermal efficiency. Coal has heat of combustion about 30 MJ/kg, and burning 1 kg releases about 2.5 kg of CO₂. How much CO₂ does the plant emit per second?

**Check the Carnot bound:** $\eta_C = 1 - 300/800 = 62.5\%$. The plant's 35% is below this — physically allowed.

**Heat input rate:** The plant outputs $W/t = 10^9$ J/s. At 35% efficiency, $Q_H/t = 10^9/0.35 \approx 2.86 \times 10^9$ J/s.

**Coal burn rate:** At 30 MJ/kg, the burn rate is $2.86 \times 10^9 / 3 \times 10^7 \approx 95$ kg/s.

**CO₂ rate:** $2.5 \times 95 \approx 240$ kg/s — about 20,000 metric tons per day, or 7 million metric tons per year.

**Heat dumped to the cold reservoir:** $Q_C/t = Q_H/t - W/t \approx 1.86$ GW — nearly twice the electrical output, going into a river or cooling tower. This is why coal plants need enormous quantities of cooling water and why those concrete cooling towers are so large.

Now scale down by $10^9$. The same arithmetic governs the 1 W metabolic heat output of a small bird. The first law balances the energy budget; the second law sets the maximum work fraction; both the plant and the bird fall below the Carnot limit for the same fundamental reason. Engines and animals obey the same laws.

---

## What the Second Law Doesn't Explain

Here is the honest stopping point.

The second law says entropy increases. Processes run toward greater disorder, toward more microstates. But the microscopic laws are time-symmetric — every molecular collision runs the same forwards and backwards. So why does the bulk behavior pick a direction?

The answer is statistical: disordered states are overwhelmingly more probable. A gas that has filled a room *could*, in principle, spontaneously concentrate into one corner — it's not forbidden by any microscopic law. It just has a probability so small that "impossible" is effectively accurate for any system with more than a handful of molecules.

But that raises a deeper question: why did the universe start in such a low-entropy state? The second law says entropy has been increasing since the beginning. That means the beginning had very low entropy. Why? That question lives at the boundary of thermodynamics and cosmology, and nobody has a complete answer.

The second law works beautifully going forward. Why time has the direction it does — why the initial conditions were special — is one of the genuinely open questions at the foundations of physics.

---

## Common Misconceptions

*"The first law tells you how efficient an engine can be."* It tells you energy is conserved. It says nothing about direction or efficiency. That's the second law's job.

*"A better engine could beat the Carnot limit."* The Carnot bound isn't an engineering limitation. No amount of better machining or smarter design crosses it. It follows from the impossibility of the Clausius violation, which has never been observed in nature.

*"Entropy is disorder."* It's a useful metaphor. Technically, entropy is the logarithm of the count of microstates. "Disorder" works as intuition but fails in edge cases — use the counting definition when you need to compute.

*"The Carnot formula works with Celsius temperatures."* It does not. $T_C$ and $T_H$ must be in kelvin. Putting in Celsius gives nonsense — and the error is hard to spot because the formula still produces a number between 0 and 1 for many inputs.

*"Refrigerators violate the second law."* They don't. Moving heat from cold to hot requires work, and the waste heat dumped to the room more than compensates for the local entropy decrease inside the refrigerator. Total entropy of the universe increases.

---

## What Would Change My Mind

The Carnot bound has been tested for two centuries in every heat engine built. No confirmed violation exists. A reproducible experiment showing an engine achieving efficiency above $1 - T_C/T_H$ — with all heat inputs and outputs properly tracked — would force a reconstruction of thermodynamics from the foundations. Quantum thermodynamics is an active research frontier; some quantum protocols extract work in surprising ways, but all so far remain consistent with the second law when entropy is properly accounted. The bound appears robust.

---

## Still Puzzling

*Why does entropy have the direction it does?* The microscopic laws are time-symmetric, yet bulk processes pick one direction. The answer involves probability — more disordered states are more numerous — but that only pushes the question back: why did the universe start with low entropy? This remains genuinely open.

*Maxwell's demon.* A thought experiment: a tiny demon opens a door between two halves of a gas box, selectively letting fast molecules through one way and slow molecules through the other. It seems to decrease entropy without doing work. The resolution: the demon must store information about each molecule, and erasing that information — necessary for any cyclic process — itself generates entropy. Information and thermodynamics are connected at a deep level. Chapter 10 returns to this.

---

## LLM Exercise — Chapter 7: Efficiency and Entropy in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An efficiency calculation (and ideally an entropy estimate) for one heat-engine-like or work-conversion process inside your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs.
My anchor phenomenon is [paste from Chapter 1].

For Chapter 7 (Thermodynamics), I want to identify ONE energy-conversion
moment in my phenomenon that operates as some kind of heat engine,
refrigerator, or biological metabolism, and compute an efficiency for it.

Please:

1. Identify the conversion. Examples:
   - Coffee maker: how much electricity → heat in coffee → heat lost to air?
   - Bike commute: chemical energy in food → mechanical work pedaling →
     heat dumped from body. What's the metabolic efficiency?
   - Car commute: chemical energy in gasoline → mechanical work moving
     the car → waste heat in radiator/exhaust.

2. Identify the relevant temperatures (T_hot reservoir, T_cold reservoir
   if applicable). Compute the Carnot bound. Compare to the actual
   efficiency.

3. Estimate the entropy generated per use. Use ΔS = Q/T for the heat
   dumped to the cold reservoir. Report in J/K.

4. State the inputs you used (sources, uncertainty).

5. Sanity check against published efficiency for a comparable system.

6. Identify the single most leveraged variable for improving the
   efficiency — usually T_hot. Explain why.

7. Connect to Chapter 8 (Oscillations) if there's a periodic component
   to your phenomenon.

Save the output as logbook/chapter-07-thermodynamics.md.
```

### What this produces

Your seventh Logbook entry — an efficiency and entropy budget for the energy-conversion in your phenomenon.

### How to adapt this prompt

- *For phenomena without an obvious heat engine* (a static phenomenon like a building): focus on heat losses through the envelope and the COP of any HVAC system.
- *For biological phenomena* (cycling, running, breathing): the body is the engine; food is the fuel; metabolic heat is the waste.
- *For Claude Code:* If you have measured power input and output traces, fit them and compute time-averaged efficiency directly.

### Connection to previous chapters

Builds on Chapter 6's Carnot analysis and Chapter 5's PV diagram work. The temperatures must be in kelvin. The first-law balance is the budget; the second-law bound is the ceiling.

### Preview of next chapter

Chapter 8 introduces oscillations — periodic motion, springs, pendulums, simple harmonic motion. The energy bookkeeping habits installed here reappear in any damped oscillator, where entropy generation drains the stored mechanical energy over time.

---

**Tags:** thermodynamics, Carnot, entropy, heat-engines, second-law, first-law, PV-diagram, refrigerator, heat-pump, COP
