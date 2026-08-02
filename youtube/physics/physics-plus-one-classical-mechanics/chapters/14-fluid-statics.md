# Chapter 14 — Fluid Statics

*At the bottom of the ocean, everything weighs the same per square inch — and that inch has to hold.*

---

## A submersible at 10,928 meters

In 2019, Victor Vescovo descended in a titanium submersible called the *Limiting Factor* to the bottom of the Challenger Deep: 10,928 meters below the surface of the Pacific Ocean, the deepest place on Earth. The descent took four hours. At that depth, the pressure outside the hull is roughly 1,100 times atmospheric — about 110 megapascals, or 16,000 pounds per square inch.

To survive this, the crew sphere is a 9-centimeter-thick titanium shell machined to sub-millimeter precision. Every square inch of its outer surface is being squeezed by the equivalent of ten compact cars stacked on top of it.

How do you know the pressure before you go? You don't send a pressure gauge down first. You calculate. The depth is known. The density of seawater is known — about $1{,}030 \text{ kg/m}^3$. Multiply by gravitational acceleration and depth:

$$P = \rho g h = 1030 \times 9.80 \times 10{,}928 \approx 1.10 \times 10^8 \text{ Pa.}$$

That is 110 MPa. The engineers who designed the sphere used that number — derived from nothing more than the weight of a column of water divided by area — to calculate how thick the walls had to be. The submersible was built. Vescovo went down. He came back up. The formula was right.

This chapter is about that formula, why it is right, and what else follows from the same logic. Pressure in a fluid. Why pressure increases with depth. Why an enclosed fluid transmits pressure everywhere. And why things float — which Archimedes figured out around 250 BCE and which has not required revision since.

---

## Density and pressure

Two quantities underlie everything else.

**Density** is mass per unit volume:

$$\rho = \frac{m}{V}.$$

Some values worth keeping in your head: fresh water at 4°C is $1{,}000 \text{ kg/m}^3$; seawater, about $1{,}030 \text{ kg/m}^3$; air at sea level, $1.21 \text{ kg/m}^3$. The factor-of-a-thousand difference between water and air sets up all of buoyancy. Aluminum is $2{,}700 \text{ kg/m}^3$; steel, $7{,}800$; gold, $19{,}300$. Gold is nearly twenty times denser than water — which is why Archimedes's trick works: a gold crown and a fake crown of the same mass will displace very different volumes of water when submerged.

**Pressure** is force per unit area:

$$P = \frac{F}{A}.$$

Units: pascals, where $1 \text{ Pa} = 1 \text{ N/m}^2$. Atmospheric pressure at sea level is about $101{,}325 \text{ Pa} = 1 \text{ atm}$. One atmosphere is also about $14.7 \text{ psi}$ and $760 \text{ mmHg}$ (the units used for blood pressure). The pascal is a small unit — you need $100{,}000$ of them to reach one atmosphere — so practical pressure often gets expressed in kilopascals, megapascals, or atmospheres instead.

The same force distributed over different areas gives different pressures. A 70 kg person in regular boots (contact area about $0.06 \text{ m}^2$) presses on snow at about $11{,}400 \text{ Pa}$. The same person in snowshoes (area $0.40 \text{ m}^2$) presses at about $1{,}700 \text{ Pa}$ — nearly seven times less. Snow that collapses under the boots holds under the shoes. Same weight. Different pressure. Different outcome.

Now here is the key property of pressure in a static fluid — the one that makes fluid statics different from solid mechanics. Inside a static fluid, at any point, the pressure is the same in every direction. Push a tiny imaginary cube of water: the pressure on its top face equals the pressure on its bottom face, its left face, its right face, all six faces. Pressure in a fluid is not a vector. It is a scalar.

This is what distinguishes a fluid from a solid. A solid beam can be compressed along one axis while being tensed along another. A static fluid cannot sustain different pressures in different directions — any imbalance would set the fluid in motion, and we have stipulated it is static. The directional complexity collapses to a single number per point, $P(x, y, z)$. Once you know that scalar field, you know all the forces the fluid exerts on any surface: multiply by area, and the force is perpendicular to the surface.

