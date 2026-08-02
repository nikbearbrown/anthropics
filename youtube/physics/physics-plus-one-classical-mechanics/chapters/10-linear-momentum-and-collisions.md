# Chapter 10 — Linear Momentum and Collisions

*To go forward, throw something backward. The universe keeps the books.*

---

Wright-Patterson Air Force Base, 1947. A General Electric J47 turbojet is bolted to a steel test stand. Fuel lines, instrumentation, strain gauges. The throttle goes to maximum.

Air rushes in the front. Kerosene mixes with it, ignites, expands, and rushes out the back at over 600 meters per second. The strain gauges register a steady forward push of roughly 25,000 newtons — five tons of thrust. The engine is going nowhere. It is bolted to the floor. But it is pushing the test stand forward with five tons of force, and if it were attached to an airframe, it would push that airframe forward too.

The engine has no propeller. It has no paddle wheel or oar to push against the air. It pushes against nothing in the surrounding medium. Where does the force come from?

From the exhaust. The engine is throwing mass backward at 600 meters per second. By Newton's third law, the mass throws the engine forward with equal force. The faster you throw the mass, the bigger the force. The more mass you throw per second, the bigger the force. The surrounding medium is irrelevant — the engine would work in vacuum, as rocket engines do. What matters is only what exits the back.

This is momentum conservation at work. Before ignition, the engine and its fuel have zero net momentum (assuming the test stand is fixed). After any brief interval of burning, the exhaust gases carry momentum backward. The engine — and anything it is attached to — must carry the equal and opposite momentum forward. The books balance. They always balance.

Ten years after this test stand, a rocket built on exactly this principle put *Sputnik 1* into orbit. Same physics. Same conservation law. Different scale.

---

## Momentum and Impulse

Momentum is defined as mass times velocity:

$$\mathbf{p} = m\mathbf{v}.$$

It is a vector — same direction as velocity. Its units are kg·m/s. The momentum of a tennis ball served at 55 m/s is $0.057 \times 55 \approx 3.1$ kg·m/s. The momentum of a 1,500 kg car at highway speed is roughly $4.5 \times 10^4$ kg·m/s. The momentum of the Saturn V rocket on liftoff was on the order of $10^9$ kg·m/s. The quantity scales across thirty orders of magnitude in the same units.

The relationship between momentum and force is Newton's second law in its original form — which is more general than $\mathbf{F} = m\mathbf{a}$:

$$\mathbf{F}_{\text{net}} = \frac{d\mathbf{p}}{dt}.$$

For constant mass, $d\mathbf{p}/dt = m \, d\mathbf{v}/dt = m\mathbf{a}$, and we recover $F = ma$. But for a rocket burning fuel — where the mass of the system is decreasing as exhaust exits — the constant-mass form fails. The momentum form is the correct general statement.

Multiply both sides by a time interval $\Delta t$:

$$\mathbf{F}_{\text{net}} \, \Delta t = \Delta\mathbf{p}.$$

The left side is the **impulse** — force times time. The right side is the change in momentum. This is the impulse-momentum theorem: impulse equals change in momentum. It is not a new law; it is Newton's second law with time integrated out.

The practical value of the impulse form is this: you often do not know the detailed force-vs-time profile during a brief collision. What you can measure are the before and after momenta. The impulse is their difference. The average force, if you need it, is that impulse divided by the contact time.

**A worked example.** A 70 kg driver is stopped from 8.3 m/s to rest in a crash. Change in momentum: $70 \times 8.3 = 581$ kg·m/s, in the forward direction. With an airbag, the stop takes about 0.1 s. Average force: $581 / 0.1 = 5{,}810$ N — uncomfortable, survivable. Without an airbag — stopped by the steering column in about 0.01 s — the same change in momentum requires an average force of $581 / 0.01 = 58{,}100$ N. About ten times larger. The same impulse; a tenfold difference in peak force because the time interval is ten times shorter.

This is why airbags work. They extend the stopping time. The momentum change is fixed by physics. The force that delivers it is adjustable — by adjusting how long the change takes. Crumple zones in car bodies do the same thing. The padding in a football helmet does the same thing. The biomechanical principle behind every piece of impact-protection equipment is: increase $\Delta t$ to decrease $F$ for the same $\Delta p$.

---

## Conservation of Momentum

