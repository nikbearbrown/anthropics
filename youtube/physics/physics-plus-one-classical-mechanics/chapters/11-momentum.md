# Chapter 11 — Momentum: The Physics of Collision

*Why the combination of mass and velocity matters more than either alone.*

---

## Two players, one point on the field

It is fourth down, the final seconds gone. Two players sprint toward the same point. One is 280 pounds — heavier, slower, running at about $8 \text{ m/s}$. The other is 200 pounds — lighter, faster, at $10 \text{ m/s}$. They meet. One bounces backward. The other stumbles forward. Neither is moving at anything close to their pre-collision speed.

Watch it in slow motion and something strange comes clear: the heavier player, despite being slower, did more damage. The faster, lighter player was the one moved. This is not what everyday intuition predicts. You might expect the faster player to win — speed feels like power. But speed alone isn't the right quantity. Mass alone isn't either. What matters is the combination.

Physics calls that combination **momentum**, and this chapter is about what it is, how it changes, and why — in any isolated system, collision or otherwise — the total amount of it never changes.

---

## Momentum

The definition is simple: momentum is mass times velocity.

$$\mathbf{p} = m\mathbf{v}$$

We use $p$ rather than $m$ for momentum to avoid confusion with mass. Momentum is a vector — it points in the direction of motion, and it reverses when the direction reverses. The units are $\text{kg} \cdot \text{m/s}$.

Two objects can have the same momentum by very different means. A $2 \text{ kg}$ ball at $5 \text{ m/s}$ and a $1 \text{ kg}$ ball at $10 \text{ m/s}$ both carry $10 \text{ kg} \cdot \text{m/s}$ of momentum. But they are not the same object to encounter. The lighter, faster ball is harder to intercept because it covers ground faster. The heavier, slower ball, once you do get in its way, is harder to stop because it has more mass to redirect. Same momentum number, different machinery for delivering it.

Back to the football players. The 280-pound player (about $127 \text{ kg}$) at $8 \text{ m/s}$:

$$p = (127)(8) = 1016 \text{ kg} \cdot \text{m/s}.$$

The 200-pound player (about $91 \text{ kg}$) at $10 \text{ m/s}$:

$$p = (91)(10) = 910 \text{ kg} \cdot \text{m/s}.$$

The heavier player carries about 12% more momentum. That's what the slow-motion replay is actually showing — not that strength beats speed, but that mass-times-velocity beats velocity alone when the mass difference is large enough.

<!-- → [DIAGRAM: side-by-side comparison of the two football players as arrows — player 1: wide arrow (127 kg) at moderate length (8 m/s), labeled p = 1016 kg·m/s; player 2: narrower arrow (91 kg) at longer length (10 m/s), labeled p = 910 kg·m/s; the arrows should visually encode both mass (width) and velocity (length) so the reader sees why the heavier-slower player wins; caption: "same units, different machinery — mass-times-velocity, not speed alone"] -->

---

## How momentum changes: impulse

Momentum doesn't stay constant by accident. It changes when a force acts on an object over time.

Newton's second law is usually written $F = ma$. But Newton's original statement was different — he said the net external force equals the *rate of change of momentum*:

$$\mathbf{F}_\text{net} = \frac{\Delta \mathbf{p}}{\Delta t}.$$

For constant mass, $\Delta \mathbf{p} = m \Delta \mathbf{v} = m \mathbf{a} \Delta t$, which recovers $F = ma$. But the momentum form is more general — it applies even when mass changes (a rocket burning fuel), and it makes visible something the acceleration form hides: *time matters*.

Rearrange to:

$$\Delta \mathbf{p} = \mathbf{F}_\text{net} \, \Delta t.$$

The right side — force times time — is called **impulse**. The equation is the **impulse-momentum theorem**: the impulse delivered to an object equals its change in momentum.

The insight hiding in this equation: a large force for a short time can deliver the same impulse as a small force for a long time. Same momentum change, different experience.

