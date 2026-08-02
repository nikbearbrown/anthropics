# Chapter 1 — Temperature and Thermal Energy

*Temperature is not heat. Thermal energy is not temperature. Heat is energy in transit.*

---

You step into the ocean off the coast of Maine in July. The water is 12°C. Painfully cold. You get home and step into a bathtub at 38°C. Comfortable, warm, exactly right.

Here is the fact that should bother you: the ocean contains vastly more thermal energy than your bathtub. By many orders of magnitude. The Atlantic Ocean has roughly $10^{46}$ water molecules, each carrying kinetic energy proportional to temperature. The bathtub has maybe $10^{26}$. The ocean is thermally richer by a factor of roughly $10^{20}$ — and yet it feels cold, and the bathtub feels warm.

The reason is that your body does not sense thermal energy. It senses heat flow. And heat flow is driven not by how much thermal energy a system has, but by the difference in temperature between that system and you. Your skin is at about 33°C. The ocean at 12°C is colder than you, so heat flows out. The bathtub at 38°C is warmer than you, so heat flows in. The direction of flow has nothing to do with the ocean's enormous store of internal energy.

This is the distinction the chapter is about. Temperature, thermal energy, and heat are three different things. Confusing them is the source of more errors in thermodynamics — among students and in casual reasoning — than almost anything else. Getting them straight here will make the rest of the book much easier.

---

## Temperature

Temperature is a number that describes how fast the molecules of a substance are moving, on average. More precisely: temperature is proportional to the *average translational kinetic energy per molecule*.

In three dimensions, the equipartition theorem says each translational degree of freedom carries an average energy of $\frac{1}{2}k_BT$. A molecule free to move in $x$, $y$, and $z$ has three such degrees of freedom, so its average translational kinetic energy is $\frac{3}{2}k_BT$. Setting that equal to $\frac{1}{2}m\langle v^2 \rangle$ and solving:

$$T = \frac{m \langle v^2 \rangle}{3 k_B}$$

where $k_B = 1.38 \times 10^{-23}$ J/K is the Boltzmann constant and $\langle v^2 \rangle$ is the mean squared speed of the molecules. This is the molecular definition of temperature. It is not a postulate — it is derived from statistical mechanics, and we will rederive it properly in Chapter 4.

Two things are worth noting about this formula. First, it uses $\langle v^2 \rangle$, not $\langle v \rangle$. The mean of the squares is not the square of the mean. These are different quantities, and the distinction will matter in Chapter 4 when we look at the full speed distribution. Second, temperature is a *per-molecule* quantity — it characterizes the average energy of a single molecule, not the total energy of the system. That is why temperature is called an *intensive* variable: it does not depend on how much material you have. A thimble of water and a swimming pool at 20°C have the same temperature, despite one containing vastly more thermal energy than the other.

<!-- → [TABLE: two-column reference — Intensive vs. Extensive — rows: definition, scales with system size?, example quantities, what a thermometer measures; Temperature / Specific heat capacity in Intensive; Thermal energy U / Heat capacity mc in Extensive; reader should see exactly why "same temperature, different thermal energy" is not a contradiction] -->

We measure temperature on the Kelvin scale in thermodynamic equations. Absolute zero — $T = 0$ K — is the classical limit at which thermal motion ceases. Room temperature is 293 K. Body temperature is 310 K. The conversion is $T(\text{K}) = T(°\text{C}) + 273.15$. Since 2019, the Boltzmann constant has been fixed by definition at $k_B = 1.380649 \times 10^{-23}$ J/K, which means temperature is now defined by fixing $k_B$ — a conceptual inversion from the older approach, reflecting how precisely we can now measure molecular motion.

---

## Thermal energy

Thermal energy is the total internal kinetic energy of all the molecules in a system — their translational motion, their rotational tumbling, their vibrational stretching — plus the potential energy stored in the forces between them.

It is an *extensive* variable: it grows with the size of the system. Double the number of molecules at the same temperature and you double the thermal energy. For a monatomic ideal gas, where there are no rotational or vibrational modes and no intermolecular forces, the thermal energy is simply:

$$U = \frac{3}{2} N k_B T$$

For a diatomic gas at moderate temperatures — where rotational modes are excited but vibrational modes are not yet active — each molecule has five active degrees of freedom instead of three:

