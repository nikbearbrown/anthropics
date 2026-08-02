# Chapter 14 — Heat and Heat Transfer Methods

*Energy in transit: why your kitchen tile lies to you, and what it's really saying.*

---

## The tile and the carpet

It is winter, just before sunrise. You walk from your bedroom across a thick wool carpet, then through a doorway onto a ceramic kitchen tile. The carpet felt fine. The tile feels like a slap.

Stick a thermometer to each surface and both read the same number — somewhere around 18°C. The tile is not colder than the carpet. What the tile does is remove heat from your foot faster than the carpet does. Your foot is not a thermometer. It's a heat-flux meter. What it reports is not temperature — it's the rate at which energy is leaving your skin.

This is the central trick of the entire chapter, and once you see it, a lot of phenomena that seemed puzzling become obvious. The pile of wool fibers in the carpet traps still air, and air is a terrible conductor — energy seeps out of your foot so slowly that your skin barely registers it. The ceramic tile is a continuous solid lattice, with thousands of times the conductivity of trapped air, and it pulls energy out of your foot fast enough to feel cold even though the tile and the carpet are, thermally, at the same place.

The nineteenth-century French physicist Jean-Baptiste Joseph Fourier had a phrase for this kind of thing — he would have said the carpet and the tile are at the same *temperature* but present different *thermal resistances* to your foot. Temperature tells you the state of an object. Heat flux tells you how fast energy is flowing. Your nervous system evolved to care about the second, not the first. So did the engineers who designed your kitchen floor.

<!-- → [FIGURE: Side-by-side cross-section of carpet and ceramic tile at microscopic scale — carpet showing trapped air pockets between fibers, tile showing continuous crystalline lattice. Caption: "Same surface temperature, different thermal resistance. The carpet's trapped air is the insulator; the tile's continuous lattice is the conductor. The difference in feel is a difference in k, not in T."] -->

---

## Heat is not a substance

Before Joule, the dominant theory of heat was that it was a weightless, invisible fluid called *caloric* — stored in hot bodies and released into cold ones, like water flowing downhill. The theory was not stupid. It made real predictions. It explained why a hot iron cooled over time (caloric leaking out), why rubbing two sticks together made fire (caloric squeezed out of them), why a gas heated on compression (caloric compressed into a smaller volume). Lavoisier listed caloric among the elements. It was a serious scientific idea, held by serious scientists, for over sixty years.

What killed it was a paddle wheel.

In 1845, James Prescott Joule — son of a Manchester brewer, working in a laboratory adjacent to his father's brewery — took a heavy weight on a rope, looped the rope over a pulley, and let the weight fall while it turned a paddle wheel submerged in an insulated tank of water. He measured the temperature of the water before. He measured it after. The water was warmer. Not by much — Joule needed thermometers calibrated to a hundredth of a degree, and the patience of a man who had grown up timing yeast fermentations. But warmer, repeatably, in proportion to how far the weight had fallen.

If heat were a substance, no amount of mechanical stirring should produce it. What Joule showed was that mechanical work and heat are interchangeable. The gravitational potential energy of the weight became kinetic energy of the paddle wheel became, eventually, increased random motion of the water molecules. Not a new substance. Not caloric flowing in from anywhere. Just the same energy, reclassified from one form to another. The conversion:

$$1.000 \text{ kcal} = 4186 \text{ J}.$$

That number — four thousand one hundred and eighty-six joules per kilocalorie — is why the SI unit of energy is named the joule, and why thermodynamics is the branch of physics where two previously separate traditions (mechanics and heat) had to be welded into one.

The consequence for language is important. *Heat* is not a property an object has. It's the name for energy flowing across a boundary driven by a temperature difference. A coffee cup at 80°C does not "contain heat." It contains *internal energy* — the sum of the kinetic and potential energies of every molecule inside it. Heat is what that internal energy becomes when it crosses the boundary into your hand. The moment the flow stops, there is no heat — only internal energy on both sides.

The distinction matters more than it might seem. You can raise the internal energy of a system in two ways: do work on it (the paddle wheel), or transfer heat to it (a stove burner). After the fact, the system cannot tell you which path was used. It has more internal energy. That's all. Heat and work are not properties of systems; they're descriptions of processes.

