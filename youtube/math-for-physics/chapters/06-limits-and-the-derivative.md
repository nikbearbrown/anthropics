# Limits and the Derivative

*How fast is it going* right now*? — the limit of a ratio of vanishing changes.*

---

## The cold open: the speedometer paradox

Felix Baumgartner is falling. His altitude, ignoring the thin air at the top of his jump, is the parabola we met in the last chapter:

$$y(t) = y_0 - \tfrac{1}{2} g t^2, \qquad g = 9.8\ \text{m/s}^2.$$

We can answer easy questions immediately. *How fast was he going on average over the first 30 seconds?* Average velocity is displacement over time, $\Delta y / \Delta t$ — a slope between two points on the curve, and the parabola hands us the two heights. But mission control wanted something harder. *How fast is he going at the instant the clock reads exactly 30 seconds?* Not averaged over an interval — *at that instant*.

This is the speedometer paradox, and it is genuinely strange. Velocity is displacement divided by elapsed time. But at a single instant, no time elapses and the object does not move: displacement is zero, elapsed time is zero, and the ratio is $0/0$, which is nonsense. Yet the speedometer in your car displays a definite number at every instant. Something is being computed. The whole of differential calculus exists to make sense of that number — to extract a meaningful ratio from two quantities that are both racing toward zero. The tool that does it is the **derivative**, and the idea that makes the derivative honest is the **limit**.

---

## The tool, named: the derivative

The **average velocity** of an object over a time interval is the change in position divided by the change in time:

$$\bar{v} = \frac{x(t + \Delta t) - x(t)}{\Delta t}.$$

The expression on the right is called the **difference quotient**: a change in output over a change in input. Geometrically it is the slope of the **secant line** — the straight line through the two points $(t, x(t))$ and $(t+\Delta t,\, x(t+\Delta t))$ on the graph.

The **instantaneous velocity** is what the average velocity approaches as we shrink the interval $\Delta t$ toward zero — as the second point slides down the curve toward the first, and the secant line tilts toward the **tangent line** that just grazes the curve at $t$. We write this as a **limit**:

$$v(t) = \lim_{\Delta t \to 0} \frac{x(t + \Delta t) - x(t)}{\Delta t} = \frac{dx}{dt}.$$

This limit, for a general function $f$, is the **derivative**:

$$f'(x) = \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.$$

The derivative is the instantaneous rate of change of $f$, and geometrically it is the slope of the tangent line to the graph at $x$. The two notations — Newton's $f'$ and Leibniz's $df/dx$ — name the same object.

A warning about $dx/dt$ that will save you grief later: it *looks* like a fraction, "$dx$ divided by $dt$," and in certain controlled situations (the chain rule, separable differential equations) it can be manipulated like one. But it is *defined* as a single object — a limit — not as one number divided by another. Treat it as a fraction only when a theorem licenses it; we will flag those moments when they come.

---

## Development: what a limit actually is, and why we need it

Early calculus worked spectacularly and rested on nothing. Newton spoke of "fluxions" — the rate at which a flowing quantity changes — and Leibniz of "infinitesimals," quantities smaller than any positive number yet not zero. In 1734 the philosopher George Berkeley published a devastating critique. To compute a derivative, the early calculators would divide by a small quantity $h$ (so $h \neq 0$, division is legal) and then, at the end, *set $h = 0$* to finish. But $h$ cannot be both nonzero and zero. Berkeley called these vanishing infinitesimals "the ghosts of departed quantities." The method gave right answers, but its foundation was incoherent.

The repair, worked out by Cauchy in the 1820s and made fully precise by Weierstrass, is the **limit**, and it is the reason we never actually set $h = 0$. The statement

$$\lim_{h \to 0} g(h) = L$$

does *not* mean "the value of $g$ when $h = 0$." It means: we can force $g(h)$ to be as close to $L$ as we please, by taking $h$ close enough to zero *but not equal to zero*. The function need never reach $L$, and $g$ need not even be defined at $h = 0$ — which is exactly our situation, since the difference quotient is $0/0$ at $h = 0$ and undefined there. The limit asks what value the difference quotient *approaches*, not what it *equals* at the forbidden point. That single distinction — between the value approached and the value attained — dissolves Berkeley's paradox. We do not divide by zero and we do not set $h$ to zero; we watch where the ratio is heading as $h$ shrinks, and we name that destination the derivative.

