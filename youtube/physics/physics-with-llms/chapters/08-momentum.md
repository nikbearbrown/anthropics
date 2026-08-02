# Momentum: The Physics of Collision

**Suggested titles:**
1. Momentum: Why Mass and Speed Both Matter in a Crash
2. Momentum and Impulse: How Collisions Really Work
3. The Unstoppable Force: Understanding Momentum, Impulse, and Collision

**TL;DR:** Momentum is mass in motion—the quantity that tells you how hard it is to stop a moving object. Impulse is the push you apply to change that momentum. In isolated systems, momentum is always conserved: the total before a collision equals the total after, which is why collisions follow predictable rules.

---

## Chapter Opening: Two Players Collide

It is fourth down, the final seconds slipping away, and two American football players sprint toward the same point on the field. One is heavier—280 pounds, running hard at 8 meters per second. The other is faster—200 pounds, moving at 10 meters per second on an intersecting angle. They meet. One player bounces backward, crumpled. The other stumbles forward but keeps his feet. Neither is moving at their pre-collision speed. Both have changed direction.

Watch this moment in slow motion and you see something strange: the heavier player, moving more slowly, did more damage. The lighter player, moving faster, was moved more. This is not intuitive. Your everyday language calls it "force" or "strength," but physics has a more precise word. It sees something the naked eye cannot quite resolve. The difference is not just speed. It is not just mass. It is the *combination* of the two, and it has a name: momentum.

In this chapter, we will learn why the heftier player, despite his slower pace, carried more momentum than the quicker one. We will learn how to calculate momentum and how to predict what happens when moving objects collide. We will learn why collisions between pool balls look different from collisions between cars. And we will learn one of physics' most powerful laws: in a closed system, the total momentum before a collision is always equal to the total momentum after. This law is so reliable that physicists use it to solve problems where they cannot measure individual velocities directly. It is a lens for seeing what is hidden.

**Learning objectives by the end of this chapter:**
- Define momentum and calculate it for moving objects
- Understand how force and time together change momentum
- Apply the impulse-momentum theorem to real collisions
- Explain conservation of momentum in isolated systems
- Distinguish elastic collisions (bouncing) from inelastic collisions (sticking)
- Use conservation of momentum to predict post-collision velocities

**Prerequisites:** You should be comfortable with Newton's laws of motion, particularly the concept of force and acceleration. You should also understand vectors and basic algebra.

---

## Concept 1: Linear Momentum and the Power of Time

### What Momentum Actually Is

In everyday speech, we say someone "has momentum" when they cannot be stopped. A team "loses momentum" when the other side scores. These uses are not wrong; they point at something real. But the word obscures the machinery.

Momentum, in physics, is the product of mass and velocity. Write it this way:

$$\mathbf{p} = m\mathbf{v}$$

where *p* is momentum (we use *p*, not *m*, to avoid confusion with mass), *m* is mass, and *v* is velocity. Momentum is a vector—it has both magnitude and direction. If an object is moving east, its momentum points east. If it reverses direction, the momentum reverses with it.

The SI unit for momentum is kilogram-meters per second, written kg·m/s. It is not a familiar unit, so let's attach a meaning to it. A 2-kilogram ball rolling at 5 m/s has momentum of 10 kg·m/s. A 1-kilogram ball rolling at 10 m/s also has momentum of 10 kg·m/s. Same momentum, different machinery. The first relies on mass; the second relies on velocity.

This is the core trade-off of momentum: you can move a heavy object slowly or a light object quickly and produce the same total momentum. But there is an asymmetry that matters for collisions. Watch what happens when you try to stop each ball. The heavy one, moving slowly, is easy to intercept—you step in front of it, and friction or your shoe absorbs the momentum. The light one, moving quickly, can slip through the same interception. The mass difference affects stopping distance and impact force, even though the momentum is identical.

### How Force and Time Work Together

Momentum does not stay constant by accident. It changes when a force acts on an object. Newton formulated his second law in two ways. Most textbooks write:

