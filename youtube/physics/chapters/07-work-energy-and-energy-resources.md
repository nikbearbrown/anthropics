# Chapter 7 — Work, Energy, and Energy Resources

*The number that stays the same while everything else changes.*

---

Forty miles outside the city, on a wooded hillside, there is a lake that doesn't belong there. It sits halfway up the ridge, behind a concrete dam, connected by pipes to a lower lake at the foot of the hill. At two in the morning, when the city is asleep and electricity is cheap, pumps run for hours pushing water from the lower lake up to the upper one. By dawn, the upper reservoir is full.

At five in the evening, when everyone gets home and turns on their appliances and the grid starts straining, valves open. Water falls back down through the pipes, spins turbines, and generates electricity that goes back onto the grid. By midnight, the upper reservoir is empty again.

![Cross-section of a pumped-storage plant: upper reservoir at altitude, lower reservoir, penstock with reversible turbine-pump, transformer. Off-peak: motor pumps water up (PE gain). On-peak: water falls through turbine,...](../images/07-work-energy-and-energy-resources-fig-01.png)
*Figure 7.1 — Pumped-Storage Hydroelectric — A Gravitational Battery*

![Sankey energy flow diagram. Grid electricity input 4.61 TJ. Charging losses 0.46 TJ (pump motor 10%). Stored as gravitational PE 4.15 TJ. Discharge losses 0.62 TJ (turbine + generator 15%). Useful output 3.53 TJ. Roundtrip...](../images/07-work-energy-and-energy-resources-fig-06.png)
*Figure 7.6 — Pumped-Storage Roundtrip — 4.61 TJ In, 3.53 TJ Out, 77% Efficient*

This is a pumped-storage hydroelectric plant. It is, in every physical sense, a battery. But instead of storing energy as a chemical potential, it stores energy gravitationally — lifted water has more potential energy than water at the bottom of the hill. Letting the water fall back converts that potential energy to kinetic energy (fast water in a pipe), then to electrical energy (turbines driving generators). The roundtrip efficiency is about seventy-five percent. A quarter of the energy you pump up comes back as heat in the machinery, friction in the pipes, turbulence in the reservoirs. Conservation of energy doesn't say all the energy returns as electricity. It says all the energy goes *somewhere*. The quarter that doesn't come back as electricity ends up as low-grade heat, warming the surrounding rock and water by amounts too small to notice but precisely accountable.

I want to start here because this story contains everything this chapter is about. A concept — energy — that comes in many forms (gravitational, kinetic, electrical, thermal, chemical). A principle — that the total is always conserved. A tool — the work-energy theorem — for tracking how energy moves from form to form. And a connection to the practical economy of the world: power, efficiency, the cost of keeping the lights on.

The pumped-storage plant is physics at industrial scale. The physics is exactly the same as a ball falling off a table.

---

## Work: what it means to transfer energy

Carry a briefcase across a level office floor at constant velocity. You are exerting an upward force to support the briefcase against gravity. The briefcase moves forward. How much work do you do on the briefcase?

Zero.

This is the one place where physics and everyday language genuinely disagree, and the disagreement is worth taking seriously. The force you apply is upward. The displacement is horizontal. They are perpendicular. A force perpendicular to motion transfers no energy to the object — it merely redirects the object, or in this case just holds it up against gravity while it moves forward on its own.

Now carry the same briefcase up a flight of stairs. The force is upward; the displacement has an upward component. Work is done. Energy is transferred to the briefcase — specifically, gravitational potential energy increases.

The general formula is:

$$W = F d \cos\theta,$$

where $F$ is the magnitude of the (constant) force, $d$ is the distance the object moves, and $\theta$ is the angle between the force and the displacement. Three cases set the pattern: $\theta = 0°$ (force aligned with motion, full work), $\theta = 90°$ (force perpendicular to motion, zero work), $\theta = 180°$ (force opposing motion, negative work).

