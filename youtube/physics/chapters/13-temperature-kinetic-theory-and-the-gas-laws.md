# Chapter 13 — Temperature, Kinetic Theory, and the Gas Laws

*Hot is fast. That's the whole secret — and it takes a chapter to say it properly.*

---

![Stylized buckled welded rail. For a 1 km steel rail with α = 12×10⁻⁶/K and ΔT = 70 K, ΔL = 0.84 m must go somewhere. When both ends are constrained, the expansion buckles the rail into a lateral S-curve, derailing trains. CSX...](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-01.png)
*Figure 13.1 — Railroad Sun-Kink — ΔL = αL₀ΔT, Sideways When Constrained*

![Left: bar chart of linear expansion coefficient α (×10⁻⁶/K) for aluminum 25, copper 17, steel 12, Pyrex 3, Invar 1.2. Right: water density vs temperature (0–10 °C) peaking at 4 °C. Below 4 °C, water expands as it cools — why...](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-03.png)
*Figure 13.3 — Thermal Expansion — Materials Compared and Water's Anomaly*

In July 2002, a CSX freight train derailed in Maryland because the tracks buckled in the summer heat. The rails were continuously welded — no expansion gaps — and the day was unusually hot. Steel has a linear thermal expansion coefficient of about $1.2 \times 10^{-5}$ per kelvin. A $1{,}000 \text{ m}$ stretch of rail expanding from $-20°\text{C}$ in winter to $+50°\text{C}$ in summer grows by:

$$\Delta L = \alpha L_0 \Delta T = (1.2 \times 10^{-5})(1{,}000)(70) = 0.84 \text{ m}.$$

Almost a meter. If the rail is constrained — spiked, ballasted, welded at both ends — it can't grow longitudinally. So the expansion goes sideways. The rail forms a snake-like S-curve several meters off-line. A train passes over it and comes off the track.

The engineers who designed modern welded rail knew all of this. They lay the rails at a carefully chosen "neutral temperature" — neither compressed in summer nor in tension in winter — and they pack the ballast tightly to resist lateral movement. But they can't make the expansion go away. The underlying physics is that materials expand when you heat them, and the expansion is a relentless linear function of temperature change. You can engineer around it. You cannot repeal it.

This chapter is about why. Temperature, at the macroscopic scale, is what thermometers measure. At the microscopic scale, it turns out to be something specific: the average kinetic energy of randomly moving molecules. Connecting those two descriptions — the thermometer reading and the molecular motion — is one of the deepest results in all of physics. The railroad track is one face of it; the blue color of the sky, the metabolism of bacteria, the surface temperature of stars, and the reason your tires go flat in winter are other faces of the same thing.

---

![Three parallel vertical thermometers showing Celsius, Fahrenheit, and Kelvin scales side by side. Marked: absolute zero (-273.15 °C / -459.67 °F / 0 K), water freezing (0 / 32 / 273.15), room temperature (20 / 68 / 293.15),...](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-02.png)
*Figure 13.2 — Three Temperature Scales — Celsius, Fahrenheit, Kelvin Aligned*

## Temperature: the three scales and what they mean

A thermometer is a device that reaches thermal equilibrium with whatever it's in contact with and shows you a number. Two systems are at the same temperature if, when you bring them into contact, no heat flows between them. This is the zeroth law of thermodynamics — or, as Feynman put it, the law that defines what temperature *is*. Temperature is the thing that's the same when two systems have stopped exchanging heat.

Three scales:

**Celsius.** Water freezes at $0°$ and boils at $100°$ at one atmosphere. Convenient for weather and cooking; used almost everywhere except the United States.

**Fahrenheit.** Water freezes at $32°$ and boils at $212°$. Used in the U.S. The conversion: $T_F = \tfrac{9}{5}T_C + 32$, or equivalently $T_C = \tfrac{5}{9}(T_F - 32)$.

**Kelvin.** Zero kelvin is absolute zero — the temperature at which molecular motion would, classically, cease entirely. The kelvin degree is the same size as the Celsius degree, just shifted: $T_K = T_C + 273.15$. Since 2019, the kelvin has been defined by fixing Boltzmann's constant at $k_B = 1.380649 \times 10^{-23} \text{ J/K}$ exactly — pulling the temperature scale off the properties of any particular substance and onto a fundamental constant of nature, in the same spirit as the kilogram redefinition we saw in Chapter 1.