$$F_{\text{net}} = ma$$

But Newton's original statement was about momentum. He said: the net external force equals the rate of change of momentum.

$$\mathbf{F}_{\text{net}} = \frac{\Delta \mathbf{p}}{\Delta t}$$

These two equations are not different—they are the same law, written two ways. When mass is constant, the second form simplifies to the first. But the second form is more general and more revealing.

Rearrange it and you get:

$$\Delta \mathbf{p} = \mathbf{F}_{\text{net}} \Delta t$$

The left side is the change in momentum. The right side is force multiplied by time. That product has a name: **impulse**. The equation itself is called the **impulse-momentum theorem**.

Here is where time becomes visible. A large force acting for a short time can produce the same momentum change as a small force acting for a long time. A boxer's punch delivers force for perhaps 10 milliseconds. A safety net catches a falling person and applies a smaller force, but over a longer time—perhaps 1 second. The momentum change can be identical: the impulse is the same, even though the mechanics differ.

This is why padded dashboards in cars save lives. In a crash, your momentum does not magically disappear. The car must apply a force to reverse it. Padding increases the time over which that force acts. A shorter time means a larger force concentrated into a smaller area—bruising, fractures, death. A longer time spreads that force across a larger area over a longer duration—compression, discomfort, survival.

### Worked Example: Venus Williams' Serve

During the 2007 French Open, Venus Williams hit the fastest recorded serve in a women's match: 58 m/s, or about 209 km/h. A tennis ball has mass 0.057 kg. The ball starts at rest (or nearly so) and reaches 58 m/s when it leaves the racquet. It stays in contact with the racquet for about 5 milliseconds.

How much force did the racquet exert on the ball?

Start with impulse:

$$\Delta \mathbf{p} = \mathbf{F}_{\text{net}} \Delta t$$

Calculate the change in momentum:

$$\Delta p = m(v_f - v_i) = (0.057)(58 - 0) = 3.306 \text{ kg·m/s}$$

Now solve for force:

$$F_{\text{net}} = \frac{\Delta p}{\Delta t} = \frac{3.306}{5 \times 10^{-3}} = 661 \text{ N}$$

This is the average force over those 5 milliseconds. For comparison, 661 newtons is about the weight of 67 kilograms (147 pounds) pressing down. The racquet delivered the momentum equivalent of lifting a person half a meter in a single fifth of a second. And it did so across a contact patch perhaps an inch wide.

This is not the most common way to solve for force. You might instead find acceleration and use F = ma. But using impulse reveals what time does: the short contact time is what makes the force so large. If the ball stayed in contact with the racquet for 50 milliseconds instead of 5 milliseconds—a tenfold increase—the force would drop to 66 newtons. Same momentum change, spread over ten times longer, means one-tenth the force.

### Common Misconceptions

**Misconception 1:** "Momentum and kinetic energy are the same thing."

They are not. Momentum is *p = mv*. Kinetic energy is *KE = (1/2)mv*². They both depend on mass and velocity, but they scale differently. If you double the mass while keeping velocity constant, momentum doubles but kinetic energy also doubles. If you double the velocity while keeping mass constant, momentum doubles but kinetic energy quadruples. They respond to changes differently, and they have different units (kg·m/s vs. joules). In collisions, momentum is conserved; kinetic energy is not. This difference matters.

**Misconception 2:** "A force applied for a short time can never do as much as a force applied for a long time."

This confuses force with impulse. A large force applied briefly can deliver more impulse than a small force applied for a long time. The impulse is the product: Δp = F·Δt. A punch delivers high force for milliseconds; a push delivers low force for seconds. Both can produce the same momentum change. What matters for stopping something is impulse, not the size of the force alone.

**Misconception 3:** "Impulse and force are the same."

Force is an instantaneous push. Impulse is force multiplied by the time it acts. They have different units and different meanings. A large force for zero time delivers zero impulse. A small force for infinite time delivers infinite impulse. The two parameters trade off.

