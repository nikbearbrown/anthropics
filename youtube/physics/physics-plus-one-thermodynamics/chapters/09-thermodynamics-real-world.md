# Chapter 9 — Thermodynamics in the Real World

*Where Carnot bounds meet engineering reality: real cycles, real losses, real applications.*

---

## The heat pump that beats the furnace

A natural-gas furnace converts about 95% of the chemical energy in the gas into heat for your house. That sounds hard to beat. A modern air-source heat pump consumes one kilowatt-hour of electricity and delivers three to four kilowatt-hours of heat. That sounds like it violates conservation of energy.

It doesn't. The heat pump isn't creating energy — it's moving it. The extra two to three kilowatt-hours came from the cold outdoor air. The heat pump is a refrigerator running in reverse: it takes heat from outside (cold, but not zero) and pumps it into your house (warm), using electricity to drive the process uphill against the natural temperature gradient. The first law is satisfied. The second law is satisfied. The performance is just better than you might expect because you're not generating heat from scratch — you're relocating heat that already exists.

In a mild climate with cheap electricity, the heat pump costs less to operate than the gas furnace. In a very cold climate, the outdoor temperature gets close to the indoor temperature you're trying to maintain, the pump's performance degrades, and gas starts winning on cost. The crossover point is not a law of physics — it's an engineering and economic calculation that depends on local electricity prices, local fuel prices, and the local winter temperature distribution.

This is the chapter about how thermodynamics actually works in the field. Not the ideal Carnot engine with frictionless pistons and infinitely slow processes, but the machines real engineers design and operate: steam power plants, gas turbines, jet engines, refrigerators. Every one of them is bounded by Carnot. Every one of them falls short of Carnot by specific, identifiable amounts. The interesting physics is in understanding why they fall short, how much of the gap is recoverable in principle, and where the engineering frontier currently sits.

---

## Steam and the Rankine cycle

The steam power plant is the workhorse of large-scale electricity generation. Coal, natural gas, nuclear, geothermal, concentrated solar — all of them, at their core, heat water to make steam, use the steam to spin a turbine, and then condense the steam back into water to complete the cycle. The thermodynamic description of this is called the Rankine cycle.

The four steps are: heat water in a boiler until it becomes high-pressure steam, expand the steam through a turbine (which does work and drops in pressure and temperature), condense the exhaust steam back to liquid water in a condenser (rejecting heat to the environment), and pump the liquid back up to boiler pressure. The pump requires a small input of work; the turbine produces a large output. The difference is the net work of the cycle.

The Carnot efficiency for a plant with a boiler at 600°C (873 K) and a condenser at 40°C (313 K) is:

$$\eta_C = 1 - \frac{313}{873} = 64\%.$$

Modern coal and gas plants achieve about 35 to 45%. They're capturing roughly 60 to 70% of what Carnot allows. Where does the rest go?

Several places. The turbine doesn't expand steam perfectly isentropically — there's friction in the blades, heat loss through the casing, flow separation at off-design conditions. A real turbine has an isentropic efficiency of 85 to 92%: it extracts 85 to 92 cents of work for every dollar the ideal turbine would extract. The condenser operates with a finite temperature difference between the steam and the cooling water, generating entropy. Pipe friction causes pressure drops throughout the system. Combustion is incomplete.

Each of these losses has a name and a quantification. The isentropic efficiency of the turbine, $\eta_T = W_\text{actual}/W_\text{isentropic}$, tells you how much work you're actually getting versus the theoretical maximum. The isentropic efficiency of the compressor or pump, $\eta_C = W_\text{isentropic}/W_\text{actual}$, tells you how much extra work you're paying. These numbers come from measurements and from detailed fluid-dynamics calculations, and engineers spend careers trying to push them toward 100%.

Superheat is one of the practical tools. If you heat the steam beyond its saturation temperature at a given pressure — into the "superheated" regime where it behaves more like an ideal gas — you both increase the average temperature at which heat is added and reduce the moisture content in the turbine exhaust. Moisture droplets destroy turbine blades. Superheating solves two problems at once: it moves the average temperature $T_H$ upward (which the Carnot formula says improves efficiency), and it keeps the working fluid in a cleaner thermodynamic state throughout the expansion.

