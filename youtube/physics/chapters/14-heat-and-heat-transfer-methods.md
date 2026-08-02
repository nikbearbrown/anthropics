# Chapter 14 — Heat and Heat Transfer Methods

*The floor isn't colder than the carpet. It just steals heat faster.*

---

Walk barefoot from a bedroom carpet onto a kitchen tile on a winter morning. The tile feels cold. Stick a thermometer on both surfaces — within measurement error, they're the same temperature. Room temperature. Neither is cold.

What your foot is measuring is not temperature. It's the *rate* at which energy is leaving your skin. The carpet is woven from wool fibers that trap still air between them. Air is a terrible conductor — energy seeps out of your foot through it slowly enough that your skin barely notices. The tile is a continuous ceramic lattice, and it pulls heat out of your foot about a thousand times faster than the trapped air does. Same temperature. Wildly different rate.

This is the central distinction of the chapter, and it's one that everyday language actively obscures. We say things like "the cold came in through the window" or "the heat is in the room" as if cold were a substance flowing inward and heat were a fluid pooling somewhere. Neither is right. Heat is what *moves* between two objects when their temperatures differ, and the interesting physics is not whether heat moves but *how fast* and *by what mechanism*.

---

## What heat is — and what it isn't

![Schematic of Joule's apparatus: descending mass turns a pulley that drives a paddle stirring water in an insulated vessel. The water's temperature rises by a measurable amount. Established 4.184 J of work per calorie of heat —...](../images/14-heat-and-heat-transfer-methods-fig-01.png)
*Figure 14.1 — Joule's Paddle Wheel (1845) — Mechanical Work Becomes Heat at a Fixed Ratio*

In the 1840s, James Joule set up an insulated tank of water with a paddle wheel inside it. He connected the paddle wheel to a rope, the rope to a pulley, and the pulley to a hanging weight. The weight fell. The paddle wheel turned. The water temperature rose.

Joule was doing something that seems obvious now but was genuinely controversial at the time: he was converting mechanical work into heat, and measuring both sides of the conversion carefully enough to get the ratio. The result:

$$1 \text{ kcal} = 4186 \text{ J}.$$

One kilocalorie — the amount of heat that warms one kilogram of water by one degree Celsius — is exactly 4,186 joules of mechanical work. The two things, heat and work, are not different substances; they're two paths to the same destination, internal energy.

<!-- → [FIGURE: Joule's paddle-wheel apparatus. Labeled components: hanging mass (shows gravitational PE), rope and pulley, paddle wheel inside insulated water tank, thermometer in water. Arrow showing mass falling, arrow showing paddle rotating, arrow showing temperature rising. Caption: Joule's experiment converted a measurable mechanical energy (mgh) into a measurable temperature rise (mc∆T), establishing that 1 kcal = 4186 J. The conceptual point: two physically different paths — work and heat — produce identical changes in internal energy.] -->

Before Joule, the dominant theory was *caloric* — that heat was a weightless fluid carried inside hot objects and released when they cooled. The caloric theory made many correct predictions, which is why it lasted until the 1840s despite being wrong. What finally killed it was the simple observation that you can do unlimited work and generate unlimited heat from a single object (a cannon being bored, in Count Rumford's experiment; a water tank, in Joule's), without the object running out of "caloric fluid." Heat is not a thing an object has. It's a flow of energy.

The precise definition: **heat** is the spontaneous transfer of energy driven by a temperature difference. Not energy stored — energy *moving*. A coffee cup at 80°C contains internal energy; the flow of energy from cup to air is heat. When the cup reaches room temperature, the flow stops. After that, there is no more heat, even though the cup still contains plenty of internal energy.

![Two side-by-side panels showing a barefoot on tile (k=2.5 W/m·K, feels cold) vs carpet (k=0.04 W/m·K, feels warm) — both at the same 18 °C. Bottom: log bar chart of k values from aerogel 0.013 to silver 429.](../images/14-heat-and-heat-transfer-methods-fig-02.png)
*Figure 14.2 — Tile vs Carpet — Skin Reports Heat-Flow Rate, Not Temperature*

