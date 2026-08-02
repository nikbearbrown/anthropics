# Chapter 8 — Work and Kinetic Energy

## Three title options

1. **Energy in Motion — Why Force and Distance Together Tell a Story**
2. **Work and Speed — The Hidden Link Newton Missed at First**
3. **From Effort to Motion — The Line Integral That Changes Everything**

---

## TL;DR

Energy methods solve problems Newton's laws cannot easily handle. The work-energy theorem says that the net work on an object equals its change in kinetic energy — a statement so useful that it bypasses force, acceleration, and time altogether when you only care about speed at different points along a path.

---

## Chapter opening — The archer and the arc

You are drawing back a bow. At rest, the bow is straight — a stick of ash wood held together by a bowstring under mild tension. But as you pull, you feel resistance. The deeper you draw, the harder you pull. At full draw — 28 inches back in Olympic competition — you are working against the elastic stiffness of the limbs. Energy is flowing from your muscles into the bow's structure. You hold the bow drawn for a breath, and the bow holds that energy, stored.

Then you release.

The string snaps forward. The limbs accelerate from rest to peak velocity in milliseconds. The arrow catches that speed — a well-tuned arrow leaves a modern competition bow at roughly 90 meters per second. The kinetic energy at release is the energy you stored when you drew. You did not need to know the force at every point of the draw. You did not need to calculate the acceleration of each limb. You simply recognized that mechanical energy moved from your hand to the bow's limbs to the arrow's motion, and the equation $K = \frac{1}{2}mv^2$ tells you how much speed that energy became.

This is the economy of energy methods. When the forces are complicated or the path is curved or the force itself changes with position — when Newton's second law becomes a differential equation you do not want to solve — the machinery of work and kinetic energy gives you the final answer without the intermediate details.

This chapter teaches you three things. First: what work is, measured in line integrals along any path the object takes. Second: what kinetic energy is, and why $K = \frac{1}{2}mv^2$ emerges naturally from the definitions of work and force. Third: what power is — the rate at which work flows, measured in watts, the same unit a light bulb's rating comes in.

The theme running through all three is conservation. Work done on an object is never lost; it becomes kinetic energy. Power is work per unit time. Learning to see energy as a flowing, countable quantity will change how you read the physical world.

### Learning objectives

By the end of this chapter you will be able to:

- **Calculate** work done by constant and variable forces along curved paths using the line integral $W = \int \vec{F} \cdot d\vec{r}$, and recognize when work is positive, negative, or zero.
- **Derive** kinetic energy from the definition of work and Newton's second law, establishing that $K = \frac{1}{2}mv^2$ and that $W_{\text{net}} = \Delta K$.
- **Apply** the work-energy theorem to find unknown speeds or forces without explicitly solving for acceleration.
- **Distinguish** between work done *by* a force and work done *against* a force.
- **Calculate** power as both $P = \frac{dW}{dt}$ and $P = \vec{F} \cdot \vec{v}$, and relate power to energy transfer.

### Prerequisites

- Vectors: components, magnitude, dot product, and the geometric interpretation $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$.
- Calculus: definite integrals, the chain rule, and the chain of differentials.
- Newton's second law: $\vec{F} = m\frac{d\vec{v}}{dt}$.
- One-dimensional kinematics: the relationship between position $x(t)$, velocity $v(t) = \frac{dx}{dt}$, and acceleration $a(t) = \frac{dv}{dt}$.

### Why this chapter matters

Work and energy are not more fundamental than force and acceleration. Force comes first historically and logically. But energy methods solve problems that force methods leave intractable. A projectile following a curved path under gravity? Force gives you a differential equation. Energy gives you an answer. A block sliding down a frictionless surface of any shape? Force is helpless without knowing the normal force at every point. Energy does not care what the shape is. A car climbing a hill against wind resistance? Force makes you sum all the resistance forces separately. Energy collapses them into one number: how much power the engine supplies. When the forces are complicated or unknown, energy works.

---

## Concept 1 — Work as a line integral: $W = \int \vec{F} \cdot d\vec{r}$

### The scene: pushing a lawn mower

You are mowing your lawn. The mower is a simple machine: a frame with wheels, a blade underneath, and a handle at the back. You grip the handle and push. The handle makes an angle of 35 degrees below the horizontal. You apply a force of 75 newtons. The grass is level. You push the mower 25 meters to the far end of the yard.

How much work have you done?

