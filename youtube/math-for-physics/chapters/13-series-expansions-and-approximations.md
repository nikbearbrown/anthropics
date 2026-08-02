# Series, Expansions, and Approximations

*Why "assume a small angle" is really a Taylor truncation — and how it makes the unsolvable solvable*

## A pendulum whose equation cannot be solved

A pendulum is the most familiar oscillator there is, and yet its exact equation of motion is, in a precise sense, unsolvable. Newton's second law for the swinging bob gives

$$\ddot\theta = -\frac{g}{L}\sin\theta.$$

This looks almost like the harmonic-oscillator equation $\ddot\theta = -\omega^2\theta$ of Chapter 11 — but for the $\sin\theta$ where we want a plain $\theta$. That single trigonometric function ruins everything. The equation is *nonlinear*: doubling $\theta$ does not double $\sin\theta$, so the superposition that made the spring tractable fails. There is no solution in terms of the elementary functions you know; the exact period requires elliptic integrals, which have no closed form.

Every introductory course escapes this trap with one sentence: "For small angles, $\sin\theta \approx \theta$." Make that replacement and the equation becomes $\ddot\theta = -(g/L)\theta$, which *is* the harmonic oscillator, solved on sight, giving $T = 2\pi\sqrt{L/g}$. The escape works. But it is almost never explained. Why is $\sin\theta \approx \theta$? How small is "small"? What error are we committing, and when does it matter?

The honest answer is that "$\sin\theta \approx \theta$" is not a convenient fiction — it is the first term of an exact infinite series, the **Taylor series** of the sine, and "assume a small angle" means "keep the first term and throw the rest away." That move — approximating a complicated function by the first few terms of a polynomial — is one of the most powerful and most often-used tools in all of physics. It is the subject of this chapter. The pendulum is the doorway, and behind it sits the machinery that quietly underwrites Chapters 11 and 12 as well.

## The tool, named

A **sequence** is an ordered list of numbers; a **series** is their sum. The series we care about are **power series** — infinite sums of powers of $x$, $\sum_{n=0}^{\infty} c_n x^n$ — because a power series is a polynomial of infinite degree, and polynomials are the functions we know how to differentiate, integrate, and evaluate.

The central result is the **Taylor series**: any sufficiently smooth function $f$ can be reconstructed near a point $a$ from its value and all its derivatives there,

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}\,(x - a)^n.$$

When the expansion point is $a = 0$ it is called a **Maclaurin series**, and that is the form we use for $\sin x$, $\cos x$, and $e^x$. Three ideas organize the chapter:

1. **Deriving** the series for the functions physics needs, by repeated differentiation.
2. **Truncating** — keeping the first one or two terms — to get the **small-angle** and **binomial** approximations, with an honest account of the error.
3. **Convergence** at the level of intuition: when does adding more terms actually home in on the function, and over what range?

The judgment this chapter installs is not a calculation a computer makes for you. A machine can print the whole Taylor series; it cannot decide that $\theta = 5^\circ$ is "small enough" to drop the cubic term *for this problem*, nor recognize that expanding a potential about its minimum is the move that reveals simple harmonic motion. Knowing **when and to what order to truncate, and what you give up**, is the transferable skill.

## Development

### Building a Taylor series by repeated differentiation

The Taylor formula is not magic; it is the only polynomial that can match a function's value and all its derivatives at a point. Suppose we want a power series $f(x) = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + \cdots$ that agrees with $f$ near $x = 0$. Differentiate repeatedly and evaluate at $0$:

- $f(0) = c_0$, so $c_0 = f(0)$.
- $f'(x) = c_1 + 2c_2 x + 3c_3 x^2 + \cdots$, so $f'(0) = c_1$, giving $c_1 = f'(0)$.
- $f''(x) = 2c_2 + 6c_3 x + \cdots$, so $f''(0) = 2c_2$, giving $c_2 = f''(0)/2$.
- $f'''(0) = 6c_3$, giving $c_3 = f'''(0)/6 = f'''(0)/3!$.

The pattern is forced: the coefficient of $x^n$ must be $c_n = f^{(n)}(0)/n!$. That *is* the Maclaurin series, and we just derived it by demanding that the polynomial reproduce every derivative at the origin. The factorial $n!$ appears because differentiating $x^n$ that many times brings down $n\cdot(n-1)\cdots 1 = n!$.

### The three series physics lives on

**Sine.** The derivatives of $\sin x$ cycle: $\sin x \to \cos x \to -\sin x \to -\cos x \to \sin x$. At $x = 0$ they take the values $0, 1, 0, -1, 0, 1, \dots$ Only odd powers survive, with alternating sign:

$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

**Cosine.** The derivatives of $\cos x$ at $0$ are $1, 0, -1, 0, 1, \dots$ Only even powers survive:

$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$

**Exponential.** Every derivative of $e^x$ is $e^x$, which is $1$ at $x = 0$. So every coefficient is $1/n!$:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$

These three series are exact — they converge to the functions for *all* real $x$ — and they are the ones we borrowed in Chapter 12 to prove Euler's formula. (Substituting $x = i\theta$ into the exponential series and sorting by powers of $i$ produced $\cos\theta + i\sin\theta$; that derivation rested on exactly these three expansions. The back-reference is deliberate: this chapter conceptually *precedes* the complex-exponential chapter even though it sits after it.) They also underlie Chapter 11: the exponential series is what makes $e^{-\lambda t}$ a sensible object, and the growth/decay solutions live on it.

These series were first found not in Europe but in 14th-century Kerala: Mādhava of Sangamagrāma derived the sine, cosine, and arctangent expansions — with error terms — roughly 250 years before Newton and Taylor [verify]. The European names (Taylor 1715, Maclaurin 1742 for the $a=0$ case) attach to a result with a much older and more global lineage [contested — see pantry].

### Truncation: the small-angle approximation, derived and bounded

Now keep only the leading terms. From the sine series, dropping everything past the first term:

$$\sin\theta \approx \theta.$$

This is the small-angle approximation, and it is now *derived*, not asserted: it is the Maclaurin series of $\sin$ truncated after one term. The next term tells you the error you are committing. The first term you dropped is $-\theta^3/3! = -\theta^3/6$, so

$$\sin\theta = \theta - \frac{\theta^3}{6} + \cdots, \qquad \text{error of "}\sin\theta \approx \theta\text{"} \approx \frac{\theta^3}{6}.$$

This is the crucial point that lets us answer "how small is small?" — *with a number*. The relative error is roughly $(\theta^3/6)/\theta = \theta^2/6$. At $\theta = 15^\circ = 0.262$ rad, that is $0.262^2/6 \approx 0.011$, about 1%. At $\theta = 5^\circ$, it falls to about 0.1%. The approximation is not exact and not arbitrary: it is a controlled error that grows like $\theta^2$, and *you* decide whether that is tolerable for the job at hand. One warning that trips up everyone: the series, and therefore the approximation, holds only for $\theta$ in **radians**. Using degrees gives nonsense.

![The line y = θ and the curve y = sin θ drawn together over small angles, with the widening gap between them marked as the error θ³/6.](images/13-series-expansions-and-approximations-fig-02.png)
*Figure 13.2 — The small-angle approximation sin θ ≈ θ. Near zero the line and curve coincide; the gap (the dropped term ≈ θ³/6) grows with angle, giving a relative error ≈ θ²/6 — about 1% at 15°, 0.1% at 5°.*

Keeping the cosine to its first nontrivial term gives the companion result

$$\cos\theta \approx 1 - \frac{\theta^2}{2},$$

which is what you use whenever a problem needs the *height* a pendulum rises or the second-order correction to an energy.

### The binomial approximation

A second workhorse comes from Newton's generalized binomial theorem (c. 1665) [verify]:

$$(1 + x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \cdots \qquad (\text{any real } n).$$

This is itself a Taylor series — expand $f(x) = (1+x)^n$ about $0$ and you reproduce it. For small $x$, keep the first two terms:

$$(1 + x)^n \approx 1 + nx \qquad (|x| \ll 1).$$

This collapses square roots, reciprocals, and odd powers into simple linear estimates. For example $\sqrt{1 + x} = (1+x)^{1/2} \approx 1 + \tfrac{x}{2}$, and $\dfrac{1}{1 - x} = (1-x)^{-1} \approx 1 + x$. Physics is full of $\sqrt{1 \pm x}$ and $(1 \pm x)^n$ with a small $x$ — relativistic corrections, gravitational potentials far from a body, the next-order pendulum period — and the binomial approximation is how you tame them.

### Convergence, at the level you need

A power series is an *infinite* sum, and infinite sums can fail to settle on a value. The three series above converge for every $x$, but not all series are so generous. The geometric series

$$\frac{1}{1 - x} = 1 + x + x^2 + x^3 + \cdots$$

converges only for $|x| < 1$; feed it $x = 2$ and the partial sums $1, 3, 7, 15, \dots$ run off to infinity while the left side is a finite $-1$. Every power series has a **radius of convergence**: a range of $x$ around the expansion point within which adding terms homes in on the function, and outside which it diverges. For intro purposes you do not need the $\varepsilon$–$N$ machinery (that is the analysis course); you need the picture: a truncated Taylor series hugs the true curve near the expansion point and peels away from it farther out, and each extra term widens the region of good agreement. Truncation is trustworthy *near* the point and progressively untrustworthy away from it — which is exactly why "small angle" must be small.

![The curve y = sin x with its one-, two-, and three-term Taylor approximations; each truncation tracks the true curve farther from the origin before peeling away.](images/13-series-expansions-and-approximations-fig-01.png)
*Figure 13.1 — Taylor approximations of sin x converging. The one-term line y = x peels off first; adding terms widens the region of agreement, with the three-term polynomial tracking sin x furthest.*

## Worked examples

### Example 1 — Linearizing the pendulum, with the error attached

The exact equation $\ddot\theta = -(g/L)\sin\theta$ is nonlinear and unsolvable in elementary functions. Replace $\sin\theta$ by its one-term Taylor series:

$$\sin\theta \approx \theta \;\Longrightarrow\; \ddot\theta \approx -\frac{g}{L}\theta.$$

This is the harmonic oscillator of Chapter 11 with $\omega^2 = g/L$, instantly solved: $\theta(t) = \theta_0\cos\omega t$ and $T = 2\pi\sqrt{L/g}$. The truncation is the *entire reason* the pendulum has a clean period formula. And we can now say what we paid: for a release angle of $15^\circ$, the relative error in the linearized force is about 1%, so the period formula is good to that order. Release the pendulum at $45^\circ$ and the dropped $\theta^3$ term is no longer negligible — the true period is several percent longer than $2\pi\sqrt{L/g}$, and the harmonic model degrades. The approximation has a domain, and you now know its edge.

### Example 2 — The amplitude correction to the pendulum period

To see the next layer, keep the *cubic* term of the sine. Carrying the $-\theta^3/6$ correction through a careful expansion of the pendulum's motion yields the leading amplitude-dependent correction to the period [verify]:

$$T \approx 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{\theta_0^2}{16}\right).$$

The structure is exactly what the chapter predicts: the first correction is proportional to $\theta_0^2$, the same order as the squared-angle error we estimated. For $\theta_0 = 0.5$ rad ($\approx 29^\circ$), the correction factor is $1 + 0.25/16 \approx 1.016$, a 1.6% lengthening of the period — small, but measurable with a decent stopwatch, and a direct experimental confirmation that "small angle" was an *approximation* all along, not an identity.

### Example 3 — Why every smooth potential is harmonic near its minimum

Here is the deepest use of Taylor expansion in mechanics, and it explains why oscillation is *universal*. Take any potential energy $U(x)$ with a minimum at $x = x_0$. Expand it in a Taylor series about that minimum:

$$U(x) = U(x_0) + U'(x_0)(x - x_0) + \frac{1}{2}U''(x_0)(x - x_0)^2 + \cdots$$

At a minimum the slope vanishes, $U'(x_0) = 0$, so the linear term is gone. Drop the cubic and higher terms (legitimate for small displacements). Letting $u = x - x_0$,

$$U(x) \approx U(x_0) + \frac{1}{2}U''(x_0)\,u^2.$$

This is exactly the potential energy of a spring, $\tfrac12 k u^2$, with **effective spring constant** $k = U''(x_0)$ — the curvature of the potential at its minimum. The restoring force is $F = -dU/dx \approx -U''(x_0)\,u$, Hooke's law. So *any* system displaced slightly from a stable equilibrium oscillates simple-harmonically, regardless of how complicated its potential is, because the second-order Taylor term always looks like a spring. The harmonic oscillator of Chapter 11 is not a special case; it is what every smooth minimum becomes when you zoom in. A molecule vibrating in its interatomic potential, an atom in a crystal lattice, a marble in a bowl — all are springs to leading order, and the spring constant is a second derivative.

## Back to the pendulum

We began with a confession: the pendulum's exact equation $\ddot\theta = -(g/L)\sin\theta$ cannot be solved in elementary functions. The course's escape hatch — "$\sin\theta \approx \theta$" — turns out to be the first term of the sine's Taylor series, and "assume small angle" means "truncate after one term." With that single, honest approximation the nonlinear equation becomes the harmonic oscillator we already solved, and the period $T = 2\pi\sqrt{L/g}$ falls out. We can even quote the error (about 1% at $15^\circ$) and compute the next correction ($T$ grows like $1 + \theta_0^2/16$). The shortcut was never a fiction; it was a controlled truncation of an exact series, and recognizing it as such converts a memorized rule into a general technique.

That technique is the secret engine of the two preceding chapters. The exponential, sine, and cosine series proved Euler's formula in Chapter 12; the linearization-near-a-minimum is why Chapter 11's harmonic oscillator describes *everything* near stable equilibrium. Series are the connective tissue of Part III.

## Where it generalizes

Taylor approximation is the universal way to replace a hard function by an easy one over a limited range, and it appears wherever calculation must be done. Every calculator computes $\sin$, $\cos$, $e^x$, and logarithms by summing truncated series. Relativistic mechanics recovers the Newtonian kinetic energy $\tfrac12 mv^2$ as the first correction term in the binomial expansion of $mc^2/\sqrt{1 - v^2/c^2}$. Numerical methods for differential equations (Euler's method, Runge–Kutta) are built on Taylor steps. Economic and engineering models routinely linearize about an operating point — which is the small-angle move wearing a different hat. The general statement "a smooth function looks linear up close, and quadratic a little farther out" is the foundation of optimization, perturbation theory, and error analysis across every quantitative field.

The continuous analogue — representing a function not by powers of $x$ but by a sum of *sines and cosines* of many frequencies — is **Fourier series**, the subject of Chapter 14, and its further generalization to the **Fourier transform** belongs to **Volume 2**. What no software supplies is the judgment: which point to expand about, how many terms to keep, and whether the discarded terms are truly negligible *for the problem in front of you*. The machine can generate the series; deciding that $\theta = 5^\circ$ is small enough — and knowing it stops being small at $45^\circ$ — is the physicist's job, and the cleanest example in this book of math as judgment rather than computation.

## Exercises

1. **Derive a series.** Build the Maclaurin series of $\cos x$ from scratch by computing $f(0), f'(0), f''(0), \dots$ for $f(x) = \cos x$, and write out the first three nonzero terms. Then estimate $\cos(0.2)$ using those terms and compare to a calculator.

2. **How small is small? (derivation).** Using the next term of the sine series, derive the expression $\theta^2/6$ for the relative error of $\sin\theta \approx \theta$. Find the largest angle (in degrees) for which this approximation is good to better than 0.5%.

3. **Binomial in action.** Use $(1+x)^n \approx 1 + nx$ to estimate $\sqrt{1.02}$ and $1/\sqrt{0.98}$ without a calculator, then state the exact values and the error in each.

4. **Cosine correction.** A pendulum of length $L$ swings to a maximum angle $\theta_0$. Using $\cos\theta \approx 1 - \theta^2/2$, find an approximate expression for the height $h = L(1 - \cos\theta_0)$ the bob rises, and use it with energy conservation to estimate its maximum speed at the bottom.

5. **Every minimum is a spring (derivation).** A particle moves in the potential $U(x) = U_0\big[(x_0/x)^{12} - 2(x_0/x)^{6}\big]$ (a Lennard-Jones-type well) with a minimum at $x = x_0$. By Taylor-expanding $U$ about $x_0$ to second order, find the effective spring constant $k = U''(x_0)$ and hence the angular frequency of small oscillations of a mass $m$ in this well. (You may quote $U''(x_0) = 72\,U_0/x_0^2$ or derive it.)

## Sources

- Mādhava of Sangamagrāma (c. 1340–1425) and the Kerala school — power-series expansions of sine, cosine, arctangent, with error terms; transmitted through Nilakantha's *Tantrasangraha* and the *Yuktibhāṣā*. [verify]
- Brook Taylor, *Methodus Incrementorum Directa et Inversa* (1715) — the general Taylor expansion. [verify]
- Colin Maclaurin, *A Treatise of Fluxions* (1742) — the $a = 0$ (Maclaurin) special case. [verify]
- Isaac Newton, generalized binomial theorem (c. 1665; *Epistola prior*, 1676) — $(1+x)^n$ for real $n$. [verify]
- Joseph-Louis Lagrange, *Théorie des fonctions analytiques* (1797) — the remainder term that makes truncation rigorous. [verify]
- Source physics: *Oscillations* (small-angle pendulum, amplitude correction, oscillation near a potential minimum), retained physics chapter 17. Back-references to Chapters 11 and 12 of this book.