<!-- → [FIGURE: Schematic of Joule's paddle-wheel apparatus — a weight on a rope descending through a height h, turning a paddle wheel inside an insulated tank of water. Labels: mgh (gravitational PE lost), Q (heat equivalent), ΔT (measured temperature rise). Caption: "Joule's experiment in one diagram. The only way to reconcile the measurement is if mechanical energy and heat are the same thing counted differently."] -->

---

## Warming and melting: two very different uses of energy

When you heat something without changing its phase, the energy you add goes into the kinetic energy of the molecules — faster vibration in solids, faster tumbling and translation in liquids and gases. The temperature rises. The relationship is:

$$Q = mc\Delta T,$$

where $Q$ is the heat transferred in joules, $m$ is the mass in kilograms, $c$ is the specific heat of the material in J/(kg·°C), and $\Delta T$ is the temperature change.

Specific heat is the thing that varies most between materials. Water sits at 4186 J/(kg·°C) — the highest of any common substance. Iron: 452. Copper: 387. Lead: 128. Aluminum: 900. Glass: 840. The four-hundred-to-one spread between lead and water is not trivial. If lead had water's specific heat, your kitchen plumbing would take four times as long to reach steady temperature in the morning. If water had lead's specific heat, the ocean would warm and cool forty times faster, and the entire climate system of Earth would be unrecognizable.

<!-- → [TABLE: Specific heats of common substances — columns: substance, c in J/(kg·°C), relative to water (water = 1.00). Rows: water, human body, ethanol, aluminum, glass, iron/steel, copper, silver, lead. Caption: "Water's anomalously high specific heat is not a curiosity — it is the thermal backbone of Earth's climate and of biological temperature regulation."] -->

Why is water's specific heat so anomalously high? Because of hydrogen bonds. Each water molecule is bonded to several neighbors through weak but persistent electromagnetic connections. When you add heat, some of the energy goes into stretching and breaking these bonds before any of it can accelerate the molecules. More energy input is required to produce the same temperature rise. Water is, in a real physical sense, resisting the thermometer.

This same anomaly explains why the ice floats, why the oceans moderate climate, why your body temperature is so stable. You are roughly 60% water by mass. Your body's specific heat averages about 3500 J/(kg·°C) — close to water's. Warming a 70 kg person by one degree requires about 245 kJ — the energy in a modest slice of bread. Your body does not overheat easily because you are mostly a very large container of water.

Now consider what happens when you add heat to a system undergoing a phase change — ice melting at 0°C, water boiling at 100°C. The thermometer sits still. The temperature does not change. The energy goes entirely into rearranging molecular bonds, not into molecular speed. The word *latent*, from the Latin for hidden, describes it perfectly — the heat is hidden, doing chemical work that shows no thermal signature.

$$Q = mL_f \quad \text{(melting or freezing)},$$
$$Q = mL_v \quad \text{(vaporization or condensation)}.$$

For water: $L_f = 334 \text{ kJ/kg}$, $L_v = 2256 \text{ kJ/kg}$. The vaporization latent heat is enormous — almost seven times the fusion latent heat, and equivalent to the energy required to heat a kilogram of liquid water from 0°C all the way to 540°C if no boiling occurred. When a pot of water finally reaches a rolling boil, nearly all the burner's power is going into vaporization — the temperature is stuck at 100°C, and the steam carries away 2256 kJ for every kilogram that leaves.

<!-- → [CHART: Heating curve for water — temperature (y-axis, 0 to 150°C) vs. heat added (x-axis, in kJ/kg). Shows: rising slope (ice warming, c = 2090), flat region at 0°C (melting, Lf = 334 kJ/kg), rising slope (liquid water warming, c = 4186), flat region at 100°C (vaporization, Lv = 2256 kJ/kg), rising slope (steam warming). Student should see immediately that the vaporization plateau is by far the longest — it dominates the energy budget.] -->

This is the reason orange growers in Florida spray their trees with water before a frost. As the spray freezes, each kilogram releases 334 kJ — enough to hold the surface of the fruit just at 0°C rather than below it. It looks paradoxical: you're protecting fruit from freezing by dousing it with water that freezes. The physics is in the latent heat of fusion. The water sacrifices itself to hold the temperature.

And it's the reason an iceberg takes decades to melt. The thermal calculation is straightforward: take the mass of the ice, multiply by $L_f$, divide by the rate of heat input. For a large Ross Ice Shelf iceberg — hundreds of kilometers long — the answer comes out to around fifty years of sustained solar irradiation. The latent heat of water is an enormous buffer against temperature change, at every scale from a glass of soda to the polar ice caps.

---

## Three ways energy moves

There are exactly three mechanisms by which heat transfers between objects. Every thermal phenomenon in the universe is some combination of them. Learning to identify which one dominates in a given situation is most of what heat-transfer engineering actually is.

**Conduction** is atom-to-atom vibration — energy passed along through a stationary material by direct physical contact. The rate is:

$$\frac{Q}{t} = \frac{kA(T_2 - T_1)}{d},$$

where $k$ is the thermal conductivity of the material, $A$ is the cross-sectional area perpendicular to the flow, $d$ is the thickness, and $T_2 - T_1$ is the temperature difference across it. The conductivity $k$ varies by four orders of magnitude between silver ($k \approx 420$ W/(m·°C)) and Styrofoam ($k \approx 0.010$ W/(m·°C)), and that range is what makes thermal engineering possible. A copper saucepan conducts stovetop heat into your food quickly. A Styrofoam cooler blocks that same heat efficiently. Same physics, opposite applications.

<!-- → [TABLE: Thermal conductivities of common materials — columns: material, k in W/(m·°C), practical application. Rows: silver, copper, aluminum, steel (stainless), ice, glass, water, wood, air, Styrofoam. Caption: "Four orders of magnitude between silver and Styrofoam. This range is the engineering freedom that makes insulation and heat sinks possible."] -->

The R-value printed on insulation batts is just $d/k$ in the customary units Americans use for construction — a ratio of thickness to conductivity, which is directly proportional to resistance to heat flow. Higher R, more resistance, slower heat loss. The underlying equation is the same one Fourier wrote down in 1822.

A Styrofoam cooler with walls 2.5 cm thick and total surface area 0.95 m², holding ice at 0°C in a car trunk at 35°C, conducts heat inward at a rate of about 13 watts — less than a dim lightbulb. Over a long summer day, that adds up to roughly 1.1 MJ, enough to melt about 3.4 kg of ice. That's a seven-pound bag, which is close to what grocery-store experience confirms. The equation works.

**Convection** is bulk fluid motion carrying energy from one place to another. Hot fluid rises because it's less dense; cool fluid sinks; a circulation pattern forms and the energy goes along for the ride. Atmospheric circulation, ocean currents, the way a room heated by a baseboard radiator eventually warms top to bottom — all convection.

We don't usually write a single tidy rate equation for convection, because the rate depends on the fluid's viscosity, the geometry, the gravity field, and a dozen other things that require fluid mechanics to handle properly. What we do instead is track the moving mass. If $m$ kilograms of air at temperature $T_1$ is replaced by air at temperature $T_2$ per unit time, then the power required to warm the incoming air is $\dot{m} c \Delta T$, and the bookkeeping reduces to a version of $Q = mc\Delta T$ applied to the moving fluid.

A typical older house replaces its entire interior air volume every thirty minutes through gaps and leaks. A 650 m³ house, with an interior-to-exterior temperature difference of 10°C, loses about 4.6 kilowatts just to air infiltration — forty-six hundred-watt bulbs of heating that vanishes invisibly through cracks in the walls. Modern weatherization, getting air turnover down to once every two hours, cuts that by a factor of four. The physics is entirely in the moving mass formula; the engineering is in finding and sealing the leaks.

**Radiation** requires no medium at all. Every object above absolute zero emits electromagnetic radiation. At room temperature, that radiation is entirely in the infrared — invisible, but carrying energy. At red-hot temperatures (around 800 K), it begins to bleed into the visible spectrum. At the surface temperature of the sun (5800 K), the peak is in green light with tails extending into ultraviolet.

The rate equation is the Stefan-Boltzmann law:

$$\frac{Q}{t} = \sigma e A T^4,$$

where $\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴) is a fundamental constant, $A$ is the radiating surface area, $T$ is the absolute temperature in *kelvin*, and $e$ is the emissivity — a number between 0 (perfect mirror, radiates nothing) and 1 (perfect black body, radiates maximally). Human skin, regardless of its color in the visible spectrum, has an infrared emissivity around 0.97 — we are nearly perfect black bodies in the thermal infrared, which is why night-vision cameras see us so easily.

