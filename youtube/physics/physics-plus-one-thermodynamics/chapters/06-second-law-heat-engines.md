# Chapter 6 — The Second Law and Heat Engines

*The Carnot bound, the arrow of time, and why heat engines are limited.*

---

## The Embarrassing Question

Here is something that should bother you.

The first law of thermodynamics says energy is conserved. You can't create it or destroy it. Fine. But suppose I take a gas, expand it isothermally, let it do some work, and then ask: can I take all that work and convert it back into heat and exactly restore the gas to its starting state? The first law says yes — energy is conserved in both directions. Nothing in energy accounting forbids the reverse.

And yet. When you burn fuel in an engine, you cannot convert all of the heat into work. You always have to dump some heat to a cold reservoir. The smoke coming out of your car's exhaust isn't a design flaw — it's a fundamental constraint of nature. Every engine ever built, no matter how clever, no matter how frictionless, throws away some fraction of its heat as waste.

Why?

That's the question Sadi Carnot asked in 1824 — and answered — before anyone had even properly formulated the first law. His answer is one of the strangest and most powerful results in all of physics: the maximum efficiency of any heat engine depends only on the temperatures of its hot and cold reservoirs. Not on what fuel it burns. Not on what gas it uses. Not on how cleverly it's engineered. Only on the temperatures.

Let me show you why.

---

## What the Second Law Actually Says

The first law is about quantities: energy is conserved, full stop. The second law is about *direction*. It's a statement about which processes happen spontaneously and which don't.

There are two ways to say it, and they turn out to be the same thing.

**The Kelvin-Planck statement:** You cannot build a cyclic device that takes in heat from a single reservoir and converts all of it into work. There must always be a cold reservoir to dump some heat into.

**The Clausius statement:** Heat does not spontaneously flow from a cold object to a hot one.

Neither of these is a force law or an energy balance. They're statements about direction — about the fact that certain processes, while perfectly consistent with energy conservation, simply never happen. Hot coffee cools. It does not spontaneously heat up. A broken egg does not reassemble. Perfume diffuses across a room. It does not spontaneously concentrate back into the bottle.

The interesting thing is that these two statements — one about engines, one about heat flow — are logically equivalent. If you could violate one, you could violate the other. Suppose you could build a device that converts heat entirely into work — no cold reservoir needed. Take that work and use it to run a refrigerator, which pumps heat from a cold body to a hot one. Net result: heat moved from cold to hot with no other change in the universe. That's a violation of Clausius. Run the argument the other way and you get the same equivalence.

The two statements are the same law wearing different clothes.

---

## The Carnot Engine

Carnot's genius was to ask: among all possible engines operating between a hot reservoir at temperature $T_H$ and a cold reservoir at $T_C$, which one is the most efficient? And what *is* that maximum efficiency?

He constructed an ideal engine — the Carnot engine — made entirely of reversible steps. A *reversible* process is one that could, in principle, be run backwards without leaving any net change in the universe. It's an idealization: no friction, no finite temperature differences, everything infinitely slow and perfectly quasi-static. Real processes are never reversible; reversibility is an idealized ceiling.

The Carnot cycle has four legs:

**1→2. Isothermal expansion at $T_H$.** The gas is placed in contact with the hot reservoir and expands slowly. Heat $Q_H$ flows in from the reservoir at exactly $T_H$ — reversibly, because there's no temperature difference driving an irreversible flow. The gas does work.

**2→3. Adiabatic expansion.** The gas is removed from contact with any reservoir and continues to expand. No heat flows. The gas cools from $T_H$ down to $T_C$ by doing work at the expense of its internal energy.

**3→4. Isothermal compression at $T_C$.** The gas is placed in contact with the cold reservoir and compressed slowly. Heat $Q_C$ flows out to the reservoir at exactly $T_C$ — again reversibly. Work is done on the gas.

**4→1. Adiabatic compression.** The gas is removed from the cold reservoir and compressed back to its starting state. Temperature rises from $T_C$ to $T_H$. No heat flows.

On the PV diagram, this looks like a lens shape: two hyperbolic isotherms (at $T_H$ and $T_C$) connected by two adiabats. The enclosed area is the net work per cycle.

