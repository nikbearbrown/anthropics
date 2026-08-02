# Chapter 13 — Temperature, Kinetic Theory, and the Gas Laws

*What a thermometer measures, and what lives underneath it.*

---

## A railroad track buckles in Maryland

July 2002, Maryland. A CSX freight train is moving along a stretch of continuously welded rail. The day is brutally hot — air temperature in the upper nineties, the steel baking in direct sun. The lead engineer feels the locomotive lurch. Behind him, several cars leave the rails. The track has buckled sideways: sun-kinked, in railroad terminology, bent into an S-curve several meters wide.

The physics is unforgiving. Steel has a thermal expansion coefficient of about $1.2 \times 10^{-5}$ per degree Celsius. A stretch of rail one kilometer long, going from $-20°$C in winter to $+50°$C in summer, expands by:

$$\Delta L = \alpha L_0 \Delta T = (1.2 \times 10^{-5})(1000)(70) = 0.84 \text{ m}.$$

Almost a meter. If both ends are fixed — welded, ballasted, spiked — that expansion can't go longitudinally, so it goes sideways. The rail becomes a snake, and anything running over it derails.

This is the chapter about temperature. Not temperature as a thing you read off a gauge, but temperature as something physical — something happening to the atoms. The railroad track tells you that temperature changes make materials expand, and that even a tiny coefficient of expansion, multiplied over enough material, produces forces large enough to destroy infrastructure. But that's the easy story. The harder, more interesting story is what temperature actually *is* at the level of the atoms. And the answer to that question, once you see it, changes how you think about heat, about gases, about pressure — about almost everything in thermodynamics.

<!-- → [FIGURE: Photo or schematic of sun-kinked rail — overhead view showing an S-curve buckle in otherwise straight track. Caption: "Sun-kink on continuously welded rail. The track expanded; both ends were fixed; the expansion went sideways. The numbers in the text predict this."] -->

---

## Temperature scales and what the zeroth law is saying

Operationally, two objects are at the same temperature if, when you bring them into thermal contact, no heat flows from one to the other. That's the zeroth law of thermodynamics: it's the statement that temperature is a real quantity, that it's the same in both objects when they've equilibrated, and that it's the thing that determines which way heat will flow when two objects touch. Heat flows from high temperature to low. Temperature is what tells you the direction.

Three scales have been invented to measure it.

Celsius (°C) anchors to water: freezing at 0°, boiling at 100° at one atmosphere. Most of the world uses it for everyday life. Fahrenheit (°F) anchors to a different set of reference points and compresses the degree size; water freezes at 32°, boils at 212°. The United States uses it for weather. Neither of these is the right scale for physics.

The right scale is Kelvin. It starts at *absolute zero* — the temperature at which molecular thermal motion would be as small as it can be — and uses the same size degree as Celsius. The conversion is simply $T_K = T_C + 273.15$. Why Kelvin is the right scale isn't a convention; it's physics. The gas laws, the kinetic theory, the blackbody radiation law, the entropy formula — all of them involve temperature multiplicatively, as $T$ in the denominator of an exponent or the numerator of a product. With Celsius, you'd be multiplying by an arbitrarily shifted number and getting nonsense. With Kelvin, $T = 0$ is the physically meaningful zero: the absence of thermal energy.

In 2019, the kelvin was formally redefined: instead of being tied to the triple point of water (the unique temperature at which ice, liquid water, and water vapor coexist — 273.16 K exactly), it was tied to the Boltzmann constant $k_B = 1.380649 \times 10^{-23}$ J/K, fixed by definition. This is the same 2019 redefinition that tied the kilogram to Planck's constant and the ampere to the electron charge. The idea is always the same: anchor a unit to a fundamental constant of nature, not to a lump of matter or a property of one particular substance. Temperature is now defined in terms of energy per molecule per unit of $T$ — which is, as we'll see, exactly what temperature *is*.

