# Chapter 6 — Dynamics: Force and Newton's Laws of Motion

*Three sentences written in Latin in 1687 that still predict everything mechanical.*

---

Yankee Stadium, late innings, a one-run game. Mariano Rivera comes in from the bullpen — forty-three years old, last season, the most prolific closer in the history of the sport. The hitter sets up. Rivera throws his cutter: a fastball that, instead of rotating purely backward, spins slightly off-axis so that in the last fifteen feet it darts an inch or two toward the hitter's hands. The hitter swings. There is a crack that is not the usual crack. The bat splits at the handle. The ball dribbles harmlessly to the pitcher.

The common reading: the bat hit the ball, transferred force into it, end of story. The more honest reading is that the bat hit the ball *and the ball hit the bat* — with exactly equal force in exactly opposite directions. The ball, arriving at 40 meters per second, pushed back on the bat with the same magnitude of force the bat applied to it. With a Rivera cutter, the contact point was a few inches from the sweet spot, close enough to the handle that the wood couldn't bear the load. The bat broke not because the hitter swung too hard. It broke because the ball pushed on the bat with the same force the bat pushed on the ball — in the wrong place along the lever.

This is one half of Newton's third law made visible. A force never exists alone. To exert is also to receive. The bat and the ball are not in different positions in this story; they are both participants in the same interaction, viewed from opposite ends.

<!-- → IMAGE: high-speed photograph of a baseball bat at the moment of contact with a ball — ideally a split-second image showing bat deformation; caption should label the force the bat exerts on the ball (→) and the equal and opposite force the ball exerts on the bat (←), and note that the contact point here is near the handle, not the sweet spot -->

The chapter ahead is about three sentences Isaac Newton wrote in 1687. They explain why things move, why they stop, why they don't move when they look like they should, and why a baseball can shatter seasoned ash. They also explain why a rocket goes up, why a car needs a road, and why, when you lean against a wall, the wall is — quietly, invisibly, exactly — pushing back on you.

---

## The First Law: Change Requires a Cause

Aristotle, around 350 BCE, had a theory of motion that everyone believed for the next two thousand years. The natural state of a body, he said, is rest. Things in motion slow down and stop because that is what they want to do. To keep something moving, you have to keep pushing. This matches everyday experience perfectly. Push a book across a table; it slows and stops. Roll a ball across a carpet; it slows and stops. Aristotle's claim — *motion requires a sustained cause* — is what your living room teaches you.

It is also wrong.

Galileo, around 1600, started undoing it with one observation. Push a book across a rough table; it slows quickly. Push it across glass; it slows less. Push it across wet ice; it barely slows at all. The slowing is not what the book wants to do. It is what friction does to the book. As the surface gets smoother, the slowing diminishes. Extrapolate to perfect smoothness, and the slowing vanishes entirely. The book would slide forever.

Switch on an air-hockey table. The puck glides across the surface on a thin film of air and does not appreciably slow. Switch the air off and the puck stops within an inch. The variable is not what the puck is doing. It is what the table is doing to the puck.

Newton wrote this insight down as a law. A body at rest remains at rest. A body in motion remains in motion at constant velocity. Unless — here is the critical clause — a net external force acts on it. The natural state of a body, in the absence of forces, is *constant velocity*, which includes zero as a special case. Slowing down is not a default; it is an effect that requires a cause, exactly as speeding up does.

Two phrases in the law need unpacking. *External* means applied from outside the system you are analyzing. If you are analyzing a car, your push on the gas pedal transfers through the engine to the road and back to the car — that is external. Internal forces, between parts of the system, cancel in pairs and do not change the system's motion. *Net* means the vector sum of all external forces. Two equal forces applied in opposite directions produce a net of zero. The object does not accelerate, even though forces are acting.

This resolves the apparent paradox of everyday life. The book pushed across a table eventually stops — Aristotle looks right. But there are two forces on the moving book: your push forward, and friction backward. When you stop pushing, the friction does not stop. The net force is now backward. The book decelerates. The first law was right the whole time; we were miscounting forces.