---

## Concept 2: Conservation of Momentum in Isolated Systems

### Why Momentum is Conserved

Imagine two pool balls on a frictionless table. Ball A, moving at 2 m/s, collides with ball B, stationary. After the collision, ball A slows to 0.5 m/s and ball B moves forward at 1.5 m/s. Assume both balls have the same mass.

Before collision: *p*_total = m(2) + m(0) = 2m
After collision: *p*_total = m(0.5) + m(1.5) = 2m

The total is unchanged. Ball A lost some momentum, but ball B gained it. The system conserved it.

This is not a coincidence. It follows from Newton's third law: when A pushes on B, B pushes back on A with equal force in the opposite direction. Both pushes last the same amount of time (the collision is simultaneous). By the impulse-momentum theorem:

$$\Delta p_A = F_A \Delta t$$
$$\Delta p_B = -F_A \Delta t$$

So:

$$\Delta p_A + \Delta p_B = 0$$

The changes in momentum cancel. If nothing else exerts a force on the system (no friction, no external push), the total momentum stays constant.

This works for any number of objects and any type of collision, provided no external force acts. We call such a system an **isolated system**. In an isolated system, the **law of conservation of momentum** states:

$$\mathbf{p}_{\text{tot}} = \text{constant}$$

or more explicitly:

$$p_1 + p_2 + \cdots = p'_1 + p'_2 + \cdots$$

where the primes denote values after the collision or event.

### The Scope and Limits of Isolation

On Earth, nothing is truly isolated. Friction acts on pool balls. Air resistance acts on flying objects. Gravity acts on everything. Yet conservation of momentum is one of physics' most reliable laws. Why?

The answer lies in thinking about which system you are analyzing. If you consider only the two colliding pool balls, friction will eventually cause momentum to be "lost" (converted to heat and sound in the table). But if you expand the system to include the table and the Earth, the momentum is still there—the Earth's motion changes by a minuscule amount when the ball transfers momentum to it. The effect is too small to measure, but it is real.