In everyday English, work is effort, exhaustion, the feeling at the end of the day. In physics, work has a precise definition. Work is done when a force causes a displacement. But there is a catch: only the *component* of the force in the direction of the displacement does work.

You are pushing down and forward. The grass cannot move down — it stays at ground level. The grass moves forward. So only the forward component of your force — the component parallel to the displacement — does work.

The mathematics handles this with a dot product.

### The definition of infinitesimal work

The infinitesimal work done by a force $\vec{F}$ through an infinitesimal displacement $d\vec{r}$ is

$$dW = \vec{F} \cdot d\vec{r} = |\vec{F}| |d\vec{r}| \cos\theta$$

where $\theta$ is the angle between the force vector and the displacement vector. This is true regardless of whether the force is constant or varies with position.

The dot product captures what matters: if the force points in the same direction as the motion ($\theta = 0°$), then $\cos\theta = 1$ and $dW = |\vec{F}| |d\vec{r}|$ — maximum work. If the force is perpendicular to the motion ($\theta = 90°$), then $\cos\theta = 0$ and $dW = 0$ — no work. If the force opposes the motion ($\theta = 180°$), then $\cos\theta = -1$ and $dW < 0$ — the force removes energy.

### Work along a path: the line integral

For a displacement from point A to point B, the total work is the sum of all infinitesimal contributions:

$$W_{AB} = \int_{A}^{B} \vec{F} \cdot d\vec{r}$$

This is a *line integral* — an integral along the path the object follows, not just along the straight-line distance from A to B.

Here is the key insight: **for a constant force, the work depends only on the endpoints**, not on the path between them. If you push the mower 25 meters straight across the yard, or if you push it 20 meters in one direction and then 15 meters perpendicular (25 meters of total path length), the work done by gravity is the same either way. The reason is that for constant $\vec{F}$, you can factor it out of the integral:

$$W_{AB} = \vec{F} \cdot \int_{A}^{B} d\vec{r} = \vec{F} \cdot (\vec{r}_{B} - \vec{r}_{A})$$

The integral of displacement depends only on the endpoints. But **for a variable force** — one that changes direction or magnitude as the object moves — the path *does* matter. A spring force is a variable force. The work done by a spring depends on the path you take through its displacement because the force magnitude changes.

### The trade-off: line integrals versus forces

Energy methods sidestep the need to know the force at every point. If you are sliding down a frictionless hill of any shape, and you only care about your final speed, you do not need to know the normal force the hill exerts at every point. You only need the initial height and the final height — the endpoints of the path.

But energy methods lose information. When you calculate work, you get a number: joules of energy transferred. You do not get a vector. If you know the work a force did, you cannot immediately reconstruct the *direction* of motion. A 10-joule displacement could be upward, downward, or at any angle. Knowing the work does not tell you the velocity vector — only its magnitude, via the kinetic energy.

The calculus trade-off is also real. Calculating a line integral can be intricate when the force is complicated or the path is curved. A constant force is trivial. A variable force along a curved path may require parametrizing the path and evaluating an integral that has no closed form.

### Worked example — the lawn mower

You push a 25-kg lawn mower at a constant 35 degrees below the horizontal with a force of 75 newtons, moving it 25 meters across level ground. The mower travels in a straight line.

*What is the work done by you on the mower?*

The force is constant, so use $W = \vec{F} \cdot d = Fd\cos\theta$.

$W = (75 \text{ N})(25 \text{ m})\cos(35°) = 1875 \cos(35°) \approx 1875 \times 0.819 = 1536 \text{ J}$

This is roughly 1.5 kilojoules.

*What is the work done by gravity on the mower?*

Gravity pulls straight down. The mower moves horizontally. The angle between them is 90 degrees. $W_{\text{grav}} = (mg) \times 25 \times \cos(90°) = 0$.

Gravity does no work on the mower because the displacement has no vertical component. The normal force, which points perpendicular to the ground, also does no work — the mower does not move perpendicular to the ground.

*What is the work done by friction?*

The problem does not specify friction, so we assume it is negligible. If there were friction, it would oppose the motion, $\theta = 180°$, and do negative work.

*Sense-check:* 1.5 kilojoules is about the energy burned by one sixth of a gram of fat. Mowing a 25-meter strip is noticeable work, but not strenuous. The number passes the sniff test.

### Common misconceptions