Why does kelvin matter? Because the gas law and kinetic theory both involve temperature *multiplicatively*. When you write $PV = nRT$ or $\tfrac{1}{2}m\overline{v^2} = \tfrac{3}{2}k_BT$, the $T$ must be in kelvin. If you use Celsius, you're multiplying by an arbitrarily shifted number, and the equations fail. Kelvin is the scale where $T = 0$ means something physically real: the absence of thermal kinetic energy.

### Thermal expansion

When you heat a material, it expands. Macroscopically:

$$\Delta L = \alpha L_0 \Delta T,$$

where $\alpha$ is the **coefficient of linear expansion** (units: $1/\text{K}$), $L_0$ is the initial length, and $\Delta T$ is the temperature change.

Some typical values: aluminum ($25 \times 10^{-6}/\text{K}$), steel ($12 \times 10^{-6}/\text{K}$), Pyrex glass ($3 \times 10^{-6}/\text{K}$). These are small numbers, which is why thermal expansion is easy to ignore in everyday life and catastrophic when you forget it in engineering.

For volume expansion, $\Delta V = \beta V_0 \Delta T$, where $\beta \approx 3\alpha$ for solids (because expansion happens in all three directions). For liquids, $\beta$ is measured directly; water's $\beta \approx 210 \times 10^{-6}/\text{K}$ at room temperature, much larger than for glass.

Water has a famous anomaly: between $0°\text{C}$ and $4°\text{C}$, it *contracts* on warming rather than expanding. Liquid water is denser at $4°\text{C}$ than at $0°\text{C}$, which is why ice floats and why ponds freeze from the top down. If ice sank, ponds would freeze solid from the bottom up, destroying aquatic life in winter. The anomaly is essential for life.

<!-- → [INFOGRAPHIC: density of water vs. temperature from 0°C to 10°C — showing the maximum density at 4°C, the decrease below 4°C as ice formation begins, and the normal expansion above 4°C; student should see why the coldest surface water is less dense than slightly warmer water at the bottom, causing stratification and top-down freezing] -->

The microscopic reason for expansion: atoms in a solid vibrate in potential wells that are slightly asymmetric — steeper on the compression side than the expansion side. When thermal energy increases, the atoms vibrate with greater amplitude and their average position shifts outward. That outward shift is what we measure as expansion. The asymmetry is mild, which is why $\alpha$ is small. Over large structures and large temperature ranges, the mild asymmetry adds up.

### Thermal stress

If a material is constrained and can't expand, the attempted expansion creates compressive stress. The stress is:

$$\sigma = Y \alpha \Delta T,$$

derived by combining Hooke's law ($\sigma = Y \epsilon$) with the thermal strain ($\epsilon = \alpha \Delta T$). For steel over a $30°\text{C}$ temperature rise: $\sigma = (200 \times 10^9)(12 \times 10^{-6})(30) = 72 \text{ MPa}$. That's below steel's yield stress ($\sim 250 \text{ MPa}$), but it's enough to drive lateral buckling if the rail has any play sideways. The Maryland track buckled, not because the steel yielded, but because sideways motion was easier than compressive yielding.

---

## The ideal gas law: pressure, volume, temperature, and amount

Take a balloon at room temperature and put it in a freezer. When you take it out, it's smaller. The air inside hasn't escaped. What changed?

Temperature dropped. Volume and amount of gas are linked through temperature by the ideal gas law:

$$PV = nRT,$$

where $P$ is pressure in pascals, $V$ is volume in cubic meters, $n$ is the number of moles of gas, $R = 8.314 \text{ J/(mol·K)}$ is the universal gas constant, and $T$ is temperature in kelvin. Equivalently, using the number of molecules $N$ directly:

$$PV = Nk_BT.$$

The law is the union of three earlier experimental observations. **Boyle's law** (1660s): at constant temperature and amount, pressure and volume are inversely proportional. **Charles's law** (1787): at constant pressure and amount, volume is proportional to absolute temperature. **Avogadro's law** (1811): at constant pressure and temperature, volume is proportional to number of molecules. All three are special cases of $PV = nRT$.

