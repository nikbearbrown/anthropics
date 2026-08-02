# Complex Numbers and Exponentials

*How an "impossible" number becomes the easiest language for oscillation*

## A phase that trig refuses to simplify

In the previous chapter the damped oscillator handed us a solution of the form

$$x(t) = A_0\,e^{-bt/2m}\cos(\omega t + \phi).$$

Two things are happening at once: the amplitude is *decaying* (the $e^{-bt/2m}$ factor) and the position is *oscillating* (the cosine). They are stapled together by multiplication, and whenever you want to combine two such oscillations — add the responses of two driven masses, or superpose two waves of the same frequency but different phase — you are forced into the thicket of trigonometric identities. Adding $A\cos(\omega t + \phi_1) + B\cos(\omega t + \phi_2)$ by the angle-sum formulas is a page of algebra that hides what is geometrically a simple thing.

Here is the deeper irritation. The decaying amplitude and the steady oscillation feel like two unrelated phenomena — one an exponential, one a sinusoid — yet they always travel together, and the characteristic equation of Chapter 11 produced them from a *single* complex root $r = -\tfrac{b}{2m} \pm i\omega$. That hint is the whole chapter. There is a number system in which decay and oscillation are not two things but one: the real part and the imaginary part of a single exponent. Master it, and the page of trig collapses to one line of arithmetic.

The number system is the **complex numbers**, and its central identity — Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ — is the most efficient tool in all of oscillation physics. The damped oscillator is the doorway. What looks like pure abstraction will turn out to be the most *practical* thing in the book.

## The tool, named

A **complex number** is a number of the form $z = a + bi$, where $a$ and $b$ are ordinary real numbers and $i$ is a symbol with the single defining property

$$i^2 = -1.$$

We call $a$ the **real part** ($\operatorname{Re} z$) and $b$ the **imaginary part** ($\operatorname{Im} z$). The names are historical accidents that actively mislead — there is nothing unreal about $i$; engineers even write it $j$ to avoid clashing with electric current. A complex number is simply a *pair* of reals carrying its own arithmetic, and that arithmetic is exactly what we need.

The chapter does three things:

1. Sets up complex **arithmetic** and the **complex plane**, where multiplication has a startling geometric meaning.
2. **Derives** Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ from power series — proves it, rather than asserting it.
3. Shows that a real oscillation is the **real part of a complex exponential**, $A\cos(\omega t + \phi) = \operatorname{Re}\!\big(Ae^{i\phi}e^{i\omega t}\big)$, and uses this to make oscillation problems trivial.

The discipline the whole chapter asks of you: **complexify to compute, then take the real part to interpret.** A computer multiplies complex numbers without thinking; the human decides to write the oscillation as an exponential in the first place, and remembers which physical quantity is the real part at the end.

## Development

### Arithmetic from one rule

Everything follows from $i^2 = -1$ and the ordinary rules of algebra. Addition is componentwise:

$$(a + bi) + (c + di) = (a + c) + (b + d)i.$$

Multiplication is the usual distribution, with $i^2$ replaced by $-1$ wherever it appears:

$$(a + bi)(c + di) = ac + adi + bci + bdi^2 = (ac - bd) + (ad + bc)i.$$

The one genuinely new move is *division*, handled by the **complex conjugate** $\bar z = a - bi$. Note that $z\bar z = (a+bi)(a-bi) = a^2 + b^2$, a real, non-negative number. So to divide, multiply top and bottom by the conjugate of the denominator:

$$\frac{1}{c + di} = \frac{c - di}{(c+di)(c-di)} = \frac{c - di}{c^2 + d^2}.$$

This is the trick that makes a complex amplitude — a single division — encode both the size and the phase lag of a driven oscillator, where the trig approach needs two separate calculations.

### The complex plane: where multiplication becomes rotation

Plot $z = a + bi$ as the point $(a, b)$ in a plane: horizontal axis for the real part, vertical for the imaginary. This is the **complex plane**, invented by the surveyor Caspar Wessel in 1799 (and named for Argand, who rediscovered it in 1806, and legitimized by Gauss) [verify]. A complex number is now an arrow from the origin, described equally well by its length and its direction:

$$r = |z| = \sqrt{a^2 + b^2} \quad (\text{modulus}), \qquad \theta = \operatorname{atan2}(b, a) \quad (\text{argument}).$$

