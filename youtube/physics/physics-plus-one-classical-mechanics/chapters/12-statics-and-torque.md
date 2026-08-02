# Chapter 12 — Statics and Torque

*Nothing is harder to hold still than something that wants to fall.*

---

The Vasco da Gama Bridge outside Lisbon opened in March 1998. It spans the Tagus estuary for about 17 kilometers. The main cable-stayed section runs 830 meters, with a deck suspended from two towers each rising 148 meters above the waterline. A car driving across weighs perhaps 15,000 newtons. The deck weighs hundreds of millions of newtons more. Wind loads during a storm add lateral forces on the order of tens of kilonewtons per meter of deck. The region experienced a magnitude 8.7 earthquake in 1755.

For the bridge to work, nothing moves. Not a millimeter of translation. Not a fraction of a degree of rotation. Every cable carries a specific tension. Every tower bears a specific load distributed across its concrete base. The whole structure is frozen in a precise equilibrium — one that every engineer who worked on the project had to calculate in advance and trust completely.

This is statics: the physics of not moving. Which turns out to be more subtle than it sounds.

You might think that keeping something still just requires balancing the forces — what pushes up matches what pushes down, what pulls left matches what pulls right. That is necessary. It is not sufficient. A system can have perfectly balanced forces and still rotate. Think of a steering wheel: push on the left side with your right hand and pull on the right side with your left hand — equal and opposite forces, summing to zero, yet the wheel spins. The forces are balanced; the rotation is not.

Keeping something truly still requires two independent conditions: the forces must sum to zero *and* the torques — the rotational tendencies — must sum to zero. Both. Always. This chapter is about what torque is, how to calculate it, and how the two conditions together let you determine every force in a structure that is not moving.

<!-- → DIAGRAM: two-panel illustration of the steering-wheel insight — left panel: a steering wheel with two hands, right hand pushing left side forward and left hand pulling right side backward, labeled "ΣF = 0 (forces balanced)" with a green checkmark, but a curved arrow showing the wheel spinning clockwise, labeled "Στ ≠ 0 (torques NOT balanced)" with a red X; right panel: the same wheel with both hands pushing forward at the same point, labeled "ΣF ≠ 0" red X and "Στ = 0" green checkmark — student should see that the two conditions are independent and neither alone guarantees stillness -->

---

## The First Condition: Forces Must Balance

Start with the simpler half. For a body in equilibrium, the net external force is zero:

$$\sum \mathbf{F}_{\text{external}} = 0.$$

In components, for a 2D problem: $\sum F_x = 0$ and $\sum F_y = 0$. In 3D, a third equation. The procedure is identical to the free-body-diagram method from Chapter 6. Identify all external forces, resolve them into components, set each component sum to zero.

A book on a table: gravity pulls it down at $mg$; the table's normal force pushes it up at $N$. Net force zero: $N = mg$. Simple.

A sign hanging from two ropes at different angles: now two unknowns (the two tensions), two equations (one per axis). The system is determined — you can solve for both tensions from the force balance alone. The steeper rope carries more of the vertical load; the more angled rope contributes more horizontal force. You can work it all out algebraically from the geometry of the angles.

What force balance alone cannot handle is any situation where more than two unknown forces act. A beam supported at two ends with a load somewhere along it has three unknowns (the two support forces and the position-dependent distribution of the load), but only two force equations. You are stuck — unless you invoke the second condition.

---

## Torque: The Rotational Tendency of a Force

Before stating the second condition, we need the concept it involves.

You already know this concept from daily experience. Loosening a stuck bolt: you grip the wrench far from the bolt's head, not close to it. A long wrench handle breaks a bolt free that a short handle cannot. The force you apply is the same; what differs is where you apply it. The *rotational effect* of a force depends not just on the force but on where it is applied relative to the pivot.

The quantity that captures this is **torque**:

$$\tau = rF\sin\theta,$$

where $r$ is the distance from the pivot point to where the force is applied, $F$ is the force magnitude, and $\theta$ is the angle between the force vector and the line from pivot to application point.

Three equivalent ways to say the same thing. You can write $\tau = r_\perp F$, where $r_\perp$ is the perpendicular distance from the pivot to the line along which the force acts — the *lever arm*. Or $\tau = r F_\perp$, where $F_\perp$ is the component of force perpendicular to the line from pivot to application point. All three give the same number. The form you use depends on what is easier to measure in the specific problem.

