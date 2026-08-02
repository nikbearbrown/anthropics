# Chapter 15 — Thermodynamics

*Why two-thirds of your gasoline disappears as heat — and why that can't be fixed.*

---

A barrel of crude oil contains about 6.1 gigajoules of chemical energy. Refine it, ship it, pump fifty liters into a car. That tank holds roughly 1.7 GJ — enough, in principle, to lift the car sixty kilometers straight up. The car uses it to go about 700 km on a highway.

Where did the rest go?

Almost two-thirds left as heat — in the radiator, in the exhaust, in the warm undercarriage you can feel after a long drive. The engine converted only about 25–35% of the chemical energy into useful forward motion. This is not laziness in the automotive industry, not a failure of engineering that will be solved by a better design. It is because no engine that takes in heat at one temperature and exhausts it at another can exceed a specific, calculable maximum efficiency, and modern gasoline engines already operate close to that maximum.

The maximum was first derived in 1824 by a 28-year-old French military engineer named Sadi Carnot, watching coal-burning steam engines transform the British economy — working it out before the words *energy* and *thermodynamics* even existed in their modern form. His answer:

$$\text{Eff}_\text{max} = 1 - \frac{T_c}{T_h},$$

where $T_h$ is the absolute temperature at which the engine takes in heat and $T_c$ the temperature at which it exhausts. For a gasoline engine with combustion at about $2{,}200 \text{ K}$ and exhaust near $600 \text{ K}$, the theoretical ceiling is about $73\%$. Real engines lose another $40$ percentage points to friction, incomplete combustion, and geometry. The hard ceiling is set by law. The gap below the ceiling is engineering.

This chapter is about the two laws behind that ceiling, and what follows from them.

---

## The first law: the ledger

In the winter of 1782, Lavoisier and Laplace built a nested set of metal buckets in a Paris laboratory, surrounded the inner bucket with ice, and put a guinea pig inside. As the animal's body heat melted the ice, water dripped out, and they measured it. The mass of melt times the latent heat of fusion told them how many calories the animal had given off.

Then they had a separate apparatus burn an identical mass of the same food in pure oxygen and measured the combustion heat. The two outputs agreed within measurement error.

The animal was not a magical heat source. It was a slow-burning piece of food. The chemical energy of the food, oxidized by breathing, came out as heat at exactly the rate the chemistry predicted. Lavoisier and Laplace had stumbled into the first law of thermodynamics half a century before it was named. *Energy in equals energy out.*

More precisely, the **first law of thermodynamics** is:

$$\Delta E_\text{int} = Q - W,$$

where $\Delta E_\text{int}$ is the change in the system's internal energy, $Q$ is heat flowing *into* the system, and $W$ is work done *by* the system on its surroundings. Signs: heat in is positive, work out is positive. Internal energy rises if you add heat and falls if the system does work.

**Internal energy** is the sum of the kinetic and potential energies of every molecule in the system. For an ideal gas, it depends only on temperature: $E_\text{int} = \frac{3}{2}Nk_BT$ for a monatomic gas. Heat and work are not stored quantities — they are energy *in transit*, crossing the system boundary. A gas doesn't *contain* heat the way it contains internal energy. Heat is what happens to energy when it crosses a boundary because of a temperature difference. Work is what happens when it crosses a boundary through a mechanical displacement.