The fourth-power dependence is the number worth sitting with. A surface at 600 K doesn't radiate twice as much as one at 300 K. It radiates $2^4 = 16$ times as much. Double the temperature and the radiated power goes up by a factor of sixteen. This is why engineering thermal insulation around a hot furnace is so much harder than insulating a warm room — the radiation terms become dominant, and they scale brutally.

For a body at temperature $T_1$ surrounded by an environment at $T_2$, what matters is the *net* radiation:

$$\frac{Q_\text{net}}{t} = \sigma e A (T_2^4 - T_1^4).$$

A person with skin temperature 33°C (306 K), surface area 1.5 m², emissivity 0.97, standing in a room at 22°C (295 K):

$$\frac{Q_\text{net}}{t} = (5.67 \times 10^{-8})(0.97)(1.5)\left[(295)^4 - (306)^4\right] \approx -99 \text{ W}.$$

About a hundred watts leaving the body by radiation alone. A resting adult produces around 125 watts of metabolic heat. Without clothes, in a room that most people would describe as comfortable, you are radiating away nearly all of your metabolic output just to the walls. This is why an unclothed person in a 22°C room feels cold even though the room temperature is above the skin temperature of your extremities. What your nervous system is measuring is not air temperature — it is heat flux, and the heat flux at your skin is substantial.