<!-- → [TABLE: Three temperature scales side by side — columns: scale, absolute zero, water freezes, water boils, typical room temperature, conversion formula. Rows: Celsius, Fahrenheit, Kelvin. Student should see at a glance why Kelvin is the natural choice: it's the only one with a physically meaningful zero.] -->

---

## Thermal expansion: the mechanism

When you heat a solid, it expands. The formula is:

$$\Delta L = \alpha L_0 \Delta T,$$

where $\alpha$ is the coefficient of linear expansion — a small number, typically $10^{-6}$ to $10^{-5}$ per kelvin depending on the material. Aluminum: $25 \times 10^{-6}/K$. Steel: $12 \times 10^{-6}/K$. Pyrex glass: $3 \times 10^{-6}/K$, which is why Pyrex is used for cookware — it barely changes shape when you move it from a cold oven to a hot flame.

Why do solids expand at all? At the atomic level, atoms in a solid sit in potential wells — each atom is held near an equilibrium position by the forces from its neighbors. The well is shaped roughly like a parabola: symmetric about the minimum, rising steeply on both sides. But only roughly. The actual well is *asymmetric*: it rises more steeply when atoms are pushed together (compression) than when they're pulled apart (extension). When you heat the solid, the atoms vibrate more vigorously — greater amplitude. And because of the asymmetry, the average position shifts slightly outward. More vibration means more displacement from center, and the asymmetric well means the average is not at the center. Macroscopically: the material expands.

<!-- → [FIGURE: Diagram of an asymmetric atomic potential well — a U-shaped curve, steeper on the left (compression) than on the right (extension). Two horizontal lines showing total energy at low T and high T. Vertical dashed lines at the classical turning points for each energy level. The midpoint of the turning points (average position) shifts right as energy increases. Caption: "The asymmetry of the potential well is the entire reason solids expand. A symmetric well would show no net shift in average position, and no expansion."] -->

The asymmetry is mild, which is why $\alpha$ is small. But integrate that small coefficient over a kilometer of railroad track and you get almost a meter of expansion. The engineering response is to lay continuously welded rail at a neutral temperature — neither under tension nor compression at the temperature when it was installed — and to pack ballast tightly so lateral motion is resisted. You can manage the physics. You cannot eliminate it.

Water is the famous exception to the "solids expand, liquids expand" story. Between 0°C and 4°C, water *contracts* on heating — it becomes *denser* as it warms from the freezing point to 4°C, then expands beyond that. This is why ice floats: solid ice is less dense than liquid water at 4°C. And it's why lakes and ponds freeze from the top down rather than the bottom up. As the surface water cools below 4°C, it becomes less dense and stays at the top. The denser 4°C water sinks to the bottom. The surface freezes while the bottom stays liquid — and aquatic life survives winter underneath the ice. The anomaly is real and consequential.

---

## The ideal gas law

Take a balloon, inflate it at room temperature, tie it off. Put it in the freezer. An hour later, take it out. The balloon is smaller — visibly so. The amount of gas inside hasn't changed; the rubber kept it sealed. What happened?

The gas contracted because the temperature dropped. At roughly constant pressure (the rubber provides only a small extra contribution to the pressure balance), a drop in temperature means a proportional drop in volume. This is just one version of the ideal gas law:

$$PV = nRT,$$

where $P$ is absolute pressure in pascals, $V$ is volume in cubic meters, $n$ is the number of moles, $R = 8.314$ J/(mol·K) is the universal gas constant, and $T$ is temperature in kelvin — not Celsius, not Fahrenheit.

Equivalently, using the number of molecules $N$ rather than moles:

$$PV = Nk_BT,$$

with $k_B = R/N_A = 1.381 \times 10^{-23}$ J/K, Boltzmann's constant. These are the same equation. The choice between them is whether you're counting molecules ($N$) or counting moles ($n$); the physics is identical.

The law combines three earlier empirical observations. Boyle found, around 1660, that at fixed temperature and amount, $P$ and $V$ are inversely proportional: $PV = \text{const}$. Charles found, around 1787, that at fixed pressure and amount, volume is proportional to temperature: $V \propto T$. Avogadro found that at fixed pressure and temperature, volume is proportional to the number of molecules. Combine all three and you get $PV = nRT$.

A useful reference point: at standard temperature and pressure (0°C = 273.15 K, 1 atm = 101,325 Pa), one mole of any ideal gas occupies:

$$V = \frac{nRT}{P} = \frac{(1)(8.314)(273.15)}{101{,}325} \approx 22.4 \text{ L}.$$

Twenty-two and a half liters per mole at standard conditions. This number is worth remembering; it's the most-used result in introductory chemistry, and it falls directly out of the gas law.

The law works well for gases at moderate pressures and temperatures — nitrogen, oxygen, helium, hydrogen, air, most common gases at conditions between a rough vacuum and several atmospheres. It breaks down when molecules are close together (high pressure) or when attractive forces between molecules matter (low temperature). The van der Waals equation adds two correction terms — one for intermolecular attraction, one for the finite volume of the molecules themselves — and handles those regimes. But for almost everything introductory physics needs, the ideal version is the right tool.

One thing constantly catches students: the $T$ in $PV = nRT$ is in kelvin. Always. The law says volume is proportional to absolute temperature. At absolute zero, volume would be zero (the gas would have no thermal motion to push on the walls). If you use Celsius, you're computing ratios like $T_2/T_1$ as $(25°\text{C})/(0°\text{C}) = 25/0$ — which is infinite — instead of $(298\text{ K})/(273\text{ K}) \approx 1.09$. Use Celsius in a gas-law calculation and you will get a wildly wrong answer.

---

## Kinetic theory: temperature is molecular kinetic energy

Here is the deep idea, and it is worth sitting with.

A sealed container holds a gas. The gas has a temperature $T$, a pressure $P$, a volume $V$, and the molecules inside are moving — constantly, chaotically, in all directions. The pressure on the walls isn't a smear; it's the sum of billions of tiny momentum kicks as molecules bounce off the walls. The temperature isn't a reading on a gauge; it's the average kinetic energy of those molecules.

Precisely:

$$\frac{1}{2}m\overline{v^2} = \frac{3}{2}k_BT.$$

The average kinetic energy of a molecule — $\tfrac{1}{2}m\overline{v^2}$, where $m$ is the mass of one molecule and $\overline{v^2}$ is the mean square speed — equals $\tfrac{3}{2}k_BT$. The factor of 3 comes from three independent directions of motion: $x$, $y$, and $z$. Each direction contributes $\tfrac{1}{2}k_BT$ to the average energy. This is the equipartition theorem: each degree of freedom gets $\tfrac{1}{2}k_BT$.

Temperature, at bottom, is just a measure of how fast molecules are moving on average.

From this you can compute the root-mean-square speed — the square root of the mean squared velocity, a useful measure of the typical molecular speed:

$$v_{\text{rms}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3k_BT}{m}}.$$