<!-- → DIAGRAM: a wrench on a bolt showing all three torque formulations simultaneously — the bolt is the pivot; a force F is drawn at angle θ from the wrench handle; one bracket labels r (distance from bolt to hand); a perpendicular drop from the bolt to the force's line of action labels r⊥ (the lever arm); a component decomposition labels F⊥ (the component perpendicular to the wrench); three separate inset boxes show τ = rF sinθ, τ = r⊥F, and τ = rF⊥ with a note that all three give the same value — student should see that the three forms are geometrically equivalent and choose whichever is most convenient -->

Two things zero out the torque. If $r = 0$ — the force is applied at the pivot — there is no torque regardless of how large the force is. If $\theta = 0°$ or $180°$ — the force points directly toward or away from the pivot — there is also no torque: $\sin 0 = \sin 180 = 0$. Pulling along the wrench's length, toward or away from the bolt, does not rotate the bolt at all.

Units: N·m. The same as energy — and this is unfortunate, because torque is not energy. They are dimensionally identical but conceptually distinct. Torque is a rotational analog of force; energy is what is transferred when a force acts over a displacement. Do not confuse them.

Sign convention: counterclockwise torques are positive, clockwise are negative. This is arbitrary but must be held consistently throughout a given problem.

---

## The Second Condition: Torques Must Balance

The second equilibrium condition is:

$$\sum \tau_{\text{external}} = 0,$$

evaluated about any chosen pivot point.

That last phrase — *any chosen pivot* — deserves emphasis. The object is not actually rotating, so there is no natural axis. You invent one for the purpose of the calculation. You can put the pivot anywhere you like — on the object, off the object, in empty space. The equilibrium condition holds everywhere.

And a clever choice makes the algebra dramatically simpler. If you put the pivot at the location where an unknown force is applied, that force has a lever arm of zero — it contributes nothing to the torque equation. It drops out. You have one fewer unknown to track. In most statics problems, the strategy is: identify the unknown you least want to deal with, put the pivot there, and let the torque equation tell you everything else.

**A worked example.** A uniform 50 kg beam, 4.0 m long, is supported at both ends. A 100 kg person stands 1.0 m from the left support. What force does each support exert?

The unknowns are the two support forces, $F_L$ and $F_R$. Force balance gives one equation: $F_L + F_R = (50 + 100) \times 9.80 = 1{,}470$ N. One equation, two unknowns — not yet determined.

Take torques about the left support. $F_L$ has zero lever arm and drops out. The beam's own weight acts at the center, 2.0 m away. The person's weight acts 1.0 m away. $F_R$ acts 4.0 m away.

$$\sum \tau = 0: \quad +4.0 \, F_R \; - \; 2.0 \times 490 \; - \; 1.0 \times 980 = 0.$$

$$4.0 \, F_R = 980 + 980 = 1{,}960 \implies F_R = 490 \text{ N.}$$

From force balance: $F_L = 1{,}470 - 490 = 980$ N.

Check: the left support carries twice as much as the right, because the person stands close to the left end. The lever arm of the person's weight about the right support is 3.0 m — three times the lever arm about the left support. The torque balance distributes the load accordingly.

<!-- → DIAGRAM: horizontal beam free-body diagram for the worked example — beam drawn as a horizontal rectangle 4.0 m long; left support (F_L = 980 N, ↑) at left end; right support (F_R = 490 N, ↑) at right end; beam weight (490 N, ↓) at center labeled "2.0 m from each end"; person weight (980 N, ↓) labeled "1.0 m from left, 3.0 m from right"; bracket arrows showing the lever arms used in the torque equation; student should see why the left support carries more — the person is 3× closer to the left than to the right -->

This is the rhythm of every statics problem: force balance gives you one set of equations, torque balance gives you one more, together they determine the unknowns.

---

## The Body as a Structure

Let us apply both conditions to something more intimate than a bridge: your own arm.

Your forearm holding a book is a lever. The biceps muscle attaches to the radius (the forearm bone) about 5 cm from the elbow joint. Your hand, holding the book, is about 30 cm from the elbow. The book's weight pulls down at 30 cm from the pivot; the biceps pulls up at 5 cm from the pivot.