<!-- → [DIAGRAM: two panels side by side — left: a small cube submerged in fluid with equal-length arrows labeled P pointing inward on all six faces; right: a solid block with different-length arrows on different faces (σ_xx ≠ σ_yy), labeled "stress can differ by direction"; caption: "in a static fluid, pressure is the same in every direction — a scalar, not a vector; in a solid, normal stress varies by axis"] -->

---

## Pressure with depth

The depth-pressure formula has the simplest possible derivation. Imagine a column of fluid with cross-section $A$ extending from the surface to depth $h$. The fluid in the column has mass $\rho A h$. Its weight is $\rho A h g$. That weight is supported by the pressure at the bottom of the column minus the pressure at the top:

$$(P_\text{bottom} - P_\text{top}) \times A = \rho A h g.$$

Divide through by $A$:

$$P_\text{bottom} = P_\text{top} + \rho g h.$$

If the surface is exposed to atmosphere at pressure $P_0$:

$$P = P_0 + \rho g h.$$

<!-- → [DIAGRAM: a vertical fluid column of cross-section A from the surface (labeled P_top = P_0, downward arrow) to depth h (labeled P_bottom, upward arrow); the column interior labeled "mass = ρAh, weight = ρAhg"; a bracket along the side labels the depth h; the three derivation steps written as callouts alongside: (P_bottom − P_top)×A = ρAhg → divide by A → P = P_0 + ρgh; caption: "the pressure at any depth is just the weight of the fluid column above it, per unit area — area cancels, shape is irrelevant"] -->

Notice what does not appear in this formula: the area of the column, the shape of the container, the total volume of fluid. The pressure at depth $h$ depends only on the density of the fluid, the gravitational acceleration, and the depth. A narrow laboratory cylinder and a wide ocean basin have exactly the same pressure at 10 meters below their surfaces if both are filled with water. This seems surprising until you see the derivation: it is simply the weight of the column above, per unit area. The width of the container is irrelevant.

<!-- → [DIAGRAM: three containers side by side — a narrow graduated cylinder, a wide flat aquarium, and an irregular vessel (wider at top, narrow at bottom) — all filled with water to the same height h; at the bottom of each, an identical pressure label "P = P_0 + ρgh"; caption: "the pressure at depth h is the same in all three — because it depends only on the height of water above, not on the container's shape or total volume"] -->

Every meter of fresh water adds $\rho g \times 1 \text{ m} = 1000 \times 9.80 \approx 9{,}800 \text{ Pa}$ — about 0.097 atmospheres. Ten meters of fresh water adds almost exactly one atmosphere. This is why scuba divers feel ear pressure at depth and why free divers must equalize frequently. A swimming pool 2 meters deep has, at the bottom, $1.2$ atmospheres absolute — one from the air above, plus $0.2$ from the water column.

The formula assumes the fluid is incompressible and that $g$ is constant. For water, both assumptions are excellent even at thousands of meters — water is nearly incompressible, compressing by only about $0.05\%$ per atmosphere. For air, neither assumption holds well over large altitude ranges; air density falls off with altitude in a way that requires integration rather than simple multiplication. The linear formula works over short altitude ranges. For airplane cabins, mountaineering, and atmospheric science you need the integral form. The Mariana Trench calculation at the chapter's opening works precisely because seawater is nearly incompressible.

---

## Pascal's principle and hydraulic systems

Here is a fact about enclosed fluids that follows directly from the depth-pressure relation. Suppose you have a sealed container of fluid — no free surface — and you increase the pressure at one point by pushing on a piston. The pressure at every other point in the fluid increases by the same amount. This is **Pascal's principle**: pressure applied to an enclosed fluid is transmitted undiminished to every part of the fluid and to the walls of the container.

The proof is in the formula. $P = P_0 + \rho g h$. If $P_0$ increases by $\Delta P$, then $P$ at every depth increases by $\Delta P$. The geometry is irrelevant — the increment propagates everywhere.