![Cubic box containing gas molecules in random motion. Several molecules collide with the walls, transferring momentum. Time-averaged force per unit area equals the macroscopic pressure. Connects to ½mv̄² = (3/2)k_BT.](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-05.png)
*Figure 13.5 — Pressure From Molecular Collisions — The Macro-Micro Bridge*

The law assumes that molecules don't interact except during brief elastic collisions, and that they have no volume themselves. This "ideal gas" approximation is excellent for nitrogen, oxygen, hydrogen, helium, and most common gases at temperatures above their condensation points and pressures below a few hundred atmospheres. Real gases deviate at high pressure (molecules are close enough for intermolecular forces to matter) and low temperature (same reason). For everything in this chapter and most of the book, the ideal gas law is exact enough.

![PV diagram with isotherms for T = 100 K, 200 K, 300 K, 400 K. Each curve is P = nRT/V — hyperbolas. Along one curve: Boyle (T const, PV = const). Vertical (V const): Charles, P/T = const. Reference point: 1 mole at STP (273 K)...](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-04.png)
*Figure 13.4 — Ideal Gas Law — Four Isotherms on the PV Plane*

One useful benchmark: at $T = 273.15 \text{ K}$ (0°C) and $P = 1 \text{ atm}$, one mole of ideal gas occupies:

$$V = \frac{nRT}{P} = \frac{(1)(8.314)(273.15)}{101{,}325} \approx 22.4 \text{ L}.$$

This $22.4 \text{ L/mol}$ at STP (standard temperature and pressure) is worth committing to memory. It's the most-quoted result in introductory chemistry.

### A tire warming up

A car tire is inflated to gauge pressure $230 \text{ kPa}$ at $T_1 = 15°\text{C} = 288 \text{ K}$. After driving, the tire warms to $40°\text{C} = 313 \text{ K}$. Volume doesn't change. New gauge pressure?

Absolute initial pressure: $P_1 = 230 + 101 = 331 \text{ kPa}$.

At constant $V$ and $n$: $P_1/T_1 = P_2/T_2$, so:

$$P_2 = 331 \times \frac{313}{288} \approx 360 \text{ kPa}.$$

New gauge: $360 - 101 = 259 \text{ kPa}$ — about $12\%$ higher than cold. This matches the familiar advice to check tire pressure cold: driven tires read higher, but the air hasn't changed, only the temperature. The increase doesn't blow the tire, but it does affect the contact patch and handling.

The one thing to get right: always use *absolute* pressure in the gas law, and always use *kelvin* for temperature. Using gauge pressure or Celsius produces nonsense.

<!-- → [CHART: tire pressure (absolute) vs. temperature — x-axis from -20°C to 60°C (253 K to 333 K), y-axis from 250 to 450 kPa; two lines: one for a tire inflated to 230 kPa gauge at 15°C, one for the same tire at 250 kPa gauge — both showing the linear P vs. T relationship from PV = nRT at constant V; horizontal dashed line at 101 kPa (atmospheric) to show the gauge reference; student should see that the pressure rise from cold to hot is predictable and modest] -->

---

## Kinetic theory: temperature is average kinetic energy

Here is the deep question. We've said temperature is what thermometers measure, and that it's related to molecular motion. What is the exact relationship?

For an ideal gas in thermal equilibrium at temperature $T$, kinetic theory gives:

$$\frac{1}{2}m\overline{v^2} = \frac{3}{2}k_BT.$$

The left side is the average kinetic energy per molecule ($m$ is the molecular mass, $\overline{v^2}$ is the mean-square speed). The right side involves only Boltzmann's constant and the absolute temperature. Three degrees of freedom (motion in $x$, $y$, $z$) each contribute $\tfrac{1}{2}k_BT$ — this is the **equipartition theorem**.

Rearranging for the root-mean-square speed:

$$v_{\text{rms}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3k_BT}{m}}.$$

For nitrogen molecules ($m = 28 \times 1.66 \times 10^{-27} \text{ kg} = 4.65 \times 10^{-26} \text{ kg}$) at room temperature ($T = 293 \text{ K}$):

$$v_{\text{rms}} = \sqrt{\frac{3(1.38 \times 10^{-23})(293)}{4.65 \times 10^{-26}}} \approx 510 \text{ m/s}.$$

Five hundred and ten meters per second. Faster than the speed of sound. The air molecules around you right now, the ones you're breathing, are moving at supersonic speeds in all random directions.