This definition rules out "the room feels cold" as a physical claim about the room. What's cold is the rate of heat transfer away from your body — which depends not just on the temperature difference but on what's between you and the surroundings. A tile and a carpet at the same temperature offer different resistances to that flow. The tile feels colder because it moves heat faster.

---

## Specific heat: why water is special

Pour 250 mL of water into a copper-bottomed pan and put it on a 1,500-watt burner. Now do the same with cooking oil. The oil heats faster. Not because oil and water are at different temperatures or because the burner outputs more power — but because water resists being heated more strongly than almost any other common substance.

The number that captures this resistance is the **specific heat** $c$: the energy required to raise one kilogram of a substance by one degree Celsius. Formally:

$$Q = mc\Delta T,$$

where $Q$ is the heat added in joules, $m$ is mass in kilograms, and $\Delta T$ is the temperature change in °C or K (the units are equivalent for a *difference*).

Water's specific heat is $4186 \text{ J/(kg·°C)}$ — five times that of glass, roughly ten times that of iron. Among common materials, water is an outlier, and its outlier status matters more than almost any other physical property of the substance. A planet with oceans has a massive thermal buffer: to change Earth's average surface temperature by one degree, you have to add or remove roughly $10^{26}$ joules from the ocean — a timescale measured in centuries. That's the climate system's thermal inertia. It comes directly from the specific heat of water.

<!-- → [TABLE: Specific heats of common substances. Columns: substance, c (J/(kg·°C)). Rows: Water (15°C) 4186, Ice (avg) 2090, Human body (avg) 3500, Ethanol 2450, Aluminum 900, Glass 840, Iron/steel 452, Copper 387, Silver 235, Lead 128. Caption: Water's specific heat is anomalously high. The human body sits near water because it's mostly water. Metals are far lower — the same heat input warms metal much more than it warms water.] -->

**A calorimetry calculation.** Pour 0.250 kg of 20°C water into a 0.500 kg aluminum pan at 150°C, on an insulated pad. What's the final temperature?

Energy is conserved. Heat lost by the pan equals heat gained by the water:

$$m_\text{Al}\,c_\text{Al}(150 - T_f) = m_w\,c_w(T_f - 20).$$

Solve:

$$T_f = \frac{m_\text{Al}\,c_\text{Al}(150) + m_w\,c_w(20)}{m_\text{Al}\,c_\text{Al} + m_w\,c_w} = \frac{(0.500)(900)(150) + (0.250)(4186)(20)}{(0.500)(900) + (0.250)(4186)} \approx 59°\text{C}.$$

The final temperature is far closer to the water's starting point (20°C) than to the pan's (150°C), even though the pan is hotter. Water dominates the thermal balance because its specific heat is more than four times aluminum's. The mass ratio partly compensates; the specific heat ratio overwhelms it.

---

## Phase change: where the temperature holds still

Heat $Q = mc\Delta T$ works fine when nothing is melting or boiling. But at a phase transition — ice melting at 0°C, water boiling at 100°C — the temperature stops changing even as energy continues to flow in. The energy is going into rearranging molecular bonds, not speeding up molecular motion. The thermometer shows nothing. The molecules are doing enormous amounts of work on each other.

The heat required to melt (or freeze) a mass $m$:

$$Q = mL_f.$$

The heat required to vaporize (or condense) a mass $m$:

$$Q = mL_v.$$

$L_f$ and $L_v$ are called **latent heats** — *latent* meaning hidden, because the energy vanishes from the thermometer's view while it's happening.