Torque balance about the elbow:

$$F_{\text{biceps}} \times 0.05 = W_{\text{book}} \times 0.30.$$

$$F_{\text{biceps}} = W_{\text{book}} \times \frac{0.30}{0.05} = 6 \, W_{\text{book}}.$$

To hold a 5 kg book — weight 49 N — the biceps pulls with about 294 N. Six times the book's weight.

This is biology's structural trade-off, not a design failure. Muscles attached close to joints produce small forces through large ranges of motion: the hand moves 30 cm for every 5 cm the biceps shortens. You trade force for speed. But the trade-off means muscles typically operate at ten times or more the load they are moving. The tendons carrying those loads are under enormous stress, which is why tendon injuries are among the most common in athletics and the most difficult to heal.

The mechanical advantage of the biceps lever is the ratio of the effort arm to the load arm: $5/30 \approx 1/6$. A mechanical advantage less than one means you exert more force than you lift. The reverse situation — a long effort arm, short load arm — gives MA greater than one, multiplying force at the cost of speed. This is the lever in most of its engineering applications: a crowbar prying up a nail, a pair of scissors, a hydraulic jack.

<!-- → DIAGRAM: forearm as a lever — elbow joint drawn as pivot at left; forearm bone extending right; biceps muscle attachment point labeled "5 cm from elbow" with upward force arrow F_biceps (~294 N for a 5 kg book); hand at right end labeled "30 cm from elbow" with downward force arrow W_book (49 N); lever arm lengths explicitly labeled (5 cm, 30 cm); the 6:1 ratio annotated; a small inset shows the energy trade-off: "same work — 6× force, 1/6 the distance" — student should see why the muscle force is six times the load and feel the trade-off viscerally -->

The energy accounting is always exact. Work in equals work out (in a frictionless ideal machine). If you push with half the force over twice the distance, the work is the same. No machine creates energy; every machine trades it.

---

## A Ladder on a Wall

Statics problems come in many forms, but the ladder problem has become a kind of canonical example because it contains all the interesting features: a distributed-weight object, a frictionless contact (the wall), a frictional contact (the floor), and the question of whether the system will slip.

A uniform 20 kg ladder, 5.0 m long, leans against a smooth (frictionless) wall at 60° from the ground. The floor has coefficient of static friction $\mu_s = 0.40$. Will the ladder slip?

Free-body diagram. Four forces: the ladder's weight $W = 196$ N at the center (2.5 m along its length). Normal force from the floor $N_f$ upward. Friction from the floor $f$ horizontal (toward the wall — the ladder would slide outward without it). Normal force from the wall $N_w$ horizontal (outward — the wall can only push, not pull, since there is no attachment).

<!-- → DIAGRAM: ladder leaning at 60° against a smooth wall — ladder drawn as a diagonal line; four labeled force arrows: N_f (↑) at base, f (→, toward wall) at base, W = 196 N (↓) at midpoint, N_w (←, outward) at top; dashed right-angle markers showing the perpendicular distances used as torque lever arms: horizontal distance from base to weight's line (1.25 m) and vertical distance from base to wall force's line (4.33 m); the base of the ladder circled and labeled "chosen pivot"; student should see why this pivot eliminates both N_f and f from the torque equation -->

Vertical equilibrium: $N_f = W = 196$ N.

Horizontal equilibrium: $f = N_w$.

Torque about the base of the ladder (so $N_f$ and $f$ both drop out):

The weight acts at the ladder's midpoint. Its horizontal distance from the base is $2.5 \cos 60° = 1.25$ m. The wall force acts at the top of the ladder. Its perpendicular distance from the base is $5.0 \sin 60° = 4.33$ m.

$$\sum \tau = 0: \quad N_w \times 4.33 - 196 \times 1.25 = 0.$$

$$N_w = \frac{245}{4.33} \approx 56.6 \text{ N.}$$

So the friction force required is also 56.6 N. The maximum available is $\mu_s N_f = 0.40 \times 196 = 78.4$ N. Since 56.6 N $<$ 78.4 N, the ladder does not slip.