Reheat is a related strategy: expand the steam partway through the turbine, extract it, heat it again in a secondary boiler, and send it back in for the second half of the expansion. This is essentially running two Rankine cycles in sequence with a heat reinjection in between. It's operationally complicated and expensive, but modern ultra-supercritical coal plants use multiple reheat stages to push efficiencies toward 45 to 48%.

<!-- → [FIGURE: Rankine cycle schematic — four components in a loop: boiler (Q_H in), turbine (W_T out), condenser (Q_C out), pump (W_P in). Arrows show direction of fluid flow and energy transfer. A second panel shows the T-s diagram (temperature vs. entropy) for the ideal cycle with the four processes labeled. Caption: "The Rankine cycle in hardware and in thermodynamic state space. The area enclosed by the T-s loop is the net work output per unit mass of working fluid."] -->

---

## Gas turbines and the Brayton cycle

The gas turbine operates on a different thermodynamic cycle and has become the dominant technology for new power generation. Draw in air, compress it adiabatically, inject and burn fuel at roughly constant pressure, expand the hot combustion products through a turbine, exhaust to atmosphere. Four steps: adiabatic compression, isobaric heat addition, adiabatic expansion, isobaric exhaust. This is the Brayton cycle.

The ideal Brayton efficiency depends entirely on the pressure ratio — how much you compress the air before burning the fuel:

$$\eta = 1 - r_p^{(1-\gamma)/\gamma},$$

where $r_p$ is the ratio of high pressure to low pressure and $\gamma$ is the ratio of specific heats (about 1.4 for air). At a pressure ratio of 20, which is typical for a modern gas turbine:

$$\eta = 1 - 20^{-0.286} \approx 58\%.$$