Now the most important result in this chapter. Consider a system of two objects exerting forces on each other — two carts colliding on a track, two billiard balls making contact, a rifle and a bullet at the moment of firing. Newton's third law says the force each object exerts on the other is equal in magnitude and opposite in direction. The impulse each object delivers to the other is therefore equal and opposite. The change in momentum of object 1 is equal and opposite to the change in momentum of object 2. The total change in momentum of the system is zero.

In an isolated system — one with no net external force acting on it — the total momentum does not change:

$$\mathbf{p}_{\text{total},i} = \mathbf{p}_{\text{total},f}.$$

This is the conservation of momentum. It follows directly from Newton's third law applied to internal forces. Internal forces change the momenta of individual objects within the system; they cannot change the total.

"Isolated" is a qualifier that matters. No system in the real world is perfectly isolated — gravity and friction are always acting. But for brief collisions, the impulse from external forces during the contact time is often negligible compared to the impulse from the contact forces themselves. A car crash takes 0.1 s; gravity and friction during that interval deliver tiny impulses compared to the collision forces. Momentum is approximately conserved, and the approximation is very good.

**A worked example: recoil.** A 5.0 kg rifle fires a 0.020 kg bullet at 400 m/s. Before firing, the system is at rest: total momentum zero. After firing:

$$0 = (0.020)(400) + (5.0) v_r.$$

$$v_r = -\frac{(0.020)(400)}{5.0} = -1.6 \text{ m/s.}$$

The rifle recoils at 1.6 m/s backward. The rifle is 250 times heavier than the bullet; it moves 250 times slower. Their momenta are equal and opposite — 8 kg·m/s each — and the total is still zero. The rifle's recoil, the airbag's function, and the jet engine's thrust are all expressions of the same bookkeeping principle: the total stays the same.

The reason the conservation law exists is deeper than Newton's third law. In 1918, Emmy Noether proved that every continuous symmetry of the laws of physics implies a corresponding conservation law. Momentum conservation is the consequence of *translational symmetry* — the laws of physics are the same here as they are over there. If the laws of physics were different at different locations in space, momentum would not be conserved. The conservation law is not an accident; it is the mathematical signature of a symmetry. Energy conservation corresponds to time-translation symmetry — the laws of physics are the same today as they were yesterday. Angular momentum conservation corresponds to rotational symmetry. The three great conservation laws of classical mechanics each encode a different fact about the uniformity of space and time.

---

## Collisions: Elastic and Inelastic

Momentum conservation applies to all isolated-system collisions. Kinetic energy conservation does not. The distinction gives us two categories.

In an **elastic collision**, both momentum and kinetic energy are conserved. Two equations, two unknowns (the final velocities). Closed form. For a 1D elastic collision where object 1 hits a stationary object 2:

$$v_{1f} = \frac{m_1 - m_2}{m_1 + m_2} v_{1i}, \qquad v_{2f} = \frac{2m_1}{m_1 + m_2} v_{1i}.$$

For equal masses: $v_{1f} = 0$, $v_{2f} = v_{1i}$. Object 1 stops dead; object 2 moves off with object 1's original velocity. This is the cue ball on a billiard table, squarely hitting an equal-mass target ball — the cue ball stops, the target rolls. It is also Newton's cradle: drop one ball, one flies out the far end. The result looks surprising until you see that it is the only outcome consistent with both conservation equations simultaneously.

For unequal masses, the formulas reveal the structure. If $m_1 \gg m_2$ (very heavy hits very light): the heavy object barely slows, and the light object launches at approximately $2v_{1i}$ — twice the incoming speed. If $m_1 \ll m_2$ (very light hits very heavy): the light object bounces back at nearly its original speed, and the heavy one barely moves. The bowling ball and the ping-pong ball confirm both limits.

In an **inelastic collision**, momentum is conserved but kinetic energy is not. Some of the kinetic energy converts to heat, sound, and permanent deformation. The energy equation no longer holds — you need a replacement. The simplest case is the **perfectly inelastic collision**, where the objects stick together:

$$(m_1 v_{1i} + m_2 v_{2i}) = (m_1 + m_2) v_f.$$

One equation, one unknown. The kinetic energy lost goes into deformation, heat, and sound — often a large fraction.

For 2D collisions, momentum is conserved along each axis independently:

$$p_{x,i} = p_{x,f}, \qquad p_{y,i} = p_{y,f}.$$