For nitrogen at room temperature ($T = 293$ K, $m = 28 \times 1.66 \times 10^{-27}$ kg $= 4.65 \times 10^{-26}$ kg):

$$v_{\text{rms}} = \sqrt{\frac{3(1.38 \times 10^{-23})(293)}{4.65 \times 10^{-26}}} \approx 510 \text{ m/s}.$$

Five hundred and ten meters per second. Faster than the speed of sound in air (about 343 m/s). The air molecules around you right now, at room temperature, are moving faster than a supersonic aircraft — individually, randomly, in every direction.

Why doesn't perfume fill a room instantly, then? Because the molecules don't travel in straight lines. They collide with each other constantly. The mean free path — the average distance a nitrogen molecule travels between collisions at standard conditions — is about 70 nanometers. At 510 m/s and 70 nm mean free path, a molecule undergoes roughly $7 \times 10^9$ collisions per second. It's moving at supersonic speed but zigzagging through a traffic jam. Net diffusion across a meter takes minutes, not milliseconds.

<!-- → [FIGURE: Illustration contrasting two scales — left panel: single molecule path at 510 m/s with straight-line arrow (labeled "if no collisions: room in ~2 ms"); right panel: same molecule shown as a random walk zigzagging through many collisions over the same time interval, covering a fraction of a meter. Caption: "Speed vs. diffusion. The molecules are fast; the traffic jam is real."] -->

