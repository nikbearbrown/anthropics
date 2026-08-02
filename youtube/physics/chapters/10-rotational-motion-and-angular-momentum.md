# Chapter 10 — Rotational Motion and Angular Momentum

*The same mechanics, turned.*

---

In 1054 AD, Chinese and Arab astronomers watched a star explode. For three weeks it was bright enough to see in daylight. For almost two years it remained visible at night. Today, in the same patch of sky in the constellation Taurus, we see a cloud of gas still expanding outward — the Crab Nebula — and at its center, a tiny object, barely ten kilometers across, that weighs about one and a half times as much as the Sun.

That object rotates. About thirty times per second.

![Two-panel comparison: figure skater pulling arms in (R drops 10×, ω rises 100×) and stellar core collapse to a neutron star (R drops 10⁵×, ω rises 10¹⁰× — from one rev/month to 30 rev/s for the Crab Pulsar). Same L = Iω...](../images/10-rotational-motion-and-angular-momentum-fig-05.png)
*Figure 10.5 — Skater and Crab Pulsar — Same Conservation Law, Wildly Different Scales*

The star that collapsed to make it was rotating roughly once per month. Then the collapse happened — the core shrank from perhaps a billion meters across to ten thousand meters across, a factor of about $10^5$ in radius, $10^{10}$ in area. The moment of inertia, which scales as $R^2$, shrank by that factor. And because no external torque acts on a collapsing star to change its angular momentum, the angular velocity had to grow by the same factor. A rotation period of one month became, in a few seconds, a rotation period of a few milliseconds. One of the most violent events in the universe — and it's the same physics as a figure skater pulling her arms in.

This chapter is about rotation. Everything in it has an exact parallel in the previous eight chapters. Position becomes angle, velocity becomes angular velocity, mass becomes moment of inertia, force becomes torque, momentum becomes angular momentum. The equations are the same structure. The conservation law is new, but the reasoning that produces it is the same reasoning that produced conservation of linear momentum. The only genuinely new idea here is that the "mass" for rotation — the moment of inertia — depends not just on how much mass an object has but on where that mass is relative to the axis of rotation.

<!-- → [FIGURE: Two-panel size comparison. Left: a red supergiant star with radius ~7×10⁸ m, slowly rotating (one arrow indicating direction, labeled "~1 rev/month"). Right: a neutron star with radius ~10⁴ m, rapidly rotating (multiple arrows, labeled "~30 rev/s"). Both labeled with their radii. Caption: The same star, before and after core collapse. The radius shrank by a factor of ~70,000. The moment of inertia shrank by the square of that factor. Angular momentum conservation required the rotation rate to increase by the same factor.] -->

---

## The vocabulary: everything has an angular twin

Start with a wheel spinning about a fixed axle. A point on the rim traces a circular arc. If the wheel has turned through angle $\theta$ (in radians), a point at radius $r$ has traveled arc length:

$$s = r\theta.$$

This is the definition of a radian — the angle such that $s = r$. It's why radians are the natural unit: no conversion factor, just the geometry.

Differentiate once with respect to time. The rate at which the angle changes is the **angular velocity**:

$$\omega = \frac{d\theta}{dt},$$

and the rate at which a point on the rim moves is the **tangential speed**:

$$v = r\omega.$$

Differentiate again. The rate at which $\omega$ changes is the **angular acceleration** $\alpha$, and the tangential acceleration of a point on the rim is $a_t = r\alpha$. There is also the centripetal acceleration from Chapter 6, $a_c = v^2/r = r\omega^2$, pointing inward; the total acceleration of a rim point is the vector sum of these two.