Two equations in 2D. If elastic, the energy equation provides a third. Otherwise, you need geometric information (one of the final angles, typically) to close the system.

**A worked example: 2D inelastic collision.** A 1,000 kg car moving east at 20 m/s collides with a 1,500 kg truck moving north at 15 m/s. They stick together.

Before the collision:
- Car: $p_x = (1000)(20) = 20{,}000$ kg·m/s east, $p_y = 0$.
- Truck: $p_x = 0$, $p_y = (1500)(15) = 22{,}500$ kg·m/s north.

After (combined mass 2,500 kg):
$$v_x = \frac{20{,}000}{2500} = 8.0 \text{ m/s}, \qquad v_y = \frac{22{,}500}{2500} = 9.0 \text{ m/s.}$$

Magnitude: $v = \sqrt{8.0^2 + 9.0^2} = \sqrt{145} \approx 12.0$ m/s.

Direction: $\theta = \tan^{-1}(9.0/8.0) \approx 48°$ north of east.

Kinetic energy before: $\frac{1}{2}(1000)(20)^2 + \frac{1}{2}(1500)(15)^2 = 200{,}000 + 168{,}750 = 368{,}750$ J.

Kinetic energy after: $\frac{1}{2}(2500)(12.0)^2 = 180{,}000$ J.

Energy lost: $188{,}750$ J — just over half the initial kinetic energy, converted to the crumpling of metal, the generation of heat, the sound of impact.

This energy loss is the diagnostic of inelasticity. Real collisions between macroscopic objects — cars, billiard balls, football players — are always at least partially inelastic. Truly elastic collisions exist at the atomic scale, where no permanent deformation is possible, and as an idealization for hard spheres in introductory mechanics. In practice, every collision that makes a sound or leaves a dent is inelastic.

---

## The Rocket Revisited

Return to the test-stand engine. Now we can be precise. Let $M$ be the mass of the rocket at some moment, $v_e$ the exhaust speed relative to the rocket, and $dM/dt$ the rate at which mass is ejected (negative, since mass is leaving). The thrust — the force on the rocket — is:

$$F_{\text{thrust}} = -v_e \frac{dM}{dt}.$$

This follows directly from the momentum form of Newton's second law: the exhaust carries momentum $v_e |dM|$ backward in every interval $dt$; the rocket must gain that same momentum forward.

The rocket equation — how much the rocket can change its velocity by burning all its fuel — integrates this to give Tsiolkovsky's result:

$$\Delta v = v_e \ln\!\left(\frac{m_0}{m_f}\right),$$

where $m_0$ is the initial mass and $m_f$ is the final mass (after burning). The logarithm is what makes spaceflight expensive. To get a large $\Delta v$, you can either increase $v_e$ (better engines) or increase the mass ratio $m_0/m_f$ (more fuel per payload). But carrying more fuel means the fuel itself must also be accelerated at the start — which is why rocket staging exists. Each discarded stage removes dead mass from the system, improving the mass ratio for subsequent burns.

The Saturn V, which put astronauts on the Moon, started with $m_0 / m_f$ ratios that would be impossible as a single stage. Staged, it worked. The rocket equation — derived from the conservation of momentum — told engineers exactly how much staging was needed.

---

## Two Conservation Laws Together

This chapter's conversation partner is Chapter 9 (work and energy). Both are conservation laws. Neither is more fundamental than the other. They answer different questions.

Energy conservation is a scalar law. It tells you about speeds — specifically, that the sum of kinetic and potential energy is constant in conservative systems, and that when it is not, something has been converted to heat. Energy accounting requires expanding the ledger when heat appears.

Momentum conservation is a vector law. It tells you about directions and outcomes after collisions. No ledger expansion needed — momentum does not convert to heat. What goes into the collision as momentum must come out the other side, in the same total direction, no matter what happens internally.

For any 1D elastic collision: two equations (momentum and energy), two unknowns, closed form. For a perfectly inelastic collision: one equation (momentum), one unknown, also closed form. For 2D elastic: three equations, four unknowns — you need one additional geometric constraint. The machinery is systematic, and most collision problems in classical mechanics reduce to identifying which conservation laws apply and counting equations against unknowns.

The power is in what you do not need to know. When a bat hits a baseball, the force during contact varies in a complicated way over the millisecond of contact. The contact deforms both surfaces. The stress propagates through the wood. None of this is necessary for computing the ball's outgoing velocity. You need only the masses, the velocities before, and whether the collision is approximately elastic. The conservation principle bypasses the mechanism entirely.

