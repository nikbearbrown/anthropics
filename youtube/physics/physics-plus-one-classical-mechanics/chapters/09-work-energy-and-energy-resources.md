# Chapter 9 — Work, Energy, and Energy Resources

*The one thing that is always conserved, and what it means to spend it.*

---

## A pumped-storage reservoir, off-peak hours

Forty miles outside any city, on a wooded hillside, sits an upper reservoir — a man-made lake with a concrete dam, half a kilometer above a lower lake at the foot of the hill. At 2:00 AM, when electricity demand is low and electricity is cheap, large pumps lift water from the lower lake to the upper one. The pumps run for hours. By dawn, the upper reservoir is full.

At 5:00 PM, when demand peaks, valves open. Water flows back down through turbines and generates electricity that is sold at peak prices. By midnight, the upper reservoir is empty again.

This is a pumped-storage hydroelectric plant — a battery. But instead of storing energy chemically, it stores energy *gravitationally*. Lifted water has more potential energy than water at the bottom. When you let it fall, that potential energy converts to kinetic energy (water moving fast through pipes) and then to electrical energy (turbines spinning generators). The whole cycle is a translation between forms.

The roundtrip efficiency is about 75%. A quarter of the energy you pump up is lost — to friction in the pumps, drag in the pipes, heat in the generators, turbulence in the water column. Conservation of energy doesn't say all the energy comes back as electricity. It says all the energy goes *somewhere*. Most of what doesn't come back as electricity ends up as low-grade heat in the surrounding rock and water, warming the hillside by an amount too small to measure except over long times.

This chapter is about that translation. Work is what transfers energy from one form to another. Kinetic energy, potential energy, and thermal energy are the accounts the energy moves between. The total never changes. And power is the rate — how fast the translation happens, and at what fraction of the input makes it out as something useful.

Pumped storage is one example. Your body, your car, every star burning in the sky is doing the same bookkeeping. Once you understand the ledger, you can read any of them.

---

## Work

The word "work" has a technical meaning in physics that is narrower than the everyday sense, and the narrowing matters.

A person carries a briefcase across a level office floor at constant velocity. From a physicist's perspective, the work done on the briefcase is zero. The person feels tired — their muscles are doing work on themselves, compressing and extending against their own skeleton. But the force they apply to the briefcase (upward, supporting its weight against gravity) is perpendicular to the briefcase's motion (horizontal). Force perpendicular to displacement does no work.

Now the same person carries the briefcase up a flight of stairs at constant velocity. The upward force now has a component aligned with the upward displacement. Work is done. The briefcase gains gravitational potential energy equal to the work input.

The physics definition: for a constant force $\mathbf{F}$ acting through displacement $\mathbf{d}$,

$$W = Fd\cos\theta,$$

where $\theta$ is the angle between the force and the displacement. Three cases worth knowing cold:

- $\theta = 0°$: force aligned with motion. $W = Fd$. Full work done.
- $\theta = 90°$: force perpendicular to motion. $W = 0$. The briefcase across the floor.
- $\theta = 180°$: force opposite to motion. $W = -Fd$. Friction slowing a sliding object.

Negative work removes energy from the object. Positive work adds it. The unit of work is the joule: one newton-meter.

Now the deep result that connects force to speed. The *net* work done on an object — the sum of work by every force acting on it — equals the change in its kinetic energy:

$$W_\text{net} = \Delta KE = \tfrac{1}{2}mv_f^2 - \tfrac{1}{2}mv_i^2.$$

This is the **work-energy theorem**. The derivation is short: apply $F = ma$, multiply both sides by displacement $d$, substitute $v_f^2 = v_i^2 + 2ad$ from Chapter 3. The result is universal. Any time net work is done on an object, its kinetic energy changes by exactly that amount, regardless of the path taken.

Kinetic energy is $KE = \tfrac{1}{2}mv^2$. A $1 \text{ kg}$ object at $1 \text{ m/s}$ carries $0.5 \text{ J}$. A $1500 \text{ kg}$ car at $30 \text{ m/s}$ carries $675{,}000 \text{ J}$. Same formula; the numbers differ because the car is a thousand times heavier and the speed appears squared.