<!-- → [FIGURE: Rotating wheel diagram showing a point on the rim. Two perpendicular acceleration arrows at the point: a_t (tangential, in direction of motion) and a_c (centripetal, toward center). Velocity vector shown tangent to the circle. Caption: A point on a spinning wheel has two acceleration components — tangential (changing its speed) and centripetal (changing its direction). They're perpendicular and both nonzero when the wheel is speeding up.] -->

The rotational kinematic equations for constant angular acceleration $\alpha$ follow immediately from the translational ones by substituting $\theta$ for $x$, $\omega$ for $v$, and $\alpha$ for $a$:

$$\omega = \omega_0 + \alpha t,$$
$$\theta = \theta_0 + \omega_0 t + \tfrac{1}{2}\alpha t^2,$$
$$\omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0).$$

That's the entire rotational kinematics toolkit. Not new equations — the same equations, with the variables renamed.

**A quick example.** A motorcycle wheel of radius $0.30 \text{ m}$ spins from rest to a rim speed of $30 \text{ m/s}$ in $5$ seconds. Final angular velocity: $\omega = v/r = 30/0.30 = 100 \text{ rad/s}$. Angular acceleration: $\alpha = \Delta\omega/\Delta t = 100/5 = 20 \text{ rad/s}^2$. Total angle turned: $\theta = \tfrac{1}{2}\alpha t^2 = \tfrac{1}{2}(20)(25) = 250 \text{ rad} \approx 40 \text{ revolutions}$. Same algebra as a decelerating car in Chapter 2 — different labels.

<!-- → [TABLE: Linear-rotational analogies. Two-column table. Left column header: Linear. Right column header: Rotational. Rows: position x / angle θ, velocity v / angular velocity ω, acceleration a / angular acceleration α, mass m / moment of inertia I, force F / torque τ, p = mv / L = Iω, KE = ½mv² / KE_rot = ½Iω², F = ma / τ = Iα, conservation of p / conservation of L. Caption: Every linear quantity has a rotational twin. The equations are structurally identical — the same physics, turned.] -->

---

## What resists rotation: moment of inertia

In translational mechanics, mass is the measure of inertia — how hard it is to change velocity. In rotational mechanics, the analog is **moment of inertia** $I$ — how hard it is to change angular velocity. But there is a crucial difference: mass is just a number for a given object, while moment of inertia depends on the axis of rotation and on how the mass is distributed relative to that axis.

For a single point mass $m$ at distance $r$ from the axis:

$$I = mr^2.$$

For an extended body, sum over all mass elements:

$$I = \sum m_i r_i^2 \quad \text{(or } \int r^2\, dm \text{ for continuous bodies)}.$$

![Two stylized skater silhouettes: arms out (large moment of inertia, slow spin) and arms in (small moment of inertia, fast spin). L = Iω is constant; if I drops by 4×, ω rises by 4×.](../images/10-rotational-motion-and-angular-momentum-fig-01.png)
*Figure 10.1 — Skater Spin — L = Iω Conserved; Pull Arms In, ω Quadruples*

The $r^2$ dependence is the key. Mass far from the axis contributes much more to $I$ than the same mass close to the axis. This is why it's harder to start a merry-go-round spinning by pushing at the center than by pushing at the rim. It's why a figure skater pulls her arms in to spin faster — she's reducing the distance of her arm mass from the rotation axis, reducing $I$.

For common shapes (derivable by integration, but taken as given here):

- Solid disk or cylinder, axis through center: $I = \tfrac{1}{2}MR^2$.
- Thin hoop, axis through center: $I = MR^2$.
- Solid sphere: $I = \tfrac{2}{5}MR^2$.
- Thin rod, axis through center: $I = \tfrac{1}{12}ML^2$.
- Thin rod, axis through end: $I = \tfrac{1}{3}ML^2$.

Notice that the hoop has twice the moment of inertia of the solid disk with the same mass and radius. All the hoop's mass is at the maximum distance $R$; the disk's mass is spread from the center out, so the average $r^2$ is smaller. Same mass, same radius, but the hoop is harder to spin up and harder to spin down.

