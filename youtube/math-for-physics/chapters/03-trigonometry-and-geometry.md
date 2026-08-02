# Trigonometry and Geometry

*Turning an angle into lengths — and the small-angle behavior that calculus and oscillation will need.*

## Cold open: a block on a ramp, and a force pointing the wrong way

A block sits on a ramp tilted at angle $\theta$. Gravity pulls it straight down with force $mg$. But the block cannot move straight down — the ramp is in the way. It can only slide *along* the slope, or press *into* the surface. So the single downward force $mg$ has to be split into two pieces: one component down the slope (which tries to slide the block) and one perpendicular to the slope (which the surface pushes back against). The whole problem turns on a question that trips up a startling number of students: *which piece gets the sine, and which gets the cosine?*

You cannot solve a single force-on-an-incline problem, a single projectile, a single tension in an angled rope, without answering that question — and answering it not by memorizing "SOH-CAH-TOA" but by understanding what a sine and a cosine actually *are*. This chapter builds trigonometry as the mathematics of turning an angle into lengths, and ends with a preview of the most useful approximation in all of physics: that for small angles, $\sin\theta \approx \theta$.

## The tool, named

**Trigonometry** is the mathematics that relates an angle to lengths. Its core objects are the three functions sine, cosine, and tangent, understood through two complementary pictures:

1. **The right triangle** — for an acute angle $\theta$ in a right triangle, $\sin\theta$, $\cos\theta$, and $\tan\theta$ are ratios of side lengths.
2. **The unit circle** — for *any* angle, $\cos\theta$ and $\sin\theta$ are the coordinates of a point on a circle of radius 1, which extends the functions beyond $90°$ and makes their periodicity visible.

Alongside these come the **radian** — the natural, dimensionless measure of angle as arc-length-per-radius — and the **laws of sines and cosines** for triangles that are not right-angled. The historical thread is global: Hipparchus and Ptolemy tabulated *chords*; the Indian mathematician Āryabhaṭa (499 CE) replaced the chord with the *half-chord*, which is our sine. (The word "sine" is a chain of translation accidents: Sanskrit *jyā* → Arabic *jiba* → misread as *jaib*, "fold/bosom" → Latin *sinus*.)

## Development and derivation

### The right triangle and the three ratios

Take a right triangle with an acute angle $\theta$. Label the sides relative to $\theta$: the **hypotenuse** (opposite the right angle), the side **opposite** $\theta$, and the side **adjacent** to $\theta$. The three functions are defined as ratios:

$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}, \qquad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}, \qquad \tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{\sin\theta}{\cos\theta}.$$

Because these are ratios of lengths, they are *pure numbers* — dimensionless. And because all right triangles with the same angle $\theta$ are similar (their sides are proportional), the ratios depend only on $\theta$, not on the triangle's size. That is the whole reason trigonometry works: an angle determines the *shape* of the triangle, hence its side ratios, regardless of scale.

### Components from magnitude and angle: the central derivation

Here is the move the cold open demands. A vector (a force, a velocity) has a magnitude $F$ and points at angle $\theta$ measured from a chosen axis. We want its components along and perpendicular to that axis. Drop a perpendicular from the vector's tip to the axis; this builds a right triangle in which the vector is the hypotenuse (length $F$), the along-axis component is the *adjacent* side, and the perpendicular component is the *opposite* side. By the definitions above:

$$F_{\text{along}} = F\cos\theta \quad(\text{adjacent}), \qquad F_{\perp} = F\sin\theta \quad(\text{opposite}).$$

So **the component along the direction you measure the angle from carries the cosine; the component perpendicular to it carries the sine.** That rule — read off the triangle, not memorized as a chant — settles every "is it sine or cosine?" question. The reference matters: if you measure the angle from the *other* axis, the roles of sine and cosine swap, precisely because the "adjacent" and "opposite" sides have swapped.

A built-in check: the components must rebuild the original magnitude by the Pythagorean theorem.