A worked example. You push a $1500 \text{ kg}$ stalled car along a level road with $400 \text{ N}$ of horizontal force for $20 \text{ m}$. Friction opposes motion at $200 \text{ N}$.

Work by your push: $(400)(20)\cos 0° = 8000 \text{ J}$.

Work by friction: $(200)(20)\cos 180° = -4000 \text{ J}$.

Work by gravity and normal force: zero (both perpendicular to motion).

Net work: $8000 - 4000 = 4000 \text{ J}$.

Work-energy theorem, starting from rest:

$$4000 = \tfrac{1}{2}(1500)v_f^2 \implies v_f = \sqrt{\frac{8000}{1500}} \approx 2.3 \text{ m/s}.$$

Sanity check: net force is $200 \text{ N}$, acceleration is $200/1500 \approx 0.133 \text{ m/s}^2$. Using the kinematics from Chapter 3: $v^2 = 2(0.133)(20) = 5.33$, $v = 2.3 \text{ m/s}$. Same answer. Good — the work-energy theorem is equivalent to Newton's second law applied over a displacement. It's not a new law; it's a different way to use the old one.

The advantage of the work-energy approach: you don't need to know the direction of the final velocity, only the magnitude. For problems where forces act at various angles and you want the speed at the end, scalar bookkeeping is often much cleaner than vector force analysis.

---

## Potential energy and conservation

Here is the next step in the accounting. Some forces — gravity, spring forces, the electric force from fixed charges — have a special property: the work they do depends only on where you start and where you end, not on the path you took. These are called **conservative forces**, and they let you define a *stored* form of energy called **potential energy**.

The rule is: the work done by a conservative force on an object equals the *decrease* in potential energy:

$$W_\text{conservative} = -\Delta PE.$$

For gravity near Earth's surface:

$$PE_g = mgh,$$

where $h$ is height above some chosen reference level. The reference is arbitrary — only changes in $PE_g$ matter physically. On Earth's surface, the choice is usually "height above the floor" or "height above the ground."

For a spring (Hooke's law, from Chapter 7):

$$PE_s = \tfrac{1}{2}kx^2,$$

where $x$ is the displacement from the spring's natural length.

The payoff is **conservation of mechanical energy**: when only conservative forces act,

$$KE_i + PE_i = KE_f + PE_f.$$

Total mechanical energy is constant. It shifts between kinetic and potential, but the sum stays fixed.

A roller coaster car starts from rest at the crest of a hill $40 \text{ m}$ above the bottom. How fast is it going at the bottom?

$$mgh = \tfrac{1}{2}mv^2 \implies v = \sqrt{2gh} = \sqrt{2(9.80)(40)} \approx 28 \text{ m/s}.$$

About $100 \text{ km/h}$. One line. No need to know the shape of the track, the slope at any point, or the direction of any intermediate force. The path doesn't matter because the only force doing work is gravity, and gravity is conservative. You just compare the energy at the start and end.

This is why the potential-energy framework is worth the conceptual investment. It replaces a potentially hard integral along a curved path with a single equation comparing two states. The trick is recognizing when only conservative forces act — and when they don't.

Friction is not conservative. Drag is not conservative. They depend on path length, not just endpoints. A crate pushed $5 \text{ m}$ directly across a floor encounters half the friction work of a crate pushed along a $10 \text{ m}$ zigzag between the same two points. You cannot define a potential energy for friction. When friction is present, mechanical energy decreases — it converts to thermal energy, heating the surfaces — and you have to account for it explicitly:

$$KE_i + PE_i + W_\text{nc} = KE_f + PE_f,$$

where $W_\text{nc}$ is the work done by non-conservative forces (negative for friction). *Mechanical* energy is not conserved. *Total* energy — including thermal — always is. The bookkeeping just got harder because the ledger now has more accounts.

A pendulum bob of mass $0.50 \text{ kg}$ is released from rest at height $0.20 \text{ m}$ above its lowest point. Ignoring air resistance:

$$PE_i = mgh_i = (0.50)(9.80)(0.20) = 0.98 \text{ J}, \quad KE_i = 0.$$

At the bottom, $h = 0$ so $PE_f = 0$:

$$0.98 = \tfrac{1}{2}(0.50)v_f^2 \implies v_f = \sqrt{\frac{2 \times 0.98}{0.50}} = 1.98 \text{ m/s}.$$

The mass canceled. The bob's speed at the bottom depends only on the height it fell from. A heavier bob would reach the same speed. This is the same principle that makes every mass fall at the same rate under gravity: the mass appears in both the force (gravity) and the inertia (Newton's second law), and it cancels in the motion. Here it appears in both the potential energy and the kinetic energy, and it cancels again.

