# Chapter 2 — Temperature and Thermal Energy

*Temperature is not heat. Thermal energy is not temperature. Heat is energy in transit.*

---

Here is a fact that surprises almost everyone the first time they hear it. The Atlantic Ocean contains more thermal energy than a cup of coffee at 95°C. Far more. By many, many orders of magnitude. And yet if you drop that cup of coffee into the ocean, heat flows *out* of the coffee and *into* the ocean — from the smaller object into the larger one. The ocean, despite its vastly greater thermal energy, absorbs heat from the cup.

Why? Because heat does not flow from the object with more energy to the object with less. Heat flows from the object with higher *temperature* to the object with lower temperature. And temperature is not the same thing as thermal energy.

This distinction — temperature versus thermal energy versus heat — is the single most important thing to get straight in all of thermodynamics. Every confusion I have ever seen in a student's understanding of heat engines, refrigerators, entropy, or climate science traces back to blurring one of these three things into another. The chapter ahead sorts them out.

---

## Temperature

Temperature is a number that tells you how fast the molecules in a substance are moving, on average. More precisely: temperature is proportional to the average translational kinetic energy per molecule.

In three dimensions, each molecule has three translational degrees of freedom — it can move in $x$, $y$, and $z$. The equipartition theorem says each degree of freedom carries, on average, $\frac{1}{2}k_B T$ of energy, where $k_B = 1.38 \times 10^{-23}$ J/K is the Boltzmann constant. So the average translational kinetic energy of a single molecule is $\frac{3}{2}k_B T$, and the temperature is:

$$T = \frac{m \langle v^2 \rangle}{3 k_B}$$

This is the molecular definition. Temperature is the mean of $v^2$ across all molecules, weighted by mass, divided by $3k_B$. It is a per-molecule quantity — it characterizes the *average* energy per particle, not the total energy of the system. That is why temperature is called an *intensive* variable: it does not depend on how much stuff you have. A thimble of water and a swimming pool, both at 20°C, have the same temperature despite having wildly different amounts of thermal energy.

Notice that the definition uses $\langle v^2 \rangle$, not $\langle v \rangle$. These are different. The mean of the squares is not the square of the mean — a fact that will matter in Chapter 3 when we look at the full speed distribution. For now, the important thing is that temperature measures the width of the molecular speed distribution, not the mean speed directly.

<!-- → [TABLE: intensive vs. extensive variables — two columns (Intensive / Extensive), rows: definition, example quantities, behavior when system is doubled, thermometer reads; Temperature and Specific heat capacity go in Intensive; Thermal energy U and Heat capacity mc go in Extensive; reader should see the contrast that motivates the bathtub/ocean example] -->

The scale we use for thermodynamic calculations is the Kelvin scale. Absolute zero — $T = 0$ K — corresponds to the classical limit of no thermal motion. Room temperature is about 293 K. Body temperature is 310 K. The boiling point of water is 373 K. Kelvin and Celsius differ by exactly 273.15: $T(\text{K}) = T(°\text{C}) + 273.15$. Since 2019, $k_B$ is exact by SI definition: $k_B = 1.380649 \times 10^{-23}$ J/K. This means temperature is now defined by fixing $k_B$, not the other way around — an elegant inversion that reflects how precisely we can measure molecular motion.

---

## Thermal energy

Thermal energy is the total internal kinetic energy of all the molecules in a system — translational, rotational, vibrational — plus the potential energy stored in the forces between molecules.

It is an *extensive* variable: it grows with the size of the system. Double the number of molecules at the same temperature, and you double the thermal energy. This is exactly what makes the ocean's thermal energy so enormous despite its moderate temperature: there are roughly $10^{46}$ water molecules in the Atlantic, and each one carries $\frac{3}{2}k_B T$ of translational kinetic energy.

For a monatomic ideal gas — atoms with no rotational or vibrational modes, no intermolecular forces — the thermal energy is simply:

$$U = \frac{3}{2} N k_B T$$

For a diatomic gas at moderate temperatures, where rotation is excited but vibration is not, the count of active degrees of freedom rises to 5:

$$U = \frac{5}{2} N k_B T$$