![Bar chart of root-mean-square molecular speeds at room temperature: H₂ 1900 m/s, He 1350, N₂ 510, O₂ 480, CO₂ 410, Ne 600. Reference: speed of sound in air 343 m/s. Diffusion is slow because of ~10⁹ collisions per second —...](../images/13-temperature-kinetic-theory-and-the-gas-laws-fig-06.png)
*Figure 13.6 — v_rms at 293 K — All Faster Than Sound, Yet Perfume Diffuses Slowly*

The reason you don't feel them all arrive at once from the same direction is that they're going in every direction, and cancelling. And the reason perfume doesn't fill a room in a millisecond, despite molecules moving at $500 \text{ m/s}$, is that each molecule collides with about $10^9$ other molecules per second, each collision sending it off in a new random direction. The mean free path — the average distance between collisions at standard conditions — is about $70 \text{ nm}$. Moving at $500 \text{ m/s}$ while changing direction every $70 \text{ nm}$ is equivalent to a random walk that drifts across a meter in minutes.

The kinetic-theory formula also explains something striking about different gases. At the same temperature, all gases have the same average kinetic energy ($\tfrac{3}{2}k_BT$ per molecule). But that energy is distributed between speed and mass. Lighter molecules move faster:

- Hydrogen ($m = 2 \text{ amu}$): $v_{\text{rms}} \approx 1{,}930 \text{ m/s}$ at $300 \text{ K}$.
- Nitrogen ($m = 28 \text{ amu}$): $v_{\text{rms}} \approx 517 \text{ m/s}$.
- Carbon dioxide ($m = 44 \text{ amu}$): $v_{\text{rms}} \approx 412 \text{ m/s}$.

Hydrogen moves nearly five times faster than CO₂ at the same temperature. This is not a coincidence; it follows directly from the formula ($v_{\text{rms}} \propto 1/\sqrt{m}$, and $\sqrt{44/2} \approx 4.7$).

<!-- → [TABLE: rms speeds of common gas molecules at 300 K — columns: molecule, molar mass (amu), m (kg), v_rms (m/s); rows: H₂ (2, 3.32×10⁻²⁷, 1930), He (4, 6.65×10⁻²⁷, 1370), N₂ (28, 4.65×10⁻²⁶, 517), O₂ (32, 5.31×10⁻²⁶, 484), CO₂ (44, 7.31×10⁻²⁶, 412); final row: speed of sound in air at 300 K (343 m/s) for comparison — student should see that all molecules move faster than sound, lighter ones much faster, and understand the 1/√m dependence] -->

This speed difference has a planetary consequence. Earth's escape velocity is $11{,}200 \text{ m/s}$. The rms speed of hydrogen at room temperature is $1{,}930 \text{ m/s}$ — only $17\%$ of escape velocity, but molecules aren't all at the rms speed. The Maxwell-Boltzmann distribution has a long tail: a significant fraction of hydrogen molecules are moving at $11{,}000 \text{ m/s}$ or faster. That tail continuously leaks hydrogen to space. Over geological time ($4.5 \times 10^9$ years), essentially all of Earth's primordial hydrogen escaped. Nitrogen ($m = 14\times$ heavier) moves $\sqrt{14} \approx 3.7\times$ slower on average; the tail above escape velocity is negligible, and nitrogen has stayed with us.

### The ideal gas law, derived

The ideal gas law isn't just an empirical observation — it follows from kinetic theory. Here is the derivation in brief. Consider a cubical box of side $L$ containing $N$ molecules. A molecule moving in the $x$-direction hits the wall and bounces back: the momentum transfer is $2mv_x$. The time between successive collisions of one molecule with that wall is $2L/v_x$. So the average force from one molecule is $2mv_x / (2L/v_x) = mv_x^2/L$. Summing over all $N$ molecules and all three directions, using $\overline{v^2} = 3\overline{v_x^2}$ by symmetry, and $PV = F \cdot L$:

$$PV = \frac{1}{3}Nm\overline{v^2} = \frac{2}{3}N \cdot \frac{1}{2}m\overline{v^2} = \frac{2}{3}N \cdot \frac{3}{2}k_BT = Nk_BT.$$

Which is exactly $PV = Nk_BT$. The ideal gas law is not an empirical coincidence. It is a theorem of classical mechanics applied to a gas of non-interacting particles.