The $v_{\text{rms}}$ formula tells you something important about which molecules stay and which escape. At a given temperature $T$, every molecule has the same average kinetic energy $\tfrac{3}{2}k_BT$. Since $\text{KE} = \tfrac{1}{2}mv^2$, lighter molecules must move faster to have the same energy. Hydrogen at 300 K:

$$v_{\text{rms}} = \sqrt{\frac{3k_BT}{m_{\text{H}_2}}} \approx 1{,}930 \text{ m/s}.$$

That's already about 17% of Earth's escape velocity (11,200 m/s). But the Maxwell-Boltzmann distribution — the full probability distribution of molecular speeds — has a long tail to high speeds. A significant fraction of hydrogen molecules, at any time, are moving well above the rms speed. Over geological time, that high-speed tail has literally leaked hydrogen off Earth. The atmosphere you're breathing has lost most of its original hydrogen; what's here now is bound up in water and organic compounds. Nitrogen and oxygen, being fourteen to sixteen times heavier, have rms speeds much lower than escape velocity, so they stay. The Moon, with escape velocity of only 2,380 m/s, has lost nearly everything — its lack of atmosphere is a direct consequence of the $v_{\text{rms}} \propto 1/\sqrt{m}$ scaling.

<!-- → [CHART: Bar chart of v_rms at 300 K for H₂, He, H₂O, N₂, O₂, CO₂ — bars in ascending order of molecular mass, heights decreasing. Earth escape velocity (11,200 m/s) and Moon escape velocity (2,380 m/s) shown as horizontal reference lines. Student should see immediately which gases escape from each body.] -->

---

## Where the gas law comes from

The ideal gas law is not just an empirical summary. You can derive it from kinetic theory, and the derivation is worth seeing because it shows where both $P$ and $T$ come from at the molecular level.

Imagine a cubic box of side $L$ containing $N$ molecules, each of mass $m$. Consider one molecule moving with speed $v_x$ in the $x$-direction. It bounces between two opposite walls. Each time it hits a wall, it reverses direction: momentum change $2mv_x$. The time between collisions with that wall is $2L/v_x$ (travel to the far wall and back). Force on the wall from this one molecule: momentum transfer divided by time:

$$F_{\text{one}} = \frac{2mv_x}{2L/v_x} = \frac{mv_x^2}{L}.$$

Sum over all $N$ molecules. Pressure is force per area, and area is $L^2$:

$$P = \frac{F}{L^2} = \frac{Nm\overline{v_x^2}}{L^3} = \frac{Nm\overline{v_x^2}}{V}.$$

Now, by symmetry, $\overline{v_x^2} = \overline{v_y^2} = \overline{v_z^2} = \tfrac{1}{3}\overline{v^2}$. So:

$$P = \frac{Nm \cdot \tfrac{1}{3}\overline{v^2}}{V} = \frac{2}{3}\frac{N}{V} \cdot \frac{1}{2}m\overline{v^2}.$$

But $\tfrac{1}{2}m\overline{v^2} = \tfrac{3}{2}k_BT$ (equipartition). Substitute:

$$P = \frac{2}{3}\frac{N}{V} \cdot \frac{3}{2}k_BT = \frac{Nk_BT}{V},$$

which is $PV = Nk_BT$. The ideal gas law. Derived from Newton's second law applied to bouncing molecules, with temperature defined as average kinetic energy.