<!-- → [CHART: two-panel force-vs-time graph showing equal impulse delivered two ways — left panel: tall narrow rectangle (large F, short Δt) labeled "unpadded impact"; right panel: short wide rectangle (small F, long Δt) labeled "padded impact"; both rectangles have the same area (= impulse = Δp); caption: "the area under each curve is identical — the physics requires the same momentum change either way; padding controls the shape, not the area"] -->

During the 2007 French Open, Venus Williams hit a serve at $58 \text{ m/s}$. A tennis ball has mass $0.057 \text{ kg}$; it started at rest and reached $58 \text{ m/s}$ while in contact with the racquet for about $5 \text{ ms} = 0.005 \text{ s}$.

Change in momentum:

$$\Delta p = m(v_f - v_i) = (0.057)(58 - 0) = 3.31 \text{ kg} \cdot \text{m/s}.$$

Average force:

$$F = \frac{\Delta p}{\Delta t} = \frac{3.31}{0.005} = 661 \text{ N}.$$

That's the weight of a $67 \text{ kg}$ person pressing down on the ball — through a contact patch about an inch wide, in one-fifth of a second. The force is enormous because the contact time is tiny. If the ball stayed on the strings ten times longer — $50 \text{ ms}$ instead of $5 \text{ ms}$ — the same momentum change would require only $66 \text{ N}$. The impulse is fixed by the physics; the force is set by the time you spread it over.

<!-- → [INFOGRAPHIC: the Venus Williams serve — show the ball path from rest to 58 m/s with a 5 ms contact window annotated; alongside, show the force calculation chain: Δp = 3.31 kg·m/s → F = Δp/Δt = 661 N → equivalent to ~67 kg weight; then a second column showing what happens if Δt = 50 ms instead: same Δp, F drops to 66 N; caption: "the impulse (area) is fixed by the ball's mass and final speed — contact time sets the force"] -->

This is why padding works. A car crash must reverse the momentum of the passenger — there is no way around that. What you can control is the time over which the reversal happens. An unpadded dashboard delivers the impulse in milliseconds: enormous force, concentrated on a small area. A padded dashboard delivers the same impulse over tens of milliseconds: force one-tenth as large, spread across a larger area. The momentum change is identical. The consequences for the passenger are not. This is why airbags were invented; it is why crumple zones exist; it is why every safety advance in collision engineering is fundamentally an exercise in increasing contact time.

---

## Conservation of momentum

Now the deep result.

Two pool balls on a frictionless table. Ball A, mass $m$, moves at $v_A = 2 \text{ m/s}$ and strikes ball B (same mass), at rest. After the collision, A has slowed to $0.5 \text{ m/s}$ and B moves forward at $1.5 \text{ m/s}$.

Before: $p_\text{total} = m(2) + m(0) = 2m$.

After: $p_\text{total} = m(0.5) + m(1.5) = 2m$.

The total is unchanged. Ball A lost momentum; ball B gained it. The system kept the total.

This is not coincidence. It follows from Newton's third law. When A pushes on B during the collision, B pushes back on A with equal force in the opposite direction. Both forces act for the same time — they are the two sides of the same contact. By the impulse-momentum theorem:

$$\Delta p_A = F_{AB} \, \Delta t, \quad \Delta p_B = -F_{AB} \, \Delta t.$$

The sum: $\Delta p_A + \Delta p_B = 0$. Whatever A loses, B gains. The total cannot change.

