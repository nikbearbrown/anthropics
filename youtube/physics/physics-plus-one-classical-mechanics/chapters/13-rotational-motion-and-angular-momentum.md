# Chapter 13 — Rotational Motion and Angular Momentum

*The same mechanics, turned sideways.*

---

## A figure skater at the World Championships, March 2010

Yu-Na Kim of South Korea is in the middle of her free skate at the 2010 Winter Olympics in Vancouver. She is in a high-speed combination spin. Arms outstretched, leg extended — slow, graceful rotation, maybe two revolutions per second. Then she pulls her arms tightly into her chest and brings her free leg in close to her body. She accelerates. Within a second she is rotating much faster — perhaps four or five revolutions per second — fast enough that her face becomes a blur on television.

She did not push against anything. No external torque acted on her (ice friction is small enough to ignore over the second of the maneuver). Yet her angular velocity changed dramatically. Where did the angular acceleration come from?

The answer is conservation of angular momentum. By pulling her arms in, she reduced her **moment of inertia** $I$ — the rotational analog of mass, which measures how the mass of her body is distributed relative to her spin axis. Mass close to the axis contributes less to $I$ than mass far from it. Pulling her arms in moved mass closer to the axis; $I$ dropped. Because angular momentum $L = I\omega$ is conserved, when $I$ shrinks, $\omega$ must grow proportionally. The product stays constant.

<!-- → [DIAGRAM: two silhouettes of a figure skater side by side — left: arms and leg extended (slow spin, large I, slow ω, annotated I_i = 4.0 kg·m², ω_i = 1.5 rev/s); right: arms pulled in, leg tucked (fast spin, small I, fast ω, annotated I_f = 1.0 kg·m², ω_f = 6.0 rev/s); draw horizontal arrows indicating the axis of rotation through the head-to-toe line; annotate L = Iω = constant on both panels; caption: "same angular momentum, one-quarter the moment of inertia, four times the spin rate"] -->

This is the same principle that makes a tornado spin up as it tightens, the same principle that governs why neutron stars rotate hundreds of times per second. The story of this chapter is that every piece of linear mechanics — position, velocity, mass, force, momentum, kinetic energy, conservation laws — has an exact rotational analog. The structure is identical. Only the symbols change.

---

## The rotational vocabulary

Before the physics, the language.

For an object rotating about a fixed axis, the angle $\theta$ plays the role of position, angular velocity $\omega$ plays the role of velocity, and angular acceleration $\alpha$ plays the role of linear acceleration. A point at distance $r$ from the axis has:

$$s = r\theta \quad \text{(arc length)}, \qquad v = r\omega \quad \text{(tangential speed)}, \qquad a_t = r\alpha \quad \text{(tangential acceleration)}.$$

There is also the centripetal acceleration from Chapter 6, $a_c = v^2/r = r\omega^2$, pointing inward, which exists even when nothing is speeding up or slowing down — it's responsible for changing the *direction* of the velocity. A point on a spinning object has both: tangential (changing speed) and centripetal (changing direction), perpendicular to each other, with total magnitude $\sqrt{a_t^2 + a_c^2}$.

For constant angular acceleration $\alpha$, the kinematic equations are exactly the Chapter 3 equations with $\theta$, $\omega$, $\alpha$ replacing $x$, $v$, $a$:

$$\omega = \omega_0 + \alpha t,$$

$$\theta = \theta_0 + \omega_0 t + \tfrac{1}{2}\alpha t^2,$$

$$\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0).$$

The natural unit for angle is the **radian** — defined as arc length divided by radius. This makes $s = r\theta$ exact with no conversion factor. One full revolution is $2\pi$ radians. One radian is about $57.3°$. When you see RPM in a physics problem, convert to rad/s immediately: $1 \text{ rev/s} = 2\pi \text{ rad/s}$.

