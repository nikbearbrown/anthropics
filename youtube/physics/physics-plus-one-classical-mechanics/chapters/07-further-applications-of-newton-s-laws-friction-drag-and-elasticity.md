# Chapter 7 — Further Applications of Newton's Laws: Friction, Drag, and Elasticity

*Where the second law meets the real world, and three empirical force laws fill in the blanks.*

---

## A skier in the Karakoram, January 2018

Andrzej Bargiel, 30 years old, Polish, stands at $8{,}611 \text{ m}$ on the summit of K2 — the world's second-highest mountain, often called the most lethal of the eight-thousanders. He clicks into his skis. He is the first person ever to attempt to ski K2 from the summit to base camp without removing his skis. The slope in the upper sections runs around $50°$, alternating ice and snow, exposed to a fall of more than two vertical kilometers.

He skis it. Six hours down through the Bottleneck, the Black Pyramid, around the séracs of the Shoulder. He arrives at base camp on his own legs, on his own skis, alive.

What kept him on the mountain instead of accelerating off it?

On a frictionless $50°$ slope, a body accelerates at $g\sin 50° \approx 7.5 \text{ m/s}^2$ down the fall line — roughly $25 \text{ km/h}$ added to your speed every second. With kinetic friction between ski edges and packed snow, the acceleration becomes $g(\sin\theta - \mu_k\cos\theta)$. For a coefficient of friction around $0.05$, the acceleration drops to about $7.2 \text{ m/s}^2$ — barely changed. Friction alone doesn't save you on K2.

What saves you is turn geometry. Bargiel isn't sliding straight down. Each turn rotates his ski edges so that friction acts perpendicular to the fall line, shedding speed and redirecting momentum. The mountain doesn't care about his courage or his fitness. It cares about one thing: the net vector sum of gravity, normal force, and friction, and whether that sum is pulling him off the slope or keeping him on it. Friction is what makes the vector sum manageable.

<!-- → [DIAGRAM: side-by-side comparison of straight-line vs. carved-turn force diagrams on a 50° slope — left panel: gravity, normal force, and small friction all shown as vectors for a skier going straight down (net force strongly down-slope); right panel: same forces for a skier mid-turn, with friction rotated perpendicular to velocity, showing how the net force can point toward the slope center rather than down the fall line; caption: "friction alone barely changes the acceleration; friction redirected by turn geometry is what controls speed"] -->

Friction is also what makes cars stop, bolts stay tight, and walking possible. This chapter is about friction and two close relatives — drag and elasticity — that together cover nearly every contact interaction the engineering world cares about. Each is an empirical law: fitted to measurement, not derived from first principles, valid within a domain, wrong outside it. Newton's second law tells you that $\mathbf{F}_\text{net} = m\mathbf{a}$; these three laws tell you what to put on the left side.

---

## Friction

### Static and kinetic

Push a $100 \text{ kg}$ wooden crate across a concrete floor. Push gently and it doesn't move — friction adjusts itself to match exactly whatever you're applying. Push harder: still nothing. Then at some threshold, the crate suddenly slides. And once it's sliding, you find you don't have to push nearly as hard to keep it going.

Almost everything quantitative about friction is already in that anecdote.

When surfaces are in contact but not sliding, **static friction** can take any value up to a maximum:

$$f_s \leq \mu_s N,$$

where $N$ is the normal force pressing the surfaces together and $\mu_s$ is the **coefficient of static friction** — a dimensionless number that depends on the two materials. Static friction is not a fixed value; it is whatever is needed to prevent sliding, up to the maximum $\mu_s N$. Push with $50 \text{ N}$ on a crate whose maximum static friction is $200 \text{ N}$, and the friction force is $50 \text{ N}$, not $200$.

Once sliding begins, **kinetic friction** takes over:

$$f_k = \mu_k N.$$

This is an equality, not an inequality. Kinetic friction has a definite value once surfaces are in relative motion. And for almost every material pair, $\mu_k < \mu_s$ — the crate sticks until it suddenly slides, and it's harder to start sliding than to maintain it.