This derivation is worth sitting with. "Pressure" and "temperature" are macroscopic concepts — things you measure with gauges and thermometers. Kinetic theory shows they emerge from something mechanical: the momentum transfers of individual molecules bouncing off walls and from each other. Macroscopic thermodynamics, from microscopic Newtonian mechanics. Boltzmann spent decades fighting to establish this connection against physicists who doubted atoms existed. He was right.

---

## What temperature actually is

Step back and look at what this chapter has established.

**Temperature** is a macroscopic property tied to the average kinetic energy of molecules: $\bar{KE} = \tfrac{3}{2}k_BT$. "Hot" means molecules moving fast on average. "Cold" means molecules moving slowly on average. Absolute zero ($T = 0$) is the limit where the average kinetic energy approaches zero — unreachable in practice, approached but never achieved.

**Thermal expansion** is a macroscopic consequence: faster-vibrating atoms push outward in asymmetric potential wells. The expansion is small per degree but relentless.

**The ideal gas law** connects pressure, volume, temperature, and amount: $PV = nRT$. It's derived from kinetic theory; it's verified by every balloon and tire and weather balloon in the world.

**Molecular speeds** are large — hundreds of meters per second at room temperature — but thermal averaging and constant collisions prevent the kinetic energy from manifesting as directed flow.

<!-- → [INFOGRAPHIC: Maxwell-Boltzmann speed distribution for nitrogen at three temperatures — 200 K, 300 K, 600 K — showing three curves on the same axes (x: molecular speed 0–2000 m/s, y: relative probability); at higher T, the peak shifts right and broadens; mark v_rms on each curve; student should see that temperature shifts and broadens the whole distribution, not just the average, and should understand why the high-speed tail matters for atmospheric escape] -->

The scale shift available here: room temperature ($300 \text{ K}$) has $k_BT \approx 0.026 \text{ eV}$ of thermal energy per molecule. The interior of the sun ($\sim 1.5 \times 10^7 \text{ K}$) has $k_BT \approx 1.3 \text{ keV}$ — enough to ionize atoms and fuse nuclei. The cosmic microwave background today ($T = 2.7 \text{ K}$) has $k_BT \approx 2 \times 10^{-4} \text{ eV}$ — cold enough that photons can barely shake a molecule. The same formula $\bar{KE} = \tfrac{3}{2}k_BT$ works at every scale. The physics doesn't change; only the numbers do.

---

## Exercises

### Warm-up

**13.1** *(LO 1)* Convert each temperature: (a) $25°\text{C}$ to Fahrenheit and Kelvin; (b) $98.6°\text{F}$ (body temperature) to Celsius and Kelvin; (c) $0 \text{ K}$ to Celsius and Fahrenheit; (d) $4{,}000 \text{ K}$ (surface of a cool star) to Celsius.

**13.2** *(LO 2)* A steel railroad rail is $25 \text{ m}$ long at $20°\text{C}$. ($\alpha_{\text{steel}} = 12 \times 10^{-6}/\text{K}$.) (a) By how much does it expand on a $45°\text{C}$ day? (b) What gap must be left between rails to accommodate summer expansion from $-10°\text{C}$ to $+50°\text{C}$?

**13.3** *(LO 3)* A sealed container holds $0.50 \text{ mol}$ of gas at $300 \text{ K}$ and $1.0 \text{ atm}$. (a) What is the volume? (b) The container is heated to $600 \text{ K}$ at constant volume. What is the new pressure?

**13.4** *(LO 4)* Compute $v_{\text{rms}}$ for helium atoms ($m = 6.65 \times 10^{-27} \text{ kg}$) at $300 \text{ K}$. Is this faster or slower than nitrogen at the same temperature? By what factor, and why?

### Application

**13.5** *(LO 2)* A glass beaker ($V_0 = 500 \text{ mL}$, Pyrex $\alpha = 3 \times 10^{-6}/\text{K}$) is filled to the brim with water ($\beta = 210 \times 10^{-6}/\text{K}$) at $20°\text{C}$. Both are heated to $80°\text{C}$. (a) By how much does the water volume increase? (b) By how much does the beaker volume increase? (c) How much water spills over?