This is the most common place students stumble: the limit is the value the function *heads toward*, which may be a value it never takes. Hold that thought through the next derivation, where the difference quotient is meaningless at $h = 0$ yet has a perfectly definite limit.

![The parabola x = ½gt² with a fixed point at t and several secant lines to points at t+Δt for shrinking Δt; as Δt → 0 the secant tilts toward the tangent, and the difference quotient Δx/Δt approaches the derivative dx/dt.](images/06-limits-and-the-derivative-fig-01.png)
*Figure 6.1 — The derivative is the limit of the difference quotient: we never set Δt = 0, we watch where the ratio heads.*

---

## Development: the derivative from the limit, computed by hand

Before any rules, do it once the honest way. Take the falling-body building block $f(t) = t^2$ and compute its derivative straight from the definition.

$$f'(t) = \lim_{h \to 0} \frac{f(t+h) - f(t)}{h} = \lim_{h \to 0} \frac{(t+h)^2 - t^2}{h}.$$

Expand the square:

$$(t+h)^2 - t^2 = t^2 + 2th + h^2 - t^2 = 2th + h^2.$$

So the difference quotient is

$$\frac{2th + h^2}{h} = \frac{h(2t + h)}{h} = 2t + h.$$

That cancellation is legal precisely because $h \neq 0$ inside the limit — we are not yet at the forbidden point. Now take the limit as $h \to 0$. The term $2t$ does not involve $h$; the term $h$ heads to zero:

$$f'(t) = \lim_{h \to 0}(2t + h) = 2t.$$

The derivative of $t^2$ is $2t$. Watch what happened: at $h = 0$ exactly, the original expression was $0/0$, undefined — Berkeley's ghost. But the *limit* is a clean $2t$, because we asked where $2t + h$ was heading, not what the indeterminate form equalled. This is the entire mechanism of differentiation, performed once with nothing hidden.

---

## Development: the rules as labor-saving devices

Computing every derivative from the limit would be exhausting. The rules below are theorems — each provable from the limit definition — that let us differentiate by recognition instead. We state them and indicate where each comes from.

**The power rule.** For any constant exponent $n$,

$$\frac{d}{dx}\,x^{n} = n\,x^{\,n-1}.$$

For $n = 2$ this gives $2x$, matching the hand computation above. The general result comes from expanding $(x+h)^n$ by the binomial theorem: the leading correction term is $n x^{n-1} h$, every other term carries a higher power of $h$ and dies in the limit, and dividing by $h$ leaves $n x^{n-1}$.

