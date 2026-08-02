# Differentiation in Motion: Vector-Valued and Parametric Functions

*The derivative scales up without a new idea: a vector function is several functions stacked, so you differentiate each one.*

---

## The cold open: the apex of the throw, and the impossible turn

Throw a ball. At the very top of its arc, what is its velocity?

Most people, asked this, say zero — the ball has stopped rising, it is momentarily at rest, surely it is not moving. That answer is half right and therefore wrong. The *vertical* part of the velocity is indeed zero at the top; that is what "top" means. But the ball is still sailing sideways at whatever horizontal speed it had when it left your hand. Its velocity at the apex is not zero — it points purely horizontally. The mistake comes from treating velocity as a single number when it is really two numbers that change independently, and nothing exposes that independence as cleanly as calculus.

Now a second scene from the source chapter. A fighter jet at 134 m/s pulls a tight turn. The pilot feels crushed into the seat — at an 8-g turn, eight times their own weight pressing sideways. The jet's *speed* is constant the whole way around; the speedometer never moves. Yet the pilot is being violently accelerated. How can there be acceleration when the speed does not change? "Constant speed means no acceleration" is the twin of the apex error, and the same tool kills both: the derivative of a vector. This chapter takes the derivative we built for a single quantity and lets it act on motion in two and three dimensions — where the answers to both puzzles fall straight out of the math.

---

## The tool, named: the vector-valued function and its derivative

A particle moving through space has a position that is a vector changing in time — a **vector-valued function**:

$$\vec{r}(t) = x(t)\,\hat{i} + y(t)\,\hat{j} + z(t)\,\hat{k},$$

where $\hat{i}, \hat{j}, \hat{k}$ are the fixed unit vectors along the three axes, and $x(t), y(t), z(t)$ are ordinary scalar functions — the **components**. Writing position this way is the same as describing a curve **parametrically**: as the parameter $t$ runs, the tip of $\vec{r}(t)$ traces the path through space, one point per instant.

The central fact of this chapter is short. To differentiate a vector-valued function, **differentiate each component**:

$$\vec{v}(t) = \frac{d\vec{r}}{dt} = \frac{dx}{dt}\,\hat{i} + \frac{dy}{dt}\,\hat{j} + \frac{dz}{dt}\,\hat{k} = v_x\,\hat{i} + v_y\,\hat{j} + v_z\,\hat{k}.$$

That is the whole tool. No new limit, no new theory — just the single-variable derivative of Chapter 6, applied three times in parallel.

---

## Development: why componentwise differentiation is legitimate

This is not a definition pulled from a hat; it follows from the derivative we already have. The derivative of $\vec{r}$ is, by definition, the limit of a difference quotient — but now the thing in the numerator is a *vector* difference:

$$\frac{d\vec{r}}{dt} = \lim_{\Delta t \to 0} \frac{\vec{r}(t + \Delta t) - \vec{r}(t)}{\Delta t}.$$

Vectors subtract component by component, and a vector divided by a scalar scales each component. The unit vectors $\hat{i}, \hat{j}, \hat{k}$ are *constant* — they do not change with $t$ — so they ride along untouched through the limit. Writing it out:

$$\frac{\vec{r}(t+\Delta t) - \vec{r}(t)}{\Delta t} = \frac{x(t+\Delta t)-x(t)}{\Delta t}\,\hat{i} + \frac{y(t+\Delta t)-y(t)}{\Delta t}\,\hat{j} + \frac{z(t+\Delta t)-z(t)}{\Delta t}\,\hat{k}.$$

Taking $\Delta t \to 0$, each bracketed difference quotient becomes the ordinary derivative of its component. The limit of a vector is the vector of the limits. So differentiating a vector function reduces to three independent single-variable problems — and that *independence* is the resolution of both cold-open puzzles. The rate of change of $x$ is computed from $x(t)$ alone; it knows nothing of what $y$ is doing. Differentiating again gives the **acceleration vector** the same way:

$$\vec{a}(t) = \frac{d\vec{v}}{dt} = a_x\,\hat{i} + a_y\,\hat{j} + a_z\,\hat{k}.$$

---

## Development: the independence of perpendicular motions

A projectile under gravity alone has acceleration only downward: $a_x = 0$, $a_y = -g$. Launched from the origin at speed $v_0$ and angle $\theta_0$, its position is the parametric pair

$$x(t) = (v_0\cos\theta_0)\,t, \qquad y(t) = (v_0\sin\theta_0)\,t - \tfrac{1}{2}g t^2.$$