<!-- → [DIAGRAM: Carnot cycle on a PV diagram — two labeled isotherms (upper hyperbola at T_H, lower at T_C) connected by two adiabats; four states labeled 1, 2, 3, 4; arrows showing clockwise traversal; enclosed area shaded and labeled "W = net work"; caption: "Two temperatures, four legs, one lens shape — the most efficient engine thermodynamics permits."] -->

The efficiency of this engine is:

$$\eta_C = 1 - \frac{T_C}{T_H}$$

Temperatures must be in kelvin — absolute temperatures, not Celsius. At $T_H = 600$ K and $T_C = 300$ K, the Carnot efficiency is exactly 50%. Half the heat becomes work; half is dumped to the cold reservoir.

Now here is Carnot's theorem: *no engine operating between the same two reservoirs can exceed this efficiency*. Not a slightly different design. Not a cleverer gas. Not a better material. Nothing.

The proof is elegant. Suppose you have a super-Carnot engine with efficiency $\eta > \eta_C$, operating between the same $T_H$ and $T_C$. Use its work output to drive a Carnot engine running in reverse — as a refrigerator. Tune the sizes so the refrigerator pumps exactly as much heat into the hot reservoir as the super-engine takes out. Net result: the cold reservoir loses heat, the hot reservoir is unchanged, and no net work is done or consumed. Heat has flowed spontaneously from cold to hot with no other effect. That's a violation of the Clausius statement.

Since the Clausius statement is an axiom — it's never been violated in nature, in any experiment, ever — the super-Carnot engine cannot exist. $\eta_C$ is the absolute upper bound.

There's a corollary that's equally striking: *all reversible engines operating between the same two reservoirs have the same efficiency*. The working substance is completely irrelevant. Carnot proved this using steam; it would have been the same for ideal gas, liquid sodium, a rubber band, or anything else. The efficiency is a function only of $T_H$ and $T_C$. This is why the kelvin temperature scale can be defined thermodynamically — the Carnot efficiency gives you a way to compare temperatures that doesn't depend on any particular material's properties.

<!-- → [CHART: η_C = 1 − T_C/T_H plotted as a surface or family of curves — either a 2D plot of η_C vs T_C/T_H from 0 to 1, or a set of curves for fixed T_H (500 K, 1000 K, 2000 K) showing η_C vs T_C; student should see that η_C → 1 only as T_C → 0 K, and η_C → 0 as T_C → T_H; annotate real-world points: coal plant (T_H=870, T_C=320), car engine (T_H=2000, T_C=400), OTEC (T_H=300, T_C=280)] -->

---

## What the Carnot Bound Means in Practice

Let me put some numbers on this.

A modern coal-fired power plant burns fuel at around $T_H = 870$ K and rejects heat to a condenser at around $T_C = 320$ K. The Carnot efficiency is:

$$\eta_C = 1 - \frac{320}{870} \approx 63\%$$

Real coal plants achieve about 40%. They're operating at roughly two-thirds of the thermodynamic maximum. The gap comes from irreversibilities: heat exchangers operating across finite temperature differences, steam turbines with fluid friction, pumps with mechanical losses. Every source of irreversibility eats into the gap between real and Carnot.

A car engine is much worse. Peak combustion temperatures are around 2000 K; the exhaust dumps heat at around 400 K.

$$\eta_C = 1 - \frac{400}{2000} = 80\%$$

Real gasoline engines achieve around 25–35%. They're running at less than half the Carnot limit, and the gap is even larger than in the power plant case. A large part of it is the Otto cycle itself — the actual thermodynamic cycle of a gasoline engine — is not the Carnot cycle, so even a perfectly frictionless, perfectly quasi-static Otto engine would fall short of 80%. The rest is mechanical and thermal loss.

Now for a thought that might seem counterintuitive: the Carnot bound says nothing about friction. Even in a completely frictionless engine, you cannot exceed $\eta_C$. Friction makes engines worse, but removing friction entirely doesn't get you to 100% efficiency. The limit is deeper than friction — it's a statement about the nature of heat itself.

---

## Refrigerators and Heat Pumps