$$F_{\text{along}}^2 + F_{\perp}^2 = F^2\cos^2\theta + F^2\sin^2\theta = F^2(\cos^2\theta + \sin^2\theta) = F^2,$$

using the **Pythagorean identity** $\cos^2\theta + \sin^2\theta = 1$, which is just the Pythagorean theorem applied to the unit circle. The decomposition loses nothing; it only re-expresses the vector along chosen axes.

### The unit circle and the radian

The right-triangle picture caps angles at $90°$ — you cannot have an "opposite side" for a $120°$ angle in a right triangle. The unit circle removes the cap. Place a circle of radius 1 at the origin. For an angle $\theta$ measured counterclockwise from the positive $x$-axis, define the point on the circle to be at coordinates

$$(\cos\theta,\ \sin\theta).$$

For acute $\theta$ this agrees exactly with the triangle definitions (hypotenuse $=1$). But now $\theta$ can be anything: at $\theta = 90°$ the point is $(0,1)$, so $\cos 90° = 0$ and $\sin 90° = 1$; at $\theta = 180°$ it is $(-1,0)$; and as $\theta$ keeps increasing the point cycles around, which is *why* sine and cosine are periodic with period one full turn.

![Unit circle of radius 1 with a point at angle θ from the +x axis located at (cosθ, sinθ); the horizontal leg is cosθ, the vertical leg is sinθ, and the arc length equals θ in radians.](images/03-trigonometry-and-geometry-fig-01.png)
*Figure 3.1 — Cosine and sine are the coordinates of a point on the unit circle, extending the right-triangle ratios to any angle.* The unit circle is the natural home of the trig functions — and, as you will see in Chapter 12, it is literally the picture behind oscillation and the complex exponential.

This also forces the right way to *measure* an angle. The **radian** measures an angle by the length of arc it cuts on a unit circle: an angle of one radian subtends an arc equal to the radius. A full circle has circumference $2\pi r$, so a full turn is $2\pi$ radians; $180° = \pi$ radians; one radian is about $57.3°$. The radian is dimensionless (it is a length divided by a length), and it is *not just another unit to convert to* — it is the measure that makes the calculus of trig functions clean. This is not a convention but a mathematical fact: the derivative formulas $\frac{d}{d\theta}\sin\theta = \cos\theta$ and $\frac{d}{d\theta}\cos\theta = -\sin\theta$ hold *only* when $\theta$ is in radians. A 2025 multinational survey found that only about a quarter of college students recognized this; roughly 71% wrongly believed any unit works `[verify — arXiv:2503.01525]`. A student who differentiates $\sin(\text{degrees})$ as if the rule still applied will get every oscillation problem wrong. The radian earns its place in Chapter 6.

### The laws of sines and cosines

Not every triangle has a right angle, and angled-rope and force-triangle problems often do not. For a general triangle with sides $a, b, c$ opposite angles $A, B, C$:

$$\textbf{Law of sines:}\quad \frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C},$$

$$\textbf{Law of cosines:}\quad c^2 = a^2 + b^2 - 2ab\cos C.$$

The law of cosines is the Pythagorean theorem with a correction term: when $C = 90°$, $\cos C = 0$ and it collapses to $c^2 = a^2 + b^2$. These let you solve a triangle — and therefore add or resolve vectors arranged head-to-tail — without first decomposing into perpendicular components.

### The small-angle approximation: a preview

Here is the result that makes the rest of the book possible. For small angles measured *in radians*,

$$\sin\theta \approx \theta, \qquad \tan\theta \approx \theta, \qquad \cos\theta \approx 1 - \tfrac{1}{2}\theta^2.$$

You can *see* the first one on the unit circle: for a small angle, the arc length (which is $\theta$, by the definition of the radian) and the vertical drop (which is $\sin\theta$) become nearly the same short segment. As $\theta$ shrinks, the arc and the chord and the sine all converge. Made precise, this is the statement