One more thing about potential energy that students often miss: it doesn't belong to the object alone. Gravitational PE belongs to the object-Earth *system* — you can't have gravitational potential energy without two interacting masses. The single-object language ("the ball has $mgh$ of PE") is a useful shortcut, but the energy is stored in the interaction, not in the ball.

---

## Power and efficiency

Energy alone doesn't tell you whether a process is fast or slow, useful or wasteful. Two more quantities do.

**Power** is the rate of energy transfer:

$$P = \frac{W}{t} = \frac{\Delta E}{\Delta t}.$$

Unit: one joule per second = one watt. For a force $F$ moving something at speed $v$ in the same direction:

$$P = Fv.$$

Some scales worth having in your head:

- A person at rest: about $100 \text{ W}$ (metabolic, mostly heat).
- Brisk walking: $200$–$300 \text{ W}$.
- An elite athlete sprinting: up to $2{,}000 \text{ W}$ briefly.
- One horsepower: $746 \text{ W}$ (defined as approximately the sustained work rate of a draft horse).
- A small car cruising at highway speed: $\sim 30{,}000 \text{ W}$.
- A nuclear power plant: $\sim 10^9 \text{ W}$ ($1 \text{ GW}$).

The joule is a small unit — a lifted apple (roughly $1 \text{ N}$ over $1 \text{ m}$) stores about $1 \text{ J}$. The kilowatt-hour (kWh) is more practical at human scales: $1 \text{ kWh} = 3.6 \times 10^6 \text{ J}$. Electricity is sold by the kWh; a typical U.S. household uses $\sim 30 \text{ kWh/day}$, which is an average power of about $1{,}250 \text{ W}$ — roughly the sustained output of a dozen or so people working hard.

**Efficiency** is the fraction of input energy that becomes useful output:

$$\eta = \frac{E_\text{useful}}{E_\text{input}}.$$

A car engine: about $25\%$ (the rest leaves as exhaust heat). A coal-fired power plant: $\sim 35\%$. A modern LED light: $\sim 40\%$ light, $60\%$ heat. An incandescent bulb: $\sim 5\%$ light, $95\%$ heat — which is why replacing incandescents with LEDs is one of the cheapest efficiency gains in household energy. Efficiencies are bounded at $100\%$ by conservation of energy; they are bounded well below $100\%$ by thermodynamic laws we will meet in Chapter 15, where the second law will explain why no heat engine can be perfectly efficient.

A person consumes $2{,}500 \text{ kcal}$ of food per day. $1 \text{ kcal} = 4{,}184 \text{ J}$, so:

$$E = 2500 \times 4184 \approx 1.05 \times 10^7 \text{ J} = 10.5 \text{ MJ}.$$

Over $86{,}400 \text{ s}$ in a day:

$$P = \frac{1.05 \times 10^7}{86{,}400} \approx 121 \text{ W}.$$

A sedentary person runs at roughly the same power as a $100 \text{ W}$ incandescent light bulb. A vigorously exercising person reaches $500$–$1{,}000 \text{ W}$ — five to ten light bulbs — which is why gymnasiums get warm quickly and why marathon runners need massive cooling. The human body is about $25\%$ efficient at converting food to mechanical work, similar to a car engine, with the remainder leaving as heat.

---

## The universal currency

Step back and look at what these three concepts do together.