In practice, we use conservation of momentum when we can reasonably neglect external forces. Two cars colliding on a frictionless surface (or one where friction is the same before and after, so it doesn't change the total)—momentum is conserved. Two football players colliding—the friction with the ground is small compared to the forces they exert on each other, so momentum is approximately conserved for the duration of the collision. A rocket in space expelling fuel—the system includes the rocket and the expelled fuel, and momentum is conserved if you account for both.

The limitation is important to name: if an external force is large compared to the internal forces between colliding objects, conservation fails. A car hitting a building does not conserve total momentum, because the building is anchored to the Earth, and the Earth is enormous. The building's "recoil" is undetectable because the Earth absorbs the momentum.

### Worked Example: The Ice Hockey Goalie

A goalie stands on a frictionless ice rink, at rest. A hockey puck, mass 0.150 kg, travels at 35 m/s. He catches it. The goalie has mass 70 kg. What is their combined velocity after the catch?

This is a perfectly inelastic collision: the puck and goalie stick together and move as one object afterward. Apply conservation of momentum:

$$m_{\text{puck}} v_{\text{puck}} + m_{\text{goalie}} v_{\text{goalie}} = (m_{\text{puck}} + m_{\text{goalie}}) v'$$

$$(0.150)(35) + (70)(0) = (0.150 + 70) v'$$

$$5.25 = 70.15 \, v'$$

$$v' = 0.0749 \text{ m/s}$$

The goalie recoils backward at about 7.5 centimeters per second. The puck's momentum is transferred, but because the goalie is so much more massive, the momentum change produces a tiny velocity. The momentum is conserved: the total before (5.25 kg·m/s) equals the total after (5.25 kg·m/s). What changed is how that momentum is distributed—almost all of it was the puck's motion before; now it is spread across both the puck and the goalie, resulting in a slow backward glide.

### Common Misconceptions

**Misconception 1:** "In a collision, momentum is always conserved."

Momentum is conserved only when no external force acts on the system. If friction is large, if gravity is significant (as in a vertical collision without a supporting surface), or if the system is not closed, momentum can appear to be "lost." It is not lost—it is transferred to something outside the system.

**Misconception 2:** "If momentum is conserved, kinetic energy must also be conserved."

This is false. Momentum and kinetic energy are independent. In a collision between a car and a wall, momentum is not conserved (the wall is anchored to the Earth). But even in an isolated system where momentum is conserved, kinetic energy can be lost. In an inelastic collision, the objects slow down or come to rest; the kinetic energy is converted to heat, sound, and deformation. Momentum and energy are not the same.

**Misconception 3:** "Conservation of momentum means objects stop moving."

It does not. It means the total momentum of the system is unchanged. In a collision, one object may come to rest while another moves faster, or both may move more slowly than before, or one may reverse direction. The total momentum remains constant, but the distribution changes. "Conserved" means the sum is unchanged, not that motion ceases.

---

## Concept 3: Elastic and Inelastic Collisions

### The Two Types and Why They Matter

Two types of collisions behave fundamentally differently: **elastic** and **inelastic**.

In an **elastic collision**, the objects separate after impact. They bounce off each other. Kinetic energy is conserved—the total energy of motion before the collision equals the total after. This is a strict definition. In real life, perfectly elastic collisions happen only with subatomic particles or objects on near-frictionless surfaces like ice or air tables.

In an **inelastic collision**, kinetic energy is not conserved. The objects slow down, or they stick together and move as one. The "lost" energy is converted to heat, sound, deformation, or other forms. A car crash is highly inelastic. Two balls of clay slamming together are inelastic. The extreme case is a **perfectly inelastic collision**, where the objects stick together and move as a single body afterward.

The key trade-off: momentum is always conserved (in an isolated system), but kinetic energy is conserved only in elastic collisions. This distinction is not academic. It tells you whether an object will shatter, how much heat will be released, whether people inside vehicles will survive. Energy dissipation is a signature of inelasticity.

### Why Elasticity Changes Everything

Consider two scenarios, both involving a 1,000 kg car traveling at 10 m/s colliding with a stationary identical car on a frictionless surface.

**Scenario 1: Elastic collision**

Before: *p* = 1,000(10) + 1,000(0) = 10,000 kg·m/s

For an elastic collision between equal masses where one is at rest, the moving object stops and the stationary object takes on the original velocity:

After: Car 1 comes to rest (v' = 0). Car 2 moves at 10 m/s.

Total momentum after: 1,000(0) + 1,000(10) = 10,000 kg·m/s ✓ conserved

Kinetic energy before: (1/2)(1,000)(10)² = 50,000 joules

Kinetic energy after: (1/2)(1,000)(0)² + (1/2)(1,000)(10)² = 50,000 joules ✓ conserved

**Scenario 2: Inelastic collision (both cars stick together)**

Before: *p* = 10,000 kg·m/s (same as before)

After: Both cars move together.

$$(1,000)(10) + (1,000)(0) = (2,000) v'$$
$$v' = 5 \text{ m/s}$$

Total momentum after: 2,000(5) = 10,000 kg·m/s ✓ conserved

Kinetic energy after: (1/2)(2,000)(5)² = 25,000 joules

Energy "lost" (converted to heat, sound, deformation): 50,000 − 25,000 = 25,000 joules

In the elastic case, the collision is clean—one car transfers its motion to the other. In the inelastic case, the total kinetic energy is halved. The cars crumple, the impact is loud, and the temperature rises. The same momentum change produces opposite outcomes for energy.

Here is the deeper insight: elastic collisions are rare, but they teach you how objects can exchange momentum without loss. Inelastic collisions are common, and they teach you that energy is not conserved in the way momentum is. This is why physicists separate the two: they are governed by different rules.

### Worked Example: Two-Dimensional Elastic Collision

A hockey puck of mass 0.250 kg (puck 1) slides at 2 m/s on ice and strikes a stationary puck of mass 0.400 kg (puck 2). The puck emerges from the collision at an angle of 45° to its original direction, with speed 1.50 m/s. What are the speed and direction of puck 2 after the collision?

Set up a coordinate system with the *x*-axis along puck 1's original motion. Momentum is conserved along both axes.

**Along the x-axis:**

$$m_1 v_1 = m_1 v'_1 \cos \theta_1 + m_2 v'_2 \cos \theta_2$$

**Along the y-axis:**

$$0 = m_1 v'_1 \sin \theta_1 + m_2 v'_2 \sin \theta_2$$

Solving these equations using the given values:

$$v'_2 \approx 0.886 \text{ m/s}$$
$$\theta_2 \approx 312° \text{ (or } -48°)$$

The lighter puck is deflected at a large angle; the heavier puck moves more slowly but at a smaller deflection angle. Momentum is conserved along both axes, though the individual pucks change direction and speed.

### Common Misconceptions

**Misconception 1:** "Elastic collisions are bouncier than inelastic collisions."

Elasticity is not about the visual appearance of a bounce. It is about whether kinetic energy is conserved. A ball bouncing on concrete may look bouncy (elasticity ≈ high) but lose some energy with each bounce (pure elasticity would mean infinite bouncing). The terms describe the energy budget, not the phenomenology.

**Misconception 2:** "If a collision is inelastic, the objects must stick together."

Inelastic means kinetic energy is not conserved. Objects can undergo an inelastic collision without sticking—they can bounce off each other but lose energy to heat and deformation. A perfectly inelastic collision is the special case where they stick. But "inelastic" is broader.

**Misconception 3:** "Elastic collisions are impossible in the real world."

True that perfectly elastic collisions are impossible. But collisions between objects on very-low-friction surfaces (air hockey tables, ice) approximate elasticity well enough for practical calculation. Elasticity is an idealization, but a useful one.

---

## Integration: Momentum, Impulse, and Collision as One System

You now have three concepts. Let me show how they weave together.

Momentum tells you how hard an object is to stop: *p = mv*.

Impulse tells you how a force, over time, changes that momentum: Δ*p* = *F* Δ*t*.

Conservation of momentum tells you that in an isolated system, the total before an event equals the total after: *p*_total = constant.

Elasticity tells you whether kinetic energy is also conserved.

Here is how they connect: When two objects collide, their individual momenta change. But the change in one object's momentum is equal and opposite to the change in the other's (by Newton's third law, acting over the same time). The total momentum of the system remains constant. How long the collision lasts determines whether anyone is injured or property is damaged. Whether kinetic energy is conserved tells you whether the collision is a bounce or a crumple.

In a car crash, an airbag extends the duration of the impact (increasing Δ*t*), which decreases the force (*F* = Δ*p* / Δ*t*). The momentum of the passenger's body is reversed. But the impulse that does this work is the same whether or not the airbag is present; the airbag just distributes that impulse over a larger area and longer time. The kinetic energy is lost (converted to heat and sound), making the collision highly inelastic. But momentum is conserved: the passenger's momentum change equals the negative of the airbag's backward impulse.

In pool, when the cue ball strikes another ball elastically, the two exchange momentum with little energy loss. The cue ball slows or stops; the struck ball moves at the original velocity. The collision is crisp. Mastering this trade-off—understanding when momentum transfers cleanly and when energy is lost—is the difference between advanced play and chaos.

---

## Exercises

### Warm-up

1. **Calculating momentum:** A basketball of mass 0.6 kg is moving at 5 m/s to the right. What is its momentum? In which direction?

2. **Impulse and force:** A soccer ball of mass 0.43 kg is kicked from rest to a velocity of 12 m/s in 0.05 seconds. What is the impulse? What is the average force exerted by the foot?

3. **Identifying isolated systems:** For each scenario, decide whether momentum is conserved (isolated system) or not. Explain briefly.
   - (a) Two billiard balls colliding on a pool table with minimal friction.
   - (b) A baseball hit into the air and caught by an outfielder.
   - (c) Two ice skaters pushing each other on a frozen pond.
   - (d) A car skidding to a stop on a wet road.

### Application

4. **Conservation of momentum in one dimension:** A 1,200 kg car traveling at 15 m/s collides with a 1,000 kg car at rest. If they stick together (perfectly inelastic), what is their final velocity?

5. **Recoil velocity:** An astronaut of mass 70 kg (including suit) is floating in space and throws a wrench of mass 2 kg away at 5 m/s relative to the astronaut's initial position. What is the astronaut's recoil velocity?

6. **Comparing elastic and inelastic collisions:** A 2 kg ball moving at 4 m/s collides head-on with a 1 kg ball at rest. Calculate:
   - (a) The total momentum before the collision.
   - (b) The kinetic energy before the collision.
   - (c) If the collision is perfectly inelastic, what is the final velocity?
   - (d) What is the kinetic energy after the perfectly inelastic collision?
   - (e) How much energy is "lost"?

### Synthesis and Challenge

7. **Two-dimensional collision:** A 0.5 kg puck moving at 3 m/s collides with a 0.3 kg puck at rest on ice. After the collision, the first puck moves at 2 m/s at an angle of 30° to its original direction. Find the velocity (magnitude and direction) of the second puck.

8. **Real-world impulse design:** A safety engineer is designing a new padding for a football helmet. An impact delivers a 2,000 newton-second impulse. The helmet currently spreads this over 20 milliseconds, resulting in a 100,000 newton average force. If the engineer doubles the padding thickness to spread the impact over 40 milliseconds, what is the new average force? Why might this be safer?

9. **Conservation of momentum with friction:** Two cars collide on a road where friction cannot be ignored. Explain why, even though momentum is not conserved for the car-road system alone, momentum is conserved if you include the entire Earth as part of the system. What assumption allows physicists to ignore this complication in practice?

---

## Summary

Momentum is the product of mass and velocity, *p* = m**v**. It is a vector quantity, pointing in the direction of motion. Objects with high momentum are hard to stop.

Impulse is the product of force and time, Δ*p* = **F** Δ*t*. A large force for a short time and a small force for a long time can produce the same impulse and thus the same change in momentum.

The impulse-momentum theorem connects Newton's second law to momentum: **F**_net = Δ**p** / Δ*t*. This form is more general than *F* = m*a* because it accounts for systems where mass changes.

In an isolated system (where no external force acts), the total momentum is conserved: *p*_total = *p'*_total. This law is derived from Newton's third law and is one of the most reliable principles in physics.

Elastic collisions conserve kinetic energy; the objects separate and bounce off. Inelastic collisions do not conserve kinetic energy; energy is converted to heat, sound, or deformation. Momentum is conserved in both types, as long as the system is isolated.

The distinction between momentum and kinetic energy is critical: momentum is always conserved in an isolated system, but kinetic energy is only conserved in elastic collisions. This difference explains why collisions have different outcomes—why some deform objects and others transfer motion cleanly.

---

## Connections Forward

Momentum and impulse set the stage for understanding rotational motion. Just as linear momentum describes the inertia of straight-line motion, **angular momentum** describes the inertia of spinning objects. A figure skater spinning with arms outstretched slows down when pulling arms inward because angular momentum is conserved and moment of inertia decreases.

Energy and momentum are the two pillars of collision analysis. When both are conserved, the collision is elastic and reversible. When only momentum is conserved, energy is dissipated, and the collision is irreversible. In later chapters, we will use both principles together to analyze complex systems.

Impulse appears again in the study of forces over time. In materials science, engineers use impulse to design structures that absorb impact—car frames that crumple, parachutes that deploy, bumpers that compress. The same principle that governs collision also governs how we protect against collision.

---

**What would change my mind:** If I were shown an example of an isolated system in which total momentum is not conserved, or a real-world elastic collision where kinetic energy is lost without evidence of external force, I would revise this chapter's central claims.

**Still puzzling:** Why angular momentum conservation appears to apply even more rigidly than linear momentum conservation in some systems (e.g., spinning neutron stars) remains something I do not fully understand. The physics of what "drives" this seems deeper than current formulations capture.

**Tags:** momentum, impulse, collision, conservation laws, elastic, inelastic, Newton's third law, isolated systems, kinetic energy
---

## LLM Exercise — Chapter 8: Momentum (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the marble (or coin) collision demo + the balloon-rocket demo.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 8 demo. Notebook in this Claude Project. Chapter 8 taught:
linear momentum p = mv; conservation of momentum (in collisions and
all isolated-system interactions); impulse F·Δt = Δp; elastic
collisions (KE conserved) vs. inelastic (KE not conserved, often
because heat or deformation absorbs some).

Two demos. Pick at least one.

**Demo A — Equal-Mass Marble Collision (Elastic)**

The classic Newton's cradle demonstration without buying one:

- Get 4-5 identical marbles or steel ball bearings.
- Lay them in a straight line on a smooth surface (a flat table).
- Fire one marble at the line at moderate speed. Predict what
  happens.

The momentum-conservation prediction (with elastic collision):
the IMPACT marble stops; the FAR-END marble of the row shoots out
at the impact velocity. The middle marbles stay put.

Why? Each collision is elastic; momentum and KE both transfer
through the chain. Only the end marble has nowhere to transfer
its momentum, so it leaves.

If your collisions are inelastic (the marbles deform), you'll
see all marbles move together at lower speed. The demo is most
striking with hard, smooth marbles.

**Demo B — Balloon Rocket (Action-Reaction + Momentum)**

- Tape a balloon to a small toy car or a straw threaded onto a
  string stretched across a room.
- Inflate the balloon. Release.
- The balloon's air rushes out one direction; the balloon-and-car
  rushes the other.

The momentum conservation: the system's total momentum starts at
zero. The escaping air carries momentum in one direction; the
balloon must carry equal-and-opposite momentum.

Measure: distance traveled by the car. Predict using approximate
mass of escaping air × estimated exhaust velocity = momentum
imparted to the car.

**Use Claude as a thinking partner:**
- For Demo A: "Predict what happens if I fire two marbles at
  once. Does the cradle eject two marbles from the far end?"
- For Demo B: "Estimate the exhaust velocity and mass of air
  for a typical balloon. Does my predicted car distance match
  the observed?"

**Notebook entry should include:**
- Photo of setup.
- Pre-demo prediction.
- For A: which marbles moved, in what order; whether KE was
  visibly conserved (no slowing).
- For B: distance traveled by car; estimated momentum balance.
- One observation that surprised you.

End with: explain (without using the word "rocket") how a real
rocket gets to space using only the principles you've just
demonstrated.
```

---

**What this produces:** A demo entry confirming momentum conservation. Students who fire two marbles into the cradle and see two come out the other end usually remember the lesson better than any textbook treatment.

**How to adapt this prompt:**

- *For your own project:* The marble-cradle demo works best with steel ball bearings, but glass marbles work too. Pool balls are excellent if you have a pool table.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional for video-based velocity extraction.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 4's F = ma is being integrated over time to give impulse = Δp; Ch 5's vector decomposition applies to 2D collisions if you want to extend.

**Preview of next chapter:** Chapter 9 is work, energy, and simple machines. You'll build a simple lever and measure mechanical advantage directly — the ancient observation that "give me a place to stand and I can move the world" gets quantified.


---

## AI Wayback Machine

**Daniel Bernoulli** worked out conservation principles in fluid and particle dynamics in Hydrodynamica (1738).

**Run this:**

```
Who is Daniel Bernoulli, and how does their work connect to momentum we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Daniel Bernoulli"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Daniel Bernoulli's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Daniel Bernoulli's framework."

What changes? What gets better? What gets worse?
