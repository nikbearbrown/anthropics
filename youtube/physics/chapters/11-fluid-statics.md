# Chapter 11 — Fluid Statics

*Why pressure has no direction, and why that changes everything.*

---

In 2019, Victor Vescovo descended $10{,}928 \text{ m}$ to the bottom of the Challenger Deep — the deepest known point in any ocean — in a custom-built submersible called the *Limiting Factor*. The pressure outside the hull at that depth is roughly $1{,}100$ times atmospheric: about $110 \text{ MPa}$, or the equivalent of ten compact cars stacked on every square inch of the titanium sphere that kept him alive.

Here is how you compute that number. You don't need a pressure gauge that can survive $110 \text{ MPa}$. You need the depth and the density of seawater:

$$P = \rho g h = 1{,}030 \times 9.80 \times 10{,}928 \approx 1.10 \times 10^8 \text{ Pa}.$$

That's it. One equation, three numbers, the crushing force that the hull engineers had to design against. The depth-pressure formula is derived from nothing more exotic than weighing the column of water above a point and dividing by area. Yet it predicts pressures that destroy everything not specifically engineered to survive them — and it does so exactly, all the way to the bottom of the ocean.

This is the character of fluid statics. The machinery is simple. The consequences run from the Mariana Trench to the pressure in your car's tires to why an ice cube floats in a glass of water. The same equations, different numbers.

---

## Pressure: the scalar that replaces a thousand force vectors

When a solid pushes on something, it pushes in a definite direction. A beam under compression pushes downward at its base. A wall pushes outward against whatever leans on it. Force has direction.

![Two panels: left shows pressure in a static fluid acting equally in all directions on a small probe (a scalar). Right shows stress in a stretched solid: forces are different along principal directions (a tensor).](../images/11-fluid-statics-fig-01.png)
*Figure 11.1 — Fluid Pressure Is Isotropic — Solid Stress Is Directional*

A fluid at rest is different. At any point inside a static fluid, the pressure acts equally in every direction. The fluid pushes on every face of any imaginary surface you insert — upward, downward, sideways — with the same force per unit area. Pressure is a **scalar**: a single number per point, carrying no directional information.

This is not immediately obvious. It's worth deriving, at least in outline. Imagine a tiny wedge of fluid — a triangular prism — in equilibrium. The forces on its three faces must balance. If the pressure on the slanted face were different from the pressure on either rectangular face, there would be a net force on the wedge and it would accelerate. For any angle of wedge in any orientation, equilibrium requires the pressure on all faces to be equal. Since the angle is arbitrary, the pressure must be the same in every direction.

This property — pressure is the same in every direction at a point in a static fluid — is what distinguishes fluid from solid. A solid can sustain shear: push it sideways with the surface held fixed, and it holds. A fluid cannot. Any horizontal gradient in pressure at a fixed depth would cause horizontal flow; the fluid would move until the gradient was eliminated. Static means the flow has stopped, which means the pressure has settled into a distribution where the only gradients are vertical.

The formula for pressure is:

$$P = \frac{F}{A}.$$

Units: pascals, $1 \text{ Pa} = 1 \text{ N/m}^2$. The atmosphere at sea level is about $10^5 \text{ Pa}$ — the weight of the entire air column above you, per square meter of your body. You don't feel it because every surface inside your body is at the same pressure, pushing outward.

<!-- → [INFOGRAPHIC: diagram of a submerged object showing pressure arrows pointing inward from all sides — top, bottom, left, right, and at 45° — all equal in length at the same depth, to make concrete the isotropy of pressure in a static fluid; label "pressure acts equally in all directions at this depth"] -->

Some pressure values worth internalizing:

The atmosphere at sea level: $1.013 \times 10^5 \text{ Pa} = 1 \text{ atm} \approx 14.7 \text{ psi} \approx 760 \text{ mmHg}$. A car tire (gauge pressure above atmospheric): $\sim 2$–$3 \text{ atm}$. Blood pressure (systolic): $\sim 120 \text{ mmHg} \approx 16 \text{ kPa}$. The deepest ocean: $\sim 1{,}100 \text{ atm}$.