$$\lim_{\theta\to 0}\frac{\sin\theta}{\theta} = 1 \quad(\theta \text{ in radians}),$$

a limit first made explicit by Cotes and put on rigorous footing by Cauchy. <!-- FACT-CHECK FLAG: UNVERIFIED — Cauchy (1821) rigorous-limit attribution is standard; the specific "first made explicit by Cotes" claim for lim sinθ/θ could not be corroborated. See factchecks/03-trigonometry-and-geometry-assertions.md --> The Indian mathematician Mādhava (c. 1400) found the full power series for sine and cosine — $\sin\theta = \theta - \theta^3/6 + \cdots$ — roughly 250 years before Newton and Leibniz; the small-angle forms are just its leading terms. We will derive that series properly in Chapter 13. For now, hold onto the picture: *for small angles, the sine is the angle.*

![A zoomed unit-circle wedge where the arc length θ and the vertical drop sinθ nearly coincide, beside a plot of y=θ (line) and y=sinθ (curve) hugging near the origin and diverging past about half a radian.](images/03-trigonometry-and-geometry-fig-03.png)
*Figure 3.3 — As θ shrinks, the arc, the chord, and sinθ converge: sinθ ≈ θ in radians, the linearization that makes oscillation solvable.*

## Worked examples

### Example 1 — Resolving weight on an incline

Return to the cold open. The block's weight $mg$ points straight down; the incline is tilted at angle $\theta$. Choose axes *along* the slope and *perpendicular* to it. The geometry (a short exercise in similar triangles) shows that the angle between the weight vector and the *perpendicular*-to-slope axis equals $\theta$. So, reading off the triangle with the angle measured from the perpendicular axis:

$$\text{component into the surface} = mg\cos\theta, \qquad \text{component down the slope} = mg\sin\theta.$$

The *down-slope* (driving) component carries the sine; the *into-surface* (normal) component carries the cosine. Sanity check the extremes: at $\theta = 0$ (flat ground) the down-slope component is $mg\sin 0 = 0$ — nothing drives the block, correct — and the into-surface component is $mg\cos 0 = mg$, the full weight, correct. At $\theta = 90°$ (vertical wall) the down-slope component is $mg$ (free fall along the wall) and the normal component is zero. The limits confirm the assignment.

![A block on a ramp at angle θ with the weight mg resolved into a down-slope component mg sinθ and an into-surface component mg cosθ; an inset checks the flat and vertical limits.](images/03-trigonometry-and-geometry-fig-02.png)
*Figure 3.2 — Build the right triangle and read the ratios: the driving component carries the sine, the normal component the cosine.*

### Example 2 — Projectile range and why 45° is best

Launch a projectile at speed $v_0$ and angle $\theta$ above the horizontal. The initial velocity splits into a horizontal component $v_0\cos\theta$ (constant, no horizontal force) and a vertical component $v_0\sin\theta$ (decelerated by gravity). Working through the kinematics (Chapter 7 does this with calculus; here we quote the result), the range on level ground is

$$R = \frac{v_0^2 \sin 2\theta}{g},$$

using the double-angle identity $2\sin\theta\cos\theta = \sin 2\theta$. Read it: $R$ is largest when $\sin 2\theta = 1$, i.e. $2\theta = 90°$, i.e. $\theta = 45°$. And because $\sin 2\theta$ is symmetric about $90°$, complementary angles give *equal* range: $30°$ and $60°$ land at the same spot. The trigonometry hands you both the optimum and the symmetry.

### Example 3 — A force triangle with the law of sines

A weight hangs from two ropes meeting at a knot at known angles; the three forces (two tensions and the weight) must sum to zero, so drawn head-to-tail they form a closed triangle. The interior angles of that force triangle are set by the rope angles, and the law of sines relates each tension to the angle opposite it:

$$\frac{T_1}{\sin\alpha_1} = \frac{T_2}{\sin\alpha_2} = \frac{w}{\sin\alpha_w}.$$