The factor in front of $Nk_BT$ counts the number of ways the molecule can store energy. A nitrogen molecule tumbling through space has three translational modes and two rotational modes (rotation about the bond axis contributes negligibly at normal temperatures); hence five-halves. At very high temperatures, vibrational modes wake up and add two more, giving $\frac{7}{2}Nk_BT$. The thermal energy of a real gas is richer than it looks.

The relationship $U = \frac{3}{2}Nk_BT$ contains both concepts at once: $T$ is the intensive variable characterizing each molecule, $N$ is what makes the total energy extensive, and $k_B$ converts between the molecular and macroscopic scales. You cannot read thermal energy off a thermometer — a thermometer tells you $T$, not $U$. To get $U$, you need both $T$ and $N$.

---

## Heat

Heat is energy in transit. It is not a property of a system — it is what happens at the boundary between two systems when they are at different temperatures.

The sign convention used throughout this book: $Q > 0$ when heat flows *into* the system; $Q < 0$ when heat flows *out*. This convention is not universal — some older texts reverse it — but it is consistent with the modern statement of the first law: the internal energy of a system increases when heat enters and when work is done on it.

Heat has units of joules. An older unit, the calorie, is 4.184 J — the energy needed to raise one gram of water by one degree Celsius at standard pressure. The dietary Calorie (capital C) is a kilocalorie: 4184 J.

There are three mechanisms by which heat moves, and they are physically distinct.

<!-- → [INFOGRAPHIC: three-panel comparison of conduction, convection, and radiation — each panel shows the physical mechanism (molecular collisions along a rod; rising hot fluid with circulation arrows; electromagnetic waves crossing a vacuum gap), names the governing law (Fourier / empirical convection coefficient / Stefan-Boltzmann), and gives a real-world example; reader should see at a glance that the three mechanisms require different physical conditions and have different rate laws] -->

**Conduction** is heat transfer through a material by molecular collision, without bulk motion of the material. The molecules in the hotter region vibrate faster; they collide with their slower neighbors and transfer kinetic energy along a temperature gradient. The rate is described by Fourier's law:

$$\frac{dQ}{dt} = -kA\frac{dT}{dx}$$

where $k$ is the thermal conductivity of the material, $A$ is the cross-sectional area, and $dT/dx$ is the temperature gradient. Metals conduct heat well because free electrons — in addition to atomic vibrations — carry energy rapidly. Insulators (air, wood, aerogel) conduct poorly because there are no free electrons and the atomic network is either low-density or disordered.

**Convection** is heat transfer by bulk motion of a fluid. Hot fluid rises (it is less dense), carries thermal energy upward, and is replaced by cooler fluid from below. This is why you stir a pot when cooking, why heating systems blow warm air from floor vents rather than ceiling vents, and why wind matters more than air temperature on a cold day. The rate of convective heat transfer depends on fluid velocity, geometry, and a collection of empirical parameters that constitute most of the engineering science of heat transfer.

**Radiation** is heat transfer by electromagnetic waves, requiring no material medium. Every object above absolute zero emits radiation; the rate is given by the Stefan-Boltzmann law:

$$P = \sigma A T^4$$

where $\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴) is the Stefan-Boltzmann constant, $A$ is the surface area, and $T$ is the absolute temperature. The strong dependence on $T^4$ means that radiation is negligible at room temperature compared to conduction and convection, but becomes dominant at high temperatures — the Sun radiates at ~5800 K; incandescent bulbs at ~2800 K; a human body at 310 K emits in the infrared, visible to thermal cameras.

The net radiated power of an object at temperature $T$ in surroundings at temperature $T_{\text{env}}$ is:

$$P_{\text{net}} = \sigma A (T^4 - T_{\text{env}}^4)$$

This is the quantity that matters for heat loss: it is the difference of fourth powers, not the difference of temperatures.

<!-- → [CHART: log-scale plot of radiated power P vs. temperature T from 100 K to 10000 K for a 1 m² blackbody — mark labeled points for human body (310 K), incandescent bulb filament (~2800 K), and Sun surface (~5800 K); reader should viscerally see how steeply T⁴ rises and why radiation dominates at high temperatures but is negligible at room temperature] -->

---

## The Zeroth Law

Before we can use temperature in any quantitative way, we need to establish that it is a well-defined property — that when two objects are at the same temperature, they are in thermal equilibrium with each other. This sounds obvious, but it requires proof.