**Constant multiple and sum.** Constants pass through ($\frac{d}{dx}[c\,f] = c\,f'$) and derivatives add term by term ($\frac{d}{dx}[f+g] = f' + g'$). Both follow from the limit being a linear operation.

**The product rule (Leibniz, 1684).** The derivative of a product is *not* the product of the derivatives. Instead,

$$\frac{d}{dx}\,[u\,v] = u'\,v + u\,v'.$$

Leibniz derived it by considering how a small change in $x$ changes the rectangle of sides $u$ and $v$: the area grows by a strip $v\,du$, a strip $u\,dv$, and a tiny corner $du\,dv$ that vanishes in the limit.

**The quotient rule.** For a ratio,

$$\frac{d}{dx}\!\left[\frac{u}{v}\right] = \frac{u'\,v - u\,v'}{v^{2}}.$$

**The chain rule.** This is the one whose neglect breaks the most derivations. For a composition $f(g(x))$,

$$\frac{d}{dx}\,f(g(x)) = f'(g(x))\cdot g'(x).$$

You differentiate the outer function evaluated at the inner one, then *multiply by the derivative of the inner function*. The reason is exactly the fraction-like behavior of Leibniz's notation: writing $u = g(x)$, $\frac{df}{dx} = \frac{df}{du}\cdot\frac{du}{dx}$. The factor you must not forget appears when the inside is more than a bare $x$. For example,

$$\frac{d}{dt}\,\sin(\omega t) = \cos(\omega t)\cdot \omega = \omega\cos(\omega t),$$

using the standard derivatives $\frac{d}{dx}\sin x = \cos x$ and $\frac{d}{dx}\cos x = -\sin x$ (themselves provable from the limit and the small-angle behavior of sine). Drop the factor $\omega$ and the circular-motion derivation of the next chapter collapses; we are flagging it here so you carry it forward.

---

## Development: the derivative as an object — second derivatives

A derivative is not just a number attached to a point; it is itself a new *function* — the slope at every point — which you can graph, reason about, and differentiate again. Differentiating $v(t)$ gives **acceleration**:

$$a(t) = \frac{dv}{dt} = \frac{d}{dt}\frac{dx}{dt} = \frac{d^{2}x}{dt^{2}}.$$

Acceleration is the *second derivative* of position. The notation $d^2x/dt^2$ records "differentiate $x$ twice with respect to $t$." This is the payoff of treating the derivative as an object: velocity is the slope of position, acceleration is the slope of velocity, and the same machine applies at each level.

![Three stacked plots sharing a time axis: position x = ½gt² (parabola), its slope velocity v = gt (rising line), and the slope of velocity, acceleration a = g (flat line); arrows link "slope of" between panels.](images/06-limits-and-the-derivative-fig-02.png)
*Figure 6.2 — Each curve is the slope of the one above it: differentiating descends from position to velocity to constant acceleration.*

---

## Worked examples

### Example 1 — Free fall: position to velocity to acceleration

Baumgartner's distance fallen from rest is $x(t) = \tfrac{1}{2} g t^2$. Differentiate once, using the power rule and the constant multiple rule:

$$v(t) = \frac{dx}{dt} = \tfrac{1}{2} g \cdot 2t = g\,t.$$

At $t = 30\ \text{s}$, his instantaneous speed is $v = (9.8)(30) = 294\ \text{m/s}$ downward — the answer mission control wanted, and the answer the speedometer paradox demanded. Differentiate again:

$$a(t) = \frac{dv}{dt} = g = 9.8\ \text{m/s}^2,$$

a constant. The power rule applied once gives velocity; applied twice it gives constant acceleration — the cleanest demonstration that constant-force motion has a second derivative that does not change. (We are neglecting air resistance; the real jump was faster, because the model ignores drag, as the source chapter notes.)

### Example 2 — A thrown ball, every rule once

A ball thrown upward has $x(t) = x_0 + v_0 t - \tfrac{1}{2} g t^2$. Term by term, using the sum and power rules:

$$v(t) = \frac{dx}{dt} = 0 + v_0 - \tfrac{1}{2}g\cdot 2t = v_0 - g t, \qquad a(t) = \frac{dv}{dt} = -g.$$

The velocity is a *linear* function of time (slope $-g$); the acceleration is constant and negative. Note what differentiation did to the constant $x_0$: its derivative is zero. A constant has no rate of change — it is flat, slope zero everywhere — which is why initial position drops out of the velocity entirely.

### Example 3 — The chain rule on rotation (a preview)

A point moving on a circle has horizontal position $x(t) = r\cos(\omega t)$. Its horizontal velocity requires the chain rule: the outer function is cosine, the inner is $\omega t$.

$$v_x(t) = \frac{dx}{dt} = -r\sin(\omega t)\cdot \frac{d}{dt}(\omega t) = -r\,\omega\sin(\omega t).$$

The factor $\omega$ from the inner derivative is non-negotiable. This is exactly the calculation that, done for both coordinates and then differentiated a second time, produces the centripetal acceleration of the next chapter — which is why we drilled the chain rule above.

---

## Return to the cold open

The speedometer paradox is resolved. At a single instant, displacement and elapsed time are both zero and their ratio $0/0$ is meaningless — Berkeley was right about that. But the instantaneous velocity is not that ratio; it is the *limit* of the difference quotient as the interval shrinks, the value $\Delta x / \Delta t$ heads toward as $\Delta t \to 0$. For Baumgartner's fall, that limit is $v(t) = g t$, and at $t = 30\ \text{s}$ it is a perfectly definite $294\ \text{m/s}$. The speedometer is, in effect, computing a derivative — the slope of the position curve at the present instant, the tangent line's steepness — and the limit is what lets it do so without ever dividing by zero. The two-point average of the cold open has become a one-point instantaneous rate, which is the first of the two questions calculus answers.

---

## Where it generalizes

The derivative is one idea — the limit of a ratio of changes — and it answers "how fast is this changing right now?" no matter what the quantities are. The rate of change of kinetic energy with time is *power*. The slope of a potential-energy curve gives a *force*, $F = -dU/dx$ — a derivative that has nothing to do with time at all, reading rate against position instead. Outside physics it is the same tool: a marginal cost is the derivative of total cost, a population's growth rate is the derivative of its size, the velocity of a chemical reaction is a derivative of concentration. What the math cannot do for you is decide that a question *is* a rate question, or choose what to differentiate with respect to what. A symbolic engine differentiates flawlessly once you hand it $f(x)$ — but recognizing that "where is the force largest?" means "examine $dU/dx$," or that the speedometer problem requires a limit at all, is the modeling judgment that took mathematicians a century and a half, from Newton to Weierstrass, to make precise. That judgment is yours; the cranking is the machine's.

---

## Exercises

1. **(From the definition.)** Using only the limit definition of the derivative (no rules), compute $f'(x)$ for $f(x) = 3x^2 + 5$. Show the cancellation of $h$ and the limit explicitly, and explain at which step you are allowed to cancel $h$ and why.

2. **(Power rule fluency.)** Differentiate: (a) $x^5$; (b) $7t^3 - 2t$; (c) $\sqrt{x} = x^{1/2}$; (d) $1/x = x^{-1}$. State the rule used for each.

3. **(Chain rule.)** Differentiate with respect to $t$: (a) $\cos(3t)$; (b) $\sin(\omega t + \phi)$ for constants $\omega, \phi$; (c) $(2t^2 + 1)^4$. For each, name the inner function and the factor it contributes.

4. **(Velocity and acceleration.)** A particle has position $x(t) = -3t^2 + 12t + 5$ (meters). Find $v(t)$ and $a(t)$. At what time is the velocity zero, and what is the particle's position then? (This is the turning point — interpret it.)

5. **(Derivation.)** Derive the power rule for the specific case $\frac{d}{dx}x^3 = 3x^2$ directly from the limit definition. Expand $(x+h)^3$, form the difference quotient, cancel $h$, and take the limit, explaining at each step why no division by zero occurs. Then state the general pattern your computation reveals.

---

## Sources

- Isaac Newton, *De analysi per aequationes numero terminorum infinitas* (1669; pub. 1711) and *Method of Fluxions* (1671; pub. 1736) — fluxions as instantaneous rates; velocity as the fluxion of position. [verified — see factchecks/06-limits-and-the-derivative-assertions.md] (original primary sources)
- Gottfried Wilhelm Leibniz, "Nova Methodus pro Maximis et Minimis," *Acta Eruditorum* (1684) — the first printed differential calculus; the product rule and the $dx$ notation. [verified — see factchecks/06-limits-and-the-derivative-assertions.md] (original primary source)
- George Berkeley, *The Analyst* (1734) — the "ghosts of departed quantities" critique motivating the limit. [verified — see factchecks/06-limits-and-the-derivative-assertions.md] (original primary source)
- Augustin-Louis Cauchy, *Cours d'analyse* (1821) and *Résumé des leçons sur le calcul infinitésimal* (1823) — refounding calculus on the limit. [verified — see factchecks/06-limits-and-the-derivative-assertions.md] (original primary sources)
- Karl Weierstrass (lectures, c. 1861, transmitted via students) — the modern $\varepsilon$–$\delta$ form of the limit; Bernard Bolzano (c. 1817) gave an earlier rigorous version. [verified — Bolzano 1817 / Cauchy 1821 / Weierstrass c.1861 confirmed; the precise Cauchy/Weierstrass/Bolzano attribution is debated, see factchecks/06-limits-and-the-derivative-assertions.md and pantry]
- Source chapter (this book's archive): "Motion Along a Straight Line" — $v = dx/dt$, $a = dv/dt = d^2x/dt^2$, and the free-fall worked numbers.
- D. Tall & S. Vinner, "Concept image and concept definition in mathematics," *Educational Studies in Mathematics* 12 (1981): 151–169 — the limit-as-value-approached misconception. [verified — see factchecks/06-limits-and-the-derivative-assertions.md]