---

## How pressure varies with depth

![A column of fluid with cross-sectional area A and height h. Pressure at depth h equals atmospheric P₀ plus the weight of fluid above, per unit area: P = P₀ + ρgh. The slope is 9,800 Pa/m for water.](../images/11-fluid-statics-fig-02.png)
*Figure 11.2 — Hydrostatic Pressure — Weight of the Column Above*

The depth-pressure relation follows from a single free-body diagram. Consider a column of fluid of cross-section $A$ between depth $h_1$ (top) and depth $h_2 > h_1$ (bottom). The weight of the column is $\rho A (h_2 - h_1) g$. The column is in equilibrium: the pressure at the bottom pushing up must exceed the pressure at the top pushing down by exactly the column's weight per unit area:

$$P_2 - P_1 = \rho g (h_2 - h_1).$$

Measuring from the free surface (where $P = P_0$, atmospheric pressure):

$$P = P_0 + \rho g h.$$

![Three differently shaped containers filled with water to the same height h. Pressure at the bottom is the same in all three: P = P₀ + ρgh. The width or amount of water above an arbitrary point does not change the pressure at...](../images/11-fluid-statics-fig-03.png)
*Figure 11.3 — Hydrostatic Paradox — Shape Doesn't Matter, Only Depth*

![Logarithmic ladder of pressure at various depths in water. Teacup 7 cm (0.7 kPa above atm), swimming pool 2 m (20 kPa), shipwreck 100 m (1 MPa), Titanic depth 3800 m (38 MPa), Mariana Trench 11,000 m (110 MPa = ~16,000 psi)....](../images/11-fluid-statics-fig-07.png)
*Figure 11.7 — Pressure vs Depth — Teacup to the Bottom of the Ocean*

Three things about this formula. First, notice what doesn't appear: the shape of the container. A tall narrow test tube and a wide swimming pool of the same depth have the same pressure at the bottom. The only thing that matters is the vertical height of fluid above the point. Second, the formula is linear: every additional meter of water adds $\rho g \times 1 \text{ m} = 1{,}000 \times 9.80 \approx 9{,}800 \text{ Pa} \approx 0.1 \text{ atm}$. At $10 \text{ m}$ depth, you've added a full atmosphere. This is why scuba divers feel pressure in their ears almost immediately, and why untrained breath-hold divers who try to descend past $20 \text{ m}$ are working against three atmospheres of absolute pressure. Third, the formula requires incompressible fluid — constant $\rho$. Water is nearly incompressible to depths of kilometers; air is not, which is why the atmospheric pressure calculation requires an integral (the scale height of the atmosphere is about $8 \text{ km}$, and density falls exponentially with altitude).

<!-- → [INFOGRAPHIC: two containers side by side — a tall narrow test tube and a wide shallow swimming pool, both filled to the same height h; dashed horizontal line at depth h in each; pressure label P = P₀ + ρgh at the bottom of both; arrow pointing to the label "same pressure at same depth, regardless of container shape" — to make concrete that depth, not container geometry, determines pressure] -->

### Pascal's principle and the hydraulic jack

If you increase the pressure at one point in an enclosed fluid by $\Delta P$ — say by pushing a piston — that pressure increase propagates unchanged through the entire fluid. This is **Pascal's principle**. It follows directly from the depth-pressure relation: adding $\Delta P$ at any point shifts $P_0$ uniformly everywhere.

![Cross-section of a hydraulic jack. Small input piston (area A₁, force F₁) connected by incompressible fluid to large output piston (area A₂, force F₂). Pascal: F₁/A₁ = F₂/A₂. Trade-off: small force over long distance lifts...](../images/11-fluid-statics-fig-04.png)
*Figure 11.4 — Hydraulic Jack — Same Pressure, Different Areas, Force Amplified*