<!-- → [INFOGRAPHIC: three side-by-side diagrams showing the three canonical work cases — (1) force arrow parallel to displacement (θ = 0°, W = Fd labeled), (2) force arrow perpendicular to displacement (θ = 90°, W = 0 labeled, e.g. carrying briefcase horizontally), (3) force arrow antiparallel to displacement (θ = 180°, W = −Fd labeled, e.g. friction on sliding block) — student should see the angle geometry that determines the sign and magnitude of work] -->

Negative work removes energy from an object. Friction acting on a sliding crate does negative work on the crate — it takes kinetic energy away and dissipates it as heat. The formula is the same; the angle just happens to be $180°$.

Units: a newton times a meter is a joule. $1 \text{ N} \cdot \text{m} = 1 \text{ J}$.

### The work-energy theorem

The payoff for defining work this way is an exact relationship between work and motion. The *net* work done on an object — the sum of work by every force acting on it — equals the change in its kinetic energy:

$$W_{\text{net}} = \Delta KE = \tfrac{1}{2} m v_f^2 - \tfrac{1}{2} m v_i^2.$$

Kinetic energy is $KE = \tfrac{1}{2}mv^2$. A $1{,}500 \text{ kg}$ car at $30 \text{ m/s}$ has $KE = \tfrac{1}{2}(1500)(900) = 675{,}000 \text{ J}$. A $5 \text{ g}$ bullet at $400 \text{ m/s}$ has $KE = \tfrac{1}{2}(0.005)(160{,}000) = 400 \text{ J}$.

The derivation of the work-energy theorem is short: start with $F = ma$, multiply both sides by displacement $d$, and use the kinematic result $v_f^2 = v_i^2 + 2ad$ to replace $ad$ with $\tfrac{1}{2}(v_f^2 - v_i^2)$. The result is universal: whenever net work is done on an object, its kinetic energy changes by exactly that much — not approximately, exactly.

What the work-energy theorem buys you is a shift from vector bookkeeping to scalar bookkeeping. Newton's laws require you to track directions; the work-energy theorem gives you magnitudes directly. The cost is that you don't know in which direction the velocity ends up — only how fast. For problems where you need a speed but don't need a direction, the scalar accounting is faster and cleaner.

### Pushing a stalled car

You push a $1{,}500 \text{ kg}$ car along a level road with $400 \text{ N}$ over $20 \text{ m}$. Friction opposes the motion with $200 \text{ N}$. What is the car's final speed from rest?

![Three panels showing the work formula at different angles: (1) briefcase carried horizontally at constant height, θ=90°, W=0; (2) suitcase lifted up stairs, θ=0°, W=Fd; (3) sliding object with friction, friction opposite...](../images/07-work-energy-and-energy-resources-fig-02.png)
*Figure 7.2 — Work = F · d · cos θ — Three Cases by Geometry*

Work by your push: $(400)(20)\cos0° = 8{,}000 \text{ J}$.
Work by friction: $(200)(20)\cos180° = -4{,}000 \text{ J}$.
Work by gravity and normal force: zero (both perpendicular to motion).
Net work: $8{,}000 - 4{,}000 = 4{,}000 \text{ J}$.

Apply the theorem: $4{,}000 = \tfrac{1}{2}(1{,}500)v_f^2$, so $v_f = \sqrt{8{,}000/1{,}500} \approx 2.3 \text{ m/s}$.

Cross-check with Newton's second law: net force $= 200 \text{ N}$, acceleration $= 200/1{,}500 \approx 0.133 \text{ m/s}^2$. Kinematic equation $v^2 = 2ad = 2(0.133)(20) = 5.33$, $v = 2.31 \text{ m/s}$. Same answer. The two approaches have to agree — the work-energy theorem is derived from Newton's laws.

---

## Potential energy and conservation

![Roller coaster profile with three points: A (top, high PE, low KE), B (bottom, low PE, high KE), C (mid-height, middle of both). Stacked bar at each point shows KE blue and PE red summing to constant total mechanical energy...](../images/07-work-energy-and-energy-resources-fig-03.png)
*Figure 7.3 — Roller Coaster — KE Climbs Where PE Falls, Sum Stays Constant*