Run the Carnot engine backwards. Instead of heat flowing in at $T_H$ and work coming out, you put work in and heat flows from $T_C$ to $T_H$. That's a refrigerator.

The figure of merit for a refrigerator isn't efficiency — it's the coefficient of performance, or COP:

$$\text{COP}_{\text{ref}} = \frac{Q_C}{W}$$

How much heat do you remove from the cold side per joule of work input? The Carnot bound gives the maximum:

$$\text{COP}_{\text{Carnot, ref}} = \frac{T_C}{T_H - T_C}$$

For a household freezer at $-18^\circ\text{C} = 255$ K in a kitchen at $22^\circ\text{C} = 295$ K:

$$\text{COP}_{\text{Carnot}} = \frac{255}{295 - 255} = \frac{255}{40} = 6.4$$

Ideally, one joule of electrical work removes 6.4 joules of heat from the freezer. Real refrigerators achieve COPs of 2–4 — well below the Carnot limit, for the same reasons real engines fall short: irreversibilities in the compressor, heat exchangers operating at finite temperature differences, throttling valves that expand refrigerant irreversibly.

A heat pump is the same device, but we care about the heat delivered to the warm side rather than the heat removed from the cold side. You're heating your house by extracting heat from the cold outdoor air and pumping it inside. The COP:

$$\text{COP}_{\text{HP}} = \frac{Q_H}{W} = \text{COP}_{\text{ref}} + 1$$

The Carnot bound for a heat pump between 0°C outside and 20°C inside (273 K and 293 K):

$$\text{COP}_{\text{Carnot, HP}} = \frac{293}{293 - 273} = \frac{293}{20} \approx 14.7$$

Even if a real heat pump achieves only a quarter of the Carnot COP — say, 3.6 — it's still delivering 3.6 joules of heat for every joule of electricity. Compare that to a resistance heater, which delivers exactly 1 joule of heat per joule of electricity. The heat pump wins by a factor of 3.6, and it wins because most of the heat it delivers came from the outdoors for free. The work input just drives the transfer.

This is why heat pumps are one of the more interesting options in energy efficiency. The COP is always greater than 1 — you always get more heat out than work in — because the work isn't creating the heat, it's just moving it.

---

## A Worked Example

A real heat engine absorbs $Q_H = 1000$ J from a hot reservoir at $T_H = 800$ K and rejects $Q_C = 650$ J to a cold reservoir at $T_C = 400$ K.

**Actual efficiency:** $\eta = W/Q_H = 350/1000 = 35\%$.

**Carnot efficiency:** $\eta_C = 1 - 400/800 = 50\%$.

**The gap:** The engine is operating at 70% of the Carnot limit. Some irreversibility is eating 15 percentage points of efficiency.

Now let's track what happens to entropy. The hot reservoir at 800 K loses 1000 J, so its entropy changes by:

$$\Delta S_H = -\frac{1000}{800} = -1.25 \text{ J/K}$$

The cold reservoir at 400 K gains 650 J:

$$\Delta S_C = +\frac{650}{400} = +1.625 \text{ J/K}$$

Net entropy change of the universe per cycle: $-1.25 + 1.625 = +0.375$ J/K. The universe's entropy increased. The process is irreversible.

For a Carnot engine running between the same temperatures with the same $Q_H = 1000$ J: it would reject $Q_C = 500$ J (since $\eta_C = 50\%$). The cold reservoir's entropy change would be $+500/400 = +1.25$ J/K — exactly canceling the hot reservoir's $-1.25$ J/K. Net entropy change: zero. The Carnot cycle is reversible, which means it generates no entropy.

This is the connection between efficiency and entropy. Every departure from Carnot efficiency corresponds to entropy generation. The closer you run to Carnot, the less entropy you generate. The Carnot engine, running reversibly, generates none.

<!-- → [INFOGRAPHIC: Side-by-side Sankey diagrams — left: Carnot engine (Q_H=1000 J in, W=500 J out, Q_C=500 J rejected, ΔS_universe=0); right: real engine (Q_H=1000 J in, W=350 J out, Q_C=650 J rejected, ΔS_universe=+0.375 J/K); the "wasted" 150 J of extra heat rejection in the real engine highlighted in red; caption: "The gap between real and Carnot is exactly the entropy generated per cycle."] -->

