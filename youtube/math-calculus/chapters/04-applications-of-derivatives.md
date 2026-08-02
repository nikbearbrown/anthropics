# Chapter 4 — Applications of Derivatives

## TL;DR

- What the derivative is actually for — and why a camera operator is solving calculus problems with their wrists.
- The chapter moves through Related rates: two clocks, one equation, Linear approximation: the tangent line earns its keep, Critical points: where the derivative goes quiet, The Mean Value Theorem: averaging and instantaneity, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*What the derivative is actually for — and why a camera operator is solving calculus problems with their wrists.*

![Rocket-and-camera geometry ](images/04-applications-of-derivatives-fig-01.png)
*Figure 4.1 — Rocket-and-camera geometry *

A rocket lifts off. A camera operator on the ground tilts the lens upward to track it. Simple enough picture. But here's what's actually happening to that operator's hands.

The rocket is climbing. The angle between the camera and the ground is increasing. Both of those statements are about rates — how fast the height changes, how fast the angle changes. And the two rates are tied together by geometry. You can't change one without the other responding, in a specific amount, at each specific moment. The operator isn't just tilting. The operator is solving a physics problem with their wrists, in real time, whether they know the calculus or not.

If the rocket is 500 feet high, climbing at 100 feet per second, and the camera sits 1000 feet from the pad, the angle $\theta$ satisfies $\tan\theta = h/1000$. Differentiate both sides with respect to time — the chain rule fires on the left, giving $\sec^2\theta \cdot (d\theta/dt)$, and on the right, giving $(1/1000)(dh/dt)$ — and you get

$$\sec^2\theta \cdot \frac{d\theta}{dt} = \frac{1}{1000} \cdot \frac{dh}{dt}$$

At $h = 500$, $\tan\theta = 0.5$, so $\sec^2\theta = 1 + \tan^2\theta = 1.25$. With $dh/dt = 100$:

$$\frac{d\theta}{dt} = \frac{100}{1000 \cdot 1.25} = 0.08 \text{ rad/s}$$

About 4.6 degrees per second. At launch, when the rocket is barely off the pad and the angle is nearly flat, the rate is much faster — the camera sweeps quickly across the low part of the arc. High up, when the rocket is nearly overhead, the angle barely changes even though the rocket is screaming upward. The operator's job gets easier as the rocket climbs, not harder. That's the geometry of the inverse tangent. You only see it if you differentiate.

![Line chart of dθ/dt (angular rate) on the](images/04-applications-of-derivatives-fig-02.png)
*Figure 4.2 — Line chart of dθ/dt (angular rate) on the*

That's the flavor of this whole chapter. We know how to differentiate. Now we ask what derivatives are *for*.

---

## Related rates: two clocks, one equation

The rocket problem is one instance of a general structure. Two quantities both depend on time. They're linked by an equation. Differentiate the equation and you get a relationship between the rates. That relationship lets you find one rate if you know the other.

Here's the pattern, made explicit. A ladder — 13 feet long — leans against a wall. The bottom slides outward at 2 feet per second. How fast does the top slide down when the bottom is 5 feet from the wall?

Let $x$ be the distance from the wall to the bottom, $y$ the height of the top. They're related by the Pythagorean theorem:

$$x^2 + y^2 = 169$$

Differentiate both sides with respect to $t$:

$$2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$$

When $x = 5$: $y = \sqrt{169 - 25} = 12$. With $dx/dt = 2$:

$$2(5)(2) + 2(12)\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{5}{6} \text{ ft/s}$$

The top is falling at 5/6 of a foot per second. The negative sign is the calculus's way of saying "downward."

![Ladder diagram ](images/04-applications-of-derivatives-fig-03.png)
*Figure 4.3 — Ladder diagram *

The interesting thing about related rates isn't the arithmetic. It's the move. You took a static geometric equation — Pythagoras — and by differentiating with respect to time, turned it into a dynamic equation about rates. The same equation that constrains positions also constrains velocities. There's a whole philosophy in that: the structure of the world that determines where things are also determines how fast they're moving.

The errors in related-rates problems almost never come from the differentiation. They come from setting up the wrong equation — using the wrong geometric relationship, or writing an equation that only holds at one instant instead of generally. A picture almost always fixes this. Draw the situation at a general time, not at the specific instant you're asked about. Write the equation that holds at every time. Then differentiate.

---

## Linear approximation: the tangent line earns its keep

There's a concrete payoff to understanding the tangent line as more than a geometric object. The tangent line at a point is the *best* linear approximation to the function near that point. That means for inputs close to the anchor point, the tangent line is a usable substitute for the function — simpler to evaluate, close enough in answer.