The hydraulic jack exploits this. A small piston of area $A_1$ is pushed down with force $F_1$, increasing the pressure in the fluid by $\Delta P = F_1/A_1$. A large piston of area $A_2$ on the other side of the fluid experiences the same pressure increase, generating a force:

$$F_2 = \Delta P \times A_2 = F_1 \times \frac{A_2}{A_1}.$$

If the large piston has fifty times the area of the small one, you get fifty times the force. A modest push produces a force large enough to lift a car.

<!-- → [DIAGRAM: cross-section of a hydraulic jack — small piston on the left (labeled A_1, F_1 ↓) connected via fluid to a large piston on the right (labeled A_2 ≫ A_1, F_2 ↑ with a longer arrow); the same ΔP arrow points into both fluid regions; two annotations below: "force amplification = A_2/A_1" and "distance ratio = A_1/A_2 (large piston moves less)"; caption: "same pressure increment ΔP acts on both pistons — but large area means large force; the trade is force for distance, just like a lever"] -->

This is not free energy. Energy is conserved. The large piston moves $A_1/A_2$ times as far as the small one. Work in (small force times large distance) equals work out (large force times small distance). Pascal's principle redistributes force at the cost of distance — exactly the same trade as a mechanical lever, expressed in fluid language rather than rigid-body language. A hydraulic jack is a lever with an arbitrarily adjustable ratio, set by the ratio of piston areas.

The hydraulic brake in your car works the same way. You push on a small pedal; the master cylinder transmits the pressure to brake cylinders at each wheel that have larger areas; the calipers grip the rotors with forces much larger than your foot could produce directly. The fluid is the mechanical linkage. Unlike a cable, it can route around corners, through complex geometry, to every wheel simultaneously, and it applies the same pressure increment everywhere it goes.

---

## Archimedes' principle

Around 250 BCE, Archimedes of Syracuse was asked whether King Hiero's crown was pure gold or had been adulterated with silver. The density argument was obvious in retrospect: gold and silver have different densities, so a crown of the same mass would have a different volume if it contained silver. But how to measure the volume of an irregular shape without melting it down? The legend says a bath gave him the insight — water displaced by a submerged object reveals the object's volume. The principle he arrived at is more powerful than just volume measurement.

**Archimedes' principle:** the buoyant force on any object submerged in a fluid equals the weight of the fluid the object displaces.

The derivation is clean. Consider a cube submerged in fluid with its top face at depth $h_1$ and its bottom face at depth $h_2 = h_1 + L$. Pressure on the top face: $P_0 + \rho g h_1$, pushing down. Pressure on the bottom face: $P_0 + \rho g h_2$, pushing up. Net upward force:

$$(P_0 + \rho g h_2 - P_0 - \rho g h_1) \times A = \rho g (h_2 - h_1) \times A = \rho g L A = \rho_\text{fluid} g V.$$

Here $V = LA$ is the cube's volume, and $\rho_\text{fluid} g V$ is the weight of a volume $V$ of fluid — the weight of the displaced fluid. The result generalizes to any shape, because any shape can be decomposed into small cubes. The pressure difference between bottom and top always produces an upward force equal to the weight of the displaced fluid.

<!-- → [DIAGRAM: a cube submerged in fluid — top face at depth h_1 with a downward arrow labeled P_top = P_0 + ρgh_1; bottom face at depth h_2 = h_1 + L with a longer upward arrow labeled P_bottom = P_0 + ρgh_2; side faces with equal horizontal arrows (they cancel); a net upward arrow labeled F_buoy = ρ_fluid · g · V beside the cube; the derivation steps shown as a brief callout: "ΔP × A = ρg(h_2 − h_1) × A = ρgV"; caption: "buoyancy comes entirely from the pressure difference between bottom and top faces — the horizontal forces cancel"] -->

Whether an object sinks or floats comes down to a comparison of densities. If the object's density exceeds the fluid's, its weight exceeds the maximum buoyant force (when fully submerged), and it sinks. If the object's density is less, the buoyant force when fully submerged exceeds the weight, and the object rises until partially submerged — floating at whatever depth brings the buoyant force back into balance with the weight.

