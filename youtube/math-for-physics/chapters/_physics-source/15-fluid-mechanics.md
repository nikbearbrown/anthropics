# Fluid Mechanics: How Things Flow


## TL;DR

- TL;DR: Fluids (liquids and gases) exert pressure that increases with depth and creates buoyant forces that lift objects.
- The chapter moves through The Shape of Density, Concept 1: Pressure and Buoyancy—Why Things Float, The Mechanism: From Depth to Buoyant Force, Named Trade-Off: Incompressible Fluid Assumption, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

**TL;DR:** Fluids (liquids and gases) exert pressure that increases with depth and creates buoyant forces that lift objects. When fluids flow, energy conservation gives us Bernoulli's equation, which explains why moving fluids have lower pressure. Viscosity—internal friction—resists flow in real fluids, and Poiseuille's equation shows that a small change in pipe radius has enormous effects on flow rate.

---

## The Shape of Density

Dawn on a still morning, and a hot-air balloon crew is preparing for flight. The operator lights the burner—a pulse of propane flame. Inside the envelope, air temperature spikes to 100°C while the outside air stays at 15°C. You can see the math immediately: density is mass per unit volume, $\rho = m/V$. As the air inside heats, its molecules move faster and spread out. The same mass of air now occupies more space. The air inside becomes less dense than the surrounding atmosphere.

This difference in density is the entire story of buoyancy. The balloon envelope displaces a volume of outside air. That displaced air has weight. The upward force—the buoyant force—equals the weight of the fluid displaced. This is Archimedes' principle, stated in 212 BCE by a Greek mathematician who likely discovered it in a bathtub. The principle works because pressure increases with depth in any fluid, so the upward pressure force on the bottom of the balloon is greater than the downward pressure force on the top. The balloon rises.

**Learning objectives.** By the end of this chapter, you will:

- Calculate pressure at a given depth using hydrostatic equilibrium
- Apply Archimedes' principle to floating and submerged objects
- Use the continuity equation to relate flow velocity to cross-sectional area
- Derive Bernoulli's equation from energy conservation and use it to predict pressure changes in flowing fluids
- Calculate flow resistance using Poiseuille's law and explain why pipe radius matters so much
- Determine whether flow is laminar or turbulent using the Reynolds number

**Prerequisites:** Calculus I (derivatives, integrals), Newton's second law, work-energy theorem, conservation of mechanical energy.

---

## Concept 1: Pressure and Buoyancy—Why Things Float

### The Mechanism: From Depth to Buoyant Force

Let's start with the simplest fact: pressure is force per unit area, $p = F/A$. In a fluid at rest, this pressure acts perpendicular to any surface. A deeper point in a fluid experiences more pressure because the weight of fluid above it presses down.

Consider a thin horizontal layer of fluid at depth $h$ below the surface, with area $A$ and thickness $\Delta y$. The forces on this layer are:
- Downward: pressure from above, $p(y) \cdot A$
- Upward: pressure from below, $p(y + \Delta y) \cdot A$
- Downward: the layer's own weight, $\Delta m \cdot g = \rho A \Delta y \cdot g$

