# Applications of Newton's Laws — Friction, Drag, and Centripetal Force

## Suggested titles

1. When Newton's Laws Meet the Real World — Friction, Air Resistance, and Curves
2. How Objects Really Move — Hidden Forces That Change Everything
3. Beyond Acceleration — What Happens When Forces Push Back

---

## TL;DR

When you apply a force to an object, the world pushes back. Friction opposes your push; air resistance increases with speed; curves demand invisible forces pointing inward. Newton's laws tell you the rules, but this chapter shows you how to see the forces that actually live in the world.

---

## Chapter Opening — The Three Places Where Things Get Real

Talladega Superspeedway, turn three, on a Sunday in spring. A NASCAR driver sits in a car that weighs just over 1,500 kilograms and moves through the banked curve at 320 kilometers per hour. The turn has a 33-degree banking — the track surface tilts steeply, like a wall leaning inward. The driver does not grip the wheel any harder through the turn. He does not lean. The car doesn't slip sideways, and nobody watching thinks it's about to crash.

Now imagine the same car on a flat parking lot, on level ground, traveling at the same speed. It immediately slides off into the adjacent county.

The difference is invisible. It lives in how the ground pushes on the tires, how gravity pulls downward, how the track's angle lets the normal force do something it couldn't do on flat pavement. None of this appears in the cartoon version of Newton's second law — the one where you draw a box, attach arrows, and report the acceleration. The real work of engineering and physics happens in understanding what forces actually act on an object moving through the actual world, where friction refuses to disappear, where air pushes back harder as you go faster, and where moving in a circle requires a constant push toward the center.

This chapter takes Newton's three laws — the ones you now know by heart — and drops them into three real situations where they matter. In each, a force you can almost ignore at slow speeds or over short distances becomes the whole story.

### Learning objectives

By the end of this chapter, you will be able to:

- Distinguish static friction from kinetic friction and express each mathematically using the coefficient of friction and the normal force.
- Solve problems with friction on horizontal and inclined surfaces, including the special case where an object slides at constant velocity.
- Model the behavior of drag force as proportional to velocity squared (for large objects at moderate to high speeds) and derive terminal velocity from the condition of force balance.
- Solve differential equations describing motion under velocity-dependent drag, showing how velocity approaches a limiting value over time.
- Apply Newton's second law to circular motion, derive the centripetal force requirement from the kinematic expression $a_c = v^2/r$, and solve banked-curve problems without invoking friction.
- Recognize inertial forces as artifacts of noninertial reference frames and distinguish the Coriolis force from the fictitious centrifugal force.

### Prerequisites

- Comfort with Newton's three laws and free-body diagrams.
- Ability to resolve vectors into components.
- Calculus I: derivatives, integrals, and separation of variables in differential equations.
- Familiarity with trigonometry on inclined planes from Chapter 5.

### Why this chapter matters

Friction seems obvious until you ask *why* it exists and *when* it changes. Drag seems like air resistance until you realize the same force launches airplanes and keeps the climate stable. Centripetal force seems mysterious until you see it's not a new force at all — it's just the name for whatever force points toward the center of a curve. Once you understand these three, you can solve problems that range from a crate sliding down a ramp to a skydiver reaching terminal velocity to a car navigating a banked turn without slipping. More than that: you understand the world as it actually behaves, not the simplified model.

---

## Concept 1 — Static and Kinetic Friction: The Force That Wakes When You Try to Move

### Hook: The crate problem

Push on a heavy wooden crate. The crate doesn't move. You push harder. It still sits there. You push *much* harder — enough that your arm aches — and suddenly the crate seems to slip and start moving. Once it's in motion, you notice something odd: you need *less* force to keep it moving at constant speed than you needed to get it moving in the first place.

This is friction. It is not a constant force. It is a responsive force — it grows as you push, up to a limit, then drops the moment the object starts to slide.

### What friction actually is (and what it isn't)

Friction opposes motion (or attempted motion) between two objects in contact. The mechanics of it are not simple. At the microscopic scale, the two surfaces are not smooth. They have tiny peaks and valleys. When you try to slide one across the other, you must either break apart the adhesive bonds between surface molecules or raise one object so that only the peaks touch, letting it skip across the valleys without fully making contact. The harder you press the surfaces together, the more molecular contact you create, and the more force you need to overcome it.

Here are the two types:

**Static friction** acts when two surfaces are not moving relative to each other. If you push a crate with 50 newtons and it doesn't move, static friction is pushing back with 50 newtons. If you push with 100 newtons and it still doesn't move, static friction pushes back with 100 newtons. Static friction matches your push, *up to a maximum*. Once you exceed that maximum, the object slides.

**Kinetic friction** acts when two surfaces *are* moving relative to each other. Once the crate starts to slide, kinetic friction takes over. Kinetic friction is roughly constant — it no longer grows to match your push. That's why the crate accelerates once you give it the extra nudge.