<!-- → [DIAGRAM: two-object collision showing the Newton's-third-law proof — draw ball A and ball B in contact; show equal and opposite force arrows (F_AB on B, –F_AB on A) acting for the same time Δt; below, show the impulse calculation: ΔpA = +F·Δt (A slows), ΔpB = –F·Δt (B speeds up), sum = 0; caption: "conservation is not a separate law — it follows directly from Newton's third law applied over a collision time"] -->

This argument holds for any number of objects, any type of interaction, provided no *external* force acts on the system. We call such a system **isolated**, and we state the result as the **law of conservation of momentum**:

$$p_{1,i} + p_{2,i} + \cdots = p_{1,f} + p_{2,f} + \cdots$$

The total momentum before any event equals the total momentum after.

A goalie stands at rest on a frictionless ice rink. A hockey puck, $m = 0.150 \text{ kg}$, arrives at $35 \text{ m/s}$. The goalie ($M = 70 \text{ kg}$) catches it. What is their combined velocity?

$$m v_\text{puck} = (m + M) v',$$

$$(0.150)(35) = (70.15) v',$$

$$v' = \frac{5.25}{70.15} \approx 0.0749 \text{ m/s}.$$

About $7.5 \text{ cm/s}$ backward. The puck carried $5.25 \text{ kg} \cdot \text{m/s}$ of momentum; so does the goalie-plus-puck after the catch. The momentum was conserved; it was just spread across $470$ times more mass, resulting in $470$ times less velocity.

<!-- → [DIAGRAM: before-and-after momentum diagram for the goalie catch — left: puck arrow (0.150 kg, 35 m/s, p = 5.25 kg·m/s) moving right, goalie at rest; right: combined goalie-plus-puck arrow (70.15 kg, 0.075 m/s, p = 5.25 kg·m/s) moving right at barely visible speed; annotate both arrows to the same momentum scale; caption: "same total momentum before and after — the arrow got 470× heavier and 470× shorter"] -->

Nothing is truly isolated on Earth — friction acts on pool balls, air resistance acts on everything, gravity is everywhere. But conservation of momentum is still one of physics' most reliable tools because we can always choose our system to include whatever external agents we care about. If you include the Earth in the system when a car skids to a stop, momentum is conserved: the car loses momentum, the Earth gains an imperceptibly small amount in the opposite direction. The Earth is so massive that its velocity change is $\sim 10^{-25} \text{ m/s}$ — unmeasurable, but real. The law is exact; the approximation is in how much of the universe we bother to include.

In practice, we use conservation of momentum when external forces are small compared to the collision forces, or when we only care about the collision itself (which happens so fast that external forces don't have time to deliver significant impulse). This is almost always a good approximation for high-speed collisions.

---

## Elastic and inelastic collisions

Momentum is always conserved in an isolated system. Kinetic energy is not. The distinction between these two facts is where collision physics gets interesting.

An **elastic collision** is one where kinetic energy is also conserved — the objects bounce, and the total $\tfrac{1}{2}mv^2$ of the system before equals the total after. A perfectly elastic collision is an idealization; it happens with good approximation for hard objects on low-friction surfaces (billiard balls, steel bearings, some atomic and subatomic collisions), but never exactly in everyday life.

An **inelastic collision** is one where kinetic energy is not conserved. Some of it converts to heat, sound, and deformation. A **perfectly inelastic collision** is the extreme case: the objects stick together and move as one body after impact.

The most important thing to know: **both types conserve momentum**. They differ in what happens to kinetic energy.

Two identical cars, each $1{,}000 \text{ kg}$. One moves at $10 \text{ m/s}$, the other is at rest. They collide on a frictionless track.

**Elastic case:** Equal masses, one at rest — the moving object stops and the stationary one takes its velocity. After: car 1 at $0$, car 2 at $10 \text{ m/s}$. Momentum conserved: $10{,}000 \text{ kg} \cdot \text{m/s}$ before and after. Kinetic energy: $50{,}000 \text{ J}$ before and after. Clean transfer.

**Perfectly inelastic case:** They stick together.

$$m v_0 = 2m v', \quad v' = \frac{v_0}{2} = 5 \text{ m/s}.$$

Momentum: $(1{,}000)(10) = (2{,}000)(5) = 10{,}000 \text{ kg} \cdot \text{m/s}$. Conserved.

Kinetic energy after: $\tfrac{1}{2}(2{,}000)(5)^2 = 25{,}000 \text{ J}$. Before: $50{,}000 \text{ J}$. Half the kinetic energy is gone — converted to crushing metal, heat, and sound. The cars crumple, the air rings with the impact, the temperature of the deformed steel rises slightly. Total energy is still conserved — it just left the mechanical ledger.

<!-- → [TABLE: side-by-side comparison of the elastic vs. perfectly inelastic car collision — rows: initial momentum, final momentum, initial KE, final KE, KE lost, what happened to the lost energy; elastic column: p conserved, KE conserved, 0 lost, "transferred cleanly"; inelastic column: p conserved, KE halved, 25,000 J lost, "heat + sound + deformation"; caption: "momentum: same rule in both columns — kinetic energy: different fate"] -->

The intuition worth keeping: elastic collisions transfer motion cleanly without loss. Inelastic collisions are the signature of real-world deformation and dissipation. Knowing which type you're dealing with tells you whether to bring in the energy equation or not.

A subtlety about kinetic energy that trips up almost every student: momentum and kinetic energy scale differently with velocity. Momentum scales as $v$; kinetic energy scales as $v^2$. If you double the speed, momentum doubles but kinetic energy quadruples. This means two objects with equal momenta do not have equal kinetic energies unless they also have equal masses. The football players from the opening have similar momenta (~$1000 \text{ kg} \cdot \text{m/s}$ each), but the faster, lighter player has more kinetic energy — he's harder to stop with a simple interception, even though the heavier player delivers more momentum on direct contact. Same quantity? Different quantities. Watch the exponents.

---

## All three ideas together

Momentum, impulse, and conservation are not separate topics bolted together for a chapter. They are the same story told in three registers.

**Momentum** tells you the state: how much motion a mass is carrying, in what direction.

**Impulse** tells you the process: how a force over time changes that state. The impulse-momentum theorem is Newton's second law integrated over time.

**Conservation** tells you the constraint: in any isolated system, the vector sum of momenta is fixed. The distribution can shift — one object gains what another loses — but the total doesn't move.

The practical lesson of all three together is what engineers use every day. An airbag needs to deliver a specific impulse (reversing the passenger's momentum), in the minimum force, across the maximum time. A crumple zone is designed so that the car's front absorbs momentum slowly rather than transmitting it instantly to the passengers. A parachute extends the time over which terminal-velocity momentum is removed, keeping the landing force survivable. The physics is the same in all three cases: $F = \Delta p / \Delta t$, and you want $\Delta t$ large.

One more example, this one going the other way. A rocket in deep space fires its engine. There is no air, no ground, no thing to push against. How does it move?

Before the engine fires, the total momentum of the rocket-plus-fuel system is zero (the rocket is at rest). When the engine fires, hot exhaust gas is expelled backward at high speed. That exhaust carries momentum in the backward direction. The rocket must carry equal momentum in the forward direction. The total is still zero; the distribution has shifted. The rocket accelerates forward not because the exhaust pushes against anything, but because the law of momentum conservation requires that when exhaust goes one way, the rocket goes the other. Newton's third law and momentum conservation are the same statement; the rocket is just a dramatic demonstration of it.

This is the same principle as the balloon-rocket demo. The same principle as the goalie catching the puck. The same principle as two football players meeting at the line of scrimmage. Momentum is carried by every moving mass in the universe, and the total — when you account for every piece of the system — is always the same before and after any interaction.

<!-- → [INFOGRAPHIC: three-panel "same principle, different scale" — left: balloon car on a string (exhaust goes left, car goes right, total p = 0 throughout); center: goalie catching puck (puck momentum transfers to heavier system, p conserved); right: rocket in space (exhaust backward, rocket forward, total p = 0 throughout); caption: "balloon, goalie, rocket — the same momentum-conservation argument, three different envelopes"] -->

---

## Exercises

### Warm-up

**11.1** A basketball of mass $0.6 \text{ kg}$ moves at $5 \text{ m/s}$ to the right. What is its momentum? In which direction?

**11.2** A soccer ball of mass $0.43 \text{ kg}$ is kicked from rest to $12 \text{ m/s}$ in $0.05 \text{ s}$. (a) What is the impulse? (b) What is the average force exerted by the foot?

**11.3** For each scenario, decide whether momentum is approximately conserved (isolated system) and explain briefly: (a) two billiard balls colliding on a pool table with minimal friction; (b) a baseball hit into the air and caught by an outfielder; (c) two ice skaters pushing each other on a frozen pond; (d) a car skidding to a stop on a wet road.

### Application

**11.4** A $1{,}200 \text{ kg}$ car traveling at $15 \text{ m/s}$ collides with a $1{,}000 \text{ kg}$ car at rest. They stick together. What is their final velocity?

**11.5** An astronaut of mass $70 \text{ kg}$ (suit included) floats in space and throws a $2 \text{ kg}$ wrench at $5 \text{ m/s}$ relative to her initial position. What is her recoil velocity?

**11.6** A $2 \text{ kg}$ ball at $4 \text{ m/s}$ collides head-on with a $1 \text{ kg}$ ball at rest. (a) Total momentum before. (b) Kinetic energy before. (c) Final velocity if perfectly inelastic. (d) Kinetic energy after. (e) Energy "lost."

### Synthesis

**11.7** A $0.5 \text{ kg}$ puck at $3 \text{ m/s}$ collides with a $0.3 \text{ kg}$ puck at rest on ice. After the collision, the first puck moves at $2 \text{ m/s}$ at $30°$ to its original direction. Find the velocity (magnitude and direction) of the second puck.

**11.8** A safety engineer is designing helmet padding. An impact delivers $2{,}000 \text{ N} \cdot \text{s}$ of impulse. The current padding spreads this over $20 \text{ ms}$, resulting in $100{,}000 \text{ N}$ average force. If doubled padding extends contact to $40 \text{ ms}$, what is the new average force? Why might this matter for injury?

**11.9** Two cars collide on a road where friction is significant. Explain why momentum is not conserved for the two-car system alone, but is conserved if you include the entire Earth. What assumption lets physicists ignore this in practice?

### Challenge

**11.10** A ballistic pendulum: a bullet of mass $0.010 \text{ kg}$ is fired at $300 \text{ m/s}$ into a stationary wooden block of mass $2.0 \text{ kg}$ hanging on a string. The bullet embeds in the block. (a) Using momentum conservation, find the velocity of the block-plus-bullet immediately after impact. (b) Using energy conservation, find how high the block swings. (c) How much kinetic energy was lost in the collision? Where did it go?

**11.11** Explain, using only momentum conservation and no other principle, how a rocket in deep space — with nothing to push against — can accelerate forward. What is the "system," and what has zero net momentum?

---

## LLM Exercise — Chapter 11: Momentum (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.  
**What you're building this chapter:** the marble (or coin) collision demo + the balloon-rocket demo.  
**Tool:** Claude Project for the entry.

### The Prompt

```
Chapter 11 demo. Notebook in this Claude Project. Chapter 11 taught:
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

### What this produces

A demo entry confirming momentum conservation. Students who fire two marbles into the cradle and see two come out the other end usually remember the lesson better than any textbook treatment.

### How to adapt this prompt

- *For your own project:* The marble-cradle demo works best with steel ball bearings, but glass marbles work too. Pool balls are excellent if you have a pool table.
- *For ChatGPT or Gemini:* Works as written.
- *For Claude Code:* Optional for video-based velocity extraction.
- *For a Claude Project:* Append.

### Connection to previous chapters

Chapter 6's $F = ma$ is being integrated over time to give impulse $= \Delta p$; Chapter 5's vector decomposition applies to 2D collisions.

### Preview of next chapter

Chapter 12 introduces rotational motion and angular momentum — the rotational analogue of everything in this chapter. A figure skater pulling in her arms is conservation of angular momentum in action.

---

## AI Wayback Machine

**Daniel Bernoulli** worked out conservation principles in fluid and particle dynamics in *Hydrodynamica* (1738).

**Run this:**

```
Who is Daniel Bernoulli, and how does their work connect to momentum we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Daniel Bernoulli"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Daniel Bernoulli's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Daniel Bernoulli's framework."

What changes? What gets better? What gets worse?
