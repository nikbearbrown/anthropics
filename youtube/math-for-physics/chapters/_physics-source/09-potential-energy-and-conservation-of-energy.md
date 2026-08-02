# Chapter 9 — Potential Energy and Conservation of Energy


## TL;DR

- TL;DR: A system does work to lift an object against gravity.
- The chapter moves through Three Title Options, Cold Open, Concept 1 — Conservative Forces and Potential Energy, Gravitational Potential Energy Near Earth's Surface, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

## Three Title Options

1. The Work Stored: How Energy Changes Form Without Disappearing
2. What the System Remembers: Potential Energy and the Conservation Law
3. The Ledger Never Closes: Why Energy Changes Shape But Never Amount

---

**TL;DR:** A system does work to lift an object against gravity. That work doesn't vanish — it hides in the object's height, waiting to turn back into motion. The rule is simple: in a closed system with only conservative forces, the total mechanical energy $E = K + U$ never changes. This turns hard dynamics problems into bookkeeping problems.

---

## Cold Open

At the top of a roller coaster's first hill, something has done work. A motor or a chain has pulled a 1,000-kilogram car up 45 meters of vertical height against Earth's gravity. The motor has spent energy — real electrical energy, burning real fuel, or both. Once the car reaches the crest and stops, that spent energy seems to have vanished. The car isn't moving. It's sitting still.

Then the chain releases. The car tips over the edge, picks up speed, drops back down. At the bottom of the hill, it's moving at 30 meters per second. It climbs the next hill, which is slightly shorter — 40 meters instead of 45. The car makes it to the top of that hill, still moving, and coasts through. It descends again, picks up speed, climbs the next rise, and does it all again. A perfect loop, a perfect exchange. Down becomes kinetic energy; up becomes gravitational energy held in suspension; kinetic becomes potential; potential becomes kinetic. The conversion runs on schedule, and the only leak is friction and air drag.

The motor did work once. That work got transformed into a shape that could be released later. It got transformed again, and again. The total of kinetic plus potential stays constant — or would, if friction let it. This is conservation of mechanical energy. It is the most powerful shortcut in introductory physics because it lets you bypass the complicated forces — normal forces, friction, air drag, the tension in the string or the track — and jump straight to the answer: what's the speed here, given only where it started?

Here is the scene more carefully. The car sits on the crest before the first drop. Its kinetic energy is zero — it's stationary. Its gravitational potential energy is large, set by its mass, gravity's pull, and how high it sits. When it falls, gravity pulls it downward. Gravity does positive work on the moving car. The work-energy theorem says this work shows up as an increase in kinetic energy. The car speeds up. As it falls, its height decreases. A force pulling downward, over a distance in the direction of that force, does positive work — lots of it. But something else is shrinking: the height above the ground. The gravitational potential energy *decreases* as the kinetic energy *increases*. They are opposite. The total remains constant. You can read the future of the roller coaster without solving a single differential equation. You just need the bookkeeping rule.

---

## Concept 1 — Conservative Forces and Potential Energy

A conservative force is one whose work depends only on the start and end positions, not on the path taken. Gravity is conservative. A spring force is conservative. Friction is not — it bleeds energy, and the amount of bleeding depends on how far you slide, which depends on the path. Friction is dissipative, non-conservative. The path matters.

For any conservative force, we define potential energy $U$ such that the work done by that force equals the negative change in potential energy:

$$W_{\text{conservative}} = -\Delta U = -(U_f - U_i) = U_i - U_f$$

Rearranging:

$$\Delta U = U_f - U_i = -W_{\text{conservative}}$$

This is the definition. It is not derived. It is a choice we make — a useful one. When a conservative force does positive work, the potential energy decreases. When a conservative force does negative work (when we lift something against gravity), the potential energy increases. The potential energy stores the work that a conservative force could release if we let the system go.

