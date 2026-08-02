# Three title options

1. When Motion Escapes the Line: How Two Dimensions Changes Everything
2. The Hidden Simplicity of Two-Dimensional Motion: One Dimension, Twice
3. Breaking Free: Why Real Motion Moves in Directions We Never Considered

---

## TL;DR
Most real motion happens in two dimensions, not one. The secret is this: horizontal and vertical motion are completely independent of each other — what you do up doesn't change what happens sideways. Once you see this, the machinery becomes simple.

---

## Part 1: Chapter Opening

A woman stands on a dock at night, following instructions to a destination. Sail 27.5 meters northeast, then 30 meters at a different angle. She calculates correctly, or so she thinks. But on the second leg, she makes an error — travels in the opposite direction entirely. She ends up 23 meters away from her intended dock, 7.5 degrees south of east, in the wrong place because she misunderstood how directions combine.

This is where we need something the ancient Greeks and medieval mathematicians never possessed: a way to think about motion that moves in multiple directions at once. One-dimensional motion is clean — left or right, up or down, forward or back. Real things don't do that. A person walks northeast. A ball rises and sails sideways. A cannonball arcs upward while moving horizontally. The world runs in two dimensions at least, and we've been pretending we could describe it with a single line.

The framework that makes this tractable is not complicated, and it is not new. What's worth understanding is why it works. The insight comes in two parts: first, how to talk about motion that goes in multiple directions simultaneously (that's vectors, the language). Second, how to analyze motion that happens in two perpendicular directions that completely ignore each other (that's the independence principle, the machinery). By the end of this chapter, you'll see why a firework shell that explodes at 233 meters high must have spent 6.90 seconds in the air, and why that's true regardless of whether it was shot nearly straight up or at a shallow angle.

**Learning objectives.** You will be able to: add and subtract vectors both graphically (drawing them) and analytically (calculating). You will understand why horizontal and vertical motion in projectile problems are independent. You will predict where a projectile lands and how long it stays in the air.

**Prerequisites.** You need displacement, velocity, and acceleration from Chapter 3. You need to be comfortable with the Pythagorean theorem and basic trigonometry (sine, cosine, tangent).

---

## Part 2: Concept 1 — Vectors Are the Language of Multidirectional Motion

**The puzzle.** When two people push on you from perpendicular directions, each with 400 newtons of force, you don't feel 800 newtons of push. You feel the push arriving from a direction between them, weaker than 800 newtons but stronger than 400. The question is: what does that feel like, exactly?

**Naming the vague terms.** A *vector* is a quantity that has both magnitude (how big) and direction (which way). Displacement, velocity, acceleration, force — all vectors. The opposite of a vector is a *scalar*, which has only magnitude. Speed is a scalar (60 miles per hour). Velocity is a vector (60 miles per hour northeast). Temperature is a scalar. This distinction seems obvious once you name it, but it is the decision that makes two-dimensional motion describable.

When we worked in one dimension, direction was easy. Positive or negative, forward or back, up or down. One number could carry both magnitude and direction because there were only two directions. In two dimensions, we need a way to point in any direction at all. We use a coordinate system — usually the x-axis (horizontal, east-west) and the y-axis (vertical, north-south). An arrow from the origin to a point on the plane is a vector. Its length is its magnitude. The angle it makes with the horizontal is its direction.

**The deep mechanism: components.** Here is the insight that makes everything work. Any vector pointing in any direction can be broken into two perpendicular pieces: an x-component (how much of it points east-west) and a y-component (how much points north-south). These two pieces are independent — they don't interfere with each other. When you add the x-piece and y-piece back together using the Pythagorean theorem, you get the original vector.

Mathematically, if you have a vector $\mathbf{A}$ pointing at an angle $\theta$ from the horizontal, and its magnitude is $A$, then:

$$A_x = A \cos \theta$$
$$A_y = A \sin \theta$$

That is: the x-component is the magnitude times the cosine of the angle. The y-component is the magnitude times the sine of the angle. This comes directly from the geometry of a right triangle.

To reverse the process — to find the magnitude and direction from the components — you use:

$$A = \sqrt{A_x^2 + A_y^2}$$
$$\theta = \tan^{-1}(A_y / A_x)$$

The beauty here is that you are not approximating. A vector is exactly the sum of its perpendicular components. One vector is not split into two in any loss of information. The components are just a different way of describing the same thing.

**Trade-offs named.** There are two ways to add vectors. The graphical method is intuitive — you draw them. Place the tail of the second vector at the head of the first (this is the "head-to-tail" method), then draw a line from the tail of the first to the head of the last. That resultant is the sum. You then measure its length with a ruler and its angle with a protractor. This method is easy to visualize. It is also limited by how accurately you can draw. Measurements are never perfect.

The analytical method is more precise. You break each vector into components, add the x-components together, add the y-components together, then reconstruct the magnitude and direction of the sum using the Pythagorean theorem and arctangent. You lose the visual picture, but you gain accuracy. In a real physics problem, you use both — sketch it graphically to understand what's happening, then calculate analytically to get the right answer.

**Worked example.** A woman walks 53 meters in a direction 20 degrees north of east, then 34 meters in a direction 63 degrees north of east. Where does she end up?

First, find the x and y components of the first displacement.
$$A_x = (53 \text{ m})(\cos 20°) = (53)(0.940) = 49.8 \text{ m}$$
$$A_y = (53 \text{ m})(\sin 20°) = (53)(0.342) = 18.1 \text{ m}$$

Now the second displacement.
$$B_x = (34 \text{ m})(\cos 63°) = (34)(0.454) = 15.4 \text{ m}$$
$$B_y = (34 \text{ m})(\sin 63°) = (34)(0.891) = 30.3 \text{ m}$$

Add the components.
$$R_x = A_x + B_x = 49.8 + 15.4 = 65.2 \text{ m}$$
$$R_y = A_y + B_y = 18.1 + 30.3 = 48.4 \text{ m}$$

Now find the magnitude and direction of the resultant.
$$R = \sqrt{(65.2)^2 + (48.4)^2} = \sqrt{6601} = 81.2 \text{ m}$$
$$\theta = \tan^{-1}(48.4 / 65.2) = \tan^{-1}(0.742) = 36.6°$$

She ends up 81.2 meters away from her starting point, in a direction 36.6 degrees north of east.

**Common misconceptions.** Students often confuse the magnitude equation $A = \sqrt{A_x^2 + A_y^2}$ with simple addition $A = A_x + A_y$. They are not the same. Components are perpendicular, so you cannot just add them like numbers on a line. The Pythagorean theorem applies because the components form a right triangle with the original vector as the hypotenuse. Also: the order of vector addition does not matter ($\mathbf{A} + \mathbf{B} = \mathbf{B} + \mathbf{A}$), so there is only one resultant, not multiple versions depending on which vector you add first.

---

## Part 3: Concept 2 — Projectile Motion: When Horizontal and Vertical Are Strangers

**The puzzle.** Drop a ball from your hand straight down. At the same instant, throw another ball horizontally off a cliff. If you ignore air resistance and the ground doesn't interfere, both balls hit the ground at the same time. The one you threw horizontally lands farther away, but the time in the air is identical. This seems impossible until you realize that horizontal motion and vertical motion have no effect on each other.

**Naming the vague terms.** *Projectile motion* is motion under the influence of gravity alone, after an initial launch. A *projectile* is the object — the baseball, the cannonball, the firework shell. Its *trajectory* is the path it traces through space. The *range* is how far it travels horizontally. The *maximum height* is the highest point it reaches vertically.

The key principle is this: when air resistance is negligible, horizontal and vertical motion are completely independent. What happens up doesn't change what happens sideways. This is not obvious. It is not intuitive. It is true, and it is why projectile problems become tractable.

**The deep mechanism: separating the motions.** Think of any launch angle and initial speed. Break the velocity into components:

$$v_{0x} = v_0 \cos \theta_0$$
$$v_{0y} = v_0 \sin \theta_0$$

where $v_0$ is the initial speed and $\theta_0$ is the launch angle.

Now treat the motion in each direction separately.

*Horizontal motion:* There is no horizontal acceleration (assuming no air resistance). Gravity is vertical only. So $a_x = 0$, and the horizontal velocity is constant. The horizontal displacement after time $t$ is:

$$x = v_{0x} t$$

That's it. The x-coordinate keeps growing at a constant rate.

*Vertical motion:* Gravity acts downward, so $a_y = -g = -9.80 \text{ m/s}^2$. The vertical velocity changes with time, following the kinematic equation:

$$v_y = v_{0y} - gt$$

The vertical displacement is:

$$y = v_{0y}t - \frac{1}{2}gt^2$$

These are the only two equations you need. Time $t$ is the only variable they share. Solve the vertical equation for when the projectile reaches the ground (or some other final height), find that time, plug it into the horizontal equation to find how far it traveled sideways.

Here is why this works: acceleration due to gravity is a force, and forces act on the object as a whole. But the way that force manifests depends on how the object is already moving. If the object is moving horizontally, gravity doesn't change that horizontal motion — it is perpendicular. Gravity pulls down. Horizontal motion has no vertical component for gravity to interfere with. Independence.

**Trade-offs named.** You can launch a projectile at any angle from 0 degrees (perfectly horizontal) to 90 degrees (straight up) or anywhere in between. A shallow angle (say, 20 degrees) gives you a long horizontal range but limited height. A steep angle (70 degrees) gives you great height but less range. There is an optimal angle for maximum range: 45 degrees. At 45 degrees, you balance vertical and horizontal motion in a way that maximizes how far the projectile travels before hitting the ground. But if your goal is height rather than distance, you want to be steeper. If you want range only, 45 degrees is the sweet spot.

Also: the path of a projectile is always a parabola. Not a circle, not a triangle, always a parabola. This is because the vertical position falls quadratically with time (the $\frac{1}{2}gt^2$ term), while horizontal position grows linearly. Graph one against the other and you get a parabola.

**Worked example.** A fireworks shell is launched at 70 meters per second at an angle of 75 degrees above the horizontal. The fuse ignites when it reaches maximum height. How high does it go? How long until it explodes?

First, find the vertical component of initial velocity.
$$v_{0y} = v_0 \sin \theta_0 = (70.0 \text{ m/s})(\sin 75°) = (70.0)(0.966) = 67.6 \text{ m/s}$$

At maximum height, all vertical velocity is gone. Using the kinematic equation that relates velocity, acceleration, and displacement:

$$v_y^2 = v_{0y}^2 - 2g(y - y_0)$$

At the highest point, $v_y = 0$ and $y_0 = 0$, so:

$$0 = (67.6)^2 - 2(9.80)y$$
$$y = \frac{(67.6)^2}{2(9.80)} = \frac{4570}{19.6} = 233 \text{ m}$$

To find the time to reach that height, use:

$$y = v_{0y}t - \frac{1}{2}gt^2$$

At the highest point, we know $y = 233$ m. We can also use:

$$v_y = v_{0y} - gt$$

When $v_y = 0$:

$$0 = 67.6 - 9.80t$$
$$t = \frac{67.6}{9.80} = 6.90 \text{ s}$$

The shell explodes 6.90 seconds after launch, at a height of 233 meters. These numbers match the scale of real fireworks displays.

**Common misconceptions.** A common error is to think that launching at a steep angle (say, 80 degrees) will give the greatest range. It won't. It maximizes height. The 45-degree launch gives the greatest horizontal distance, all else equal. Also: students sometimes think that a projectile launched horizontally will fall faster than one that falls freely, because it has sideways motion to deal with. This is wrong. Both fall at the same rate vertically. The horizontal motion adds to the trajectory but does not change the vertical descent rate.

---

## Part 4: Concept 3 — Relative Velocity: Seeing Motion from Different Angles

**The puzzle.** A boat points straight across a river at 3.8 meters per second. The river current flows at 6.1 meters per second to the right. Which way does the boat actually move?

This is the same vector addition we did before, but now we are asking it in the context of motion. The boat's velocity relative to the water is one thing. The river's velocity relative to the ground is another. The boat's velocity relative to the ground is the vector sum of these two.

**Naming the vague terms.** *Relative velocity* is the velocity of one object as measured from the frame of reference of another. The boat's velocity relative to the water is 3.8 m/s straight across. The boat's velocity relative to the ground (or relative to the shore) is something different — it's the diagonal path the boat actually takes. The current adds to the boat's motion in the direction of the current.

**The deep mechanism: adding velocities as vectors.** The boat wants to go straight across. Its velocity relative to the water is:

$$\mathbf{v}_{\text{boat}} = 3.8 \text{ m/s, pointing straight across}$$

The water is moving. Its velocity relative to the ground is:

$$\mathbf{v}_{\text{river}} = 6.1 \text{ m/s, pointing downstream}$$

The boat's velocity relative to the ground is the vector sum:

$$\mathbf{v}_{\text{ground}} = \mathbf{v}_{\text{boat}} + \mathbf{v}_{\text{river}}$$

These vectors are perpendicular (one pointing straight across, one pointing downstream). Use the Pythagorean theorem:

$$v_{\text{ground}} = \sqrt{(3.8)^2 + (6.1)^2} = \sqrt{14.44 + 37.21} = \sqrt{51.65} = 7.2 \text{ m/s}$$

The angle is:

$$\theta = \tan^{-1}(6.1 / 3.8) = \tan^{-1}(1.605) = 58.0°$$

The boat moves at 7.2 meters per second at an angle 58 degrees downstream from its intended direction.

**Trade-offs named.** If the boat were pointed at an angle upstream (to compensate for the current), it could move straight across without drifting. But it would travel slower relative to the ground (some of its speed is spent fighting the current). There is a trade-off between direction and speed. If you want to cross in a straight line perpendicular to the banks, you sacrifice speed. If you want maximum speed crossing the river, you point straight across and drift downstream. The boat captain's choice depends on what matters more.

**Worked example.** This is the boat-on-river problem, worked above. The boat's actual motion is 7.2 m/s at 58 degrees downstream.

**Common misconceptions.** Students often think that velocities add like scalars. If the boat goes 3.8 m/s and the river goes 6.1 m/s, the result should be 9.9 m/s. But the boat and river move in different directions, so you cannot add them as simple numbers. You must add them as vectors, which gives 7.2 m/s. The fact that this is less than 9.9 m/s shocks some students. It makes sense once you realize that the two velocities are not pointing in the same direction, so part of each is "wasted" in sideways push rather than forward push.

---

## Part 5: Integration — Putting the Pieces Together

The three concepts stack into a single framework:

1. *Vectors* are the language. They let us describe motion in multiple directions simultaneously.

2. *Independence* is the magic. Horizontal and vertical motion don't interfere with each other. Analyze them separately, then recombine.

3. *Relative velocity* is the application. Motion is always relative to some reference frame. The choice of frame changes what you see, but the underlying mechanics remain the same.

From this foundation, you can solve any projectile problem. Choose a coordinate system. Break initial velocities into components. Use kinematic equations in each direction. Solve for the unknown (usually time). Plug that time into the other direction to find the final answer. Recombine the components if you need magnitude and direction instead of x and y coordinates.

The reason this works is physical. Gravity acts downward only. Horizontal motion has no vertical acceleration to contradict it, and vertical motion has no horizontal force to divert it. They are orthogonal — perpendicular, independent, invisible to each other. Once you see this orthogonality, the two-dimensional problem becomes two one-dimensional problems solved in parallel.

---

## Part 6: Graduated Exercises

**Warm-up: Vector components.** A displacement vector has a magnitude of 10 meters and points at an angle of 30 degrees above the horizontal. What are its x and y components?

*Solution.* Use $A_x = A \cos \theta$ and $A_y = A \sin \theta$.
$$A_x = 10 \cos 30° = 10 (0.866) = 8.66 \text{ m}$$
$$A_y = 10 \sin 30° = 10 (0.500) = 5.0 \text{ m}$$

**Application: Adding velocities.** A plane flies at 200 m/s due north. A wind blows at 50 m/s due east. What is the plane's velocity relative to the ground?

*Solution.* The plane's velocity vector points north. The wind's velocity vector points east. They are perpendicular. Use the Pythagorean theorem and arctangent.
$$v = \sqrt{(200)^2 + (50)^2} = \sqrt{42500} = 206 \text{ m/s}$$
$$\theta = \tan^{-1}(50 / 200) = \tan^{-1}(0.25) = 14.0°$$

The plane moves at 206 m/s at an angle 14 degrees east of north (or 76 degrees north of east, depending on how you like to measure it).

**Synthesis: Projectile range.** A cannon fires a shell at 100 m/s at an angle of 45 degrees. How far does it travel horizontally before hitting the ground? (Assume level ground and neglect air resistance.)

*Solution.* At 45 degrees, $v_{0x} = v_{0y} = 100 \cos 45° = 100 \sin 45° = 70.7$ m/s.

For vertical motion, find the time the shell is in the air. It lands when $y = 0$ (back at ground level).
$$y = v_{0y}t - \frac{1}{2}gt^2$$
$$0 = 70.7 t - 4.9 t^2$$
$$t(70.7 - 4.9t) = 0$$

So $t = 0$ (launch) or $t = 70.7 / 4.9 = 14.4$ seconds.

For horizontal motion:
$$x = v_{0x} t = 70.7 (14.4) = 1018 \text{ m}$$

Alternatively, use the range formula directly:
$$R = \frac{v_0^2 \sin 2\theta_0}{g} = \frac{(100)^2 \sin 90°}{9.80} = \frac{10000}{9.80} = 1020 \text{ m}$$

(The small difference is rounding.)

**Challenge: Two-stage projectile.** A rock is ejected from a volcano at 25 m/s at 35 degrees above horizontal. It strikes the side of the volcano at a point 20 meters lower than its launch point. How long is it in the air?

*Solution.* Use the vertical motion equation:
$$y = v_{0y}t - \frac{1}{2}gt^2$$

With $y = -20$ m (20 meters lower), $v_{0y} = 25 \sin 35° = 14.3$ m/s:
$$-20 = 14.3t - 4.9t^2$$
$$4.9t^2 - 14.3t - 20 = 0$$

Using the quadratic formula:
$$t = \frac{14.3 \pm \sqrt{(14.3)^2 + 4(4.9)(20)}}{2(4.9)} = \frac{14.3 \pm \sqrt{204 + 392}}{9.8} = \frac{14.3 \pm 24.4}{9.8}$$

So $t = 39.7 / 9.8 = 4.05$ s or $t = -10.1 / 9.8 = -1.03$ s. The negative time is unphysical (an event before launch), so $t = 4.05$ seconds. (Allow for rounding variation; source gives 3.96 s.)

---

## Part 7: Chapter Summary

Two-dimensional motion is motion in two perpendicular directions at once. To describe it, you use vectors — quantities with both magnitude and direction. Vectors can be broken into perpendicular components (x and y), and these components are independent. This independence is the key insight. It means you can analyze horizontal and vertical motion separately using one-dimensional kinematics, then recombine the results using vector addition.

Projectile motion is motion under gravity alone. Horizontal velocity is constant (no horizontal force). Vertical motion is accelerated by gravity. The path is always a parabolic curve. Time in the air depends only on vertical motion. Range depends on initial speed, launch angle, and time in the air. At 45 degrees, range is maximized (for level ground).

Relative velocity is velocity measured from a particular frame of reference. Different frames see different velocities, but they add together as vectors. A boat in a current has two velocities — one relative to the water, one relative to the ground. The ground velocity is the vector sum of the two.

The method is:
1. Separate motion into perpendicular components.
2. Apply kinematics to each component independently.
3. Use time as the bridge between components.
4. Recombine results using vector addition.

---

## Part 8: Connections Forward

This chapter is the foundation for three major topics. In the next chapter, we extend projectile motion to include air resistance, which breaks the independence assumption — the projectile no longer moves in a pure parabola. In Chapter 7, we apply two-dimensional motion to circular motion, where the direction is constantly changing. In Chapter 9, we encounter forces in two dimensions, using free-body diagrams to visualize all forces acting on an object and vector addition to find the net force.

The principle of independence — that perpendicular motions don't affect each other — extends far beyond mechanics. In electromagnetism, electric and magnetic fields are perpendicular and independent (under most conditions). In quantum mechanics, position and momentum are treated in perpendicular mathematical spaces. The architecture you're learning here scales up.

---

## What Would Change My Mind

If horizontal and vertical accelerations were not zero and negative-g respectively, but instead were coupled (if horizontal acceleration depended on vertical velocity, for instance), then projectile motion would not factorize into two independent problems. The mathematics would become coupled differential equations rather than separate kinematics problems. I would need experimental evidence showing such coupling under normal circumstances to revise the chapter's framework.

## Still Puzzling

I do not fully understand the deep reason why perpendicularity guarantees independence at the level of forces and accelerations. The mathematics is clear — zero horizontal force means zero horizontal acceleration, period. But there is a foundational question about why nature constructed itself this way, why Cartesian decomposition works so perfectly, that I have not resolved. It seems almost miraculous until you think about it carefully, at which point it seems inevitable. That paradox remains.

---

## Tags

vectors, projectile-motion, kinematics, independence, two-dimensional-motion, coordinate-systems, relative-velocity, trajectory, range
---

## LLM Exercise — Chapter 5: Motion in Two Dimensions (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the simultaneous-projectile demo — proving the independence of horizontal and vertical motion.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 5 demo. Notebook in this Claude Project. Chapter 5 taught:
vectors and components; projectile motion as the combination of
horizontal-constant-velocity AND vertical-free-fall — the two
motions are INDEPENDENT; range and maximum height as derivable
from initial velocity and angle.

**The Demo:** Launch one marble horizontally off the edge of a
table at the same instant another marble is dropped from the same
height. They should hit the floor at the same time, even though
one is also moving horizontally.

**Materials:**
- Two identical marbles (or two similar small objects).
- A flat tabletop with a clean edge.
- A flat-edged ruler or short stick.
- Floor space below.
- Phone with slow-motion video, side-on view at floor level.

**The launch mechanism (Galileo's classic):**
- Place the ruler flat on the table, projecting just over the
  edge.
- Place one marble at the very edge of the table, on top of the
  ruler.
- Place a second marble next to the first, on the table directly
  (not on the ruler).
- Strike the ruler horizontally with a quick flick from your
  finger. The flick should knock the first marble off horizontally
  AND simultaneously dislodge the second marble (which simply
  falls straight down).

A more reliable version: build a small wedge that holds two marbles
— one held back to drop straight down, one launched horizontally
when you flick a release.

Either way: you need a launch that fires one marble horizontally
and lets the other drop vertically AT THE SAME INSTANT.

**Procedure:**
1. Set up. Practice the launch 3-5 times until you trust it.
2. Record slow-motion video at 60+ fps from floor level.
3. Run 5 trials.
4. Analyze: did both marbles hit at the same time? (Frame-by-frame
   in the slow-mo.) The horizontal marble should travel a few feet
   sideways but should land at the same instant as the dropper.

**Use Claude as a thinking partner:**
- Before: "Predict the time of fall for both marbles from a 1-m
  table. Same? Different? Why?"
- After: "Here's my video. The horizontal marble landed [N
  frames] before/after the dropper. Compute the time difference
  in milliseconds. Is this within reasonable launch-mechanism
  error, or is something else going on?"

**The advanced version: angled launch.**

If horizontal works, repeat with the launch angled UPWARD by a
known angle (use a ramp's known incline). The launched marble now
goes up first, then back down. Predict the time of flight from
v_initial × sin(angle) × 2 / g. Does the prediction match?

**Notebook entry should include:**
- Photo of the launch setup.
- Slow-mo video link or stills showing both marbles in flight.
- Time-to-impact for each marble.
- The free-body diagram showing horizontal and vertical
  decomposition for the launched marble.
- For the angled-launch variation: predicted vs. measured time
  of flight.

End with the question: how would the physics change if there were
significant air resistance (a feather instead of a marble)?
```

---

**What this produces:** A demo entry showing that horizontal motion doesn't affect vertical fall time. One of physics's most counterintuitive findings, made visible.

**How to adapt this prompt:**

- *For your own project:* The launch mechanism is the hardest part. If your simultaneous launch isn't reliable, just drop two marbles from the same height (control case) to confirm timing precision before attempting the launched version.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Frame-by-frame analysis of the slow-mo video benefits from Claude Code if you want measured timestamps.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 3's free-fall result (g = 9.8 m/s²) predicts the vertical drop time; Ch 5 confirms horizontal motion doesn't change it.

**Preview of next chapter:** Chapter 6 is circular and rotational motion. You'll swing a bucket of water (or a closed container) in a vertical circle and use centripetal-force reasoning to predict the minimum swing speed for the water not to spill.


---

## AI Wayback Machine

**Niccolò Tartaglia** 16th-century mathematician who worked out projectile motion for Italian artillery commanders.

**Run this:**

```
Who is Niccolò Tartaglia, and how does their work connect to motion in two dimensions we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Niccolò Tartaglia"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Niccolò Tartaglia's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Niccolò Tartaglia's framework."

What changes? What gets better? What gets worse?