For water: $L_f = 334 \text{ kJ/kg}$ to melt ice at 0°C. $L_v = 2256 \text{ kJ/kg}$ to vaporize water at 100°C. That vaporization number is staggering — it's equivalent to the energy required to heat liquid water from 0°C all the way to 540°C if it didn't boil. This is why evaporation is such an efficient cooling mechanism. When you sweat, a fraction of a gram of water evaporating off your skin removes hundreds of joules of energy from your body. The water carried that latent heat away invisibly.

<!-- → [FIGURE: Temperature vs. heat added diagram for water being heated from -20°C ice through melting, through liquid heating, through boiling to steam. Flat plateaus at 0°C (melting, labeled Q = mL_f) and 100°C (vaporization, labeled Q = mL_v). Sloped sections labeled Q = mc∆T with different slopes for ice, liquid, and steam. Caption: During a phase transition, temperature holds constant while heat flows in. The two plateaus for water absorb vastly more energy than the sloped warming sections.] -->

The orange growers in Florida spray their trees with water the night before a hard frost. As the temperature drops to 0°C, the water freezes — and each kilogram of water that freezes releases 334 kJ of latent heat into the air around the fruit. The ice sheathing the orange is not the danger; it's the heat factory that keeps the fruit itself just barely above freezing. This is latent heat of fusion deployed as antifreeze.