Since the layer is not accelerating (it's in equilibrium), these forces balance:

$$p(y + \Delta y) \cdot A = p(y) \cdot A + \rho A \Delta y \cdot g$$

Dividing by $A \Delta y$ and taking the limit as $\Delta y \to 0$:

$$\frac{dp}{dy} = \rho g$$

This differential equation says: as you go deeper (increasing $y$ downward), pressure increases proportionally to the density and gravitational acceleration. Integrating from the surface (where $p = p_0$) to depth $h$:

$$\int_{p_0}^{p} dp = \int_0^h \rho g \, dy$$

$$p - p_0 = \rho gh$$

$$p = p_0 + \rho gh$$

This is **hydrostatic pressure**. At the ocean floor 11 km deep, with seawater density $\rho \approx 1025 \, \text{kg/m}^3$:

$$p = 101,300 \, \text{Pa} + (1025)(9.81)(11,000) = 101,300 + 111,000,000 \approx 111 \, \text{MPa}$$

That's roughly 1,100 times atmospheric pressure. Life at that depth has walls thick enough to resist it.

Now, why do objects float? Imagine a sphere submerged in water. The pressure is higher on the bottom than on the top. The net result is an upward force—the buoyant force. To find its magnitude, consider what would happen if we removed the sphere and let fluid fill its place. That fluid would be in equilibrium, so the pressure forces on it would balance its weight. Therefore, the buoyant force equals the weight of the fluid displaced.

**Archimedes' principle:** The buoyant force on an object equals the weight of the fluid it displaces.

$$F_B = \rho_{fluid} V_{displaced} g$$

An object floats if $F_B > $ its weight. It sinks if $F_B < $ its weight. It stays suspended if $F_B = $ its weight.

The key insight: *density determines floating.* A ship is made of steel (density $\approx 7,850 \, \text{kg/m}^3$), which sinks. But shape the steel into a hull with a large volume—the average density of hull + air inside becomes less than water's density. The ship floats. Load the ship with cargo, increase the average density, and it sits deeper in the water but still floats. Fill the hold with water, make the average density equal to seawater's, and the ship becomes neutrally buoyant—exactly submerged.

### Named Trade-Off: Incompressible Fluid Assumption

We derived $p = p_0 + \rho gh$ by assuming density is constant with depth. For water, this works beautifully—an extremely large pressure is required to change water's volume. In the ocean, even at 11 km depth, seawater is compressed by only about 4.7%. For most problems, treating it as incompressible is fine.

But the atmosphere is compressible. Air density drops noticeably with height. At sea level, $\rho \approx 1.29 \, \text{kg/m}^3$. At 5 km altitude, it's roughly half. The hydrostatic formula $p = p_0 + \rho gh$ breaks down. Instead, pressure drops exponentially: $p(h) = p_0 \exp(-h/H)$, where $H$ is a scale height (about 8,800 m). This is why airplane cabins need pressurization—outside the cabin at cruise altitude (10-12 km), pressure is 10-25% of sea-level pressure.

### Worked Example: Mercury Barometer

Evangelista Torricelli invented the barometer in 1643 by filling a glass tube with mercury and inverting it into a pool of mercury. The mercury in the tube falls until its weight is balanced by atmospheric pressure pushing up from the pool.

At equilibrium, the pressure at the surface of the mercury pool equals the pressure at the bottom of the mercury column in the tube. The surface is at atmospheric pressure $p_0$. Inside the tube above the mercury is nearly a vacuum, so pressure there is roughly zero. The pressure at the base of the column is:

$$p_{base} = 0 + \rho_{Hg} g h = p_0$$

Solving for height:

$$h = \frac{p_0}{\rho_{Hg} g}$$

Mercury has density 13,600 kg/m³. At sea level:

$$h = \frac{101,300}{(13,600)(9.81)} = 0.760 \, \text{m} = 760 \, \text{mm}$$

This is why barometric pressure is often quoted as "760 mm of mercury" or "760 mm Hg." The number is just a rearrangement of the hydrostatic formula.

Water, being 13.6 times less dense than mercury, would require a column 13.6 times taller—about 10.3 meters. No wonder mercury is used: a portable barometer with a 10-meter tube is impractical.

### Common Misconceptions

**Misconception 1:** "Pressure at a depth depends on the shape of the container." 

This is false. Pressure depends only on depth, not on the area or shape of the container. A tall, narrow tube 1 meter deep has the same pressure at the bottom as a wide tank 1 meter deep. Pressure is local—it depends only on the height of fluid above. This is why water seeks the same level in containers of different shapes connected at the bottom.

**Misconception 2:** "Objects at greater depth are pushed down harder by pressure."

True, pressure increases with depth, but that increased pressure acts in all directions equally. An object at depth feels pressure pushing down from above, but also pushing up from below, pushing sideways from the sides. The *net* force is the difference—which is upward if the object is less dense than the fluid. Pressure alone doesn't push things down; only the *difference* in pressure creates a net force.

---

## Concept 2: Fluid Dynamics—Bernoulli and the Continuity Equation

### The Mechanism: Energy Conservation in Moving Fluids

Imagine water flowing through a pipe that narrows. What happens to the speed? By mass conservation (the continuity equation), the same volume of water must flow past any cross-section per unit time. If the pipe narrows, area decreases, so velocity must increase to maintain the same flow rate.

$$Q = A_1 v_1 = A_2 v_2$$

If $A_2 < A_1$, then $v_2 > v_1$.

Now, where does the extra kinetic energy come from? From the work done by pressure. In the wider section, fluid upstream pushes on the fluid ahead with a certain pressure. In the narrower section, the fluid is moving faster—it has more kinetic energy—so the pressure pushing it along must be higher. Wait: shouldn't higher speed require higher pressure to push the fluid? No. Here's the subtlety: in the narrow section, the pressure is *lower*, not higher. The work is done *by* the pressure difference, not against it.

Let's derive Bernoulli's equation from energy conservation. Consider a small element of fluid flowing through a pipe of varying diameter and height. At location 1, the element has:
- Pressure: $p_1$
- Velocity: $v_1$
- Height: $h_1$

At location 2:
- Pressure: $p_2$
- Velocity: $v_2$
- Height: $h_2$

The work done on the fluid element by pressure forces is:

$$W_{pressure} = (p_1 - p_2) \Delta V$$

where $\Delta V$ is a volume of fluid passing through. By the work-energy theorem, this work equals the change in kinetic energy plus the work against gravity (change in potential energy):

$$p_1 \Delta V - p_2 \Delta V = \frac{1}{2}(\rho \Delta V)(v_2^2 - v_1^2) + \rho g \Delta V (h_2 - h_1)$$

Dividing by $\Delta V$:

$$p_1 - p_2 = \frac{1}{2}\rho(v_2^2 - v_1^2) + \rho g(h_2 - h_1)$$

Rearranging:

$$p_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = p_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

This is **Bernoulli's equation**. Along a streamline (the path of a fluid element), the sum of pressure, kinetic energy per unit volume, and gravitational potential energy per unit volume is constant:

$$p + \frac{1}{2}\rho v^2 + \rho g h = \text{constant}$$

The three terms have physical meaning:
- $p$: the pressure energy available to do work
- $\frac{1}{2}\rho v^2$: kinetic energy per unit volume
- $\rho g h$: gravitational potential energy per unit volume

Their sum is constant for an incompressible, frictionless fluid along a streamline. This is purely energy conservation. The derivation required no empirical assumptions—only Newton's laws and calculus.

### A Critical Implication: Fast Flow, Low Pressure

From Bernoulli's equation at constant height ($h_1 = h_2$):

$$p_1 + \frac{1}{2}\rho v_1^2 = p_2 + \frac{1}{2}\rho v_2^2$$

Rearranging:

$$p_1 - p_2 = \frac{1}{2}\rho(v_2^2 - v_1^2)$$

If $v_2 > v_1$ (fast flow), then the right side is positive, so $p_1 > p_2$. The faster-moving fluid has *lower* pressure. This is **Bernoulli's principle**, and it contradicts intuition for many people. You might expect that fast-moving fluid would have high pressure. In fact, the opposite is true—fast flow is accompanied by low pressure.

This has practical consequences:
- A shower curtain bulges inward when the shower is on because the fast-moving water and air create low pressure inside the stall, and atmospheric pressure pushes the curtain inward.
- Two cars passing on the highway are drawn toward each other because the high-speed air between them has low pressure.
- An airplane wing works because the curved top surface forces air to move faster than the flat bottom. The lower pressure on top creates a lift force.

### Worked Example: Water Pressure in a Hose

A garden hose (radius 0.9 cm) with a nozzle (radius 0.25 cm) carries water at 0.5 L/s. The water emerges from the nozzle at atmospheric pressure (1.01 × 10⁵ Pa). What is the pressure in the hose?

First, find velocities using $Q = Av$:

In the hose: $v_1 = \frac{Q}{A_1} = \frac{0.5 \times 10^{-3}}{π(0.009)^2} = 1.96 \, \text{m/s}$

In the nozzle: $v_2 = \frac{Q}{A_2} = \frac{0.5 \times 10^{-3}}{π(0.0025)^2} = 25.5 \, \text{m/s}$

Assuming horizontal flow (constant height), Bernoulli's principle gives:

$$p_1 = p_2 + \frac{1}{2}\rho(v_2^2 - v_1^2)$$

$$p_1 = 1.01 \times 10^5 + \frac{1}{2}(1000)[(25.5)^2 - (1.96)^2]$$

$$p_1 = 1.01 \times 10^5 + 500(650 - 3.8)$$

$$p_1 = 1.01 \times 10^5 + 323,100 = 4.24 \times 10^5 \, \text{Pa}$$

The pressure in the hose is 4.24 times atmospheric. This pressure difference—the pumping pressure—is what forces the water through and accelerates it in the nozzle. The faster the water moves, the lower the pressure in the high-speed region. This is pure Bernoulli.

### Common Misconceptions

**Misconception 1:** "Higher speed means higher pressure in a fluid."

False. Bernoulli's equation shows the opposite: when a fluid accelerates (speed increases), pressure decreases, not increases. The pressure drop is what *enables* the acceleration. This is often counterintuitive because we confuse the force that causes acceleration (which can be large) with the pressure in the moving region (which is actually low).

**Misconception 2:** "Bernoulli's equation predicts that any moving fluid has zero pressure."

False. Bernoulli's equation says the *sum* $p + \frac{1}{2}\rho v^2 + \rho g h$ is constant. A fast-moving fluid can have low pressure, but the kinetic energy term is large. A slow-moving fluid can have high pressure. The sum is what's conserved, not the pressure alone.

---

## Concept 3: Real Fluids—Viscosity and Poiseuille's Law

### The Mechanism: Friction Inside Fluids

Pour juice. It flows freely. Pour maple syrup. It clings to the pitcher and flows slowly. The difference is viscosity—the internal friction of the fluid.

At the molecular level, as one layer of fluid moves relative to another, collisions between molecules resist the relative motion. Viscosity measures this resistance. Formally, for a fluid between two parallel plates where the top plate moves at velocity $v$ and the bottom is stationary, with the plates separated by distance $L$, the force required to maintain motion is:

$$F = \eta A \frac{v}{L}$$

where $\eta$ is the **coefficient of viscosity**, with SI units Pa·s (pascal-seconds) or N·s/m².

Rearranging:

$$\eta = \frac{FL}{Av}$$

This is the definition of viscosity from experimental observation.

Viscosity varies dramatically across fluids. At 20°C:
- Air: 0.0181 mPa·s
- Water: 1.002 mPa·s (about 55 times more viscous than air)
- Whole blood: 3.015 mPa·s (3 times more viscous than water)
- Olive oil: 138 mPa·s
- Honey: 2,000–10,000 mPa·s

Notice that gases have tiny viscosity; liquids are much thicker. And viscosity depends strongly on temperature. For water, viscosity at body temperature (37°C) is 0.6947 mPa·s—noticeably less than at 20°C. This is why honey pours faster when warm.

When a real fluid flows through a pipe, viscosity causes resistance. The flow is no longer uniform; the fluid moves fastest at the center and slower near the walls (where friction with the pipe surface slows it). This is **laminar flow with no-slip boundary conditions**: the layer of fluid touching the wall has zero velocity relative to the wall.

For laminar flow through a tube of radius $r$ and length $L$ with a pressure difference $\Delta p = p_1 - p_2$, the resistance to flow is:

$$R = \frac{8\eta L}{\pi r^4}$$

This is **Poiseuille's law for resistance**, named after Jean-Louis Poiseuille (1799–1869), a French physician who studied blood flow. The flow rate is:

$$Q = \frac{\Delta p}{R} = \frac{(p_1 - p_2)\pi r^4}{8\eta L}$$

### The $r^4$ Scaling: A Trade-Off

Notice the $r^4$ term. The flow rate depends on the *fourth power* of the radius. This has enormous consequences:

- Double the radius: flow rate increases by $2^4 = 16$ times.
- Halve the radius: flow rate decreases by a factor of 16.

This scaling explains why clogged arteries are dangerous. A coronary artery stenosis (narrowing) that reduces the radius by half cuts flow to one-sixteenth. A slight narrowing appears minor but has severe effects. Conversely, a small increase in artery diameter (say, through exercise-induced vascular remodeling) dramatically improves flow.

The formula $Q = \frac{\Delta p \pi r^4}{8\eta L}$ also shows why:
- Longer tubes have more resistance (proportional to $L$).
- More viscous fluids flow more slowly (proportional to $1/\eta$).
- Higher pressure difference drives more flow (proportional to $\Delta p$).

But the radius dominates everything. This is the clever—and beautiful—part: the tube geometry has far more control over flow than any other factor.

### Worked Example: Blood Flow in a Narrowed Artery

A normal coronary artery has radius 2 mm. A stenosis narrows it to 1.5 mm. The pressure drop across the artery is 5 mmHg = 666 Pa. Blood viscosity at body temperature is about 2.5 mPa·s, and the artery length is 10 cm. What is the flow rate in each case?

**Normal artery:**

$$Q_1 = \frac{(666)\pi(0.002)^4}{8(0.0025)(0.1)} = \frac{666 \times π \times 1.6 \times 10^{-11}}{0.002}$$

$$Q_1 = \frac{3.35 \times 10^{-8}}{0.002} = 1.68 \times 10^{-5} \, \text{m}^3\text{/s} = 1.68 \, \text{mL/s}$$

**Stenosed artery (radius 1.5 mm):**

$$Q_2 = \frac{(666)\pi(0.0015)^4}{8(0.0025)(0.1)} = \frac{666 \times π \times 5.06 \times 10^{-12}}{0.002}$$

$$Q_2 = \frac{1.06 \times 10^{-8}}{0.002} = 5.3 \times 10^{-6} \, \text{m}^3\text{/s} = 0.53 \, \text{mL/s}$$

The ratio is:

$$\frac{Q_2}{Q_1} = \frac{(1.5)^4}{(2.0)^4} = \frac{5.06}{16} = 0.316$$

A 25% reduction in radius cuts flow to 31.6%—less than one-third. The narrowed artery cannot supply adequate oxygen to heart muscle, causing angina. This is why drug-eluting stents (which prop open the artery) or bypass surgery (which reroutes blood) can be lifesaving.

### Laminar vs. Turbulent: The Reynolds Number

When does laminar flow break down into chaotic turbulence? The answer depends on a dimensionless number, the **Reynolds number**:

$$Re = \frac{\rho v D}{\eta}$$

where $\rho$ is density, $v$ is average velocity, $D$ is the pipe diameter, and $\eta$ is viscosity. The Reynolds number compares the strength of inertial forces (which resist changes in motion) to viscous forces (which cause friction).

- Low $Re$ (< 2,300 for pipe flow): viscous forces dominate, flow is smooth and laminar.
- High $Re$ (> 4,000): inertial forces dominate, flow is turbulent and chaotic.
- In between: transition zone, either laminar or turbulent depending on disturbances.

In the coronary artery example above, at 1.68 mL/s with an artery diameter of 4 mm and blood viscosity of 2.5 mPa·s:

$$v = \frac{Q}{A} = \frac{1.68 \times 10^{-6}}{π(0.002)^2} = 0.133 \, \text{m/s}$$

$$Re = \frac{(1050)(0.133)(0.004)}{0.0025} = 224$$

Blood flow in arteries is always laminar (low Reynolds number) because the vessels are small and blood is viscous. Turbulence appears only in severely narrowed vessels or at junctions where flow separates. In a large river or the ocean, Reynolds numbers are enormous, and flow is turbulent.

### Common Misconceptions

**Misconception 1:** "Viscosity is just thickness; thicker fluids are always more viscous."

Viscosity and thickness are different. Viscosity is resistance to flow per unit of velocity gradient. A thick fluid like honey is viscous. But some thick fluids (like very cold tar) can have different viscosity than you'd predict from appearance alone. Viscosity is defined precisely by the equation $F = \eta A(v/L)$, not by whether a fluid "looks thick."

**Misconception 2:** "Poiseuille's $r^4$ law means small pipes always have low flow."

Only in laminar flow. If the pipe is very narrow and the fluid very viscous, flow is laminar and Poiseuille's law applies. But in a turbulent system, other factors dominate. Also, the $r^4$ relationship assumes the pipe is smooth and the flow is steady—both assumptions that can fail in real organs and devices.

---

## Integration: How These Three Concepts Connect

Pressure, buoyancy, and flowing fluids are three faces of the same physics:

1. **Static fluids**: Pressure increases with depth ($p = p_0 + \rho gh$). Objects float or sink based on density. Buoyant force = weight of displaced fluid.

2. **Ideal (frictionless) flowing fluids**: Energy is conserved along a streamline. Bernoulli's equation ($p + \frac{1}{2}\rho v^2 + \rho gh = \text{const}$) shows that when fluid accelerates, pressure drops. This explains lift on aircraft wings, the behavior of shower curtains, and why narrowing a hose increases water speed.

3. **Real flowing fluids**: Viscosity resists flow. Poiseuille's law ($Q = \frac{\Delta p \pi r^4}{8\eta L}$) shows that small changes in vessel diameter have enormous effects on flow. This is critical in blood flow, water transport, and industrial fluid systems.

These are not separate topics. A hot-air balloon rises because of density and buoyancy (concept 1). Water flows through a narrowing nozzle faster due to energy conservation (concept 2). Blood pressure must overcome viscous resistance in capillaries (concept 3).

---

## Graduated Exercises

**Warm-up (conceptual, no calculation needed):**

1. Why does a balloon rise when you heat the air inside it? What would happen if you heated it only to body temperature (37°C) instead of 100°C?

2. Explain why a shower curtain bulges inward when you turn on hot water. Which concept (pressure, buoyancy, or viscosity) is most relevant?

3. Mercury barometers are fragile. Water-filled ones would be much taller (about 10 meters instead of 0.76 meters). Why isn't water used instead of mercury?

**Application (calculate a result):**

4. A scuba tank gauge reads 200 psi gauge pressure. (a) What is the absolute pressure in the tank? (Atmospheric pressure is 14.7 psi.) (b) At what depth in freshwater would you experience the same absolute pressure?

5. A fire hose (inside diameter 5 cm) carries water at 50 L/s. (a) What is the water velocity in the hose? (b) If the hose is connected to a nozzle (inside diameter 1 cm), what is the velocity in the nozzle? (c) Assuming level, frictionless flow and atmospheric pressure at the nozzle exit, what is the gauge pressure in the hose?

**Synthesis (combine concepts):**

6. A pipe carries oil (viscosity 0.1 Pa·s, density 850 kg/m³) at a flow rate of 10 liters per minute. The pipe has radius 1 cm and is 50 meters long. (a) Using Poiseuille's law, calculate the pressure drop due to viscosity. (b) Calculate the Reynolds number. Is the flow laminar?

7. A cylindrical water tank (radius 2 m) has a small hole (radius 2 cm) at the bottom. The tank is filled to a height of 5 meters. (a) Using Bernoulli's equation, estimate the velocity of water exiting the hole. (Hint: assume the velocity at the top surface is negligibly small.) (b) Calculate the volume flow rate. (c) Roughly how long would it take to empty the tank? (This is simplified; in reality, viscosity slows the flow.)

**Challenge (apply broadly):**

8. A stenosed artery has its radius reduced to 70% of normal. Assuming the pressure drop across the artery remains constant and the flow is laminar, by what factor does the volumetric flow rate decrease? Explain why even small arterial narrowing is clinically significant.

9. An airplane wing is designed so that air moves 1.5 times faster over the upper surface than the lower surface. Both surfaces are at the same height. Using Bernoulli's principle, estimate the pressure difference between upper and lower surfaces. (Air density is about 1.2 kg/m³; use an average velocity of 100 m/s in the formula.) Why would increasing the airspeed further be dangerous to the aircraft structure?

---

## Summary

Fluid mechanics rests on three pillars:

**Pressure and buoyancy** arise from the fact that pressure increases with depth in a static fluid. The hydrostatic formula $p = p_0 + \rho gh$ describes this. Archimedes' principle—buoyant force equals the weight of displaced fluid—explains floating and sinking. Objects float if their average density is less than the fluid's density.

**Bernoulli's equation** is energy conservation for moving fluids. Along a streamline, $p + \frac{1}{2}\rho v^2 + \rho gh = \text{constant}$. This shows that moving fluids have lower pressure than stationary ones, explaining lift on aircraft, the drawing-together of fast vehicles, and the behavior of jets and nozzles.

**Viscosity and Poiseuille's law** describe real fluids. Resistance to laminar flow is $R = \frac{8\eta L}{\pi r^4}$, giving flow rate $Q = \frac{\Delta p \pi r^4}{8\eta L}$. The fourth-power dependence on radius means small changes in vessel diameter have enormous effects on flow. The Reynolds number determines whether flow is laminar or turbulent.

The three concepts are linked: buoyancy explains why fluids move (density differences), Bernoulli explains *how* they move (energy conservation), and viscosity explains what *resists* their motion (internal friction). Together, they account for nearly all practical fluid behavior—from blood circulation to weather systems to aircraft performance.

---

## What Would Change My Mind

If an experiment showed that Archimedes' principle—buoyant force equals weight of displaced fluid—fails for objects of very small size or in non-Newtonian fluids, the chapter's foundation would need revision. So far, all evidence supports it.

## Still Puzzling

The precise mechanism of lift on aircraft wings remains subtle. Bernoulli's equation captures part of it, but the full story involves circulation (vorticity) and the Kutta-Joukowski theorem. Why circulation arises from the interaction of air and a curved airfoil shape is elegant but not yet explained in this chapter.

---

**Tags:** #fluid-mechanics #pressure #buoyancy #Bernoulli #Poiseuille #viscosity #laminar-flow #continuity-equation #energy-conservation #Archimedes

**Author:** Nik Bear Brown

**Byline:** This chapter represents my current reading of the physics of fluids, written for students who want to see the derivations and understand where the results come from. The machinery matters more than the names. The method is honest about what we understand and what still puzzles us.


---

## LLM Exercise — Chapter 15: Bernoulli, Buoyancy, and Pipes

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A Bernoulli-equation verifier for incompressible flow, buoyancy calculations, and a Poiseuille-flow pipe simulator.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 15 task in the physics-simulation-toolkit. The chapter
covered fluid statics (pressure, buoyancy) and fluid dynamics
(continuity, Bernoulli, viscosity). Build the implementations and
verify on canonical engineering cases.

In `chapters/ch15_fluids/`:

1. `simulations.py`:
   - `pressure_at_depth(depth, fluid_density, atmospheric_pressure)` —
     $P = P_0 + \rho g h$.
   - `buoyancy_force(submerged_volume, fluid_density)` —
     Archimedes: $F_B = \rho V g$.
   - `continuity(area1, velocity1, area2)` — $A_1 v_1 = A_2 v_2$
     for incompressible flow.
   - `bernoulli(p1, v1, h1, p2, v2, h2, rho)` — verifies
     $P + \frac{1}{2}\rho v^2 + \rho g h = \text{const}$ along a
     streamline.
   - `reynolds_number(rho, v, L, mu)` — $Re = \rho v L / \mu$.
   - `poiseuille_flow(pressure_drop, radius, length, viscosity)` —
     volumetric flow rate $Q = \pi r^4 \Delta P / (8 \mu L)$.
   - `venturi(area1, area2, p1, p2, rho)` — solve for v1, v2 given
     pressures and areas.

2. `test_simulations.py`:
   - Submerged object: a sphere of density 2700 kg/m³ (aluminum)
     placed in water (1000 kg/m³). It sinks; verify the buoyancy
     force is $\rho_{\text{water}} V g$.
   - Floating object: a sphere of density 800 kg/m³ (oak) in water.
     It floats; verify the fraction submerged is $\rho_{\text{oak}} /
     \rho_{\text{water}} = 0.8$.
   - Venturi: air flowing through a pipe that narrows from 10 cm to
     5 cm. By continuity, velocity quadruples in the narrow section.
     By Bernoulli, the pressure drops. Verify the pressure drop
     against the analytical formula.
   - Poiseuille: water flowing through a 1-meter pipe of 1 cm
     diameter under 1 kPa pressure drop. Compute Q. Verify Reynolds
     number to confirm laminar flow regime (Re < 2300).

3. `benchmarks.py` — for a fixed pressure drop, sweep pipe diameters
   and plot flow rate vs. diameter. The $r^4$ scaling should be
   empirically dramatic — doubling diameter increases flow by 16x.
   This is why blood-vessel narrowing matters so much in medicine.

4. `README.md` — decision cards. "Surprising findings": the
   $r^4$ scaling of Poiseuille flow; quantify the flow drop when a
   blood vessel narrows by 20%.

Commit as `ch15: fluid statics and dynamics with Bernoulli and
Poiseuille`.
```

**What this produces:** Bernoulli, buoyancy, continuity, and Poiseuille-flow implementations with engineering-relevant tests. The Poiseuille $r^4$ scaling is the medical and engineering payoff.

**How to adapt this prompt:**

- *For your own project:* CFD (computational fluid dynamics) is a much larger world — Navier-Stokes solvers, turbulence models. This exercise sticks to integrable analytical cases.
- *For ChatGPT / Gemini:* Both work. The Reynolds-number boundary between laminar and turbulent is the standard heuristic; mention the transition is not sharp.
- *For Claude Code:* Native fit. Plot the flow-rate-vs-diameter scaling.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 2 units, Ch 8 energy conservation (Bernoulli is energy conservation per unit volume).

**Preview of next chapter:** Chapter 17 implements simple harmonic motion — the differential equation solved analytically and numerically, with damping and resonance from a driven oscillator.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Marie Tharp** was the first comprehensive maps of the Atlantic Ocean floor (1957) and the global ocean floor (1977) — produced from sonar bathymetry traces while she was barred from going to sea — which revealed the Mid-Atlantic Ridge with its central rift valley and provided the visual evidence that convinced geologists of plate tectonics — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Marie Tharp, and how does their work on ocean-floor bathymetry, the Mid-Atlantic Ridge, and the case for plate tectonics connect to fluid mechanics applied to oceanography and the dynamics of the planet's largest fluid system? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Marie Tharp"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe Tharp's specific 1953 discovery of the rift valley running down the center of the Mid-Atlantic Ridge — what made her see it in the bathymetric data when others didn't, and what objections her co-worker Bruce Heezen raised before being convinced
- Ask: "Tharp's name was left off many of her own maps for decades. The 1977 *World Ocean Floor Panorama* finally credited both her and Heezen. What changed institutionally between 1957 and 1977 that allowed the credit, and what didn't change?"
- Add the constraint: "Answer using one specific bathymetric feature Tharp identified and what its discovery contributed to the eventual plate-tectonics synthesis"

What changes? What gets better? What gets worse?