The application that every car owner has relied on: the hydraulic jack. You push down on a small piston of area $A_1$ with force $F_1$. The pressure increase is $\Delta P = F_1 / A_1$. A large piston of area $A_2$ now has a force $F_2 = \Delta P \times A_2 = F_1 (A_2 / A_1)$ pushing up on it.

Say $A_1 = 5 \text{ cm}^2$ and $A_2 = 250 \text{ cm}^2$. A $200 \text{ N}$ push on the small piston produces $200 \times (250/5) = 10{,}000 \text{ N}$ on the large one — enough to lift a $1{,}000 \text{ kg}$ car. Force multiplied by $50$.

But: the large piston moves $1/50$ as far as the small one. Push the small piston down $10 \text{ cm}$; the car rises $2 \text{ mm}$. Volume is conserved ($A_1 d_1 = A_2 d_2$), so work is conserved: $F_1 d_1 = F_2 d_2$. Pascal's principle redistributes force at the cost of distance — exactly like a lever, operated with fluid instead of a rigid bar.

<!-- → [INFOGRAPHIC: hydraulic jack diagram — small piston on left (area A₁ = 5 cm², force F₁ = 200 N down, displacement d₁ = 10 cm), connected by fluid to large piston on right (area A₂ = 250 cm², force F₂ = 10,000 N up, displacement d₂ = 2 mm); show the equal pressure in the connecting fluid; label the mechanical advantage = A₂/A₁ = 50 and note that work in = work out] -->

---

## Why things float: Archimedes

Around 250 BC, Archimedes was asked by King Hiero II of Syracuse to determine whether a crown was pure gold or adulterated with silver. The legend says the insight came in the bath: as he submerged, water overflowed, and he realized the volume of water displaced equals the volume of the submerged body. Since gold and silver have different densities, comparing a crown's mass (easily weighed) to its volume (determined by water displacement) would reveal whether it was pure. The shout and the sprint through the streets naked are part of the legend. The physics is real.

**Archimedes' principle:** the buoyant force on an object (fully or partially submerged) equals the weight of the fluid it displaces.

The derivation is just the depth-pressure formula applied to a cube. Submerge a cube of side $L$ with its top at depth $h_1$ and bottom at depth $h_2 = h_1 + L$. Pressure on the bottom: $P_0 + \rho g h_2$. Pressure on the top: $P_0 + \rho g h_1$. Net upward force:

$$(P_{\text{bottom}} - P_{\text{top}}) \times L^2 = \rho g (h_2 - h_1) \times L^2 = \rho g L^3 = \rho g V.$$

That's $\rho V g$ — the weight of a volume $V$ of fluid. The buoyant force is exactly the weight of fluid displaced. The argument generalizes to any shape, since any shape can be thought of as assembled from tiny cubes.

From this principle, the floating/sinking condition is immediate. An object sinks if its weight exceeds the maximum buoyant force, which occurs when the object is fully submerged and displaces its own volume of fluid. The maximum buoyant force is $\rho_{\text{fluid}} g V_{\text{object}}$. The weight is $\rho_{\text{object}} g V_{\text{object}}$. The object floats if $\rho_{\text{object}} < \rho_{\text{fluid}}$; sinks if $\rho_{\text{object}} > \rho_{\text{fluid}}$.

A steel ship doesn't contradict this. Steel ($\rho \approx 7{,}800 \text{ kg/m}^3$) is much denser than water ($1{,}000 \text{ kg/m}^3$). A solid block of steel sinks. But a ship is mostly empty space — a hollow hull that encloses a large volume of air. The ship's total mass divided by its total volume gives an *average* density much less than water's. That average density is what determines floating.