**13.6** *(LO 3)* A scuba diver's tank holds $11.0 \text{ L}$ of air at $200 \text{ atm}$ and $20°\text{C}$. (a) How many moles of gas? (b) The diver descends to a depth where ambient pressure is $4.0 \text{ atm}$. If the regulator delivers air at ambient pressure, what volume of air (at $4.0 \text{ atm}$) does the tank contain? (c) If the diver breathes $0.50 \text{ L/breath}$ at depth pressure, how many breaths does the tank supply?

**13.7** *(LO 3)* A weather balloon at sea level has volume $4.0 \text{ m}^3$ at $20°\text{C}$ and $1.0 \text{ atm}$. It rises to $10 \text{ km}$, where pressure is $0.26 \text{ atm}$ and temperature is $-50°\text{C}$. What is the balloon's new volume? (Use the full ideal gas law — don't assume constant temperature.)

**13.8** *(LO 4)* At what temperature would the rms speed of nitrogen molecules equal the speed of sound in air at room temperature ($343 \text{ m/s}$)? Is this above or below room temperature, and does that make sense?

### Synthesis

**13.9** *(LO 1, 2, 3)* A propane tank for a gas grill contains propane at gauge pressure $860 \text{ kPa}$ at $20°\text{C}$. On a hot summer day, the tank temperature reaches $45°\text{C}$. (a) What is the new absolute pressure? (b) What is the new gauge pressure? (c) If the relief valve opens at $1{,}400 \text{ kPa}$ gauge, at what temperature would it open?