A floating object displaces a weight of fluid equal to its own weight. This is worth pausing on. An iceberg with density $917 \text{ kg/m}^3$ floating in fresh water (density $1{,}000 \text{ kg/m}^3$) submerges $917/1000 = 91.7\%$ of its volume. In seawater ($1{,}030 \text{ kg/m}^3$), it submerges $917/1030 = 89\%$. The famous "nine-tenths underwater" is approximately correct for seawater. The exact fraction depends only on the ratio of densities.

<!-- → [DIAGRAM: an iceberg cross-section as a tall rectangle — a waterline cuts across it; above the line labeled "~11% visible" with light hatching; below labeled "~89% submerged (seawater)"; a second smaller panel shows the same iceberg in fresh water with slightly more submerged (~92%); below both panels: "submerged fraction = ρ_ice / ρ_fluid — only the density ratio matters, not the size or shape"] -->

A steel ship floats not because steel is less dense than water — steel is about $7.8$ times denser. It floats because the average density of the ship as a whole (steel hull plus enclosed air) is less than water. The hull's enclosed volume gives the ship enough displacement capacity that the buoyant force, spread across all that volume, exceeds the ship's weight. Fill the hull with water — which eliminates the air — and the average density rises well above water's, and the ship sinks. The Titanic sank not because water is heavier than steel, but because flooding the compartments eliminated the air volume that gave the ship its buoyancy.

The gold crown, now quantified. A crown weighs $7.84 \text{ N}$ in air. Submerged in water, a scale reads $6.84 \text{ N}$. The buoyant force is $7.84 - 6.84 = 1.00 \text{ N}$. By Archimedes' principle, this equals the weight of the displaced water: $F_b = \rho_\text{water} g V$, so

$$V = \frac{1.00}{1000 \times 9.80} \approx 1.02 \times 10^{-4} \text{ m}^3.$$

The mass of the crown is $7.84/9.80 = 0.800 \text{ kg}$. Its density: $0.800 / (1.02 \times 10^{-4}) \approx 7{,}840 \text{ kg/m}^3$. Gold's density is $19{,}300 \text{ kg/m}^3$. The crown is not pure gold — its density is barely above steel's. Archimedes was right to be suspicious, and now you know exactly how suspicious to be.

---

## The pressure field from trench to teacup

Return to the opening. Why does the depth-pressure formula work across such a vast range — from a two-meter swimming pool to an eleven-kilometer ocean trench?

Because it is, at its core, Newton's first law applied to a column of fluid in equilibrium. The weight of the fluid above pushes down; the pressure from the fluid below pushes up; they balance. The formula $P = P_0 + \rho g h$ is not a special fluid equation. It is the condition for static equilibrium of a fluid element. Nothing more.

The same logic that produces $9{,}800 \text{ Pa}$ per meter of water produces $110 \text{ MPa}$ at $10{,}928 \text{ m}$. The multiplier is the depth. The physics is identical. This is the kind of universality that is worth pausing to feel: a formula derived by balancing the weight of a thin fluid layer works equally well for a teacup and for the deepest trench in the ocean.

<!-- → [CHART: logarithmic pressure scale on the vertical axis — labeled points from top to bottom: atmosphere (101 kPa), scuba diver at 30 m (4 atm / ~400 kPa), *Titanic* depth 3,800 m (~38 MPa), Challenger Deep 10,928 m (~110 MPa); each labeled with the situation and the calculated P = P_0 + ρgh value; a straight line through all points confirms linear depth-pressure relationship; caption: "the same formula, the same slope of 9,800 Pa/m — from a swimming pool to the deepest trench"] -->

What the formula does not contain is equally important to name. The horizontal extent of the fluid. The shape of the container. The position in the horizontal plane. Pressure in a static fluid is a function only of depth and the surface conditions. This simplicity is the gift of isotropy: because the fluid has no preferred direction in the horizontal, the pressure field has no preferred horizontal direction. It varies only with the one remaining variable: depth.