Clothes work primarily by trapping an insulating layer of air between you and the environment — reducing $k$ in the conduction equation. The emissivity of clothing in the infrared is high (close to 1 for most fabrics), so radiation still occurs, but the intervening layer of air makes the effective $T_2$ in the radiation formula the temperature of the fabric surface rather than the room walls, which reduces the net flux.

---

## Radiation and the planet

The Stefan-Boltzmann law has one application that transcends everything else on this page: it sets the temperature of Earth.

The sun radiates as a near-perfect black body at roughly 5800 K and delivers about 1361 watts per square meter to the top of Earth's atmosphere — the solar constant. Earth, as a sphere, intercepts solar energy over a cross-sectional area of $\pi R^2$, but radiates it back to space over its full surface area of $4\pi R^2$. Earth also reflects about 30% of incoming sunlight (the albedo). The rest is absorbed and must eventually be re-radiated as infrared to maintain thermal equilibrium.

Setting energy in equal to energy out:

$$\frac{\pi R^2 \cdot S \cdot (1 - a)}{4\pi R^2} = \sigma T^4,$$

where $S \approx 1361$ W/m², $a \approx 0.30$, and $\sigma$ is the Stefan-Boltzmann constant. Solving for $T$:

$$T = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4} \approx 255 \text{ K} = -18°\text{C}.$$

Earth's actual average surface temperature is about 288 K — 15°C. The difference, 33 degrees, is the greenhouse effect. It is not a complicated mechanism: the atmosphere is nearly transparent to visible sunlight (which comes in) and partly opaque to infrared radiation (which tries to go out). Carbon dioxide, water vapor, and methane absorb outgoing infrared and re-radiate it in all directions, including back down to the surface. The surface must warm until it radiates enough at its new higher temperature to balance the incoming solar flux despite the partial atmospheric blockage. The 33-degree difference between the blackbody calculation and the observed temperature is the size of that effect, naturally.

The fourth-power scaling is what makes climate sensitivity to small atmospheric changes nonlinear and consequential. Doubling CO₂ changes the effective emissivity of the atmosphere by a small amount. But even a small upward shift in equilibrium temperature releases water vapor (another greenhouse gas), which amplifies the forcing further. The basic physics is entirely in the rate equations above.