If the floor were oilier — say $\mu_s = 0.25$ — the maximum available friction would be $0.25 \times 196 = 49$ N, less than the required 56.6 N. The ladder would slip. The calculation tells you the exact threshold.

What happens if a person climbs the ladder? They add weight, and their weight's lever arm grows as they ascend. The required friction force increases. At some point it exceeds $\mu_s N_f$ and the ladder slips. You can calculate exactly how far up the person can safely climb — and the answer depends on the mass of the person, the mass of the ladder, the angle, and the friction coefficient. This is the kind of specific, checkable prediction that distinguishes physics from vague intuition.

---

## Stability

There is a third idea in statics, subtler than the two equilibrium conditions: the difference between stable and unstable equilibrium.

Balance a pencil on its tip. It satisfies both equilibrium conditions instantaneously — net force zero, net torque zero. But tap it, and it falls. The equilibrium was unstable: any small perturbation creates a torque that pushes it further from equilibrium rather than back toward it.

Stand the same pencil on its eraser. Tap it, and it wobbles and returns. Stable equilibrium: perturbations create restoring torques.

The geometric criterion is simple. An object's equilibrium is stable if the vertical line through its center of mass falls within its base of support. Stable: tilt it a little, and the center of mass is still above the base; gravity pulls it back. Unstable: the center of mass is directly above a point, and any tilt takes it outside the base.

<!-- → DIAGRAM: three side-by-side panels for stable, unstable, and neutral equilibrium — each shows an object (bowl + marble, hill + marble, flat surface + marble), the center of mass marked with a dot, and a vertical dashed line from the center of mass to the base; left panel (stable): center of mass above the bowl's base, with a curved "restoring" arrow when tilted; middle panel (unstable): center of mass directly above the tip of the hill, with a "destabilizing" arrow on any tilt; right panel (neutral): center of mass always at the same height on the flat surface, no restoring or destabilizing tendency — student should see the geometric criterion directly and be able to apply it to any shape -->

This is why wide vehicles are more stable than narrow ones, and why lowering a vehicle's center of mass improves its stability in turns. In a lateral turn, the effective gravity vector tilts — combine the downward pull of gravity with the inward centripetal acceleration and the net direction is toward the outside of the turn. If that vector's line passes outside the base of support (the track width between the wheels), the vehicle tips over. The wider the track, the larger the tilt required to tip. The lower the center of mass, the more tilt required before the line exits the base.

The same principle governs your posture. You stand upright because your center of mass is above your feet. Carrying a heavy backpack shifts your center of mass backward; you lean forward to compensate, keeping the total center of mass over your base. A person with a large anterior load (late pregnancy, say) adopts a characteristic lumbar curvature for exactly this reason — the body continuously adjusts its configuration to maintain balance, which is a dynamic version of the static analysis.

---

## Two Conditions Together

Step back. Two equilibrium conditions:

Force balance: $\sum \mathbf{F} = 0$. Nothing translates.

Torque balance: $\sum \tau = 0$ about any pivot. Nothing rotates.

Together, they produce — in 2D — three equations. Three unknowns can be determined. Many structures have exactly three unknown reaction forces and are therefore *statically determinate*: the equilibrium equations alone are sufficient to find every force. Add a fourth support and the system becomes *statically indeterminate*: the equilibrium equations are no longer sufficient; you need to know how the materials deform under load. That is the territory of structural engineering and elasticity, beyond what statics alone can reach.

The scale of application is vast. The same two equations describe a $0.5$ kg book on a kitchen table and a $17$ km cable-stayed bridge. In both cases, nothing is translating, nothing is rotating, and every force is determined by the requirement that both sums vanish. The Vasco da Gama Bridge is a large bookkeeping exercise — but the physics is the two equilibrium conditions, applied at every cross-section, for every cable, at every load case the engineers considered. Same equations. Many more terms.

What makes statics tractable is the strategic pivot. Any structure with unknown forces at multiple locations can be attacked by choosing pivots that eliminate unknowns. The unknown you least want appears at the pivot; its lever arm is zero; it contributes nothing to the torque equation; you solve for everything else first, then use the force balance to find what remains. This is not a trick. It is the method.

---

## What Would Change My Mind