The limits are worth knowing. Water is nearly incompressible, so $\rho$ stays essentially constant — the formula is exact to within fractions of a percent even at full ocean depth. Air is not: its density falls off with altitude, and the correct relation involves an integral that gives an exponential rather than linear pressure-altitude curve. Over short altitude ranges the linear approximation works well; for anything involving significant vertical extent in the atmosphere, it does not.

And what the formula does not explain: why is pressure isotropic in a static fluid? The mechanical argument — fluids cannot sustain static shear, so they must transmit pressure equally in all directions — is correct. Its molecular basis, which requires statistical mechanics and the kinetic theory of gases, comes in Chapter 19. Until then, isotropy is a fact to use; the reason it holds is a fact to notice.

The design of Victor Vescovo's submersible required knowing the pressure at depth, the stress it would place on a curved titanium shell, and the failure mode if that stress exceeded the material's yield strength. The first step — the pressure — was $P = \rho g h$, the formula in this chapter. The second and third steps are materials engineering, outside this book's scope. But the physics was the entry point. It always is.

---

## Exercises

### Warm-up

**14.1** A $5.0 \text{ kg}$ block of aluminum ($\rho = 2{,}700 \text{ kg/m}^3$) is placed in a tank of water. (a) What is its volume? (b) What is the buoyant force when fully submerged? (c) Does it sink or float? Explain using the density comparison.

**14.2** A force of $600 \text{ N}$ is applied to a surface of area $0.015 \text{ m}^2$. (a) What is the pressure in Pa? (b) Convert to atm and psi. (c) Is this above or below atmospheric pressure?

**14.3** What is the gauge pressure (above atmospheric) at a depth of $8.0 \text{ m}$ in fresh water? Express in Pa and in atm.

**14.4** A $2.0 \text{ kg}$ object weighs $18 \text{ N}$ in air and $12 \text{ N}$ when fully submerged in water. (a) What is the buoyant force? (b) What is the object's volume? (c) What is its density? (d) Does it sink or float in seawater ($\rho = 1{,}030 \text{ kg/m}^3$)?

### Application

**14.5** A hydraulic lift has a small piston of area $15 \text{ cm}^2$ and a large piston of area $600 \text{ cm}^2$. (a) What input force is needed to lift a $1{,}200 \text{ kg}$ car? (b) If the small piston moves down $25 \text{ cm}$, how far does the car rise? (c) How much work is done by the input force? By the output force? Are they equal?

**14.6** A scuba diver descends to $30 \text{ m}$ in seawater ($\rho = 1{,}030 \text{ kg/m}^3$). (a) What is the absolute pressure at that depth in Pa and atm? (b) If the tank delivers air at the same pressure as the surrounding water, what pressure is the diver breathing at $30 \text{ m}$?

**14.7** A wooden block ($\rho_\text{wood} = 650 \text{ kg/m}^3$, volume $0.0040 \text{ m}^3$) floats in fresh water. (a) What fraction of the block is submerged? (b) What is the mass of water displaced? (c) Compare the weight of displaced water to the block's weight.

**14.8** Verify the Mariana Trench calculation from the chapter opening: apply $P = \rho g h$ at $h = 10{,}928 \text{ m}$ in seawater ($\rho = 1{,}030 \text{ kg/m}^3$). Express the result in Pa, atm, and psi. Confirm it is roughly $1{,}100$ times atmospheric pressure.

### Synthesis

**14.9** A hollow steel sphere (outer radius $0.15 \text{ m}$, inner radius $0.12 \text{ m}$, steel density $7{,}800 \text{ kg/m}^3$) is placed in seawater. (a) Calculate the mass of steel in the sphere. (b) Calculate the buoyant force when fully submerged. (c) Does it float or sink? (d) If it floats, what fraction protrudes above the waterline? If it sinks, how much additional enclosed air volume would make it neutrally buoyant?

**14.10** A person's blood pressure is measured at $120/80 \text{ mmHg}$ at heart level. Blood ($\rho_\text{blood} \approx 1{,}060 \text{ kg/m}^3$) must travel from the heart to the brain ($\sim 30 \text{ cm}$ above heart level) and to the feet ($\sim 120 \text{ cm}$ below). (a) What is the hydrostatic pressure increase in blood at foot level compared to heart level? Express in mmHg and Pa. (b) What pressure must the heart supply to push blood upward to the brain against the hydrostatic gradient? (c) Why does standing for long periods cause fluid to pool in the legs?