<!-- → [FIGURE: Earth energy-balance diagram — left side: solar input (S·πR²·(1-a)) shown as incoming arrows hitting Earth's disk; right side: infrared output (σT⁴·4πR²) shown as outgoing arrows from the full sphere. Middle: atmosphere layer shown partially blocking outgoing IR (greenhouse effect). Caption: "The 33-degree gap between the bare-rock blackbody temperature (255 K) and Earth's actual surface temperature (288 K) is the greenhouse effect, derived from nothing more than energy balance and the Stefan-Boltzmann law."] -->

---

## What runs through all of it

Step back. Three mechanisms. Five rate equations. One principle tying them together.

The mechanisms — conduction, convection, radiation — all have the same underlying logic: a temperature difference exists, and energy flows from high to low until the difference is gone. The specific rate depends on what's in the way: the conductivity of the material, the geometry of the flow, the emissivity of the surface. Change the material, same principle. Change the geometry, same principle.

The state equations — $Q = mc\Delta T$ for warming without phase change, $Q = mL$ for phase change at fixed temperature — describe what happens to the energy once it arrives. Some goes into molecular speed (temperature change). Some goes into rearranging molecular bonds (phase change), hiding as latent heat with no thermometric signature.

The deep puzzle — the one this chapter raises and does not answer — is why heat flows only from hot to cold. Every individual molecular collision is microscopically time-reversible. You could, in principle, film a single molecule bouncing off a wall and run the film backwards and see nothing physically impossible. Yet in bulk, energy never spontaneously flows from cold to hot. The asymmetry is real, and it is not explained by the equations in this chapter. It is the second law of thermodynamics, and we will meet it head-on in Chapter 15. The rate equations above tell you how fast heat moves. The second law will tell you what fraction of that heat can ever become useful work — and why the answer is always less than you might hope.

---

## Still puzzling

*Why does heat flow only from hot to cold when molecular collisions are individually reversible?* This is the second law, and its statistical underpinning — that the direction of bulk heat flow is determined by the overwhelming probability of disordered states over ordered ones — is one of the deepest ideas in all of physics. Boltzmann spent years defending it and never saw it universally accepted in his lifetime.

*Why is thermal conductivity so different across materials?* In metals, free electrons carry most of the heat — the same electrons that carry current, which is why electrical conductors are also thermal conductors (the Wiedemann-Franz law). In insulators, lattice vibrations (phonons) carry heat instead, and their mean free path determines the conductivity. This is why diamond, an electrical insulator, is the best thermal conductor known — the crystal structure allows phonons to travel enormous distances without scattering.

*What determines emissivity?* In principle, the absorptivity and emissivity of a surface are equal at every wavelength — a surface that absorbs well at a given wavelength emits well at that wavelength. This is Kirchhoff's law of thermal radiation, and it is the connection between optics and thermodynamics. The black paint that makes a surface good at absorbing visible light may not make it good at absorbing or emitting infrared — because the molecular resonances at visible wavelengths and infrared wavelengths are different. Carbon black has high emissivity across almost all wavelengths. Polished aluminum does not.

---

## Exercises

### Warm-up

**W1.** A 0.400 kg block of copper ($c = 387$ J/(kg·°C)) is heated from 20.0°C to 95.0°C. How much heat was added? Now repeat for an equal mass of water ($c = 4186$ J/(kg·°C)) over the same temperature range. By what factor does the water require more heat than the copper, and why?

*Tests: $Q = mc\Delta T$ with two materials; connects numerical result to the physical meaning of specific heat. Difficulty: low.*

**W2.** How much heat is required to melt 0.250 kg of ice at 0°C? How much to vaporize 0.250 kg of water at 100°C? Express both in joules and in kilocalories. What does the ratio $L_v / L_f$ tell you about the relative energy cost of these two phase changes?

*Tests: latent heat formulas, unit conversion, ratio interpretation. Difficulty: low.*

**W3.** A glass window pane is 1.20 m² in area and 5.0 mm thick ($k_\text{glass} = 0.84$ W/(m·°C)). The interior is at 20°C and the exterior at $-5$°C. At what rate (in watts) does heat conduct through it? How much energy is lost in one hour?

*Tests: conduction rate equation — identifying area, thickness, $\Delta T$, and $k$. Difficulty: low.*

**W4.** A person has skin temperature 33°C, surface area 1.70 m², and emissivity 0.97. The room walls are at 20°C. Compute the net radiative power leaving the person. Remember to use kelvin.

*Tests: Stefan-Boltzmann net radiation equation, and the mandatory unit conversion to kelvin. Difficulty: low.*

---

### Application

**A1.** You drop three ice cubes (8.0 g each, at 0°C) into 0.300 kg of coffee at 75°C in an insulated mug. What is the final temperature once all the ice has melted? (Treat the coffee as water.) Show each energy-balance step explicitly: energy to melt the ice, energy to warm the meltwater from 0°C to $T_f$, energy lost by the coffee.

*Tests: combining $Q = mL_f$ and $Q = mc\Delta T$ in a single calorimetry balance — the most common multi-step heat problem. Difficulty: medium.*

**A2.** A Styrofoam picnic cooler has total surface area 0.80 m² and walls 3.0 cm thick ($k = 0.010$ W/(m·°C)). It holds 2.0 kg of ice at 0°C. The air temperature is 32°C. (a) At what rate does heat conduct into the cooler? (b) How long, in hours, before all the ice melts? ($L_f = 334$ kJ/kg.)

*Tests: conduction rate equation feeding into a latent-heat calculation — two equations in sequence. Difficulty: medium.*

**A3.** A 0.500 kg aluminum pan ($c = 900$ J/(kg·°C)) sitting at 180°C is filled with 0.400 kg of water at 18°C. Assuming no heat loss to the surroundings, find the equilibrium temperature. Check: does your answer make physical sense given the relative specific heats and masses?

*Tests: calorimetry with two objects exchanging heat — solving the energy-balance equation for $T_f$. Difficulty: medium.*

**A4.** Compute the net radiative power lost by a person (skin at 33°C, area 1.70 m², $e = 0.97$) standing outdoors on a clear night, where the effective sky temperature is $-20$°C (253 K). Compare to the same person indoors at 20°C. By what factor does outdoor radiative loss exceed indoor?

*Tests: net Stefan-Boltzmann formula at two different environment temperatures; reinforces the fourth-power dependence. Difficulty: medium.*

---

### Synthesis

**S1.** You want to cool 0.350 kg of coffee from 90°C to 50°C. Option A: wait for it to cool by radiation and convection (roughly 80 W total loss rate from a typical mug). Option B: stir in ice cubes at 0°C. (a) How long does Option A take? (b) How many grams of ice does Option B require? (c) Which option changes the total mass of liquid in the mug, and by how much?

*Tests: combining a rate-equation estimate with a latent-heat calculation; connects two different energy mechanisms to the same outcome. Difficulty: medium-high.*

**S2.** The Earth's bare-rock blackbody equilibrium temperature is 255 K, but the actual surface temperature is 288 K. Using the Stefan-Boltzmann law, compute: (a) the power per square meter that Earth's surface radiates at 255 K; (b) the power per square meter it radiates at 288 K; (c) the additional power per square meter that the greenhouse effect is effectively trapping at the surface. Express (c) as a percentage of the total solar input per unit surface area ($S(1-a)/4 \approx 238$ W/m²).

*Tests: applying the Stefan-Boltzmann law quantitatively to Earth's energy balance — connects the chapter's physics to climate science. Difficulty: medium-high.*

---

### Challenge

**C1.** A double-paned window consists of two glass panes (each 0.80 cm thick, $k = 0.84$ W/(m·°C)) separated by a 1.0 cm air gap ($k = 0.023$ W/(m·°C)). Total area: 1.50 m². Inside temperature: 15°C. Outside: $-10$°C. Treat the three layers as thermal resistors in series (each with resistance $R = d/kA$), find the total resistance, and compute the heat-loss rate. Then compute the rate for a single pane of the same total thickness (2.60 cm) of solid glass. By what factor does the air gap reduce heat loss, and why is the factor so large despite the gap being only 1 cm wide?

*Tests: series thermal resistance, quantifying the insulating effect of trapped air — requires setting up the resistance analogy and comparing two configurations. Difficulty: high.*

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
- *For Claude Code:* If you have time-series temperature data (from a thermometer or smart device), use Code instead — fit an exponential decay and extract the time constant, which will give you an effective $h \cdot A$ product for the system.

### Connection to previous chapters

Builds on Chapter 13's temperature/equilibrium definitions. Uses Chapter 7's energy bookkeeping. The uncertainty propagation rules from Chapter 1 still apply.

### Preview of next chapter

Chapter 15 introduces the laws of thermodynamics — energy conservation including heat, the impossibility of perfect engines, and entropy. The Chapter 15 LLM Exercise will ask you to compute an efficiency for whatever heat-conversion process is lurking in your phenomenon.

---

## AI Wayback Machine

**Joseph Fourier** developed the mathematical theory of heat conduction in 1822 — including the partial differential equation that bears his name. Modern heat transfer engineering still uses Fourier's framework directly.

**Run this:**

```
Who was Joseph Fourier, and how does the Fourier heat equation connect to heat transfer we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Joseph Fourier"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through the Fourier heat equation and what each term represents physically.
- Ask it about Fourier's parallel role as governor of Egypt under Napoleon — and how that work shaped his physics.

What changes? What gets better? What gets worse?

---

**Tags:** heat-transfer, specific-heat, latent-heat, conduction, radiation
