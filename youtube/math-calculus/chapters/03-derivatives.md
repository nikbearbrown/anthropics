# Chapter 3 — Derivatives

## TL;DR

- Instantaneous rates of change — and why a 270 mph car is a calculus textbook in motion.
- The chapter moves through The derivative as a limit, When the derivative fails to exist, The rules: from limits to algebra, The chain rule: composition done right, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Instantaneous rates of change — and why a 270 mph car is a calculus textbook in motion.*

In 2014, the Hennessey Venom GT accelerated from 0 to 200 mph in 14.51 seconds. Its top speed, recorded the same year on the Kennedy Space Center shuttle landing facility runway, was 270.49 mph.

Take the average. Two hundred miles per hour over 14.51 seconds is roughly 13.78 mph per second of acceleration, sustained — a number that means almost nothing on its own. What you actually want to know is what was happening *at* a particular instant. At second one, the car was barely moving. At second fourteen, it was nearly at 200 mph. At second seven, somewhere in between, the engine was working at the absolute edge of what its drivetrain could deliver. The acceleration was different at every moment.

That's the question. Not "what was the average rate?" but "what was the rate *right now*?" For a car, the answer changes how you tune the suspension, when the gearbox shifts, where the limits of grip are. For a stock price, it tells you whether the recent climb is decelerating. For a chemical reaction, it tells you when to add the next reagent. The instantaneous rate of change is the most useful number in nature, and the trouble is that you can't measure it directly. An instant has no duration. There is no time over which to average. The whole notion of "rate at a point" looks paradoxical — until you have the limit.

That's where Chapter 2 ends and this one begins. The instantaneous rate of change is a limit. It has a name. It is the *derivative*.

![Secant line tilting toward tangent ](images/03-derivatives-fig-01.png)
*Figure 3.1 — Secant line tilting toward tangent *

---

## The derivative as a limit

Take a function $f$ and a point $x$. Pick a small number $h$. The average rate of change of $f$ between $x$ and $x + h$ is the slope of the line connecting $(x, f(x))$ to $(x + h, f(x + h))$ — the *secant line*:

$$\text{average rate} = \frac{f(x + h) - f(x)}{h}$$

This is just rise over run. Nothing mysterious. The trouble is that this rate depends on $h$ — it's the average over the interval, not the rate at the point.

Now do what Chapter 2 taught. Take the limit as $h$ approaches zero:

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

When this limit exists, we call it the *derivative* of $f$ at $x$. Geometrically, the secant line tilts toward the tangent line — the line that just grazes the curve at $(x, f(x))$ — and the derivative is the slope of that tangent. Physically, if $f$ is a position function, the derivative is the instantaneous velocity. If $f$ is a velocity function, the derivative is the instantaneous acceleration. The derivative is the rate of change at a point, made rigorous by the limit.

Watch the machinery on $f(x) = x^2$. The difference quotient is