### Challenge

**14.11** Design problem: a submersible must reach $500 \text{ m}$ in seawater while maintaining interior pressure at $1 \text{ atm}$. (a) What is the exterior pressure at $500 \text{ m}$? (b) What is the pressure difference the hull must withstand, in MPa? (c) The sphere has inner radius $0.80 \text{ m}$. If the hull material has compressive yield strength $500 \text{ MPa}$ and the required safety factor is $3$, what minimum wall thickness is needed? Use the thin-shell approximation: wall stress $= \Delta P \times r / (2t)$ where $t$ is wall thickness. (d) Compare to the $9 \text{ cm}$ titanium hull of the *Limiting Factor* at $11 \text{ km}$.

---

## LLM Exercise — Chapter 14: Fluid Statics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** A pressure or buoyancy analysis of one fluid element in your anchor phenomenon.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 14, I want to apply fluid statics — pressure, depth,
buoyancy — to one fluid in my phenomenon. Please:

1. Identify ONE fluid element in my phenomenon (a static fluid or
   a fluid at near-equilibrium). Examples:
   - Bike commute: tire pressure (gauge vs. absolute); pressure
     under each wheel.
   - Coffee maker: pressure of the water column above the heating
     element; pressure at the brewing chamber gasket.
   - Basketball: pressure inside the inflated ball.
   - Marathon: blood pressure in the runner's circulatory system
     at heart vs. feet (hydrostatic gradient).
   - Espresso: pressure profile in the puck during 9-bar
     extraction (the static piece can be analyzed first).

2. Identify the relevant fluid statics quantity: pressure, depth,
   density, buoyancy.

3. Compute it using P = F/A, P = ρgh, or Archimedes' principle
   as appropriate.

4. Express the result in multiple units (Pa, atm, mmHg, psi as
   appropriate).

5. Sanity check: does the magnitude match what you'd expect?
   (Tire pressures ~a few atm; blood pressure ~100 mmHg systolic;
   a basketball ~8 psi gauge.)

6. Identify which assumption (incompressible, static, no
   temperature gradient) is most likely to bite.

7. One sentence on how this connects to Chapter 15 (fluid
   dynamics) — when fluid moves, pressure becomes part of an
   energy budget along with kinetic energy and elevation.

Save the output as logbook/chapter-14-fluid-statics.md.
```

### What this produces

A fourteenth Logbook entry: a fluid-statics analysis of one element in your phenomenon, often surprising in the magnitudes.

### How to adapt this prompt

- *For phenomena with no obvious fluid* (a basketball shot in air): the air around the ball is a fluid; air pressure changes with altitude can be relevant.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have pressure-time data from a sensor, paste it for analysis.

### Connection to previous chapters

Builds on Chapter 6 (force, here as pressure × area), Chapter 9 (energy in hydraulic systems), Chapter 12 (statics — fluid statics is a special case of static equilibrium).

### Preview of next chapter

Chapter 15 takes fluids into motion. Bernoulli's principle relates fluid speed to pressure along a streamline: $P + \rho g h + \tfrac{1}{2}\rho v^2 = \text{constant}$. The continuity equation describes how flow speed changes with pipe cross-section. Together they predict everything from Venturi meters to airplane lift to blood flow through arteries.

---

## AI Wayback Machine

**Blaise Pascal** worked out fluid pressure in the 1640s — including the principle that any pressure applied to an enclosed fluid is transmitted undiminished throughout. Modern hydraulic systems are still applications of Pascal's principle.

**Run this:**

```
Who was Blaise Pascal, and how does Pascal's principle connect to
the fluid statics we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about his
career or ideas.
```

→ Search **"Blaise Pascal"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a hydraulic press multiplies force using Pascal's principle.
- Ask it about Pascal's parallel career inventing the first calculating machine and pioneering probability theory.

What changes? What gets better? What gets worse?