Here is the property of matter that makes the first law non-trivial: **inertia**. Inertia is the tendency of an object to resist changes in its state of motion. A heavy object is harder to start and harder to stop than a light one. The quantitative measure of inertia is **mass**, in kilograms. Not weight — we will separate those carefully — but the intrinsic resistance to acceleration that an object carries regardless of where in the universe it sits.

The payoff of the first law is enormous. It licenses every problem where you assert that an object moving at constant velocity has zero net force. A car cruising at steady speed on a flat highway — engine running, friction present — has zero net force, because constant velocity is the signature of zero net force. The engine's forward push exactly cancels the drag. You do not press the gas harder to maintain speed; you press it just enough to cancel what is slowing you down. Steady motion does not mean no forces. It means no *net* force. Conflating those two is the most common Aristotelian residue in beginner intuition, and catching it is the first law's job.

<!-- → DIAGRAM: side-by-side comparison of a book sliding on three surfaces — rough table (large friction arrow backward, short distance traveled), smooth glass (smaller friction arrow, longer distance), frictionless ice (no friction arrow, arrow extending to edge of frame labeled "continues forever") — student should see Galileo's extrapolation: as friction diminishes, the distance before stopping grows without limit, implying constant velocity with no friction at all -->

---

## The Second Law: $F = ma$

A child sitting in a wagon. Two friends push from different directions at different angles. The wagon accelerates in some direction, at some rate. Newton's second law tells you how to predict that direction and that rate from the forces and the mass.

$$\mathbf{F}_{\text{net}} = m\mathbf{a}$$

Three symbols. Each has a precise meaning. Half the work of using this equation is being careful about which symbol means what.

$\mathbf{F}_{\text{net}}$ is the vector sum of every external force on the system. Add them as vectors. If three forces act, the net force is their vector sum, direction and all. Internal forces do not appear — they cancel in pairs by the third law, which we will see shortly.

$m$ is the inertial mass of the system, in kilograms. A scalar, always positive.

$\mathbf{a}$ is the acceleration of the system's center of mass — a vector, pointing in the same direction as the net force, with magnitude $|\mathbf{F}_{\text{net}}| / m$.

The equation says: a net external force causes an acceleration, in the direction of the force, with magnitude inversely proportional to the mass. Push hard on something light: large acceleration. Push gently on something heavy: small acceleration. The proportionality is exact — it is not approximate, not a tendency, not a rule of thumb. In components, the equation splits into independent statements along each axis: $F_{\text{net},x} = ma_x$, $F_{\text{net},y} = ma_y$. Two-dimensional problems become two one-dimensional problems, solved separately, then combined.

Weight and mass are different things, and this equation makes the difference precise. Near Earth's surface, gravity pulls every object downward with a force

$$\mathbf{W} = m\mathbf{g}$$

where $\mathbf{g}$ is the local gravitational acceleration, about $9.80 \text{ m/s}^2$ downward. Weight is a *force*, measured in newtons. Mass is a *property*, measured in kilograms. A 1 kg object on Earth weighs 9.80 N. The same 1 kg object on the Moon weighs 1.62 N — the Moon's gravitational acceleration is about one-sixth of Earth's. Mass is what the object is; weight is what gravity does to it in a particular place. The factor of $g$ converts between them, going one direction or the other, and mixing them up by a factor of ten is one of the most reliable ways to get a wrong answer.

<!-- → TABLE: two-column comparison — Earth vs Moon — rows: local gravitational acceleration (9.80 m/s² / 1.62 m/s²), mass of a 1 kg object (1 kg / 1 kg), weight of that object (9.80 N / 1.62 N), weight of a 65 kg person (637 N / 105 N); the mass rows are identical; the weight rows differ by a factor of ~6; student should see that mass is invariant while weight changes with location -->