$$\frac{f(x + h) - f(x)}{h} = \frac{(x + h)^2 - x^2}{h} = \frac{x^2 + 2xh + h^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h$$

For any $h \neq 0$, the average rate is $2x + h$. Take the limit as $h \to 0$: the $h$ vanishes, and you're left with $2x$. So $f'(x) = 2x$. The derivative of $x^2$ is $2x$.

Notice what just happened. We started with a function defined at every $x$. We constructed, for each $x$, a *new* number — the slope at that point. The collection of those numbers is itself a function. The derivative isn't just a value; it's a new function $f'$ derived from the original $f$. Wherever the limit exists, $f'$ is defined. Where the limit fails, $f'$ is not.

This dual nature — derivative as a number at a point, derivative as a function over a domain — is worth holding clearly. Both are right. The derivative *at* $x = 3$ for $f(x) = x^2$ is the number 6. The derivative *function* is $f'(x) = 2x$, defined for every real number.

There are two competing notations, both useful. Lagrange's $f'(x)$ reads the derivative as a function of $x$. Leibniz's $\frac{df}{dx}$ or $\frac{d}{dx}f(x)$ reads it as the ratio of a tiny change in $f$ to a tiny change in $x$ — closer to the limit definition, more cumbersome to write but easier to manipulate when the chain rule shows up.

---

## When the derivative fails to exist

The limit defining $f'(x)$ doesn't always exist. When it fails, the failure modes are visible in the graph of $f$.

The first failure mode is *discontinuity*. If $f$ has a jump or a hole at $x$, the difference quotient has no chance — the function isn't even continuous there, and a tangent line through a point that doesn't exist is meaningless. Differentiability at $x$ requires continuity at $x$. The implication is one-way: continuous functions can fail to be differentiable, but discontinuous functions cannot be differentiable.

The second failure mode is the *corner*. The function $f(x) = |x|$ is continuous everywhere, including at $x = 0$. But there's no single tangent line at $x = 0$. From the right, the slope is 1. From the left, the slope is $-1$. The one-sided limits of the difference quotient disagree, so the two-sided limit doesn't exist. The corner has no tangent.

The third failure mode is the *vertical tangent*. The function $f(x) = x^{1/3}$ is continuous and smooth-looking, but at $x = 0$ the tangent line is vertical. The slope is "infinite" in the same colloquial sense as $\lim_{x \to 0^+} 1/x$ — the limit blows up. There's a tangent line you could draw, but it doesn't have a finite slope, and the derivative isn't a finite number.

![Side-by-side diagram of differentiability failures ](images/03-derivatives-fig-02.png)
*Figure 3.2 — Side-by-side diagram of differentiability failures *

The trade-off named here is one to keep close: differentiability is *stronger* than continuity. Every differentiable function is continuous. Most continuous functions are differentiable. But you cannot run the implication backwards — being continuous doesn't earn you a derivative. The corners and vertical tangents are continuous; they're just not smooth enough.

For most functions you'll meet in this book — polynomials, rational functions away from their poles, exponentials, sines, cosines, logarithms on their domains — the derivative exists everywhere. The failure modes are real but localized. They matter when they show up; they don't show up often.

---

## The rules: from limits to algebra

If you had to compute every derivative from the limit definition, calculus would be a slow craft. Fortunately, the limit work has been done once, in clean cases, and what remains is algebra. The differentiation rules turn an analytical operation into a mechanical one.

The **power rule** is the workhorse. For any real number $n$,

$$\frac{d}{dx}\bigl(x^n\bigr) = n x^{n-1}$$

This handles $x^2$ (giving $2x$, as we computed above), $x^3$ (giving $3x^2$), $x^{-1}$ (giving $-x^{-2}$, i.e., $-1/x^2$), and even $x^{1/2}$ (giving $\frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$). The proof for positive integer $n$ is a binomial expansion of $(x+h)^n$, an exercise in the limit definition. The extension to all real exponents requires the chain rule and logarithmic differentiation, which arrive shortly. For our purposes the rule works for any $n$ and you can memorize it as such.

The **sum rule** says the derivative of a sum is the sum of the derivatives: $(f + g)' = f' + g'$. This follows directly from the linearity of limits. The derivative passes through addition. So does scalar multiplication: $(cf)' = c f'$. The derivative of a polynomial is therefore mechanical — differentiate term by term, using the power rule on each monomial. The derivative of $x^4 - 5x^3 + 7x - 11$ is $4x^3 - 15x^2 + 7$.

The **product rule** is where the algebra stops being obvious. The derivative of a product is *not* the product of the derivatives. The correct rule is

$$\frac{d}{dx}\bigl(f \cdot g\bigr) = f'(x) g(x) + f(x) g'(x)$$

There's a geometric picture for this. Imagine $f$ and $g$ as the two sides of a rectangle with area $A = f \cdot g$. Increase each side by a tiny amount: $f$ increases by $f'(x) \, dx$, $g$ increases by $g'(x) \, dx$. The new area is $(f + f' \, dx)(g + g' \, dx) = fg + fg' \, dx + f'g \, dx + f' g' (dx)^2$. The change in area $dA$ is the sum of the two thin strip contributions $f g' \, dx + f' g \, dx$, plus the corner term $f' g' (dx)^2$ which vanishes faster than $dx$ and contributes nothing in the limit. Divide both sides by $dx$ and you have the product rule.

![Product-rule rectangle picture ](images/03-derivatives-fig-03.png)
*Figure 3.3 — Product-rule rectangle picture *

The **quotient rule** follows from the product rule applied to $f \cdot (1/g)$:

$$\frac{d}{dx}\!\left(\frac{f(x)}{g(x)}\right) = \frac{f'(x) g(x) - f(x) g'(x)}{[g(x)]^2}$$

The minus sign in the numerator is where errors tend to creep in. The order matters: it's "low-d-high minus high-d-low, all over low-squared," in the mnemonic that has saved generations of students.

A worked case. To differentiate $\frac{3x + 1}{x^2 + 1}$, set $f = 3x + 1$ and $g = x^2 + 1$. Then $f' = 3$ and $g' = 2x$. The quotient rule gives

$$\frac{d}{dx}\!\left(\frac{3x+1}{x^2+1}\right) = \frac{3(x^2+1) - (3x+1)(2x)}{(x^2+1)^2} = \frac{3x^2 + 3 - 6x^2 - 2x}{(x^2+1)^2} = \frac{-3x^2 - 2x + 3}{(x^2+1)^2}$$

There's a trade-off worth naming here. The limit definition is canonical — it's what a derivative *is*. The rules are fast — they're how you actually compute. The price of the rules is memorization and error-proneness; the price of the limit definition is slowness. For routine computation, use the rules. When in doubt, fall back to the limit definition. The two will always agree.

---

## The chain rule: composition done right

Functions composed inside other functions are everywhere. The chain rule handles them.

If $y = f(g(x))$, then

$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$$

In Leibniz notation, where the chain rule looks almost like algebraic cancellation: if $y = f(u)$ and $u = g(x)$, then

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

Read this aloud: the rate at which $y$ changes with $x$ equals the rate at which $y$ changes with $u$, times the rate at which $u$ changes with $x$. Each derivative is a rate, and the rates compose multiplicatively. If $y$ is going up twice as fast as $u$, and $u$ is going up three times as fast as $x$, then $y$ is going up six times as fast as $x$. The chain rule encodes this and nothing more.

A worked case. Differentiate $h(x) = (x^2 + 3)^5$. Identify the outer and inner: outer is "raise to the fifth power," $f(u) = u^5$; inner is $u = g(x) = x^2 + 3$. Then $f'(u) = 5u^4$ and $g'(x) = 2x$. The chain rule:

$$h'(x) = 5(x^2 + 3)^4 \cdot 2x = 10x(x^2 + 3)^4$$

The mental motion: differentiate the outer function leaving the inner alone, then multiply by the derivative of the inner. Power-rule the outer, treat $g(x)$ as if it were a variable, then attach $g'(x)$ as a multiplicative factor.

![Differentiate from the outside in, multiplying the derivative of each layer.](images/03-derivatives-fig-04.png)
*Figure 3.4 — Chain rule as nested boxes *

The chain rule is the most heavily used tool in differential calculus. Once you've internalized the pattern — outer-of-inner times derivative-of-inner — most computations dissolve into a few mechanical lines.

---

## The transcendental functions

Polynomials and rationals are differentiable by the rules above. The transcendental functions — sine, cosine, the natural exponential, the logarithm — have derivatives that have to be derived once from limits, then memorized.

For sine and cosine, the result is

$$\frac{d}{dx}(\sin x) = \cos x \qquad \frac{d}{dx}(\cos x) = -\sin x$$

Two warnings, both consequential.

First: these formulas are valid *only* when $x$ is measured in radians. In degrees, an extra factor of $\pi/180$ appears, because the slope of a sine curve plotted with degrees on the horizontal axis is geometrically different from the slope of the same curve plotted with radians. The radian formulation is what makes the formula clean. There's a reason mathematicians and physicists insist on radians; this is the reason.

Second: the derivation uses the limit $\lim_{\theta \to 0} (\sin \theta)/\theta = 1$, which is the calculus equivalent of "for small angles, the sine of an angle is approximately the angle itself." That limit is geometrically self-evident on the unit circle and rigorously provable by squeeze-theorem arguments. Once you have it, the derivative formulas for sine and cosine fall out from the difference quotient and the angle-addition identities.

For the natural exponential, the rule is even cleaner:

$$\frac{d}{dx}(e^x) = e^x$$

The exponential function is its own derivative. This isn't a coincidence; it's the property that defines $e$. The number $e \approx 2.718$ is the unique base for which the slope of the exponential curve at $x = 0$ equals 1 — i.e., for which the function and its derivative coincide. Any other base $b$ gives $\frac{d}{dx}(b^x) = b^x \ln b$, with the constant factor $\ln b$ correcting for the choice of base. Pick $b = e$ and the constant becomes 1. That's why $e$ is "natural."

The derivative of the natural logarithm is

$$\frac{d}{dx}(\ln x) = \frac{1}{x}, \qquad x > 0$$

This follows from the inverse-function relationship: $\ln$ is the inverse of $e^x$, and the derivative of an inverse function at a point is the reciprocal of the original derivative at the corresponding point. Since $e^x$ has derivative $e^x$, and $\ln x$ is the inverse, its derivative is $1/e^{\ln x} = 1/x$.

These four formulas — for $\sin x$, $\cos x$, $e^x$, and $\ln x$ — combined with the chain, product, and quotient rules, generate the derivative of essentially any function you will encounter in introductory calculus.

---

## Higher-order derivatives: jerk, snap, and the Venom GT

Once you have a derivative function $f'(x)$, you can differentiate it to get $f''(x)$, the *second derivative*. Differentiate again for $f'''(x)$, and so on. These are called *higher-order derivatives*, and they have physical meaning when the original function is a position.

If $s(t)$ is position as a function of time, then $s'(t) = v(t)$ is velocity, and $s''(t) = a(t)$ is acceleration. The third derivative $s'''(t)$ has a name too: *jerk*, the rate of change of acceleration. The fourth is *snap*. The fifth and sixth are *crackle* and *pop*, named by physicists with a sense of humor that their grant proposals do not always reveal.

These aren't pedagogical curiosities. Jerk is what you feel when an elevator starts moving — not the acceleration itself, but the sudden change in acceleration. Engineers designing roller coasters constrain jerk explicitly because uncontrolled jerk produces neck injuries. Anti-lock braking systems modulate the deceleration on a millisecond timescale precisely to manage jerk. Higher-order derivatives are how the world tells you it's changing the rules of how things change.

Now, the Venom GT.

Real cars don't accelerate at a constant rate. The engine has its peak torque band; the gearbox shifts; aerodynamic drag grows with the square of speed. A reasonable first-order model for how a high-performance car approaches its top speed is

$$v(t) = v_{\max}\bigl(1 - e^{-t/\tau}\bigr)$$

where $v_{\max}$ is the top speed and $\tau$ is a time constant that depends on the car. (This is a standard automotive approximation. The specific $\tau$ for the Venom GT is not from a manufacturer specification; we're using the model qualitatively, not as a precision engineering claim.)

Differentiate to find the acceleration:

$$a(t) = \frac{dv}{dt} = v_{\max} \cdot \frac{d}{dt}\bigl(1 - e^{-t/\tau}\bigr) = v_{\max} \cdot \left(0 - e^{-t/\tau} \cdot \left(-\frac{1}{\tau}\right)\right) = \frac{v_{\max}}{\tau} \, e^{-t/\tau}$$

Look at what this says. At $t = 0$, the acceleration is $v_{\max}/\tau$ — the maximum, the launch shove. As $t$ grows, the acceleration decays exponentially toward zero. The car never quite reaches its top speed; it asymptotes. Like the relativistic mass at the speed of light, the model has a finite limit it can approach but not arrive at. The cost of each next mph grows exponentially.

For the Venom GT — top speed 270.49 mph, 0-to-200 in 14.51 seconds — pick $\tau$ so the model passes through both anchors. Setting $v(14.51) = 200$ with $v_{\max} = 270.49$ gives

$$200 = 270.49(1 - e^{-14.51/\tau}) \implies e^{-14.51/\tau} = 1 - \frac{200}{270.49} \approx 0.2606 \implies \tau \approx \frac{14.51}{1.345} \approx 10.79 \text{ seconds}$$

Then the launch acceleration is $a(0) = v_{\max}/\tau \approx 270.49/10.79 \approx 25.1$ mph per second, or about 1.14 g. That's the moment the driver is pinned to the seat.

Differentiate again to get the jerk:

$$j(t) = \frac{da}{dt} = \frac{v_{\max}}{\tau} \cdot \left(-\frac{1}{\tau}\right) e^{-t/\tau} = -\frac{v_{\max}}{\tau^2} e^{-t/\tau}$$

The jerk is most negative at $t = 0$ — the moment the launch shove begins to fade. As $t$ grows, the jerk decays (in magnitude) along with everything else. The driver feels the launch first as the maximum acceleration, then as the steady fade of that acceleration into nothing.

The car is a calculus textbook in motion. Position is what you see. Velocity is the speedometer. Acceleration is what your body registers as force. Jerk is the change in that force — the texture of the launch. Each of these is the derivative of the previous one. The whole hierarchy is built from the same operation, applied repeatedly.

![Time-series plot of v(t), a(t), and j(t) for](images/03-derivatives-fig-05.png)
*Figure 3.5 — Time-series plot of v(t), a(t), and j(t) for*

---

## The one idea to carry forward

The derivative is the limit of an average rate of change as the interval shrinks to zero. That is the whole definition. Every formula, every rule, every transcendental result in this chapter follows from it.

The power, sum, product, quotient, and chain rules turn the analytical operation of taking a limit into the algebraic operation of mechanical manipulation. You don't have to recompute the limit every time. The formulas memorize the limit work and let you compute fast. But when you forget a rule, or when a function refuses to fit any of the standard patterns, you can always go back to

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

and recover from first principles.

The derivative is more than a rate of change. It is a function — a new object built from the original — whose value at each point is the slope of the original's tangent line. It can be differentiated again, and again, producing a hierarchy of higher-order derivatives that describe how the original function bends, and how that bending itself is changing. For physical systems, those higher derivatives encode the texture of motion: not just where you are, not just how fast you're moving, but how that motion is changing on every timescale.

The next chapter takes the derivative and asks what it's *for*. We've built the tool. Chapter 4 puts it to work — related rates, linear approximation, optimization, finding maxima and minima, sketching curves from their derivatives. Every application starts from what we've built here: the derivative as a limit, the rules that compute it, the higher-order derivatives that encode bending.

The Venom GT crossed 200 mph in 14.51 seconds because at every instant during those 14.51 seconds, the acceleration had a specific finite value. That value was the derivative of velocity. The velocity was the derivative of position. The position was where the car was. Differentiation is the operation that lets you extract each of these from the next. Done.

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a collaborative thinking partner — asking it to check your reasoning, generate similar problems, or explain a step you're stuck on. The goal is to think alongside the tool, not to have the tool think for you.

**Exercise 1.** Ask an LLM to compute the derivative of $f(x) = x^3$ from the limit definition — not from the power rule. Before seeing its work, expand $(x+h)^3$ yourself, build the difference quotient, simplify, and take the limit. Compare your derivation step by step with the LLM's. Did it expand correctly? Did it cancel the $h$ properly before taking the limit, rather than substituting $h = 0$ in the unsimplified expression?

**Exercise 2.** Give an LLM the function $f(x) = |x^2 - 4|$ and ask whether $f$ is differentiable at $x = 2$. Before seeing the answer, sketch the graph mentally — where does the absolute value introduce corners? Solve it yourself and compare. If the LLM gives a one-word answer, push back: "Why? Show me the one-sided limits of the difference quotient at $x = 2$."

**Exercise 3.** Ask an LLM to derive the quotient rule from the product rule. The standard derivation writes $f/g$ as $f \cdot g^{-1}$ and applies the product rule together with the chain rule applied to $g^{-1}$. Walk the LLM through your version. Does the LLM correctly handle the chain rule on $g^{-1}$, getting $-g'/g^2$? Or does it shortcut to the formula and skip the derivation?

**Exercise 4.** Tell an LLM: "I claim that $\frac{d}{dx}(\sin x) = \cos x$ holds in *both* radians and degrees, because the formula doesn't have any units in it." Have the LLM evaluate the claim. The expected answer is that the claim is wrong — the formula assumes radians. Push the LLM until it gives a clean explanation of why the radian-vs-degree distinction matters and what extra factor appears in degrees. The geometric reason involves $\lim_{\theta \to 0}(\sin \theta)/\theta$, which equals 1 in radians and $\pi/180$ in degrees.

**Exercise 5.** Give an LLM the function $h(x) = \sin(\cos(e^x))$ and ask it to compute $h'(x)$. Before looking at the answer, identify the chain of compositions yourself: outermost is sine, middle is cosine, innermost is exponential. Differentiate from the outside in, multiplying the derivative of each layer. Check the LLM's answer — did it apply the chain rule three times correctly? Did it preserve the negative sign from $(\cos)' = -\sin$?

**Exercise 6.** Build, with an LLM, a position function $s(t)$ that gives a non-trivial velocity, acceleration, and jerk. Try $s(t) = t^4 - 4t^3 + 5t^2 + 2t$. Compute $v(t), a(t), j(t)$ yourself. Ask the LLM to verify each one, then ask it to identify the times at which (a) the velocity is zero, (b) the acceleration is zero, and (c) the jerk is zero. What does each of those instants represent physically? If the LLM gives only the algebra, push it for the interpretation.

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Maria Gaetana Agnesi** wrote *Instituzioni analitiche* in 1748 — the first textbook to cover both differential and integral calculus in a unified system. The curve called the "witch of Agnesi" is a mistranslation; the Italian was "averse" or "turning," not "witch."

**Run this:**

```
Who was Maria Gaetana Agnesi, and how does her unified treatment of calculus connect to the derivatives we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

→ Search **"Maria Gaetana Agnesi"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to derive the curve known as the "witch of Agnesi" and explain how Agnesi originally presented it.
- Ask it about Agnesi's later abandonment of mathematics for the religious care of the poor — and what that suggests about 18th-century intellectual life.

What changes? What gets better? What gets worse?