<!-- → [TABLE: Latent heats for common substances. Columns: substance, L_f (kJ/kg), L_v (kJ/kg). Rows: Water (334, 2256), Ethanol (108, 879), Nitrogen (25.5, 201), Mercury (11.8, 272), Lead (24.5, 871). Caption: Water's latent heats are exceptionally large relative to its mass. L_v for water is 6.7× L_f — it takes far more energy to boil water than to melt ice. Evaporative cooling exploits L_v directly.] -->

---

## The three modes of heat transfer

Everything we've discussed so far has been about how much energy is exchanged and what temperature change results. Now we need to ask: how does the energy get from one place to another in the first place? There are three fundamentally different mechanisms.

### Conduction

In conduction, energy travels through stationary matter by direct atomic contact — vibrating atoms jostle their neighbors, electrons move through a lattice. The rate:

$$\frac{Q}{t} = \frac{k A (T_2 - T_1)}{d},$$

where $k$ is the **thermal conductivity** of the material (W/(m·°C)), $A$ is the cross-sectional area, $d$ is the thickness, and $T_2 - T_1$ is the temperature difference across the slab.

<!-- → [TABLE: Thermal conductivities of common materials. Columns: material, k (W/(m·°C)). Rows: Silver 420, Copper 390, Aluminum 220, Steel (stainless) 14, Ice 2.2, Glass 0.84, Water 0.6, Wood 0.08–0.16, Air 0.023, Styrofoam 0.010. Caption: Thermal conductivities span four orders of magnitude. This spread is what makes engineering possible: copper to move heat quickly, Styrofoam to block it.] -->

![Horizontal log bar chart of thermal conductivity k (W/m·K) for nine materials: aerogel 0.013, air 0.025, wool 0.04, wood 0.12, water 0.6, steel 50, aluminum 235, copper 400, silver 429. Insulators on the left, conductors on...](../images/14-heat-and-heat-transfer-methods-fig-05.png)
*Figure 14.5 — Thermal Conductivity — Five Decades from Aerogel to Silver*

The four orders of magnitude between silver and Styrofoam is what makes thermal engineering possible. A copper saucepan conducts stovetop heat efficiently into your food. A Styrofoam cooler uses conductivity a hundred times lower than glass to keep the heat *out* of your beer. The building insulation R-value is just the ratio $d/k$ in customary units — the bigger the ratio of thickness to conductivity, the slower the conduction.

**Example: a Styrofoam cooler.** Walls 2.5 cm thick, $A = 0.95 \text{ m}^2$, inside at 0°C, outside at 35°C:

$$\frac{Q}{t} = \frac{(0.010)(0.95)(35)}{0.025} \approx 13 \text{ W}.$$

Over 24 hours: $Q \approx 1.1 \times 10^6 \text{ J}$. Mass of ice melted: $Q/L_f = 1.1 \times 10^6 / 334{,}000 \approx 3.3 \text{ kg}$ — about a 7-pound bag. Grocery-store experience confirmed.

<!-- → [FIGURE: Cross-section of Styrofoam cooler wall. Labels: T_outside = 35°C on right, T_inside = 0°C on left, thickness d = 2.5 cm, area A = 0.95 m². Arrow showing heat flow direction (right to left). Q/t = 13 W labeled. Second panel showing the ice-melt consequence: 3.3 kg melted per day. Caption: The conduction formula applied to a real insulation problem. All four variables (k, A, ΔT, d) are measurable; the result matches the grocery-store experience of a bag of ice lasting about a day.] -->

### Convection

In convection, energy moves by the bulk motion of a fluid. Hot fluid rises (lower density), cool fluid sinks, a circulation forms, and energy is carried along. This is how a room radiator heats a room, how the atmosphere moves warm air from equator to poles, how your coffee cools when you blow on it.

For convection, there's no single clean rate equation analogous to the conduction formula — the rate depends on geometry, fluid properties, viscosity, gravity, and the specific flow pattern. The practical approach: track the moving mass. If you know the mass of fluid moving and by how much its temperature changes, $Q = mc\Delta T$ applied to the fluid gives you the heat transfer.

**Example: a leaky house.** A house with volume 648 m³ has all its air replaced every 30 minutes (old, drafty). The cold outside air entering must be warmed by 10°C. Mass of air per replacement: $(1.29 \text{ kg/m}^3)(648 \text{ m}^3) \approx 836 \text{ kg}$. Energy: $(836)(1000)(10) \approx 8.4 \times 10^6 \text{ J}$. Rate: $8.4 \times 10^6 / 1800 \approx 4.6 \text{ kW}$, just from air infiltration. That's 46 hundred-watt bulbs burning continuously, just to overcome the house leaking. A well-sealed modern house turns over its air every 2 hours instead of every 30 minutes, cutting that loss by a factor of four.

### Radiation

In radiation, energy travels as electromagnetic waves. No medium required. Every object above absolute zero emits radiation; every object absorbs radiation from its surroundings. This is how the Sun's energy reaches Earth across 150 million kilometers of vacuum.

The rate of emission from a surface:

$$\frac{Q}{t} = \sigma e A T^4,$$

![Radiation power per square meter (W/m²) vs absolute temperature (K) for a blackbody. Curve P = σT⁴. Reference markers: human skin 310 K (~520 W/m²), red-hot stove 700 K, incandescent filament 3000 K, Sun surface 5800 K...](../images/14-heat-and-heat-transfer-methods-fig-06.png)
*Figure 14.6 — Stefan-Boltzmann — P ∝ T⁴, Double T and Radiation Rises 16×*

where $\sigma = 5.67 \times 10^{-8} \text{ W/(m}^2\text{·K}^4)$ is the **Stefan-Boltzmann constant**, $A$ is the surface area, $T$ is the absolute temperature in **kelvin** (not Celsius — this matters enormously), and $e$ is the **emissivity**, a dimensionless number from 0 to 1 indicating how efficiently the surface radiates. A perfect black-body has $e = 1$; human skin in the infrared has $e \approx 0.97$.

The fourth-power dependence is dramatic. A surface at 600 K radiates not twice but $2^4 = 16$ times as much as one at 300 K.

For an object at temperature $T_1$ in surroundings at $T_2$, the *net* radiative transfer is:

$$\frac{Q_\text{net}}{t} = \sigma e A (T_2^4 - T_1^4).$$

**Example: a person standing in a cold room.** Skin temperature 33°C (306 K), surface area 1.5 m², emissivity 0.97, room temperature 22°C (295 K):

$$\frac{Q_\text{net}}{t} = (5.67 \times 10^{-8})(0.97)(1.5)(295^4 - 306^4) \approx -99 \text{ W}.$$

Nearly 100 watts of radiation leaving the body. A resting person generates about 125 W metabolically. Without clothing, in a 22°C room, they're radiating most of that away — plus losing more through conduction and convection. This is why an unclothed person in a room that feels comfortable to a clothed person feels cold. The room is at 22°C; your skin is at 33°C; the walls at 22°C are cooler than you, and the radiation is flowing outward at nearly your metabolic rate.

Notice that you're radiating right now, into this room. So is everything around you. The net flow depends on which is hotter — you or the walls. If the walls were hotter, heat would flow toward you.

<!-- → [FIGURE: Person standing in a room. Three labeled arrows leaving the body: "Conduction — contact with floor and clothes," "Convection — warm air rising from skin surface," "Radiation — infrared emission to walls (~99 W labeled)." Metabolic heat input arrow (125 W) entering the body. Caption: All three modes of heat transfer operate simultaneously. At rest in a cool room, radiation alone accounts for most heat loss. Clothing reduces all three.] -->

---

## Which mode dominates?

![Three side-by-side panels. Conduction: metal rod heated at one end; atomic vibration propagates. Convection: pot of water on burner with circulation loop. Radiation: hot object emits IR through vacuum — Stefan-Boltzmann T⁴.](../images/14-heat-and-heat-transfer-methods-fig-04.png)
*Figure 14.4 — Three Modes of Heat Transfer — Conduction, Convection, Radiation*

In any real situation, all three modes operate simultaneously. A coffee cup loses heat by conduction through the ceramic, by convection of air rising off the hot surface, and by infrared radiation in every direction. The skill is identifying the dominant mechanism so you can reason about the system.

Some rough rules: radiation dominates when temperature differences are large or when the object is isolated in vacuum. Conduction dominates when objects are in direct contact and the path is a good conductor. Convection dominates when there's a fluid present, especially when the fluid is forced (a fan, a pump, the wind). Practical heat-transfer engineering rarely uses just one; insulation design, for instance, works by blocking conduction (foam fills the air gaps so air can't convect) while radiation is typically small at room temperature.