Differentiate each component independently:

$$v_x(t) = \frac{dx}{dt} = v_0\cos\theta_0, \qquad v_y(t) = \frac{dy}{dt} = v_0\sin\theta_0 - g t.$$

Read what the math says. The horizontal velocity $v_x$ is a *constant* — it contains no $t$, because the $x$-equation contained no acceleration. Gravity appears only in the $y$-component and cannot reach across to touch $v_x$. This is not a modeling convenience; it is a theorem about the derivative. The $y$-equation cannot influence $dx/dt$ because $dx/dt$ is computed from $x(t)$ alone.

So at the apex, where $v_y = 0$ (set $v_0\sin\theta_0 - g t = 0$), the horizontal velocity is *still* $v_0\cos\theta_0 \neq 0$. The ball is moving purely horizontally, not at rest. The "velocity is zero at the top" error is the failure to see the two components as independent; differentiating componentwise *proves* they are. A ball dropped from a moving train and a ball thrown from it hit the floor at the same time, for the same reason: the vertical motion does not consult the horizontal.

![A parabolic projectile trajectory with velocity arrows at launch, apex, and descent, each resolved into a constant horizontal component vₓ and a varying vertical component v_y; at the apex the velocity arrow is purely horizontal.](images/07-differentiation-in-motion-fig-01.png)
*Figure 7.1 — Componentwise differentiation makes the independence of horizontal and vertical motion a theorem: at the apex v_y = 0 but vₓ ≠ 0.*

---

## Development: centripetal acceleration by differentiating a rotating vector

Now the marquee derivation — the jet's impossible turn, made possible. Consider a particle in uniform circular motion: constant radius $r$, constant angular rate $\omega$ (radians per second). Its angle at time $t$ is $\theta = \omega t$, so its position is

$$\vec{r}(t) = r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}.$$

**Differentiate once for velocity.** Each component needs the chain rule — the inner function is $\omega t$, contributing a factor $\omega$ (exactly the factor we drilled in Chapter 6):

$$\vec{v}(t) = \frac{d\vec{r}}{dt} = -r\omega\sin(\omega t)\,\hat{i} + r\omega\cos(\omega t)\,\hat{j}.$$

The *speed* is the magnitude of this vector:

$$|\vec{v}| = \sqrt{(r\omega)^2\sin^2(\omega t) + (r\omega)^2\cos^2(\omega t)} = r\omega\sqrt{\sin^2 + \cos^2} = r\omega.$$

Using $\sin^2 + \cos^2 = 1$, the speed is the constant $r\omega$ — the speed never changes, just as the jet's speedometer says. But the velocity *vector* is not constant: its direction rotates, always staying perpendicular to $\vec{r}$ (tangent to the circle). Constant magnitude, changing direction — that is the whole secret. A changing vector has a nonzero derivative even when its length is fixed.

**Differentiate again for acceleration.** Apply the chain rule once more:

$$\vec{a}(t) = \frac{d\vec{v}}{dt} = -r\omega^2\cos(\omega t)\,\hat{i} - r\omega^2\sin(\omega t)\,\hat{j}.$$

Factor out $-\omega^2$ and look at what remains:

$$\vec{a}(t) = -\omega^2\left[r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}\right] = -\omega^2\,\vec{r}(t).$$

The acceleration is $-\omega^2$ times the position vector. The minus sign means it points *opposite* to $\vec{r}$ — straight back toward the center. Its magnitude is

$$a_c = \omega^2 r,$$

and since $v = r\omega$ gives $\omega = v/r$,

$$\boxed{\,a_c = \frac{v^2}{r}\,.}$$

There it is. The famous $v^2/r$ is not a formula to memorize — it falls out of differentiating a rotating unit vector twice. The acceleration is nonzero even though the speed is constant, because acceleration is the derivative of the *velocity vector*, and that vector is turning.

![A circle with the position vector r to the particle, the velocity v tangent and perpendicular to r with constant magnitude rω, and the acceleration a = −ω²r pointing back to the center; a panel shows the two differentiations giving the boxed a_c = v²/r.](images/07-differentiation-in-motion-fig-02.png)
*Figure 7.2 — Differentiating a rotating vector twice yields acceleration pointing at the center: a_c = v²/r, nonzero even at constant speed.* The pilot in the 8-g turn is being accelerated toward the center of the circle at $8g$; the speed never changes, but the direction does, and the derivative sees the direction.