This derivation is one of the genuinely beautiful moments in physics. The macroscopic quantity on the left — pressure, something you measure with a gauge — follows algebraically from the microscopic picture on the right: $N$ molecules bouncing around with average energy $\tfrac{3}{2}k_BT$. Thermodynamics and mechanics are unified. "Pressure" is not a fundamental thing; it's what a very large number of collisions looks like when you can't track them individually.

<!-- → [FIGURE: Schematic of the derivation — a cube with side L, one molecule shown bouncing between two walls with velocity arrows v_x and -v_x, momentum-change label 2mv_x at the wall, time-between-collisions label 2L/v_x alongside the path. Caption: "The entire gas law in one molecule. Scale up to N, average over directions, substitute equipartition — done."] -->

---

## Three scales, one underlying reality

Step back. Temperature is what a thermometer measures — Celsius, Fahrenheit, or Kelvin, depending on the thermometer and the convention. But what it's measuring, at the atomic level, is the average kinetic energy of randomly-moving molecules. The Kelvin scale is "absolute" not because of an arbitrary convention but because zero kelvin is the point where that kinetic energy is zero — where the molecules stop.

The ideal gas law $PV = nRT$ is a summary of three centuries of careful experiment — Boyle, Charles, Avogadro — but it also falls out in about ten lines of algebra from Newton's laws applied to molecules. Pressure is time-averaged momentum transfer. Temperature is average kinetic energy. Volume is just the container size. The three are linked because all three are aspects of the same molecular motion.

Thermal expansion of solids fits into the same picture. Atoms vibrate in an asymmetric potential well. More temperature means more vibration means more displacement from center, averaged over time. Coefficient $\alpha$ is small because the asymmetry of the well is small. But the integrated effect over large structures is not small — as the railroad engineers in Maryland learned.

The range of temperatures where this framework applies is extraordinary. Atmospheric chemistry at 250 K. A car engine at 1,000 K. The surface of the sun at 5,800 K. The core of a star at $10^7$ K. The same equation $\tfrac{1}{2}m\overline{v^2} = \tfrac{3}{2}k_BT$ runs through all of it, with corrections only at the extremes where quantum statistics or relativistic speeds become relevant. As a piece of unification — macroscopic thermodynamics and microscopic Newtonian mechanics joined by a single equation — it's hard to beat.

---

## Still puzzling

*Why is there an absolute zero?* Classical kinetic theory says all molecular motion ceases at $T = 0$. Quantum mechanics says not quite: zero-point motion remains even at absolute zero, a consequence of the uncertainty principle. The third law of thermodynamics says you can get arbitrarily close to absolute zero but never actually reach it in a finite number of steps. Why zero is a limit rather than a value you can reach — why the last fraction of a kelvin requires infinitely many steps — is one of those things that statistical mechanics explains formally but doesn't make intuitively obvious.

*Why does the Maxwell-Boltzmann distribution have the shape it does?* The distribution of speeds isn't just a bell curve. It's a skewed distribution with a long tail to high speeds. The peak (most probable speed) is lower than the mean, which is lower than the rms — there are more molecules moving slowly than moving very fast, but the very fast tail exists and matters. Deriving this distribution requires statistical mechanics — specifically, counting the number of ways to distribute total energy among molecules, then finding the distribution that maximizes that count subject to fixed total energy. That's the Boltzmann factor, and it underlies not just gas speeds but the population of atomic energy levels, the spectrum of thermal radiation, and the rates of chemical reactions.

*Why do ideal gases exist at all?* The ideal gas is a model: point particles, no intermolecular forces. Real molecules are not points, and they do interact. Yet the ideal gas law works remarkably well for real gases at room temperature and moderate pressures. Why? Because at those conditions, molecules spend most of their time far apart — mean free path far exceeds molecular diameter — so interactions are brief and infrequent. The corrections (van der Waals, virial expansion) are small. The ideal limit is an excellent approximation because the gas is mostly empty space.

---

## Exercises

### Warm-up

**W1.** Convert the following temperatures, showing your work: (a) 37°C (body temperature) to Fahrenheit and Kelvin; (b) 98.6°F to Celsius and Kelvin; (c) 0 K to Celsius and Fahrenheit. What do you notice about (a) and (b)?