The greenhouse effect is radiation physics applied to a planetary scale. Earth's atmosphere is partly transparent to incoming solar radiation (visible light, which the Sun emits because its surface is at 5800 K) but absorbs the outgoing infrared radiation that Earth's cooler surface emits. The atmosphere re-radiates that infrared back toward the surface. The net effect: Earth's surface is about 33°C warmer than it would be under the same solar input with no atmosphere. Adding CO₂ strengthens the infrared absorption layer — more of the outgoing radiation is intercepted and returned. The Stefan-Boltzmann law then requires the surface to warm until it re-achieves energy balance at the new, higher radiative impedance.

<!-- → [FIGURE: Earth energy balance diagram. Sun arrow (1361 W/m² incoming). Earth cross-section showing: 30% reflected (albedo), 70% absorbed. Outgoing infrared arrow from surface, partially blocked by atmosphere layer labeled "CO₂ and H₂O absorb and re-emit." Net effect: surface temperature ~288 K instead of ~255 K (no atmosphere). Caption: The greenhouse effect is the Stefan-Boltzmann law applied to a planet. The surface must radiate at T⁴ to balance incoming solar power; greenhouse gases raise the effective radiating altitude, requiring a warmer surface to emit the same total power.] -->

---

## The equations, together

The full toolkit for any heat-transfer problem:

For warming or cooling without phase change: $Q = mc\Delta T$.

![Temperature versus heat added: warming ice (slope 1/c_ice), melting plateau at 0 °C (334 kJ/kg), warming water (slope 1/c_water), boiling plateau at 100 °C (2260 kJ/kg, much wider), warming steam (slope 1/c_steam). The boiling...](../images/14-heat-and-heat-transfer-methods-fig-03.png)
*Figure 14.3 — Phase Change — Temperature vs Heat for Water from Ice to Steam*