<!-- → [FIGURE: Side-by-side diagrams of a solid disk and a hoop, same radius and mass. Each labeled with its I formula. Caption: Same mass M, same radius R. The hoop's moment of inertia is MR² — twice the disk's ½MR² — because all the hoop's mass sits at radius R while the disk's mass is distributed from 0 to R. This difference determines who wins a rolling race.] -->

<!-- → [TABLE: Moment of inertia for common shapes. Columns: shape, axis, formula, I/MR² ratio. Rows: solid disk (through center, ½MR², 0.5), thin hoop (through center, MR², 1.0), solid sphere (through center, ⅖MR², 0.4), thin rod (through center, 1/12 ML², depends on L/R), thin rod (through end, ⅓ML², depends). Caption: The I/MR² ratio is the shape factor that determines rolling-race outcomes. Smaller ratio = faster at the bottom of a ramp. The solid sphere wins any rolling race against a disk or hoop of the same mass and radius.] -->

This leads directly to the rotational Newton's second law:

$$\tau_{\text{net}} = I\alpha.$$

The torque $\tau$ (from Chapter 9, $\tau = rF\sin\theta$ — force times perpendicular distance from the axis) drives angular acceleration inversely proportional to the moment of inertia. Apply the same torque to a hoop and a disk: the disk accelerates faster, because its $I$ is smaller. Exactly as in translation: same force, lighter object accelerates more.

**A worked example.** A playground merry-go-round approximated as a solid disk: $M = 200 \text{ kg}$, $R = 1.5 \text{ m}$.

$$I = \tfrac{1}{2}MR^2 = \tfrac{1}{2}(200)(1.5)^2 = 225 \text{ kg·m}^2.$$

A child pushes tangentially at the rim with $F = 50 \text{ N}$, so $\tau = RF = (1.5)(50) = 75 \text{ N·m}$.

$$\alpha = \frac{\tau}{I} = \frac{75}{225} \approx 0.33 \text{ rad/s}^2.$$

In thirty seconds of steady pushing, it reaches $\omega = \alpha t = 0.33 \times 30 = 10 \text{ rad/s}$, about $1.6$ revolutions per second. A child's gentle push, sustained, produces a respectable spin rate. The moment of inertia determined how quickly the energy accumulated in rotation.

---

## Rotational kinetic energy and rolling

A rotating object has kinetic energy stored in its rotation:

$$KE_{\text{rot}} = \tfrac{1}{2}I\omega^2.$$

The parallel to $\tfrac{1}{2}mv^2$ is exact, with $I$ replacing $m$ and $\omega$ replacing $v$.

An object that is both translating and rotating — a ball rolling across the floor — has both kinds:

$$KE_{\text{total}} = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2.$$

![Four objects released simultaneously from the top of a frictionless ramp. The frictionless block slides fastest; among rolling objects, sphere > disk > hoop. Mass distribution (via I) determines how much PE goes to translation...](../images/10-rotational-motion-and-angular-momentum-fig-03.png)
*Figure 10.3 — Rolling Race — Block, Sphere, Disk, Hoop Down the Same Ramp*

For rolling without slipping, $v = R\omega$, which links the two. Energy conservation then tells you something about which shapes roll faster down an incline. Take two objects of the same mass and radius — a solid disk and a hoop — released from the same height $h$ on a ramp. Energy conservation:

$$mgh = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2.$$

Substitute $v = R\omega$ and the appropriate $I$. For the disk ($I = \tfrac{1}{2}mR^2$):

$$mgh = \tfrac{1}{2}mv^2 + \tfrac{1}{2}(\tfrac{1}{2}mR^2)(v/R)^2 = \tfrac{3}{4}mv^2 \implies v = \sqrt{\tfrac{4}{3}gh}.$$

For the hoop ($I = mR^2$):

$$mgh = \tfrac{1}{2}mv^2 + \tfrac{1}{2}(mR^2)(v/R)^2 = mv^2 \implies v = \sqrt{gh}.$$

The disk reaches the bottom faster — $\sqrt{4gh/3}$ vs. $\sqrt{gh}$. Gravity had the same energy to distribute for both objects; the disk, with smaller $I$, put more of it into translational motion. The hoop, with larger $I$, put more into rotation. Both conserved energy, but with different allocations.