In **polar form**, $a = r\cos\theta$ and $b = r\sin\theta$, so $z = r(\cos\theta + i\sin\theta)$.

![The complex number z = 3 + 2i drawn as an arrow in the complex plane, with its rectangular parts a and b, its modulus r, and its argument θ all marked.](images/12-complex-numbers-and-exponentials-fig-01.png)
*Figure 12.1 — One number, two descriptions: z = 3 + 2i as rectangular parts (a, b) = (3, 2) or as a length r = √13 at angle θ ≈ 33.7°.*

Now watch what multiplication does. Multiply two numbers in polar form, $z_1 = r_1(\cos\theta_1 + i\sin\theta_1)$ and $z_2 = r_2(\cos\theta_2 + i\sin\theta_2)$:

$$z_1 z_2 = r_1 r_2\big[(\cos\theta_1\cos\theta_2 - \sin\theta_1\sin\theta_2) + i(\sin\theta_1\cos\theta_2 + \cos\theta_1\sin\theta_2)\big].$$

The two parenthesized expressions are exactly the angle-sum identities for cosine and sine:

$$z_1 z_2 = r_1 r_2\big[\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)\big].$$

**Multiplying complex numbers multiplies their lengths and adds their angles.** Multiplication is a rotation-and-scaling. In particular, multiplying by $i$ (length 1, angle $90^\circ$) rotates any number a quarter turn counterclockwise: $i\cdot 1 = i$, $i\cdot i = -1$, $i\cdot(-1) = -i$, $i\cdot(-i)=1$ — a full circle in four steps. This single fact, that *rotation is multiplication*, is why complex numbers are the language of anything that goes around: oscillations, waves, alternating current.

### Euler's formula, derived

We can now prove the identity that ties the whole subject together. In Chapter 13 you will derive the Maclaurin series — the infinite-polynomial representations — of the three functions we need. We borrow the results here (this is the deliberate back-reference the book promises):

$$e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$$
$$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$
$$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

Euler's move (1748) was to put $x = i\theta$ into the exponential series [verify]. Using the powers of $i$ — $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, then repeating — compute term by term:

$$e^{i\theta} = 1 + i\theta + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!} + \frac{(i\theta)^4}{4!} + \cdots
= 1 + i\theta - \frac{\theta^2}{2!} - i\frac{\theta^3}{3!} + \frac{\theta^4}{4!} + \cdots$$

Sort the terms into those without $i$ (even powers) and those with $i$ (odd powers):

$$e^{i\theta} = \underbrace{\left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right)}_{\cos\theta} + i\underbrace{\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right)}_{\sin\theta}.$$

The two grouped series are precisely the series for cosine and sine. Therefore

$$\boxed{e^{i\theta} = \cos\theta + i\sin\theta.}$$

This is **Euler's formula**, and it is now *proved*, not announced. Set $\theta = \pi$ and it gives $e^{i\pi} = -1$, the celebrated identity $e^{i\pi} + 1 = 0$ — but the formula's worth is not its beauty; it is what it does to oscillation.

Two immediate consequences. First, polar form becomes compact: any complex number is $z = re^{i\theta}$. Multiplication is then obvious from the exponent rule, $z_1 z_2 = r_1 r_2 e^{i(\theta_1+\theta_2)}$ — lengths multiply, angles add, exactly as we found. Second, $e^{i\theta}$ traces the **unit circle**: as $\theta$ runs from $0$ to $2\pi$, the point $(\cos\theta, \sin\theta)$ goes once around. A number $e^{i\omega t}$, with $\theta = \omega t$ growing in time, is a point circling the origin at angular rate $\omega$ — a **rotating phasor**.