For phase change at constant temperature: $Q = mL_f$ (melting/freezing) or $Q = mL_v$ (vaporization/condensation).

For conduction rate through a slab: $Q/t = kA(T_2 - T_1)/d$.

For convection of a bulk fluid: track the mass flow and apply $Q = mc\Delta T$ to the moving fluid.

For radiation: $Q/t = \sigma e A (T_2^4 - T_1^4)$ — always in kelvin.

Any thermal engineering problem is some combination of these, with the proviso that energy is conserved: whatever flows in must either be stored (raising temperature) or flow out.

To feel the scale, consider an iceberg from the Ross Ice Shelf — 160 km × 40 km × 250 m, mass roughly $1.5 \times 10^{15}$ kg. To melt it:

$$Q = mL_f = (1.5 \times 10^{15})(334{,}000) \approx 5 \times 10^{20} \text{ J}.$$

The top surface is $6.4 \times 10^9 \text{ m}^2$. At 100 W/m² of solar input for 12 hours per day, the daily energy input is about $2.8 \times 10^{16}$ J. Days to melt by sunlight: $5 \times 10^{20} / 2.8 \times 10^{16} \approx 18{,}000$ days — roughly 50 years.

The latent heat of water is what makes that number so large. The latent heat of fusion alone requires vastly more energy per kilogram than any temperature change would. That's why icebergs in warm water persist for years, why glaciers take decades to respond to warming, and why the most visible consequences of climate change lag so far behind the temperature records that drive them. The ice is a heat sink with a 50-year time constant, governed entirely by $Q = mL_f$.

Scale that down by 15 orders of magnitude and you have the ice cube in your glass. Same physics, same equations. It takes about ten minutes to melt for the same reason the iceberg takes decades — the latent heat that must flow in per unit mass is the same.

---

## Exercises

### Warm-up

**14.1** *(LO 1)* Convert 250 Calories (dietary) to joules. Estimate how long you'd need to lift a 50 kg barbell through 0.5 m, once per second, to burn that energy.

**14.2** *(LO 2)* A 0.500 kg copper block is heated from 20.0°C to 80.0°C. How much heat was added? ($c_\text{Cu} = 387 \text{ J/(kg·°C)}$.)

**14.3** *(LO 3)* How much heat converts 0.100 kg of ice at 0°C to liquid water at 0°C? To convert that liquid to steam at 100°C? Compare the two.

**14.4** *(LO 4)* A 1.0 m² glass window (5.0 mm thick) separates 20°C inside from 0°C outside. Heat conduction rate? ($k_\text{glass} = 0.84 \text{ W/(m·°C)}$.)

### Application

**14.5** *(LO 2)* An 80,000-L swimming pool warms by 1.50°C from sunlight. Energy absorbed? In kWh? Cost at $0.15/kWh?

**14.6** *(LO 3)* Three ice cubes (6.0 g each, 0°C) dropped into 0.250 kg of soda at 20°C in a foam cup. Final temperature when all ice melts? (Treat soda as water.)

**14.7** *(LO 5)* Unclothed person in a 5°C walk-in cooler. Skin 33°C, area 1.7 m², emissivity 0.97. Net radiative heat loss in watts? Is this above or below a sedentary metabolic rate of 100 W?

**14.8** *(LO 4)* Attic: 15 cm of fiberglass ($k = 0.040 \text{ W/(m·°C)}$), 150 m² ceiling, inside 20°C, attic 5°C. Power leaking through ceiling? Daily cost at $0.15/kWh?

### Synthesis

**14.9** *(LO 2, 3)* A 0.500 kg aluminum pan holds 1.50 L of water initially at 18°C on a 1,500 W burner. (a) Time to boil? (b) Once at 100°C, what rate (g/s) is water boiling away if all burner power goes to vaporization?