At $x = a$, the tangent line is $L(x) = f(a) + f'(a)(x - a)$. For $x$ near $a$, $L(x) \approx f(x)$.

Say you want $\sqrt{4.1}$ without a calculator. Anchor at $a = 4$, where $\sqrt{4} = 2$ exactly. The derivative of $\sqrt{x}$ is $1/(2\sqrt{x})$, so $f'(4) = 1/4$. The tangent line approximation:

$$\sqrt{4.1} \approx 2 + \frac{1}{4}(4.1 - 4) = 2 + \frac{0.1}{4} = 2.025$$

The actual value is 2.0248. The error is 0.0002. That's less than a hundredth of a percent, computed in your head from one multiplication.

The technique has a name in engineering: *first-order approximation*. The idea is that near a known point, any smooth function behaves like a line. Use the line, get a fast answer, know the error is small because you stayed close to the anchor.

What happens when you move away from the anchor? The error grows. At $x = 5$, the tangent-line approximation gives $2 + (1/4)(1) = 2.25$, but $\sqrt{5} \approx 2.236$. The error is now 0.6 percent — sixty times larger than at $x = 4.1$. Accuracy degrades with distance from the anchor. The further you go, the worse the approximation. This is not a flaw in the technique; it's built into what "linear" means. A straight line is a perfect approximation to a curved function at one point and progressively wrong everywhere else.

![The tangent line is perfect at a = 4 and progressively wrong everywhere else — the error grows with distance from the anchor](images/04-applications-of-derivatives-fig-04.png)
*Figure 4.4 — Graph of y = √x (solid curve) and*

The differential notation makes this concrete. Call a small change in $x$ by the name $dx$. The change in $f$ predicted by the tangent line is $dy = f'(x) \, dx$. The actual change in $f$ is $\Delta y = f(x + dx) - f(x)$. For small $dx$, $\Delta y \approx dy$. The differential $dy$ is the linear estimate; $\Delta y$ is what the function actually does. They agree to first order.

This setup will matter in Chapter 5. The integral is, among other things, a sum of tiny $dy$'s — infinitesimal contributions, each a differential. Linear approximation isn't just a computational trick; it's the philosophical foundation of the whole integral idea.

---

## Critical points: where the derivative goes quiet

A function reaches a maximum or minimum only in specific places. The question is: which ones?

At an interior maximum or minimum, the tangent line must be horizontal. If it weren't — if the function were still rising or falling at the extremum — you could move slightly in the direction of increase and find a higher (or lower) value, contradicting the assumption. So at any interior extremum, $f'(c) = 0$.

