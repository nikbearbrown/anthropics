# Differential Equations and Oscillatory Motion

*When the unknown is a function, not a number — and the equation tells you its rate of change*

## A mass that knows where it will be

Pull a mass on a spring out to a distance $A$ from rest, hold it, and let go. You know, before releasing it, roughly what will happen: it will rush back through the middle, overshoot, swing out the far side, and come back — over and over, ticking like a metronome. The question is precise: *where is the mass at time $t$?* Not where it is now, not its average position, but its exact location at every future instant.

The physics gives you a relation, but a strange one. Hooke's law says the spring pulls back in proportion to how far the mass is displaced: $F = -kx$. Newton's second law says force is mass times acceleration: $F = ma$. And acceleration is the second time-derivative of position, $a = \ddot{x}$. Put them together:

$$m\ddot{x} = -kx, \qquad \text{or} \qquad \ddot{x} = -\frac{k}{m}\,x.$$

Stare at this for a moment, because it is unlike every equation in the earlier chapters. It does not say "$x$ equals some number." It says: *the second derivative of $x$ is proportional to the negative of $x$ itself.* The unknown is not a number — it is the entire function $x(t)$, the whole history of the motion. And the equation does not hand you that function; it hands you a relationship the function must satisfy. We are asked to find a function whose second derivative is, up to a negative constant, the function we started with.

That is a **differential equation**, and learning to solve it is the subject of this chapter. The mass on a spring is the doorway, but the same equation will turn out to govern pendulums, atoms, AC circuits, and quantum oscillators — every system that returns toward equilibrium when pushed away from it.

## The tool, named

A **differential equation** (ODE, for *ordinary* differential equation, when there is a single independent variable like time) is an equation relating an unknown function to its own derivatives. Its **solution** is a function — in fact a whole *family* of functions, narrowed to one specific motion only when you supply **initial conditions** (where the mass starts and how fast).

We will handle two kinds:

- **First-order, separable** equations, of the form $\dfrac{dy}{dt} = (\text{function of } y)\times(\text{function of } t)$. These describe exponential growth and decay, and they are the gentlest introduction because you solve them by ordinary integration.
- **Second-order, linear, constant-coefficient** equations, of which $\ddot{x} = -\omega^2 x$ is the headline example. These describe oscillation, and we solve them by the **characteristic-equation method**.

Two ideas run through everything. First, the **order** of an equation is the highest derivative it contains; Newton's law is second order because acceleration is a second derivative — *the physics is what makes the equation second order*. Second, you can always **check a proposed solution by substituting it back in and differentiating** — which turns "guessing the answer" from an act of faith into a verifiable step.