Typical coefficients:

| Surfaces | $\mu_s$ | $\mu_k$ |
|---|---|---|
| Rubber on dry concrete | 1.0 | 0.7 |
| Wood on wood | 0.5 | 0.3 |
| Steel on steel (dry) | 0.6 | 0.3 |
| Waxed wood on wet snow | 0.14 | 0.1 |
| Teflon on steel | 0.04 | 0.04 |
| Synovial joints (human knee) | 0.01 | 0.003 |

Notice the human joint at the bottom. Biology has engineered nearly frictionless bearings inside your knees and hips — synovial fluid lubricates collagen surfaces to a coefficient that would embarrass most machine designs.

<!-- → [CHART: friction force vs. applied force graph for a single object — x-axis: applied horizontal force (0 to well past sliding threshold); y-axis: friction force; flat line rising with slope 1 (static friction matching applied force) up to a peak at μₛN, then dropping to a lower constant value μₖN once sliding begins; annotate the peak as "maximum static friction," the drop as "kinetic takes over," and the flat right portion as "kinetic friction = constant"; caption: "the crate doesn't move until you exceed μₛN, and then it's easier to keep moving than it was to start"] -->

These values are approximate. Real friction coefficients depend on temperature, humidity, surface preparation, contamination, sliding speed, and whether the surfaces were recently in contact. The simple laws $f_s \leq \mu_s N$ and $f_k = \mu_k N$ are empirical fits that work well enough to design brakes and predict skidding distances, and should not be trusted to better than a factor of two under varying conditions.

Three misconceptions worth clearing immediately.

First: friction does not scale with contact area. A wide tire and a narrow tire with the same load on the same road produce the same friction force, because $f = \mu N$ depends on normal force, not how that force is spread across area. Real tires deviate from this at the edges of the regime, but the core result is robust.

Second: static friction is not always $\mu_s N$. It is *at most* $\mu_s N$. The crate in a gentle breeze experiences static friction equal to the tiny wind force on it, not the maximum value.

Third, and most counterintuitively: friction does not always oppose motion. It opposes *relative sliding between surfaces*. When a car accelerates from rest, the tire's contact patch tries to slide backward relative to the road — so friction from the road acts *forward* on the tire, and therefore forward on the car. Static friction from the road is what makes a car go. Without it, the wheels spin uselessly.

### A worked example — the slope and the coefficient

A skier glides down a $25°$ slope at constant velocity. What is the coefficient of kinetic friction?

Constant velocity means zero net force. Free-body diagram: weight $mg$ straight down, normal force $N$ perpendicular to the slope, kinetic friction $f_k$ up the slope opposing the motion.

Choose axes along and perpendicular to the slope. Perpendicular balance gives $N = mg\cos 25°$. Along-slope balance gives $f_k = mg\sin 25°$.

Apply $f_k = \mu_k N$:

$$\mu_k = \frac{mg\sin 25°}{mg\cos 25°} = \tan 25° \approx 0.466.$$

Two elegant results fall out immediately. The mass cancels — the coefficient equals $\tan\theta$ regardless of the skier's weight. And this gives a measurement technique: set any object sliding on an adjustable slope until it moves at constant velocity, measure the angle, and $\mu_k = \tan\theta$. Tilt the slope until the object just barely begins to slide and $\mu_s = \tan\theta_\text{just barely}$. Geometry plus equilibrium, no dynamometer required.

The value $0.47$ is higher than waxed wood on wet snow ($0.10$), which suggests poor wax, warm sticky snow, or a beginner's clunky skis. A real competition skier on good conditions might have $\mu_k \approx 0.03$.

<!-- → [DIAGRAM: free-body diagram for the skier on a 25° slope — show the slope as a tilted surface, weight mg straight down, normal force N perpendicular to slope surface, kinetic friction fₖ pointing up the slope; decompose weight into mg sinθ (along slope, down) and mg cosθ (into slope); label each force with its expression; show the two balance equations alongside; caption: "tilted axes make the algebra clean — align one axis with the slope, and both equations become one-liners"] -->

