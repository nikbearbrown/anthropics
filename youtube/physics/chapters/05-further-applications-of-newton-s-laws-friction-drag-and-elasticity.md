# Chapter 5 — Further Applications of Newton's Laws: Friction, Drag, and Elasticity

*Three empirical laws that turn F = ma into engineering.*

---

In January 2018, a Polish alpinist named Andrzej Bargiel stood at the summit of K2 — the second-highest mountain on Earth, widely considered the most lethal of the eight-thousanders — and clicked into his skis. He was about to attempt something no one had done: ski K2 from summit to base camp without removing his skis. The upper sections run at about $50°$. Ice and compacted snow in alternating bands. A fall in the wrong place means a drop of more than two vertical kilometers.

He skied it. Six hours of continuous descent through the Bottleneck, the Black Pyramid, around the séracs of the Shoulder. He arrived at base camp alive, on his own legs, on the same skis he'd left the summit on.

What kept him on the mountain? The short answer is: friction. The long answer is what this chapter is about.

![Stylized steep slope of K2. Two paths: straight-down line (gravity pulls fast, friction barely resists) vs serpentine turn path (geometry trades altitude for distance). At extreme grades, only turning keeps speed survivable.](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-01.png)
*Figure 5.1 — Bargiel's K2 Descent — Turns Shed Speed When Friction Can't*

On a frictionless $50°$ slope, a body accelerates at $g\sin50° \approx 7.5 \text{ m/s}^2$ — roughly $25 \text{ km/h}$ of speed added every second, no limit, no stopping. With friction, the acceleration becomes $g(\sin\theta - \mu_k\cos\theta)$. For waxed steel edges on packed snow, $\mu_k$ is something like $0.05$, which drops the acceleration from $7.5$ to about $7.2 \text{ m/s}^2$ — barely changed by friction alone. But Bargiel wasn't sliding straight down. He was making turns. Each turn lets friction do useful work in a different direction. With the right geometry, the force balance can be managed into something near a steady velocity.

Friction doesn't just oppose motion. In the right context, it controls motion. It is what makes mountains skiable, cars stoppable, bolts stay tight, and walking possible.

![Three-column comparative table. Each column lists: form of the resistive force or response; range of applicability; failure mode where the simple model breaks down. Friction (μN, contact), drag (½ρCAv² above Re ~1000),...](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-07.png)
*Figure 5.7 — Domain Map — Friction, Drag, Elasticity: Where They Work, Where They Break*

This chapter is about three contact-force laws — friction, drag, and elasticity — that complete the practical side of Newton's framework. Each one is an empirical law: it was fitted to measurement, not derived from first principles. Each one has a domain where it works and a domain where it breaks down. Together, they cover nearly every contact interaction that matters at engineering scale.

<!-- → [IMAGE: photograph or diagram of a skier in a steep carved turn on a high-angle alpine slope, with force arrows labeled: weight down the slope, normal force perpendicular to slope, friction force directed up and across the slope — to make concrete the multi-directional friction geometry of the opening hook] -->

---

## Friction: the force that adjusts itself

Here is the essential strangeness of static friction: it is not a fixed force. It is a variable force that adjusts itself, within limits, to match whatever is being applied to the object.

![Plot of friction force versus applied force. Friction equals the applied force (45° line) up to μ_s N (static maximum), then drops abruptly to μ_k N (kinetic, constant). Hallmark sawtooth profile.](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-02.png)
*Figure 5.2 — Friction Force vs Applied Force — Static Climbs, Then Drops to Kinetic*

Push a heavy crate with $10 \text{ N}$. Static friction pushes back with $10 \text{ N}$. Push with $50 \text{ N}$. Friction pushes back with $50 \text{ N}$. Push with $200 \text{ N}$ — and the crate moves. The static friction was adjusting up to some maximum, and when the applied force exceeded that maximum, sliding began.

Once the crate slides, friction changes character. It is no longer an adjusting force trying to prevent relative motion; it is a definite, calculable force opposing the sliding. And it is smaller than the maximum static friction: the crate, once started, takes less force to keep moving than to start.

These two behaviors are captured in two equations.

Before sliding:

$$f_s \leq \mu_s N,$$

where $N$ is the normal force pressing the surfaces together and $\mu_s$ is the **coefficient of static friction**. The $\leq$ is doing essential work here. Static friction is whatever it needs to be, up to the maximum $\mu_s N$. If you apply less than the maximum, the crate doesn't move and friction matches your push exactly.

After sliding:

$$f_k = \mu_k N,$$