$$U = \frac{5}{2} N k_B T$$

The factor in front counts the number of independent ways the molecule can store energy. A nitrogen molecule tumbling through space has three translational modes and two rotational modes (rotation about the molecular axis contributes negligibly for a symmetric diatomic molecule); hence five-halves. At very high temperatures, vibrational modes wake up and add two more terms, giving $\frac{7}{2}Nk_BT$. The thermal energy of a real gas holds more than the simple formula suggests — a point that will matter when we calculate heat capacities.

The relation $U = \frac{3}{2}Nk_BT$ encodes both concepts at once: $T$ is the intensive, per-molecule quantity; $N$ is what makes the total energy extensive; $k_B$ converts between them. A thermometer measures $T$, not $U$. To know the thermal energy of a system you need both its temperature and how much of it there is.

---

## Heat

Heat is energy in transit. It is not a property stored in a system — it is what happens at the boundary between two systems at different temperatures.

When the ocean and your skin are in contact, energy crosses the boundary from higher temperature to lower temperature. That crossing is heat. Once the energy has crossed and is stored in your body's molecules, it is thermal energy, not heat. The word "heat" properly refers only to the *flow*, not to what is stored.

The sign convention used throughout this book: $Q > 0$ when heat flows into the system, $Q < 0$ when heat flows out. The internal energy of a system increases when heat enters and when work is done on it — that is the first law, which we take up in Chapter 5.

There are three mechanisms by which heat moves, and they are physically distinct.

**Conduction** moves heat through a material by molecular collision, without bulk motion of the material. In the hotter region, molecules vibrate faster; they collide with their slower neighbors and transfer kinetic energy along the temperature gradient. The rate is described by Fourier's law: $dQ/dt = -kA\,(dT/dx)$, where $k$ is the thermal conductivity, $A$ is cross-sectional area, and $dT/dx$ is the temperature gradient. Metals conduct well because free electrons carry energy efficiently alongside atomic vibrations. Insulators — air, wood, aerogel — conduct poorly because neither electrons nor atomic structure moves energy efficiently.

**Convection** moves heat by the bulk flow of a fluid. Hot fluid is less dense and rises; it carries thermal energy upward and is replaced by cooler fluid from below. This is why you stir a pot, why warm air vents are placed near the floor, and why wind chill matters on a cold day — moving air carries away the warm layer near your skin faster than still air would.

**Radiation** moves heat as electromagnetic waves and requires no material medium at all. Every object above absolute zero emits radiation. The rate is given by the Stefan-Boltzmann law:

$$P = \sigma A T^4$$

where $\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴) is the Stefan-Boltzmann constant. The $T^4$ dependence is steep: radiation is negligible compared to conduction and convection at room temperature, but becomes dominant at high temperatures. The Sun, with a surface temperature of about 5800 K, loses energy almost entirely by radiation. A human body at 310 K emits in the infrared — visible to thermal cameras, but carrying far less power per unit area.

When an object is surrounded by an environment at temperature $T_\text{env}$, the net radiated power is:

$$P_\text{net} = \sigma A (T^4 - T_\text{env}^4)$$

It is the difference of fourth powers, not the difference of temperatures, that drives the net flow.

<!-- → [INFOGRAPHIC: three-panel mechanism diagram — conduction (temperature gradient along a metal rod with molecular collision arrows), convection (circulation loop in a heated fluid with rising hot and sinking cool arrows), radiation (electromagnetic waves leaving a glowing object into vacuum); each panel names the governing law, gives one real-world example, and states whether material medium is required; reader sees at a glance the physical distinction between the three] -->

---

## The Zeroth Law

Before temperature can be used as a measurable quantity, we need to establish that it is a well-defined one — that two objects at the same temperature are genuinely in thermal equilibrium with each other.

The Zeroth Law of Thermodynamics states: if system A is in thermal equilibrium with system C, and system B is in thermal equilibrium with system C, then A is in thermal equilibrium with B.

This sounds obvious. But without it, thermometry breaks down. A thermometer placed in two objects reads the same value in both. The Zeroth Law is what guarantees that the two objects would be in equilibrium with each other — that "same temperature" is a transitive relation. Without transitivity, temperature readings would not be comparable. The law was identified by Ralph Fowler in the 1930s and named "zeroth" because it is logically prior to the First and Second Laws, which had already been named. It is the law that makes the concept of temperature coherent.