Real simple-cycle gas turbines achieve about 35 to 40%. The gap from 58% to 38% is again a collection of specific losses: turbine blade cooling (you have to bleed cool compressor air to keep the blades from melting, which is parasitic work), compressor isentropic efficiency (you're putting in more work to compress than the ideal), combustion inefficiency, exhaust heat carried away at still-high temperature.

That last one — exhaust heat — is the most interesting. A gas turbine exhausts at 500 to 600°C. That's hot. If you throw that heat away, you've wasted a substantial energy stream. If you use it to drive a secondary Rankine steam cycle, you've captured most of it as additional electrical work.

This is the combined-cycle gas turbine, and it's where modern power generation is most efficient. The Brayton top cycle runs at 38% electric efficiency. Its hot exhaust (say, 600°C) drives a Rankine bottom cycle at perhaps 35% efficiency. The combined output:

Gas turbine captures 38% of the fuel as electricity. Of the remaining 62%, the Rankine cycle captures 35%, which is $0.35 \times 0.62 = 22\%$ of the original fuel. Total: $38 + 22 = 60\%$.

Modern advanced combined-cycle plants achieve 60 to 62% net electric efficiency — a factor of nearly two improvement over a simple gas turbine. The US Department of Energy's Advanced Turbine Program has targeted 65%, which would require higher firing temperatures, better cooling, and lower pressure losses throughout. It's a materials and engineering problem now more than a thermodynamics problem. The physics allows 65% or higher; the engineering is the constraint.

<!-- → [FIGURE: Combined-cycle plant Sankey diagram — fuel energy (100%) entering from the left; Brayton gas turbine on top extracting 38% as electricity; exhaust stream at 62% feeding the Rankine steam cycle below; steam cycle extracting 22% as electricity; final heat rejection of 40% to cooling tower on the right. Caption: "The combined cycle captures two successive bites from the same fuel stream. The Carnot ceiling for the overall system is set by the highest temperature (combustion, ~1400°C) and the lowest (condenser, ~40°C) — about 82%. The real plant achieves 60%."] -->

---

## Refrigeration and the vapor-compression cycle

A refrigerator is a heat engine running backwards. Instead of taking heat from a hot reservoir and converting some of it to work, you supply work and pump heat from a cold reservoir (the inside of the refrigerator) to a hot one (your kitchen). The measure of performance is the coefficient of performance:

$$\text{COP} = \frac{Q_C}{W},$$

where $Q_C$ is the heat removed from the cold space and $W$ is the work input. The Carnot COP for a refrigerator is:

$$\text{COP}_\text{Carnot} = \frac{T_C}{T_H - T_C}.$$

For a household freezer at $-15$°C (258 K) with the kitchen at 25°C (298 K), this is $258/(298-258) = 6.5$. Meaning: the ideal refrigerator would remove 6.5 joules of heat from the freezer for every joule of electrical work it consumes. Real household refrigerators achieve COPs of 2 to 4. They're running at about 30 to 60% of the Carnot limit.

The practical cycle is the vapor-compression cycle: compress low-pressure refrigerant vapor to high pressure (work in), condense it to liquid in the coils on the back of the refrigerator (rejecting heat to the kitchen), drop the pressure suddenly through an expansion valve (the throttling process — irreversible, and that irreversibility is a real efficiency cost), and let the low-pressure liquid evaporate inside the refrigerator (absorbing heat from the food). Repeat.

The throttling step is inherently irreversible. You're reducing pressure suddenly, which generates entropy. You can't avoid it entirely — you need to reduce the pressure somehow to get the refrigerant back to the low-pressure side. The expansion valve is simple, cheap, and reliable, but it wastes some of the work you put in at the compressor. An expansion turbine could recover some of that work, but it adds mechanical complexity. For household refrigerators, the valve wins on cost. For large industrial refrigeration plants, expansion turbines are sometimes worthwhile.

The history of refrigerants is a case study in thermodynamics colliding with environmental chemistry. The first widely used synthetic refrigerant, R-12 (dichlorodifluoromethane, a CFC), was introduced in the 1930s — non-toxic, non-flammable, stable. Thermodynamically excellent. By the 1980s it was clear that CFCs were accumulating in the stratosphere and destroying ozone. The Montreal Protocol of 1987 phased them out. R-134a (an HFC, no chlorine, no ozone depletion) replaced R-12. Then climate scientists noted that HFCs are potent greenhouse gases. The industry is now transitioning again, toward low-global-warming-potential refrigerants: R-32, propane (R-290), carbon dioxide (R-744). Each transition requires new compressor designs because the thermodynamic properties of the working fluid change the optimal pressure ratio and cycle parameters. The physics of the vapor-compression cycle stays the same. The engineering recalibrates around new working fluids.

<!-- → [TABLE: Refrigerant history — columns: refrigerant name, chemical family, ozone depletion potential (ODP), global warming potential (GWP), current status. Rows: R-12 (CFC, high ODP, high GWP, phased out), R-134a (HFC, zero ODP, high GWP, being phased out), R-32 (HFC, zero ODP, lower GWP, transitional), R-290/propane (natural, zero ODP, near-zero GWP, growing), R-744/CO₂ (natural, zero ODP, GWP=1, growing in commercial). Caption: "Each generation of refrigerant solves the environmental problem of the previous one while introducing a new constraint. The thermodynamic cycle is unchanged; only the working fluid and the hardware change."] -->

---

## Where heat goes: combined heat and power

A power plant running at 40% electrical efficiency throws away 60% of the fuel's energy as heat — usually to a river or a cooling tower. That heat is low grade (maybe 50 to 80°C after condensation), but it's real energy, and in northern Europe it heats buildings.

Combined heat and power (CHP), also called cogeneration, captures that rejected heat for district heating, industrial process heat, or desalination instead of dumping it to the environment. The electrical efficiency might drop slightly (the condenser operates at a higher temperature to deliver useful heat, which by the Carnot formula reduces the electrical conversion efficiency). But the total fraction of the fuel converted to something useful — electricity plus heat — can reach 80 to 90%.

Copenhagen runs much of its district heating from CHP plants. The same is true across much of Scandinavia and Central Europe. Industrial parks in Germany are designed so that a gas turbine's exhaust heat drives the factory's process heating, and the turbine's electricity powers the factory's motors. You're not beating Carnot — you're just using all of your allocation instead of dumping it.

The economic calculation depends entirely on whether there's a local use for the low-grade heat. In a dense cold-climate city, there is. In a rural warm-climate area, there usually isn't. This is why CHP penetration in the United States is lower than in Scandinavia: American building stock is lower density, and American winters are less severe on average, reducing the demand for district heat.

---

## Data centers as thermodynamic machines

A data center consuming 100 megawatts converts essentially all of that electricity into heat. A computation moves electrons through resistors, and in the thermodynamic accounting, the work done on the electrons becomes heat — immediately, completely, unavoidably, as far as classical thermodynamics is concerned. (Chapter 10 examines whether there's a fundamental minimum energy per computation; the answer from quantum information theory is yes, but current computers are far above that limit.) The data center is, from the building's perspective, a 100-megawatt electric heater.

The metric that captures how efficiently a data center handles this heat is the power usage effectiveness, or PUE:

$$\text{PUE} = \frac{\text{total facility power}}{\text{IT equipment power}}.$$

A PUE of 1.0 means every watt entering the facility goes directly to computation. A PUE of 2.0 means you're spending one watt on cooling and infrastructure for every watt on computation. Modern hyperscale data centers — Google, Microsoft, Meta — report PUEs of 1.1 to 1.2. Older facilities often run 1.5 to 2.0.

Getting from 1.5 to 1.1 is mostly thermodynamics and fluid mechanics. You want to cool the servers as directly as possible with as little temperature difference between the heat source and the coolant as possible, using as little fan and pump energy as possible. Free cooling — using outdoor air directly when the ambient temperature is low enough — eliminates the refrigeration cycle entirely. It's the thermodynamically cleanest solution: cold air already at the right temperature, no compressor required. This is why major data centers are built in Iceland, Sweden, Finland, and the Pacific Northwest. The local thermodynamics subsidize the operating cost.

---

## The climate as a heat engine

The largest thermodynamic machine on Earth isn't any power plant. It's the climate system.

Solar radiation delivers about 1361 watts per square meter to the top of the atmosphere. Averaged over the sphere and accounting for albedo (the fraction of sunlight reflected back to space), the Earth absorbs roughly 240 W/m². This heat drives the entire climate: evaporation, atmospheric circulation, ocean currents, weather.

The climate system converts some fraction of this absorbed solar energy into the kinetic energy of winds and ocean currents. Estimates put this at about 2 to 4% — roughly 4 to 7 petawatts out of 120 petawatts absorbed. The rest is re-radiated to space as thermal infrared without doing mechanical work.

What's the Carnot efficiency of this heat engine? Take the equatorial surface temperature as $T_H \approx 300$ K and the upper troposphere temperature as $T_C \approx 220$ K:

$$\eta_C = 1 - \frac{220}{300} = 27\%.$$

The atmosphere converts only about 2 to 4% of absorbed solar heat to kinetic energy, compared to a Carnot limit of 27%. The gap isn't surprising — the atmosphere isn't optimized to extract work. It loses efficiency to precipitation (condensation converts kinetic energy of rising air parcels to heat), to turbulent dissipation of winds back to heat through friction, and to the fact that most of the absorbed heat is at temperatures much lower than 300 K.

Climate change doesn't violate any thermodynamics. It shifts the boundary conditions. More greenhouse gases reduce the effective temperature at which Earth radiates to space (because the radiation now originates from a higher, colder layer of the atmosphere rather than from the surface), which means the equilibrium surface temperature must rise. The circulation patterns of the atmospheric heat engine change in response. The thermodynamic principles are exact and well-understood. The complexity is in the coupling between the dynamics, the chemistry, and the radiation physics.

<!-- → [FIGURE: Earth as a heat engine — schematic showing solar input (240 W/m² average) arriving at the surface, the atmospheric heat engine extracting ~2-4% as kinetic energy of winds and ocean currents, and the remainder re-radiated as infrared. Carnot efficiency bar (27%) shown alongside actual conversion efficiency (2-4%), with the gap labeled "irreversibility: precipitation, turbulent dissipation, absorption at low T." Caption: "The climate system is the largest heat engine on the planet. Its Carnot efficiency is 27%; it actually converts 2-4% of absorbed solar heat to mechanical work. The gap is not a design flaw — it's the second law operating at planetary scale."] -->

---

## What the efficiency gap is really about

Every real engine falls short of Carnot. That's not a failure of engineering — it's the second law. The question is how much of the gap is recoverable and how much is inherent.

Some losses are in principle recoverable. A turbine with better blade aerodynamics, closer tolerances, and more precisely controlled inlet conditions has higher isentropic efficiency. The gap between a 1970s gas turbine and a modern one is largely recovered from exactly this kind of engineering improvement. Some losses are economic rather than thermodynamic — larger heat exchangers mean smaller temperature differences across them, which means less entropy generation, which means higher efficiency, but they cost more capital. The engineer chooses the efficiency-cost tradeoff; physics doesn't fix it.

Some losses are inherent to the cycle choice. The throttling valve in a vapor-compression refrigerator is irreversible because the expansion is sudden and uncontrolled. You can replace it with an expansion turbine to recover some work, but the turbine has its own inefficiencies and costs. The free expansion of hot combustion gases into the turbine at conditions far from the working fluid's design point generates entropy that can't be recovered without fundamentally redesigning the cycle.

The Carnot efficiency is a ceiling derived from first principles. Every kilowatt of entropy generation between the hot reservoir and the cold one represents work you could have extracted but didn't. The engineering progress of the last two centuries has been, in large part, the story of identifying and reducing those entropy generation rates — with combined-cycle gas turbines, supercritical steam conditions, improved turbomachinery, and smarter heat integration — without ever crossing the ceiling.

<!-- → [CHART: Bar chart comparing ideal vs. actual efficiencies for Rankine, simple Brayton, combined-cycle CCGT, household refrigerator (COP as fraction of Carnot COP), and heat pump (COP as fraction of Carnot COP). Each bar pair shows: Carnot/ideal limit (dark) and real-world achieved (light). Caption: "The gap between ideal and real is different for each machine, but the pattern is the same: real devices run at 40-70% of their thermodynamic ceiling. The combined cycle is the closest to its ceiling; the household refrigerator is furthest."] -->

---

## Still puzzling

*Can quantum effects improve engine efficiency?* Quantum thermodynamics is a young field. There are proposals for quantum heat engines — operating on two-level quantum systems, using quantum coherence to enhance performance — that may slightly exceed classical limits in certain narrow regimes. Whether any of these effects are practically useful at engineering scales is unresolved.

*What is the ultimate efficiency of computing?* Rolf Landauer showed in 1961 that erasing one bit of information has a minimum thermodynamic cost of $k_B T \ln 2$ — about $3 \times 10^{-21}$ J at room temperature. Current transistors dissipate something like $10^{-15}$ J per operation — a million times Landauer's limit. There's thermodynamic room for a millionfold improvement in computational energy efficiency before fundamental physics becomes the constraint. Whether the engineering to capture that room is achievable is an open question.

*How much more efficient can combined cycles get?* The DOE Advanced Turbine Program targets 65% net electric efficiency for combined-cycle plants. Getting there requires firing temperatures above 1700°C, which requires either better ceramic thermal barrier coatings on turbine blades or novel cooling architectures. Materials science is the constraint, not thermodynamics.

---

## Exercises

### Warm-up

**W1.** A steam power plant operates with a boiler at 550°C (823 K) and a condenser at 35°C (308 K). (a) What is the Carnot efficiency limit? (b) If the plant actually achieves 40% efficiency, what fraction of the Carnot limit is that? (c) If 500 MW of heat enters the boiler, how much electrical power is generated and how much heat is rejected to the condenser?

*Tests: Carnot efficiency formula applied to a Rankine plant; using efficiency to split power between useful output and waste heat. Difficulty: low.*

**W2.** A household freezer maintains $-10$°C (263 K) in a kitchen at 22°C (295 K). (a) What is the Carnot COP? (b) If the actual COP is 2.8, how much electrical power does the refrigerator consume to remove 150 W of heat from the freezer? (c) How much heat is expelled to the kitchen?

*Tests: COP definition and Carnot COP for a refrigerator; tracking heat flows including the work input. Difficulty: low.*

**W3.** A gas turbine has a pressure ratio $r_p = 18$ and operates on air ($\gamma = 1.4$). (a) What is the ideal Brayton efficiency? (b) The turbine inlet temperature is 1300°C (1573 K) and the compressor inlet is 25°C (298 K). What is the Carnot efficiency for these temperatures? (c) Why is the Brayton efficiency lower than the Carnot efficiency?

*Tests: Brayton efficiency formula and comparison to Carnot ceiling; the student must recognize that the Brayton efficiency is for the ideal cycle, which still falls short of Carnot because heat addition and rejection occur over ranges of temperature, not at fixed temperatures. Difficulty: medium.*

---

### Application

**A1.** A gas turbine (simple Brayton cycle) with pressure ratio $r_p = 20$ and $\gamma = 1.4$ burns fuel at a rate equivalent to 400 MW of heat input. (a) Ideal Brayton efficiency? (b) Actual efficiency if turbine isentropic efficiency is 88% and compressor isentropic efficiency is 84%? (c) Electrical output and exhaust heat at actual efficiency?

To estimate actual efficiency from isentropic efficiencies: the work extracted by the turbine is reduced by $\eta_T = 0.88$, and the work consumed by the compressor is increased by $1/\eta_C = 1/0.84$. Use the ideal work values from part (a), then adjust.

*Tests: isentropic efficiency as the bridge from ideal to real cycle performance; quantifying how much each imperfect component costs. Difficulty: medium.*

**A2.** The exhaust from the gas turbine in A1 exits at 580°C (853 K). This waste heat is fed into a Rankine bottom cycle with a condenser at 40°C (313 K). The Rankine cycle achieves 33% of its Carnot limit. (a) What is the Carnot efficiency of the bottom cycle? (b) What is the actual bottom-cycle efficiency? (c) How much additional electricity does the bottom cycle generate from the exhaust stream? (d) What is the combined-cycle total efficiency?

*Tests: chaining two cycles in series using the waste-heat cascade; shows how combined-cycle efficiency emerges from sequential capture. Difficulty: medium-high.*

**A3.** A heat pump heats a house in winter. Outdoor temperature: 2°C (275 K). Indoor setpoint: 21°C (294 K). The heat pump runs at 45% of its Carnot COP. (a) What is the Carnot COP for heating? (b) What is the actual COP? (c) At what rate must the heat pump consume electricity to deliver 8 kW of heat? (d) Compare to an electric resistance heater delivering the same 8 kW. What fraction of the electricity does the heat pump save?

Note: COP for a heat pump (heating mode) $= T_H / (T_H - T_C)$.

*Tests: heat-pump COP in heating mode; comparison with resistance heating makes the efficiency advantage concrete. Difficulty: medium.*

---

### Synthesis

**S1.** A combined heat and power (CHP) plant burns 1000 MW of fuel. It generates electricity at 38% efficiency and captures 45% of the rejected heat for district heating (the remaining rejected heat is lost to the cooling system). (a) How much electricity is generated? (b) How much heat is available for district heating? (c) What is the overall energy utilization (electricity + useful heat, as a fraction of fuel input)? (d) Compare to: a standalone power plant at 38% efficiency plus a separate natural-gas boiler at 90% efficiency, each supplying the same electricity and heat. Which uses less fuel overall?

*Tests: CHP energy accounting and comparison to the separate-systems baseline — the canonical argument for why cogeneration saves primary energy. Difficulty: medium-high.*

**S2.** A data center consumes 80 MW of IT equipment power and has a PUE of 1.35. (a) What is the total facility power draw? (b) How much power goes to cooling and infrastructure? (c) The data center is in a warm climate where outdoor air cooling is unavailable; the chillers operate between a server-inlet temperature of 27°C (300 K) and an outdoor temperature of 35°C (308 K). What is the Carnot COP of this refrigeration system? (d) If the chillers run at 50% of Carnot COP, how much of the 80 MW of IT heat can be removed per watt of chiller electricity? (e) What PUE would be achieved if free cooling (COP → ∞) became available? What does this tell you about the thermodynamic value of data-center siting?

*Tests: PUE as an energy-accounting metric; connects refrigeration COP to operational cost and shows why geography matters thermodynamically. Difficulty: high.*

---

### Challenge

**C1.** Derive the ideal Brayton efficiency $\eta = 1 - r_p^{(1-\gamma)/\gamma}$ from first principles. Start from the four Brayton processes: (1) isentropic compression from $T_1$ to $T_2$, (2) isobaric heat addition from $T_2$ to $T_3$, (3) isentropic expansion from $T_3$ to $T_4$, (4) isobaric heat rejection from $T_4$ to $T_1$. Use the isentropic relation $T_2/T_1 = r_p^{(\gamma-1)/\gamma}$ for both the compression and expansion steps. Show that $T_3/T_4 = T_2/T_1$, then write the efficiency as $\eta = 1 - Q_C/Q_H = 1 - (T_4 - T_1)/(T_3 - T_2)$ and simplify.

*Tests: deriving the Brayton efficiency from the isentropic temperature relations — requires careful application of the isentrope relation at two different pressure ratios and algebraic simplification. Difficulty: high.*

---

## LLM Exercises

### Build the heat-engine efficiency explorer (`09-heat-engine-explorer.html`)

> **Show.** Various cycle efficiencies: Carnot ($1 - T_C/T_H$), Otto ($1 - 1/r^{\gamma-1}$), Rankine (depends on superheat, pressure), Brayton ($1 - r_p^{(1-\gamma)/\gamma}$).
>
> **Say.** Build an engine-efficiency comparison tool.
>
> **Constrain.** D3 v7. Engine selector (Carnot, Otto, Rankine simplified, Brayton, Vapor-compression refrigeration). Sliders for the relevant parameters: $T_H, T_C, r, r_p, \gamma$. Display: ideal efficiency from formula; actual efficiency (irreversibility slider, 0=ideal, 1=maximum losses); entropy generation rate; comparison Sankey diagram. Filename: `09-heat-engine-explorer.html`.
>
> **Verify.** (a) Carnot at $T_H = 600, T_C = 300$: 50% efficiency. (b) Otto at $r=10$, $\gamma=1.4$: 60% ideal. (c) Brayton at $r_p=20$, $\gamma=1.4$: 58% ideal. (d) Real engines at full irreversibility setting: half the ideal.

### Exploration

- Compare Otto and Brayton at the same compression ratio. Brayton is typically more efficient at lower pressure ratios; Otto wins at high.
- Build a refrigerator at $T_C = -18°$C, $T_H = 25°$C. The Carnot COP is 6.4; real COP 2.5–4.0. Why the gap?
- Try a CHP scenario (high-efficiency cycle followed by waste-heat recovery). Total energy utilization can exceed 80%.

### Extension prompt (chapter bridge)

> **Show.** Real engines lose efficiency to irreversibility. But where does the deepest irreversibility come from? Maxwell's demon suggests there might be a thermodynamic cost for *information*.
>
> **Say.** Build a Maxwell's-demon simulator showing the second law surviving information-processing.
>
> **Constrain.** A box with N particles, a "demon" at a door that opens for fast particles going one way. After M cycles, the demon's memory has stored M bits. Compute the entropy reduction of the gas; compare to the entropy cost of erasing the demon's memory at Landauer's bound.
>
> **Verify.** When you include memory erasure, total entropy of (gas + memory + environment) is non-negative — second law holds.

Save as `09b-maxwells-demon-preview.html`. Bridge to Chapter 10.

---

**Tags:** Rankine cycle, Brayton cycle, vapor-compression refrigeration, combined cycle, isentropic efficiency, combined heat and power, PUE, data center, climate thermodynamics