A motorcycle wheel of radius $0.30 \text{ m}$ accelerates from rest to $30 \text{ m/s}$ (the wheel's rim speed, equal to the bike's road speed) in $5 \text{ s}$. At the end, $\omega = v/r = 30/0.30 = 100 \text{ rad/s}$. Angular acceleration: $\alpha = 100/5 = 20 \text{ rad/s}^2$. Angle turned through: $\theta = \tfrac{1}{2}\alpha t^2 = \tfrac{1}{2}(20)(25) = 250 \text{ rad} \approx 40 \text{ rev}$. You didn't need a new formula for any of that — just Chapter 3 with new symbols.

<!-- → [TABLE: two-column side-by-side display of the linear (Chapter 3) and rotational kinematic equations — row 1: v = v₀ + at | ω = ω₀ + αt; row 2: x = x₀ + v₀t + ½at² | θ = θ₀ + ω₀t + ½αt²; row 3: v² = v₀² + 2aΔx | ω² = ω₀² + 2αΔθ; at the bottom, the motorcycle wheel worked example with all steps; caption: "the same three equations — only the variable names changed"] -->

---

## Torque and moment of inertia

Linear dynamics: $F_\text{net} = ma$. Net force equals mass times acceleration.

Rotational dynamics: $\tau_\text{net} = I\alpha$. Net torque equals moment of inertia times angular acceleration.

**Torque** is what makes things rotate. From Chapter 9: $\tau = rF\sin\theta$, where $r$ is the distance from the pivot to where the force is applied, $F$ is the force magnitude, and $\theta$ is the angle between the force vector and the lever arm. Maximum torque when force is perpendicular to the lever arm ($\sin 90° = 1$); zero torque when force is parallel to it ($\sin 0° = 0$). This is why you push a door near the edge, not the hinge.

**Moment of inertia** $I$ is the rotational analog of mass. But where mass is a single number for an object, moment of inertia depends on how the mass is *distributed* relative to the rotation axis:

$$I = \sum_i m_i r_i^2.$$

Each piece of mass $m_i$ at distance $r_i$ from the axis contributes $m_i r_i^2$. Mass close to the axis barely contributes; mass far from the axis contributes quadratically. This is why the skater's arms matter so much — they are the farthest mass from her spin axis.

For simple shapes with uniform density:

| Shape | Axis | $I$ |
|---|---|---|
| Solid disk or cylinder | Through center | $\tfrac{1}{2}MR^2$ |
| Hoop or thin-walled cylinder | Through center | $MR^2$ |
| Solid sphere | Through center | $\tfrac{2}{5}MR^2$ |
| Thin rod | Through center | $\tfrac{1}{12}ML^2$ |
| Thin rod | Through end | $\tfrac{1}{3}ML^2$ |

Notice the disk versus the hoop: same mass $M$, same radius $R$, but $I_\text{disk} = \tfrac{1}{2}MR^2$ while $I_\text{hoop} = MR^2$. The hoop's mass is all at maximum distance from the axis; the disk's mass is spread throughout the interior, averaging to half the rim distance squared. When you roll a disk and a hoop of the same mass and radius down a ramp, the disk wins — it has less rotational inertia to spin up, so it converts more of the gravitational potential energy into useful translational motion.

<!-- → [DIAGRAM: two cross-sections side by side — left: solid disk with mass spread across the full interior, each annular ring labeled with its r_i contribution to I; right: hoop with all mass concentrated at the outer radius R; below each, show the resulting I formula; caption: "same total mass, same outer radius — but where the mass lives changes everything; the hoop has twice the moment of inertia of the disk"] -->

A playground merry-go-round, approximated as a solid disk: $M = 200 \text{ kg}$, $R = 1.5 \text{ m}$. Moment of inertia:

$$I = \tfrac{1}{2}(200)(1.5)^2 = 225 \text{ kg·m}^2.$$

A child pushes tangentially at the rim with $50 \text{ N}$. Torque: $\tau = RF = (1.5)(50) = 75 \text{ N·m}$. Angular acceleration:

$$\alpha = \frac{\tau}{I} = \frac{75}{225} \approx 0.33 \text{ rad/s}^2.$$