---

## Specific heat capacity

When heat flows into an object, the object's temperature rises. How much it rises per joule of heat added depends on the substance — specifically on its specific heat capacity $c$:

$$Q = mc\Delta T$$

Water has $c = 4186$ J/(kg·K). This is anomalously high. The reason is hydrogen bonding: water molecules form a network of hydrogen bonds with their neighbors, and energy goes not only into speeding up molecular motion but also into stretching and bending that network. More modes of energy storage means more energy required per degree of temperature rise.

The consequences are large. Oceans moderate Earth's climate precisely because water can absorb or release vast amounts of thermal energy with only modest changes in temperature. Coastal cities have milder climates than inland cities at the same latitude. The human body is about 60% water by mass — the high specific heat prevents dangerous temperature swings when metabolism generates or withdraws heat suddenly.

Compare water with metals: copper has $c = 385$ J/(kg·K); iron, 449; aluminum, 900. The same joule that raises a kilogram of water by 0.24°C raises a kilogram of copper by 2.6°C — more than ten times as much. This is why a metal pan heats up almost instantly over a flame while a pot of water takes minutes to boil.

---

## Calorimetry

When two objects at different temperatures come into thermal contact in an insulated system, heat flows from hot to cold until they reach a common equilibrium temperature $T_f$. Conservation of energy requires that the heat lost by the hotter object equal the heat gained by the cooler:

$$m_1 c_1 (T_1 - T_f) = m_2 c_2 (T_f - T_2)$$

Solving for $T_f$:

$$T_f = \frac{m_1 c_1 T_1 + m_2 c_2 T_2}{m_1 c_1 + m_2 c_2}$$

This is a weighted average of the initial temperatures, weighted by heat capacity $mc$ — not by mass alone. The object with higher heat capacity pulls the equilibrium temperature toward its initial value.

Let me work through it. A 200 g copper block at 80°C dropped into 500 g of water at 20°C:

$$(0.200)(385)(80 - T_f) = (0.500)(4186)(T_f - 20)$$

$$77(80 - T_f) = 2093(T_f - 20)$$

$$6160 - 77T_f = 2093T_f - 41860$$

$$48020 = 2170T_f \implies T_f \approx 22.1°\text{C}$$

The copper drops 58°C. The water rises 2°C. The asymmetry is not about size — the water's heat capacity ($500 \times 4186 = 2093$ J/K) is 27 times the copper's ($200 \times 385 = 77$ J/K). The water barely notices the copper's thermal energy, because it takes so much more energy per degree to raise water's temperature.

This calculation assumes perfect insulation — no heat lost to surroundings. Real calorimetry enforces this with insulated containers; high-precision work uses vacuum-jacketed Dewar flasks and accounts for the heat capacity of the container itself.

<!-- → [IMAGE: thermal equilibration diagram for the copper-water example — two vertical bars representing initial temperatures (copper 80°C, water 20°C) converging to a shared T_f = 22.1°C, with bar widths proportional to heat capacity mc; copper bar narrow (mc = 77 J/K), water bar wide (mc = 2093 J/K); caption: "The weighted average pulls almost entirely toward the water's initial temperature because its heat capacity is 27× larger"] -->

---

## Thermal expansion

As temperature rises, molecules move faster and vibrate more vigorously. In a solid, the intermolecular potential is asymmetric — molecules are easier to push apart than to compress — so the average separation grows with energy. The macroscopic result is expansion.

For a linear dimension $L$:

$$\Delta L = \alpha L_0 \Delta T$$

where $\alpha$ is the linear thermal expansion coefficient. Steel: $\alpha \approx 12 \times 10^{-6}$/K. Aluminum: $\alpha \approx 23 \times 10^{-6}$/K.

A 10 m steel rail warming from 20°C to 50°C expands by $\Delta L = (12 \times 10^{-6})(10)(30) = 3.6$ mm. Negligible if unconstrained. If bolted at both ends, that 3.6 mm of blocked expansion builds into a compressive stress of $\sigma = E\alpha\Delta T = (200 \times 10^9)(12 \times 10^{-6})(30) = 72$ MPa — roughly half the yield strength of structural steel. Bridges, railroad tracks, and highway slabs all require expansion joints. The gaps look minor; they are doing serious structural work.