**Work** ($W = Fd\cos\theta$) transfers energy between systems or between forms. The work-energy theorem makes the connection to kinetic energy exact: net work equals $\Delta KE$, always.

**Potential energy** captures the energy stored in configurations under conservative forces — gravity, springs, electric fields. Conservation of mechanical energy lets you solve problems by comparing states at two points in time, without integrating along the path.

**Power** and **efficiency** connect the idealized physics to the real world of machines, budgets, and biology. Power tells you the rate; efficiency tells you the loss.

The scale range is one of the most striking things about this framework. The conservation principle that predicts a pendulum bob's swing speed at $1 \text{ J}$ is the same principle that governs the operation of a pumped-storage reservoir at $10^{12} \text{ J}$ and the orbital kinetic energy of the Earth at $10^{33} \text{ J}$. The algebra is the same; only the exponents change.

The pumped-storage plant from the opening, fully calculated: $10^9 \text{ kg}$ of water at $400 \text{ m}$ average height above the lower reservoir.

Stored potential energy:

$$PE = mgh = (10^9)(9.80)(400) = 3.92 \times 10^{12} \text{ J} = 3.92 \text{ TJ}.$$

In kWh: $3.92 \times 10^{12} / (3.6 \times 10^6) \approx 1.09 \times 10^6 \text{ kWh}$ — enough to power roughly $30{,}000$ U.S. homes for a day.

Turbines at $90\%$ efficiency, releasing over $4$ hours:

$$P_\text{out} = \frac{0.90 \times 3.92 \times 10^{12}}{4 \times 3600} \approx 245 \text{ MW}.$$

Pumps at $85\%$ efficiency to refill:

$$E_\text{input} = \frac{3.92 \times 10^{12}}{0.85} \approx 4.61 \text{ TJ}.$$

Roundtrip: $3.53 \text{ TJ}$ out for $4.61 \text{ TJ}$ in, or about $77\%$. The missing $23\%$ is heat — in the water, the machinery, the rock.

The pumped-storage calculation is the opening story, now with numbers. The energy went up as electrical work, sat as gravitational potential energy, came back as electrical work, and the gap between what went in and what came out is heat too diffuse to recover. Conservation of energy accounts for every joule. The total is unchanged. The *useful* fraction shrank at every conversion step.

Feynman said in his lectures that we have no knowledge of what energy *is* — only that it is a number we can compute about a system that happens to be conserved through time. The conservation law works whether or not you understand what's being conserved. What you've learned in this chapter is not what energy is. It's how to keep track of it.

---

## Exercises

### Warm-up

**9.1** You push a $20 \text{ kg}$ box across a frictionless floor with $50 \text{ N}$ for $4.0 \text{ m}$. (a) How much work do you do? (b) What is the box's final kinetic energy if it started from rest? (c) What is its final speed?

**9.2** You carry a $5 \text{ kg}$ bag of groceries at constant velocity for $20 \text{ m}$ across a level parking lot. How much work do you do on the bag?

**9.3** A $0.5 \text{ kg}$ rock is held $3.0 \text{ m}$ above the ground. (a) What is its gravitational PE relative to the ground? (b) If dropped, what is its speed just before impact (ignore air drag)?

**9.4** A $1{,}500 \text{ W}$ hair dryer runs for $10$ minutes. (a) How much energy in joules? (b) In kWh? (c) At $\$0.15$/kWh, what does it cost?

### Application

**9.5** A $60 \text{ kg}$ skier starts from rest at the top of a slope $30 \text{ m}$ above the bottom. Ignoring friction, what is her speed at the bottom?

**9.6** A $1{,}200 \text{ kg}$ car traveling at $20 \text{ m/s}$ skids to a stop on a level road. The kinetic friction coefficient is $\mu_k = 0.6$. (a) Compute the initial KE. (b) Use the work-energy theorem to find the stopping distance.

**9.7** A spring with $k = 200 \text{ N/m}$ is compressed by $0.10 \text{ m}$. (a) What is the elastic PE stored? (b) If released and pushing a $0.20 \text{ kg}$ ball, what is the ball's launch speed?