In thirty seconds of steady pushing, the merry-go-round spins up to about $10 \text{ rad/s} \approx 95 \text{ RPM}$. Unrealistically fast for a real merry-go-round (friction and the children's weight slow it considerably), but the order of magnitude is right for the idealized problem.

Two misconceptions to clear immediately. First: moment of inertia is not just the mass — it depends on both mass and geometry. Two objects of equal mass can have very different $I$ if their shapes differ. Second: $I$ changes with the axis. A thin rod spun about its center ($I = \tfrac{1}{12}ML^2$) is four times easier to spin than the same rod spun about its end ($I = \tfrac{1}{3}ML^2$). The axis is not optional information.

---

## Rotational kinetic energy

A rotating body has kinetic energy — the energy of all its mass elements moving in circles. Add up $\tfrac{1}{2}m_i v_i^2$ for every piece, substitute $v_i = r_i \omega$, and the sum becomes:

$$KE_\text{rot} = \tfrac{1}{2}I\omega^2.$$

Exactly parallel to $KE = \tfrac{1}{2}mv^2$, with $I$ replacing $m$ and $\omega$ replacing $v$.

An object that is rolling without slipping — a wheel, a ball, a cylinder — has both translational and rotational kinetic energy simultaneously:

$$KE_\text{total} = \tfrac{1}{2}Mv^2 + \tfrac{1}{2}I\omega^2.$$

The rolling constraint ($v = R\omega$ for no slipping) links the two. For a given total energy (say, from rolling down a height $h$), the split between translational and rotational depends on the shape. For a sliding block (no rotation): all energy goes to $\tfrac{1}{2}Mv^2$, giving $v = \sqrt{2gh}$. For a solid disk: $KE_\text{rot}/KE_\text{trans} = (I/MR^2)/1 = (\tfrac{1}{2}MR^2/MR^2) = \tfrac{1}{2}$, so only $\tfrac{2}{3}$ of the energy goes to translation, giving $v = \sqrt{\tfrac{4}{3}gh}$. For a hoop: the ratio is $1$, so only half the energy goes to translation, giving $v = \sqrt{gh}$. The rolling race: sliding block $>$ solid sphere $>$ solid disk $>$ hoop. Shape alone determines the order; mass and radius cancel.

<!-- → [CHART: inclined ramp with four objects at the top — sliding block, solid sphere, solid disk, hoop — and their finishing positions at the bottom shown as a ranked result; annotate each with its speed formula (v = √(2gh), v = √(10gh/7), v = √(4gh/3), v = √(gh)) and the fraction of energy going to rotation (0%, 29%, 33%, 50%); caption: "more energy locked in rotation → slower translation — shape, not mass or size, decides the race"] -->

---

## Angular momentum and its conservation

Every moving mass has linear momentum $p = mv$. Every rotating body has **angular momentum**:

$$L = I\omega.$$

Units: $\text{kg·m}^2/\text{s}$. Direction: along the rotation axis (right-hand rule — curl the fingers of your right hand in the direction of rotation; your thumb points along $L$).

The rotational form of Newton's second law is:

$$\tau_\text{net} = \frac{\Delta L}{\Delta t}.$$

Exactly parallel to $F_\text{net} = \Delta p / \Delta t$. If no external torque acts: $\Delta L = 0$, so $L$ is constant. This is **conservation of angular momentum**: in the absence of external torques, the total angular momentum of a system does not change.

$$L_i = L_f \quad \implies \quad I_i \omega_i = I_f \omega_f.$$

Now the skater. Arms extended: $I_i = 4.0 \text{ kg·m}^2$, $\omega_i = 1.5 \text{ rev/s}$. Arms pulled in: $I_f = 1.0 \text{ kg·m}^2$. No external torque. So:

$$(4.0)(1.5) = (1.0)\omega_f \implies \omega_f = 6.0 \text{ rev/s}.$$

She quadruples her spin rate when she reduces her moment of inertia by a factor of four.

Now check the kinetic energy. Before: $KE_i = \tfrac{1}{2}(4.0)(2\pi \times 1.5)^2 \approx 178 \text{ J}$. After: $KE_f = \tfrac{1}{2}(1.0)(2\pi \times 6.0)^2 \approx 711 \text{ J}$. The kinetic energy *quadrupled*. Where did the extra energy come from? Her muscles. She did work pulling her arms inward against the dynamics of the rotating system — and that work appears as additional kinetic energy. Angular momentum is conserved; energy is not (it came from a biological source). These are two independent accounting systems, and they give different answers here for a good reason.

<!-- → [CHART: two-panel bar chart for the skater — left panel: I (bars at 4.0 and 1.0 kg·m²) and ω (bars at 1.5 and 6.0 rev/s) before and after, showing L = Iω constant (same product = 6.0 in both); right panel: KE before (178 J) and after (711 J), showing KE quadrupled; annotate: "L conserved — same total" on left; "KE increased — muscles did work" on right; caption: "two independent books: angular momentum stays flat; kinetic energy rises because work was done"] -->

Now the pulsar. In 1054 AD, Chinese and Arab astronomers recorded a sudden bright "guest star" — what we now know was a supernova in Taurus. At its center today sits the **Crab Pulsar**: a neutron star, roughly $1.4$ solar masses compressed into a sphere of radius $\sim 10 \text{ km}$, rotating about $30$ times per second. We know because it pulses — each rotation sweeps a beam of radio emission across Earth, and we detect $30$ pulses per second.

The progenitor star, before collapse, had a radius of perhaps $7 \times 10^8 \text{ m}$ and rotated perhaps once per month. When the core collapsed to $10^4 \text{ m}$, the moment of inertia (scaling as $R^2$) shrank by a factor of roughly $(7 \times 10^8 / 10^4)^2 = 5 \times 10^9$. Conservation of angular momentum requires $\omega$ to grow by the same factor. One rotation per month becomes one rotation per $\sim 0.5 \text{ μs}$ — actually faster than observed, which is consistent with angular momentum being partially carried away by the explosion's ejecta. The rough calculation is right.

This is not a coincidence of scale. The same formula — $I_i \omega_i = I_f \omega_f$ — that describes the skater's spin-up describes the formation of pulsars. The physics doesn't care about the size of the system. It cares about whether external torques act. When they don't, angular momentum is conserved, from a figure skater's arms to a collapsing stellar core.

<!-- → [INFOGRAPHIC: two-panel scale comparison — left: Sun-size progenitor star (radius ~7×10⁸ m, rotation period ~1 month, I large) collapsing with inward arrows; right: neutron star result (radius ~10⁴ m, rotation period ~33 ms, I reduced by 5×10⁹); connect the two with L = Iω = constant; annotate the factor-of-5×10⁹ reduction in I and corresponding increase in ω; caption: "the same formula at 40 orders of magnitude of difference in angular momentum"] -->

---

## The parallel table

Every quantity and equation in linear mechanics has a rotational counterpart:

| Linear | Rotational |
|---|---|
| Position $x$ | Angle $\theta$ |
| Velocity $v$ | Angular velocity $\omega$ |
| Acceleration $a$ | Angular acceleration $\alpha$ |
| Mass $m$ | Moment of inertia $I$ |
| Force $F$ | Torque $\tau$ |
| $F = ma$ | $\tau = I\alpha$ |
| Momentum $p = mv$ | Angular momentum $L = I\omega$ |
| Kinetic energy $\tfrac{1}{2}mv^2$ | Rotational KE $\tfrac{1}{2}I\omega^2$ |
| Conservation of $p$ (no $F_\text{ext}$) | Conservation of $L$ (no $\tau_\text{ext}$) |

This is not an analogy — it is a derivation. Rotational quantities are exactly what you get when you apply the linear quantities to a collection of point masses constrained to move in circles around a common axis. The algebra of $\sum m_i r_i^2$ is why $I$ appears where $m$ appeared; the algebra of $\sum m_i r_i^2 \omega$ is why $L = I\omega$ plays the role that $p = mv$ played.

The conservation laws are independent. Angular momentum can be conserved while linear momentum is not (a spinning top on a rough floor loses linear momentum to friction but, approximately, keeps angular momentum). Linear momentum can be conserved while angular momentum is not (two particles flying past each other, one deflected, change their angular momenta about any external point while keeping total linear momentum fixed). They are separate symmetries of nature — translational invariance gives linear momentum conservation; rotational invariance gives angular momentum conservation. Noether's theorem (which we meet in the AI Wayback Machine below) makes this precise.

The scale range of the conservation law is one of the most striking things about it. An ice skater's angular momentum as she spins: roughly $10 \text{ kg·m}^2/\text{s}$. Earth's rotational angular momentum: $7 \times 10^{33} \text{ kg·m}^2/\text{s}$. The Crab Pulsar's: somewhere around $10^{40} \text{ kg·m}^2/\text{s}$. The same algebra. The same conservation law. Across forty orders of magnitude, the product $I\omega$ is what stays fixed when no external torques act.

<!-- → [INFOGRAPHIC: vertical logarithmic scale showing angular momentum values — rungs: spinning top (~10⁻³ kg·m²/s), figure skater (~10 kg·m²/s), bicycle wheel in motion (~1 kg·m²/s), Earth's daily rotation (~7×10³³ kg·m²/s), Crab Pulsar (~10⁴⁰ kg·m²/s); annotate each rung with what system it is and its approximate L; caption: "the same conservation law — L = Iω = const when τ_ext = 0 — across 43 orders of magnitude"] -->

---

## Exercises

### Warm-up

**13.1** A wheel of radius $0.40 \text{ m}$ rotates at $20 \text{ rad/s}$. (a) What is the linear speed of a point on the rim? (b) What is its angular velocity in RPM?

**13.2** A flywheel accelerates from $10 \text{ rad/s}$ to $30 \text{ rad/s}$ in $5.0 \text{ s}$. (a) Angular acceleration? (b) Angle turned through in those $5$ seconds?

**13.3** A solid disk of mass $5.0 \text{ kg}$ and radius $0.30 \text{ m}$ is acted on by a torque of $10 \text{ N·m}$ applied at the rim. What is its angular acceleration?

**13.4** A spinning ice skater has $I = 5.0 \text{ kg·m}^2$ and $\omega = 4.0 \text{ rad/s}$. What is her angular momentum?

### Application

**13.5** A solid sphere of mass $2.0 \text{ kg}$ and radius $0.10 \text{ m}$ rolls without slipping at $5.0 \text{ m/s}$. Compute (a) translational KE, (b) rotational KE, (c) total KE, (d) fraction in rotation.

**13.6** A solid disk of mass $3.0 \text{ kg}$ and radius $0.50 \text{ m}$ rolls without slipping down a $30°$ incline of height $2.0 \text{ m}$. (a) Use energy conservation to find the speed at the bottom. (b) Compare to a frictionless slide of the same height.

**13.7** A merry-go-round (solid disk, $200 \text{ kg}$, $1.5 \text{ m}$ radius) spins at $1.0 \text{ rad/s}$. A $40 \text{ kg}$ child jumps on at the rim. (a) New angular velocity? (b) How much KE was lost? (c) Where did it go?

**13.8** An astronaut floating in space holds a spinning bicycle wheel ($I = 0.50 \text{ kg·m}^2$, $\omega = 30 \text{ rad/s}$) and inverts it (flips its axis $180°$). The astronaut has $I_\text{astronaut} = 4.0 \text{ kg·m}^2$ about the same axis. What angular velocity does the astronaut acquire?

### Synthesis

**13.9** A car wheel of mass $20 \text{ kg}$ and radius $0.30 \text{ m}$ spins up from rest as the car accelerates from $0$ to $25 \text{ m/s}$ in $8 \text{ s}$ with no slipping. Compute: (a) the angular acceleration, (b) the angular displacement during the acceleration, (c) the moment of inertia (treat as a solid disk), (d) the torque applied to the wheel.

**13.10** A solid disk falls down a string wound around its rim (Maxwell's wheel), mass $0.50 \text{ kg}$, radius $0.20 \text{ m}$. (a) What is the linear acceleration of its center? (b) After falling $1.0 \text{ m}$, what is its translational KE? Rotational KE?

**13.11** A neutron star with mass $1.4$ solar masses and radius $10 \text{ km}$ spins at $30 \text{ Hz}$. (a) Compute its angular momentum (treat as a uniform sphere). (b) The progenitor star had radius $7 \times 10^8 \text{ m}$; what was its rotation period before collapse, assuming angular momentum was conserved?

### Challenge

**13.12** A figure skater holds her arms out, $I = 5 \text{ kg·m}^2$, spinning at $2 \text{ rev/s}$. She pulls her arms in to $I = 1 \text{ kg·m}^2$. Compute (a) her new angular velocity, (b) kinetic energy before and after, (c) the work she did pulling her arms in, (d) verify the work equals the increase in rotational KE.

**13.13** A gyroscope wheel ($I = 0.10 \text{ kg·m}^2$, $\omega = 200 \text{ rad/s}$) is mounted on an axle supported only at one end. The wheel weighs $2.0 \text{ kg}$ and the axle from support to wheel center is $0.20 \text{ m}$. Compute the precession rate $\Omega = MgL/(I\omega)$ in rad/s and in RPM.

---

## LLM Exercise — Chapter 13: Rotational Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** A rotational analysis of one rotating element of your anchor phenomenon, with $I$, $\omega$, $L$, and $KE_\text{rot}$ computed.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 13, I want to apply rotational dynamics — moment of inertia, angular acceleration, angular momentum — to one rotating element of my phenomenon. Please:

1. Identify ONE rotating component in my phenomenon. Examples:
   - Bike commute: the wheel rotation, which has moment of inertia and angular momentum.
   - Coffee maker: a centrifugal pump impeller; a rotating burr grinder.
   - Basketball: the ball's spin during the shot (back-spin or side-spin).
   - Marathon: a runner's swinging arms (modeled as rotating rods).
   - Espresso: a rotating tamper or a spinning piston in the pump.

2. Compute the moment of inertia $I$ using the appropriate formula for the shape (disk, hoop, sphere, rod). State the formula.

3. Compute the angular velocity $\omega$ from the linear velocity (using $v = r\omega$) or from RPM data.

4. Compute the angular momentum $L = I\omega$ and the rotational kinetic energy $KE_\text{rot} = \tfrac{1}{2} I\omega^2$.

5. If a torque is involved (acceleration), compute it from $\tau = I\alpha$.

6. Sanity-check with one Fermi estimate.

7. Identify which assumption (rigid body, no slip, axis through center) is most likely to bite.

8. One sentence on how this connects to Chapter 14 (fluid statics) — fluids don't rotate as rigid bodies, so the moment-of-inertia framework needs modification.

Save the output as logbook/chapter-13-rotation.md.
```

### What this produces

A thirteenth Logbook entry: a rotational-dynamics analysis applied to your phenomenon, often surprising in how much energy is locked up in rotation.

### How to adapt this prompt

- *For phenomena with no obvious rotation* (a vertical pour): treat the curl or vortex of any flowing fluid as quasi-rotational; or examine an oscillating system as rotational about its pivot.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have video of a spinning object, paste frame-time data and let Claude compute angular velocity from frame analysis.

### Connection to previous chapters

Builds directly on Chapter 6 (uniform circular motion). Adds angular acceleration and dynamics. Generalizes Chapters 6 (force), 9 (KE), and 11 (momentum) to rotational form.

### Preview of next chapter

Chapter 14 begins fluids — statics and flow. Fluids don't rotate as rigid bodies (different parts can have different angular velocities); the rotational framework needs extension into vorticity. But the energy and momentum frameworks carry over.

---

## AI Wayback Machine

**Emmy Noether** proved in 1915 that every continuous symmetry of a physical system corresponds to a conservation law — including the connection between rotational symmetry and angular momentum conservation. The theorem is a foundation of modern physics; she was a Jewish woman who could not hold a salaried university position in Germany.

**Run this:**

```
Who was Emmy Noether, and how does Noether's theorem connect to the angular momentum we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Emmy Noether"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what Noether's theorem says about three specific symmetries — time, space, rotation — and the conservation laws each implies.
- Ask it about the institutional barriers Noether navigated as a Jewish woman at Göttingen and Bryn Mawr.

What changes? What gets better? What gets worse?