**Work is not the same as effort.** You can apply a large force and do zero work if there is no displacement. Stand against a wall and push with all your might — zero displacement, zero work. You can do work with a small force: a feather falling from a roof, pulled down by gravity's tiny force, moves a large distance and does work on the air it passes through.

**Work can be negative.** When friction opposes motion, it does negative work. This does not mean friction is "adding energy backwards" — it means friction *removes* energy, and negative work is the sign language physicists use to record removal. A force that opposes motion always does negative work.

**The path matters when the force is variable.** For constant forces, path-independence is real and useful. But a spring force, an electric force, a drag force — these change as the object moves. The work can differ for different paths. Always check whether the problem specifies a path before assuming path-independence.

---

## Concept 2 — Kinetic energy and the work-energy theorem

### The scene: the pile driver

Imagine a construction site. A pile driver is a simple machine: a heavy hammer on top of a tall frame. The hammer is hoisted 5 meters above a wooden pile. Then it is released. It falls, accelerating under gravity, and strikes the pile with tremendous force. The kinetic energy at impact is what drives the pile into the ground.

How much kinetic energy does the hammer have just before it hits?

Gravity did work on the hammer during the fall. How much work? The force is gravity, the displacement is downward, and they align, so $W = mg \times h = (500 \text{ kg})(9.8 \text{ m/s}^2)(5 \text{ m}) = 24,500 \text{ joules}$.

That work must go somewhere. It becomes the hammer's motion — its kinetic energy.

### Deriving kinetic energy from Newton's second law

Start with the definition of work for a net force:

$$dW_{\text{net}} = \vec{F}_{\text{net}} \cdot d\vec{r}$$

Newton's second law gives $\vec{F}_{\text{net}} = m\frac{d\vec{v}}{dt}$. Substitute:

$$dW_{\text{net}} = m\frac{d\vec{v}}{dt} \cdot d\vec{r}$$

Here comes a clever algebraic move. Since $d\vec{r} = \vec{v} \, dt$, we can substitute:

$$dW_{\text{net}} = m\frac{d\vec{v}}{dt} \cdot (\vec{v} \, dt) = m \, d\vec{v} \cdot \vec{v}$$

The $dt$ cancels. Now integrate both sides from point A to point B:

$$W_{\text{net},AB} = \int_{A}^{B} m \, d\vec{v} \cdot \vec{v}$$

This integral looks strange. Use the vector calculus identity $\vec{v} \cdot d\vec{v} = \frac{1}{2} d(v^2)$ — the dot product of a vector with its own differential is half the differential of the squared magnitude. (If you are uncomfortable with this, work in Cartesian components: $v_x dv_x + v_y dv_y + v_z dv_z = \frac{1}{2} d(v_x^2 + v_y^2 + v_z^2) = \frac{1}{2} d(v^2)$.)

$$W_{\text{net},AB} = \int_{A}^{B} m \times \frac{1}{2} d(v^2) = \frac{1}{2}m \left[ v_B^2 - v_A^2 \right] = K_B - K_A$$

This defines kinetic energy:

$$K = \frac{1}{2}mv^2$$

And this is the **work-energy theorem**:

$$W_{\text{net}} = \Delta K = K_{\text{final}} - K_{\text{initial}}$$

The net work done on an object equals its change in kinetic energy. No acceleration needed. No time needed. No intermediate positions needed. Only the net work and the speeds at the start and end.

### Why this matters: a curved path

Imagine a marble rolling down a bumpy, curved track from height $h_1$ to height $h_2$. The normal force from the track is huge, but it is perpendicular to the motion at every point, so it does zero work. Friction at each point is complicated — the track texture varies. But gravity does work: $W_{\text{grav}} = -mg(h_2 - h_1) = mg(h_1 - h_2)$.

By the work-energy theorem:

$$\frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2 = mg(h_1 - h_2)$$

Solve for $v_2$:

$$v_2^2 = v_1^2 + 2g(h_1 - h_2)$$

This is the final answer. You do not need to integrate the normal force. You do not need the shape of the track. If you know the initial speed, the initial height, the final height, and gravity, you know the final speed. Energy methods hand you the problem's skeleton.

### The trade-off: direction versus magnitude

A force vector has magnitude and direction. The kinetic energy $K = \frac{1}{2}mv^2$ has only magnitude — it depends on the speed $v = |\vec{v}|$, not the direction of $\vec{v}$.