**9.8** A car climbs a $5\%$ grade ($\sin\theta \approx 0.05$) at a constant $20 \text{ m/s}$. Mass is $1{,}500 \text{ kg}$. (a) What is the rate at which the engine does work against gravity, ignoring friction and drag? (b) What is this in horsepower ($1 \text{ hp} = 746 \text{ W}$)?

### Synthesis

**9.9** A roller coaster car of mass $400 \text{ kg}$ starts from rest at $h = 50 \text{ m}$ and reaches the bottom at $25 \text{ m/s}$. (a) Compute the final KE. (b) Compute the initial PE. (c) How much mechanical energy was lost to friction? (d) Where did that energy go?

**9.10** You climb a $20 \text{ m}$ flight of stairs in $30 \text{ s}$. Your mass is $70 \text{ kg}$. (a) How much work do you do against gravity? (b) What is your average mechanical power output? (c) Look up a typical efficiency for the human body (food calories to mechanical work) and use it to estimate how many food calories the climb required.

**9.11** A $0.5 \text{ kg}$ ball is thrown straight up at $15 \text{ m/s}$ from ground level. Using energy conservation, find: (a) the maximum height, (b) the speed when the ball is half that height, (c) the speed when it returns to ground level.

### Challenge

**9.12** A pumped-storage plant lifts $3 \times 10^9 \text{ kg}$ of water through $250 \text{ m}$ of elevation. (a) Total gravitational PE stored? (b) If pumped over $8$ hours at $80\%$ efficiency, what input power is required? (c) If discharged over $4$ hours at $90\%$ efficiency, what output power is delivered? (d) What roundtrip efficiency does this plant achieve?

**9.13** Estimate the kinetic energy of (a) a $5 \text{ g}$ bullet at $400 \text{ m/s}$; (b) a $1{,}500 \text{ kg}$ car at $30 \text{ m/s}$; (c) the Earth orbiting the Sun (mass $6 \times 10^{24} \text{ kg}$, orbital speed $30{,}000 \text{ m/s}$). Compare them in orders of magnitude.

---

## LLM Exercise — Chapter 9: Energy Bookkeeping for Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** An energy budget for one cycle of your anchor phenomenon, with input, useful output, and dissipated forms identified.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 9, I want to build an energy budget for one cycle or one event of my phenomenon. Please:

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

7. One sentence on how this connects to Chapter 10 (momentum) — energy conservation gives you speeds; momentum conservation gives you what gets transferred in collisions.

Save the output as logbook/chapter-09-energy.md.
```

### What this produces

A ninth Logbook entry: an energy budget for your phenomenon, often illuminating which parts are inefficient and which are not.

### How to adapt this prompt

- *For phenomena with mostly heat output* (a coffee maker, a hair dryer): efficiency is mostly the question of "what fraction of electrical input ends up doing the intended thing vs. heating the surroundings."
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have power data (a smart-meter reading, an electricity bill), paste it; let Claude compute energy and efficiency directly.

### Connection to previous chapters

Builds directly on Chapter 6 (force). Energy is what work *transfers* — and work is force times displacement. Friction (Chapter 7) is the principal source of mechanical-to-thermal conversion. Chapter 8's circular motion is interesting here: at constant speed, gravity does no net work on a satellite.

### Preview of next chapter

Chapter 10 introduces momentum, the other great conservation law of mechanics. While energy conservation gives you final speeds, momentum conservation governs collisions — what shares with what when two objects hit each other.

---

## AI Wayback Machine

**James Prescott Joule** demonstrated in 1843 that mechanical work can be converted to heat at a fixed ratio — the mechanical equivalent of heat. The result killed the caloric theory of heat and unified energy as a single quantity that flows between forms.

**Run this:**

```
Who was James Prescott Joule, and how does the mechanical equivalent of heat connect to the work and energy we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"James Prescott Joule"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Joule's paddle-wheel experiment in detail — what was measured, how was it converted?
- Ask it about Joule's role as a brewer's son and how that work shaped his physics.

What changes? What gets better? What gets worse?