The two equilibrium conditions are exact in classical mechanics for any rigid body at rest. They are derived directly from Newton's laws, and they fail only if Newton's laws fail — which, at bridge-and-ladder scales, they do not. What requires extension, not revision, is the rigid-body assumption: real materials deform under load, and when deformations are significant (very slender structures, near-failure conditions), the geometry changes during loading and the simple static analysis becomes approximate. Structural mechanics and finite-element methods handle this. They do not overthrow the equilibrium conditions; they apply them to the deformed geometry.

## Still Puzzling

Why does the "any pivot" theorem hold? The equilibrium conditions say both the net force and the net torque are zero. If you shift the pivot point by some vector $\mathbf{d}$, each force's torque changes by $\mathbf{d} \times \mathbf{F}_i$. Sum over all forces: $\mathbf{d} \times \sum \mathbf{F}_i = \mathbf{d} \times \mathbf{0} = \mathbf{0}$. The total torque is unchanged because the net force is zero. The two conditions are therefore not independent in the way they first appear — they are coupled through this identity, and together they are exactly sufficient for equilibrium in any dimension. The coupling is subtle and worth sitting with.

---

## Exercises

### Warm-up

**1.** A 3.0 kg book sits on a level table. (a) What is the normal force? (b) Someone stacks a second 1.5 kg book on top. What is the normal force now? (c) Someone presses down on the stack with an additional 10 N. What is the normal force now?

*Tests: $\sum F_y = 0$; normal force as whatever is required for equilibrium, not a fixed quantity.*

**2.** A force of 50 N is applied perpendicular to the end of a wrench 0.30 m long. (a) What is the torque? (b) If the same force is applied at 30° to the wrench instead of perpendicular, what is the torque now? (c) Which angle produces more torque, and why?

*Tests: $\tau = rF\sin\theta$; maximum torque at 90°.*

**3.** Identify each as stable, unstable, or neutral equilibrium, and state the geometric reason: (a) a marble at the bottom of a bowl, (b) a marble at the top of a hill, (c) a marble on a flat table, (d) a tall narrow bookcase on a smooth floor, (e) a wide squat stool.

*Tests: center-of-mass criterion for stability; applying geometric reasoning rather than intuition.*

**4.** A 4.0 m uniform beam of mass 20 kg is supported at both ends with no additional load. What force does each support exert? (You should be able to answer this without a calculation — explain your reasoning.)

*Tests: symmetry argument; center of mass at midpoint means equal support forces. Tests whether the student can reason without computing.*

---

### Application

**5.** A 4.0 m uniform 30 kg plank is supported at both ends. A 70 kg person stands 1.0 m from the left end. Find the support force at each end using both conditions of equilibrium.

*Tests: full two-condition analysis; strategic pivot choice.*

**6.** A 6.0 m uniform 18 kg ladder leans against a frictionless wall at 65° from the horizontal. (a) Draw the free-body diagram and label all four forces. (b) Find the wall's normal force. (c) Find the floor's friction force. (d) What minimum coefficient of static friction is required?

*Tests: full ladder analysis; identification of which contact is frictionless vs. frictional; strategic pivot at the base.*

**7.** A lever has an effort arm of 0.80 m and a load arm of 0.10 m. (a) What is the mechanical advantage? (b) A 60 N force is applied at the effort end — what load can be lifted? (c) If the effort end moves 0.40 m, how far does the load end move? (d) How much work is done by the effort force? By the load force? Are they equal?

*Tests: mechanical advantage; energy conservation in a simple machine; force-distance trade-off.*

**8.** Your forearm is horizontal, holding a 4.0 kg textbook. The biceps muscle attaches 5.0 cm from the elbow; the book is 32 cm from the elbow; the forearm itself has mass 1.5 kg and its center of mass is 15 cm from the elbow. (a) Draw the free-body diagram of the forearm. (b) Write the torque equation about the elbow. (c) Find the biceps force required. (d) Does the result surprise you?

*Tests: full forearm lever including forearm's own weight; applying torque balance to a biological structure.*

---

### Synthesis

**9.** A 1,200 kg truck is parked with its center of mass 2.5 m from the left end of a uniform 8.0 m bridge whose mass is 4,000 kg. Find the support force at each end.

*Tests: two distributed loads (bridge weight at center, truck weight off-center); full equilibrium analysis.*