**14.10** *(LO 6)* A campfire warms you at 1 m distance. Identify the dominant mode. Now you hold your hands directly above the flames. Does the dominant mode change? Why?

**14.11** *(LO 5, beyond chapter)* The Sun radiates as a black body at 5800 K. Compute total power output (radius $7.0 \times 10^8$ m). Then intensity at Earth's distance ($1.5 \times 10^{11}$ m). Compare to published solar constant 1361 W/m².

### Challenge

**14.12** *(LO 2, 3, beyond chapter)* Cool a 350 g cup of 95°C coffee to 45°C. Either evaporate some coffee ($L_v = 2340 \text{ kJ/kg}$ at this temperature) or add 0°C ice. For each path, how many grams of water must evaporate, or how many grams of ice must melt?

**14.13** *(LO 5, 6, beyond chapter)* A double-paned window has two 0.80 cm glass panes with a 1.00 cm air gap, total area 1.50 m², inside 15°C, outside −10°C. Compute heat-loss rate treating the three layers as series resistors. Compare to a single-pane window of the same total thickness (2.60 cm of pure glass). Why does the air gap provide such disproportionate insulation?

---

## LLM Exercise — Chapter 14: Heat Transfer in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A heat-transfer balance for one moment of your anchor phenomenon — at least one mode (conduction, convection, or radiation) computed honestly with units and uncertainty.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste the 1-sentence description from Chapter 1].

For Chapter 14 (Heat and Heat Transfer), I want to apply heat-transfer physics to ONE moment of my phenomenon where temperature change or thermal flow matters.

Please:

1. Identify ONE specific thermal moment in my phenomenon. Examples:
   - Coffee maker: the rate of heat loss from the carafe when full of hot coffee.
   - Bike commute: the rate at which I lose heat to the wind by forced convection.
   - Marathon: the metabolic heat I generate per minute and how my body sheds it.
   - Espresso machine: the energy required to bring the boiler from 20°C to 95°C.

2. Identify which mode of heat transfer dominates (conduction, convection, radiation, or a phase change). Justify.

3. Write the relevant equation. List inputs I need: surface areas, temperatures, masses, conductivities, emissivities. For each, tell me where to source the number and what uncertainty to expect.

4. Plug in and solve. Report Q (or Q/t) with proper units and uncertainty.

5. Sanity check against a published number for a comparable system if possible.

6. Identify ONE assumption that might fail in my actual situation and flag it.

7. Connect to Chapter 15 (Thermodynamics) — what efficiency or work-vs-heat question is now lurking?

Save the output as logbook/chapter-14-heat-transfer.md.
```

### What this produces

Your fourteenth Logbook entry — a quantified heat balance that turns the chapter's equations into a defensible number for your anchor phenomenon.

### How to adapt this prompt

- *For phenomena dominated by phase change* (boiling, sweating, freezing): emphasize $Q = mL$ over $Q = mc\Delta T$.
- *For phenomena dominated by radiation* (anything with the sun, anything with infrared imaging): use the net Stefan-Boltzmann formula and remember to convert temperature to kelvin.
- *For Claude Code:* if you have time-series temperature data (from a thermometer or smart device), use Code instead — fit an exponential decay and extract the time constant, which gives you an effective $hA$ product for the system.

### Connection to previous chapters

Builds on Chapter 13's temperature and equilibrium definitions. Uses Chapter 7's energy bookkeeping. Uncertainty propagation from Chapter 1 still applies.

### Preview of next chapter

Chapter 15 introduces thermodynamics — energy conservation including heat, the impossibility of perfect engines, and entropy. The Chapter 15 LLM Exercise will ask you to compute an efficiency for whatever heat-conversion process is lurking in your phenomenon.

---

**Tags:** heat-transfer, specific-heat, latent-heat, conduction, radiation