where $\mu_k$ is the **coefficient of kinetic friction**. This is an equality — once sliding begins, kinetic friction has a definite value. And for almost every material pair, $\mu_k < \mu_s$: starting takes more force than sustaining.

Here are typical values:

<!-- → [TABLE: coefficients of static and kinetic friction for representative material pairs — rubber on dry concrete (μs ≈ 1.0, μk ≈ 0.7), rubber on wet concrete (0.7, 0.5), wood on wood (0.5, 0.3), steel on steel dry (0.6, 0.3), waxed wood on wet snow (0.14, 0.1), Teflon on steel (0.04, 0.04), synovial joints in humans (0.01, 0.003) — to give students a feel for the range and to highlight the remarkable performance of biological joint lubrication] -->

Notice the bottom entry. The synovial fluid in your knee and hip joints gives a kinetic friction coefficient of about $0.003$ — lower than Teflon on steel. Biology has engineered, inside the human body, essentially frictionless bearings. Ball-bearing assemblies in precision machinery achieve similar values with metal parts. The difference between a healthy joint and an arthritic one is largely a tribological story.

Microscopically, friction at a surface comes from two sources: adhesion — molecular attractions at the real contact points between the two surfaces — and interlocking of the asperities, the microscopic bumps, on each surface. Both depend on how hard the surfaces are pressed together, which is why both $f_s$ and $f_k$ scale with $N$. The contact area doesn't appear in the equations because increasing the contact area spreads the same force over more points without increasing the force per point, so the total friction stays the same. A wide tire and a narrow tire on the same car generate (within the simple model) the same friction from the road.

### A skier at constant velocity

![Free-body diagram on a tilted axis: gravity decomposed into components parallel and perpendicular to slope. Normal force balances perpendicular weight. For constant velocity (no net force), kinetic friction equals parallel...](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-03.png)
*Figure 5.3 — Skier on a 25° Slope — Constant Velocity Implies μ_k = tan θ*

A skier of mass $m = 62 \text{ kg}$ descends a $25°$ slope at constant velocity. What is the coefficient of kinetic friction?

Constant velocity means zero net force. Let $x$ run down the slope, $y$ perpendicular to the slope away from the surface.

Perpendicular balance: $N = mg\cos25°$.

Along-slope balance: $mg\sin25° - f_k = 0$, so $f_k = mg\sin25°$.

Apply the friction law: $\mu_k N = mg\sin25°$, which gives:

$$\mu_k = \frac{mg\sin25°}{mg\cos25°} = \tan25° \approx 0.47.$$

Two things to notice. First, $m$ cancels: the coefficient of friction at constant velocity equals $\tan\theta$, regardless of how heavy the skier is. This is a beautiful result. Second, it gives you a measurement technique: tilt a surface until an object slides at constant velocity, and $\mu_k = \tan\theta$. For static friction, tilt until the object *just barely starts to slide*, and $\mu_s = \tan\theta_{\text{threshold}}$. Geometry and equilibrium together measure friction.