This is one of the deep structural features of physics: high-level conservation laws let you predict outcomes without understanding the underlying dynamics in detail. It is not that the underlying dynamics are unimportant — they determine whether a collision is elastic or inelastic, and how much energy is lost. But for computing the post-collision velocities given that information, the conservation laws are sufficient, and they are also exact.

---

## What Would Change My Mind

Conservation of momentum has never been observed to fail in an isolated system. Every apparent violation — the missing energy in beta decay (Chapter 31), the anomalous galaxy rotation curves — has been explained by invoking an unobserved participant (the neutrino, dark matter), not by abandoning conservation. If a well-controlled experiment ever showed genuine non-conservation of momentum in an isolated system with no obvious undetected participants, it would mean the translational symmetry of space is broken at some scale — one of the most significant discoveries in the history of physics.

## Still Puzzling

Conservation of momentum holds exactly in any isolated system. But what is the total momentum of the universe? If the universe is finite and closed, the total should be conserved and in some sense defined. If it is infinite, the total is undefined. The cosmological expansion of space complicates things further — in general relativity, momentum conservation becomes local rather than global. The clean Newtonian principle we have been using is an excellent local approximation; at cosmological scales, it requires the full machinery of general relativity to state correctly.

---

## LLM Exercise — Chapter 10: Momentum and Collisions in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A momentum-and-impulse analysis of a key collision or transfer event in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 10, I want to apply momentum conservation and impulse
to one event in my phenomenon involving a transfer of motion or a
collision. Please:

1. Identify ONE collision, impact, or momentum-transfer event.
   Examples:
   - Bike commute: pedaling — each pedal stroke transfers momentum
     from leg to chain to wheels. Or a sudden stop (brake = impulse).
   - Coffee maker: water hitting the puck (impulse on the grounds).
   - Basketball: ball bouncing off the floor; ball-rim collision.
   - Marathon: footstrike — each stride is an impulse from the ground.
   - Espresso: water hitting the puck at 9 bar; water exiting the
     basket as a stream.

2. Set up the momentum conservation. Identify all bodies in the
   "system." Are external forces negligible during the relevant time?

3. Compute the momentum change and the average force from impulse:
   F = Δp / Δt.

4. If the event is a collision, classify it: elastic, partially
   inelastic, or perfectly inelastic. Compute the energy lost.

5. Sanity check with one Fermi estimate.

6. Identify which simplification (negligible external forces, point
   masses, instantaneous transfer) is most likely to bite.

7. One sentence on how this connects to Chapter 11 (statics) —
   when momentum is constant at zero, you have static equilibrium.

Save the output as logbook/chapter-10-momentum.md.
```

### What this produces

A Logbook entry: a momentum analysis of one event in your phenomenon, often revealing forces that are larger than they look.

### How to adapt this prompt

- *For phenomena without obvious collisions* (a steady-state cup of coffee): focus on impulses — the impulse to lift it, the impulse from each sip.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have force-time data (e.g., from a smartwatch accelerometer), import and integrate to get impulse.

### Connection to previous chapters

Builds on Chapter 6 (force) — impulse is force × time. Builds on Chapter 9 (energy) — collisions can lose energy but always conserve momentum. Vector decomposition from Chapter 3 returns for 2D collisions.

### Preview of next chapter

Chapter 11 introduces statics — the special case where total momentum is zero everywhere (nothing is moving) and total torque is zero (nothing is rotating). The analysis that lets us solve dynamic collisions also underlies static structures.

---

## AI Wayback Machine

**Christiaan Huygens** worked out the laws of elastic collisions in 1656 — establishing momentum conservation and the role of vector quantities decades before Newton's *Principia*. His work also produced the first pendulum clock.

**Run this:**

```
Who was Christiaan Huygens, and how does his work on collisions
connect to momentum and collisions covered in this chapter? Keep it
to three paragraphs. End with the single most surprising thing about
his career or ideas.
```

→ Search **"Christiaan Huygens"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Huygens's specific argument for momentum conservation in a two-ball elastic collision.
- Ask it about Huygens's wave theory of light — and the century-long contest with Newton's particle theory.

What changes? What gets better? What gets worse?

---

*Tags: momentum; conservation; collisions; impulse; recoil; elastic; inelastic; rocket*