A roller coaster car sits at the top of a $40 \text{ m}$ hill, speed nearly zero. You want to know how fast it will be going at the bottom. You could track the slope angle at every point, compute the component of gravity along the track, integrate the forces. Or you could note that the car started with gravitational potential energy $mgh$ and zero kinetic energy, and will end with (approximately) zero potential energy and all of that as kinetic energy:

$$mgh = \tfrac{1}{2}mv^2 \implies v = \sqrt{2(9.8)(40)} \approx 28 \text{ m/s}.$$

About $100 \text{ km/h}$. One line. No need to know the shape of the track.

This shortcut works because gravity is a *conservative force* — one whose work depends only on the starting and ending heights, not on the path between them. Take any route from the top of the hill to the bottom, with no friction: gravity will have done the same amount of work. Because of this path-independence, we can define a **potential energy** — a number stored in the configuration of a system — such that the work done by the conservative force equals the *drop* in potential energy. Energy converted from potential to kinetic; total unchanged.

Gravitational potential energy near Earth's surface:

$$PE_g = mgh.$$

The reference height is arbitrary — only *changes* in $PE_g$ matter physically. Measure $h$ from the floor, the ground, the center of the Earth; the *change* $\Delta(mgh)$ when the object moves from one height to another is the same regardless.

Elastic potential energy stored in a spring compressed or stretched by $x$ from its natural length:

$$PE_s = \tfrac{1}{2}kx^2.$$

When only conservative forces act, the total mechanical energy is constant:

$$KE_i + PE_i = KE_f + PE_f.$$

This is conservation of mechanical energy. It is the most powerful shortcut in introductory mechanics, and it works whenever friction is absent (or negligible).

When friction is present, mechanical energy is not conserved — it decreases. But *total* energy is still conserved. Friction converts mechanical energy to thermal energy, which is just kinetic energy at the molecular scale. The work done by friction appears as an explicit term:

$$KE_i + PE_i + W_{\text{nc}} = KE_f + PE_f,$$

![Two side-by-side comparisons. Left: gravity (conservative) — moving an object along two different paths between same endpoints yields the same work. Right: friction (non-conservative) — work depends on path length, not just...](../images/07-work-energy-and-energy-resources-fig-04.png)
*Figure 7.4 — Conservative vs Non-Conservative — Does the Path Matter?*

where $W_{\text{nc}}$ is the work done by non-conservative forces (negative for friction, since friction always opposes motion).

<!-- → [CHART: energy bar chart for the roller coaster problem — two side-by-side bar diagrams, one at the top of the hill (tall PE bar, zero KE bar) and one at the bottom (zero PE bar, tall KE bar of equal height), with total energy marked by a horizontal line at the same level in both — illustrating conservation of mechanical energy as a constant total with changing distribution] -->

### A pendulum released from height

A $0.50 \text{ kg}$ pendulum bob is released from rest at $0.20 \text{ m}$ above its lowest point. What is its speed at the bottom?

Set $h = 0$ at the lowest point.

Initial: $PE_i = (0.50)(9.80)(0.20) = 0.98 \text{ J}$, $KE_i = 0$.
Final: $PE_f = 0$, $KE_f = \tfrac{1}{2}(0.50)v_f^2$.

Conservation: $0.98 = \tfrac{1}{2}(0.50)v_f^2$, so $v_f = \sqrt{2 \times 0.98 / 0.50} = \sqrt{3.92} \approx 1.98 \text{ m/s}$.

Notice the mass vanished. The speed at the bottom of a swing depends only on the height fallen, not on the bob's mass. A heavier bob and a lighter bob dropped from the same height swing through the bottom at the same speed. This is not an approximation; it is exact within the no-friction idealization.

The same mass-independence you know from free fall: in vacuum, a cannon ball and a feather fall at the same rate. Conservation of energy gives the same result by a different path.

---

## Power and efficiency: energy at a rate

Knowing the total energy in a system tells you nothing about how quickly it flows. The joule is a tiny unit at human scales — a lit match releases about $1{,}000 \text{ J}$, which sounds impressive until you realize that happens in about a second, and a second of a running car engine releases about $30{,}000 \text{ J}$. The *rate* matters. That rate is power:

$$P = \frac{W}{t} = \frac{\Delta E}{\Delta t}.$$

Units: joules per second, called watts. One watt is one joule per second.

Equivalently, for a force moving an object at constant velocity:

$$P = Fv\cos\theta.$$

Some power values worth internalizing:

![Logarithmic power ladder with labeled examples: 100 W (person at sustained work), 1 kW (microwave), 100 kW (car), 1 MW (locomotive), 100 MW (medium turbine), 1 GW (full nuclear plant). Each rung is a factor of 10.](../images/07-work-energy-and-energy-resources-fig-05.png)
*Figure 7.5 — Power — From a Lightbulb to a Nuclear Plant*

A resting human body dissipates about $100 \text{ W}$ as metabolic heat — just keeping warm and breathing. Walking briskly requires about $300 \text{ W}$. A serious athlete at full sprint puts out $1{,}000$–$2{,}000 \text{ W}$, briefly. A small car cruising at highway speed requires about $30{,}000 \text{ W}$ at the engine. A nuclear power plant outputs about $10^9 \text{ W}$. The ratio between a resting human and a nuclear power plant is about $10^7$ — seven orders of magnitude, covered by the same unit.

<!-- → [INFOGRAPHIC: logarithmic power scale from 10⁻² W to 10¹² W — labeled with recognizable reference points: resting human body (100 W), sprinting athlete (1,000 W), small car (30 kW), locomotive (4 MW), large nuclear plant (1,000 MW) — to give students visceral scale for what watts mean across the range of human experience] -->

**Efficiency** is the fraction of input energy that ends up doing useful work:

$$\eta = \frac{E_{\text{useful}}}{E_{\text{input}}}.$$

An incandescent bulb: about $5\%$ light, $95\%$ heat. A modern LED: about $40\%$ light. A car engine: about $25\%$ mechanical output. A coal-fired power plant: about $35\%$ electrical output. A human body converting food to mechanical work: roughly $20$–$25\%$.

These numbers are not engineering failures that clever design could eliminate. They are bounded above by thermodynamic limits — the second law of thermodynamics, which we will meet in Chapter 15, states that any conversion of heat to work is inherently less than $100\%$ efficient. Every real process dissipates *some* energy to heat. The question is always: how much, and is that acceptable?

### The human energy budget

A person eats $2{,}500 \text{ kcal}$ in a day. What average power does that represent?

Conversion: $1 \text{ kcal} = 4{,}184 \text{ J}$.

$$E = 2{,}500 \times 4{,}184 \approx 1.05 \times 10^7 \text{ J}.$$

Average power over $86{,}400$ seconds:

$$P = \frac{1.05 \times 10^7}{86{,}400} \approx 121 \text{ W}.$$

About $120 \text{ W}$ — slightly above the resting metabolic rate of $\sim 100 \text{ W}$, accounting for the energy of light daily activity. A person running a marathon expends roughly $2{,}500$–$3{,}000 \text{ kcal}$ in four hours, producing an average mechanical power of perhaps $400$–$500 \text{ W}$ — and a metabolic heat output that requires sweating at a liter per hour to stay cool.

The rule of thumb: the human body at rest runs at about the same power as a standard incandescent light bulb. At moderate exercise, it runs at three or four light bulbs. At peak athletic effort, it briefly runs at ten or more — which is why exercise rooms overheat and why marathons in warm weather are physiologically dangerous.

---

## Everything as one account

Pull back and look at what these three ideas make together.

Work is the mechanism of energy transfer. The work-energy theorem says that net work equals the change in kinetic energy — exactly, always, derivable from Newton's laws. Potential energy is a bookkeeping device that captures the work done by conservative forces in a convenient stored form, so you don't have to re-integrate every time you want to know a final speed. Conservation of mechanical energy is the consequence: when only conservative forces act, the total KE + PE is constant. Power is the rate at which the transfer happens, and efficiency is the fraction that ends up useful.

The universal claim underneath all of this is: energy is conserved. Completely. Always. In every form.