### The mathematics of friction

The coefficients of static and kinetic friction — written $\mu_s$ and $\mu_k$ — describe how much friction a particular pair of surfaces creates. Rubber on dry concrete has $\mu_s \approx 1.0$; waxed wood on wet snow has $\mu_s \approx 0.14$. The human knee joint, lubricated by synovial fluid, has $\mu_s \approx 0.016$. These are empirical facts, measured in laboratories and real-world conditions.

The magnitude of static friction satisfies an inequality:

$$f_s \leq \mu_s N$$

where $N$ is the normal force (the force perpendicular to the surface, pressing the two objects together). The $\leq$ symbol is the key. Static friction *can* reach $\mu_s N$, but it doesn't always. It can be anything from zero up to that maximum.

Kinetic friction has no inequality:

$$f_k = \mu_k N$$

Once an object is sliding, kinetic friction equals the product of $\mu_k$ and the normal force, no more, no less. Notice that $\mu_k < \mu_s$ always — kinetic friction is less than the maximum static friction. That's why it's easier to keep something moving than to get it started.

### The trade-off: Responsiveness vs. friction

Static friction is responsive — it grows to meet whatever you do, up to its limit. Kinetic friction is constant — once you're moving, the friction doesn't change if you speed up or slow down (as long as you keep sliding). This creates a design problem in any system with friction.

Consider a brake on a bicycle. You want a system that *does not* slip at low speeds (static friction keeps you in place) but *does* slip smoothly once you start moving (kinetic friction brings you to a stop without stuttering). Drum brakes or disc brakes must manage this transition. Get it wrong and you either lock the brakes (uncontrolled skidding) or fail to stop (insufficient friction).

The same trade-off shows up in the design of shoes, tires, and joint replacements. You want maximum grip (high $\mu_s$) but smooth motion once contact begins (reasonable $\mu_k$). Evolution solved this problem in animal joints by introducing a lubricating fluid; engineering solves it with surface treatments and materials science.

### Worked example — Block on a horizontal surface, deciding which type of friction acts

A 20-kilogram crate rests on a floor. The coefficient of static friction is $\mu_s = 0.70$; the coefficient of kinetic friction is $\mu_k = 0.60$. A horizontal force $P$ is applied to the crate.

(a) If $P = 20.0$ N, what is the friction force?
(b) If $P = 120.0$ N, what is the friction force?
(c) If $P = 180.0$ N, what is the friction force and the resulting acceleration?

**Given:** $m = 20.0$ kg, $\mu_s = 0.70$, $\mu_k = 0.60$.

**Solution:**

First, find the normal force. Since there is no vertical acceleration: $N = mg = (20.0)(9.80) = 196$ N.

The maximum static friction is: $f_{s,\max} = \mu_s N = (0.70)(196) = 137$ N.

**(a) $P = 20.0$ N:**

Since $P = 20.0$ N $< 137$ N, the crate does not move. Static friction matches the applied force: $f_s = 20.0$ N (pointing opposite to $P$).

**(b) $P = 120.0$ N:**

Since $P = 120.0$ N $< 137$ N, the crate still does not move. Static friction: $f_s = 120.0$ N.

**(c) $P = 180.0$ N:**

Since $P = 180.0$ N $> 137$ N, the crate overcomes static friction and begins to slide. Now kinetic friction acts:

$$f_k = \mu_k N = (0.60)(196) = 118 \text{ N}$$

Applying Newton's second law horizontally:

$$F_{\text{net}} = P - f_k = ma$$
$$180.0 - 118 = (20.0) a$$
$$a = 3.10 \text{ m/s}^2$$

**Check:** The applied force exceeds the maximum static friction, so sliding occurs. Kinetic friction then reduces the net force, but not to zero, so the crate accelerates. This matches intuition.

**General lesson:** Before solving a friction problem, ask: Is this object moving? If not, try static friction (it adjusts to match the applied force, up to $\mu_s N$). If yes, use kinetic friction ($\mu_k N$). The answer to that question determines which equation you use.

### Common misconceptions

**Static friction always equals $\mu_s N$.** Wrong. It can be *anything* from zero up to $\mu_s N$. Only when the object is on the verge of sliding does static friction equal $\mu_s N$.

**Kinetic friction depends on speed.** Wrong. The formula $f_k = \mu_k N$ applies at any speed, as long as the object is sliding. Kinetic friction is (approximately) independent of how fast you're moving.

**Friction always slows things down.** Wrong. Friction between your foot and the ground propels you forward. Friction between a car's tires and the road lets it accelerate and turn. Friction can speed you up, slow you down, or change your direction — depending on which way it acts.

---

## Concept 2 — Drag and Terminal Velocity: When the Air Pushes Back So Hard That Acceleration Stops