Before solving any second-law problem, draw a **free-body diagram**: reduce the object to a point, draw an arrow for every external force acting on it, label each arrow. Then choose axes. Then sum forces along each axis. Then apply $F_{\text{net}} = ma$ along each axis separately. This is the algorithm. The hard part is not the algebra — it is identifying all the external forces without inventing imaginary ones (centrifugal force, the "force of motion") or omitting real ones (the normal force from the floor, which is easy to forget because it does not move anything by itself).

<!-- → DIAGRAM: free-body diagram of the stalled car — a dot or simple rectangle at center; four labeled arrows: "Push (400 N, →)", "Friction (200 N, ←)", "Weight W = mg (14,700 N, ↓)", "Normal force N (14,700 N, ↑)"; two axes labeled x (horizontal) and y (vertical); the vertical pair visibly equal and canceling, the horizontal pair showing a net 200 N residual in the push direction; student should see the four-force structure and how the two-axis split works before the algebra -->

**A worked example.** You push a stalled 1,500 kg car along a level road with a horizontal force of 400 N. Rolling friction opposes the motion at 200 N.

Draw the free-body diagram. Four forces: your push, 400 N forward. Friction, 200 N backward. Weight, $mg = 1500 \times 9.80 = 14{,}700 \text{ N}$ downward. Normal force from the road, 14,700 N upward.

Apply the second law vertically: $N - W = 0$, since the car is not accelerating through the pavement. Normal force confirmed equal to weight.

Apply it horizontally: $F_{\text{net}} = 400 - 200 = 200 \text{ N}$. So:

$$a = \frac{F_{\text{net}}}{m} = \frac{200}{1500} \approx 0.13 \text{ m/s}^2.$$

Sanity check: 400 N is roughly 90 pounds of force — hard but plausible for a person pushing a car. Getting 0.13 m/s² means the car gains about 1.3 m/s over ten seconds. That is about 3 mph in ten seconds — slow, as shoving a dead car should be. The numbers are right.

Notice that the vertical axis also needed checking, even though the answer was trivially zero. It confirmed the normal force, which we will need when friction problems arrive in the next chapter. Half the value of free-body diagrams is in the forces you confirm as balanced; you only get to ignore them once you have confirmed they are.

---

## The Third Law: Forces Come in Pairs

A competitive swimmer at the start of a race waits at the wall. The buzzer sounds. She pushes hard against the wall with her feet — and shoots forward into the pool. The wall did not move. She did.

What was the force on her that accelerated her body forward?

Her muscles pushed against the wall. The wall, in response, pushed her forward with exactly the same magnitude of force, in the opposite direction. The force *on her* — which is what the second law needs — came from the wall. Without the wall pushing back, she would have nothing to push against. She cannot accelerate herself in open water the way she can push off a wall; that is why swimmers sprint into the turn.

Newton's third law: whenever one body exerts a force on a second body, the first experiences a force that is equal in magnitude and opposite in direction to the force it exerts. Symbolically, if A pushes B with force $\mathbf{F}$, then B pushes A with force $-\mathbf{F}$. Equal magnitude, opposite direction, and — this is the critical part — they act on *different objects*.

The confusion that almost every student hits: "If every action has an equal and opposite reaction, how does anything ever accelerate? Don't the forces cancel?" They do not cancel, because they live on different objects. When the swimmer's feet push the wall forward with 500 N, the wall pushes her backward with 500 N. The 500 N on the wall would accelerate the wall — except the wall is bolted to the pool, which is bolted to the Earth, so the effective mass is enormous and the acceleration negligible. The 500 N on the swimmer accelerates *her*, and her mass is small, so her acceleration is substantial. Same force pair, radically different consequences, because the two forces act on objects of very different mass.

The trick for identifying third-law pairs is this: write "X exerts force on Y," then flip it to "Y exerts force on X." If both are true and the forces are equal and opposite, you have a pair.

The Earth pulls you down (gravity, about 700 N for a 70 kg person). You pull the Earth up (gravity, also 700 N). That is a pair. The Earth's resulting acceleration — $700 \div (6 \times 10^{24}) \approx 10^{-22} \text{ m/s}^2$ — is unmeasurably small but not zero. The road pushes up on a car's tires; the tires push down on the road. Pair. A book sits on a table; the table pushes up on the book; the book pushes down on the table. Pair.