This claim is not derived from anything deeper in classical physics — it is, in some ways, the deepest thing classical physics says. Every apparent violation has turned out, on closer examination, to be a previously unrecognized form of energy. When radioactive nuclei were seen emitting electrons with a range of energies rather than a fixed one — violating energy conservation in every individual decay — Wolfgang Pauli proposed in 1930 that a hidden particle (which Fermi named the neutrino) was carrying away the missing energy. The neutrino was detected experimentally in 1956. The conservation law was not wrong; the bookkeeping was incomplete.

Feynman, in his Lectures, said that energy is a number we compute about a system that has the remarkable property of staying the same as the system evolves. We don't know what energy "is," in any deeper sense. We know the ledger balances. That is what physics has found: a number that never changes, even as every other number changes wildly.

Consider the pumped-storage plant we started with. Fill in the numbers. The upper reservoir holds $1.0 \times 10^9 \text{ kg}$ of water at an average height of $400 \text{ m}$:

$$PE = mgh = (10^9)(9.80)(400) = 3.92 \times 10^{12} \text{ J} = 3.92 \text{ TJ}.$$

Turbines at $90\%$ efficiency, discharging over four hours ($14{,}400 \text{ s}$):

$$P_{\text{out}} = \frac{0.90 \times 3.92 \times 10^{12}}{14{,}400} \approx 245 \text{ MW}.$$

Pumps at $85\%$ efficiency to fill the reservoir:

$$E_{\text{input}} = \frac{3.92 \times 10^{12}}{0.85} \approx 4.61 \text{ TJ}.$$

Roundtrip: $3.53$ TJ out for $4.61$ TJ in — about $77\%$ efficient. The $23\%$ that doesn't come back is heat in the machinery, turbulence in the water, electrical resistance in the generators. It went somewhere. It is still accounted for. The ledger balances.

<!-- → [INFOGRAPHIC: Sankey diagram for the pumped-storage cycle — wide input arrow (4.61 TJ, grid electricity in) splits into a thick "useful output" arrow (3.53 TJ, grid electricity out) and a narrower "losses" arrow (1.08 TJ, heat in pumps/pipes/turbines); student should see that total energy is conserved while useful fraction is 77%] -->

The same accounting covers the roller coaster falling forty meters, the pendulum swinging through its arc, the skydiver reaching terminal velocity (where all the gravitational potential energy is being continuously converted to thermal energy in the air — no net change in kinetic energy, but the conversion is still happening). The scale changes; the principle doesn't.

---

## Exercises

### Warm-up

**7.1** *(LO 1)* You push a $20 \text{ kg}$ box across a frictionless floor with a horizontal $50 \text{ N}$ force over $4.0 \text{ m}$. (a) How much work do you do? (b) What is the box's final kinetic energy if it started from rest? (c) What is its final speed?

**7.2** *(LO 1)* You carry a $5.0 \text{ kg}$ bag of groceries at constant velocity for $20 \text{ m}$ across a level parking lot, holding it with an upward force equal to its weight. How much work do you do on the bag? Explain why, even though you are exerting a force and covering a distance.

**7.3** *(LO 3)* A $0.50 \text{ kg}$ rock is held $3.0 \text{ m}$ above the ground. (a) What is its gravitational PE relative to the ground? (b) If released from rest, what is its speed just before hitting the ground? (Ignore air drag.)

**7.4** *(LO 5)* A $1{,}500 \text{ W}$ hair dryer runs for $10$ minutes. (a) How much energy does it use, in joules? (b) In kilowatt-hours? (c) At $\$0.15$ per kWh, what does it cost?

### Application

**7.5** *(LO 2, 3)* A $60 \text{ kg}$ skier starts from rest at the top of a slope $30 \text{ m}$ above the bottom. Ignoring friction and drag, what is her speed at the bottom? Would a $90 \text{ kg}$ skier reach the same speed? Explain.