**10.** A semi-truck has its center of mass 1.8 m above the road surface and a track width (distance between wheels) of 2.4 m. (a) On flat ground, what is the critical tilt angle at which it just tips? (b) In a turn, the effective gravity vector tilts outward due to centripetal acceleration. If the truck rounds a curve of radius 40 m at 15 m/s, by what angle does the effective gravity tilt? (c) Does the truck tip?

*Tests: stability criterion applied quantitatively; connecting centripetal acceleration to the stability analysis from Chapter 8.*

---

### Challenge

**11.** A uniform door of mass 25 kg, height 2.0 m, and width 0.90 m hangs from two hinges — one 0.25 m from the top, one 0.25 m from the bottom. (a) Draw the free-body diagram of the door. (b) The door's weight acts at its center. Taking torques about the bottom hinge, find the horizontal force the top hinge must exert. (c) Apply force balance to find the horizontal force at the bottom hinge. (d) What direction does each horizontal hinge force act, and why must they be in opposite horizontal directions?

*Tests: non-trivial free-body diagram with hinge forces; torque balance where the pivot is not at a support; force balance to close the system; physical reasoning about force directions.*

---

## LLM Exercise — Chapter 12: Statics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A static-equilibrium analysis of one part of your anchor phenomenon at rest.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 12, I want to apply the two conditions of static
equilibrium (ΣF = 0, Στ = 0) to one stationary element of my
phenomenon. Please:

1. Identify ONE stationary structural element in my phenomenon.
   Examples:
   - Bike commute: bike at rest leaning against a wall — what
     tension in any straps, what friction at the floor?
   - Coffee maker: brewing chamber gasket under pressure load —
     what static force balance keeps it sealed?
   - Basketball: a basketball balanced on a fingertip — what
     center-of-mass condition?
   - Marathon: a runner standing at the starting line — what
     muscles are active to maintain posture?
   - Espresso: portafilter handle locked into the group head —
     what torque balance holds it in place under 9 bar?

2. Draw (in ASCII or describe) the free-body diagram. Identify all
   external forces and where they act.

3. Apply ΣF = 0 along each axis. Apply Στ = 0 about a clever
   pivot.

4. Solve for the unknown forces. Report with units and percent
   uncertainty.

5. Sanity-check: does the magnitude of the muscle/cable/contact
   force surprise you? (Most do — they're often much larger than
   expected.)

6. Identify stability (stable, unstable, neutral) and the geometric
   criterion: does the center of mass fall within the base of
   support?

7. One sentence on how this connects to Chapter 13 (rotational
   dynamics) — when torques don't balance, the object accelerates
   rotationally.

Save the output as logbook/chapter-12-statics.md.
```

### What this produces

A Logbook entry: an equilibrium analysis revealing the often-surprising forces in stationary structures.

### How to adapt this prompt

- *For phenomena without obvious static structures* (a moving phenomenon): focus on a moment when the system is briefly at rest — a basketball at the apex of its arc, a runner at the moment of foot plant, a bike at a traffic light.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have a CAD model or measurements, paste dimensions.

### Connection to previous chapters

Builds directly on Chapter 6 (force balance is part of Newton's first law). Adds rotational equilibrium. Uses vector decomposition from Chapter 3 and friction from Chapter 7.

### Preview of next chapter

Chapter 13 generalizes everything here to moving rotational systems. Where statics has $\sum \tau = 0$, dynamics has $\sum \tau = I\alpha$ — the rotational analog of $F = ma$. The framework is identical; only the right-hand side becomes nonzero.

---

## AI Wayback Machine

**Archimedes of Syracuse** worked out the law of the lever and the basics of static equilibrium in the 3rd century BCE — "Give me a place to stand, and I will move the Earth." His treatises on mechanics established statics as a quantitative science.

**Run this:**

```
Who was Archimedes, and how does his work connect to the statics
and torque we covered in this chapter? Keep it to three paragraphs.
End with the single most surprising thing about his career or ideas.
```

→ Search **"Archimedes"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Archimedes's geometric proof of the law of the lever.
- Ask it about the loss of Archimedes's writings — and their partial recovery from the Archimedes Palimpsest.

What changes? What gets better? What gets worse?

---

*Tags: statics; torque; equilibrium; mechanical-advantage; free-body-diagram; lever; stability*