Now an important non-pair. When a book rests on a table, two forces act on the book: gravity pulling it down, and the normal force pushing it up. Those two forces are equal and opposite on the book's free-body diagram — they have to be, because the book is in equilibrium. But they are *not* a third-law pair. Both forces act on the same object (the book), and third-law pairs never act on the same object. The third-law partner of "Earth's gravity on the book" is "book's gravity on the Earth." The third-law partner of "table's normal force on the book" is "book's normal force on the table." Two pairs, four forces, none of the four on the same object as its partner.

<!-- → DIAGRAM: book-on-table scene showing all four forces explicitly — book drawn as a rectangle on a table surface; arrow 1: "Earth pulls book down (gravity, ↓)" on the book; arrow 2: "Table pushes book up (normal, ↑)" on the book; arrow 3: "Book pulls Earth up (gravity, ↑)" — drawn on Earth below (or labeled separately); arrow 4: "Book pushes table down (normal, ↓)" — drawn on the table surface; two colored brackets identifying the two third-law pairs, neither bracket spanning forces on the same object; student should see that equilibrium (arrows 1 and 2 canceling) is NOT the same as a third-law pair -->

Return to the opening story. The bat strikes the ball. During the brief contact — roughly one millisecond — the bat exerts an average force of around 5,000 N on the ball. By the third law, the ball exerts 5,000 N on the bat. The ball's acceleration: $5000 / 0.145 \approx 34{,}500 \text{ m/s}^2$ — about 3,500 g's, brief and ferocious. The bat's acceleration from the ball's push, if the bat were free: $5000 / 0.95 \approx 5{,}300 \text{ m/s}^2$. The hitter's hands provide an additional forward force on the bat during contact, absorbing most of the recoil — which is why hits that contact off the sweet spot sting. The bat shattering is the wood failing to transmit the reaction force from contact point to grip without exceeding its structural limits. Off the sweet spot, the lever geometry concentrates stress at the handle. The wood gives before the force reaches the hands.

---

## Three Laws Together

Step back. Three sentences.

**First:** an object's velocity does not change unless a net external force acts. Constant velocity — including rest — is the natural state.

**Second:** the net external force equals mass times acceleration. $\mathbf{F}_{\text{net}} = m\mathbf{a}$. This is the predictive engine: given forces, it gives motion.

**Third:** every force is half a pair. If A pushes B with $\mathbf{F}$, then B pushes A with $-\mathbf{F}$, on different objects, always.

**A worked example that needs all three.** Two tugboats push a $5.0 \times 10^6 \text{ kg}$ barge. Tugboat 1 pushes with $2.7 \times 10^5 \text{ N}$ in the $+x$ direction. Tugboat 2 pushes with $3.6 \times 10^5 \text{ N}$ in the $+y$ direction. The barge accelerates at $7.5 \times 10^{-2} \text{ m/s}^2$ in the direction of the combined applied force. Water drag opposes the motion. Find the drag force.

The first law frames the problem: the barge is accelerating, so the net force is nonzero — drag must be less than the applied force.

Apply the second law. The combined applied force:

$$F_{\text{app}} = \sqrt{(2.7 \times 10^5)^2 + (3.6 \times 10^5)^2} = \sqrt{7.29 \times 10^{10} + 1.30 \times 10^{11}} \approx 4.5 \times 10^5 \text{ N}.$$

The required net force to produce the observed acceleration:

$$F_{\text{net}} = ma = (5.0 \times 10^6)(7.5 \times 10^{-2}) = 3.75 \times 10^5 \text{ N}.$$

So drag is:

$$F_{\text{drag}} = F_{\text{app}} - F_{\text{net}} = 4.5 \times 10^5 - 3.75 \times 10^5 = 7.5 \times 10^4 \text{ N}.$$

The third law interprets the drag: the barge pushes water backward; the water pushes the barge backward. Drag is one half of the action-reaction pair between barge and displaced water.