![Two scenarios. Allowed: hot coffee cools in a cool room; heat flows from coffee to air. Forbidden: room cools further so coffee heats up spontaneously — never observed. Both are consistent with the first law (energy...](../images/15-thermodynamics-fig-05.png)
*Figure 15.5 — Second Law — Heat Flows Hot to Cold Spontaneously, Never the Reverse*

The first law is just energy conservation with heat and work as the two channels. It says nothing about which direction energy flows. A puddle freezing on a hot sidewalk on a summer afternoon would not violate the first law — it would conserve energy perfectly. It just never happens. For that, we need the second law.

### Work on a PV diagram

A gas in a cylinder can be described at any instant by its pressure $P$ and volume $V$. Plot these with $P$ vertical and $V$ horizontal: every state of the gas is a point. Every process (quasi-static, slow enough to be reversible) is a path. The work done by the gas in a process is the area under that path:

$$W = \int P \, dV.$$

Four process types appear constantly:

**Isobaric** (constant pressure): a horizontal line. Work = $P\Delta V$, straightforward.

**Isochoric** (constant volume): a vertical line. No displacement, so $W = 0$.

**Isothermal** (constant temperature): for an ideal gas, $PV = nRT = $ constant, so the path is a hyperbola. Since $T$ doesn't change, $\Delta E_\text{int} = 0$, and by the first law, $Q = W$: every joule of heat in comes back as work out.

**Adiabatic** (no heat exchange): $Q = 0$, so $W = -\Delta E_\text{int}$. When the gas expands and does work, its internal energy — and temperature — drop. This is why a fire extinguisher nozzle gets cold, why a bicycle pump gets warm when you compress air quickly, and why the air rushing out of a punctured tire is chilly.

<!-- → [INFOGRAPHIC: PV diagram showing the four process types — horizontal line (isobaric), vertical line (isochoric), hyperbola (isothermal, labeled PV = const), and steeper-falling curve (adiabatic); shade the area under a short isobaric segment and label it W = PΔV; show that the enclosed area of a closed loop represents net work per cycle for a heat engine] -->

![Rectangular cycle on PV diagram: isobaric expansion (1→2), isochoric pressure drop (2→3), isobaric compression (3→4), isochoric pressure rise (4→1). Net work = enclosed area = ∮P dV. Clockwise = work output (engine),...](../images/15-thermodynamics-fig-02.png)
*Figure 15.2 — PV Cycle — Work Done Per Cycle Is the Enclosed Area*

A heat engine is a system that traces a closed loop in the $PV$ plane. The gas is heated, expands and does work, then is cooled and compressed back to its starting state. The net work per cycle is the area enclosed by the loop. The efficiency is

$$\text{Eff} = \frac{W}{Q_h} = 1 - \frac{Q_c}{Q_h},$$

where $Q_h$ is heat taken in from the hot source and $Q_c$ is heat dumped to the cold exhaust. The first law guarantees $W = Q_h - Q_c$. The second law, next, tells us how small we can make $Q_c$.

---

## The second law: the direction of things

Drop a single drop of black ink into a glass of still water. Watch it for ten minutes. The ink spreads into a plume, then a haze, then disappears into uniform gray. Wait a year. The ink will not regroup into a drop. Every individual molecular collision is reversible — the physics at the microscopic level runs equally well forward and backward. But the bulk un-mixing never occurs.

This is the second law.

The first law forbids you from getting more energy out than you put in. The second law forbids the un-mixing. It specifies the direction of time as a physical — not just a philosophical — fact.

The second law has been stated three different ways, all equivalent:

![Two schematics. Heat engine: hot reservoir delivers Q_H, engine produces work W, dumps Q_C to cold reservoir, η = W/Q_H. Refrigerator: cold reservoir delivers Q_C, with work input W, machine dumps Q_H = Q_C + W to hot...](../images/15-thermodynamics-fig-01.png)
*Figure 15.1 — Heat Engine and Refrigerator — Same Machine, Reversed Energy Flows*

**Kelvin–Planck:** No heat engine can operate in a complete cycle and have its sole result be converting heat from a single reservoir entirely into work. You cannot run an engine off a single warm bath. You need two reservoirs at different temperatures, and you must dump some heat into the cold one.

**Clausius:** Heat does not spontaneously flow from a colder body to a hotter one. It can be made to flow that way — a refrigerator does it — but only with work input.

**Entropy:** In any spontaneous process in an isolated system, the total entropy increases or stays the same:

$$\Delta S \geq 0.$$

Reversible processes have $\Delta S = 0$. Real processes, with friction or turbulence or finite-temperature-difference heat transfer, have $\Delta S > 0$. Nothing in an isolated system has $\Delta S < 0$.

All three are the same statement. The third is the most useful because it can be computed.

### Carnot's bound

Carnot showed that no engine operating between a hot reservoir at $T_h$ and a cold reservoir at $T_c$ can exceed

$$\text{Eff}_\text{Carnot} = 1 - \frac{T_c}{T_h}$$

![The Carnot cycle's four reversible processes: 1→2 isothermal expansion at T_H (Q_H absorbed), 2→3 adiabatic expansion (T drops to T_C), 3→4 isothermal compression at T_C (Q_C dumped), 4→1 adiabatic compression. Efficiency η =...](../images/15-thermodynamics-fig-03.png)
*Figure 15.3 — Carnot Cycle on PV — Two Isotherms + Two Adiabats, Highest Possible Efficiency*

![Plot of Carnot efficiency η = 1 − T_C/T_H vs hot-reservoir temperature T_H, with T_C = 300 K (room temperature). Reference markers: nuclear plant (T_H~600 K, η_theo 0.50, actual 0.33), coal plant (T_H~800 K, η_theo 0.62,...](../images/15-thermodynamics-fig-04.png)
*Figure 15.4 — Carnot Efficiency vs T_H — Theoretical Maxes and Real Shortfalls*

regardless of the working substance — gas, liquid, steam, anything. This follows from the entropy balance of a reversible cycle. In a reversible engine, entropy taken from the hot reservoir equals entropy delivered to the cold reservoir: $Q_h/T_h = Q_c/T_c$. Substituting into the efficiency formula gives the Carnot result immediately. Any irreversibility generates extra entropy that must be dumped to the cold reservoir, increasing $Q_c$ and lowering efficiency below the Carnot ceiling. Real engines always fall short.

For a pressurized-water nuclear reactor with steam at $T_h = 575 \text{ K}$ and cooling water at $T_c = 308 \text{ K}$:

$$\text{Eff}_\text{Carnot} = 1 - \frac{308}{575} \approx 46\%.$$

US nuclear plants achieve about $32\text{–}34\%$. The gap is not wasted engineering; it is irreversibility that no redesign can eliminate, because the cycle involves finite-temperature-difference heat transfers (inherently irreversible) and mechanical friction.

The practical implication of Carnot's formula: the single most leveraged variable in improving a heat engine is the hot-reservoir temperature $T_h$. Every increase in $T_h$ raises the ceiling. This is why aerospace engineers pursue higher turbine inlet temperatures with materials science, why supercritical steam plants run hotter than subcritical ones, and why every generation of power plant has involved better high-temperature materials.

### Refrigerators and heat pumps

A refrigerator is a heat engine running backward. You put in work $W$; the device pumps heat $Q_c$ from the cold interior to the warm kitchen. The total heat delivered to the kitchen is $Q_h = Q_c + W$ by the first law. The **coefficient of performance** is

$$\text{COP}_\text{ref} = \frac{Q_c}{W},$$

how much cooling you get per unit of work paid. The Carnot COP:

$$\text{COP}_\text{ref,Carnot} = \frac{T_c}{T_h - T_c}.$$

COP is not bounded by 1. A kitchen refrigerator (cold at $277 \text{ K}$, warm room at $300 \text{ K}$) has Carnot COP $\approx 12$; real refrigerators run around $2\text{–}4$.

A **heat pump** uses the same device to deliver heat to a warm space. Every joule of electrical work pumps several joules of heat from cold outside to warm inside:

$$\text{COP}_\text{HP} = \frac{Q_h}{W} = \frac{T_h}{T_h - T_c} \quad \text{(Carnot)}.$$

A heat pump moving heat from $0°\text{C}$ outside to $20°\text{C}$ inside has Carnot COP $\approx 14$; real heat pumps achieve around $3\text{–}4$. That means every joule of electricity delivers $3\text{–}4$ joules of heating — compared to a baseboard electric heater, which converts 1 joule of electricity to exactly 1 joule of heat (COP = 1). Heat pumps win because they are not generating heat, they are moving it.

<!-- → [INFOGRAPHIC: side-by-side diagrams of a heat engine and a refrigerator/heat pump — both showing Q_h flowing from T_h, Q_c flowing to T_c, and W flowing out (engine) or in (refrigerator); label the efficiency formula for the engine and the COP formula for the refrigerator; student should see that these are the same device run in opposite directions] -->

### Entropy

For a reversible heat transfer $Q$ at temperature $T$, the entropy change of the receiving system is:

$$\Delta S = \frac{Q}{T}.$$

When heat flows spontaneously from a $600 \text{ K}$ source to a $300 \text{ K}$ sink:

- Hot source loses entropy: $\Delta S_h = -1{,}000/600 = -1.67 \text{ J/K}$.
- Cold sink gains entropy: $\Delta S_c = +1{,}000/300 = +3.33 \text{ J/K}$.
- Universe total: $+1.67 \text{ J/K}$.

![Four particles in a two-side box. Macrostates by left-count: (4,0) has 1 microstate, (3,1) has 4, (2,2) has 6, (1,3) has 4, (0,4) has 1. Even split has the most microstates, hence highest entropy. With 10²³ particles, the...](../images/15-thermodynamics-fig-06.png)
*Figure 15.6 — Entropy from Microstates — S = k_B ln(W)*

Entropy increased. The process is spontaneous because it is overwhelmingly more probable. There are vastly more microstates corresponding to "energy spread between two objects at similar temperatures" than to "all the energy concentrated in the hotter one."

This is Boltzmann's formulation:

$$S = k_B \ln \Omega,$$

where $\Omega$ is the number of microscopic arrangements consistent with the macroscopic state. Boltzmann had it carved on his tombstone in Vienna. A drop of ink mixed through water has an astronomically larger $\Omega$ than a drop concentrated in one spot. The second law, in Boltzmann's language, says: *systems evolve toward more probable arrangements, because there are vastly more of them.*

The ink never un-mixes not because it is forbidden by any force, but because the probability of the unmixed state is something like $10^{-10^{23}}$ at every instant. Possible in principle; never observed in practice. The second law is a statement about overwhelming probability at macroscopic scales, enforced by the combinatorial structure of the universe.

<!-- → [INFOGRAPHIC: microstate counting illustration — left panel shows 4 gas molecules all in the left half of a box (1 macrostate, Ω = 1), right panel shows the same 4 molecules spread across the whole box (many macrostates, Ω = 16 for N=4); annotate with S = k_B ln Ω for each; student should see that the "spread out" macrostate has many more microstates and therefore overwhelmingly higher probability, making it the equilibrium state — and scale the argument to N = 10²³ to explain why unmixing is never observed] -->

---

## First law, second law, together

The two laws together govern every heat engine, every refrigerator, every metabolic process.

The first law sets the energy ledger. Whatever goes in must come out — as work, as heat, or stored. No engine can output more than its input.

The second law sets the direction and the ceiling. Heat flows from hot to cold. Engines cannot exceed Carnot. Entropy of an isolated system never decreases.

Put them together in a concrete example: a 1 GW coal plant burning at $T_h = 800 \text{ K}$, exhausting at $T_c = 300 \text{ K}$, delivering electricity at $35\%$ efficiency.

Carnot check: $1 - 300/800 = 62.5\%$. The plant's $35\%$ is physically permitted.

Heat input rate: $W/\text{Eff} = 10^9/0.35 \approx 2.86 \times 10^9 \text{ J/s}$.

Coal burn rate: $2.86 \times 10^9 / (3 \times 10^7 \text{ J/kg}) \approx 95 \text{ kg/s}$.

CO₂ at 2.5 kg per kg coal: $\approx 240 \text{ kg/s}$, about $7$ million metric tons per year.

Heat to the cold reservoir: $1.86 \text{ GW}$ — which is why coal plants need cooling towers taller than houses, releasing $1.86 \text{ GW}$ of heat into air or river water that didn't ask for it.

Scale that calculation down by $10^9$ and you have the metabolic budget of a small bird. The first law balances the energy budget; the second law sets the maximum work fraction; real efficiency falls below Carnot for the same reasons in both cases. Engines and animals obey the same laws.

<!-- → [INFOGRAPHIC: energy flow Sankey diagram for the coal plant — input arrow labeled 2.86 GW (chemical/heat in at T_h), splitting into two output arrows: 1 GW (electricity out, useful work) and 1.86 GW (heat rejected to cold reservoir at T_c); mark the Carnot maximum efficiency 62.5% and the actual efficiency 35% to show the gap between the physical ceiling and the engineering reality] -->

---

## Exercises

### Warm-up

**15.1** *(LO 1)* A gas absorbs $300 \text{ J}$ of heat from a reservoir and does $200 \text{ J}$ of work on its surroundings. (a) What is the change in internal energy? (b) If instead the gas is compressed and $150 \text{ J}$ of work is done *on* it while it releases $80 \text{ J}$ of heat, what is the change in internal energy?

**15.2** *(LO 2)* A gas at $1.5 \text{ atm}$ pressure expands isobarically from $3.0 \text{ L}$ to $7.0 \text{ L}$. ($1 \text{ atm·L} \approx 101.3 \text{ J}$.) (a) How much work does the gas do? (b) If the gas is ideal and its temperature rises from $300 \text{ K}$ to $500 \text{ K}$, what is $\Delta E_\text{int}$ for a monatomic gas? (c) How much heat was added?

**15.3** *(LO 4)* A Carnot engine operates between $T_h = 800 \text{ K}$ and $T_c = 320 \text{ K}$. (a) What is the maximum efficiency? (b) If the engine produces $2{,}000 \text{ W}$ of useful power, how much heat is it taking in per second from the hot reservoir?

**15.4** *(LO 5)* A refrigerator extracts $600 \text{ J}$ of heat from its interior per cycle using $150 \text{ J}$ of electrical work. (a) What is the COP? (b) How much heat is dumped into the kitchen per cycle? (c) If $T_c = 275 \text{ K}$ and $T_h = 295 \text{ K}$, what is the Carnot COP?

### Application

**15.5** *(LO 1, 4)* A car engine burns $1 \text{ L}$ of gasoline (energy density $32 \text{ MJ/L}$) at $28\%$ thermal efficiency. (a) How much mechanical work was produced? (b) How much heat was rejected? (c) If combustion occurs near $T_h = 2{,}000 \text{ K}$ and exhaust leaves at $T_c = 700 \text{ K}$, what is the Carnot maximum, and how does the actual efficiency compare?

**15.6** *(LO 4)* A geothermal power plant has hot brine at $180°\text{C}$ and cooling water at $20°\text{C}$. (a) Convert temperatures to kelvin. (b) What is the Carnot maximum efficiency? (c) If the actual plant achieves $40\%$ of the Carnot maximum, what fraction of input heat becomes electricity?

**15.7** *(LO 5, 6)* A heat pump is used to heat a house. Outside temperature: $-5°\text{C}$. Inside: $21°\text{C}$. (a) Compute the Carnot COP for heat delivery. (b) If the actual COP is $3.2$, how much electrical power is needed to maintain $4{,}500 \text{ W}$ of heating? (c) Compare to the electrical power needed if the house used baseboard electric resistance heating (COP = 1) instead.

**15.8** *(LO 6)* $500 \text{ J}$ of heat flows irreversibly from a body at $400 \text{ K}$ to a body at $250 \text{ K}$. Compute the entropy change of: (a) the hot body, (b) the cold body, (c) the universe. Verify that $\Delta S_\text{universe} > 0$, as required by the second law.

### Synthesis

**15.9** *(LO 1, 4)* A 70 kg cyclist climbs a $200 \text{ m}$ hill at $25\%$ mechanical efficiency. (a) How much work is done against gravity? (b) How much chemical energy was burned? (c) How much heat was released by the body? (d) Express the chemical energy in dietary kilocalories. (e) Compare to a published "calories burned" estimate for moderate cycling.

**15.10** *(LO 4, 6)* A combined-cycle natural gas plant uses a gas turbine ($T_h = 1{,}600 \text{ K}$, exhausting at $800 \text{ K}$) whose exhaust then drives a steam turbine ($T_h = 800 \text{ K}$, $T_c = 310 \text{ K}$). (a) Compute the Carnot efficiency of each stage. (b) If stage 1 receives $Q_1$ of heat input and operates at its Carnot maximum, how much work does it produce and how much heat exits to stage 2? (c) Compute the combined efficiency and compare to modern combined-cycle plants ($\sim 60\%$).

**15.11** *(LO 3, 6)* Consider $N = 4$ molecules in a box divided into two equal halves. (a) List all possible macrostates (number of molecules on the left: 0, 1, 2, 3, 4) and their multiplicities $\Omega$. (b) Compute the entropy $S = k_B \ln \Omega$ for each macrostate. (c) Which macrostate has maximum entropy? (d) Scale the argument: for $N = 10^{23}$, by what factor is the "all on left" macrostate less probable than the "evenly split" macrostate? Express as a power of 10.

### Challenge

**15.12** *(LO 4, beyond chapter)* You want to build the most efficient possible heat engine using ocean surface water ($T_h \approx 300 \text{ K}$, tropical) and deep ocean water ($T_c \approx 278 \text{ K}$, at depth). This is the basis of "ocean thermal energy conversion" (OTEC). (a) What is the Carnot maximum efficiency? (b) If a plant produces $1 \text{ MW}$ of electrical output at this efficiency, what heat-flow rates are required from the warm and cold reservoirs? (c) The low efficiency means enormous water flow rates — why is the technology still potentially viable?

**15.13** *(LO 3, 6, beyond chapter)* A Stirling engine operates in a four-step cycle: (1) isothermal expansion at $T_h$, absorbing $Q_h$; (2) isochoric cooling from $T_h$ to $T_c$, with heat $Q_r$ captured by a regenerator; (3) isothermal compression at $T_c$, rejecting $Q_c$; (4) isochoric heating from $T_c$ to $T_h$, using the stored $Q_r$. (a) Draw and label the PV diagram for this cycle. (b) Show that a perfect Stirling engine (ideal regeneration) achieves Carnot efficiency. (c) Explain qualitatively what "regeneration" means physically and why it is the key to the Stirling engine's efficiency.

---



By the end of this chapter you should be able to:

1. State the first law ($\Delta E_\text{int} = Q - W$) and apply it to compute internal energy changes, heat flows, or work for any thermodynamic process.
2. Identify isobaric, isochoric, isothermal, and adiabatic processes on a $PV$ diagram and compute the work done in each.
3. State the second law in all three forms (Kelvin–Planck, Clausius, entropy) and explain why they are equivalent.
4. Compute Carnot efficiency for a heat engine given $T_h$ and $T_c$ in kelvin, and explain why real engines fall short.
5. Compute the coefficient of performance for a refrigerator or heat pump and compare to the Carnot limit.
6. Compute entropy changes using $\Delta S = Q/T$ and reason about microstate counts using $S = k_B \ln \Omega$.

**Prerequisites.** Chapter 7 (work and energy). Chapter 13 (ideal gas, temperature in kelvin). Chapter 14 (heat transfer, $Q = mc\Delta T$).

**Why this chapter matters.** Every energy conversion you depend on — the gasoline engine, the power plant supplying your electricity, the air conditioner in summer, the metabolism keeping you alive — is governed by these two laws. The Carnot efficiency sets the ceiling; the engineering determines how close you get. Understanding both is what separates a physicist from someone who just reads fuel-economy labels.

---

## ↳ Dig Deeper — Why work and heat are not state variables

*Internal energy depends only on the current state of a system. Heat and work depend on the path taken to get there. This distinction shapes the entire mathematical structure of thermodynamics.*

**Prompt:**
> Explain the distinction between state functions (internal energy, temperature, pressure) and path functions (heat and work). Use a gas expanded from state A to state B by two different paths — isothermal, then adiabatic-then-isobaric. Show that $\Delta E_\text{int}$ is the same for both paths (depends only on endpoints), but $Q$ and $W$ are not. End with one sentence on why this is why we never speak of "the heat content of an object."

**What to do with the output:** Save it. The state-vs-path distinction is the mathematical key to enthalpy, free energy, and chemical thermodynamics in any later course.

---

## ↳ Dig Deeper — Why the Carnot bound depends only on temperature ratios

*The Carnot formula $1 - T_c/T_h$ is independent of the working substance. Understanding why requires the entropy bookkeeping of a reversible cycle.*

**Prompt:**
> Walk through why Carnot efficiency depends only on $T_c$ and $T_h$ and not on the working substance. Start with the entropy balance: in a reversible cycle, $Q_h/T_h = Q_c/T_c$. Combine with $W = Q_h - Q_c$ to derive $W/Q_h = 1 - T_c/T_h$. Then explain why no real engine can do better: any irreversibility generates extra entropy that must be dumped to the cold reservoir, increasing $Q_c$ and decreasing efficiency. End with one sentence on why turbine inlet temperature is the highest-leverage variable in power-plant design.

**What to do with the output:** Save it. The Carnot bound governs everything from your refrigerator to a fusion reactor. This derivation is worth carrying in your head.

---

## ↳ Dig Deeper — Entropy and the arrow of time

*The second law says entropy increases in isolated systems. But every fundamental microscopic law of physics is time-symmetric — it runs equally well forward and backward. How does the arrow of time emerge from time-symmetric microphysics?*

**Prompt:**
> Explain the relationship between the second law of thermodynamics and the "arrow of time." Start with the observation that individual particle collisions are time-reversible (Newton's laws, Maxwell's equations, quantum mechanics — all time-symmetric). Then explain how Boltzmann's $S = k_B \ln \Omega$ resolves the apparent paradox: the second law is not a fundamental law but a statistical fact about overwhelming probability at large N. Address the "past hypothesis" — the puzzling observation that the early universe appears to have been in an extraordinarily low-entropy state, which is what gives time its direction. End with one sentence on what would have to be true for the second law to be violated macroscopically.

**What to do with the output:** Save it. The arrow-of-time problem sits at the intersection of thermodynamics, statistical mechanics, and cosmology and remains one of the genuinely open questions in fundamental physics.

---

## LLM Exercise — Chapter 15: Efficiency and Entropy in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An efficiency calculation (and entropy estimate) for one heat-engine-like or work-conversion process in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 15 (Thermodynamics), I want to identify ONE energy-conversion moment in my phenomenon that operates as a heat engine, refrigerator, or biological metabolism, and compute an efficiency for it.

Please:

1. Identify the conversion. Examples:
   - Coffee maker: how much electricity → heat in coffee → heat lost to air?
   - Bike commute: chemical energy in food → mechanical work pedaling → heat dumped from body.
   - Marathon: same, integrated over 4 hours.
   - Car commute: chemical energy in gasoline → mechanical work → waste heat.
   - Espresso machine: electrical energy → boiler heat → pressure → kinetic water flow. Where does most energy go?

2. Identify T_hot and T_cold where applicable. Compute the Carnot bound. Compare to actual efficiency.

3. Estimate the entropy generated per use. Use ΔS = Q/T for the heat dumped to the cold reservoir.

4. Sanity check against published efficiency for a comparable system.

5. Identify the single most leveraged variable for improving efficiency — usually T_hot.

6. Connect to Chapter 16 if there's a periodic component — e.g., the cadence of cycling or the heating cycle of the coffee maker.

Save the output as logbook/chapter-15-thermodynamics.md.
```

### What this produces

Your fifteenth Logbook entry — an efficiency and entropy budget for the energy conversion in your phenomenon. By this entry, the Logbook has fifteen chapters of analysis built on the single anchor phenomenon you chose in Chapter 1.

### How to adapt this prompt

- *For phenomena without an obvious heat engine* (a static structure, a building): focus on HVAC heat losses and the COP of the heating/cooling system.
- *For biological phenomena:* the body is the engine; food is the fuel; metabolic heat is the waste.
- *For Claude Code:* if you have measured power input and output traces, compute time-averaged efficiency directly.

### Connection to previous chapters

Builds on Chapter 14's heat-transfer rates and Chapter 7's work-energy bookkeeping. Temperatures in kelvin (Chapter 13). First-law balance is the budget; second-law Carnot bound is the ceiling.

### Preview of next chapter

Chapter 16 begins oscillations and waves — periodic motion, springs, pendulums, simple harmonic motion. Energy trades between kinetic and potential in each cycle, with damping (entropy generation from Chapter 15) draining the amplitude over time.

---

## What would change my mind

The Carnot bound is among the most thoroughly tested results in physics. The argument would need revision if a future device — perhaps exploiting quantum coherence in a carefully engineered working substance — were shown to deliver work from heat above the Carnot bound for a given $T_h, T_c$ pair. No such device has been demonstrated. The second law is, as far as experiment shows, exact.

## Still puzzling

The deepest puzzle thermodynamics raises and cannot resolve: *why was the universe's entropy so low at the beginning?* The second law says systems evolve toward more probable — higher-entropy — arrangements. The natural prior would be a universe starting at high entropy. But every cosmological measurement points to an early universe in an extraordinarily low-entropy state — smooth, hot, nearly homogeneous. We can apply the second law beautifully going forward in time. Why time has the direction it does — why there is a "before" and an "after" at all — that remains open.

---

## AI Wayback Machine

**Sadi Carnot** wrote *Reflections on the Motive Power of Fire* in 1824 — establishing the theoretical limits of heat-engine efficiency before the laws of thermodynamics had been formalized. He died of cholera at 36, leaving the field to Clausius and Kelvin.

**Run this:**

```
Who was Sadi Carnot, and how does the Carnot cycle connect to the thermodynamics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Nicolas Léonard Sadi Carnot"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the four steps of the Carnot cycle and explain why no real engine can exceed its efficiency.
- Ask it about how Carnot's unpublished notebooks anticipated parts of the second law decades before it was formalized.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 16 begins oscillations — periodic motion, springs, pendulums. The energy bookkeeping habits from this chapter reappear: in an oscillator, kinetic and potential energies trade back and forth, with damping (entropy generation) draining amplitude over time. Chapter 17 extends to sound. Much later, quantum mechanics (Chapter 29) and statistical mechanics revisit the microstate-counting interpretation of entropy from this chapter. The second law you met here is, in a deep sense, the law that selects which direction time runs — and it will stay in the background of every physical process in the rest of the book.

---

**Tags:** thermodynamics, Carnot, entropy, heat-engines, second-law