---

## Drag

### Terminal velocity — and why the feather and the hammer tell different stories in air

In a vacuum, every object falls at the same acceleration. On Earth, they don't — and now we know why.

Jump out of an aircraft at $4{,}000 \text{ m}$ in a stable face-down position. For the first second, you fall almost like a vacuum object: $g = 9.80 \text{ m/s}^2$, speed rising quickly. Air drag at low speed is small. But drag scales with $v^2$ — double your speed and drag quadruples. By the time you've reached $50 \text{ m/s}$, the drag force pressing up on your chest equals your weight pressing down. Net force: zero. Acceleration: zero. You're at **terminal velocity**, and there you stay until you pull the rip cord.

The equation governing drag at intermediate speeds — fast enough for turbulent flow around the object, slow enough to ignore compressibility — is:

$$F_D = \tfrac{1}{2} C \rho A v^2,$$

where $C$ is the dimensionless **drag coefficient** (depends on shape), $\rho$ is the fluid density, $A$ is the cross-sectional area presented to the flow, and $v$ is speed relative to the fluid. Set this equal to weight to find terminal velocity:

$$\tfrac{1}{2} C \rho A v_t^2 = mg, \quad \implies \quad v_t = \sqrt{\frac{2mg}{\rho C A}}.$$

Note the dependencies. Heavier means faster ($v_t \propto \sqrt{m}$). Larger area means slower ($v_t \propto 1/\sqrt{A}$). Denser fluid means much slower ($v_t \propto 1/\sqrt{\rho}$; water is $830$ times denser than air, so terminal velocity in water is about $\sqrt{830} \approx 29$ times slower than in air for the same object).

A $75 \text{ kg}$ skydiver in a stable face-down position, with $A = 0.70 \text{ m}^2$, $C = 0.70$, $\rho_\text{air} = 1.21 \text{ kg/m}^3$:

$$v_t = \sqrt{\frac{2 \times 75 \times 9.80}{1.21 \times 0.70 \times 0.70}} = \sqrt{\frac{1470}{0.593}} \approx 50 \text{ m/s}.$$

About $180 \text{ km/h}$. Published values for face-down skydivers run $50$–$60 \text{ m/s}$; our number sits comfortably in range. In a streamlined head-down dive, area $A$ and coefficient $C$ both fall, and terminal velocity can exceed $90 \text{ m/s}$. Under an open parachute, $A$ rises from $0.70 \text{ m}^2$ to roughly $30 \text{ m}^2$ and $C$ rises to about $1.4$, so terminal velocity drops to a survivable $\sim 5 \text{ m/s}$.

<!-- → [CHART: speed vs. time graph for a skydiver from jump to parachute deployment — curve starts at 0, rises steeply under near-free-fall acceleration, then flattens asymptotically toward terminal velocity (~50 m/s); at parachute deployment, curve drops sharply to the new lower terminal velocity (~5 m/s); annotate: "acceleration ≈ g at low speed," "net force → 0 at terminal velocity," "parachute triples C·A, dropping vₜ by factor of ~3"] -->

Now return to the feather and the hammer. On the Moon, no air, both fall at $g_\text{Moon} = 1.62 \text{ m/s}^2$, simultaneous arrival. On Earth, the feather has an enormous $A/m$ ratio — its terminal velocity is perhaps $1 \text{ m/s}$, reached essentially instantly. The hammer's $A/m$ ratio is small; its terminal velocity in air exceeds $30 \text{ m/s}$, so over a lab-bench drop it never approaches terminal velocity and falls nearly like a vacuum object. The two *appear* to fall at different rates because air drag dominates for one and not the other — not because gravity treats them differently.