Sanity check: drag is about 17% of the applied force. For a flat-bottomed barge moving slowly through water, viscous drag at low speed is plausible at that fraction. The acceleration — 7.5 cm/s² — means the barge gains about 4.5 m/s over a minute of sustained push, which is fast for a barge but not physically absurd for short-duration acceleration.

All three laws exercised: the first framed what kind of problem we have (nonzero net force, because nonzero acceleration); the second computed the magnitude; the third explained what drag physically is.

---

## What These Laws Do Not Explain

The three laws describe what forces *do* once they exist. They do not explain where forces come from. Gravity, contact forces, friction, tension, air drag — these all feed into $\mathbf{F}_{\text{net}} = m\mathbf{a}$ as inputs. The second law processes them into motion. But the origin of each force is a separate question.

It turns out that every push, pull, contact force, friction, normal force, and tension you encounter in this book ultimately reduces to one of four fundamental interactions: gravity, electromagnetism, the strong nuclear force, and the weak nuclear force. The strong force binds atomic nuclei; the weak force governs certain radioactive decays; neither matters directly for mechanics problems. Gravity governs the weight of objects and the orbits of planets. And nearly every *contact* force — friction, normal force, tension, the rigidity of a chair — is electromagnetic in origin: when two surfaces touch, the electron clouds of their atoms repel each other. That repulsion is what prevents you from falling through the floor. The floor does not feel electric; the force has no net charge. But the underlying mechanism is electrons pushing electrons.

Newton's framework provides no explanation of this. Within his system, the equality of inertial mass (the $m$ in $F = ma$) and gravitational mass (the source of gravity's pull) is an unexplained coincidence, confirmed experimentally to one part in $10^{13}$ but without theoretical justification. Einstein's general relativity eventually resolves it — in that framework, gravity is not a force at all but the curvature of spacetime, and the equivalence of the two kinds of mass becomes structural rather than coincidental. That is a later story. For now, the equality is a free gift from nature that we use without fully understanding.

---

## The Scale of It

The same three laws govern a baseball bat shattering at 5,000 N over a millisecond, a person walking at a few newtons of net force over seconds, a car cruising with zero net force over hours, and a planet orbiting the Sun under $3.5 \times 10^{22}$ N of gravitational pull over billions of years. The equation $\mathbf{F}_{\text{net}} = m\mathbf{a}$ scales without modification across more than thirty orders of magnitude in mass and at least as many in time. That kind of universality is not something you prove — it is something you notice, and marvel at, and then use.

<!-- → INFOGRAPHIC: logarithmic scale spanning from "bat-ball contact (5×10³ N, ~1 ms)" through "person walking (~10 N, seconds)" through "car on highway (~0 N net, hours)" to "Earth orbiting Sun (3.5×10²² N, years)" — each entry labeled with force magnitude and timescale; a single equation F = ma floats above the entire scale; student should feel the span viscerally — the same equation covers this entire range without modification -->

The one idea that survives all the formalism: **forces cause changes in motion, not motion itself.** This single sentence inverts two thousand years of Aristotelian physics. Once it is genuinely internalized — not memorized but felt — every later mechanics problem falls into a pattern: identify the object, identify the external forces, sum them vectorially, divide by mass, get acceleration. The difficulty of mechanics problems is not conceptual after this chapter. It is the bookkeeping: making sure you find all the forces, getting the directions right, choosing axes that make the algebra tractable. The physics is in the three laws. The work is in applying them carefully.

---

## What Would Change My Mind

The chapter rests on the claim that Newton's three laws, with relativistic and quantum corrections for extreme conditions, suffice to describe the mechanical behavior of every system humans engineer or encounter. That would need revision if everyday macroscopic phenomena required corrections outside those already known regimes — which would mean new physics has been discovered. Physicists have been actively looking for over a century. None has been found.

## Still Puzzling