The Zeroth Law states: if system A is in thermal equilibrium with system C, and system B is in thermal equilibrium with system C, then A is in thermal equilibrium with B.

The law was named "zeroth" because it was recognized as logically prior to the First and Second Laws but was only formalized — by Ralph Fowler in the 1930s — after those were already named. It is the law that licenses thermometry: a thermometer (system C) that reads the same value when placed in contact with two different objects (A and B) guarantees that A and B would be in equilibrium with each other. Without the Zeroth Law, temperature readings from the same thermometer could not be meaningfully compared. The entire enterprise of measurement would collapse.

---

## Specific heat capacity

When heat flows into an object, the object's temperature rises. How much it rises per joule depends on the substance — specifically on its *specific heat capacity* $c$:

$$Q = mc\Delta T$$

Here $m$ is the mass and $\Delta T$ is the temperature change. The specific heat is a material property, measured in J/(kg·K).

Water has $c = 4186$ J/(kg·K). This is anomalously high — higher than almost any other common substance. The reason is hydrogen bonding: water molecules form a network of hydrogen bonds with their neighbors, and energy input goes not just into speeding up molecular motion but also into stretching and bending that network. More modes of energy storage means more energy required per degree of temperature rise.

This high specific heat is not a curiosity — it is a fact with enormous consequences. Oceans moderate Earth's climate because they can absorb or release enormous amounts of thermal energy while barely changing temperature. Coastal cities have milder climates than inland cities at the same latitude because the ocean acts as a thermal buffer. The human body is ~60% water by mass; water's high specific heat prevents catastrophic temperature swings when metabolism generates or withdraws heat.

Compare water with metals: copper, $c = 385$ J/(kg·K); iron, $c = 449$ J/(kg·K); aluminum, $c = 900$ J/(kg·K). The same joule that raises a kilogram of water by 0.24°C raises a kilogram of copper by 2.6°C — eleven times more. This is why a copper pan heats up fast and a pot of water takes so long to boil.

---

## Calorimetry

When two objects at different temperatures come into thermal contact, heat flows from hot to cold until they reach a common equilibrium temperature $T_f$. Conservation of energy says the heat lost by the hotter object equals the heat gained by the cooler one:

$$m_1 c_1 (T_1 - T_f) = m_2 c_2 (T_f - T_2)$$

Solving for $T_f$:

$$T_f = \frac{m_1 c_1 T_1 + m_2 c_2 T_2}{m_1 c_1 + m_2 c_2}$$

This is a weighted average of the two initial temperatures, weighted by the *heat capacities* $mc$ — not by the masses alone. The object with the higher heat capacity pulls the equilibrium temperature closer to its initial value.

Let me work through a concrete example. A 200 g copper block at 80°C is dropped into 500 g of water at 20°C. What is the final temperature?

$$m_{\text{Cu}} c_{\text{Cu}} (80 - T_f) = m_{\text{H_2O}} c_{\text{H_2O}} (T_f - 20)$$

$$(0.200)(385)(80 - T_f) = (0.500)(4186)(T_f - 20)$$

$$77(80 - T_f) = 2093(T_f - 20)$$

$$6160 - 77T_f = 2093T_f - 41860$$

$$48020 = 2170T_f$$

$$T_f \approx 22.1°\text{C}$$

The copper drops 58°C. The water rises 2°C. The disproportion is not because the water is large — the water's heat capacity ($500 \times 4186 = 2093$ J/K) is 27 times the copper's ($200 \times 385 = 77$ J/K). The water barely notices.

This calculation assumes a perfectly insulated system — no heat lost to the surroundings. Real calorimetry uses insulated containers precisely to enforce this assumption. The Styrofoam cup calorimeter of an introductory chemistry lab is an imperfect but reasonable approximation; high-precision calorimetry uses vacuum-jacketed Dewar flasks and corrections for the heat capacity of the container itself.