---

## The TS Diagram

There's another way to draw thermodynamic cycles, using temperature $T$ on the vertical axis and entropy $S$ on the horizontal axis instead of pressure and volume.

On a TS diagram, a reversible isothermal process is a horizontal line (constant $T$, entropy changes as heat flows in or out). A reversible adiabatic process is a vertical line (constant $S$, since no heat flows and no entropy is generated). The Carnot cycle — two isothermals and two adiabats — becomes a rectangle.

The area enclosed by a cycle on the TS diagram equals the net heat absorbed, which for a complete cycle equals the net work. This is the direct analogue of the PV diagram, where enclosed area equals work. Each diagram reveals something the other hides: the PV diagram shows work clearly; the TS diagram shows entropy changes and irreversibility clearly.

For an irreversible engine, the cycle on the TS diagram is no longer a clean rectangle — the actual path taken by a real engine sprawls out from the ideal, and the entropy generation shows up as extra area that isn't contributing to useful work.

<!-- → [DIAGRAM: TS diagram (T vertical, S horizontal) showing two cycles on the same axes — Carnot: clean rectangle with corners labeled, horizontal isothermal legs at T_H and T_C, vertical adiabatic legs; Real engine: a rounded, distorted version of the same shape that bulges outward on the right, with the extra "irreversibility area" between real and ideal shaded and labeled "entropy generated"; caption: "The Carnot rectangle is what the cycle would look like if nothing were wasted. The bulge is waste."] -->

---

## What the Second Law Doesn't Explain

Here is the thing Carnot's analysis cannot tell you, and that thermodynamics as a whole still hasn't fully resolved.

The second law says entropy increases — processes run in the direction of increasing disorder, increasing entropy. But look at the microscopic level: every single collision between two molecules is reversible. Newton's laws are symmetric in time. If you film two molecules colliding and run the film backwards, both the forward and backward versions are perfectly consistent with the laws of mechanics.

So why does bulk behavior pick a direction?

The answer has to do with counting. There are enormously more ways for a gas to be spread throughout a container than concentrated in one corner. When you release gas into a vacuum, it spreads not because spreading is forced by some microscopic law, but because there are so many more ways to be spread than concentrated. The universe tends toward higher entropy because higher entropy states are overwhelmingly more probable — not because any law forbids the reverse.

This is a statistical argument, not a mechanistic one. And it immediately raises a harder question: if the laws are time-symmetric and the second law is about statistics, then in principle — with overwhelming improbability, but in principle — a gas that has filled a room could spontaneously concentrate back into one corner. This would violate the second law in the sense of decreasing entropy. The answer is that such events are not forbidden; they're just so improbable as to be irrelevant for any system with more than a handful of molecules. For a mole of gas, the probability is so small it makes "impossible" an understatement.

But the deeper puzzle remains: why did the universe start in such a low-entropy state? The second law works backwards in time just as well as forwards — it says entropy tends to increase, but it doesn't tell you why the initial conditions were special. That's an open question in cosmology, not thermodynamics. We'll come back to entropy more carefully in the next chapter.

---

## Common Misconceptions

*"A better engine could exceed the Carnot efficiency."* This is the most common one. The Carnot bound is not an engineering limitation — it's a consequence of the second law. Removing friction brings you closer to Carnot; it cannot take you past it. The limit comes from the temperatures of the reservoirs, not from any property of the engine.

*"Refrigerators violate the second law."* They don't. A refrigerator makes its interior colder — locally decreasing entropy — but it does so by doing work, and the waste heat dumped to the room more than compensates. The total entropy of the universe increases.

*"Heat pumps create energy."* They move energy. The heat delivered to a room is greater than the work input because most of it came from the cold outdoor air — collected for free, moved by the work input. No creation, only transfer.

*"100% efficiency is impossible only because of friction."* Even a perfectly frictionless Carnot engine running in finite time generates entropy and falls below 100%. At exactly 100% efficiency, $T_C = 0$ K — absolute zero — which is unattainable by another statement of the third law. The limit is more fundamental than friction.

---

## What Would Change My Mind