Here is a key truth: potential energy is never absolute. Only differences matter. We always choose a reference point where we say "the potential energy is zero here," and measure all other potential energies relative to that choice. At ground level in most problems, we set $U = 0$. At the unstretched position of a spring, we set $U = 0$. The choice is arbitrary — the physics doesn't care where you plant your zero — but once planted, it must stay planted throughout the problem.

### Gravitational Potential Energy Near Earth's Surface

Near Earth's surface, gravity is approximately constant: $g \approx 9.8 \, \text{m/s}^2$. The gravitational force on a mass $m$ is $F = mg$ downward. When an object rises or falls, gravity does work:

$$W = \vec{F} \cdot \vec{d} = -mg(y_f - y_i) = mg(y_i - y_f)$$

The negative sign appears because gravity points downward (negative $y$-direction) and displacement upward is positive. Gravity does *negative* work on a rising object. By our definition, the potential energy change is:

$$\Delta U = -W = mg(y_f - y_i)$$

If we choose zero potential energy at $y = 0$ (the reference height), then the potential energy at any height $y$ is:

$$U(y) = mgy$$

This is linear in height. Every meter up adds $mg$ joules. A 75-kilogram hiker climbing a 147-meter hill gains gravitational potential energy:

$$\Delta U = mg\Delta y = (75 \, \text{kg})(9.8 \, \text{m/s}^2)(147 \, \text{m}) = 108 \, \text{kJ}$$

That's not a coincidence. The motor that pulled the roller coaster car up 45 meters had to do at least that much work — and on a real coaster, more, because friction steals some.

### Elastic Potential Energy in a Spring

A spring at rest has no force. Compress it or stretch it by amount $x$ from equilibrium, and Hooke's law says the restoring force is:

$$F = -kx$$

where $k$ is the spring constant (units: N/m). The negative sign means the force points back toward equilibrium. To compress or stretch the spring, you have to do work against this force. The work done by the spring force as the spring returns from displacement $x_f$ to $x_i$ is:

$$W_{\text{spring}} = \int_{x_i}^{x_f} (-kx) \, dx = -\frac{1}{2}k(x_f^2 - x_i^2)$$

By definition, the potential energy change is:

$$\Delta U = -W_{\text{spring}} = \frac{1}{2}k(x_f^2 - x_i^2)$$

If we choose zero potential energy at the equilibrium position ($x = 0$), the potential energy at displacement $x$ is:

$$U(x) = \frac{1}{2}kx^2$$

This is *quadratic*. A spring with spring constant $k = 4 \, \text{N/cm}$ stretched 3 cm stores elastic potential energy:

$$U = \frac{1}{2}(4 \, \text{N/cm})(3 \, \text{cm})^2 = 18 \, \text{J}$$

Stretch it to 6 cm:

$$U = \frac{1}{2}(4 \, \text{N/cm})(6 \, \text{cm})^2 = 72 \, \text{J}$$

The energy quadruples when you double the stretch. This is why springs are explosively useful — a small displacement stores disproportionately large energy.

### Trade-off: Energy Method Strength and Limitation

The energy method is powerful because it sidesteps forces. You don't need to know the normal force from the track. You don't need to solve complicated differential equations. You just need to identify which forces are conservative, write down their potential energies, and bookkeep.

The limitation: this method only works when non-conservative forces either don't act or do zero work. If friction is present and significant, the mechanical energy $K + U$ is not conserved. Some energy leaks into heat. On a real roller coaster, friction and air drag steal energy continuously. The car's speed is lower at each crest than energy conservation would predict, and eventually the car won't make it over a hill. You can still use energy methods — you account for the work done by friction as an additional term — but you lose the simplicity.

### Worked Example: A Quartic Force

A particle of mass $m$ moves under a one-dimensional force $F(x) = -cx^3$, where $c = 8 \, \text{N/m}^3$. The particle's total mechanical energy is $E = 2 \, \text{J}$.

**(a) Find the potential energy function.**

By definition, $F = -\frac{dU}{dx}$, so:

$$U(x) = -\int F(x) \, dx = -\int (-cx^3) \, dx = \frac{1}{4}cx^4 + \text{const}$$