Note that mass and radius canceled. The result depends only on the ratio $I/mR^2$ — the shape, not the size or weight. A small disk and a large disk with the same ratio reach the bottom at the same speed. You can test this with any two rolling objects of the same shape and different sizes: they tie.

![Two objects: solid disk (mass spread across radius, I = ½MR²) and hoop (mass at rim, I = MR²). Same total mass M and radius R. Hoop's I is twice the disk's. Mass distribution matters.](../images/10-rotational-motion-and-angular-momentum-fig-02.png)
*Figure 10.2 — Disk vs Hoop — Where the Mass Lives Determines I*

<!-- → [FIGURE: Side-by-side inclined ramp showing disk and hoop at top, with v_disk > v_hoop labeled at bottom. Energy bar charts beside each object showing the partition: disk has more KE_trans, hoop has more KE_rot, both total mgh. Caption: Same height, same mass, same radius — but the disk wins. Its smaller moment of inertia means less energy goes into rotation and more into forward motion.] -->

---

## Angular momentum and its conservation

The rotational analog of linear momentum is **angular momentum**:

$$L = I\omega.$$

And the rotational analog of Newton's second law in momentum form ($F = dp/dt$) is:

$$\tau_{\text{net}} = \frac{dL}{dt}.$$

From this follows the conservation law immediately: if no net external torque acts, $L$ is constant. Internal torques — like a skater pulling her own arms — cancel in pairs by Newton's third law, exactly as internal forces do for linear momentum. Only external torques change $L$.

This is the conservation law that explains the figure skater, the collapsing star, and every gyroscope. Let's work through the skater explicitly.

**A figure skater.** Arms out: $I_i = 4.0 \text{ kg·m}^2$, $\omega_i = 1.5 \text{ rev/s}$.

Arms pulled in: $I_f = 1.0 \text{ kg·m}^2$.

No external torque (ice friction is negligible on short timescales). Conservation of angular momentum:

$$I_i\omega_i = I_f\omega_f \implies (4.0)(1.5) = (1.0)\omega_f \implies \omega_f = 6.0 \text{ rev/s}.$$

She quadrupled her spin rate by reducing her moment of inertia by a factor of four.

Now check the energy. Her rotational kinetic energy before: $\tfrac{1}{2}(4.0)(2\pi \times 1.5)^2 \approx 178 \text{ J}$. After: $\tfrac{1}{2}(1.0)(2\pi \times 6.0)^2 \approx 711 \text{ J}$. Energy increased by a factor of four.

![Bar chart for arms-out vs arms-in. L = Iω is the same in both. KE_rot = ½Iω² is 4× larger when arms come in, because ω rises 4×. The extra energy came from muscles doing work to pull arms in against centrifugal tension.](../images/10-rotational-motion-and-angular-momentum-fig-04.png)
*Figure 10.4 — Skater Bar Chart — L Stays, KE Quadruples; Muscles Did Work*

This is not a violation of energy conservation. Her muscles did work pulling her arms inward against the apparent centrifugal resistance. That work — about $533 \text{ J}$ — is now stored as additional rotational kinetic energy. Angular momentum was conserved; energy was added. Both conservation laws hold; they're accounting for different things.