Water is the famous exception. Between 0°C and 4°C, water *contracts* as it warms, reaching maximum density at exactly 4°C. Above 4°C it expands normally. The origin is hydrogen-bond geometry: ice has an open hexagonal lattice; as it melts, the lattice partially collapses and molecules pack more tightly. The consequence is that ice is less dense than liquid water and floats. If ice sank, lakes would freeze from the bottom up and aquatic life in cold climates would be far more precarious. The 4°C density maximum is one of the reasons cold-climate ecosystems can survive winter.

<!-- → [CHART: density of water vs. temperature from −5°C to 15°C — curve rises from ~917 kg/m³ (ice) through the melt, peaks at 999.97 kg/m³ at 4°C, then falls slowly; mark the 4°C peak with a labeled vertical dashed line; inset note: "ice floats because it lies left of this peak"; reader should see the anomaly as a narrow feature near freezing, not a general property of all temperatures] -->

---

## A note on what temperature is not

There is an old theory — the caloric theory, dominant in the eighteenth century — that heat was a weightless fluid called "caloric" that flowed from hot objects to cold ones and was conserved. It explained a lot. It also predicted that you could squeeze heat out of a substance, like water from a sponge, and that cold was the absence of caloric.

Benjamin Thompson (Count Rumford) noticed in 1798 that boring cannon barrels generated heat indefinitely, which a finite caloric store could not explain. James Joule, in the 1840s, showed through careful mechanical experiments that work and heat were interconvertible at a fixed rate — that heat was not a substance but a form of energy. The caloric theory was replaced by what we now call thermodynamics.

The reason I mention it: the intuition that cold is "something" — a substance, a presence rather than an absence — is remarkably persistent. Cold is the absence of thermal energy. There is no cold fluid, no cold caloric. When the ocean feels cold, it is because energy is leaving your body, not because cold is entering it.

---

## What comes next

Temperature describes the average molecular speed. Thermal energy is the total stored in all the molecules. Heat is what flows when temperature differs. With these three concepts in hand, Chapter 2 looks more carefully at how heat flows — the mathematics of conduction, convection, and radiation — and what happens at phase boundaries where heat flows without any temperature change at all. Chapter 4 derives the distribution of molecular speeds — the Maxwell-Boltzmann distribution — which explains not just the average but the full spread of velocities, including the tails that turn out to matter for planetary atmospheres and chemical reaction rates.

---

## Exercises

**Warm-up 1** *(Apply — temperature conversions)*
Convert each of the following to Kelvin: room temperature (20°C), body temperature (37°C), a cup of coffee (85°C), liquid nitrogen (−196°C), and the surface of the Sun (~5500°C). Which of these is closest to absolute zero in absolute terms?

**Warm-up 2** *(Apply — rms speed)*
Find the rms speed of nitrogen molecules (N₂, $m = 4.65 \times 10^{-26}$ kg) at $T = 300$ K using $v_{rms} = \sqrt{3k_BT/m}$. Then find it for water vapor (H₂O, $m = 2.99 \times 10^{-26}$ kg) at the same temperature. Which moves faster, and by what factor?

**Warm-up 3** *(Apply — specific heat)*
A 1 kg block of iron at 200°C is dropped into a large, perfectly insulated bucket of water (10 kg) at 20°C. Without computing $T_f$ yet: which object controls the final temperature more strongly, and why? Now compute $T_f$. ($c_{\text{Fe}} = 449$ J/(kg·K); $c_{\text{water}} = 4186$ J/(kg·K).)

**Application 1** *(Apply — calorimetry with three objects)*
A 150 g aluminum cup at 25°C holds 300 g of water at 90°C. A 200 g iron bolt at 25°C is then dropped in. Find the final equilibrium temperature. ($c_{\text{Al}} = 900$, $c_{\text{water}} = 4186$, $c_{\text{Fe}} = 449$ J/(kg·K).) Does the order in which you add the objects matter to the final answer? Justify.

**Application 2** *(Apply — thermal expansion and stress)*
A steel bridge span is 80 m long at 10°C. On a summer day it reaches 42°C. How much does it want to expand? If the expansion joints allow only 15 mm of total movement, will the span buckle? Compute the compressive stress if it is fully constrained. ($\alpha_{\text{steel}} = 12 \times 10^{-6}$/K; $E_{\text{steel}} = 200$ GPa; yield strength of structural steel ≈ 250 MPa.)