The value $0.47$ is considerably higher than the table's entry for waxed wood on wet snow ($\sim 0.10$). That's telling you something: either the skier is on unwaxed equipment, or the snow is unusually sticky (warm spring snow, or snow that's partly melt-frozen), or both. The table gives ideal values; real surfaces often differ by a factor of two.

<!-- → [INFOGRAPHIC: free-body diagram for a skier on an inclined slope — weight vector decomposed into components parallel and perpendicular to slope, normal force perpendicular away from slope, friction force pointing up the slope — with the angle θ labeled and the balance equations shown; student should see why the mass cancels] -->

One misconception worth confronting directly: friction can point *forward* on an object. When a car accelerates from rest, the tire is trying to spin backward relative to the road. Friction from the road opposes *that* attempted sliding — so it acts forward, on the tire, which propels the car forward. Friction opposes relative sliding between surfaces, not necessarily the motion of the object as a whole. Driving forward is powered by friction. Walking is powered by friction. You are reading this sentence, if you are sitting in a chair, because friction keeps you in place.

---

## Drag: the force that sets a speed limit

You jump out of a plane at $4{,}000 \text{ m}$. The first second is ordinary free fall: you accelerate at $g = 9.80 \text{ m/s}^2$, just as if the air weren't there. After a few seconds you're doing $40 \text{ m/s}$, and the air pressure against your body is no longer negligible. After about ten seconds, you stop accelerating. You've reached terminal velocity.

![Speed of a falling skydiver rises rapidly at first, then curves smoothly to a horizontal asymptote near 50 m/s (~180 km/h) — terminal velocity, where drag equals weight.](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-04.png)
*Figure 5.4 — Skydiver Speed vs Time — Asymptotic Approach to Terminal Velocity*

Terminal velocity is the central phenomenon of drag. A falling object in air does not accelerate forever. It accelerates until the resistive force from the air exactly equals its weight, then continues at constant speed. For a typical skydiver in a stable face-down position, that speed is around $55 \text{ m/s}$ — roughly $200 \text{ km/h}$. In a streamlined head-down dive, it can exceed $90 \text{ m/s}$. Under an open parachute, it drops to about $5 \text{ m/s}$. Same person, same weight, vastly different terminal velocities. The difference is how much surface area is presented to the airflow.

For objects moving through a fluid at intermediate speeds — fast enough for turbulence to develop, slow enough to ignore compressibility — the drag force is:

$$F_D = \tfrac{1}{2} C \rho A v^2,$$

where $C$ is the dimensionless **drag coefficient** (depends on shape), $\rho$ is the fluid density, $A$ is the cross-sectional area facing the flow, and $v$ is speed relative to the fluid.

The $v^2$ dependence is the key fact. Drag at $40 \text{ m/s}$ is sixteen times larger than drag at $10 \text{ m/s}$ — not four times, sixteen. This is why fuel consumption on a highway rises so steeply with speed: drag power scales as $v^3$, so a car going $120 \text{ km/h}$ uses roughly eight times the drag-fighting power of a car going $60 \text{ km/h}$. Streamlining matters much more at speed.

<!-- → [CHART: drag force vs. speed for a typical skydiver (C = 0.70, A = 0.70 m², ρ = 1.21 kg/m³) — x-axis speed 0–60 m/s, y-axis drag force 0–800 N, with a horizontal dashed line at mg = 735 N (for 75 kg) showing the intersection at terminal velocity ~50 m/s; student should see the v² curve and the terminal-velocity concept visually] -->

Set drag equal to weight to find terminal velocity:

$$\tfrac{1}{2} C \rho A v_t^2 = mg, \quad \text{so} \quad v_t = \sqrt{\frac{2mg}{C\rho A}}.$$

Heavier objects fall faster (scales as $\sqrt{m}$). Larger area means slower fall (scales as $1/\sqrt{A}$). Denser fluid means slower fall (scales as $1/\sqrt{\rho}$). A leaf falls slowly because $A/m$ is large; a stone falls fast because $A/m$ is small. A sheet of paper and the same sheet crumpled into a ball reach very different terminal velocities even though they have the same mass — because crumpling reduces $A$ dramatically.

### Terminal velocity of a skydiver

A $75 \text{ kg}$ skydiver in a stable horizontal position has cross-sectional area $A = 0.70 \text{ m}^2$ and drag coefficient $C = 0.70$. Take $\rho_{\text{air}} = 1.21 \text{ kg/m}^3$.

$$v_t = \sqrt{\frac{2 \times 75 \times 9.80}{1.21 \times 0.70 \times 0.70}} = \sqrt{\frac{1470}{0.593}} = \sqrt{2479} \approx 49.8 \text{ m/s}.$$

About $50 \text{ m/s}$, or $180 \text{ km/h}$. Published values for face-down skydivers range from $50$–$60 \text{ m/s}$ depending on body geometry and suit. The calculation is in the right range.

<!-- → [INFOGRAPHIC: side-by-side comparison of three body positions for the same 75 kg skydiver — face-down stable (A = 0.70 m², C = 0.70, v_t ≈ 50 m/s), head-down streamlined (A ≈ 0.30 m², C ≈ 0.50, v_t ≈ 90 m/s), open parachute (A ≈ 40 m², C ≈ 1.4, v_t ≈ 5 m/s) — with terminal velocity labeled for each, illustrating how A and C control terminal speed for the same weight] -->

How long does it take to reach terminal velocity? As a rough estimate, treat the early fall as free fall at $g$: time to reach $50 \text{ m/s}$ is $50/9.8 \approx 5 \text{ s}$, during which the skydiver falls about $\tfrac{1}{2}(9.8)(5)^2 \approx 120 \text{ m}$. This overcounts the fall (drag slows the acceleration before terminal speed is reached), but it suggests you need at least $\sim 200 \text{ m}$ of altitude to reach terminal velocity. A $4{,}000 \text{ m}$ skydive spends most of its freefall at terminal velocity.

One important caveat about the drag equation: it holds in the regime where the flow around the object is turbulent — roughly when the Reynolds number $Re = \rho v L / \eta$ (where $L$ is a characteristic size and $\eta$ is fluid viscosity) exceeds about $1{,}000$. For a skydiver at $50 \text{ m/s}$, $Re \sim 10^7$ — solidly turbulent. For a bacterium swimming in water, $Re \sim 10^{-5}$ — a completely different physical regime. In that regime, drag is proportional to $v$ rather than $v^2$ (Stokes drag: $F_D = 6\pi\eta r v$), and the formula above does not apply. The $v^2$ law is excellent for human-scale objects moving at human-scale speeds; it fails for the very small or the very fast.

---

## Elasticity: the force that restores

Pluck a steel guitar string. It deforms. Let it go. It recovers. The deformation is repeatable and reversible, and the frequency at which it vibrates is set by the same stiffness that resisted the deformation in the first place.

Hang a load from a spring. It stretches. Remove the load. It returns to its original length. Hang twice the load. It stretches twice as far.

This proportionality between deformation and applied force, within some range of deformations, is **Hooke's law**:

$$F = k \, \Delta L,$$

where $\Delta L$ is the change in length and $k$ is the **spring constant** — a number that encodes how stiff the object is. A stiff spring has large $k$; a floppy one has small $k$.

For a rod or wire of length $L_0$, cross-sectional area $A$, and made of a material with **Young's modulus** $Y$, the extension under a force $F$ is:

$$\Delta L = \frac{F}{YA} L_0.$$

![Three panels: tension (rod stretched along its axis, ΔL/L₀ = F/(EA)); shear (block twisted parallel to face, Δx/L = F/(GA)); bulk compression (cube squeezed from all sides, ΔV/V₀ = -ΔP/B). Each has its own modulus.](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-05.png)
*Figure 5.5 — Three Ways to Deform a Solid — Tension, Shear, Bulk Compression*

Young's modulus is the material's intrinsic stiffness — independent of the rod's geometry. Steel has $Y \approx 200 \times 10^9 \text{ Pa}$. Bone is about $9 \times 10^9 \text{ Pa}$ in compression. Rubber is around $10^7 \text{ Pa}$ — roughly $20{,}000$ times less stiff than steel. Every guitar string, every tendon, every crane cable, and every structural beam deforms according to this formula as long as the deformation is small enough.

![Engineering stress-strain curve: linear elastic region (Hooke's law, slope = Young's modulus); yield point near 250 MPa; plastic region with strain hardening; ultimate tensile strength ~400 MPa; necking; fracture.](../images/05-further-applications-of-newton-s-laws-friction-drag-and-elasticity-fig-06.png)
*Figure 5.6 — Stress-Strain Curve for Mild Steel — Four Regions, One Material*

That qualification matters. Hooke's law is a linear approximation. For small deformations, force and displacement are proportional. As deformations grow, the relationship curves. At the **elastic limit**, the material stops recovering: deformation becomes permanent (plastic). Beyond that, at the **ultimate tensile strength**, it fractures. The linear regime is enormous for engineering — most structural elements operate well within it — but knowing where the limit is for your material is part of knowing the law.

### Stretching a steel cable

A steel cable of length $L_0 = 10.0 \text{ m}$ and cross-sectional area $A = 1.0 \text{ cm}^2 = 1.0 \times 10^{-4} \text{ m}^2$ supports a $1{,}000 \text{ kg}$ load. How much does it stretch?

Force: $F = mg = 1{,}000 \times 9.80 = 9{,}800 \text{ N}$.

$$\Delta L = \frac{F\,L_0}{Y A} = \frac{9{,}800 \times 10.0}{200 \times 10^9 \times 1.0 \times 10^{-4}} = \frac{98{,}000}{2.0 \times 10^7} = 4.9 \times 10^{-3} \text{ m}.$$

About $5 \text{ mm}$, or $0.05\%$ of the cable's length.

This is characteristic of steel under normal structural loads. The strain ($\Delta L / L_0 = 4.9 \times 10^{-4}$) is well below the yield strain for structural steel (about $0.001$–$0.002$), so the cable is fully in the elastic regime — deforming under load, recovering when the load is removed, exactly as Hooke intended.

Notice what Hooke's law lets you do in two directions. Given a load, predict the deformation (structural design). Given a measured deformation, back-calculate the load (strain-gauge sensors, which are the basis of most force-measurement instruments). Either direction depends on the linear approximation holding, which is why every strain gauge has a rated maximum load beyond which the reading is no longer reliable.

<!-- → [CHART: stress-strain curve for a ductile metal — stress (force per area, in Pa) on y-axis, strain (ΔL/L₀, dimensionless) on x-axis — showing the linear elastic region (Hooke's law), the yield point, strain hardening, ultimate tensile strength, and fracture point; label the slope of the linear region as Young's modulus Y; student should see that the chapter's Hooke's law covers only the initial linear segment] -->

---

## Three laws, one framework

These three laws — friction, drag, elasticity — do not stand apart from Newton's second law. They are the content you substitute into it.

Without the laws, $F = ma$ is a form waiting to be filled in. With them, the form becomes a calculation. The friction law tells you what to write for the contact force at a surface. The drag law tells you what to write for the resistance of a fluid. The elastic law tells you what to write for the restoring force of a deformed material. In each case, the law is an empirical observation dressed up as an equation and given a coefficient that absorbs whatever we don't understand about the microscopic physics.

It is worth being honest about this. None of these laws derives from first principles. The friction law follows from atomistic contact mechanics in a hand-wavy way, but the actual value of $\mu$ for rubber on wet concrete is something you look up in a table, not something you derive from the atomic structure of rubber. The drag equation has a theoretical skeleton in the Navier-Stokes equations, but the drag coefficient $C$ for a specific shape is typically measured in a wind tunnel. Young's modulus has deep roots in quantum mechanics and the potential-energy wells between atoms, but the number for bone or nylon is measured, not calculated.

This is not a limitation of these laws. It is their character. They describe what nature does at a scale where the microscopic details average out into a small set of material constants. The reward is extraordinary: three simple force laws that let you compute, to within a factor of two or so, the friction on a skier, the terminal velocity of a falling object, and the deformation of a structural beam, using nothing but the laws of Chapter 4 and these three expressions.

Consider the synthesis: a skier of mass $70 \text{ kg}$ on a $20°$ slope, kinetic friction $\mu_k = 0.10$, in a crouch with $A = 0.55 \text{ m}^2$ and $C = 0.80$.

Friction: $N = mg\cos20° \approx 645 \text{ N}$, so $f_k = 0.10 \times 645 = 64.5 \text{ N}$ up the slope.

Net gravitational pull along the slope minus friction: $mg\sin20° - f_k = 70(9.80)(0.342) - 64.5 \approx 234 - 64.5 = 170 \text{ N}$.

Set that equal to drag to find terminal speed:

$$\tfrac{1}{2}(0.80)(1.21)(0.55)v_t^2 = 170, \quad v_t = \sqrt{\frac{340}{0.532}} \approx 25.3 \text{ m/s}.$$

About $91 \text{ km/h}$ — a realistic downhill speed in a tuck on a moderate slope. And her ski poles, planted briefly during a turn, each deform by a few tens of micrometers under the load of her turn, fully within the elastic limit of aluminum, recovering perfectly for the next plant.

Three forces, all active at once, all calculable, all from one underlying framework.

<!-- → [INFOGRAPHIC: free-body diagram for the skier-on-slope synthesis example — showing weight, normal force, friction (up-slope), and drag (up-slope, with v² label) acting simultaneously; annotate with the numerical magnitudes from the worked example so the student can see all three force laws contributing to the net force balance] -->

This is what it looks like when physics reaches into the real world. Bargiel's descent of K2 was governed by exactly these equations: friction coefficients near $0.05$ for his ski edges on ice, drag coefficients near $0.8$ for his crouched body, and the elastic deformation of every edge, binding, and boot flex absorbing and returning energy with every turn. He survived because those forces balanced, on every turn, for six hours. The mathematics of it is this chapter.

---

## Exercises

### Warm-up

**5.1** *(LO 1)* A $100 \text{ N}$ horizontal force is applied to a $50 \text{ kg}$ box on a level floor. The coefficients are $\mu_s = 0.40$ and $\mu_k = 0.30$. (a) Compute the maximum static friction. (b) Does the box move? (c) If it does move, what is the kinetic friction force and the net force on the box?

**5.2** *(LO 2)* A box on a ramp sits still while the angle is slowly increased. It first begins to slide at $\theta = 30.0°$. What is $\mu_s$? What would $\mu_k$ be if the box then slides at constant velocity when the ramp is set to $25.0°$?

**5.3** *(LO 3)* A $0.145 \text{ kg}$ baseball has cross-sectional area $A = 0.0042 \text{ m}^2$ and drag coefficient $C = 0.40$. It moves at $40 \text{ m/s}$ through air ($\rho = 1.21 \text{ kg/m}^3$). Compute the drag force. What fraction of the ball's weight is this drag?

**5.4** *(LO 5)* A spring stretches $5.0 \text{ cm}$ when a $2.0 \text{ kg}$ mass hangs from it at rest. (a) What is the spring constant $k$? (b) How far would it stretch under a $5.0 \text{ kg}$ load, assuming Hooke's law still holds?

### Application

**5.5** *(LO 1, 2)* A $50 \text{ kg}$ crate is pushed up a $20.0°$ ramp at constant velocity. The coefficient of kinetic friction is $\mu_k = 0.30$. (a) Draw and label the free-body diagram. (b) What pushing force, applied parallel to the ramp, is required?

**5.6** *(LO 1, 2)* A car of mass $1{,}500 \text{ kg}$ brakes from $25.0 \text{ m/s}$ to rest on dry pavement ($\mu_k = 0.70$). (a) What is the friction force? (b) What is the magnitude of deceleration? (c) How far does the car travel before stopping? (d) How would the stopping distance change if the road were wet ($\mu_k = 0.50$)?

**5.7** *(LO 3, 4)* A $60 \text{ kg}$ skydiver has cross-sectional area $A = 0.50 \text{ m}^2$ and drag coefficient $C = 0.70$ in a stable face-down position. (a) Compute her terminal velocity. (b) She opens a parachute: $A$ increases to $30 \text{ m}^2$ and $C$ becomes $1.4$. Compute her new terminal velocity. (c) By what factor did terminal velocity decrease?

**5.8** *(LO 5)* A nylon climbing rope of length $50 \text{ m}$ and cross-sectional area $1.0 \text{ cm}^2$ supports a stationary $80 \text{ kg}$ climber. Take $Y_{\text{nylon}} \approx 5 \times 10^9 \text{ Pa}$. (a) How much does the rope stretch under the climber's weight? (b) What is the strain ($\Delta L / L_0$)? (c) Is this within the elastic regime for nylon?

### Synthesis

**5.9** *(LO 2, 3, 4)* A skier of mass $70 \text{ kg}$ glides down a $25.0°$ slope. Kinetic friction coefficient: $\mu_k = 0.050$. Drag area: $A = 0.50 \text{ m}^2$, $C = 0.70$, $\rho_{\text{air}} = 1.21 \text{ kg/m}^3$. (a) What is the net downslope force from gravity minus friction at low speed (before drag matters)? (b) At what speed does drag equal that net force — i.e., what is the terminal velocity down the slope? (c) If the skier instead tucks into a crouch so $A$ drops to $0.30 \text{ m}^2$, what is the new terminal velocity?

**5.10** *(LO 1, 5)* A $20 \text{ kg}$ box hangs from a vertical spring with $k = 5{,}000 \text{ N/m}$. (a) How far does the spring stretch at rest? (b) You press down on the box with an additional $30 \text{ N}$ and hold it stationary. How much further does the spring stretch? (c) Instead of pressing, you pull the box down $1.0 \text{ cm}$ and release it. What is the initial restoring force? What will the box do?

**5.11** *(LO 1, 3, 4)* A bicyclist and bike together have mass $80 \text{ kg}$ and coast down a $5.0°$ hill at a steady $15 \text{ m/s}$. Drag area: $A = 0.50 \text{ m}^2$, $C = 1.0$, $\rho_{\text{air}} = 1.21 \text{ kg/m}^3$. (a) At terminal speed, what is the total resistive force (gravity along slope = drag + rolling friction)? (b) Compute the drag force at $15 \text{ m/s}$. (c) What rolling friction force is left over after drag is accounted for? (d) What implied "rolling coefficient" $\mu_r$ does this give (define as $f_{\text{roll}} = \mu_r N$)?

### Challenge

**5.12** *(LO 3, 4, beyond chapter)* A $1.0 \text{ μm}$ spherical bacterium ($\rho = 1{,}000 \text{ kg/m}^3$) sinks in water ($\eta = 10^{-3}$ Pa·s) under Stokes drag: $F_D = 6\pi\eta r v$. (a) Derive the terminal-velocity expression for this case and compute the value. (b) Compare to the bacterium's typical self-propelled swimming speed of about $30 \text{ μm/s}$. (c) Explain physically why bacteria need flagella to make directed progress, rather than simply drifting.

**5.13** *(LO 5, beyond chapter)* A vertical steel column $5.0 \text{ m}$ tall must support a $50{,}000 \text{ kg}$ load without compressing more than $1.0 \text{ mm}$. (a) Using $Y_{\text{steel}} = 200 \times 10^9 \text{ Pa}$, find the minimum required cross-sectional area. (b) Compute the stress (force per area) in the column at this minimum area. (c) Look up steel's yield stress (approximately $250 \times 10^6 \text{ Pa}$ for mild steel) and verify that the column is operating well within the elastic limit.

---



By the end of this chapter you should be able to:

1. Distinguish static and kinetic friction; compute each from $f_s \leq \mu_s N$ and $f_k = \mu_k N$ given the relevant coefficient and normal force.
2. Apply the friction laws to objects on level surfaces and inclined planes, including the result $\mu = \tan\theta$ at the limiting angle.
3. Compute drag force from $F_D = \tfrac{1}{2} C \rho A v^2$ and identify where this expression breaks down (very small objects: Stokes regime; speeds near or above the speed of sound).
4. Compute terminal velocity by setting drag equal to weight, and explain why it depends on $m$, $A$, and $\rho$.
5. Apply Hooke's law $F = k \Delta L$ to predict deformation under load, and identify the elastic limit beyond which the linear approximation fails.

**Prerequisites.** Chapter 4 (Newton's laws, free-body diagrams, $F = ma$). Chapter 3 (vector decomposition for inclined-plane problems). Trigonometry.

**Why this chapter matters.** These are the three contact forces real engineering touches. Friction is what makes cars stop, walking work, and bolts stay tight. Drag determines the speed limit of every object moving through air or water. Elasticity is the operating principle of every spring, beam, tendon, and string. If Chapter 4 gave you Newton's framework, this chapter fills it with content.

---

## ↳ Dig Deeper — Why does $\mu$ depend so much on conditions?

*The simple $f = \mu N$ model treats $\mu$ as a property of two materials. In reality it varies with temperature, humidity, surface preparation, contamination, and sliding speed. Modern tribology explains why, and the answers reach into surface chemistry and statistical mechanics.*

**Prompt:**
> Explain the three main mechanisms contributing to friction between dry surfaces: adhesion, asperity interlocking, and plastic/elastic deformation at contact points. For each, name one variable (temperature, humidity, surface preparation, sliding speed) that affects it and explain how. Then explain why $f = \mu N$ is independent of contact area in the basic model, and under what real-world circumstances area-independence breaks down. End with one sentence on how lubricants change the picture.

**What to do with the output:** Save it. Tribology returns in any mechanical engineering context — brakes, bearings, prosthetics, tire design. The laws in this chapter are the entry-level approximation; tribology is the correction terms.

---

## ↳ Dig Deeper — The Stokes regime: where small things live

*The drag equation $F_D = \tfrac{1}{2}C\rho Av^2$ holds at intermediate speeds and sizes. For very small objects — bacteria, dust particles, fine droplets — drag is proportional to $v$, not $v^2$. This is the Stokes regime, and it has profound consequences for biology and atmospheric science.*

**Prompt:**
> Explain the Stokes drag formula $F_D = 6\pi\eta r v$ for a sphere of radius $r$ in a fluid of viscosity $\eta$. Derive the terminal velocity for a small sphere falling under gravity in this regime. Then compute terminal velocity for (a) a $1 \text{ μm}$ bacterium ($\rho \approx 1{,}000 \text{ kg/m}^3$) in water ($\eta = 10^{-3}$ Pa·s), and (b) a $1 \text{ mm}$ raindrop in air ($\eta_{\text{air}} = 1.8 \times 10^{-5}$ Pa·s, $\rho_{\text{water}} = 1{,}000 \text{ kg/m}^3$). End with one sentence on what dimensionless number (the Reynolds number) decides which regime applies.

**What to do with the output:** Save it. The Stokes vs. turbulent regimes are foundational for fluid dynamics (Chapter 12) and for any small-scale biology or atmospheric problem.

---

## ↳ Dig Deeper — The full stress-strain curve

*Hooke's law describes the linear elastic region of a material's response to stress. Real materials have a richer story: a yield point, strain hardening, ultimate tensile strength, and fracture. Engineering materials science is largely the discipline of knowing where on this curve you're operating.*

**Prompt:**
> Sketch (in description) the typical stress-strain curve for a ductile metal like mild steel. Label and explain: (a) the linear elastic region, (b) the yield point, (c) strain hardening, (d) ultimate tensile strength, (e) fracture point. Explain what happens to a steel beam loaded to each region if you then remove the load. End with one sentence on why ductile metals are preferred over brittle ones for structural applications, even though brittle materials sometimes have higher ultimate strength.

**What to do with the output:** Save it. The Hooke's-law region in this chapter is one piece of a larger picture. The full curve is essential for Chapter 9 (statics) and for any structural or materials engineering context.

---

## LLM Exercise — Chapter 5: Friction, Drag, and Elasticity in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** Quantitative estimates of one friction, one drag, or one elastic-deformation effect in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 5, I want to apply one or more of: friction laws, drag equations, or Hooke's law to my phenomenon. Please:

1. Identify ONE relevant friction, drag, or elastic effect in my phenomenon. Examples:
   - Bike commute: rolling friction of tires against road; air drag at cruising speed; tire deformation under weight.
   - Coffee maker: friction in the pump; drag of water through coffee grounds; spring loading on the brewing chamber gasket.
   - Basketball: drag on the ball during flight; friction between hand and ball at release; deformation of ball on impact with rim.
   - Marathon: friction at each footstrike; drag at running speed; tendon/Achilles deformation under load.
   - Espresso: friction in the puck during 9-bar extraction; drag of water through grounds; spring force in the pressure relief valve.

2. Identify the relevant equation (f = μN, F_D = ½CρAv², F = kΔL).

3. Estimate the relevant inputs: coefficient, area, density, spring constant. For each: where to source the value and what uncertainty to expect.

4. Compute the force or deformation. Report with units, sig figs, and percent uncertainty.

5. Sanity-check with one Fermi estimate.

6. Identify which assumption (linear elasticity, constant μ, constant C, ignored Reynolds-regime change) is most likely to bite.

7. One sentence on what energy is lost to this force (preview Chapter 7).

Save the output as logbook/chapter-05-friction-drag-elasticity.md.
```

### What this produces

A fifth Logbook entry: a quantitative force-law analysis applied to your phenomenon, often surprising in magnitude. How big is rolling friction on a bike? Bigger than you'd guess at low speeds, smaller than drag at high speeds.

### How to adapt this prompt

- *For phenomena that are mostly steady-state:* emphasize force balance — what equals the friction or drag.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have video data (a basketball trajectory you can frame-grab), compute drag from the measured deceleration.

### Connection to previous chapters

Builds on Chapter 4 ($F = ma$) by providing specific force expressions for contact and deformation. Builds on Chapter 3 (vector decomposition) for inclined-plane work.

### Preview of next chapter

Chapter 6 takes Newton's laws to circular motion and gravitation. The Chapter 6 LLM Exercise will look at any circular or rotational element in your phenomenon — a tire turning, a stirred liquid, a curved running path — and apply centripetal-force analysis.

---

## What would change my mind

The chapter argues that three empirical force laws — friction, drag, and elasticity — are sufficient for most engineering-scale contact-force prediction. The argument would need revision if a class of common problems systematically required corrections beyond these laws. Many do (lubrication regimes, viscoelasticity, finite-deformation elasticity), but those corrections are layered on the three core laws here, not replacements for them.

## Still puzzling

The deepest puzzle this chapter raises and does not resolve: **why is friction so well-described by such a simple law?** Microscopic surfaces are atomically rough, chemically complex, dynamically rearranging under load. The naive expectation would be complicated behavior. Instead, $f \approx \mu N$ holds — often to within a factor of two — across enormous variations in conditions. Modern tribology offers partial explanations, but the depth of agreement between the simple law and observation remains philosophically striking. Feynman called friction "still the most poorly understood common phenomenon in classical physics," and the remark holds up.

---

## AI Wayback Machine

**Charles-Augustin de Coulomb** is remembered today mostly for the law of electrostatic force that carries his name. But in 1781, before his electrical work, he won a prize from the French Académie des Sciences for an essay on friction — distinguishing static from kinetic friction, characterizing the role of normal force, and producing the fundamental laws we still teach.

**Run this:**

```
Who was Coulomb, and how does his work on friction connect to Newton's-law applications in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Charles-Augustin de Coulomb"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask which of Coulomb's friction laws still hold up under modern materials science, and which have been refined.
- Ask about Coulomb's parallel career as a military engineer in the French colonies and how it shaped his experimental work.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 6 applies Newton's laws — with the contact forces from this chapter — to circular motion. Friction between car tires and a curved road sets the maximum cornering speed; Chapter 6 is where you calculate it. Chapter 7 introduces energy; friction and drag will be the principal mechanisms by which mechanical energy converts to heat. Chapter 9 (statics) uses the elasticity framework here to handle small deformations of structures under load. Chapter 12 (fluid dynamics) gives the deeper story behind the drag equation, including the Reynolds number that decides which regime applies.

---

**Tags:** friction, drag, Hookes-law, terminal-velocity, contact-forces