This is useful and limiting. Useful because speed is often all you care about: *How fast is the car going when it reaches the top of the hill?* You do not care whether it is heading north or northwest. Limiting because if you only know the kinetic energy, you cannot reconstruct the velocity vector. A 100-joule kinetic energy could be motion at 10 m/s in any direction.

The kinetic energy theorem uses only the net work — all forces combined. If you want to know *how* the object ended up moving (its direction), you still need force and acceleration. Energy gives you the magnitude. Direction requires the full vector analysis.

### Worked example — the pile driver

A 500-kilogram hammer is lifted 5 meters above a pile and released. Assume air resistance is negligible. *What is the hammer's speed just before impact?*

Method 1 (kinematics): $v^2 = v_0^2 + 2g\Delta h = 0 + 2(9.8)(5) = 98$, so $v = \sqrt{98} \approx 9.9$ m/s.

Method 2 (work-energy theorem): The net work is done by gravity. $W_{\text{net}} = mg \Delta h = (500)(9.8)(5) = 24,500$ J. The change in kinetic energy is $\Delta K = \frac{1}{2}m(v^2 - 0) = 250 v^2$. Setting them equal: $250 v^2 = 24,500$, so $v^2 = 98$ and $v \approx 9.9$ m/s.

Both methods agree, as they must. For constant forces (like gravity), kinematics is faster. For variable forces or complicated paths, energy is faster.

*Now assume there is air resistance that does −2,000 joules of work during the fall. What is the speed at impact?*

The net work is now $W_{\text{net}} = 24,500 - 2,000 = 22,500$ J. By the work-energy theorem:

$$22,500 = 250 v^2$$
$$v^2 = 90$$
$$v \approx 9.5 \text{ m/s}$$

Air resistance cost the hammer about 0.4 m/s. The calculation required no knowledge of how air resistance varies with speed — only its total work.

### Common misconceptions

**Kinetic energy is not the same as momentum.** Kinetic energy is $\frac{1}{2}mv^2$; momentum is $mv$. A heavy truck moving slowly can have less kinetic energy than a light car moving fast, but more momentum. They are different quantities doing different work.

**The work-energy theorem uses net work, not individual forces.** Some students try to write $W_{\text{gravity}} = \Delta K$, but that is only true if gravity is the *only* force doing work. If friction also acts, you must include it: $W_{\text{gravity}} + W_{\text{friction}} = \Delta K$.

**Kinetic energy is always non-negative.** Since $K = \frac{1}{2}mv^2$ and both $m$ and $v^2$ are positive (or zero), kinetic energy cannot be negative. An object with zero kinetic energy is at rest. An object cannot have "negative kinetic energy."

---

## Concept 3 — Power: the rate of energy transfer

### The scene: the power plant

A coal power plant produces electricity by burning coal, boiling water, driving turbines, and running generators. The power output is measured in megawatts — millions of watts. A 500-megawatt plant is doing 500 million joules of work every second.

Now consider a homeowner installing solar panels. The panels' power output is typically 5 to 10 kilowatts on a sunny day — 5,000 to 10,000 joules per second. On cloudy days it might drop to 1 kilowatt.

Power is not energy. Power is the *rate* at which energy flows. A small power output over a long time can deliver the same total energy as a large power output over a short time. A 60-watt light bulb left on for 10 hours uses $60 \times 10 \times 3600 = 2,160,000$ joules — about 0.6 kilowatt-hours. The same bulb run at 60 watts for 100 hours uses 6 kilowatt-hours. The rate is the same; the time and total energy are different.

### The definition of power

Power is the rate of doing work, the limit of average power as the time interval shrinks:

$$P = \frac{dW}{dt}$$

If the power is constant over a time interval, then $W = P \Delta t$. If the power varies with time, the total work is the integral:

$$W = \int P(t) \, dt$$

The units are joules per second, which is called a *watt* (W) in honor of James Watt, the engineer who improved the steam engine. A common alternative unit in the English-speaking world is the horsepower: 1 hp = 746 watts. A large horse can sustain about 1 horsepower for a day. A small car's engine produces roughly 100 to 150 horsepower.

### Power in terms of force and velocity

The instantaneous power delivered by a force $\vec{F}$ acting on a moving object is

$$P = \vec{F} \cdot \vec{v}$$

This emerges directly from the definition: $P = \frac{dW}{dt} = \frac{\vec{F} \cdot d\vec{r}}{dt} = \vec{F} \cdot \frac{d\vec{r}}{dt} = \vec{F} \cdot \vec{v}$.