Every claimed violation of the second law in two hundred years of serious physics has turned out to be wrong, poorly accounted, or a result of misidentifying system boundaries. A reproducible, well-controlled experiment showing a heat engine achieving efficiency above $1 - T_C/T_H$ — with all heat inputs and outputs properly tracked — would force a reconstruction of thermodynamics from the foundation. No such experiment exists.

Quantum thermodynamics is a genuine frontier. There are quantum protocols that can extract work from systems in ways that look surprising classically. So far, every such result is consistent with the second law when the entropy of quantum states is properly accounted for. The boundary is active research, not settled physics — but no violation has appeared.

---

## Still Puzzling

*Why does the universe have an arrow of time?* The second law gives a direction — entropy increases — but the microscopic laws are time-symmetric. The asymmetry must come from initial conditions: the universe started in a peculiarly low-entropy state. Why that initial state? Nobody knows. It's one of the deepest open questions connecting thermodynamics, cosmology, and the foundations of quantum mechanics.

*Maxwell's demon.* Imagine a tiny demon controlling a door between two halves of a gas-filled box, letting fast molecules through one way and slow ones the other. It seems to sort hot from cold without doing work — violating the second law. The resolution: the demon has to store information about each molecule, and erasing that information (which must happen for a cyclic process) itself generates entropy. The second law wins. We'll come back to this properly when we have entropy in hand.

---

## Exercises

**Warm-up 1** *(Apply — Carnot efficiency)*. A Carnot engine operates between a hot reservoir at $T_H = 750$ K and a cold reservoir at $T_C = 300$ K. Find $\eta_C$. If the engine absorbs $Q_H = 2000$ J per cycle, find the net work output and the heat rejected.

**Warm-up 2** *(Apply — refrigerator COP)*. A refrigerator maintains a freezer at $-15^\circ\text{C}$ in a kitchen at $25^\circ\text{C}$. Find the Carnot COP for this refrigerator. If the compressor does 150 J of work per cycle, how much heat is removed from the freezer at the Carnot limit?

**Warm-up 3** *(Apply — heat pump)*. A heat pump warms a house at $20^\circ\text{C}$ by extracting heat from outdoor air at $-5^\circ\text{C}$. Find the Carnot COP for the heat pump. Why is this number greater than 1, and what does that mean physically?

**Application 1** *(Apply — real vs. Carnot)*. A real steam engine absorbs $Q_H = 5000$ J from steam at $500^\circ\text{C}$ and rejects heat to a condenser at $40^\circ\text{C}$. Its actual efficiency is 28%. Find: (a) the Carnot efficiency for these temperatures; (b) the actual work output; (c) the heat rejected; (d) the entropy generated by the universe per cycle.

**Application 2** *(Analyze — the equivalence proof)*. A device absorbs 1000 J from a hot reservoir at 600 K, produces 1000 J of work, and rejects nothing to any cold reservoir. Show, using a specific construction involving a Carnot refrigerator, that this device would allow heat to flow spontaneously from cold to hot — violating the Clausius statement. What is the minimum heat a real engine *must* reject to a cold reservoir at 300 K if it absorbs 1000 J from 600 K?

**Application 3** *(Apply — comparing engines)*. Three engines all operate between $T_H = 900$ K and $T_C = 300$ K. Engine A has $\eta = 55\%$. Engine B has $\eta = 67\%$. Engine C has $\eta = 35\%$. Identify which, if any, violates the second law. For each engine that doesn't violate the law, compute the entropy generated per cycle if $Q_H = 1000$ J.

**Synthesis 1** *(Analyze — the temperature gap)*. A power company wants to build a geothermal plant using hot underground water at $150^\circ\text{C}$ and rejecting heat to a river at $20^\circ\text{C}$. Find the Carnot efficiency. Compare to a coal plant operating between $600^\circ\text{C}$ and $35^\circ\text{C}$. Both plants must deliver 100 MW of electrical power. Compute the waste heat each must dump per second. Which is harder on the river?