### Hook: The skydiver problem

A skydiver jumps from 4,000 meters. For the first few seconds, she accelerates downward at nearly $g = 9.8$ m/s² — the pull of gravity, nearly unopposed. But as her speed increases, the air begins to push back harder. At 30 m/s, the push is noticeable. At 50 m/s, it's substantial. By 55 m/s (about 200 km/h or 120 mph), something strange happens: the upward push of the air exactly balances the downward pull of gravity. The net force becomes zero. The skydiver stops accelerating.

She is now falling at constant velocity — a speed at which the forces balance. Slow down a little, and gravity pulls harder than air pushes, so she accelerates back up to that speed. Speed up a little, and air pushes harder than gravity pulls, so she decelerates back down. This constant-velocity fall is called **terminal velocity**, and it emerges naturally from Newton's second law once you write down what drag actually does.

### What drag is (and why it matters)

Drag is a force exerted by a fluid (air or water) on an object moving through it. Unlike friction between solid surfaces, which is (roughly) independent of speed, drag increases with speed. For a large object moving at moderate to high speed through air — a car, a baseball, a skydiver — the drag force is proportional to the square of the speed:

$$F_{\text{drag}} = \frac{1}{2} C \rho A v^2$$

where:

- $C$ is the **drag coefficient**, a dimensionless number depending on the object's shape. A streamlined airfoil has $C \approx 0.05$; a skydiver in horizontal position has $C \approx 1.0$; a flat plate perpendicular to the flow has $C \approx 1.12$.
- $\rho$ is the **density of the fluid**. Air at sea level has $\rho \approx 1.21$ kg/m³. Water is about 800 times denser.
- $A$ is the **cross-sectional area** of the object facing the fluid, in square meters.
- $v$ is the speed.

The $v^2$ dependence is crucial. Double your speed, and drag increases by a factor of four. This is why racing cyclists and swimmers wear tight bodysuits to reduce $A$, and why race cars are designed with low drag coefficients. At highway speeds, over half a car's engine power goes to overcoming drag.

### Terminal velocity — the emergence of a limit

Imagine a skydiver falling through air. Two forces act: gravity downward, $F_g = mg$; drag upward, $F_{\text{drag}} = \frac{1}{2} C \rho A v^2$.

Newton's second law says:

$$mg - F_{\text{drag}} = ma$$

As the skydiver falls and speeds up, $F_{\text{drag}}$ grows. At some speed — call it $v_T$ — the drag force exactly equals the gravitational force. Then:

$$mg - \frac{1}{2} C \rho A v_T^2 = 0$$

Solving for $v_T$:

$$v_T = \sqrt{\frac{2mg}{\rho C A}}$$

This is the terminal velocity. At this speed, acceleration is zero, and the skydiver continues falling at constant velocity.

Notice what the formula says: heavier objects (larger $m$) have *higher* terminal velocities. A 75-kg skydiver falling head-first (small $A$, low $C$) reaches $v_T \approx 98$ m/s (about 350 km/h or 220 mph). The same person in spread-eagle position (large $A$, higher $C$) reaches only $v_T \approx 50$ m/s (about 180 km/h or 110 mph). A 50-kg person would reach roughly 53 m/s in head-first position. This matches experience: heavier divers go faster, and changing your body position changes your speed dramatically.

### The calculus of velocity-dependent drag