![A cube of side L submerged in water. Pressure on top face is P_top; pressure on bottom face is P_bottom = P_top + ρgL. Net upward force F_b = (P_bottom − P_top)·L² = ρgL³ = weight of displaced fluid. Archimedes' principle.](../images/11-fluid-statics-fig-05.png)
*Figure 11.5 — Buoyancy from Pressure Difference — Archimedes Derived*

<!-- → [INFOGRAPHIC: comparison of three scenarios — (1) solid steel block sinking (ρ_steel >> ρ_water, weight > buoyant force), (2) same mass of steel formed into a hollow hull floating (average ρ < ρ_water, weight = buoyant force at partial submersion), (3) partially submerged hull showing waterline, displaced water volume labeled — to make concrete that it's average density, not material density, that controls floating] -->

### The crown problem

A crown weighs $7.84 \text{ N}$ in air and $6.84 \text{ N}$ when submerged in fresh water. Is it pure gold?

Buoyant force: $7.84 - 6.84 = 1.00 \text{ N}$.

Volume displaced: $F_{\text{buoy}} = \rho_{\text{water}} g V$, so $V = 1.00 / (1{,}000 \times 9.80) \approx 1.02 \times 10^{-4} \text{ m}^3$.

Mass of crown: $7.84 / 9.80 = 0.800 \text{ kg}$.

Density: $\rho = 0.800 / (1.02 \times 10^{-4}) \approx 7{,}840 \text{ kg/m}^3$.

Gold's density is $19{,}300 \text{ kg/m}^3$. The crown's density is less than half of gold's. It is not pure gold.

A pure gold crown of the same mass would displace only about $41 \text{ mL}$ of water ($0.800 / 19300 \approx 4.1 \times 10^{-5} \text{ m}^3$) and would weigh about $7.44 \text{ N}$ when submerged — not $6.84 \text{ N}$. The measured $6.84 \text{ N}$ means the crown is displacing more water than pure gold of the same mass would, which means it is less dense. The goldsmith cheated.

This calculation is also a measurement technique. Weigh an object in air; weigh it submerged. The difference is the buoyant force; from the buoyant force you get the volume; divide mass by volume to get density. You can identify a material without ever cutting it, from the outside, by its gravitational and buoyant behavior.

---

## Density and what it tells you about the world

Density — $\rho = m/V$, units $\text{kg/m}^3$ — is the property of matter that determines almost everything in fluid statics. Some values worth knowing:

Fresh water at $4°\text{C}$: $1{,}000 \text{ kg/m}^3$ (this is the definition of the original kilogram; the density of water was used as the reference). Seawater: $\sim 1{,}030 \text{ kg/m}^3$. Ice: $917 \text{ kg/m}^3$ — less dense than liquid water, which is why ice floats and why ponds freeze from the top down rather than the bottom up, which is why fish survive the winter.

Air at sea level: $1.21 \text{ kg/m}^3$. Helium: $0.18 \text{ kg/m}^3$. A helium balloon floats because helium is less dense than the surrounding air, and the air it displaces weighs more than the helium inside it.

<!-- → [TABLE: density of representative substances — air (1.21), helium (0.18), ice (917), fresh water (1,000), seawater (1,030), aluminum (2,700), iron/steel (7,800), lead (11,300), mercury (13,600), gold (19,300) — all in kg/m³; to give students a feel for the range and to support estimation problems throughout the chapter] -->

A useful pattern: most common metals have densities between $2{,}700$ (aluminum) and $20{,}000$ (platinum). Water is the natural reference at $1{,}000$. Gases at sea level are roughly $1{,}000$ times less dense than water. Anything less dense than the fluid it's in will float; anything more dense will sink.

---

## Everything together

Pull back and look at what the three pieces make.

**Pressure** ($P = F/A$) is force per unit area, scalar in a static fluid. **Depth-pressure** ($P = P_0 + \rho g h$) tells you how pressure varies with depth in an incompressible fluid — linearly, depending only on vertical height. **Pascal's principle** says any applied pressure change propagates unchanged through the fluid — the basis of hydraulic force multiplication. **Archimedes' principle** says the buoyant force equals the weight of displaced fluid — the basis of flotation.

These four statements together cover the behavior of every static fluid you will encounter: water in a pool, oil in a hydraulic brake line, seawater around a submarine, blood in the veins of someone standing, helium in a balloon. The machinery is simple. What changes is the numbers.

![Cross-section of an iceberg floating in seawater. Density of ice (917 kg/m³) divided by density of seawater (1025 kg/m³) gives 0.89 — the submerged fraction. Only the top 11% is visible.](../images/11-fluid-statics-fig-06.png)
*Figure 11.6 — Iceberg — 11% Above, 89% Below, Set by Density Ratio*

Consider the Mariana Trench example from the opening and the ice cube in a glass, as two endpoints. At $10{,}928 \text{ m}$: pressure $\approx 1{,}100 \text{ atm}$, buoyancy enormous (the submersible's hull must be heavy enough not to be pushed upward, and ballast is dropped to rise). At the kitchen table: pressure a few millimeters above ambient (negligible), buoyancy $\rho_{\text{water}} g V_{\text{ice}}$ barely exceeding the ice cube's weight. The ice cube floats with about $8\%$ of its volume above the surface (since $\rho_{\text{ice}} / \rho_{\text{water}} = 917/1000 = 0.917$, the fraction submerged is $0.917$, so $8.3\%$ floats above). This is why icebergs, with the same density ratio, have roughly $90\%$ below the surface. "Tip of the iceberg" is physics.

The depth-pressure formula works at both ends. So does Archimedes. The equations don't care about scale.

---

## Exercises

### Warm-up

**11.1** *(LO 1)* A solid block of aluminum ($\rho = 2{,}700 \text{ kg/m}^3$) has dimensions $0.10 \text{ m} \times 0.10 \text{ m} \times 0.20 \text{ m}$. (a) What is its volume? (b) What is its mass? (c) What is its weight? (d) Would it float in water? In mercury ($\rho = 13{,}600 \text{ kg/m}^3$)?

**11.2** *(LO 2)* A force of $500 \text{ N}$ is applied perpendicular to a $0.025 \text{ m}^2$ surface. (a) What is the pressure in Pa? (b) In atm? (c) In psi?

**11.3** *(LO 3)* What is the gauge pressure (above atmospheric) at the bottom of a $4.0 \text{ m}$ deep fresh-water swimming pool? Express in Pa and in atm.

**11.4** *(LO 5)* A $2.0 \text{ kg}$ object reads $19.6 \text{ N}$ on a spring scale in air and $14.7 \text{ N}$ when fully submerged in water. (a) What is the buoyant force? (b) What is the object's volume? (c) What is the object's density? (d) Will it float or sink when released?

### Application

**11.5** *(LO 3)* Compute the absolute pressure at the bottom of the Mariana Trench ($h = 10{,}928 \text{ m}$, $\rho_{\text{seawater}} = 1{,}030 \text{ kg/m}^3$, $P_{\text{atm}} = 1.01 \times 10^5 \text{ Pa}$). Express in Pa and in atm.

**11.6** *(LO 4)* A hydraulic lift in a garage has a small input piston of area $20 \text{ cm}^2$ and a large output piston of area $500 \text{ cm}^2$. (a) What input force is required to lift a $1{,}800 \text{ kg}$ car? (b) If the input piston moves down $0.25 \text{ m}$, how far does the car rise? (c) Verify that the work done by the input force equals the work done on the car.

**11.7** *(LO 5)* A block of wood with $\rho = 650 \text{ kg/m}^3$ is placed in (a) fresh water and (b) seawater ($\rho = 1{,}030 \text{ kg/m}^3$). In each case, what fraction of the block's volume is submerged?

**11.8** *(LO 5)* A helium balloon has volume $0.050 \text{ m}^3$, balloon-material mass $0.015 \text{ kg}$, and is filled with helium ($\rho_{\text{He}} = 0.18 \text{ kg/m}^3$). Air density is $1.21 \text{ kg/m}^3$. (a) What is the total weight of the balloon system (helium + material)? (b) What is the buoyant force? (c) What maximum additional mass can the balloon lift?

### Synthesis

**11.9** *(LO 1, 5)* An ice cube ($\rho_{\text{ice}} = 917 \text{ kg/m}^3$) with side length $5.0 \text{ cm}$ floats in a glass of fresh water. (a) What volume of ice is submerged? (b) What height of ice extends above the water surface? (c) If the water were replaced with seawater ($\rho = 1{,}030 \text{ kg/m}^3$), would more or less ice be above the surface? Calculate the new height.

**11.10** *(LO 3, 5)* A scuba diver descends to $30 \text{ m}$ in seawater. (a) What absolute pressure does she experience (in Pa and atm)? (b) At the surface, her buoyancy compensator (BC) vest held $4.0 \text{ L}$ of air at $1 \text{ atm}$. At $30 \text{ m}$, the air compresses. Using $P_1 V_1 = P_2 V_2$ (isothermal), what volume does the BC air occupy at depth? (c) How has the diver's buoyancy changed compared to the surface?

**11.11** *(LO 1, 4, 5)* You have a mystery metal object. In air it weighs $18.0 \text{ N}$. Submerged in fresh water it weighs $15.5 \text{ N}$. Submerged in an unknown fluid it weighs $14.0 \text{ N}$. (a) Find the object's volume. (b) Find the object's density. (c) Identify the metal (consult a density table). (d) Find the density of the unknown fluid.

### Challenge

**11.12** *(LO 3, 4, beyond chapter)* A cylindrical water tower is $20 \text{ m}$ tall with a $5.0 \text{ m}$ diameter, filled to the top. (a) What is the gauge pressure at the base? (b) What is the total force on the circular base? (c) A pipe $0.10 \text{ m}$ in diameter exits the base. If a valve is opened, what force does the water exert on the valve gate? (d) If the same pipe were connected to a hydraulic piston of area $2.0 \text{ m}^2$, what force could the water pressure produce?

**11.13** *(LO 5, beyond chapter)* A ship has mass $M = 8.0 \times 10^6 \text{ kg}$ and hull volume $V_{\text{hull}} = 9{,}000 \text{ m}^3$ (the volume enclosed by the hull below the waterline when floating). (a) Verify that this hull volume provides enough buoyancy to float the ship in seawater. (b) If the ship takes on $5.0 \times 10^5 \text{ kg}$ of water through a breach, by how much does the waterline rise? (Assume the hull cross-section at the waterline is approximately $2{,}000 \text{ m}^2$.) (c) At what total flooded mass will the ship sink?

---



By the end of this chapter you should be able to:

1. Compute density $\rho = m/V$ and use it to identify materials or predict floating/sinking behavior.
2. Compute pressure $P = F/A$ and convert between Pa, atm, mmHg, and psi.
3. Apply $P = P_0 + \rho g h$ to find pressure at any depth in a static incompressible fluid.
4. Apply Pascal's principle to hydraulic systems: compute force amplification and the corresponding distance reduction.
5. Apply Archimedes' principle to compute buoyant force and determine whether an object floats, sinks, or is neutrally buoyant.

**Prerequisites.** Chapter 4 (force, Newton's laws). Chapter 9 (statics — fluid statics is a special case where everything is in equilibrium). Chapter 7 (energy conservation, for understanding why hydraulic jacks don't multiply energy).

**Why this chapter matters.** Fluid statics underlies hydraulic engineering (cranes, brakes, lifts), naval architecture (every ship ever built), ocean and atmospheric science, medicine (blood pressure, intraocular pressure, breathing mechanics), and meteorology. The pressure at the bottom of the Mariana Trench and the pressure that makes your basketball bounce are both described by the same three equations.

---

## ↳ Dig Deeper — Why pressure is a scalar in a fluid but stress is a tensor in a solid

*Solids resist shear; fluids do not. This single physical difference means that the state of stress in a solid requires six independent numbers (a tensor), while in a static fluid it reduces to one (a scalar — pressure).*

**Prompt:**
> Explain why pressure in a static fluid can be described by a single scalar, while stress in a solid requires a tensor. Walk through the physical argument: a fluid cannot sustain static shear stress (any shear sets it in motion), so all off-diagonal stress-tensor components vanish, and the diagonal components must be equal (otherwise the fluid would shear under unequal compression). End with one sentence on what changes when the fluid moves — then viscosity introduces shear stresses, and pressure alone is no longer sufficient.

**What to do with the output:** Save it. The scalar-vs-tensor distinction is foundational to continuum mechanics and fluid dynamics. It also explains why Chapter 12's Bernoulli equation can treat pressure as a simple scalar even in a moving fluid (when viscosity is neglected).

---

## ↳ Dig Deeper — Atmospheric pressure as the weight of an air column

*Sea-level atmospheric pressure ($\sim 10^5 \text{ Pa}$) is the weight per unit area of all the air above you. But air is compressible: density decreases with altitude. Integrating the varying density gives the pressure profile of the whole atmosphere.*

**Prompt:**
> Estimate atmospheric pressure at sea level using the depth-pressure relation — or its integral form, since air density varies with altitude. Use an atmospheric scale height of about $8 \text{ km}$ (the height over which density falls by a factor of $e$) and show that integrating gives roughly $10^5 \text{ Pa}$. Then explain (a) why the simple formula $P = \rho g h$ is exact for incompressible liquids but only approximate for the atmosphere, (b) why the summit of Mt. Everest ($\sim 9 \text{ km}$) has roughly $37\%$ of sea-level pressure, and (c) what this means physiologically for climbers attempting it without supplemental oxygen.

**What to do with the output:** Save it. The atmospheric pressure calculation connects fluid statics directly to meteorology and high-altitude physiology — two fields where this physics is applied daily.

---

## ↳ Dig Deeper — Surface tension, capillary action, and how insects walk on water

*The surface of a liquid behaves like a thin elastic film under tension. This arises from cohesive forces between molecules at the surface — and it drives menisci, capillary rise, and the remarkable ability of some insects to walk on water.*

**Prompt:**
> Explain surface tension as a consequence of cohesive forces between liquid molecules at a free surface. Then (a) state the surface tension of water at room temperature ($\gamma \approx 0.073 \text{ N/m}$), (b) use Jurin's law $h = 2\gamma\cos\theta / (\rho g r)$ to compute how high water rises in a $1 \text{ mm}$ diameter glass capillary tube (contact angle $\theta \approx 0$ for water on glass, $r$ is the tube radius). End with one sentence on why mercury in a glass tube falls below the surrounding level rather than rising.

**What to do with the output:** Save it. Surface tension is the entry point to soap films, foams, lung surfactant (which keeps alveoli from collapsing), and plant transpiration — a wide range of applications that all trace back to the same molecular cohesion.

---

## LLM Exercise — Chapter 11: Fluid Statics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A pressure or buoyancy analysis of one fluid element in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 11, I want to apply fluid statics — pressure, depth, buoyancy — to one fluid in my phenomenon. Please:

1. Identify ONE fluid element in my phenomenon. Examples:
   - Bike commute: tire pressure (gauge vs. absolute); pressure under each wheel.
   - Coffee maker: pressure of the water column above the heating element; pressure at the brewing chamber gasket.
   - Basketball: pressure inside the inflated ball.
   - Marathon: blood pressure gradient between heart and feet (hydrostatic head).
   - Espresso: pressure profile in the puck during 9-bar extraction (analyze the static piece first).

2. Identify the relevant formula: P = F/A, P = P₀ + ρgh, or Archimedes' principle.

3. Compute it. Express the result in at least two unit systems (Pa, atm, mmHg, or psi as appropriate).

4. Sanity check: does the magnitude match what you'd expect?

5. Identify which assumption (incompressible, static, constant density) is most likely to fail in this case.

6. One sentence on how this connects to Chapter 12 (fluid dynamics) — when fluid moves, pressure becomes part of an energy budget that also includes kinetic energy and elevation.

Save the output as logbook/chapter-11-fluid-statics.md.
```

### What this produces

An eleventh Logbook entry: a fluid-statics analysis of one element in your phenomenon, often surprising in magnitude — tire pressures are multiple atmospheres; blood pressure at the feet is measurably higher than at the heart just from hydrostatic head.

### How to adapt this prompt

- *For phenomena without obvious fluids:* the surrounding air is a fluid. Atmospheric pressure always applies; the pressure inside any closed container (a basketball, a coffee maker, a tire) is gauge pressure above it.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have pressure-time data from a sensor, paste it for analysis.

### Connection to previous chapters

Builds on Chapter 4 (force — pressure × area gives force). Builds on Chapter 9 (fluid statics is force and torque balance applied to fluids). Connects to Chapter 7 (energy conservation is why Pascal's principle doesn't give free energy).

### Preview of next chapter

Chapter 12 takes fluids into motion. Bernoulli's equation is energy conservation along a streamline: $P + \rho g h + \tfrac{1}{2}\rho v^2 = \text{const}$. Where this chapter had pressure increasing with depth, Chapter 12 adds the kinetic-energy term — faster flow has lower pressure, which is the physics behind airplane lift, the Venturi meter, and many biological flow problems.

---

## What would change my mind

The chapter argues that the static-fluid framework — incompressible, scalar pressure, $P = \rho g h$ — is sufficient for most practical engineering and biological applications. The argument would need revision if a class of static-fluid problems systematically required corrections for compressibility or non-scalar stress. Both corrections are real (the atmosphere, viscoelastic fluids), but they're well-handled by extensions of the framework rather than replacements for it.

## Still puzzling

The deepest puzzle this chapter raises and doesn't resolve: **why is pressure isotropic in a static fluid, at the molecular level?** The macroscopic argument (no shear in a static fluid) is correct. But the molecular reason — that random thermal motion equilibrates momentum transfer in all directions equally — connects fluid statics to statistical mechanics in a way that classical Newtonian mechanics alone doesn't capture. Pressure turns out to be $\tfrac{1}{3}\rho \langle v^2 \rangle$ in an ideal gas (the result of kinetic theory), where $\langle v^2 \rangle$ is the mean-square molecular speed. This explains why pressure is a scalar: thermal agitation has no preferred direction. We won't see kinetic theory until Chapter 13.

---

## AI Wayback Machine

**Blaise Pascal** worked out the transmission of pressure in enclosed fluids in the 1640s, producing the principle that bears his name. He is one of the few people in history to have made lasting contributions to physics, mathematics, and philosophy — and to have built one of the first mechanical calculators.

**Run this:**

```
Who was Blaise Pascal, and how does Pascal's principle connect to the fluid statics we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Blaise Pascal"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Pascal's barrel experiment demonstrated pressure transmission in an enclosed fluid.
- Ask it about Pascal's parallel career inventing probability theory and the first mechanical calculator.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 12 adds motion to this chapter's statics. Bernoulli's equation — essentially energy conservation for a moving fluid — adds the kinetic-energy term $\tfrac{1}{2}\rho v^2$ to the pressure and potential-energy terms already here. The result predicts airplane lift, Venturi meters, the speed of water from a hole in a tank, and blood-flow dynamics. Chapter 13 (gas laws) treats compressible fluids, where density varies with pressure and the depth-pressure formula requires the integral form. Chapter 14 (heat) connects pressure to temperature through the ideal gas law. The static-fluid framework installed here is the foundation; every later fluid topic adds something on top of it.

---

**Tags:** fluid-statics, pressure, buoyancy, Pascals-principle, Archimedes