The $v^2$ dependence is the key design fact. Drag at $40 \text{ m/s}$ is sixteen times drag at $10 \text{ m/s}$. Engine power needed to overcome drag at constant speed scales as $F_D \times v$, which scales as $v^3$ — double your cruising speed and you need eight times the engine power. This is why streamlined cars matter almost not at all in a parking lot and enormously on a highway.

The $v^2$ form breaks at extremes. For very slow motion or very small objects — bacteria, aerosol particles, falling dust — the flow around the object never becomes turbulent and drag switches to the Stokes regime: $F_D = 6\pi\eta r v$, proportional to $v$ rather than $v^2$. A $1 \text{ μm}$ bacterium in water reaches its terminal velocity (under gravity) in microseconds, at a speed of roughly $0.1 \text{ μm/s}$ — so slow that a bacterium would need months to fall one millimeter under gravity alone. That's why bacteria need flagella: passive gravitational settling is useless to them. The boundary between the two drag regimes is set by the Reynolds number, which Chapter 12 will develop properly.

---

## Elasticity

### The law that spans a guitar string, a tendon, and a bridge cable

Pluck a steel guitar string. It vibrates at a pitch set by its tension, length, and density. Tighten the tuning peg — the string stretches, the pitch rises. Stretch a tendon in your wrist by lifting a heavy weight; the tendon elongates slightly and recovers when you set the weight down. Hang a load from a steel crane cable; the cable stretches a measurable amount and returns to its original length when the load is removed.

All three share a structure. Apply a force; the object deforms. Remove the force; it recovers. For small enough deformations, the deformation is proportional to the force. That is Hooke's law:

$$F = k \, \Delta L,$$

where $\Delta L$ is the change in length and $k$ is the **spring constant** — a property that combines the material's intrinsic stiffness and the object's geometry.

For a uniform rod or wire of length $L_0$, cross-sectional area $A$, and Young's modulus $Y$ (a material property with units of Pa):

$$\Delta L = \frac{F L_0}{Y A}.$$

Young's modulus captures the material's intrinsic resistance to being stretched or compressed, independent of the rod's particular dimensions. Some values:

- Steel: $Y \approx 200 \times 10^9 \text{ Pa}$
- Aluminum: $Y \approx 70 \times 10^9 \text{ Pa}$
- Bone (in compression): $Y \approx 9 \times 10^9 \text{ Pa}$
- Rubber: $Y \approx 10^7 \text{ Pa}$ — roughly $20{,}000$ times less stiff than steel

The $k$ in Hooke's law is not purely a material property. A long thin steel rod has a smaller $k$ than a short thick steel rod of the same material. $k = YA/L_0$: stiffness increases with cross-section and decreases with length. Geometry and material combine.

Hooke's law is a linear approximation. For small deformations, force and displacement are proportional; this is the elastic regime. For larger deformations, the relationship curves. At the **elastic limit**, permanent (plastic) deformation begins. Beyond that, fracture. A useful fact for steel: the elastic regime ends at a strain ($\Delta L / L_0$) of roughly $0.001$–$0.002$. Engineering structures are almost always designed to stay well below this.

Hooke's law generalizes to three modes of deformation beyond simple tension/compression. **Shear** deformation — sliding one face of an object relative to the opposite face — is governed by the shear modulus $S$. **Volume compression** — squeezing an object uniformly from all sides — is governed by the bulk modulus $B$. All three have the same algebraic structure: deformation proportional to applied stress (force per unit area), with a material-specific modulus governing the proportionality.

<!-- → [DIAGRAM: three-panel illustration of deformation modes — left: a rectangular block with arrows pulling top and bottom apart (tension/compression, ΔL along axis); center: the same block with the top face displaced sideways while the bottom is fixed (shear, Δx perpendicular to load); right: a sphere with pressure arrows from all directions (bulk compression, ΔV); each panel labels the relevant modulus (Y, S, B) and the deformation variable; caption: "same algebraic structure in all three cases: deformation = (stress) / (modulus)"] -->

A worked example. A $10.0 \text{ m}$ steel cable with cross-section $A = 1.0 \times 10^{-4} \text{ m}^2$ supports a $1{,}000 \text{ kg}$ load:

$$F = mg = 9{,}800 \text{ N},$$

$$\Delta L = \frac{F L_0}{Y A} = \frac{9800 \times 10.0}{200 \times 10^9 \times 1.0 \times 10^{-4}} = \frac{98{,}000}{2.0 \times 10^7} = 4.9 \times 10^{-3} \text{ m} = 4.9 \text{ mm}.$$

The cable stretches by about $5 \text{ mm}$ — half a percent of a percent of its length. Strain: $4.9 \times 10^{-4}$, well below the elastic limit. The cable recovers completely when the load is removed.

<!-- → [DIAGRAM: stress-strain curve for steel — x-axis: strain ΔL/L₀; y-axis: stress F/A; show three labeled regions: (1) linear Hooke's-law region (slope = Young's modulus Y) from 0 to ~0.001 strain, (2) yield point where permanent deformation begins, (3) fracture point; mark the steel cable example's operating strain (~4.9×10⁻⁴) with a dot well within the linear region; caption: "Hooke's law is the slope of this curve at the origin — valid until you hit the yield point, after which the material never fully recovers"] -->

What Hooke's law makes possible, practically: predict the deformation of any structure from its load and geometry; design structures to stay below specified deflections; and, reading backward, infer loads from measured deformations (strain gauges). Every accelerometer in your phone uses Hooke's law — a tiny beam deflects under acceleration, and the deflection is read electronically. Every guitar string, every trampoline, every tendon in your body is operating in the linear elastic regime of Hooke's law when it's working properly.

The misconception to avoid: Hooke's law is not universal. It holds for small deformations of a wide range of solid materials, and it breaks — suddenly or gradually — when those deformations get large enough. For rubber, the regime is broader (rubber is hyperelastic). For biological tissues, the relationship is often nonlinear from the start. The law earns its place by working extremely well within its domain and by having that domain coincide with almost all ordinary structural situations.

---

## Three laws, one framework

Step back and look at what the three empirical laws do for Newton's second law. $F = ma$ is always true. But it is useless until you know what the forces are. Friction gives you: $f = \mu N$ once you know which surfaces are in contact and whether they're sliding. Drag gives you: $F_D = \tfrac{1}{2}C\rho Av^2$ once you know the shape, the medium, and the speed. Hooke's law gives you: $F = k\Delta L$ once you know the spring constant and the deformation. Each law converts a qualitative identification of a force into a number you can put into $F = ma$ and solve.

The three laws cover an enormous practical range. Friction is why a car can stop in $30 \text{ m}$ from $100 \text{ km/h}$ and a wet road doubles that distance. Drag is why a $747$ needs $40 \text{ MW}$ of engine power to maintain cruise, and why a parachute reduces that same person's terminal velocity from $50 \text{ m/s}$ to $5 \text{ m/s}$ by changing one parameter. Elasticity is why a guitar string vibrates at the pitch it does and why a steel bridge deflects by millimeters rather than meters under traffic load.

And all three derive, in principle, from the electromagnetic interactions between atoms in materials. Friction is ultimately electrons on two surfaces attracting and interlocking. Drag is molecules being shoved aside and the momentum transferred to the fluid. Elasticity is atomic bonds stretching when the lattice is deformed. We don't compute any of these from first principles in an introductory course, because the many-body problem is intractable. Instead we fit simple laws to measurements, understand their domains, and use them. This is a clean example of the strategy physics uses throughout: find the effective description at the scale you care about, don't derive it from scratch every time.