**7.6** *(LO 2, 3, 4)* A $1{,}200 \text{ kg}$ car traveling at $20 \text{ m/s}$ skids to a stop on a level road. The kinetic friction coefficient is $\mu_k = 0.60$. (a) Compute the initial KE. (b) Use the work-energy theorem to find the stopping distance. (c) If the car had been traveling at $40 \text{ m/s}$ instead, how does the stopping distance change?

**7.7** *(LO 3)* A spring with $k = 200 \text{ N/m}$ is compressed by $0.10 \text{ m}$ and released, launching a $0.20 \text{ kg}$ ball horizontally on a frictionless surface. (a) What elastic PE is stored before release? (b) What is the ball's launch speed? (c) If the spring were compressed twice as far, how would the launch speed change?

**7.8** *(LO 5)* A car of mass $1{,}500 \text{ kg}$ climbs a $5\%$ grade ($\sin\theta \approx 0.05$) at a constant $20 \text{ m/s}$. (a) At what rate does the engine do work against gravity? (b) Convert this to horsepower ($1 \text{ hp} = 746 \text{ W}$). (c) If the car engine is $25\%$ efficient, at what rate is fuel energy being consumed?

### Synthesis

**7.9** *(LO 2, 3, 4)* A roller coaster car of mass $400 \text{ kg}$ starts from rest at the top of the first hill ($h = 50 \text{ m}$) and reaches the bottom at $25 \text{ m/s}$. (a) Compute the initial PE and final KE. (b) How much mechanical energy was lost to friction? (c) What average friction force acted over the $120 \text{ m}$ track length from top to bottom?

**7.10** *(LO 3, 5)* You climb a $20 \text{ m}$ flight of stairs in $30 \text{ s}$. Your mass is $70 \text{ kg}$. (a) How much work do you do against gravity? (b) What is your average mechanical power output in watts? (c) The human body is roughly $20\%$ efficient at converting food energy to mechanical work. How much metabolic energy did this climb require, in kilocalories?

**7.11** *(LO 1, 2, 3)* A $0.50 \text{ kg}$ ball is thrown straight up at $15 \text{ m/s}$ from ground level. Using energy conservation: (a) find the maximum height; (b) find the speed when the ball is at half that height; (c) find the speed when it returns to ground level. Does air resistance affect answer (c)?

### Challenge

**7.12** *(LO 3, 5, beyond chapter)* A pumped-storage plant lifts $3.0 \times 10^9 \text{ kg}$ of water through $250 \text{ m}$ of elevation. (a) What gravitational PE is stored? (b) The filling takes $8$ hours with pumps at $80\%$ efficiency — what input power is required? (c) The discharge takes $4$ hours with turbines at $90\%$ efficiency — what output power is delivered? (d) What roundtrip efficiency does this plant achieve?

**7.13** *(LO 2, 3, beyond chapter)* Estimate the kinetic energy of: (a) a $5.0 \text{ g}$ bullet at $400 \text{ m/s}$; (b) a $1{,}500 \text{ kg}$ car at $30 \text{ m/s}$; (c) a $70 \text{ kg}$ person walking at $1.4 \text{ m/s}$; (d) the Earth orbiting the Sun (mass $6 \times 10^{24} \text{ kg}$, orbital speed $3 \times 10^4 \text{ m/s}$). Compare these values in orders of magnitude and comment on which surprised you most.

---



By the end of this chapter you should be able to:

1. Compute the work done by a constant force at any angle to displacement: $W = Fd\cos\theta$, including the special cases $\theta = 0°$, $90°$, and $180°$.
2. Apply the work-energy theorem $W_{\text{net}} = \Delta KE$ to relate net work to changes in speed.
3. Compute gravitational potential energy ($PE_g = mgh$) and elastic potential energy ($PE_s = \tfrac{1}{2}kx^2$) and apply conservation of mechanical energy to problems where friction is negligible.
4. Apply the extended energy equation $KE_i + PE_i + W_{\text{nc}} = KE_f + PE_f$ to problems where friction or other non-conservative forces are present.
5. Compute power ($P = W/t = Fv$) and efficiency ($\eta = E_{\text{useful}}/E_{\text{input}}$) for real energy-conversion processes, and translate between joules, kilowatt-hours, and kilocalories.