(Or the derivative doesn't exist. Peaks with corners — like the vertex of $|x|$ — also qualify. The general condition is $f'(c) = 0$ or $f'(c)$ undefined.)

Points where either condition holds are *critical points*. They are the candidates for extrema. Not every candidate wins — a critical point can be a maximum, a minimum, or neither (a flat inflection point). But every interior extremum is a critical point, so finding all critical points and checking them is the complete procedure.

For a continuous function on a closed interval $[a, b]$, the absolute maximum and minimum must occur either at a critical point inside the interval or at an endpoint. So the algorithm is simply: evaluate $f$ at every critical point and at both endpoints, then compare. The largest value is the absolute maximum; the smallest is the absolute minimum.

A worked example. $f(x) = x^3 - 3x + 1$ on $[-2, 2]$. Derivative: $f'(x) = 3x^2 - 3 = 3(x-1)(x+1)$. Critical points at $x = \pm 1$, both in $(-2, 2)$.

Evaluate $f$ at $x = -2, -1, 1, 2$:

$$f(-2) = -1, \quad f(-1) = 3, \quad f(1) = -1, \quad f(2) = 3$$

Absolute maximum: 3, achieved at $x = -1$ and $x = 2$.
Absolute minimum: $-1$, achieved at $x = -2$ and $x = 1$.

![Graph of f(x) = x³ − 3x +](images/04-applications-of-derivatives-fig-05.png)
*Figure 4.5 — Graph of f(x) = x³ − 3x +*

The fact that the maximum is achieved at two different points — one a critical point, one an endpoint — is worth noticing. Both count. An endpoint can beat an interior critical point.

---

## The Mean Value Theorem: averaging and instantaneity

Here's a fact that sounds obvious: if you drive from Boston to New York in two hours and the distance is 200 miles, then at some point during the drive you were going exactly 100 miles per hour. Not approximately — *exactly*.

This is the Mean Value Theorem. If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists some $c$ in $(a,b)$ where

$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

The right side is the average rate of change over the interval — the secant slope. The theorem says this average must be instantaneously achieved somewhere inside.

![The MVT says the secant slope must be matched by the tangent somewhere inside — the average rate of change equals the instantaneous rate at some point c](images/04-applications-of-derivatives-fig-06.png)
*Figure 4.6 — Graph of a smooth curve f on [a,*

It sounds like common sense. It is not trivial to prove. The proof uses a clever auxiliary function and the extreme-value theorem, and it works only under the stated conditions (continuous on the closed interval, differentiable on the open one).

The MVT is less important as a computational tool than as an *inferential* tool. It's the theorem you invoke when you want to turn information about derivatives into information about function values. Several things we take for granted in calculus rest on it:

*If $f'(x) = 0$ everywhere on an interval, then $f$ is constant on that interval.* Proof: take any two points $a < b$. The MVT gives some $c$ with $f'(c) = (f(b) - f(a))/(b - a)$. If $f'(c) = 0$, then $f(b) = f(a)$. Since $a$ and $b$ were arbitrary, $f$ is constant.

*If $f'(x) > 0$ everywhere on an interval, then $f$ is increasing.* Same argument: the MVT forces the secant slope positive between any two points.

*If two functions have the same derivative everywhere, they differ by a constant.* Apply the zero-derivative result to their difference.

That last corollary is the one we'll use in Chapter 5. It tells us that all antiderivatives of a given function are related by additive constants — which is why $\int f(x) \, dx = F(x) + C$. The $+C$ isn't a loose end. It's the MVT.

---

## First and second derivatives tell you the shape

You want to sketch $f(x)$ accurately. You don't want to plot a hundred points. You want to understand the shape from the structure of $f$.

Two tools: the first derivative and the second derivative.

The *first derivative* tells you where the function is rising and falling. On any interval where $f'(x) > 0$, the function is increasing. On any interval where $f'(x) < 0$, it's decreasing. At a critical point where $f'$ changes sign, you have a local extremum. Changes from positive to negative: local maximum. Changes from negative to positive: local minimum. No sign change: neither.

This is the *first derivative test*, and it works even when the second derivative is complicated or zero.

The *second derivative* tells you about concavity — whether the function curves upward or downward. Where $f''(x) > 0$, the graph is *concave up*: it curves like a bowl, and tangent lines lie below the graph. Where $f''(x) < 0$, the graph is *concave down*: it curves like an arch, and tangent lines lie above. Where concavity changes is an *inflection point*, typically where $f''(x) = 0$ and $f''$ changes sign.

![Two side-by-side curve panels ](images/04-applications-of-derivatives-fig-07.png)
*Figure 4.7 — Two side-by-side curve panels *

The *second derivative test* at a critical point: if $f'(c) = 0$ and $f''(c) < 0$, the function is concave down at $c$, so it's a local maximum. If $f''(c) > 0$, it's concave up, so it's a local minimum. If $f''(c) = 0$, the test tells you nothing — fall back to the first derivative test.

Pull all of this together and you get the curve-sketching procedure: find domain, intercepts, and symmetry. Analyze $f'$ for critical points and monotonicity. Analyze $f''$ for concavity and inflection points. Identify any asymptotes. Then draw. The result is a qualitatively accurate picture of the function without having computed a single function value except where the analysis requires it.

The payoff is not just graphs. It's understanding. Running this analysis on a function tells you everything about its large-scale behavior — where it rises, where it peaks, how it bends, where it turns. That's the derivative's information content about the function.

---

## Optimization: constraints set up the game, calculus wins it

Most real optimization problems have a constraint baked in. You want to maximize area but you have a fixed length of fence. You want to minimize cost but you have a fixed volume requirement. You want to maximize the angle subtended by a painting at your eye as you approach a gallery wall — a constraint on the geometry.

The constraint is not an obstacle. It's the tool that reduces the problem from two variables to one. Once you've used the constraint to eliminate one variable, you have a single function to optimize over a single domain — and the critical-point method handles it.

The pattern: write the objective function (the thing you're maximizing or minimizing). Write the constraint. Solve the constraint for one variable; substitute into the objective. Differentiate. Find critical points. Compare values at critical points and endpoints. Interpret.

A concrete case. Enclose a rectangular field with 100 feet of fencing, using a wall as one side. Maximize the area.

Let $y$ be the side perpendicular to the wall. The fencing budget gives $x + 2y = 100$, so $x = 100 - 2y$. Area is $A(y) = xy = (100 - 2y)y = 100y - 2y^2$.

$A'(y) = 100 - 4y = 0 \implies y = 25$. Second derivative $A'' = -4 < 0$: maximum confirmed. With $y = 25$, $x = 50$. Maximum area is 1250 square feet.

What's interesting here isn't the computation. It's the proportion: $x = 2y$. The optimal wall-parallel side is twice the perpendicular. This proportion shows up whenever you optimize a rectangle with one free side, regardless of the total fencing. The calculus gives you the general answer, not just the specific number.

![Diagram of the fencing problem ](images/04-applications-of-derivatives-fig-08.png)
*Figure 4.8 — Diagram of the fencing problem *

---

## L'Hôpital, Newton, and the bridge to integration

Three more applications, each connecting derivatives to something bigger.

*L'Hôpital's rule* handles limits that come out $0/0$ or $\infty/\infty$ — called indeterminate forms because they don't evaluate to anything on their own. If $f$ and $g$ both approach zero (or both blow up) as $x \to a$, and if the limit of $f'(x)/g'(x)$ exists, then

$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

Replace the ratio with the ratio of derivatives; recompute. The rule works because near $a$, both functions look like their linear approximations: $f(x) \approx f'(a)(x-a)$ and $g(x) \approx g'(a)(x-a)$. The $(x-a)$ factors cancel, and the ratio of functions reduces to the ratio of derivatives.

The critical warning: check that you actually have an indeterminate form before applying the rule. $\lim_{x \to 0} \sin(x)/x$ is $0/0$ — apply L'Hôpital, get $\cos(x)/1 \to 1$. But $\lim_{x \to 0} x/\cos(x)$ is $0/1$ — not indeterminate, substitution gives 0 immediately. L'Hôpital applied to a non-indeterminate form gives the wrong answer.

*Newton's method* finds roots. If you want to solve $f(x) = 0$, start with a guess $x_0$ and iterate:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Geometrically: draw the tangent line at your current guess; where it crosses zero is your next guess. Repeat. The method converges fast — under good conditions, the number of correct decimal places roughly doubles at each step.

To find $\sqrt{2}$: solve $x^2 - 2 = 0$, so $f(x) = x^2 - 2$ and $f'(x) = 2x$. Start at $x_0 = 1$.

$$x_1 = 1 - \frac{-1}{2} = 1.5 \qquad x_2 = 1.5 - \frac{0.25}{3} = 1.4\overline{16} \qquad x_3 \approx 1.41421356\ldots$$

Three iterations from a poor starting guess. The quadratic convergence is what makes Newton's method the root-finding algorithm at the core of most numerical software.

![Each iteration: draw the tangent, find where it hits zero, move there. The correct digits roughly double each step.](images/04-applications-of-derivatives-fig-09.png)
*Figure 4.9 — Graph of f(x) = x² − 2 with*

*Antiderivatives* are where the chapter gestures toward what's coming. Given $f$, find $F$ such that $F'(x) = f(x)$. By the MVT corollary, all such $F$'s differ by a constant. The general antiderivative is written $\int f(x) \, dx = F(x) + C$.

The standard antiderivatives come from reversing the standard derivatives:

$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1), \quad \int e^x \, dx = e^x + C, \quad \int \cos x \, dx = \sin x + C$$

These are not new computations. They are the derivative table read backwards.

| Derivative rule (forward) |
| --- |
| d |
| d |
| d |
| d |
| d |

The Fundamental Theorem of Calculus, which Chapter 5 develops, will show that the integral — historically defined as a limit of sums, a device for computing areas and accumulated quantities — and the antiderivative are the same operation. Integration and differentiation are inverse operations. The antiderivative introduced here, at the end of a chapter on derivatives, is the hinge between the two halves of calculus.

---

## The synthesis: one rocket, every section

Come back to the rocket and the camera.

Height: $h(t) = 16t^2$. So $h'(t) = 32t$ — the rocket accelerates uniformly. Camera at $D = 1000$ ft. Angle: $\tan\theta = h/1000$.

Differentiating for the angular rate: $\sec^2\theta \cdot \theta' = (32t)/1000$. This is a related rate. With $\sec^2\theta = 1 + (16t^2/1000)^2$, you get $\theta'$ as an explicit function of $t$.

At $h = 500$: $t = 5.59$ s. $\sec^2\theta = 1.25$. $\theta' = (32 \times 5.59)/(1000 \times 1.25) \approx 0.143$ rad/s.

To find when $\theta'(t)$ peaks — when the camera's tilt-rate is fastest — differentiate $\theta'$ with respect to $t$ and set to zero. This is an optimization problem. The answer turns out to be at $t = 0$, at launch, when the angle sweeps fastest across the low flat part of its range. At high altitude, the rate slows regardless of how fast the rocket is climbing.

Linear approximation: if the current angular rate is $0.143$ rad/s, the angle 0.1 seconds from now is approximately $\theta + 0.143 \times 0.1 = \theta + 0.0143$ radians. Useful for a camera operator's tracking algorithm.

L'Hôpital: at $t = 0$, both $\theta$ and $t$ are zero, so the ratio $\theta(t)/t$ is $0/0$. L'Hôpital gives $\theta'(0)/1$, the initial angular rate.

Antiderivatives: if you know $\theta'(t)$ and want to recover $\theta(t)$, integrate. Chapter 5's machinery makes this systematic.

The derivative is not one tool. It's a family of tools — related rates, approximation, optimization, asymptotic analysis, root-finding, inversion — all expressing the same fundamental idea: the behavior of a changing quantity, to first order, near any given moment, is linear. Everything else follows from that.

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a collaborative thinking partner — asking it to check your reasoning, generate similar problems, or explain a step you're stuck on. The goal is to think alongside the tool, not to have the tool think for you.

**Exercise 1.** A spherical balloon is being inflated. Its radius is increasing at 3 cm/s. Ask an LLM to derive the rate at which the volume is increasing when the radius is 10 cm. Before looking at its work, write the equation $V = (4/3)\pi r^3$, differentiate with respect to time yourself, and substitute. Compare your derivation step-by-step with the LLM's. Did it correctly apply the chain rule, or did it treat $r$ as a constant?

**Exercise 2.** Ask an LLM to use linear approximation to estimate $\cos(0.1)$. Before seeing the response, anchor the approximation yourself at $a = 0$: what is $f(0)$ and $f'(0)$? Compute $L(0.1)$. Then ask the LLM to also estimate the error bound — how far can the true value deviate from the approximation? Evaluate whether its error analysis uses $f''$ correctly.

**Exercise 3.** Give an LLM this optimization problem: "A cylindrical can must hold 500 cubic centimeters. Find the radius and height that minimize the total surface area (including top and bottom lids)." Solve it yourself first using the constraint $\pi r^2 h = 500$ to eliminate $h$, then differentiating. Compare the LLM's setup. Did it use the constraint correctly, or did it differentiate a two-variable function?

**Exercise 4.** Ask an LLM to apply L'Hôpital's rule to evaluate $\lim_{x \to 1} (x^3 - 1)/(x^2 - 1)$. Before seeing its work, check whether the form is actually indeterminate at $x = 1$. Then evaluate the limit yourself both by factoring (no L'Hôpital needed) and by applying L'Hôpital. Compare the two methods' answers. Ask the LLM to confirm that both approaches agree, and to explain why factoring works here even when L'Hôpital does too.

**Exercise 5.** Run two iterations of Newton's method to solve $\cos x = x$ — find the fixed point where the function $f(x) = \cos x - x$ crosses zero. Start at $x_0 = 0.5$. Compute $x_1$ and $x_2$ by hand, then check your arithmetic with an LLM. Ask it to run two more iterations. How many decimal places are correct by $x_4$? Ask the LLM to explain geometrically what Newton's method is doing at each step.

**Exercise 6.** Ask an LLM to sketch (describe in words) the graph of $f(x) = x^4 - 4x^3$ by analyzing its derivatives. Conduct the analysis yourself first: find $f'(x)$, identify critical points, determine sign changes; find $f''(x)$, identify inflection points, determine concavity. Then compare your analysis to the LLM's. Did it identify all critical points? Did it correctly determine whether each is a local max, local min, or inflection point? Did it find the right inflection point(s)?

---

##  AI Wayback Machine
The ideas in this chapter didn't appear from nowhere. **Pierre de Fermat** developed methods for finding tangent lines and optimization extrema in the 1630s — predating Newton and Leibniz by a generation. His "method of adequality" is, in modern eyes, the derivative test with a different vocabulary.

**Run this:**

```
Who was Pierre de Fermat, and how does his method of adequality connect to the optimization applications of derivatives we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Pierre de Fermat"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to find a maximum using Fermat's method on one specific function — and translate the steps into modern derivative notation.
- Ask it about Fermat's day job as a magistrate, and how mathematics fit into a working lawyer's life.

What changes? What gets better? What gets worse?