This lets you read off the tensions directly from the geometry — and it makes a fact visible at a glance: *the rope more nearly opposite the weight (largest opposite angle) carries the most tension.* The same insight emerged in Chapter 2's component approach; here the triangle shows it geometrically.

## Return to the cold open

The block on the ramp is solved the moment you build the right triangle. The weight $mg$ is the hypotenuse; the component pressing into the surface (adjacent to $\theta$, measured from the surface normal) is $mg\cos\theta$; the component sliding it down the slope (opposite) is $mg\sin\theta$. "Which gets the sine?" is answered not by a mnemonic but by *drawing the triangle and reading the ratios* — and confirmed by checking that the components rebuild $mg$ via $\cos^2\theta + \sin^2\theta = 1$, and that they behave correctly as the ramp flattens or stands vertical. The student who memorized SOH-CAH-TOA can sometimes get the right answer; the student who can build and read the triangle can never get it wrong, and can handle the case where the angle is measured from the other axis without panic.

## Where it generalizes

Decomposition — projecting a quantity onto chosen axes via the cosine of the included angle — is one of the most transferable moves in applied mathematics. It is the dot product of Chapter 4 in disguise. It is how a signal is split into frequency components in Chapter 14's Fourier analysis. The unit circle reappears as the home of the complex exponential in Chapter 12, where $e^{i\theta} = \cos\theta + i\sin\theta$ makes the circle and the oscillation literally the same object. And the small-angle approximation, $\sin\theta\approx\theta$, is the hinge of the entire theory of oscillation: it is what turns the genuinely hard nonlinear pendulum equation into the solvable simple-harmonic-motion equation of Chapter 11. "Linearize near equilibrium" — replace a function by its tangent line for small displacements — is a move you will make again and again, in mechanics, circuits, control theory, and economics. A solver computes $\sin 37°$ instantly; what it will not do is *choose your axes*, *decide which component does the work*, or *know that your answer is nonsense if you fed it degrees where the calculus wanted radians.* That judgment is yours.

## Exercises

1. **(Decompose)** A force of 50 N points at $35°$ above the horizontal. Find its horizontal and vertical components, and verify they rebuild 50 N via the Pythagorean identity.

2. **(Sine or cosine)** A block sits on an incline at angle $\theta$. Without looking back at the text, draw the triangle and determine which weight component is $mg\sin\theta$ and which is $mg\cos\theta$. Justify by checking the $\theta\to 0$ limit.

3. **(Radians)** Convert $30°$, $45°$, and $90°$ to radians. Then explain, in one sentence, why $\frac{d}{d\theta}\sin\theta = \cos\theta$ fails if $\theta$ is in degrees. (Hint: think about $\lim_{\theta\to 0}\sin\theta/\theta$ in each measure.)

4. **(Derivation)** Using the small-angle approximations, show that for a pendulum the restoring "force ratio" $\sin\theta$ may be replaced by $\theta$ for small swings, and state in words why this is the step that makes the pendulum solvable. (You will complete the solution in Chapter 11.)

5. **(Law of cosines)** Two forces of 6 N and 8 N act at a $60°$ angle to each other. Use the law of cosines to find the magnitude of their resultant. (Hint: the resultant closes a triangle; mind which angle goes into the formula.)

## Sources

- Ptolemy, *Almagest* (c. 150 CE), table of chords; building on Hipparchus of Nicaea (c. 150 BCE).
- Āryabhaṭa, *Āryabhaṭīya* (499 CE) — first sine table; the *jyā → jiba → jaib → sinus* etymology (standard histories of mathematics).
- Mādhava of Sangamagrāma and the Kerala school; *Yuktibhāṣā* (c. 1400) — power series for sine and cosine.
- Roger Cotes (early 18th c.) and A.-L. Cauchy (1821) on $\lim_{\theta\to0}\sin\theta/\theta = 1$.
- Multinational PER study, "Students' difficulties distinguishing between radians and degrees," arXiv:2503.01525 (2025). `[verify]`