**Prerequisites.** Chapter 4 (Newton's laws, $F = ma$). Chapter 5 (friction as a non-conservative force). Chapter 3 (vector decomposition, for the angle in $W = Fd\cos\theta$).

**Why this chapter matters.** Energy is the universal accounting tool of physics. Every later chapter — heat, thermodynamics, electricity, waves, nuclear physics — uses some form of energy conservation as its organizing principle. This chapter installs the language and the ledger. It also connects physics to the practical economy of the real world: power grids, metabolic rates, fuel efficiency, the cost of electricity.

---

## ↳ Dig Deeper — Work done by a variable force

*The formula $W = Fd\cos\theta$ assumes the force is constant. For a spring, a varying gravitational field, or any force that changes as the object moves, the work is the integral $W = \int F \, dx$ — the area under the force-vs-position graph.*

**Prompt:**
> Explain how to compute work done by a variable force using the integral $W = \int F(x) \, dx$, and interpret it as area under the $F$-vs-$x$ curve. Compute the work to stretch a spring with spring constant $k$ from its natural length to a stretch of $\Delta L$ — show that this gives $W = \tfrac{1}{2}k(\Delta L)^2$, which equals the elastic potential energy $PE_s$. End with one sentence on how this generalizes to non-constant forces in 3D.

**What to do with the output:** Save it. The integral form of work is the bridge to elastic potential energy and to all later energy calculations involving non-constant forces (electric fields, molecular potentials, gravitational fields at large distances).

---

## ↳ Dig Deeper — Why isn't friction conservative?

*Friction depends on path length, not just endpoints. Two paths between the same start and end points but with different lengths produce different amounts of friction work — which is the definition of non-conservative. The "lost" mechanical energy is not destroyed; it becomes thermal energy in the sliding surfaces.*

**Prompt:**
> Explain why friction is a non-conservative force, with a specific worked example: compare friction work for a block sliding directly across a $5 \text{ m}$ table versus sliding $10 \text{ m}$ along a zigzag path between the same two endpoints. Show that friction work differs. Then explain what physical process converts the "lost" mechanical energy to thermal energy. End with one sentence on whether total energy conservation is violated by friction.

**What to do with the output:** Save it. The conservative/non-conservative distinction is the bridge to the broader concept of total energy conservation including thermal forms, and to the second law of thermodynamics (Chapter 15).

---

## ↳ Dig Deeper — Energy resources and the global picture

*The world used roughly $6 \times 10^{20} \text{ J}$ of primary energy in 2024 — about $19 \text{ TW}$ continuous power. Of that, roughly $80\%$ comes from fossil fuels. The numbers, the mix, and the trends are decisive for economics and climate policy.*

**Prompt:**
> Walk me through the global energy budget for the most recent year you have data on. Break it down by source (oil, coal, natural gas, nuclear, hydro, wind, solar, biomass) in both percentage and absolute terms (TW or EJ/year). Then explain (a) which sources have grown fastest in the past decade, (b) which have shrunk, and (c) what the order-of-magnitude comparison is between human energy use and the solar power incident on Earth's surface. End with one sentence on what scaling factor renewable sources would need to cover all of human demand.

**What to do with the output:** Save it. Energy resources connect directly to the global economy, policy, and climate. This Dig Deeper keeps the coverage current in ways a fixed textbook cannot.

---

## LLM Exercise — Chapter 7: Energy Bookkeeping for Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An energy budget for one cycle of your anchor phenomenon, with input, useful output, and dissipated forms identified.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 7, I want to build an energy budget for one cycle or one event of my phenomenon. Please:

1. Identify ONE complete energy cycle or event in my phenomenon. Examples:
   - Bike commute: one full ride from home to work — chemical (food) → mechanical (legs) → kinetic (bike) → friction/drag (heat).
   - Coffee maker: one brew cycle — electrical → thermal (heating water) → kinetic (water through grounds) → thermal (final coffee).
   - Basketball shot: chemical (muscles) → kinetic (ball) → gravitational PE (peak of arc) → kinetic (descent) → thermal (rim/net friction).
   - Marathon: 4-hour race — chemical (food + reserves) → mechanical (forward motion) → thermal (heat dissipated by sweating, drag, ground friction).
   - Espresso: electrical (pump) → mechanical (pressure) → kinetic (water flow) → thermal (final extracted shot).

2. Estimate the input energy (in joules or kWh).

3. Estimate the useful output (the energy that did the thing you wanted: forward motion, heated coffee, brewed shot).

4. Estimate the dissipated energy (where it went — friction, drag, heat to surroundings).

5. Compute the efficiency (useful / input).

6. Apply conservation of energy as a check: do all the pieces add up to the input?

7. One sentence on how this connects to Chapter 8 (momentum) — energy conservation gives you speeds; momentum conservation gives you what gets transferred in collisions.

Save the output as logbook/chapter-07-energy.md.
```

### What this produces

A seventh Logbook entry: an energy budget for your phenomenon, often illuminating which steps are inefficient and which are not.

### How to adapt this prompt

- *For phenomena with mostly heat output:* efficiency is the question of what fraction of electrical input ends up doing the intended thing versus heating the surroundings.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have power data (a smart-meter reading, an electricity bill), paste it and let Claude compute energy and efficiency directly.

### Connection to previous chapters

Builds directly on Chapter 4 (force) — energy is what work transfers, and work is force times displacement. Friction (Chapter 5) is the principal mechanism of mechanical-to-thermal conversion. Chapter 6's circular motion is interesting here: at constant speed, gravity does no net work on a satellite over one orbit.

### Preview of next chapter

Chapter 8 introduces momentum — the other great conservation law of mechanics. Energy conservation gives you final speeds; momentum conservation governs what happens in collisions, when two objects exchange force over a brief time.

---

## What would change my mind

The chapter argues that conservation of energy is universal and exact. The argument would need revision if a careful experiment ever found energy appearing or disappearing without conversion to a known form. Historically, every apparent violation has resolved by discovering a previously unaccounted form of energy — the neutrino was hypothesized in 1930 to save energy conservation in radioactive beta decay; it was experimentally detected in 1956. The conservation law was not wrong. The ledger was incomplete. I expect the pattern to continue.

## Still puzzling

The deepest question this chapter raises and does not resolve: **what is energy?** We can compute it, conserve it, transform it, charge for it. But asking what energy *is* — whether it has substance, whether it is "real" in any deeper sense — turns out not to have an answer physics can give. Feynman put it plainly: "It is important to realize that in physics today, we have no knowledge of what energy *is*." The conservation law works whether or not you understand what is being conserved. That is both reassuring and, if you sit with it, quite strange.

---

## AI Wayback Machine

**James Prescott Joule** demonstrated in 1843 that mechanical work and heat are interconvertible at a fixed ratio — the mechanical equivalent of heat. The result killed the caloric theory of heat and unified energy as a single quantity that flows between forms.

**Run this:**

```
Who was James Prescott Joule, and how does the mechanical equivalent of heat connect to the work and energy we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Prescott Joule"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Joule's paddle-wheel experiment in detail — what was measured, how was the conversion quantified?
- Ask it about Joule's role as a brewer's son and how that practical work shaped his physics.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 8 (linear momentum) presents the other great conservation law, which governs collisions and impulse. Together with energy conservation, it forms the full accounting of classical mechanics. Chapter 9 (statics) treats structures in equilibrium, where the energy is constant because nothing moves. Chapter 10 (rotation) extends kinetic energy to rotating bodies: rotational $KE = \tfrac{1}{2}I\omega^2$, the same form with moment of inertia replacing mass and angular velocity replacing linear velocity. Chapters 14–15 (heat, thermodynamics) extend energy conservation to thermal forms and introduce the second law — total energy is conserved, but the *useful* fraction always shrinks in any real process. Chapter 21 (electricity) introduces electrical energy and power, and connects the physics of this chapter to the global energy economy.

---

**Tags:** energy, work, power, conservation, potential-energy