<!-- → [INFOGRAPHIC: three-column "domain map" for the chapter's force laws — column 1 (Friction): situations where it dominates (walking, braking, bolts, climbing), regime where it fails (very high normal forces causing plastic surface deformation; very clean surfaces in vacuum); column 2 (Drag): situations where it dominates (skydiving, cycling, ship hulls), regime where it fails (very slow/small objects → Stokes; very fast objects → compressibility); column 3 (Elasticity): situations where it dominates (springs, beams, tendons, strings), regime where it fails (beyond elastic limit → plastic deformation → fracture); caption: "knowing the law is step one; knowing where it breaks down is step two"] -->

Feynman once remarked that friction was still, in some deep sense, the worst-understood common phenomenon in classical physics — despite $f = \mu N$ being taught in every introductory course. The law works. The microscopic story is genuinely complicated. The two facts coexist without contradiction. That is physics.

---

## Exercises

### Warm-up

**7.1** A $100 \text{ N}$ horizontal force is applied to a $50 \text{ kg}$ box on a level floor. Coefficients: $\mu_s = 0.4$, $\mu_k = 0.3$. (a) Compute the maximum static friction. (b) Will the box move? (c) If yes, what is the kinetic friction force?

**7.2** A box rests on a ramp. The angle is slowly increased. The box first slips at $\theta = 30°$. What is $\mu_s$?

**7.3** A $0.145 \text{ kg}$ baseball with $A = 0.0042 \text{ m}^2$ and $C = 0.40$ moves at $40 \text{ m/s}$ through air ($\rho = 1.21 \text{ kg/m}^3$). What is the drag force?

**7.4** A spring stretches $5.0 \text{ cm}$ when a $2.0 \text{ kg}$ mass hangs from it. What is the spring constant $k$?

### Application

**7.5** A $50 \text{ kg}$ crate is pushed up a $20°$ ramp at constant velocity. Coefficient of kinetic friction is $\mu_k = 0.30$. (a) Draw the free-body diagram. (b) What pushing force (parallel to the ramp) is required?

**7.6** A car of mass $1{,}500 \text{ kg}$ brakes from $25 \text{ m/s}$ to a stop on dry pavement ($\mu_k = 0.7$). (a) What is the friction force? (b) What is the deceleration? (c) How far does the car travel before stopping?

**7.7** A $60 \text{ kg}$ skydiver has $A = 0.50 \text{ m}^2$ and $C = 0.70$. (a) Compute her terminal velocity. (b) When she opens her parachute, $A$ increases to $30 \text{ m}^2$ and $C$ becomes $1.4$. What is her new terminal velocity?

**7.8** A nylon climbing rope of length $50 \text{ m}$ and cross-sectional area $1.0 \text{ cm}^2$ supports an $80 \text{ kg}$ climber. Take $Y_\text{nylon} \approx 5 \times 10^9 \text{ Pa}$. How much does the rope stretch?

### Synthesis

**7.9** A skier of mass $70 \text{ kg}$ glides down a $25°$ slope. The kinetic friction coefficient is $\mu_k = 0.05$. Her drag area is $A = 0.50 \text{ m}^2$, $C = 0.70$, $\rho_\text{air} = 1.21 \text{ kg/m}^3$. Find her terminal velocity down the slope.

**7.10** A $20 \text{ kg}$ box is suspended from a vertical spring with $k = 5{,}000 \text{ N/m}$. The system is at rest. (a) What is the spring's stretch? (b) If you press down on the box with an additional $30 \text{ N}$ (and hold it stationary), how much further does the spring stretch? (c) If instead you pull the box down by $1 \text{ cm}$ and release it, what is the initial restoring force?

**7.11** A bicyclist coasts down a hill of slope $5°$ at terminal speed $15 \text{ m/s}$. Bicycle plus rider mass is $80 \text{ kg}$. Drag area $A = 0.50 \text{ m}^2$, $C = 1.0$, $\rho_\text{air} = 1.21 \text{ kg/m}^3$. (a) Compute the drag force at terminal speed. (b) Compute the rolling friction force. (c) What is the implied rolling coefficient?

### Challenge

**7.12** Find the terminal velocity of a $1.0 \text{ μm}$ bacterium ($\rho = 1{,}000 \text{ kg/m}^3$) in water ($\eta = 10^{-3}$ Pa·s) using Stokes drag $F_D = 6\pi\eta r v$. Compare to the bacterium's own swimming speed (about $30 \text{ μm/s}$). What does this say about why bacteria need flagella to get anywhere useful?

**7.13** A vertical steel column $5 \text{ m}$ long supports a $50{,}000 \text{ kg}$ load. (a) For the column not to compress by more than $1 \text{ mm}$, what must its cross-sectional area be? (Use $Y_\text{steel} = 200 \times 10^9 \text{ Pa}$.) (b) What is the stress on the column? (c) Look up steel's yield stress and verify the column is well within its elastic limit.

---

## LLM Exercise — Chapter 7: Friction, Drag, and Elasticity in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** Quantitative estimates of one friction, one drag, or one elastic-deformation effect in your anchor phenomenon.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 7, I want to apply one or more of: friction laws, drag equations, or Hooke's law to my phenomenon. Please:

1. Identify ONE relevant friction, drag, or elastic effect in my phenomenon. Examples:
   - Bike commute: rolling friction of tires against road; air drag at cruising speed; tire deformation under weight (Hooke's law in compressed rubber).
   - Coffee maker: friction in the pump; drag of water through coffee grounds; spring loading on the brewing chamber gasket.
   - Basketball: drag on the ball during flight; friction between hand and ball at release; deformation of ball on impact with rim.
   - Marathon: friction at each footstrike (preventing slip); drag at running speed; tendon/Achilles deformation under load.
   - Espresso: friction in the puck during 9-bar extraction; drag of water through grounds; spring force in the pressure relief valve.

2. Identify the relevant equation ($f = \mu N$, $F_D = \tfrac{1}{2} C \rho A v^2$, $F = k \Delta L$).

3. Estimate the relevant inputs: coefficient, area, density, spring constant. For each: where to source the value and what uncertainty to expect.

4. Compute the force or deformation. Report with units, sig figs, and percent uncertainty.

5. Sanity-check with one Fermi estimate.

6. Identify which assumption (linear elasticity, constant μ, constant C, ignored Reynolds-regime change) is most likely to bite.

7. One sentence on what energy is lost to this force (preview Chapter 8).

Save the output as logbook/chapter-07-friction-drag-elasticity.md.
```

### What this produces

A seventh Logbook entry: a quantitative force-law analysis applied to your phenomenon, often surprising in magnitude. (How big is rolling friction on a bike? Bigger than you think at low speeds, smaller than drag at high speeds.)

### How to adapt this prompt

- *For phenomena that are mostly steady-state* (a coffee maker at equilibrium, a marathon at race pace): emphasize force *balance* — what equals the friction or drag.
- *For ChatGPT or Gemini:* identical with interface substitutions.
- *For Claude Code:* if you have video data (e.g., a basketball trajectory you can frame-grab) you can compute drag from the deceleration; paste the data.

### Connection to previous chapters

Builds on Chapter 6 (Newton's laws, $F = ma$) by giving you specific force laws for contact and deformation. Builds on Chapter 5 (vector decomposition) for inclined-plane work and any 2D friction problem.

### Preview of next chapter

Chapter 8 introduces energy as an alternative accounting framework. Friction and drag will be the principal mechanisms by which mechanical energy converts to heat. The Chapter 8 LLM Exercise will look at energy dissipation in your phenomenon — how much kinetic or potential energy is lost to friction or drag per cycle.

---

## AI Wayback Machine

**Charles-Augustin de Coulomb** was an 18th-century French physicist who quantified friction in his 1781 prize-winning essay — distinguishing static from kinetic friction, characterizing the role of normal force, and producing the laws we still teach. He's mostly remembered for electricity, but he founded mechanical friction theory.

**Run this:**

```
Who was Coulomb, and how does his work on friction connect to the Newton's-law applications we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Charles-Augustin de Coulomb"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Coulomb's empirical laws of friction — which still hold up under modern materials science?
- Ask it about Coulomb's parallel career as a military engineer in the French colonies.

What changes? What gets better? What gets worse?