A caution the source chapter flags: this center-seeking $a_c = r\omega^2$ is a different quantity from the *angular* acceleration $\alpha = d\omega/dt$. Here $\omega$ is constant, so $\alpha = 0$ — yet $a_c \neq 0$. Do not confuse the acceleration that turns you (centripetal, present even at steady spin) with the one that speeds the spin up (angular, present only when $\omega$ changes).

---

## Development: related rates — differentiating a constraint

Sometimes two quantities are tied together by a geometric relation, and you want to relate their *rates*. The move is to differentiate the relation with respect to time, treating each varying quantity as a function of $t$ (this is the chain rule again, applied implicitly).

Suppose two coordinates of a point obey $x^2 + y^2 = s^2$, where $s$ is a distance you care about. Differentiate both sides with respect to $t$:

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 2s\frac{ds}{dt}, \qquad\Longrightarrow\qquad \frac{ds}{dt} = \frac{x\,\dot{x} + y\,\dot{y}}{s}.$$

Knowing where the point is and how fast each coordinate changes, you get the rate of change of the distance. The discipline that makes related rates work — and the discipline this whole book preaches — is **differentiate the symbolic relation first, substitute numbers last.** Plug in numbers before differentiating and you freeze the very quantities whose rates you were trying to find.

---

## Worked examples

### Example 1 — The jet's turn radius

A jet flies at $v = 134\ \text{m/s}$. What radius produces a centripetal acceleration of $1\,g = 9.8\ \text{m/s}^2$ on the pilot? From $a_c = v^2/r$,

$$r = \frac{v^2}{a_c} = \frac{(134)^2}{9.8} = \frac{17{,}956}{9.8} \approx 1{,}833\ \text{m}.$$

For an 8-g turn the allowed acceleration is $78.4\ \text{m/s}^2$, so

$$r = \frac{17{,}956}{78.4} \approx 229\ \text{m}.$$

A tighter turn demands a far larger acceleration — and the acceleration came from differentiating the position vector twice, not from a memorized rule.

### Example 2 — Velocity vector of a satellite, componentwise

A particle has parametric position $\vec{r}(t) = (5.0t + 2.0)\,\hat{i} + 3.0t^2\,\hat{j}$ (meters). Differentiate each component:

$$\vec{v}(t) = 5.0\,\hat{i} + 6.0t\,\hat{j}, \qquad \vec{a}(t) = 0\,\hat{i} + 6.0\,\hat{j}.$$

At $t = 1.0\ \text{s}$, $\vec{v} = 5.0\,\hat{i} + 6.0\,\hat{j}$ (m/s). The acceleration is the constant $6.0\,\hat{j}$ — purely in $y$, untouched by the $x$-motion. The two directions evolve on their own; that is the independence theorem in a single line of arithmetic.

### Example 3 — Closing speed of two cars (related rates)

Car A travels east at $20\ \text{m/s}$, car B north at $15\ \text{m/s}$, both toward one intersection. At the moment A is $40\ \text{m}$ west of it and B is $30\ \text{m}$ south, how fast is the distance between them shrinking? Put A at $(-x_A, 0)$ and B at $(0, -y_B)$ with $\dot{x}_A = -20$, $\dot{y}_B = -15$ (distances decreasing). The separation is $s^2 = x_A^2 + y_B^2$. Differentiate:

$$\frac{ds}{dt} = \frac{x_A\dot{x}_A + y_B\dot{y}_B}{s} = \frac{(40)(-20) + (30)(-15)}{\sqrt{40^2 + 30^2}} = \frac{-800 - 450}{50} = -25\ \text{m/s}.$$

They are approaching at $25\ \text{m/s}$. Notice the method: differentiate the constraint symbolically, *then* put in the numbers.

---

## Return to the cold open

Both puzzles dissolve. At the apex of the thrown ball, we differentiated the parametric position componentwise and found $v_x = v_0\cos\theta_0$, a constant that the vertical motion cannot touch; the velocity at the top is horizontal, not zero. The error was treating velocity as one number instead of two independent components — and componentwise differentiation made the independence a theorem, not an opinion. For the jet, we wrote the position as a rotating vector, differentiated it twice with the chain rule, and watched $a_c = v^2/r$ appear pointing at the center. The speed was constant the whole time; the acceleration was not, because acceleration is the derivative of the velocity *vector*, and a vector of fixed length that keeps turning has a perfectly real rate of change. The derivative did not need a new idea to handle motion in a plane — it only needed to act on each component at once.