**Application 3** *(Apply — radiation)*
A human body (surface area ≈ 1.8 m², skin temperature 33°C) stands in a room at 20°C. Estimate the net power radiated. ($\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴).) How does this compare to typical resting metabolic rate (~80 W)? What does the comparison tell you about why humans need clothing in cool environments?

**Synthesis 1** *(Analyze — thermal energy vs. temperature)*
System A: 500 g of water at 80°C. System B: 5 kg of water at 25°C. (a) Which has more thermal energy? Estimate the ratio. (b) They are brought into thermal contact in an insulated container. In which direction does heat flow, and why? (c) Compute $T_f$. Does the result surprise you? What does it reveal about the relationship between thermal energy and temperature?

**Synthesis 2** *(Analyze — specific heat and climate)*
San Francisco (coastal) and Sacramento (inland, ~100 km east) are at nearly the same latitude. San Francisco's average July temperature is about 17°C; Sacramento's is about 35°C. Using what you know about water's specific heat and ocean thermal mass, explain qualitatively why this difference exists. What would happen to San Francisco's climate if the Pacific Ocean had the specific heat of iron instead of water?

**Challenge** *(Extend — Zeroth Law and thermometry)*
A student argues: "The Zeroth Law is obvious — of course if A equals C and B equals C then A equals B. That's just math." Give a physical scenario where this transitivity could, in principle, fail without the Zeroth Law as an empirical constraint. What property of real thermal systems does the Zeroth Law assert that pure logic alone does not guarantee?

---

## LLM Exercises

### Build the temperature-distribution visualizer (`01-temperature-kinetic.html`)

> **Show.** Maxwell-Boltzmann speed distribution: $f(v) = 4\pi (m/(2\pi k_B T))^{3/2} v^2 \exp(-mv^2/(2k_B T))$. Three characteristic speeds: most probable $v_{mp} = \sqrt{2k_BT/m}$, average $v_{avg} = \sqrt{8k_BT/(\pi m)}$, rms $v_{rms} = \sqrt{3k_BT/m}$.
>
> **Say.** Build a temperature + speed distribution visualizer with animated particles.
>
> **Constrain.** D3 v7. 2D box with N=100 particles colored by speed. Slider for T (50–2000 K) and molecular mass (selector for H₂=2, N₂=28, O₂=32, Ar=40). When T is changed, rescale all particle velocities accordingly. Below the box: a histogram of particle speeds updating in real time, with the analytical Maxwell-Boltzmann curve overlaid as a smooth line. Vertical markers at $v_{mp}, v_{avg}, v_{rms}$ with labels. Filename: `01-temperature-kinetic.html`.
>
> **Verify.** (a) Lower T: distribution narrows and shifts left. (b) Heavier molecule at same T: distribution narrows and shifts left. (c) $v_{mp} < v_{avg} < v_{rms}$ always (the distribution is asymmetric).

### Exploration

Compare H₂ and N₂ at the same temperature. H₂ is 14× lighter; its $v_{rms}$ is $\sqrt{14} \approx 3.7$× faster.

Raise T from 300 K to 1200 K. The distribution should broaden by a factor of 2 ($\sqrt{4}$).

What fraction of N₂ molecules at 300 K have $v > 1000$ m/s? Very small — the tail decays exponentially.

### Extension prompt (chapter bridge)

> **Show.** Different materials have different specific heats. Calorimetry: $Q_{\text{lost}} = Q_{\text{gained}}$ when systems reach equilibrium.
>
> **Say.** Build a calorimetry simulator: two substances in thermal contact, equilibrating over time.
>
> **Constrain.** Two boxes side by side, particles in each. Each box has its own initial $T_i$ and total energy. When the wall between them is "thermally conducting," energy flows: the hotter side's particles transfer energy to the cooler side via the boundary. Display each side's $T$ over time. They should converge to a common equilibrium $T_f$.
>
> **Verify.** $T_f$ matches the calorimetry calculation: $m_1 c_1 (T_1 - T_f) = m_2 c_2 (T_f - T_2)$.

Save as `01b-calorimetry-preview.html`. Bridge to Chapter 2.