*Tests: temperature-scale conversions and the physical meaning of absolute zero. Difficulty: low.*

**W2.** A steel bridge span is 500 m long at 10°C. By how much does it expand when the temperature reaches 38°C? ($\alpha_\text{steel} = 12 \times 10^{-6}/\text{K}$.) Express the answer in both meters and as a fraction of the original length.

*Tests: linear thermal expansion formula, dimensional check. Difficulty: low.*

**W3.** A sealed container holds 0.20 mol of helium at 300 K and 1.0 atm. (a) What is the volume? (b) If the temperature is raised to 450 K at constant volume, what is the new pressure?

*Tests: direct application of $PV = nRT$ in both constant-volume and constant-temperature versions. Difficulty: low.*

**W4.** Compute $v_\text{rms}$ for helium atoms at 300 K. ($m_\text{He} = 6.65 \times 10^{-27}$ kg.) Compare to the speed of sound in air (~343 m/s).

*Tests: kinetic-theory formula for rms speed. Difficulty: low.*

---

### Application

**A1.** A glass beaker (Pyrex, $\alpha = 3 \times 10^{-6}/\text{K}$, volume $V_0 = 500$ mL) is filled to the brim with water at 20°C. The beaker and water are heated together to 80°C. (a) By how much does the water volume increase? ($\beta_\text{water} = 210 \times 10^{-6}/\text{K}$.) (b) By how much does the beaker's interior volume increase? (Use $\beta \approx 3\alpha$ for Pyrex.) (c) How much water spills over?

*Tests: volumetric vs. linear expansion, and the consequence of different expansion coefficients for container and contents. Difficulty: medium.*

**A2.** A car tire is inflated to gauge pressure 220 kPa at 15°C. After a long drive the tire temperature reaches 48°C. Assuming volume is constant, find the new gauge pressure. (Remember: the gas law requires absolute pressure.)

*Tests: ideal gas law at constant volume, and the gauge-vs.-absolute pressure distinction. Difficulty: medium.*

**A3.** A scuba diver's tank holds 12.0 L of air at 200 atm and 20°C. (a) How many moles of gas are in the tank? (b) At a depth of 30 m, the ambient pressure is approximately 4.0 atm. If the regulator delivers air at ambient pressure and the temperature stays at 20°C, what volume of air (at depth pressure) does the tank effectively contain?

*Tests: ideal gas law with large pressure ratios; requires careful tracking of which variables are held fixed. Difficulty: medium.*

**A4.** At what temperature would the rms speed of nitrogen molecules ($m = 4.65 \times 10^{-26}$ kg) equal the speed of sound in air at room temperature (343 m/s)? At what temperature would it equal Earth's escape velocity (11,200 m/s)?

*Tests: inverting the $v_\text{rms}$ formula to solve for $T$; connects molecular speed to macroscopically meaningful velocities. Difficulty: medium.*

---

### Synthesis

**S1.** The Eiffel Tower is approximately 300 m tall and made primarily of iron ($\alpha = 12 \times 10^{-6}/\text{K}$). Paris temperatures range from about $-5$°C in winter to $+35$°C in summer. (a) By how much does the tower's height change between its coldest and hottest states? (b) The tower is anchored at its base. Estimate the compressive stress that would build up in the legs if the tower were rigidly prevented from expanding vertically. (Young's modulus for iron: $Y = 211 \times 10^9$ Pa.) Is this stress large enough to cause structural concern?

*Tests: thermal expansion combined with stress analysis; connects $\alpha$ to real engineering consequences. Difficulty: medium-high.*

**S2.** A weather balloon is filled with 5.0 m³ of helium at sea level (20°C, 1.0 atm). It rises to an altitude of 10 km where the pressure is 0.26 atm and the temperature is $-50$°C. (a) What is the balloon's new volume? (b) Compute $v_\text{rms}$ for helium atoms at both altitudes. (c) The balloon is designed to burst when it reaches a volume of 30 m³. Will it burst before or after reaching 10 km? Estimate the altitude at which it bursts, assuming pressure drops roughly as $P \approx P_0 e^{-h/8500}$ with $h$ in meters.