For smaller objects moving slowly through a denser fluid (a bacterium in water, a raindrop falling through air), drag is proportional to velocity, not velocity squared: $F_{\text{drag}} = bv$ (Stokes' law). This leads to a differential equation with a different character.

Consider an object falling under gravity with linear drag. Taking downward as positive:

$$mg - bv = m \frac{dv}{dt}$$

Rearranging:

$$\frac{dv}{g - (b/m)v} = dt$$

This is separable. Integrating both sides from $t = 0$ (where $v = 0$) to time $t$ (where $v = v(t)$):

$$\int_0^v \frac{dv'}{g - (b/m)v'} = \int_0^t dt'$$

The left side is a standard logarithmic integral. Evaluating:

$$-\frac{m}{b} \ln\left(g - \frac{b}{m}v\right) \Big|_0^v = t$$

$$-\frac{m}{b} \left[ \ln\left(g - \frac{b}{m}v\right) - \ln(g) \right] = t$$

Since $\ln A - \ln B = \ln(A/B)$:

$$-\frac{m}{b} \ln\left( \frac{g - (b/m)v}{g} \right) = t$$

Taking the exponential of both sides:

$$\frac{g - (b/m)v}{g} = e^{-bt/m}$$

Solving for $v$:

$$v(t) = \frac{mg}{b} (1 - e^{-bt/m})$$

Here is what this tells you: at $t = 0$, $v = 0$. As $t \to \infty$, the exponential term vanishes, and $v \to mg/b$. This limiting velocity is the terminal velocity for linear drag. But notice the path: velocity rises quickly at first, then more slowly, asymptotically approaching the limit. The object never quite reaches terminal velocity in finite time, but it gets very close. For practical purposes, after a time $t \sim 5m/b$, the object is at 99% of terminal velocity.

### Worked example — A skydiver and two body positions

An 85-kg skydiver falls in spread-eagle position. The cross-sectional area is $A = 0.70$ m², the drag coefficient is $C = 1.0$. Air density is $\rho = 1.21$ kg/m³. What is the terminal velocity?

**Given:** $m = 85$ kg, $A = 0.70$ m², $C = 1.0$, $\rho = 1.21$ kg/m³, $g = 9.80$ m/s².

**Solution:**

$$v_T = \sqrt{\frac{2mg}{\rho C A}} = \sqrt{\frac{2(85)(9.80)}{(1.21)(1.0)(0.70)}}$$

$$v_T = \sqrt{\frac{1666}{0.847}} = \sqrt{1967} = 44 \text{ m/s}$$

Converting: $44$ m/s $\times 3.6 = 158$ km/h $\approx 98$ mph.

**Check:** This matches measured values for a spread-eagle skydiver. A person in head-first position with half the area would have a terminal velocity about $\sqrt{2} \approx 1.4$ times higher, roughly 62 m/s.

**General lesson:** Terminal velocity depends on four factors: the object's weight (heavier = faster), its shape (drag coefficient), its size (cross-sectional area), and the density of the fluid. Change any one, and the terminal velocity changes. This is why raindrops fall gently (small mass, low terminal velocity) while ball bearings sink quickly through water (large mass, small area, high terminal velocity).

### Common misconceptions

**Drag is just air resistance.** Drag is a general phenomenon. Water exerts drag on fish and submarines. Honey exerts drag on a falling marble. Any fluid exerts drag.

**Terminal velocity is instantaneous.** An object approaching terminal velocity spends its first few seconds accelerating downward. Terminal velocity is a limit that is approached, not achieved in finite time (though in practice it's reached very quickly).

**Heavier objects fall faster than light objects in the same fluid.** True in free fall (both accelerate at $g$), but with drag involved, the answer depends on the ratio of mass to cross-sectional area. Two identical shapes fall at the same terminal velocity regardless of size, as long as they're made of the same material (so density is the same). A heavier object *of different shape* can fall faster or slower depending on how its area changes.

---

## Concept 3 — Centripetal Force and Banked Curves: How Things Move in Circles Without Slipping

### Hook: The NASCAR turn

The driver at Talladega navigates turn three at 320 km/h on a 33-degree banked curve. The road pushes up on the car not straight up, but at an angle — perpendicular to the surface. This normal force has two components: one pointing straight up (to balance gravity) and one pointing horizontally inward (toward the center of the turn). It is this inward component that makes circular motion possible.

If the banking angle is just right for this speed, friction doesn't enter the problem. The normal force alone does the work. This is called an **ideally banked curve** — the geometry of the road makes it possible to navigate the turn without slipping, with no help from friction.

Understand this one scenario, and you understand why highways are banked, why aircraft bank when they turn, and why a bicycle leans into a turn at a specific angle.

### Centripetal force — the requirement of circular motion

From Chapter 4, you know that circular motion requires constant acceleration toward the center of the circle, with magnitude:

$$a_c = \frac{v^2}{r}$$

where $v$ is the speed and $r$ is the radius of the circular path. Newton's second law says that to produce this acceleration, you need a net force toward the center. Call this the **centripetal force**:

$$F_c = m a_c = m \frac{v^2}{r}$$

Centripetal force is not a new type of force. It is the name for whatever force (or combination of forces) points toward the center and keeps an object moving in a circle. For a car on a curve, it might be friction. For a satellite orbiting Earth, it is gravity. For a ball on a string, it is tension. For a car on a banked curve at the ideal speed, it is the inward component of the normal force.

The key insight: $F_c$ must equal $m v^2 / r$. If the actual inward force is less than this, the object slides outward. If it is more, the object slides inward. Only at $F_c = m v^2 / r$ is circular motion at constant speed sustainable.

### The banked curve — geometry does the work

Consider a car of mass $m$ rounding a banked curve. The road is tilted at angle $\theta$ from horizontal. The car sits on the road, so the normal force $N$ acts perpendicular to the surface. This normal force has two components:

- Vertical: $N \cos \theta$ (upward)
- Horizontal: $N \sin \theta$ (inward, toward the center of curvature)

For the car not to slide off the road vertically, the vertical component must balance gravity:

$$N \cos \theta = mg \quad \text{...(1)}$$

For the car to stay on its circular path, the horizontal component must provide the centripetal force:

$$N \sin \theta = m \frac{v^2}{r} \quad \text{...(2)}$$

Divide equation (2) by equation (1):

$$\frac{N \sin \theta}{N \cos \theta} = \frac{m v^2 / r}{mg}$$

$$\tan \theta = \frac{v^2}{rg}$$

Solving for $\theta$:

$$\theta = \tan^{-1} \left( \frac{v^2}{rg} \right)$$

This is the **ideal banking angle** for a curve of radius $r$ at speed $v$. Notice what it tells you:

- Faster speeds require steeper banking. At 100 km/h on the same curve, you need less banking. At 200 km/h, you need much steeper banking.
- Sharper curves (smaller $r$) require steeper banking.
- The banking angle *does not depend on the mass of the car*. A loaded truck and an empty car navigate the same banked curve at the same speed with the same banking angle.

At the ideal angle, no friction is needed. The road's shape alone provides the right centripetal force. In reality, roads are not banked steeply enough for highway speeds (friction provides the extra inward force), and friction allows cars to take curves at slightly higher or lower speeds without slipping.

### Worked example — An ideally banked turn

The curve at Daytona International Speedway has a radius of 100 meters and is banked at 31 degrees. What is the ideal speed (the speed at which friction is not needed)?

**Given:** $r = 100$ m, $\theta = 31°$, $g = 9.80$ m/s².

**Solution:**

From $\tan \theta = v^2 / (rg)$, we get:

$$v = \sqrt{rg \tan \theta} = \sqrt{(100)(9.80) \tan 31°}$$

$$v = \sqrt{(980)(0.6009)} = \sqrt{589} = 24.3 \text{ m/s}$$

Converting: $24.3$ m/s $\times 3.6 = 87.5$ km/h $\approx 54$ mph.

**But wait.** Daytona cars race at speeds *far* above this. How is this possible?

The answer: friction. At higher speeds, the car tends to slide outward. Static friction between tire and track provides the additional inward force. At lower speeds, the car tends to slide inward (downslope), and friction points outward to prevent that. The banking of 31 degrees is the *design point* — the angle at which operations are smooth — but the curve can handle a range of speeds because friction fills in the gaps.

**Check:** Real race tracks are banked at steep angles (often 20–35 degrees) but not as steeply as the ideal angle for racing speeds would suggest. This is because excessive banking would make the track dangerous at normal highway speeds (the kind used by safety vehicles) and would require massive maintenance.

### Inertial forces in rotating reference frames

When you sit in a car going around a curve, you feel pushed outward. Is there a force pushing you out? In the reference frame of the ground (an inertial frame), no. What is actually happening is that *you* tend to continue moving in a straight line (Newton's first law), but the *car* curves to the left. The car pushes inward on you with a centripetal force that you can feel pressing against your seat.

But in the reference frame of the car (a rotating, non-inertial frame), you can *describe* the situation differently. You feel pushed outward by a fictitious force called **centrifugal force** — force that is not "real" in the sense that it has no physical origin, but which simplifies calculations in a rotating frame. Centrifugal force is $m v^2 / r$ outward.

Be careful: centrifugal force and centripetal force are not action-reaction pairs. Centrifugal force is an artifact of choosing a non-inertial reference frame. In the inertial frame of the ground, there is only the centripetal force (from the car's seat, from friction, from the road's banking) pointing inward. In the rotating frame of the car, you can add a fictitious outward force and have everything balance, but that fictitious force has no physical source.

The **Coriolis force** is a related fictitious force that arises in rotating frames when an object is *moving* within that frame. If you slide a ball radially outward on a spinning merry-go-round, the ball curves to the right in the merry-go-round's frame (Coriolis deflection) but moves in a straight line in the ground frame. Like centrifugal force, Coriolis force is useful for calculations in rotating frames but has no physical origin. Earth's rotation introduces small Coriolis effects that matter for large-scale weather systems and ballistic trajectories, but for most everyday problems, these effects are negligible.

### Worked example — Centripetal force on a flat curve

A 900-kg car takes a flat (unbanked) curve of radius 500 m at 25 m/s. Assuming static friction supplies all the centripetal force, what is the minimum coefficient of static friction needed?

**Given:** $m = 900$ kg, $r = 500$ m, $v = 25$ m/s.

**Solution:**

The centripetal force required is:

$$F_c = m \frac{v^2}{r} = (900) \frac{(25)^2}{500} = (900) \frac{625}{500} = 1125 \text{ N}$$

On a flat surface, the normal force equals the weight: $N = mg = (900)(9.80) = 8820$ N.

The maximum static friction available is: $f_{s,\max} = \mu_s N = \mu_s (8820)$.

For the car not to slip: $f_{s,\max} \geq F_c$, so:

$$\mu_s (8820) \geq 1125$$

$$\mu_s \geq 0.13$$

The minimum coefficient of static friction is approximately 0.13. Notice that this is much smaller than the typical coefficient for rubber on pavement (0.7–0.9). So a car in good condition can easily handle this turn on a flat surface — until it rains or the pavement is oil-slicked, and $\mu_s$ drops.

**General lesson:** Banking is used to reduce the dependence on friction. A banked curve can handle a range of speeds safely because the banking provides part of the centripetal force directly, and friction adjusts for deviations from the ideal speed.

### Common misconceptions

**Centripetal force is a new force, in addition to gravity, friction, and so on.** Wrong. Centripetal force is the *name* for whatever forces point toward the center and cause circular motion. It is not a separate physical force.

**Centrifugal force pushes an object outward.** Wrong in an inertial frame. Centrifugal force is fictitious — it is an artifact of using a rotating reference frame. In the ground frame, the only force is the centripetal force pointing inward.

**A banked road is banked more steeply for safety.** Wrong. A banked road is banked at the angle where circular motion is most efficient at the *design speed*. Steeper banking doesn't make the road safer — it makes it dangerous at speeds far above or below the design speed.

**Objects moving in circles are in equilibrium.** Wrong. Objects moving in circles are *accelerating* toward the center. The net force is not zero. The net force is $m v^2 / r$ inward.

---

## Integration — How the Three Forces Work Together

Return to the Talladega turn from the opening. A NASCAR driver navigates a 33-degree banked curve of radius 300 meters at 320 km/h (about 89 m/s).

The driver does not feel the forces directly. What the driver feels is the *normal force* — the push of the seat and the road on the body. The normal force acts perpendicular to the road surface. Its inward component points toward the center of the turn; its vertical component points upward.

Using the formulas from Concept 3:

$$N \cos 33° = mg \quad \text{(vertical equilibrium)}$$

$$N \sin 33° = m \frac{v^2}{r} \quad \text{(centripetal force)}$$

From the first equation, $N = mg / \cos 33°$. The second equation then gives:

$$\frac{mg \sin 33°}{\cos 33°} = m \frac{v^2}{r}$$

$$g \tan 33° = \frac{v^2}{r}$$

$$g (0.6494) = \frac{(89)^2}{300}$$

$$6.37 \text{ m/s}^2 = 26.4 \text{ m/s}^2$$

Wait. This doesn't balance. The banking alone doesn't provide enough centripetal force for this speed.

The reason: NASCAR drivers run faster than the ideal banking angle supports. Friction provides the additional inward force. The net effect is that the driver leans inward in the car seat — the friction from the seat (and the car's setup) provides a force pushing the driver toward the center of the turn in addition to the component of the normal force.

But notice: the banking does most of the work. The inward component of the normal force points toward the center at 33 degrees, reducing the dependence on friction. On a flat road (zero banking), friction would have to provide *all* the centripetal force, and the minimum coefficient of friction required would be $v^2 / (rg) = 26.4 / 9.80 \approx 2.7$. That is impossible for car tires. Banking makes high-speed turns possible.

Now apply Concept 2. The car is moving at 320 km/h through air. Drag is substantial. The engine must work hard to overcome the drag force, which is proportional to $v^2$. This is the cost of banking without friction — the car can take the turn safely, but the air resistance at high speed demands enormous power just to maintain speed in a steady turn.

Finally, apply Concept 1. The tires grip the road through friction between rubber and asphalt. The coefficient of static friction between racing slicks and the track surface at Talladega is about $\mu_s \approx 1.2$. This is exceptionally high — it requires soft rubber that wears quickly. The friction that provides the additional centripetal force also heats up the tires, which affects the coefficient itself. The pit crew monitors tire temperature because rubber becomes slicker when it overheats and grips less well when it's cold. The interplay between banking, drag, friction, temperature, and centripetal force is the machinery of high-speed racing.

---

## Exercises

### Warm-up

**Exercise 1** *(LO: static vs. kinetic friction).* A 50-kg block rests on a horizontal floor. The coefficient of static friction is $\mu_s = 0.40$; the coefficient of kinetic friction is $\mu_k = 0.30$. Calculate: (a) the maximum static friction; (b) the kinetic friction if the block is sliding.

**Exercise 2** *(LO: friction on an incline).* A 10-kg block rests on an incline tilted at 30 degrees. The coefficient of static friction is $\mu_s = 0.5$. Is the block in equilibrium? If not, what is its acceleration down the slope? (Assume it starts to move.)

**Exercise 3** *(LO: terminal velocity concept).* Two identical spheres fall through air. One is twice as dense as the other. Which has the higher terminal velocity? Explain using the formula for $v_T$.

### Application

**Exercise 4** *(LO: friction and Newton's second law).* A 100-kg box is pushed across a floor by a horizontal force of 500 N. The coefficient of kinetic friction is $\mu_k = 0.40$. Find the acceleration of the box.

**Exercise 5** *(LO: terminal velocity calculation).* A 80-kg skydiver in head-first position has a cross-sectional area of $A = 0.14$ m² and a drag coefficient of $C = 0.70$. Air density is $\rho = 1.21$ kg/m³. Calculate the terminal velocity.

**Exercise 6** *(LO: banked curve, ideal angle).* A highway curve has a radius of 200 meters. Engineers want to bank it so that a car traveling at 20 m/s (72 km/h) can safely navigate it without friction. What banking angle is required?

### Synthesis

**Exercise 7** *(LO: friction, incline, and equilibrium).* A block on a 25-degree incline is kept from sliding down by a horizontal force $F$. The coefficient of static friction is $\mu_s = 0.30$. Find the minimum force $F$ needed to prevent the block from sliding down.

**Exercise 8** *(LO: drag and differential equations).* An object falling through a medium with linear drag $F_D = bv$ reaches terminal velocity after a long time. Use the differential equation approach from Concept 2 to show that $v_T = mg/b$.

**Exercise 9** *(LO: circular motion and centripetal force).* A 1,500-kg car navigates an unbanked curve of radius 80 meters at 15 m/s. The coefficient of static friction is $\mu_s = 0.70$. Does the car slip? Explain.

**Exercise 10** *(LO: synthesis — friction, drag, and circular motion).* A motorcycle accelerates on a flat track, reaching 40 m/s. The rider then leans into a curve of radius 200 meters. The coefficient of static friction between tire and track is $\mu_s = 0.95$. Does the motorcycle slip? What is the required banking angle if the road were banked to eliminate friction at this speed?

### Challenge

**Exercise 11** *(LO: coupled systems with friction).* Two blocks are connected by a light string over a frictionless pulley. Block A (mass 4 kg) rests on a horizontal surface with coefficient of kinetic friction $\mu_k = 0.25$. Block B (mass 2 kg) hangs vertically. Find the acceleration of the system and the tension in the string.

**Exercise 12** *(LO: open-ended, drag and design).* A new vehicle is being designed to achieve maximum fuel efficiency on highways. Use the drag force formula to explain how each of the following would affect efficiency: (a) increasing the cross-sectional area; (b) decreasing the drag coefficient; (c) increasing the highway speed. Which factor has the strongest effect? Why?

---

## Chapter Summary

You now understand the three forces that dominate real-world motion.

**Friction** is a responsive force that opposes motion. Static friction grows to match an applied force up to a maximum of $\mu_s N$. Kinetic friction is constant at $\mu_k N$, slightly less than the maximum static friction. Friction doesn't always slow things down — it can propel you forward or change your direction. It depends on which way it acts.

**Drag** opposes motion through a fluid. For large objects at moderate to high speeds, drag is proportional to velocity squared: $F_D = \frac{1}{2} C \rho A v^2$. As an object falls or moves through a medium under constant drag, it asymptotically approaches a terminal velocity where the drag force balances the driving force (gravity or applied force). Terminal velocity depends on the object's weight, shape, size, and the fluid's density. Objects of different masses but the same shape reach the same terminal velocity.

**Centripetal force** is the name for whatever force (or combination of forces) points toward the center of a circular path. Its magnitude is $F_c = m v^2 / r$. For circular motion at constant speed to be possible, the net inward force must equal this value — not more, not less. Banking a curve by angle $\theta = \tan^{-1}(v^2 / rg)$ allows the normal force alone to supply the centripetal force, reducing the dependence on friction. Centrifugal force is a fictitious force that arises in rotating reference frames — it is not a real physical force.

The closing move: Newton's second law works in the real world once you account for the forces that are actually present. Friction, drag, and the geometry of curved paths were always there. Understanding them is the bridge between theory and practice.

What would change my mind: Experimental evidence that kinetic friction *does* depend significantly on sliding speed (it appears to be roughly constant, but at very high speeds or with certain material combinations, this may not hold). Or a demonstration that terminal velocity depends on mass in a way the drag formula doesn't predict.

Still puzzling: The molecular origin of the static-kinetic friction transition is not fully understood at all scales. We know it happens, and we can measure it, but the atomic-scale mechanism by which static friction suddenly "breaks" and kinetic friction takes over is still an active research area.

---

## Connections Forward

Chapter 8 (Work and Kinetic Energy) will show you that friction and drag are not conservative forces — they dissipate energy as heat. The work done against friction doesn't store energy the way lifting an object does. This is why a car coasting against air resistance slows down, and why a falling object with air resistance doesn't accelerate forever.

Chapter 10 (Rotation) will apply centripetal force to rotating objects and show how the same mathematics works for anything moving in a curved path, from a satellite orbiting Earth to a ceiling fan blade.

Later, when you encounter oscillations and waves (Chapters 15–16), you'll see that damping forces (which behave like drag) cause waves to lose energy over distance and time. The same mathematical forms reappear.

The Coriolis force, which you met briefly here, becomes essential in meteorology and oceanography — it explains why hurricanes rotate, why ocean currents curve, and why the trade winds blow the way they do. It is a reminder that reference frames matter, and choosing the right frame can make a problem much simpler or much harder.

---

## Tags

friction, drag, terminal velocity, centripetal force, banked curves, Newton's laws, calculus, differential equations, circular motion, reference frames


---

## LLM Exercise — Chapter 7: Friction, Drag, and Centripetal Scenarios

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Friction (static and kinetic) and drag forces as Force subclasses, plus simulations of the canonical scenarios — loop-the-loop, banked turn, conical pendulum, terminal velocity.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 7 task in the physics-simulation-toolkit. Extend the Ch 6
Newton's-laws framework with the workhorse applied forces and verify
the canonical scenarios.

In `chapters/ch07_applications/`:

1. `simulations.py` — Force subclasses:
   - `KineticFriction(body_id, surface_normal_fn, mu_k)` — friction
     opposing the body's velocity, with magnitude $\mu_k N$. Note:
     this becomes zero (or static) at v=0; handle the transition
     carefully with a tolerance.
   - `StaticFriction(body_id, surface_normal_fn, mu_s, applied_force_fn)`
     — magnitude up to $\mu_s N$, opposing the *would-be* slip
     direction. Returns zero force if the body is moving (kinetic
     takes over).
   - `QuadraticDrag(body_id, drag_coeff, area, fluid_density)` —
     $-\frac{1}{2}\rho C_d A |\vec{v}|\vec{v}$ (use the Ch 5 version).
   - `LinearDrag(body_id, k)` — $-k\vec{v}$, the Stokes-drag form for
     low Reynolds number.

2. Canonical scenarios in `simulations.py`:
   - `terminal_velocity(mass, drag_coeff, area, fluid_density)` —
     analytical formula and numerical verification.
   - `banked_turn(speed, radius, bank_angle)` — the no-friction-needed
     speed for a banked curve and the friction required at other speeds.
   - `loop_the_loop(radius)` — minimum speed at top of loop and the
     normal force throughout the loop.
   - `conical_pendulum(length, angle)` — the period of a conical
     pendulum, $T = 2\pi\sqrt{L\cos\theta/g}$.

3. `test_simulations.py`:
   - Skydiver: 75 kg, area ~0.7 m² spread-eagle, Cd ~1.0. Terminal
     velocity should be ~55 m/s (~120 mph). Verify by simulation
     reaching steady state.
   - Banked turn: at the design speed there should be zero friction
     required. Verify the integrator agrees with the analytical
     condition $\tan\theta = v^2/(rg)$.
   - Loop-the-loop: at the minimum-speed-at-top condition $v^2 = gr$,
     the normal force at top is exactly zero.

4. `benchmarks.py` — for the loop-the-loop, sweep entry speeds and
   plot the normal force as a function of position around the loop.
   Identify the critical entry speed below which the cart loses
   contact (normal force tries to go negative).

5. `README.md` — four decision cards. "Surprising findings": the
   skydiver terminal-velocity convergence rate; whether your specific
   parameter values match published skydiving data.

Commit as `ch07: friction, drag, and canonical Newtonian scenarios`.
```

**What this produces:** Friction and drag implementations, four canonical scenarios with analytical-vs-numerical verification, a loop-the-loop normal-force plot.

**How to adapt this prompt:**

- *For your own project:* Static friction is the trickiest piece — the velocity-zero discontinuity causes integrator issues. The standard fix is a velocity-tolerance threshold; document it.
- *For ChatGPT / Gemini:* Both work.
- *For Claude Code:* Native fit. Let it produce the loop-the-loop plot.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Extends the Ch 6 Force/System framework.

**Preview of next chapter:** Chapter 8 introduces work as a line integral and tests the work-energy theorem against simulation — the first energy-method check on the toolkit.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Guillaume Amontons** was the systematic 1699 experiments on friction that established what we now call Amontons's laws — friction force is proportional to the normal load and (largely) independent of contact area — published in the *Mémoires* of the French Academy of Sciences — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Guillaume Amontons, and how does their work on the empirical laws of friction (Amontons's laws) and the early experimental physics of contact connect to applications of Newton's laws to friction-dominated systems? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Guillaume Amontons"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe Amontons's specific 1699 experimental apparatus and how he varied normal load and contact area to isolate the friction law
- Ask: "Amontons's laws have exceptions — at very small scales, at very high loads, and on certain rough surfaces. What did Amontons himself know about these limits, and what was discovered after him?"
- Add the constraint: "Answer using one specific everyday situation (a sled, a bowed string, a finger on a touchscreen) where Amontons's laws hold and one where they fail, with the friction-physics reason for each"

What changes? What gets better? What gets worse?