This formula is powerful. If a force points in the direction of motion, $P > 0$ — the force is doing work, delivering energy. If the force points opposite the motion, $P < 0$ — the force is removing energy. If the force is perpendicular to the motion, $P = 0$ — no power flows, despite the force's magnitude.

A car climbing a hill at constant speed has zero acceleration, so the net force is zero. But the engine is doing positive work against gravity, and air resistance is doing negative work. The power the engine delivers must equal the power gravity and air resistance remove. 

$$P_{\text{engine}} = mg \sin\theta \times v + F_{\text{drag}} \times v$$

where $\theta$ is the hill's slope. For a level road with no grade, the engine power goes entirely into overcoming drag. On a steep hill, most of the power goes to fighting gravity.

### The trade-off: total energy versus instantaneous rate

Power tells you how fast energy is being transferred *right now*. Energy tells you the *total* transferred over a time interval.

This distinction matters because the same total energy can be delivered at wildly different rates. A marathoner runs 42 kilometers in about 2.5 hours, burning roughly 12 million joules (3,000 food calories). A sprinter runs 100 meters in 10 seconds, burning roughly 5,000 joules. The marathoner burns 20 times as much total energy, but at a much lower rate (1.3 megajoules per hour vs. 500 kilojoules per hour).

Energy conservation requires you to track the total. Power efficiency requires you to track the rate. If you are designing a battery for an electric car, you need both: the total energy capacity (how far can it go?) and the peak power (can the motor accelerate fast?). A battery with high energy capacity but low peak power can drive far on a level road but cannot accelerate up a hill.

### Worked example — the climbing athlete

An 80-kilogram athlete does pull-ups on a horizontal bar. Each pull-up raises the athlete's center of mass about 0.6 meters. The athlete does the movement in 0.8 seconds.

*How much work is done?*