A note on notation. The derivative of $x$ with respect to time is written three ways: Newton's dot $\dot{x}$, Leibniz's $\frac{dx}{dt}$, and Lagrange's prime $x'$. They mean the identical thing. We will use the dot for time derivatives (the physicist's habit) and $\frac{d}{dt}$ when the operation needs emphasis.

## Development: the simplest ODE first

### Separable first-order equations: exponential decay

Before the spring, solve something easier whose answer you can *derive* by integrating, so that the harder problem feels less like magic. Many physical quantities change at a rate proportional to how much of them is left: radioactive nuclei decay, a charged capacitor discharges through a resistor, a hot cup cools toward room temperature. All obey

$$\frac{dN}{dt} = -\lambda N,$$

where $N(t)$ is the amount remaining and $\lambda > 0$ is a rate constant. This is *separable*: every $N$ can be moved to one side, every $t$ to the other. Divide by $N$ and multiply by $dt$:

$$\frac{dN}{N} = -\lambda\,dt.$$

Now integrate both sides — the left over $N$, the right over $t$:

$$\int \frac{dN}{N} = -\lambda \int dt \;\Longrightarrow\; \ln N = -\lambda t + C,$$

where $C$ is a constant of integration. Exponentiate to free $N$:

$$N(t) = e^{-\lambda t + C} = e^{C}e^{-\lambda t}.$$

The constant $e^C$ is just the value of $N$ at $t = 0$, call it $N_0$. So

$$\boxed{N(t) = N_0\,e^{-\lambda t}.}$$

This is the **exponential-decay law**, and we *derived* it — no formula pulled from a hat. Check it by differentiating: $\dot N = -\lambda N_0 e^{-\lambda t} = -\lambda N$. It satisfies the equation. The **half-life** — the time for $N$ to fall to half — comes from $N_0/2 = N_0 e^{-\lambda t_{1/2}}$, giving $t_{1/2} = \dfrac{\ln 2}{\lambda}$.

Three lessons travel with you from this small example: (1) the solution is a *function*, not a number; (2) the constant of integration is fixed by an *initial condition*; (3) you *verify* by substituting back. All three return immediately for the spring.

### Second-order: solving $\ddot{x} = -\omega^2 x$

Write the spring equation with $\omega^2 \equiv k/m$, so that $\omega$ (units: radians per second) is the **natural angular frequency**:

$$\ddot{x} = -\omega^2 x.$$

We need a function whose second derivative is itself, scaled by $-\omega^2$. We know two such functions from trigonometry: differentiate $\cos\omega t$ twice and you get $-\omega^2\cos\omega t$; the same for $\sin\omega t$. Let us *verify* rather than assert. Propose

$$x(t) = A\cos\omega t + B\sin\omega t,$$

for arbitrary constants $A, B$. Differentiate once:

$$\dot{x} = -A\omega\sin\omega t + B\omega\cos\omega t.$$

Differentiate again:

$$\ddot{x} = -A\omega^2\cos\omega t - B\omega^2\sin\omega t = -\omega^2(A\cos\omega t + B\sin\omega t) = -\omega^2 x.$$

It checks. The proposed function satisfies the equation for *any* $A$ and $B$ — that two-constant freedom is exactly right for a second-order equation (a second derivative needs two integrations, hence two constants). This is the **general solution**.

Why two constants, and why does the sum work? Because the equation is **linear**: if $x_1$ and $x_2$ are each solutions, so is any combination $Ax_1 + Bx_2$. Linearity buys **superposition** — the single most important property in this book, and the foundation of everything in Chapter 14. Daniel Bernoulli applied it to vibrating strings, stating the superposition principle formally in 1753.

### Pinning down the constants with initial conditions

The general solution is a family. The actual motion is one member, selected by the starting state. Our mass is released *from rest* at displacement $A$: that is, $x(0) = A$ and $\dot{x}(0) = 0$. Apply them:

- $x(0) = A\cos 0 + B\sin 0 = A$. ✓ (consistent with our naming $A$ the amplitude)
- $\dot{x}(0) = -A\omega\sin 0 + B\omega\cos 0 = B\omega = 0 \;\Rightarrow\; B = 0.$

So for *this* release the motion is $x(t) = A\cos\omega t$ — a pure cosine, starting at the far point with zero velocity. Different initial conditions pick different members of the family; the equation is the same. **The solver gives you the family; the physics gives you the member.**

The period follows because cosine repeats every $2\pi$ radians of phase: $\omega T = 2\pi$, so

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}.$$

Notice what is *not* in this formula: the amplitude $A$. The period of a simple harmonic oscillator is independent of how far you pull it — the secret behind every pendulum clock. A stiffer spring (larger $k$) or a lighter mass (smaller $m$) means a higher $\omega$ and a shorter period: the oscillation is *faster*. That interpretive sentence is something a computer-algebra system, which would spit out $A\cos\omega t + B\sin\omega t$ in a blink, cannot supply.

![The harmonic-oscillator solution x(t) = A cos(ωt): a cosine curve with its amplitude A and period T marked.](images/11-differential-equations-and-oscillatory-motion-fig-01.png)
*Figure 11.1 — The solution x(t) = A cos(ωt). The amplitude A is set by the release; the period T = 2π/ω is set by ω alone — independent of how far the mass is pulled.*

### The characteristic-equation method: the general engine

The cosine-and-sine guess works for the undamped spring, but it does not obviously generalize. There is a systematic method, due to Euler in the 1740s [verify], that handles every constant-coefficient linear ODE: **assume an exponential solution and reduce the calculus to algebra.** Take the damped oscillator, the next equation up, which includes a friction force $-b\dot{x}$ proportional to velocity:

$$m\ddot{x} + b\dot{x} + kx = 0.$$

Try $x(t) = e^{rt}$ for some (possibly complex) number $r$. Then $\dot{x} = re^{rt}$ and $\ddot{x} = r^2 e^{rt}$. Substitute:

$$m r^2 e^{rt} + b r e^{rt} + k e^{rt} = 0.$$

Since $e^{rt}$ is never zero, divide it out and you are left with a plain quadratic — the **characteristic equation**:

$$m r^2 + b r + k = 0, \qquad r = \frac{-b \pm \sqrt{b^2 - 4mk}}{2m}.$$

The entire behavior of the oscillator is now read off the discriminant $b^2 - 4mk$:

- **Underdamped** ($b^2 < 4mk$): the roots are a *complex* pair, $r = -\tfrac{b}{2m} \pm i\omega'$. The motion is a decaying oscillation, $x(t) = A_0 e^{-bt/2m}\cos(\omega' t + \phi)$ — exactly the source-chapter result. (Why a complex root means an oscillation is the story of Chapter 12.)
- **Critically damped** ($b^2 = 4mk$): one *repeated real* root. The mass returns to equilibrium as fast as possible without overshooting — the design target for car shock absorbers.
- **Overdamped** ($b^2 > 4mk$): two *distinct real* roots, both negative. Sluggish, non-oscillating return.

Three physical regimes, three cases of a quadratic's roots. The characteristic equation has converted a question about motion into a question about where a parabola crosses zero — calculus traded for algebra. Set $b = 0$ and the roots become $r = \pm i\omega$ purely imaginary, recovering the undamped cosine-and-sine solution. The method contains the special case.

![Three displacement-versus-time curves: an underdamped curve oscillating inside a decaying envelope, a critically damped curve returning quickly without overshoot, and an overdamped curve returning slowly.](images/11-differential-equations-and-oscillatory-motion-fig-02.png)
*Figure 11.2 — The three damping regimes. The sign of the discriminant b² − 4mk decides whether the mass oscillates inside a decaying envelope (underdamped), returns fastest without overshoot (critically damped), or returns sluggishly (overdamped).*

## Worked examples

### Example 1 — Period of the mass on a spring

A $2.00$ kg mass on a spring of constant $k = 32.0$ N/m is pulled to $x = 0.020$ m and released from rest. The equation of motion is $\ddot{x} = -(k/m)x = -16.0\,x$, so $\omega = \sqrt{k/m} = \sqrt{16.0} = 4.00$ rad/s. With the release-from-rest initial conditions, $x(t) = (0.020\ \text{m})\cos(4.00\,t)$. The period is

$$T = \frac{2\pi}{\omega} = \frac{2\pi}{4.00} = 1.57\ \text{s},$$

independent of the $0.020$ m amplitude. Differentiating the solution gives the velocity $v(t) = -(0.080\ \text{m/s})\sin(4.00\,t)$ and acceleration $a(t) = -(0.32\ \text{m/s}^2)\cos(4.00\,t)$; note $a(t) = -16.0\,x(t)$ at every instant — the defining signature $\ddot{x} = -\omega^2 x$ made visible.

### Example 2 — The pendulum: the same equation in a new costume

A bob of mass $m$ on a string of length $L$ swings through angle $\theta$. Newton's second law for rotation, $\tau = I\ddot\theta$ with $I = mL^2$ and restoring torque $\tau = -mgL\sin\theta$, gives

$$mL^2\ddot\theta = -mgL\sin\theta \;\Longrightarrow\; \ddot\theta = -\frac{g}{L}\sin\theta.$$

This is *not* yet the harmonic-oscillator equation — the $\sin\theta$ makes it nonlinear and unsolvable in elementary functions. But for small swings, $\sin\theta \approx \theta$ (a Taylor truncation, the business of Chapter 13), and the equation **linearizes** to

$$\ddot\theta = -\frac{g}{L}\theta.$$

This is identical in form to the spring, with $\omega^2 = g/L$. We have already solved it: $\theta(t) = \theta_0\cos\omega t$, with period

$$T = 2\pi\sqrt{\frac{L}{g}}.$$

The point is structural: the harmonic-oscillator equation $\ddot{u} = -\omega^2 u$ is a *form*, not a single physical system. Solve it once and you have solved it for the spring ($u = x$, $\omega^2 = k/m$), the pendulum ($u = \theta$, $\omega^2 = g/L$), the LC circuit, and the vibrating molecule. The constants change; the mathematics does not.

### Example 3 — Radioactive decay, end to end

A sample of a radioisotope has decay constant $\lambda = 0.10\ \text{yr}^{-1}$. From the separable equation $\dot N = -\lambda N$ we derived $N(t) = N_0 e^{-\lambda t}$. The half-life is

$$t_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{0.10} \approx 6.93\ \text{yr}.$$

After 20 years, the fraction remaining is $N/N_0 = e^{-0.10\times 20} = e^{-2.0} \approx 0.135$ — about 13.5%, a little under two half-lives' worth. The same equation, with $\lambda$ reinterpreted as $1/RC$, gives the voltage on a discharging capacitor; with $\lambda$ as a cooling rate, Newton's law of cooling. One separable ODE, many physical clothes.

## Back to the mass on the spring