*Tests: ideal gas law with all three variables changing; kinetic-theory calculation at two conditions; requires combining the gas law with an exponential model. Difficulty: high.*

---

### Challenge

**C1.** Derive the ideal gas law $PV = Nk_BT$ from kinetic theory. Work through the argument in the text — one molecule bouncing in a box of side $L$, force on the wall, pressure — without skipping steps. At each stage, state explicitly what physical assumption you are using (elastic collision, symmetry of velocities among directions, equipartition). Identify the one step where thermodynamics enters — where a purely mechanical derivation hands off to a statistical one.

*Tests: reconstruction of the kinetic-theory derivation from first principles, with explicit attention to assumptions. Difficulty: high.*

---

## LLM Exercise — Chapter 13: Temperature and Gas Laws in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A temperature, thermal-expansion, or gas-law analysis of one element of your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 13, I want to apply temperature, thermal expansion, and/or the ideal gas law to one element of my phenomenon. Please:

1. Identify ONE temperature- or gas-related effect in my phenomenon. Examples:
   - Bike commute: tire pressure changes with temperature; metal frame thermal expansion in summer.
   - Coffee maker: water heating from 20°C to brewing temperature (~95°C); steam volume.
   - Basketball: ball pressure and temperature variations indoor vs. outdoor.
   - Marathon: body temperature regulation (sweating, evaporative cooling).
   - Espresso: water temperature, steam dynamics, temperature drop during extraction.

2. Identify the relevant equation: thermal expansion ($\Delta L = \alpha L_0 \Delta T$), ideal gas law ($PV = nRT$), or kinetic theory ($\bar{KE} = \tfrac{3}{2}k_B T$).

3. Compute the relevant quantity. Report with units, sig figs, uncertainty.

4. Sanity check with one Fermi estimate.

5. Estimate the molecular rms speed of the relevant gas if applicable.

6. Identify which simplification (ideal gas, constant α, no phase change) is most likely to bite.

7. One sentence on how this connects to Chapter 14 (heat) — temperature change requires heat transfer, and heat capacity tells you how much.

Save the output as logbook/chapter-13-temperature-gases.md.
```

### What this produces

A thirteenth Logbook entry: a thermal/gas analysis applied to your phenomenon, often surprising in the magnitude of pressure changes or molecular speeds.

### How to adapt this prompt

- *For phenomena with no obvious gas* (a marathon, a basketball shot): focus on body-temperature regulation or atmospheric conditions.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have temperature-time data, paste it.

### Connection to previous chapters

Builds on Chapter 7 (kinetic energy — temperature is average KE). Builds on Chapter 11 (pressure). Builds on Chapter 12 (gases as fluids — but compressible).

### Preview of next chapter

Chapter 14 introduces heat itself — energy in transit due to temperature difference. Heat capacity, specific heat, latent heat (phase changes), and the modes of heat transfer (conduction, convection, radiation). Together with this chapter, these establish the foundations of thermodynamics.

---

## AI Wayback Machine

**Ludwig Boltzmann** founded statistical mechanics in the 1870s — showing that thermodynamic quantities like temperature emerge from the statistical behavior of molecules. He carved his entropy formula onto his own tombstone: S = k log W.

**Run this:**

```
Who was Ludwig Boltzmann, and how does his statistical mechanics connect to the kinetic theory and gas laws we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Ludwig Boltzmann"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how the Boltzmann distribution emerges from molecular collisions.
- Ask it about Boltzmann's contested intellectual fights with Ernst Mach and Wilhelm Ostwald over whether atoms existed.

What changes? What gets better? What gets worse?

---

**Tags:** temperature, ideal-gas-law, kinetic-theory, thermal-expansion, kelvin