**13.10** *(LO 3, 4)* An automobile engine cylinder has volume $0.50 \text{ L}$ when the piston is at the bottom and is compressed to $0.05 \text{ L}$ (compression ratio 10:1) with air at $20°\text{C}$ and $1.0 \text{ atm}$. (a) Using $PV = $ const (Boyle's law, isothermal approximation), what is the pressure after compression? (b) In a real engine the compression is closer to adiabatic ($PV^{1.4} = $ const), giving a higher temperature. If $T$ rises to $700 \text{ K}$ after compression to $0.05 \text{ L}$, what is the pressure using the full ideal gas law?

**13.11** *(LO 2, 3)* A bimetallic strip consists of a $0.10 \text{ m}$ strip of steel bonded to a $0.10 \text{ m}$ strip of aluminum at $20°\text{C}$ ($\alpha_{\text{Al}} = 25 \times 10^{-6}/\text{K}$, $\alpha_{\text{steel}} = 12 \times 10^{-6}/\text{K}$). (a) When heated to $80°\text{C}$, by how much does each strip try to expand? (b) Why does the bonded strip curve, and which way does it bend? (c) What practical device uses this effect?

### Challenge

**13.12** *(LO 4, beyond chapter)* The escape velocity from the Moon is $2{,}380 \text{ m/s}$. (a) Compute $v_{\text{rms}}$ for N₂ at the Moon's dayside surface temperature ($\sim 390 \text{ K}$). (b) Compute $v_{\text{rms}}$ for H₂ at the same temperature. (c) Compare both to the Moon's escape velocity and explain qualitatively why the Moon has essentially no atmosphere despite having gravity.

**13.13** *(LO 3, beyond chapter)* The Van der Waals equation corrects for real-gas behavior: $\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT$. For CO₂: $a = 0.366 \text{ J·m}^3/\text{mol}^2$, $b = 4.29 \times 10^{-5} \text{ m}^3/\text{mol}$. (a) For $1 \text{ mol}$ of CO₂ at $300 \text{ K}$ in $V = 1.0 \text{ L}$, compute the pressure using the ideal gas law. (b) Compute using Van der Waals. (c) What is the percent difference? (d) At what volume does the ideal gas law agree with Van der Waals to within $1\%$ for CO₂ at $300 \text{ K}$?

---



By the end of this chapter you should be able to:

1. Convert temperatures between Celsius, Fahrenheit, and Kelvin, and explain why Kelvin is required for gas-law and kinetic-theory calculations.
2. Compute thermal expansion of solids ($\Delta L = \alpha L_0 \Delta T$) and thermal stress in constrained materials ($\sigma = Y\alpha\Delta T$).
3. Apply the ideal gas law $PV = nRT$ to compute changes in pressure, volume, or temperature when the other two and the amount are known.
4. Apply kinetic theory ($\bar{KE} = \tfrac{3}{2}k_BT$) to compute rms molecular speeds and connect temperature to molecular motion.
5. Interpret qualitatively why lighter molecules escape planetary atmospheres while heavier ones stay.

**Prerequisites.** Chapter 7 (kinetic energy, the microscopic quantity that temperature averages). Chapter 11 (pressure as force per area). Chapter 5 (Hooke's law and Young's modulus, for thermal stress).

**Why this chapter matters.** The gas laws underlie meteorology, refrigeration, combustion engines, scuba diving, and almost every chemical process. Kinetic theory is one of physics's deepest unifications: the macroscopic concept of temperature is microscopically just average kinetic energy. Everything that follows in thermodynamics — heat, entropy, the second law — builds on what this chapter installs.

---

## ↳ Dig Deeper — Why is the kelvin defined by Boltzmann's constant?

*Until 2019, the kelvin was defined as 1/273.16 of the temperature of the triple point of water. In 2019 it was redefined by fixing $k_B = 1.380649 \times 10^{-23} \text{ J/K}$ exactly. The redefinition removed any dependence on a particular substance.*

**Prompt:**
> Explain the 2019 redefinition of the kelvin in terms of the Boltzmann constant. Walk through (a) the previous definition based on the triple point of water, (b) why fixing $k_B$ exactly gives a more fundamental definition, (c) the physical role of the Boltzmann constant — it converts temperature (kelvin) to energy (joules), so $k_BT$ is the characteristic thermal energy per degree of freedom. End with one sentence naming the other SI units redefined in the same 2019 reform and what constants they were tied to.

**What to do with the output:** Save it. The 2019 SI redefinition is the direct continuation of the trend from Chapter 1: pull every standard off a physical artifact and onto a constant of nature.

---

## ↳ Dig Deeper — Why does breathing work? (Boyle's law in the lungs)

*Inhalation: the diaphragm contracts, the chest cavity expands, and pressure inside the lungs drops below atmospheric. Air rushes in. Exhalation: the chest contracts, pressure rises, air is pushed out. The whole mechanism is Boyle's law.*

**Prompt:**
> Apply Boyle's law to the mechanics of human breathing. (a) Estimate the lung volume change during a typical breath (~0.5 L tidal volume on a ~5 L total lung capacity). (b) Compute the pressure change inside the lungs during inhalation, assuming temperature is constant and no air has yet entered (this is the driving differential). (c) Explain how the pressure differential drives airflow until pressures equilibrate. End with one sentence on why breathing becomes labored at high altitude (reduced atmospheric pressure means a smaller absolute driving differential for the same volume change).

**What to do with the output:** Save it. Breathing as a gas-law application is a direct, personal demonstration of Boyle's law that makes the physics immediate.

---

## ↳ Dig Deeper — Maxwell-Boltzmann distribution and why hydrogen escaped Earth

*The kinetic theory gives an average molecular speed. The full distribution — the Maxwell-Boltzmann distribution — shows that a significant fraction of molecules move much faster than average. For hydrogen, this high-speed tail extends above Earth's escape velocity, continuously leaking hydrogen to space.*

**Prompt:**
> Sketch (in description) the Maxwell-Boltzmann speed distribution for a gas at fixed temperature. Label (a) the most probable speed (peak), (b) the mean speed, (c) the rms speed. Then explain why Earth has retained its nitrogen and oxygen but lost almost all primordial hydrogen and helium: use the relative rms speeds at the same temperature ($v_{\text{rms}} \propto 1/\sqrt{m}$) and Earth's escape velocity ($11{,}200 \text{ m/s}$) to show why the high-speed tail of hydrogen's distribution extends into the escape regime while nitrogen's does not. End with one sentence on why the Moon, with escape velocity $2{,}380 \text{ m/s}$, has essentially no atmosphere.

**What to do with the output:** Save it. The atmospheric escape story is one of the most beautiful applications of statistical mechanics to planetary science — and explains something you can see with your own eyes (why the Moon is airless).

---

## LLM Exercise — Chapter 13: Temperature and Gas Laws in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A temperature, thermal-expansion, or gas-law analysis of one element of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 13, I want to apply temperature, thermal expansion, and/or the ideal gas law to one element of my phenomenon. Please:

1. Identify ONE temperature- or gas-related effect. Examples:
   - Bike commute: tire pressure changes with temperature; metal frame expansion in summer.
   - Coffee maker: water heating from 20°C to 95°C; steam dynamics.
   - Basketball: ball pressure variation indoor vs. outdoor in winter.
   - Marathon: body temperature regulation (sweating, evaporative cooling).
   - Espresso: water temperature, steam dynamics, temperature drop during extraction.

2. Identify the relevant equation: thermal expansion (ΔL = αL₀ΔT), ideal gas law (PV = nRT), or kinetic theory (KE = ³⁄₂k_BT).

3. Compute the relevant quantity. Report with units, sig figs, and percent uncertainty.

4. Sanity check with one Fermi estimate.

5. If a gas is involved, compute the rms molecular speed of the relevant gas at the relevant temperature.

6. Identify which simplification (ideal gas, constant α, no phase change) is most likely to fail.

7. One sentence on how this connects to Chapter 14 (heat) — temperature change requires heat transfer, and heat capacity tells you how much energy that requires.

Save the output as logbook/chapter-13-temperature-gases.md.
```

### What this produces

A thirteenth Logbook entry: a thermal analysis applied to your phenomenon. Tire pressure changes and steam volumes are often surprisingly large; molecular speeds are always surprisingly fast.

### How to adapt this prompt

- *For phenomena with no obvious gas:* focus on liquid water behavior or solid thermal expansion.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have temperature-time data from a sensor, paste it for analysis.

### Connection to previous chapters

Builds on Chapter 7 (kinetic energy — temperature is average molecular KE). Builds on Chapter 11 (pressure). Connects to Chapter 5 (Hooke's law gives the thermal stress formula $\sigma = Y\alpha\Delta T$).

### Preview of next chapter

Chapter 14 introduces heat — energy in transit due to temperature difference. Heat capacity tells you how much energy is needed to change a substance's temperature. Latent heat describes phase transitions. Together with this chapter, Chapter 14 completes the foundation of thermodynamics.

---

## What would change my mind

The chapter argues that the ideal gas law and kinetic theory are sufficient for most introductory and engineering applications, with corrections (Van der Waals, quantum statistics) handling extremes. The argument would need revision if a class of common gas behaviors required more than mild corrections at ordinary conditions — they generally don't, outside the very-low-temperature regime where quantum statistics (Bose-Einstein condensation, Fermi degeneracy) take over.

## Still puzzling

The deepest puzzle this chapter raises: **why is there an absolute zero?** Kinetic theory says all motion stops at $T = 0$. But quantum mechanics says zero-point motion remains even there — atoms in a crystal still vibrate, helium doesn't freeze even at absolute zero unless pressurized. The third law of thermodynamics (Nernst's theorem) says you can approach absolute zero arbitrarily closely but never actually reach it. Why not? The answer involves the structure of quantum states and entropy in a way that classical mechanics cannot capture. We'll approach it from the thermodynamics side in Chapter 15.

---

## AI Wayback Machine

**Ludwig Boltzmann** built statistical mechanics in the 1870s and 1880s — showing that macroscopic thermodynamic quantities like temperature and entropy emerge from the statistical behavior of enormous numbers of molecules. He inscribed his entropy formula on his own tombstone: $S = k \log W$.

![Ludwig Boltzmann](../images/ludwig-boltzmann-h28.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Ludwig Boltzmann, and how does his statistical mechanics connect to the kinetic theory and gas laws we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Ludwig Boltzmann"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how the Boltzmann distribution emerges from the requirement of maximum entropy.
- Ask it about Boltzmann's contested battles with Ernst Mach and Wilhelm Ostwald over whether atoms were real.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 14 introduces heat itself — the energy that flows when two objects at different temperatures are brought into contact. Heat capacity, specific heat, latent heat (phase transitions), and the three modes of transfer (conduction, convection, radiation). Chapter 15 builds the full laws of thermodynamics: the first law (energy conservation including heat), the second law (entropy always increases in an isolated system), and the third law (absolute zero is unreachable). The kinetic picture established here — temperature as average molecular KE, pressure as molecular momentum transfer — underpins all of these. Statistical mechanics extends kinetic theory to all states of matter and to quantum systems; it is the deepest foundation of macroscopic physics.

---

**Tags:** temperature, ideal-gas-law, kinetic-theory, thermal-expansion, kelvin