The force is gravity: $F = mg = 80 \times 9.8 = 784$ newtons, acting downward. The displacement is upward, 0.6 meters. The angle between them is 180 degrees. The work done *by* gravity is negative: $W_{\text{by gravity}} = 784 \times 0.6 \times (-1) = -470$ joules. The work done *against* gravity (the work the athlete's muscles do) is +470 joules.

*How much power does the athlete develop?*

$P = \frac{W}{t} = \frac{470 \text{ J}}{0.8 \text{ s}} = 588$ watts.

This is about 0.8 horsepower. For comparison, an untrained person doing pull-ups might develop 300–400 watts; an elite athlete doing this at higher reps might sustain 600–700 watts. The number is reasonable.

*If the athlete continues at this power output, how long would it take to climb 10 meters (against gravity, starting from rest)?*

Work needed: $W = mg \times h = (80 \times 9.8) \times 10 = 7,840$ joules. Time: $t = \frac{W}{P} = \frac{7,840}{588} \approx 13.3$ seconds.

This assumes the athlete maintains constant power output, which is unrealistic for 13 seconds of climbing — fatigue sets in. But it is a reasonable estimate.

### Common misconceptions

**Power is not energy.** Energy has units of joules; power has units of watts (joules per second). A 100-watt bulb and a 1000-watt heater both use power. The heater uses 10 times as much power, but if the bulb is on for 10 times longer, they use the same total energy.

**Negative power means energy removal, not "backwards" power.** When friction does negative work on a moving object, we say the force does negative power. The force removes energy. There is no "backwards energy" — negative power is the signed bookkeeping for removal.

**Power depends on both force and velocity.** A small force at high velocity can deliver high power ($P = F \cdot v$). A large force at low velocity might deliver less. This is why bicycles have gears: shift to a lower gear to produce high torque (a kind of force) at low speed, or shift to a higher gear to maintain speed with less muscle force. The power output of the legs remains roughly constant; the gears redistribute it between force and speed.

---

## Integration — From archer to engine

The archer draws the bow, storing energy in the limbs. The release converts elastic potential energy to kinetic energy of the arrow. The arrow flies 100 meters downrange in 0.4 seconds. During the flight, gravity does negative work, slowing the upward component of velocity. Air resistance does negative work, slowing both components.

If the archer asked, *What is my arrow's speed at 100 meters?*, you could use kinematics (solving for the trajectory). Or you could use energy: *How much work did gravity and air resistance do? Subtract that from the arrow's initial kinetic energy. What kinetic energy remains? What speed does that correspond to?* The second path is shorter.

Power entered when the archer draws the bow at a certain speed. A well-trained archer can draw a 40-pound-force bow 28 inches in one second, delivering power $P = F \cdot v = (40 \text{ lbf})(28 \text{ in/s}) \approx 1,100 \text{ lbf} \cdot \text{in/s}$. Converting to SI units (1 lbf = 4.45 N, 1 inch = 0.0254 m): $P \approx 1,100 \times 4.45 \times 0.0254 \approx 124$ watts. This is one-sixth the power of an elite pull-up. The archer's muscles are not delivering much power, but the bow's stiffness means the force is large, and the force-distance product over the draw is significant.

Similarly, a car engine does work lifting the car up hills and accelerating it. The power output is constant (or nearly so) across most of the throttle range. Higher gear ratios trade speed for force; lower gears deliver more force at lower speed. But the power — the rate of energy transfer — stays roughly constant.

Work connects force to the energy that appears as motion. Power connects work to the rate at which it flows. The three together — force, work, power — form the complete language of how energy moves through the world.

---

## Graduated exercises

### Warm-up

**Exercise 8.1** A 10-newton force acts on a 2-kilogram block, pushing it horizontally 5 meters across a frictionless floor. How much work does the force do?

**Exercise 8.2** You lift a 20-newton briefcase straight up 1.5 meters. How much work do you do against gravity?

**Exercise 8.3** A force of 100 newtons acts on an object at 30 degrees to the direction of motion. The object moves 10 meters. How much work is done by the force?

### Application

**Exercise 8.4** A 75-kilogram person climbs stairs, gaining 4 meters in height. (a) How much work does gravity do on the person? (b) How much work does the person do against gravity?

**Exercise 8.5** A spring with constant $k = 200$ N/m is stretched from its equilibrium position by 10 centimeters. How much work must be done to stretch it that amount?

**Exercise 8.6** A 1200-kilogram car accelerates from rest to 25 m/s on level ground. What is the change in kinetic energy? If this acceleration takes 8 seconds, what is the average power delivered by the engine?

### Synthesis

**Exercise 8.7** A 50-kilogram child slides down a frictionless slide from a height of 3 meters. At the bottom, the child enters a horizontal section with friction (coefficient $\mu_k = 0.4$). How far does the child slide on the horizontal section before coming to rest? (Use energy methods; ignore the shape of the slide.)

**Exercise 8.8** An 80-kilogram runner accelerates from rest to 8 m/s in 5 seconds while maintaining constant acceleration. (a) Calculate the change in kinetic energy. (b) If the only horizontal force is the push from the legs, what average force did the runner's legs exert? (c) What is the average power output? (d) What is the instantaneous power at the 5-second mark?

**Exercise 8.9** A 2000-kilogram elevator is raised 20 meters at constant speed in 10 seconds. (a) What is the work done by the cable? (b) What is the power delivered by the cable? (c) If the actual power of the motor is 50 kilowatts, where does the "extra" power go? (Hint: What else is happening to the cable and motor?)

---

## Chapter summary

Work is the dot product of force and displacement, integrated along the path an object takes. For constant forces, work depends only on the endpoints. For variable forces, the path matters. Work is measured in joules, the same units as energy.

Kinetic energy is half the product of mass and the square of speed: $K = \frac{1}{2}mv^2$. This emerges from integrating Newton's second law, leading to the work-energy theorem: net work equals change in kinetic energy. The theorem bypasses the need to calculate force and acceleration at every point, making it invaluable when forces are complicated or paths are curved.

Power is the rate at which work is done, measured in watts. It can be calculated as $P = \frac{dW}{dt}$ or, for a force acting on a moving object, $P = \vec{F} \cdot \vec{v}$. Power is positive when a force delivers energy and negative when it removes energy.

The three concepts interlock: a force does work as it moves an object, work becomes kinetic energy, and power measures the rate of the flow. When the next chapter introduces potential energy and conservation of energy, these tools will expand to encompass all the ways energy moves through a system.

---

## What would change my mind

Evidence that the work-energy theorem fails for relativistic speeds would require revisiting the derivation. (It does not fail — Einstein's relativity modifies the kinetic energy formula to $K = (\gamma - 1)mc^2$ where $\gamma = 1/\sqrt{1 - v^2/c^2}$, and the work-energy theorem remains valid. But the classical formula is approximate at high speed.)

---

## Still puzzling

The exact trajectory a falling object follows through the air under realistic drag is not yet understood in closed form for all initial conditions. The work-energy theorem tells us the final kinetic energy, but the intermediate dynamics remain a numerical problem. This is not a weakness of the theorem — it is simply a limit of closed-form solutions in mechanics.

---

## Tags

work · kinetic-energy · work-energy-theorem · line-integral · power · dot-product · energy-methods · variable-forces · conservation-of-energy · mechanical-energy


---

## LLM Exercise — Chapter 8: Work-Energy Theorem Verification

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Work as a numerical line integral, kinetic energy tracking, and empirical verification of the work-energy theorem on the toolkit's existing scenarios.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 8 task in the physics-simulation-toolkit. The chapter
established $W = \int \vec{F} \cdot d\vec{r}$ and the work-energy
theorem $W_{\text{net}} = \Delta K$. Add the energy bookkeeping to
the toolkit and verify the theorem empirically across the scenarios
already built.

In `chapters/ch08_work_energy/`:

1. `simulations.py`:
   - `work_along_path(force_fn, path_points)` — compute the line
     integral $\int \vec{F} \cdot d\vec{r}$ as a discrete sum over the
     path's segments.
   - `kinetic_energy(body)` — $\frac{1}{2}mv^2$.
   - `instrument_system(system, log_kinetic=True, log_work_per_force=True)`
     — wrapper that, at each integration step, logs each body's
     kinetic energy and the work done by each force on each body.
   - `power(force, velocity)` — $P = \vec{F} \cdot \vec{v}$.

2. `test_simulations.py`:
   - Constant-force-along-line: the work-energy theorem becomes
     $Fd = \Delta K$, trivially verified.
   - Variable-spring force (Ch 6 Spring): work done against a spring
     pulled from 0 to x is $\frac{1}{2}kx^2$. Verify by integrating
     numerically against analytical.
   - Projectile in 2D (Ch 5): the total work done by gravity along the
     trajectory equals $-mg \cdot \Delta h$ (the negative of the
     gravitational potential energy change, which we'll formalize in
     Ch 9). Verify with the work-along-path tool.
   - Loop-the-loop (Ch 7): on a frictionless loop, $W_{\text{net}} =
     \Delta K$ for the cart. With kinetic friction added, the work
     done by friction is $-\mu_k N s$ (path-length dependent). Verify
     empirically.

3. `benchmarks.py` — for the projectile-with-drag (Ch 5), measure the
   work done by drag along the trajectory. Plot kinetic-energy
   trajectories with and without drag. The "missing" kinetic energy
   should equal the work done by drag (with sign). Confirm to within
   integration error.

4. `README.md` — decision cards for work-along-path, kinetic energy,
   and power. "Surprising findings": how the work-done-by-drag scales
   with launch angle (steeper launches stay aloft longer, more
   integrated drag work).

Commit as `ch08: work as line integral with work-energy theorem
verification`.
```

**What this produces:** Work and kinetic-energy bookkeeping, empirical verification of the work-energy theorem on four scenarios, and the drag-energy balance for projectiles.

**How to adapt this prompt:**

- *For your own project:* The work-energy theorem is *exact* in the analytical version. Any disagreement in your simulation is integration error — and quantifying it is the actual lesson.
- *For ChatGPT / Gemini:* Both work.
- *For Claude Code:* Native fit. Have it generate the comparison plots.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Instruments the systems from Ch 5–7 with energy tracking.

**Preview of next chapter:** Chapter 9 distinguishes conservative from non-conservative forces, defines potential energy for the conservative ones, and verifies total mechanical energy conservation.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Gaspard-Gustave de Coriolis** was the 1829 paper *Du calcul de l'effet des machines* that introduced the modern technical meaning of *work* into physics ($W = Fd$, force times distance along the displacement), as a measure of what a machine accomplishes — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Gaspard-Gustave de Coriolis, and how does their work on the definition of work as a line integral of force, and the early-19th-century development of energy concepts connect to the modern definition of mechanical work? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Gaspard-Gustave de Coriolis"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Coriolis's specific 1829 argument that work — not power, not effort — was the right measure of what a machine produces
- Ask: "Coriolis is famous for the Coriolis force (1835). Yet his definition of *work* (1829) is arguably more historically important. Why is the Coriolis-force name well-known and the work-definition forgotten?"
- Add the framing: "Answer as if you're writing the historical sidebar in a 2026 engineering-mechanics textbook on why $W = Fd$"

What changes? What gets better? What gets worse?