We asked: *where is the mass at time $t$?* The answer is the function $x(t) = A\cos\omega t$ with $\omega = \sqrt{k/m}$ — and we did not look it up; we *derived* it, verified it by double differentiation, and selected the cosine (rather than a sine, or some mix) by feeding in the physical fact that the mass started at rest. The period formula $T = 2\pi\sqrt{m/k}$ that you might once have memorized is now visibly a *consequence*: it is the period of a cosine whose phase advances at rate $\omega$.

That is the chapter's whole claim. "Solving the physics" of a spring *is* solving a differential equation. The equation $m\ddot{x} = -kx$ is not scaffolding around the real physics; it is the real physics, written in the only language that can express "the force depends on where you are, and the force determines how the position changes." Everything downstream — the period, the energy, the resonance of Chapter 17's Tacoma Narrows bridge — flows from this one solved equation.

## Where it generalizes

The reach of differential equations is hard to overstate, because the relation "the rate of change of a quantity depends on the quantity itself" is the natural law of almost everything that evolves. Exponential growth and decay (the separable equation) model populations, compound interest, drug clearance, and the cooling of stars. The harmonic-oscillator equation (the linear second-order equation) models not just springs and pendulums but the current in radio circuits, the vibration of atoms in a crystal lattice, and — with $\omega$ reinterpreted — the standing waves of a quantum particle in a box. The characteristic-equation method handles any constant-coefficient linear ODE, and its complex roots are the bridge to **Chapter 12**, where we will see *why* a complex exponent encodes a decaying oscillation. The small-angle move that rescued the pendulum is the **Chapter 13** business of Taylor approximation. And the leap from one oscillator to a continuum of coupled oscillators — a wave — is **Chapter 14**.

What a solver cannot do is the part that matters: decide that the force is $-kx$ in the first place, supply the physical initial conditions, and read meaning out of the answer. The computer returns $A\cos\omega t + B\sin\omega t$; you have to know that a stiffer spring oscillates faster, that "released from rest" means $B = 0$, and that the missing amplitude in the period formula is the reason clocks keep time. That interpretive judgment is the transferable skill — and it carries, unchanged, to every field that watches something change.

## Exercises

1. **Verify a solution.** Show by direct substitution that $x(t) = 3\cos(2t) - 4\sin(2t)$ satisfies $\ddot{x} = -4x$. Then find the single initial condition pair $x(0),\ \dot{x}(0)$ that this solution represents.

2. **Separable practice.** Solve $\dfrac{dy}{dt} = -3y$ with $y(0) = 5$ by separating variables and integrating. State the value of $y$ at $t = 1$ and the half-life.

3. **Read off the period.** A $0.50$ kg mass on a vertical spring stretches it $0.10$ m to a new equilibrium when hung. Find the spring constant from the equilibrium condition $kx_0 = mg$, then the angular frequency and period of small oscillations about that equilibrium. Does the period depend on how far you then pull the mass? Explain.

4. **The characteristic equation (derivation).** Starting from the damped-oscillator equation $m\ddot{x} + b\dot{x} + kx = 0$, substitute the trial solution $x = e^{rt}$ and derive the characteristic equation. For $m = 1$ kg, $k = 100$ N/m, find the value of $b$ that makes the system critically damped, and state the repeated root $r$.

5. **One form, two systems.** Show that both the spring equation $\ddot{x} = -(k/m)x$ and the small-angle pendulum equation $\ddot\theta = -(g/L)\theta$ have the form $\ddot{u} = -\omega^2 u$. Identify $\omega$ in each case, write the period of each, and explain in two sentences why solving one equation solves both.

## Sources

- Isaac Newton, *Philosophiæ Naturalis Principia Mathematica* (1687) — second law and fluxion (derivative) notation; the seed of the restoring-force equation. [verify]
- Robert Hooke, *Lectures de Potentia Restitutiva* (1678), "ut tensio sic vis" — the linear force law $F = -kx$. [verify]
- Leonhard Euler, "De integratione aequationum differentialium altiorum graduum" (1743, Euler Archive E62) — the exponential substitution $x = e^{rt}$ reducing a linear ODE to its characteristic equation. [verify]
- Daniel Bernoulli, vibrating-string work — formal statement of superposition for linear oscillation, 1753 (partial-tone recognition 1741–43, pub. 1751).
- MIT OpenCourseWare 8.03 *Vibrations and Waves*, Ch. 1, and UT Austin "Mass on Spring" notes — modern derivations of $\ddot{x} = -\omega^2 x$ and its solution.
- Source physics: *Oscillations* (mass on a spring, damped oscillator, simple pendulum) and *Gravitation*, retained physics chapters 17 and 14.