Choose zero potential energy at $x = 0$:

$$U(x) = \frac{1}{4}(8 \, \text{N/m}^3) x^4 = 2x^4 \, \text{J (with } x \text{ in meters)}$$

**(b) At what positions is the kinetic energy zero?**

At turning points, $K = 0$, so $E = U$:

$$2 = 2x^4$$
$$x^4 = 1$$
$$x = \pm 1 \, \text{m}$$

The particle can only move in the region $-1 \leq x \leq 1$ meter. Beyond that, potential energy exceeds total energy, which is impossible (kinetic energy can't be negative).

**(c) What is the maximum speed, and where does it occur?**

Maximum kinetic energy occurs at minimum potential energy, which is at $x = 0$:

$$K_{\max} = E - U(0) = 2 - 0 = 2 \, \text{J}$$

The maximum speed is:

$$v_{\max} = \sqrt{\frac{2K_{\max}}{m}}$$

Without knowing $m$, we can't compute a number. But we know this speed occurs at the equilibrium point.

### Common Misconceptions

**"Potential energy is stored in the object."** Potential energy is stored in the *system* — the interaction between the object and whatever field (gravity, spring, electric field) is exerting the force. A ball sitting on a shelf has gravitational potential energy only because Earth is pulling on it. Alone in the void, it has none.

**"You can choose any zero point, so potential energy is meaningless."** You can choose any zero point, yes. But the *differences* in potential energy are absolute — they don't depend on your choice. When you lift a 1 kg mass by 1 meter, you increase its potential energy by $mg = 9.8 \, \text{J}$, no matter where you set your origin. The zero is a choice; the difference is physics.

**"Potential energy and kinetic energy always add to the same number."** True only if no non-conservative forces act. Friction drains the total. When you slide a book across a table and it stops, the mechanical energy $K + U$ decreases — the "missing" energy has become heat.

---

## Concept 2 — Conservation of Mechanical Energy

In a closed system with only conservative forces at work, the total mechanical energy is constant:

$$E = K + U = \text{constant}$$

Equivalently:

$$K_i + U_i = K_f + U_f$$

This is the heart of the energy method. You don't need to know the forces. You don't need to solve $F = ma$. You just measure or calculate the kinetic and potential energies at two points, set them equal, and solve for the unknown.

If non-conservative forces do act and do work, then:

$$W_{\text{non-conservative}} = \Delta(K + U) = (K_f + U_f) - (K_i + U_i)$$

The work done by friction, air drag, or any dissipative force equals the change in total mechanical energy. This is why engineers care about friction — it's a direct leak from the mechanical energy budget.

### A Pendulum at Amplitude

A pendulum bob of mass $m$ is released from rest at an angle $\theta$ above the lowest point of its swing. The string has length $L$. What is the bob's speed at the lowest point?

Choose the lowest point as your reference, where gravitational potential energy is zero. At the initial angle $\theta$, the bob is at height:

$$h = L - L\cos\theta = L(1 - \cos\theta)$$

Initial energy:

$$E_i = 0 + mgh = mgL(1 - \cos\theta)$$

(Kinetic energy is zero because the bob starts from rest.)

At the lowest point:

$$E_f = \frac{1}{2}mv^2 + 0$$

(Potential energy is zero by choice; kinetic energy is maximum.)

By conservation:

$$mgL(1 - \cos\theta) = \frac{1}{2}mv^2$$

$$v = \sqrt{2gL(1 - \cos\theta)}$$

For $\theta = 30°$:

$$v = \sqrt{2(9.8 \, \text{m/s}^2)(1 \, \text{m})(1 - \cos 30°)} = \sqrt{2(9.8)(1 - 0.866)} = \sqrt{2.63} = 1.62 \, \text{m/s}$$

No calculus. No solving the differential equation of the pendulum. Just geometry, potential energy, kinetic energy, and conservation. This is why energy methods are taught first in introductory mechanics.

### A Helicopter Panel Falling Through Air

A 15 kg panel falls 1,000 meters from a hovering helicopter and hits the ground at 45 m/s. How much mechanical energy was dissipated by air resistance?

Initial state (at the helicopter):
- Height: $h_i = 1,000 \, \text{m}$
- Speed: $v_i = 0$
- Kinetic energy: $K_i = 0$
- Potential energy (zero at ground): $U_i = mgh_i = (15)(9.8)(1,000) = 147 \, \text{kJ}$
- Total: $E_i = 147 \, \text{kJ}$

Final state (at ground):
- Height: $h_f = 0$
- Speed: $v_f = 45 \, \text{m/s}$
- Kinetic energy: $K_f = \frac{1}{2}mv_f^2 = \frac{1}{2}(15)(45)^2 = 15,188 \, \text{J} \approx 15.2 \, \text{kJ}$
- Potential energy: $U_f = 0$
- Total: $E_f = 15.2 \, \text{kJ}$

The mechanical energy lost is:

$$E_{\text{dissipated}} = E_i - E_f = 147 - 15.2 = 131.8 \, \text{kJ} \approx 130 \, \text{kJ}$$

Without knowing anything about the air resistance force, we know exactly how much energy the air stole. That is the power of energy methods.

### Trade-off: When Energy Methods Work and When They Don't

Energy methods are fastest when:
- You care only about speeds or positions, not the time it takes to get there.
- The forces are complicated and you can't write a nice equation for them.
- The path is intricate — up and down, around curves — but the start and end points are clear.

Energy methods are helpless when:
- You need to know when the object reaches a certain point (not just whether it reaches).
- All the forces are *non-conservative*, like friction with no way to separate the heat.
- You need the force as a function of position — the energy tells you whether motion is allowed, but not the acceleration.

The full solution to mechanics uses both. Energy tells you the envelope of what's possible. Dynamics — $F = ma$ — tells you the time-dependent details inside that envelope.

### Worked Example: A Mass Dropped onto a Spring

A 0.2 kg mass is released from rest 0.5 meters above the free end of a vertical spring with spring constant $k = 100 \, \text{N/m}$. The mass hits the spring and compresses it. What is the maximum compression?

Choose the natural length of the spring (unstretched) as the reference point where both gravitational and elastic potential energy are zero.

Initial state:
- Height above spring: 0.5 m
- Speed: 0
- $K_i = 0$
- $U_i = mgh = (0.2)(9.8)(0.5) = 0.98 \, \text{J}$

At maximum compression (distance $d$ below the spring's natural length):
- Height: $-d$ (negative because below reference)
- Speed: 0 (turning point)
- $K_f = 0$
- $U_f = mg(-d) + \frac{1}{2}kd^2 = -0.2(9.8)d + \frac{1}{2}(100)d^2 = -1.96d + 50d^2$

By conservation:

$$0.98 = -1.96d + 50d^2$$

$$50d^2 - 1.96d - 0.98 = 0$$

Using the quadratic formula:

$$d = \frac{1.96 \pm \sqrt{(1.96)^2 + 4(50)(0.98)}}{2(50)} = \frac{1.96 \pm \sqrt{3.84 + 196}}{100} = \frac{1.96 \pm 14.14}{100}$$

Taking the positive root:

$$d = \frac{16.1}{100} = 0.161 \, \text{m} \approx 16 \, \text{cm}$$

The spring compresses 16 centimeters. Again: no force analysis, no friction, no complicated dynamics. Just potential energies and algebra.

---

## Concept 3 — Potential Energy Diagrams and Stability

A graph of potential energy $U(x)$ versus position $x$ is one of the most useful tools in mechanics. It shows not only where motion is allowed, but also where the motion is stable, where it is unstable, and where turning points occur.

### Reading the Diagram: Allowed Regions and Turning Points

On a potential energy diagram, draw a horizontal line at the height $E$ (the total mechanical energy). The region where the curve $U(x)$ is *below* the line $E$ is where motion is allowed — kinetic energy is non-negative there. The region where $U(x)$ is *above* $E$ is forbidden — kinetic energy would be negative, which is impossible.

At the intersection of the curve and the line ($U = E$), kinetic energy is zero. The particle momentarily stops. It is a turning point. If the curve goes higher on both sides, the particle bounces back. If the curve permits higher energy on one side, the particle escapes.

For gravity near Earth's surface, $U(y) = mgy$ is a straight line. Draw the line at some energy $E$. The particle can only rise to height $y_{\max} = E / (mg)$ and no higher.

For a spring, $U(x) = \frac{1}{2}kx^2$ is a parabola. The particle oscillates between $-x_{\max}$ and $+x_{\max}$, where $x_{\max} = \sqrt{2E/k}$.

### Equilibrium and Stability

At a point where $\frac{dU}{dx} = 0$, the force is zero: $F = -\frac{dU}{dx} = 0$. This is an equilibrium point. The particle can rest there — it has no tendency to move. But is the equilibrium stable or unstable?

A stable equilibrium is one where, if the particle is displaced slightly, the force pushes it back toward equilibrium. On a diagram, this occurs at a *minimum* of the potential energy curve — a valley. If the particle is slightly to the left of the valley bottom, the slope is negative, so $F = -\frac{dU}{dx}$ is positive, pushing it rightward, back toward the bottom. If it's slightly to the right, the slope is positive, so $F$ is negative, pushing it leftward. Either way, the force restores equilibrium.

An unstable equilibrium is one where a small displacement triggers a force that pushes the particle further away — over a hill on the diagram, a *maximum* of potential energy. If the particle sits at the hilltop and is nudged left, the slope is positive to the left, so $F$ is negative, pushing it further left, away from the top. Unstable.

For the spring, the minimum at $x = 0$ is stable — the spring pulls the mass back to equilibrium. For a ball balanced on the tip of a cone, the apex is an unstable equilibrium. Any tiny nudge causes the ball to roll down.

### Oscillation About a Minimum

If a particle is released near a minimum of the potential energy curve with energy only slightly above the minimum, it will oscillate back and forth between the two turning points, like a mass on a spring or a pendulum at small amplitude. The deeper and narrower the potential well, the faster the oscillation. The particle cannot escape the well unless its energy exceeds the rim height.

### A Quartic Double-Well Potential

Consider the potential $U(x) = 2(x^4 - x^2)$ with total energy $E = -0.25 \, \text{J}$.

First, find equilibrium points: $\frac{dU}{dx} = 2(4x^3 - 2x) = 8x(x^2 - 1/2) = 0$, giving $x = 0$ and $x = \pm 1/\sqrt{2} \approx \pm 0.707 \, \text{m}$.

Check stability with the second derivative: $\frac{d^2U}{dx^2} = 24x^2 - 4$.
- At $x = 0$: $\frac{d^2U}{dx^2} = -4 < 0$ — unstable (maximum).
- At $x = \pm 0.707$: $\frac{d^2U}{dx^2} = 24(0.5) - 4 = 8 > 0$ — stable (minima).

With $E = -0.25 \, \text{J}$, the particle can only move in two separate regions: one near $x = +0.707$ and another near $x = -0.707$. It oscillates within one well and can never escape to the other. This is a confined system — like an electron in a double-well potential in quantum mechanics, or a ball rolling in a double-dip valley that's too high to escape from.

If energy were raised to $E = +0.25 \, \text{J}$, the particle could move in the outer regions, far from equilibrium, oscillating with larger amplitude.

### Trade-off: Diagram Power and Dimension Limitation

Potential energy diagrams are maximally useful in one dimension. You can plot $U$ vs. $x$ and see everything: allowed regions, turning points, stable and unstable equilibrium, the speed at any position (from $K = E - U$). In two or three dimensions, you'd need a 3D or 4D plot, which is cumbersome.

The limitation: diagrams don't tell you the *time* evolution. They show where the particle can go, but not when. To find how long it takes to oscillate, you need calculus, not just the picture.

### Worked Example: Reading a Double-Well Diagram

The potential $U(x) = 2(x^4 - x^2)$ has two wells. With $E = -0.25 \, \text{J}$:

**(a) Find the turning points and allowed regions.**

At turning points, $U(x) = E$:

$$2(x^4 - x^2) = -0.25$$
$$x^4 - x^2 + 0.125 = 0$$

Let $y = x^2$:

$$y^2 - y + 0.125 = 0$$
$$y = \frac{1 \pm \sqrt{1 - 0.5}}{2} = \frac{1 \pm 0.707}{2}$$

So $y = 0.854$ or $y = 0.146$, giving $x = \pm 0.924$ or $x = \pm 0.382$.

The allowed regions are $-0.924 \leq x \leq -0.382$ and $0.382 \leq x \leq 0.924$.

**(b) In which well is the particle faster: the left or the right?**

At the stable equilibrium $x = 0.707$, the potential is:

$$U(0.707) = 2((0.707)^4 - (0.707)^2) = 2(0.25 - 0.5) = -0.5 \, \text{J}$$

The kinetic energy there is $K = E - U = -0.25 - (-0.5) = 0.25 \, \text{J}$.

By symmetry, at $x = -0.707$, the kinetic energy is also $0.25 \, \text{J}$.

The speeds are equal. (This is always true for symmetric potentials.)

---

## Integration: The Roller Coaster Revisited

Return to the roller coaster. The car enters the first descent at $h = 45 \, \text{m}$ with speed $v = 0$. At the base, it has speed $v_1$. At the top of the next hill, $h = 40 \, \text{m}$, it has speed $v_2$.

Ignoring friction and air drag:

$$mg(45) + 0 = mg(40) + \frac{1}{2}mv_2^2$$

$$v_2 = \sqrt{2g(45 - 40)} = \sqrt{2(9.8)(5)} = \sqrt{98} = 9.9 \, \text{m/s}$$

The car climbs a 35-meter hill:

$$mg(40) + \frac{1}{2}mv_2^2 = mg(35) + \frac{1}{2}mv_3^2$$

$$v_3 = \sqrt{2g(40 - 35) + v_2^2} = \sqrt{2(9.8)(5) + 98} = \sqrt{196} = 14 \, \text{m/s}$$

But if friction steals 130 kilojoules over the entire route, then the mechanical energy at the end is lower, and the car comes to rest on a hill of height $h_{\text{final}}$ where:

$$mg \cdot 45 = mg \cdot h_{\text{final}} + 130,000$$

$$(1,000)(9.8)(45) = (1,000)(9.8) h_{\text{final}} + 130,000$$

$$441,000 = 9,800 h_{\text{final}} + 130,000$$

$$h_{\text{final}} = \frac{311,000}{9,800} = 31.7 \, \text{m}$$

The car stops at a height of 31.7 meters — partway up some hill — instead of looping through the idealized track forever. This is reality. The energy method shows us not just the ideal motion but also the cost of dissipation.

---

## Graduated Exercises

### Warm-up

**Exercise 9.1** A 10 kg block is lifted 2 meters above its initial position. How much gravitational potential energy does it gain? (Take $g = 10 \, \text{m/s}^2$ for easy arithmetic.)

**Exercise 9.2** A spring with spring constant $k = 200 \, \text{N/m}$ is compressed by 0.1 meters from its natural length. How much elastic potential energy does it store?

**Exercise 9.3** A ball is dropped from rest from a height of 5 meters. Using only energy conservation (no kinematics equations), find its speed just before it hits the ground.

### Application

**Exercise 9.4** A 0.5 kg block slides down a frictionless incline of height 3 meters. At the bottom, a spring with $k = 100 \, \text{N/m}$ brings it to rest by compressing an unknown distance $d$. Find $d$.

**Exercise 9.5** A pendulum bob of mass 2 kg swings from an initial angle of 60° (from vertical, string length 1 meter). Use energy conservation to find its speed at the lowest point. (Hint: use $h = L(1 - \cos\theta)$ for the height above the lowest point.)

**Exercise 9.6** A 100 kg person climbs stairs up 4 meters in 5 seconds. How much gravitational potential energy do they gain? How much average power (in watts) did they expend?

### Synthesis

**Exercise 9.7** A roller coaster car (mass 500 kg) starts from rest at the top of a 30-meter hill, descends, and then climbs a 20-meter hill on the other side. Assume no friction. At the top of the second hill, what is the car's speed?

**Exercise 9.8** A spring gun fires a 0.02 kg projectile horizontally. The spring constant is 500 N/m and the spring is compressed 0.05 meters. Find the projectile's initial speed. (All the elastic potential energy converts to kinetic energy.)

**Exercise 9.9** A 2 kg mass oscillates on a spring with $k = 200 \, \text{N/m}$. If the mass is released from rest when the spring is compressed by 0.1 meters, what is its maximum speed and where does it occur?

### Challenge

**Exercise 9.10** A ball is thrown straight up from ground level with initial kinetic energy $K_0 = 100 \, \text{J}$. At what height is the kinetic energy exactly half the initial value? (The answer should not depend on the ball's mass.)

**Exercise 9.11** A particle moves in one dimension under the potential $U(x) = x^2 - 4x + 3$ (energy in joules, position in meters). (a) Find the equilibrium point. (b) Is it stable or unstable? (c) If the particle has total energy $E = 1 \, \text{J}$, what are the turning points?

---

## Chapter Summary

Potential energy is a storage mechanism. When a conservative force does work on an object, that work gets encoded into the object's position relative to the source of the force — its height above ground, its distance from a magnet, the compression of a spring. The potential energy at a later time can be released as kinetic energy.

The gravitational potential energy near Earth's surface is $U = mgy$, proportional to height. The elastic potential energy of an ideal spring is $U = \frac{1}{2}kx^2$, proportional to the square of the displacement.

In a closed system with only conservative forces, mechanical energy is conserved: $E = K + U = \text{constant}$. This turns complicated dynamics problems into algebraic ones. You don't need to integrate equations of motion. You just set the initial energy equal to the final energy and solve.

Potential energy diagrams show, at a glance, where motion is forbidden, where turning points occur, and where equilibrium points are stable or unstable. A minimum on the diagram is a stable equilibrium; a maximum is unstable.

The limitation: this method works only when dissipative forces are absent or negligible, or when their work can be accounted for separately. In the real world, friction and air drag are always present, and they slowly drain the mechanical energy into heat.

**What would change my mind:** If I found a system in which a force obeyed all the criteria for being conservative — path independence, zero work around a closed loop, derivable from a single potential function — yet the energy $K + U$ was not conserved in an isolated system, I would have to reconsider the definition of mechanical energy or the universality of conservation laws.

**Still puzzling:** Why does the quadratic form of spring potential energy lead to such different behavior than the linear form of gravity? The answer lies in the second derivative — it determines the frequency of oscillation — but I still find it striking that a simple change in the power law (from $x$ to $x^2$) rewrites the entire motion.

---

## Tags

#potential-energy, #conservation-of-energy, #conservative-forces, #spring-force, #gravitational-field, #work-energy-theorem, #stable-equilibrium, #energy-diagrams, #mechanics

---

**Byline:** Nik Bear Brown

**Authors' note:** This chapter was drafted for review and does not represent a final publication. Every claim about the physics is grounded in working examples; every example has been calculated or verified. The chapter assumes concurrent study of calculus and is part of a calculus-based introductory physics sequence.


---

## LLM Exercise — Chapter 9: Conservation of Energy Verification

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Potential-energy bookkeeping for conservative forces, total mechanical energy tracking, and empirical verification of conservation — including identification of where conservation breaks (non-conservative forces, integration error).

**Tool:** Claude Code.

**The prompt:**

```
Chapter 9 task in the physics-simulation-toolkit. The chapter
distinguished conservative forces (which admit a potential energy)
from non-conservative ones. Add potential-energy bookkeeping and
verify total mechanical energy conservation on the toolkit's
scenarios.

In `chapters/ch09_energy_conservation/`:

1. `simulations.py`:
   - `class PotentialEnergy` — base class with `compute(body)` →
     potential energy of the body.
   - `GravitationalPE(g_vec=(0, -9.81, 0), reference_height=0)` —
     $U = mgh$ near the surface.
   - `SpringPE(body_id_a, body_id_b, rest_length, k)` —
     $U = \frac{1}{2}k(|\vec{r}_{ab}| - L_0)^2$.
   - `total_mechanical_energy(system, potentials)` — sum of kinetic
     and potential energies over all bodies.
   - `is_conservative(force, n_samples=100)` — sample-based test:
     compute work along several closed paths between two points; if
     they all agree, the force is conservative within tolerance.

2. `test_simulations.py`:
   - Projectile no-drag (Ch 5): total mechanical energy conserved to
     within integrator precision throughout flight.
   - Spring oscillator (Ch 6 Spring with no drag): energy conserved.
     Plot K(t) and U(t) — they should be complementary, summing to a
     constant.
   - Pendulum (use a Spring at small displacement, or Ch 17 will do
     it properly): energy conserved.
   - Projectile *with* drag (Ch 5): energy *not* conserved; the
     mechanical-energy decrease equals the work done by drag
     (negative work, energy out of the system).
   - Inclined plane *with* friction (Ch 7): same — energy decreases
     by $\mu_k N s$.

3. `benchmarks.py` — for the spring oscillator, run RK4 with several
   timestep sizes (dt = T/10, T/100, T/1000, T/10000). Plot total
   mechanical energy versus time. Energy drift should decrease
   strongly with dt. For semi-implicit Euler, energy *oscillates*
   around the truth but does not drift secularly — show this on the
   plot.

4. `README.md` — decision cards. "Surprising findings": the
   contrast between explicit Euler (energy drifts up secularly),
   symplectic Euler (energy oscillates but bounded), and RK4 (energy
   conserved to high precision but not exactly). This is the
   foundational empirical observation behind symplectic integrators
   for orbital and Hamiltonian systems.

Commit as `ch09: conservation of mechanical energy verified with
integrator comparison`.
```

**What this produces:** Potential-energy bookkeeping, four scenarios verifying energy conservation, two scenarios identifying where conservation breaks (with quantified breaking), and an integrator comparison plot that motivates symplectic methods.

**How to adapt this prompt:**

- *For your own project:* Symplectic integrators are standard in orbital mechanics and molecular dynamics specifically because of the long-term energy behavior demonstrated here.
- *For ChatGPT / Gemini:* Both work.
- *For Claude Code:* Native fit. Let it generate the K(t), U(t) complementary plot — it's pedagogically beautiful.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 8 kinetic energy bookkeeping and the Ch 6–7 force scenarios.

**Preview of next chapter:** Chapter 10 introduces momentum and collisions — including the elastic/inelastic distinction and the rocket equation simulated from first principles.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Emmy Noether** was the 1918 theorem (Noether's theorem) establishing that every continuous symmetry of a physical system corresponds to a conservation law — translational symmetry to momentum, rotational symmetry to angular momentum, time-translation symmetry to energy — the mathematical foundation of all conservation laws in modern physics — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Emmy Noether, and how does their work on Noether's theorem and the symmetry-conservation correspondence connect to the conservation of energy and conservation laws in general? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Emmy Noether"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Noether's theorem on one specific symmetry — for example, time-translation invariance of the Lagrangian — and show how energy conservation follows
- Ask: "Noether worked at Göttingen without pay, then without title, then was expelled in 1933 for being Jewish. What were the institutional obstacles, and what did Hilbert say to defend hiring her?"
- Add the constraint: "Answer in the form of a Lagrangian-mechanics derivation that an undergraduate could verify — symmetry on the left, conservation law on the right"

What changes? What gets better? What gets worse?