**Synthesis 2** *(Analyze — COP and the energy bill)*. Your house loses 8 kW of heat to the cold outdoors on a winter day when inside is $20^\circ\text{C}$ and outside is $-10^\circ\text{C}$. Compare two ways to maintain the inside temperature: (a) electric resistance heating, (b) a heat pump with COP = 3.2. For each, find the electrical power required to keep the house at steady state. If electricity costs \$0.18/kWh, what is the daily cost difference?

**Challenge** *(Analyze + Apply — finite-time thermodynamics)*. The Carnot engine achieves maximum efficiency but requires infinitely slow operation (to maintain reversibility) and therefore produces zero power. A more useful quantity is the efficiency at *maximum power output*, derived by Curzon and Ahlborn in 1975:

$$\eta_{CA} = 1 - \sqrt{\frac{T_C}{T_H}}$$

For a steam plant with $T_H = 870$ K and $T_C = 320$ K: compute $\eta_C$, $\eta_{CA}$, and compare both to the real plant efficiency of about 40%. Which theoretical bound is the real plant closer to, and why does this make physical sense? (Hint: real plants must produce power in finite time.)

---

## LLM Exercises

### Build the Carnot cycle simulator (`06-carnot-cycle.html`)

> **Show.** Carnot cycle: two isothermals + two adiabats. Carnot efficiency $\eta_C = 1 - T_C/T_H$. No real engine can exceed this.
>
> **Say.** Build a Carnot cycle simulator with irreversibility control.
>
> **Constrain.** D3 v7. Split screen: PV diagram (left) and TS diagram (right). PV diagram shows two isotherms (at $T_H$, $T_C$) connected by two adiabats. TS diagram shows the rectangle. Controls: sliders for $T_H, T_C$ (both in K); slider for "irreversibility factor" (0 = Carnot ideal, 1 = maximally irreversible). At irreversibility > 0, the actual efficiency drops; show the gap as a red bar on a Sankey diagram of $Q_H, W, Q_C$. Numerical readouts: $\eta_C$, actual $\eta$, entropy generated per cycle. Filename: `06-carnot-cycle.html`.
>
> **Verify.** (a) $T_H = 600, T_C = 300$ K: $\eta_C = 0.5$. (b) Increasing $T_C$ toward $T_H$ reduces $\eta_C$ toward 0. (c) Irreversibility factor 1: efficiency drops dramatically; entropy generation rises.

### Exploration

- A Carnot engine between $T_H = 600$ K and $T_C = 300$ K has $\eta = 50\%$. Lower $T_C$ to 100 K: now $\eta = 83\%$. But to use $T_C = 100$ K, you need a cryogenic refrigerator that consumes more power than the engine produces. Real plants compromise.
- Run the cycle counterclockwise (reverse direction). The same shape, but now work is *added* (refrigerator mode). Compute the refrigerator's COP from the Sankey display.
- Compare Carnot efficiency for two power plants: a steam plant at $T_H = 870$ K / $T_C = 320$ K (a typical fossil plant) and an OTEC ocean-thermal plant at $T_H = 300$ K / $T_C = 280$ K (deep-ocean cold water vs. warm surface). OTEC efficiency is much lower because $\Delta T$ is small.

### Extension prompt (chapter bridge)

> **Show.** The Carnot cycle introduces a quantity that is conserved in reversible processes and *increases* in irreversible ones — entropy.
>
> **Say.** Build an entropy-counting simulator: a box of particles, plot the entropy as a function of distribution.
>
> **Constrain.** N=20 particles randomly hop between two halves of a box at each time step. Count microstates: $\Omega(n_{\text{left}}) = \binom{N}{n_{\text{left}}}$. Compute $S = k_B \ln \Omega$. Plot $S$ vs. time and watch it tend to the maximum.
>
> **Verify.** Starting with all 20 particles on the left ($\Omega = 1$, $S = 0$), the system evolves to about 10 particles per side ($\Omega = 184756$, $S = k_B \ln 184756 \approx 12 k_B$). Maximum entropy state.

Save as `06b-entropy-preview.html`. Bridge to Chapter 7.

---

**Tags:** second law, Kelvin-Planck statement, Clausius statement, Carnot cycle, Carnot efficiency, Carnot theorem, reversible process, irreversible process, refrigerator, heat pump, COP, TS diagram