![On the left, a phasor on the unit circle at angle θ; on the right, the cosine curve traced by the phasor's horizontal projection.](images/12-complex-numbers-and-exponentials-fig-02.png)
*Figure 12.2 — Euler's formula e^{iθ} = cos θ + i sin θ on the unit circle. The phasor's horizontal shadow (the real part) traces out cos θ — rotation projected into oscillation.*

### Oscillation as the real part of a phasor

Here is the payoff. Cosine is the horizontal shadow of a point going around a circle. Formally, since $e^{i\omega t} = \cos\omega t + i\sin\omega t$,

$$\cos\omega t = \operatorname{Re}\big(e^{i\omega t}\big), \qquad \sin\omega t = \operatorname{Im}\big(e^{i\omega t}\big).$$

A general oscillation with amplitude $A$ and phase $\phi$ is the real part of a single complex exponential:

$$A\cos(\omega t + \phi) = \operatorname{Re}\big(Ae^{i\phi}\,e^{i\omega t}\big) = \operatorname{Re}\big(\tilde A\, e^{i\omega t}\big),$$

where $\tilde A = Ae^{i\phi}$ is the **complex amplitude** — one complex number that carries *both* the size $A$ and the phase $\phi$ of the oscillation. Decay, too, folds in: a complex exponent $r = -\gamma + i\omega$ gives

$$e^{rt} = e^{(-\gamma + i\omega)t} = e^{-\gamma t}\big(\cos\omega t + i\sin\omega t\big),$$

whose real part is $e^{-\gamma t}\cos\omega t$ — *decaying oscillation in one symbol.* The exponent's real part ($-\gamma$) is the decay; its imaginary part ($\omega$) is the rotation. This is exactly the underdamped solution of Chapter 11, and now we see why the characteristic equation's complex root meant an oscillation: the imaginary part *is* the angular frequency.

## Worked examples

### Example 1 — Bombelli's cubic: imaginary numbers earning a real answer

Complex numbers entered mathematics not from geometry but as an unavoidable step in *real* algebra. In 1572, Rafael Bombelli studied the cubic $x^3 = 15x + 4$, which plainly has the real root $x = 4$ (check: $64 = 60 + 4$). Yet Cardano's solution formula produces

$$x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}.$$

The square root of a negative number — Cardano had called such things "as subtle as they are useless." Bombelli pressed on. Write $\sqrt{-121} = 11i$. He then guessed that $\sqrt[3]{2 + 11i} = 2 + i$, which we can verify with our arithmetic: $(2+i)^3 = (2+i)(2+i)(2+i)$. First $(2+i)^2 = 4 + 4i + i^2 = 3 + 4i$; then $(3+4i)(2+i) = 6 + 3i + 8i + 4i^2 = 2 + 11i$. ✓ Likewise $\sqrt[3]{2 - 11i} = 2 - i$. So

$$x = (2 + i) + (2 - i) = 4.$$

The imaginary parts cancel and leave the true real root. This is the historical case that made imaginary numbers *respectable*: they are honest intermediates that deliver correct real answers. The lesson for the physicist is identical — complexify in the middle, take the real part at the end.

### Example 2 — Adding two oscillations the easy way

Two driven motions of the same frequency, $x_1 = 3\cos(\omega t)$ and $x_2 = 4\cos(\omega t + 90^\circ)$, are to be added. By trig identities this is a chore. By phasors it is a single addition of arrows. Write each as a complex amplitude:

$$\tilde A_1 = 3e^{i0} = 3, \qquad \tilde A_2 = 4e^{i\pi/2} = 4i.$$

Add: $\tilde A = 3 + 4i$. Its modulus and argument are

$$|\tilde A| = \sqrt{3^2 + 4^2} = 5, \qquad \phi = \operatorname{atan2}(4, 3) \approx 53.1^\circ.$$

So the sum is $x_1 + x_2 = 5\cos(\omega t + 53.1^\circ)$. The amplitude and phase fell out of one right-triangle calculation in the complex plane — the same $3$-$4$-$5$ geometry you have known since trigonometry. This phasor-addition trick is the daily bread of AC-circuit analysis and wave interference.

### Example 3 — The underdamped oscillator in one exponent

Recall the underdamped characteristic roots from Chapter 11: $r = -\tfrac{b}{2m} \pm i\omega'$, with $\omega' = \sqrt{\omega_0^2 - (b/2m)^2}$. The solution is a combination of $e^{rt}$ for the two roots; taking the physically real combination,