Why is inertial mass equal to gravitational mass? Newton's second law uses inertial mass — what an object resists acceleration with. Newton's law of gravity uses gravitational mass — the quantity that determines how strongly gravity pulls. They are conceptually distinct. You could imagine a universe where a heavy object (large gravitational mass) is nonetheless easy to accelerate (small inertial mass). Experimentally, the two are equal to a precision of better than one part in $10^{13}$. Newton's framework has no explanation for this. It is simply true. Einstein's general relativity eventually reframes the question by absorbing gravity into the geometry of spacetime — at which point the equivalence becomes not a coincidence to be explained but a structural feature of the theory. That story begins in Chapter 33.

---

## Exercises

### Warm-up

**1.** A hockey puck slides across a perfectly frictionless ice surface at constant velocity. (a) What is the net force on it? (b) Are there any forces on it at all — list every force acting. (c) Is this situation consistent with Newton's first law? Explain in one sentence.

*Tests: first law; constant velocity means zero net force, not zero forces.*

**2.** A 3.0 kg object experiences a net force of 12 N eastward. (a) What is its acceleration? (b) If the net force doubles, what happens to the acceleration? (c) If the mass doubles instead, what happens?

*Tests: second law; direct and inverse proportionality.*

**3.** What is the weight (in newtons) of a 70 kg person on Earth? On the Moon, where $g = 1.62 \text{ m/s}^2$? What is the person's mass in each location?

*Tests: weight vs. mass; $W = mg$; mass as invariant.*

**4.** Identify the Newton's-third-law partner of each force: (a) Earth's gravity pulling you downward. (b) Your hand pushing a door open. (c) A horse pulling a cart forward via a harness. For each, name both objects and both force directions.

*Tests: third-law pair identification; partner forces are on different objects.*

---

### Application

**5.** A 1,200 kg car accelerates from rest to 25 m/s in 8.0 seconds on a flat road. (a) What is its acceleration? (b) What is the net force on it? (c) If air drag and rolling friction together sum to 400 N opposing motion, what forward force must the engine-and-tires produce?

*Tests: second law; net force as the difference between engine force and resistance.*

**6.** A 50 kg skydiver falls at terminal velocity — constant speed, not accelerating. (a) What is her acceleration? (b) What is the net force on her? (c) What is the magnitude of the air drag force acting on her? Which law licenses this conclusion without knowing the drag equation?

*Tests: first law applied to terminal velocity; equilibrium as zero net force.*

**7.** A 20 kg box hangs from two ropes attached to a ceiling, each rope making a 30° angle with the vertical. (a) Draw the free-body diagram with all three forces labeled. (b) Write the equilibrium equations along each axis. (c) Find the tension in each rope.

*Tests: free-body diagram with three forces; resolving tensions along axes; equilibrium.*

**8.** A 5.0 kg block sits on a frictionless horizontal surface. A horizontal force of 30 N is applied. (a) What is the block's acceleration? (b) What is the normal force from the surface? (c) Draw the free-body diagram and label all four forces before calculating anything.

*Tests: free-body diagram discipline; confirming vertical equilibrium before solving horizontal.*

---

### Synthesis

**9.** Two ice skaters — masses 50 kg and 80 kg — stand facing each other on a frictionless rink and push off simultaneously. The push lasts 0.50 s, during which the lighter skater experiences a force of 200 N. (a) What force does the heavier skater experience during the push, and by which law? (b) What are their respective accelerations? (c) After the push ends, what are their speeds? (d) Which skater moves faster, and why — even though the force on each was the same magnitude?

*Tests: third law in a symmetric interaction; second law giving different accelerations from the same force magnitude; inertia as the explanation.*

**10.** A 100 kg crate sits on a frictionless 30° ramp. (a) Sketch the free-body diagram, resolving gravity into components parallel and perpendicular to the ramp surface. (b) What is the component of gravity along the ramp? (c) What is the normal force from the ramp? (d) What is the crate's acceleration down the ramp? (e) Identify the third-law partner of the normal force.

*Tests: resolving forces along non-standard axes; normal force as perpendicular to surface; third-law partner of a contact force.*

---

### Challenge