---

## Where it generalizes

"Differentiate each component" is one of the most portable moves in applied mathematics, because *anything* described by several coordinates changing together submits to it unchanged. A robot arm's end-effector velocity, the current vector in a three-phase circuit, the rate of change of a force field along a particle's path, the velocity of a point in a computer-graphics animation — all are componentwise derivatives of vector-valued functions. Related rates is the same tool wearing different clothes: differentiate a constraint and read off how coupled quantities co-vary, whether the constraint is geometric, economic, or chemical. What the math will not do is choose the parametrization. A solver differentiates $\vec{r}(t)$ instantly — but only after a human decided to write position as a function of time at all, chose components like $(\cos\omega t, \sin\omega t)$ that *encode* "rotating at constant rate," and recognized that a second derivative pointing along $-\vec{r}$ *means* "toward the center." In related rates, the engine differentiates the constraint, but you must *find* the constraint and decide which rate is given and which is sought. The calculus is mechanical once the motion is modeled; the modeling is the irreducibly human step.

---

## Exercises

1. **(Componentwise.)** A particle has $\vec{r}(t) = (3t^2)\,\hat{i} + (4t - t^3)\,\hat{j}$ (meters). Find $\vec{v}(t)$ and $\vec{a}(t)$. Is the acceleration constant? At what time, if any, is $v_x = 0$?

2. **(Apex misconception.)** A projectile is launched at $30\ \text{m/s}$, $40^\circ$ above horizontal. Find $v_x$ and $v_y$ as functions of $t$. At the apex, give the full velocity vector (magnitude and direction) and state in one sentence why it is not zero.

3. **(Speed vs. velocity.)** For uniform circular motion $\vec{r}(t) = r\cos(\omega t)\hat{i} + r\sin(\omega t)\hat{j}$, show that $\vec{v}\cdot\vec{r} = 0$ at every instant. Interpret this geometrically — what does it say about the direction of the velocity relative to the radius?

4. **(Related rates.)** A ladder $5\ \text{m}$ long leans against a wall; its base slides away from the wall at $0.4\ \text{m/s}$. When the base is $3\ \text{m}$ from the wall, how fast is the top sliding down? Set up the constraint, differentiate symbolically, then substitute.

5. **(Derivation.)** Starting from $\vec{r}(t) = r\cos(\omega t)\,\hat{i} + r\sin(\omega t)\,\hat{j}$ with $r, \omega$ constant, derive the centripetal acceleration. Differentiate twice using the chain rule, show that $\vec{a} = -\omega^2\vec{r}$, and conclude $a_c = v^2/r$. At each differentiation, identify where the factor $\omega$ enters and why dropping it would be an error.

---

## Sources

- Isaac Newton, *Philosophiæ Naturalis Principia Mathematica* (1687), Book I — the geometric analysis of circular and centripetal motion; the coinage "centripetal." [verified — see factchecks/07-differentiation-in-motion-assertions.md] (original primary source)
- Christiaan Huygens, *De vi centrifuga* (written 1659, pub. 1703) and *Horologium Oscillatorium* (1673) — the $v^2/r$ result for circular motion by a geometric limiting argument. [verified — Huygens dates/works confirmed; the Huygens/Newton priority is debated, see factchecks/07-differentiation-in-motion-assertions.md and pantry] (original primary sources)
- J. W. Gibbs & E. B. Wilson, *Vector Analysis* (1901) — the $\hat{i}, \hat{j}, \hat{k}$ notation and componentwise differentiation of vector functions. [verified — Gibbs/Wilson standardized/popularized the notation (î,ĵ,k̂ originate with Hamilton); see factchecks/07-differentiation-in-motion-assertions.md] (original primary source)
- Leonhard Euler, *Mechanica* (1736) — recasting mechanics in analytic/component form. [verified — see factchecks/07-differentiation-in-motion-assertions.md] (original primary source)
- Source chapter (this book's archive): "Motion in Two and Three Dimensions" — the projectile parametrization, the jet barrel-roll numbers, the rotating-vector derivation of $a_c$, and the relative-motion/closing-speed problems; "Fixed-Axis Rotation" — the distinction between centripetal and angular acceleration.
- The independence-of-perpendicular-components misconception is documented in physics-education research (Halloun & Hestenes lineage). [verified — see factchecks/07-differentiation-in-motion-assertions.md]