<!-- → [FIGURE: Two-panel skater diagram. Left panel: arms out, slow rotation, I large, ω small, L = Iω labeled. Right panel: arms pulled in, fast rotation, I small, ω large, L = Iω labeled same value. Caption: L = Iω stays constant. When I shrinks by 4, ω grows by 4. The skater's muscles did work during the pull — that energy went into the increased KE. Angular momentum conservation and energy conservation are compatible.] -->

### The neutron star again

The argument for the Crab Nebula pulsar is the same algebra, scaled by fourteen orders of magnitude. The progenitor star, a red supergiant, had radius $R_i \sim 7 \times 10^8 \text{ m}$ and was rotating roughly once per month, $\omega_i \approx 2.4 \times 10^{-6} \text{ rad/s}$.

The collapsed core has radius $R_f \approx 10^4 \text{ m}$.

Treat both as uniform spheres with $I = \tfrac{2}{5}MR^2$ (a rough approximation; the mass distribution changes during collapse, but this gives the right order):

$$I \propto R^2, \quad \text{so} \quad \frac{I_f}{I_i} = \left(\frac{R_f}{R_i}\right)^2 = \left(\frac{10^4}{7\times10^8}\right)^2 \approx 2\times10^{-10}.$$

Conservation of angular momentum:

$$\omega_f = \omega_i \cdot \frac{I_i}{I_f} = 2.4\times10^{-6} \times 5\times10^9 \approx 1.2\times10^4 \text{ rad/s}.$$

That corresponds to about $2{,}000$ rotations per second — faster than the observed $30 \text{ Hz}$, which is consistent: the real collapse is messier (mass is ejected, the density profile isn't uniform, the magnetic field brakes the rotation). The order-of-magnitude prediction is right. The same principle that explains a spin in a skating rink explains a pulsar.

<!-- → [CHART: Log-scale plot showing ω vs. object for conservation-of-angular-momentum examples. Objects on x-axis: playground merry-go-round with child jumping on (ω decreases), figure skater arms out → arms in (ω increases 4×), collapsing star → neutron star (ω increases ~10⁹×). Y-axis: angular velocity in rad/s, log scale from 10⁻⁶ to 10⁴. Caption: Angular momentum conservation across fourteen orders of magnitude in angular velocity. Same algebra — I₁ω₁ = I₂ω₂ — in every case.] -->

---

## Why angular momentum is a separate conservation law

You might wonder: do we really need both conservation of linear momentum and conservation of angular momentum? Are they the same thing stated twice?

They are not. They come from different symmetries of nature. Conservation of linear momentum comes from the fact that the laws of physics are the same here as they are one meter to the left — translational symmetry of space. Conservation of angular momentum comes from the fact that the laws of physics are the same in every direction — rotational symmetry of space. These are independent symmetries, and so the conservation laws are independent.

A car moving in a straight line has linear momentum but zero angular momentum about any point on its path. A spinning top in place has angular momentum but zero linear momentum. They can be converted into each other (push the top sideways and it gains linear momentum), but each is conserved separately by a different symmetry.

This was proved in full generality by Emmy Noether in 1915. The theorem bearing her name is one of the foundational results of theoretical physics: for every continuous symmetry of the laws of physics, there exists a conserved quantity. Linear momentum from translational symmetry. Angular momentum from rotational symmetry. Energy from time-translation symmetry. The three conservation laws you've learned in this course each trace to a symmetry of the structure of the universe.

<!-- → [INFOGRAPHIC: Three-column diagram titled "Noether's Theorem." Column headers: Symmetry of Nature | Conservation Law | Example. Row 1: Space is the same in all directions (rotational symmetry) → Angular momentum L → Figure skater, pulsar. Row 2: Space is the same at all locations (translational symmetry) → Linear momentum p → Rocket, collision. Row 3: Laws are the same at all times (time-translation symmetry) → Energy E → Roller coaster, orbit. Caption: Every conservation law in this course has a symmetry behind it. Noether proved this connection in 1915. If any symmetry were broken, its conservation law would fail — and that failure would be a discovery.] -->

---

## The parallel structure, in full

Chapters 2 through 4 gave you translational mechanics. This chapter gives you the rotational twin. The table of analogies is exact:

| Linear | Rotational |
|---|---|
| Position $x$ | Angle $\theta$ |
| Velocity $v$ | Angular velocity $\omega$ |
| Acceleration $a$ | Angular acceleration $\alpha$ |
| Mass $m$ | Moment of inertia $I$ |
| Force $F$ | Torque $\tau$ |
| $F = ma$ | $\tau = I\alpha$ |
| Momentum $p = mv$ | Angular momentum $L = I\omega$ |
| $KE = \tfrac{1}{2}mv^2$ | $KE_{\text{rot}} = \tfrac{1}{2}I\omega^2$ |
| Conservation of $\mathbf{p}$ | Conservation of $\mathbf{L}$ |

The only thing that doesn't have a clean translational twin is the geometry-dependence of $I$. Mass is a fixed scalar for a given object. Moment of inertia changes with the axis you choose and with how the object deforms. That's the one genuinely new feature of rotational mechanics — and it's what lets ice skaters and pulsars change their rotation rate without any external torque.

![Logarithmic ladder labeled with L values: electron orbital (~10⁻³⁴ J·s), spinning top (~10⁻³ J·s), figure skater (~50 J·s), Earth rotation (~7×10³³ J·s), Milky Way (~10⁶⁷ J·s). One quantity from ℏ to the galaxy.](../images/10-rotational-motion-and-angular-momentum-fig-06.png)
*Figure 10.6 — Angular Momentum Across 80 Orders of Magnitude*

The scale of it is worth sitting with. Conservation of angular momentum works for a child on a playground merry-go-round ($L \sim 10^2 \text{ kg·m}^2/\text{s}$), a spinning gyroscope ($L \sim 1 \text{ kg·m}^2/\text{s}$), Earth's rotation ($L \sim 7 \times 10^{33} \text{ kg·m}^2/\text{s}$), and a neutron star ($L \sim 10^{40} \text{ kg·m}^2/\text{s}$). Across forty orders of magnitude. The same algebra.

---

## Exercises

### Warm-up

**10.1** *(LO 1)* A wheel of radius $0.40 \text{ m}$ rotates at $20 \text{ rad/s}$. (a) Linear speed of a point on the rim? (b) Angular velocity in RPM?

**10.2** *(LO 1, 2)* A flywheel accelerates from $10 \text{ rad/s}$ to $30 \text{ rad/s}$ in $5.0 \text{ s}$. (a) Angular acceleration? (b) Angle turned through?

**10.3** *(LO 3)* A solid disk ($5.0 \text{ kg}$, $0.30 \text{ m}$ radius) has torque $10 \text{ N·m}$ applied at the rim. Angular acceleration?

**10.4** *(LO 5)* A skater has $I = 5.0 \text{ kg·m}^2$ and $\omega = 4.0 \text{ rad/s}$. Angular momentum?

### Application

**10.5** *(LO 4)* A solid sphere ($2.0 \text{ kg}$, $0.10 \text{ m}$ radius) rolls without slipping at $5.0 \text{ m/s}$. (a) Translational KE. (b) Rotational KE. (c) Total KE. (d) Fraction in rotation.

**10.6** *(LO 3, 4)* A solid disk ($3.0 \text{ kg}$, $0.50 \text{ m}$ radius) rolls without slipping down a $30°$ incline of height $2.0 \text{ m}$. (a) Speed at the bottom. (b) Compare to frictionless slide from same height.

**10.7** *(LO 5)* A merry-go-round (solid disk, $200 \text{ kg}$, $1.5 \text{ m}$ radius) spins at $1.0 \text{ rad/s}$. A $40 \text{ kg}$ child jumps on at the rim. (a) New angular velocity? (b) KE lost? (c) Where did it go?

**10.8** *(LO 5)* An astronaut holds a spinning bicycle wheel ($I = 0.50 \text{ kg·m}^2$, $\omega = 30 \text{ rad/s}$). She inverts it $180°$. The astronaut has $I_{\text{body}} = 4.0 \text{ kg·m}^2$ about the same axis. What angular velocity does she acquire?

### Synthesis

**10.9** *(LO 1, 2, 3, 4)* A car wheel ($20 \text{ kg}$, $0.30 \text{ m}$ radius) spins up as the car goes from $0$ to $25 \text{ m/s}$ in $8 \text{ s}$, no slipping. (a) Angular acceleration. (b) Angular displacement during acceleration. (c) Moment of inertia (treat as solid disk). (d) Torque on the wheel.

**10.10** *(LO 2, 4, 5)* A solid disk ($0.50 \text{ kg}$, $0.20 \text{ m}$ radius) falls from a string wound around its rim (Maxwell's wheel). (a) Linear acceleration of its center. (b) After falling $1.0 \text{ m}$, translational and rotational KE.

**10.11** *(LO 5)* A neutron star ($1.4$ solar masses, $10 \text{ km}$ radius) spins at $30 \text{ Hz}$. (a) Angular momentum (uniform sphere). (b) Original rotation period if the progenitor had radius $7 \times 10^8 \text{ m}$ and angular momentum was conserved.

### Challenge

**10.12** *(beyond chapter)* A skater with $I = 5 \text{ kg·m}^2$ at $2 \text{ rev/s}$ pulls in to $I = 1 \text{ kg·m}^2$. (a) New angular velocity. (b) KE before and after. (c) Work done. (d) Show work equals KE increase.

**10.13** *(beyond chapter)* A gyroscope wheel ($I = 0.10 \text{ kg·m}^2$, $\omega = 200 \text{ rad/s}$, weight $2.0 \text{ kg}$) is mounted with its axle horizontal, supported only at one end $0.20 \text{ m}$ from the center. Compute the precession rate $\Omega = MgL/(I\omega)$ in rad/s and in RPM.

---

## LLM Exercise — Chapter 10: Rotational Motion in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A rotational analysis of one rotating element of your anchor phenomenon, with $I$, $\omega$, $L$, and $KE_{\text{rot}}$ computed.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 10, I want to apply rotational dynamics — moment of inertia, angular acceleration, angular momentum — to one rotating element of my phenomenon. Please:

1. Identify ONE rotating component in my phenomenon. Examples:
   - Bike commute: the wheel rotation, which has moment of inertia and angular momentum.
   - Coffee maker: a centrifugal pump impeller; a rotating burr grinder.
   - Basketball: the ball's spin during the shot (back-spin or side-spin).
   - Marathon: a runner's swinging arms (modeled as rotating rods).
   - Espresso: a rotating tamper or a spinning piston in the pump.

2. Compute the moment of inertia I using the appropriate formula for the shape (disk, hoop, sphere, rod). State the formula.

3. Compute the angular velocity ω from the linear velocity (using v = rω) or from RPM data.

4. Compute the angular momentum L = Iω and the rotational kinetic energy KE_rot = ½Iω².

5. If a torque is involved (acceleration), compute it from τ = Iα.

6. Sanity-check with one Fermi estimate.

7. Identify which assumption (rigid body, no slip, axis through center) is most likely to bite.

8. One sentence on how this connects to Chapter 11 (fluid statics) — fluids don't rotate as rigid bodies, so the moment-of-inertia framework needs modification.

Save the output as logbook/chapter-10-rotation.md.
```

### What this produces

A tenth Logbook entry: a rotational-dynamics analysis applied to your phenomenon, often surprising in how much energy is "locked up" in rotation.

### How to adapt this prompt

- *For phenomena with no obvious rotation* (a vertical pour): treat the curl/vortex of any flowing fluid as quasi-rotational; or examine an oscillating system as rotational about its pivot.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have video of a spinning object, paste frame-time data and let Claude compute angular velocity from frame analysis.

### Connection to previous chapters

Builds directly on Chapter 6 (uniform circular motion). Adds angular acceleration and dynamics. Generalizes Chapters 4 (force), 7 (KE), 8 (momentum) to rotational form.

### Preview of next chapter

Chapter 11 begins fluids — both static and flowing. Fluids can't be treated as rigid bodies; they deform under any shear. But the energy and momentum frameworks carry over.

---

**Tags:** rotation, angular-momentum, moment-of-inertia, conservation, torque