**11.** A 0.145 kg baseball arrives at the plate at 40 m/s and leaves the bat at 45 m/s in the opposite direction. Contact lasts 1.5 ms. (a) What is the ball's average acceleration during contact? (b) What average force did the bat exert on the ball? (c) What average force did the ball exert on the bat, and why is this force physically significant even though the bat is much heavier? (d) If the contact point were exactly at the sweet spot, the bat would not shatter — but at a few inches toward the handle, the wood fails. What does this tell you about what the third law predicts versus what the material can bear?

*Tests: third law with unequal masses; force magnitude identical on both objects; distinguishing the physics (equal forces) from the material response (unequal consequences).*

---

## LLM Exercise — Chapter 6: Forces in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A free-body diagram of a key element of your anchor phenomenon, with all forces identified, $F = ma$ applied, and at least one Newton's-third-law pair named explicitly.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 6, I want to apply Newton's three laws to my phenomenon.
Please:

1. Pick ONE moment in my phenomenon where forces are interesting.
   Examples:
   - Bike commute: the moment of pushing off from a stop sign —
     what forces accelerate me?
   - Coffee maker: the moment when water column weight pushes down
     through the basket and grounds resist — what's the force
     balance during brewing?
   - Basketball shot: the moment of release — what forces does the
     player exert and feel?
   - Marathon: a steady-state stride at race pace — what forces are
     balanced, and what produces forward motion?
   - Espresso: the puck during extraction at 9 bar — what forces act
     on the coffee, and what balances them?

2. Draw (in ASCII or describe in text) the free-body diagram for the
   chosen object. List every external force with magnitude (estimated
   or computed) and direction.

3. Apply F = ma along each axis. Solve for any unknown (the
   acceleration, an unknown force, or a needed coefficient).

4. Identify at least one Newton's-third-law action-reaction pair in
   the scene. Name both forces, both objects, and explain why the
   pair doesn't "cancel."

5. Sanity check the result with one Fermi-style estimate.

6. Identify which fundamental force (gravity, electromagnetic, etc.)
   ultimately underlies each contact force you listed.

7. One sentence on how friction (Chapter 7) will modify this
   analysis.

Save the output as logbook/chapter-06-newtons-laws.md.
```

### What this produces

A Logbook entry: a force analysis of your phenomenon with the action-reaction structure made explicit. By Chapter 6 you have foundation, kinematics, and force analysis — most of Newtonian mechanics in skeleton form for your phenomenon.

### How to adapt this prompt

- *For phenomena where motion is mostly steady-state* (a coffee maker reaching equilibrium, a marathon at constant pace): emphasize the balanced-force analysis (first law) rather than the accelerating analysis. Both are exercises of Newton's laws.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have force data (a pressure curve from an espresso machine, a wattmeter reading from a stationary bike), paste it and ask for a force-vs-time fit.

### Connection to previous chapters

Builds directly on Chapter 3's vector decomposition — forces are vectors resolved along axes exactly as velocities were. The kinematics from Chapter 4 return: once you have $a$ from the second law, you can predict velocity and position from the kinematic equations.

### Preview of next chapter

Chapter 7 specializes Newton's laws to friction, drag, and elasticity — the three force laws that answer "where do contact forces actually come from?" The Chapter 7 exercise will ask you to compute friction or drag explicitly for your phenomenon.

---

## AI Wayback Machine

**Émilie du Châtelet** translated Newton's *Principia* into French and added a commentary that introduced the concept of kinetic energy as $mv^2$ — refining Newton's framework for working physicists. Her version was the standard text on Newtonian mechanics in France for a century.

**Run this:**

```
Who was Émilie du Châtelet, and how does her translation of Newton
connect to the dynamics we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about her career
or ideas.
```

→ Search **"Émilie du Châtelet"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through du Châtelet's $mv^2$ argument and contrast it with Newton's momentum-based framing.
- Ask it about her partnership with Voltaire — and her death in childbirth at 42.

What changes? What gets better? What gets worse?

---

*Tags: Newtons-laws; force; free-body-diagram; third-law; inertia; dynamics; weight; mass*