$$x(t) = \operatorname{Re}\big(\tilde A\,e^{(-b/2m + i\omega')t}\big) = A_0\,e^{-bt/2m}\cos(\omega' t + \phi).$$

This is exactly the source-chapter formula — but now derived, not posited. The real part of the exponent, $-b/2m$, sets the decay envelope $A_0 e^{-bt/2m}$; the imaginary part, $\omega'$, sets the oscillation. Plotted in the complex plane, $e^{rt}$ is a point spiraling *inward* toward the origin: rotating (the oscillation) while shrinking (the decay). The decaying sinusoid and the inward spiral are the same object seen on two different screens — the real-axis projection and the full plane.

## Back to the phase that trig refused to simplify

We began stuck: a decaying, oscillating, phase-shifted motion that resisted combination because trigonometry treats amplitude-decay and oscillation as separate species and phase shifts as occasions for identity-juggling. Complex exponentials dissolve all three difficulties at once. Decay and oscillation become the real and imaginary parts of a single exponent $-\gamma + i\omega$. A phase shift becomes a factor $e^{i\phi}$ absorbed into a complex amplitude. Adding two oscillations becomes adding two arrows. The page of trig identities we dreaded is replaced by ordinary complex arithmetic, and at the very end we take the real part to recover the physical motion.

That is the chapter's claim made good: the "imaginary" number is not a physics gimmick but the most efficient *real* tool available for oscillation. The abstraction pays for itself within the same chapter that introduces it.

## Where it generalizes

Once you see that rotation is multiplication and oscillation is the real part of an exponential, the tool is everywhere. **De Moivre's theorem**, $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$, follows in one line from $z^n = r^n e^{in\theta}$ and computes powers and roots effortlessly; the $n$th roots of unity, $e^{2\pi ik/n}$, are equally spaced points on the unit circle and reappear as the natural frequencies of **Chapter 14**'s Fourier analysis. In electrical engineering, the entire theory of AC circuits is complex arithmetic on phasors (impedance is a complex resistance). In quantum mechanics, the wavefunction is *intrinsically* complex — there is no taking-the-real-part at the end; the imaginary part is physical. In signal processing, the complex exponential is the elementary building block of every signal. The deeper structures — analytic functions, contour integration, the residue theorem — belong to **Volume 2**.

What no software supplies is the decision to complexify and the discipline to interpret. A calculator multiplies $(2+i)(3-i)$ instantly; it cannot decide that a phase-lagged oscillation *should* be written $e^{i\omega t}$, cannot know which physical quantity is the real part, and cannot read the modulus as an amplitude and the argument as a phase. Rotation-is-multiplication and oscillation-is-the-real-part-of-an-exponential are conceptual moves — and they are exactly what carry, unchanged, into every field that deals with anything that cycles.

## Exercises

1. **Arithmetic.** Compute $(3 + 2i)(1 - 4i)$ and $\dfrac{1}{2 + i}$, writing each answer in the form $a + bi$. Then find the modulus and argument of $3 + 2i$.

2. **Rotation by $i$.** Take the point $z = 2 + i$ and compute $iz$, $i^2 z$, $i^3 z$, $i^4 z$. Plot all five points and confirm that multiplication by $i$ rotates $z$ by $90^\circ$ each time, returning to the start after four multiplications.

3. **Euler's formula (derivation).** Starting from the Maclaurin series for $e^x$, substitute $x = i\theta$, use the cycle of powers of $i$, and separate the real and imaginary terms to derive $e^{i\theta} = \cos\theta + i\sin\theta$. Then evaluate $e^{i\pi/2}$ and $e^{i\pi}$ and interpret each as a point on the unit circle.

4. **Phasor addition.** Add $5\cos(\omega t)$ and $5\cos(\omega t + 120^\circ)$ by converting each to a complex amplitude, summing, and converting back to a single amplitude-and-phase cosine. Compare the labor to doing it with the cosine angle-sum identity.

5. **Decay-and-oscillation.** A complex exponent is $r = -0.5 + 3i$ (units s$^{-1}$). Write $\operatorname{Re}(e^{rt})$ as an explicit decaying cosine, identify the decay rate and the angular frequency, and sketch the curve and the corresponding inward spiral in the complex plane.

## Sources

- Gerolamo Cardano, *Ars Magna* (1545) — cubic/quartic solutions; square roots of negatives as "subtle and useless." [verify]
- Rafael Bombelli, *L'Algebra* (1572) — the cubic $x^3 = 15x + 4$ showing imaginary intermediates yielding a real root. [verify]
- Leonhard Euler, *Introductio in analysin infinitorum* (1748), Book I, Ch. 7–8 (Euler Archive E101) — $e^{i\theta} = \cos\theta + i\sin\theta$ from the power series. [verify]
- Caspar Wessel, "Om Directionens analytiske Betegning" (1799), and Jean-Robert Argand, *Essai* (1806) — the geometric (complex-plane) interpretation; term "complex number" and full legitimacy due to Gauss (1831). [verify]
- Source physics: *Oscillations* (damped and driven oscillation, phase), retained physics chapter 17. Forward reference to series in Chapter 13 of this book.