<!-- → [IMAGE: bar chart or thermal diagram of the copper-water calorimetry example — two bars showing initial temperatures (copper at 80°C, water at 20°C) converging to T_f = 22.1°C, with bar widths proportional to heat capacity mc; reader should see why the water barely moves: its bar (mc = 2093 J/K) dwarfs the copper's (mc = 77 J/K)] -->

---

## Thermal expansion

One more phenomenon follows directly from the molecular picture. As temperature rises, molecules move faster and vibrate more vigorously. In a solid, the intermolecular potential is asymmetric — molecules are easier to push apart than to push together, so the average separation grows with energy. The macroscopic consequence is expansion.

For a linear dimension $L$:

$$\Delta L = \alpha L_0 \Delta T$$

where $\alpha$ is the linear thermal expansion coefficient. For steel: $\alpha \approx 12 \times 10^{-6}$/K. For aluminum: $\alpha \approx 23 \times 10^{-6}$/K.

A 10 m steel rail on a summer day that goes from 20°C to 50°C expands by:

$$\Delta L = (12 \times 10^{-6})(10)(30) = 3.6 \times 10^{-3} \text{ m} = 3.6 \text{ mm}$$

Negligible in isolation. But if the rail is bolted down at both ends and cannot expand, that 3.6 mm of thwarted expansion builds into a compressive stress of:

$$\sigma = E \alpha \Delta T = (200 \times 10^9)(12 \times 10^{-6})(30) = 72 \text{ MPa}$$

Seventy-two megapascals. That is roughly half the yield strength of structural steel. Engineers leave expansion joints in bridges, railroad rails, and concrete sidewalks for exactly this reason. The joints look like small gaps; they are load-bearing design features.

Water breaks the rule. Between 0°C and 4°C, water contracts as it warms — its density *increases* with temperature, reaching a maximum at 4°C. Above 4°C it expands normally. The origin is hydrogen-bond geometry: ice has an open hexagonal lattice; as it melts, the lattice partially collapses, packing molecules more tightly. The practical consequence is large: ice, being less dense than liquid water, floats. If ice sank, lakes and rivers would freeze from the bottom up, killing aquatic life. The anomaly of water's density maximum at 4°C is one of the reasons life in cold climates is possible.

<!-- → [CHART: density of water vs. temperature from −5°C to 20°C — curve shows density rising from ~917 kg/m³ (ice at 0°C) to maximum 999.97 kg/m³ at 4°C, then falling; mark the 4°C maximum with a vertical dashed line; inset label: "ice floats because it falls left of this peak"; reader should see the anomaly is a narrow feature, not a gradual slope] -->

---

## What 50 particles can show you now

The ideal-gas simulator from Chapter 0 is already computing temperature from $\langle v^2 \rangle$. The exercise in this chapter's LLM section adds a histogram of particle speeds below the box and overlays the analytical Maxwell-Boltzmann curve. That curve — which we will derive properly in Chapter 3 — is:

$$f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \exp\!\left(-\frac{mv^2}{2k_BT}\right)$$

What you should notice when you build it: the distribution has three characteristic speeds, all different.

The *most probable speed* $v_{mp} = \sqrt{2k_BT/m}$ is the peak of the distribution — the speed the largest number of molecules have.

The *mean speed* $v_{avg} = \sqrt{8k_BT/\pi m}$ is slightly to the right of the peak — the distribution is skewed, so the mean is above the mode.

The *root-mean-square speed* $v_{rms} = \sqrt{3k_BT/m}$ is the one that appears in the temperature formula. It is the largest of the three and sits furthest to the right.

The ordering $v_{mp} < v_{avg} < v_{rms}$ always holds — the distribution is asymmetric, with a long tail to the right. Heavy molecules have narrower distributions at the same temperature; lighter molecules have broader ones. Hydrogen at room temperature has molecules moving at an average of about 1700 m/s; nitrogen at 515 m/s. This is why hydrogen escapes planetary atmospheres over geological time: a large fraction of its molecules exceed escape velocity.

---

## What comes next

Temperature characterizes the average molecular speed. But "average" hides a distribution — and the distribution is interesting. Chapter 3 derives the Maxwell-Boltzmann speed distribution from statistical mechanics: why that particular shape, what the three characteristic speeds tell you, and what happens to the distribution when temperature changes or when molecules have different masses. The simulation you build at the end of this chapter is the tool you will use in Chapter 3 to watch the distribution shift in real time.

---

## Exercises

**Warm-up 1** *(Apply — temperature conversions and molecular speed)*
Compute the temperature in Kelvin for room temperature (20°C), body temperature (37°C), and the surface of the Sun (~5500°C). Then find the rms speed of nitrogen molecules ($m = 4.65 \times 10^{-26}$ kg) at room temperature using $v_{rms} = \sqrt{3k_BT/m}$.

**Warm-up 2** *(Apply — specific heat)*
A 1 kg block of copper at 100°C is placed on an insulating surface and allowed to cool to 25°C. How much thermal energy does it release? ($c_{\text{Cu}} = 385$ J/(kg·K).) Now repeat for 1 kg of water cooling the same 75°C. What does the ratio tell you about water as a thermal storage material?

**Warm-up 3** *(Apply — Stefan-Boltzmann)*
A sphere of radius 5 cm at 500 K sits in a room at 300 K. Estimate the net power radiated. ($\sigma = 5.67 \times 10^{-8}$ W/(m²·K⁴); surface area of a sphere $= 4\pi r^2$.) What happens to the net power if you double the sphere's absolute temperature to 1000 K while the room stays at 300 K?

**Application 1** *(Apply — calorimetry)*
A 300 g iron block at 150°C is dropped into 400 g of water at 22°C in an insulated container. Find the equilibrium temperature $T_f$. ($c_{\text{Fe}} = 449$ J/(kg·K); $c_{\text{water}} = 4186$ J/(kg·K).) Does the answer change if you add a 50 g aluminum stirring rod at 22°C? ($c_{\text{Al}} = 900$ J/(kg·K).) By how much?

**Application 2** *(Apply — thermal expansion and stress)*
A concrete highway slab is 15 m long at 10°C. On a hot summer day it reaches 45°C. How much does it want to expand? If expansion joints are spaced every 15 m but are only 8 mm wide, will the slab buckle? ($\alpha_{\text{concrete}} = 10 \times 10^{-6}$/K.)

**Application 3** *(Apply — conduction)*
A glass window pane is 4 mm thick, has area 1.5 m², and has thermal conductivity $k = 1.0$ W/(m·K). On a winter day the interior surface is at 18°C and the exterior at −5°C. What is the rate of heat loss through the window? How does this compare to the same window with a 10 mm air gap added (double-pane, $k_{\text{air}} = 0.025$ W/(m·K))? What does this tell you about why double-pane windows work?

**Synthesis 1** *(Analyze — connecting mechanisms)*
On a cold day your hands lose heat by all three mechanisms simultaneously. Rank conduction, convection, and radiation by their relative importance for hand heat loss at 0°C wind, and explain your ranking using the governing equations. What changes when wind speed doubles?

**Synthesis 2** *(Analyze — thermal energy vs. temperature)*
Two systems: System A is 1 kg of water at 80°C; System B is 10 kg of water at 25°C. (a) Which has more thermal energy? Estimate the ratio. (b) If A and B are brought into thermal contact in an insulated container, which direction does heat flow? (c) What is $T_f$? Does the answer surprise you?

**Challenge** *(Extend — anomalous water and ecology)*
A lake is 10 m deep. In late autumn the surface cools to 4°C, then continues to 0°C. Describe qualitatively the full density-driven circulation pattern as the lake cools from 10°C to 0°C, and explain why the bottom of the lake stays near 4°C all winter even as the surface freezes. What would happen to fish if water had normal (monotonically decreasing) density with temperature?

---

## LLM Exercises

### Build the temperature-distribution visualizer (`02-temperature-kinetic.html`)

> **Show.** Maxwell-Boltzmann speed distribution: $f(v) = 4\pi (m/(2\pi k_B T))^{3/2} v^2 \exp(-mv^2/(2k_B T))$. Three characteristic speeds: most probable $v_{mp} = \sqrt{2k_BT/m}$, average $v_{avg} = \sqrt{8k_BT/(\pi m)}$, rms $v_{rms} = \sqrt{3k_BT/m}$.
>
> **Say.** Build a temperature + speed distribution visualizer with animated particles.
>
> **Constrain.** D3 v7. 2D box with N=100 particles colored by speed. Slider for T (50–2000 K) and molecular mass (selector for H₂=2, N₂=28, O₂=32, Ar=40). When T is changed, rescale all particle velocities accordingly. Below the box: a histogram of particle speeds updating in real time, with the analytical Maxwell-Boltzmann curve overlaid as a smooth line. Vertical markers at $v_{mp}, v_{avg}, v_{rms}$ with labels. Filename: `02-temperature-kinetic.html`.
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

Save as `02b-calorimetry-preview.html`. Bridge to Chapter 3.
