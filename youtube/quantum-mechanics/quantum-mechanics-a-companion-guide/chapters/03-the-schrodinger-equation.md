# Chapter 3 — The Schrödinger Equation


## TL;DR

- The dynamical law of quantum mechanics was guessed, not proved.
- The chapter moves through The plausibility argument, The Born rule: what $|\psi|^2$ means, Normalization is preserved, and why Hermiticity is the reason, Stationary states, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The dynamical law of quantum mechanics was guessed, not proved. Here is what it says, why it works, and what it refuses to tell you.*

---

In late 1925, Erwin Schrödinger took a Christmas vacation in the Swiss Alps, at the Villa Herwig in Arosa, and came back down the mountain in January 1926 with an equation. Walter Moore's biography (*Schrödinger: Life and Thought*, Cambridge University Press, 1989) [*verify exact chapter*] describes the visit; the physics folklore fills in colorful details about who accompanied him. What is not in doubt is the result. Four papers appeared in *Annalen der Physik* beginning in January 1926 [Schrödinger, *Ann. Phys.* 79, 361–376](https://doi.org/10.1002/andp.19263840404), and within months they had reproduced every known energy level of hydrogen, explained the selection rules for atomic transitions, and given physicists a formalism they could actually use.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-schrodinger-equation-assertions.md -->

Heisenberg, Born, and Jordan had reached the same physics six months earlier through matrix mechanics. But matrix mechanics looked like nothing classical physicists had seen before — arrays of numbers following unfamiliar multiplication rules. Schrödinger's wave equation looked like a wave equation, and physicists are comfortable with wave equations. The wave-equation formulation became the standard entry point almost immediately, and it remains so now.

Here is where we are in the story. Unit 1 gave you the experimental evidence that forced quantum mechanics to exist: Planck's blackbody radiation, the photoelectric effect, the Compton scattering, de Broglie's matter waves, the Franck–Hertz experiment. Unit 2 gave you the mathematical apparatus: complex Hilbert spaces, inner products, Hermitian operators, eigenvalue equations. What is missing is a *dynamical law* — a rule that says how a quantum state changes in time. Classical mechanics has Newton's $\vec{F} = m\vec{a}$. Quantum mechanics needs its analog. The Schrödinger equation is it.

But — and this is the move this chapter has to make honestly — *the Schrödinger equation cannot be derived.* Griffiths says this directly in §1.1 of the third edition: "Where did Schrödinger's equation come from? In a sense, it cannot be derived." There is a plausibility argument that makes the equation look natural given what de Broglie and Einstein told us. The plausibility argument is worth running. But running it is not the same as deriving the equation. The Schrödinger equation has the same status as Newton's second law: a fundamental postulate that we accept because of what it explains, not because we have a deeper theory it follows from. Asking why nature uses this equation rather than some neighboring one is a question without a deeper answer inside non-relativistic quantum mechanics.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/03-the-schrodinger-equation-assertions.md -->

---

## The plausibility argument

Take de Broglie's matter wave for a free particle moving in the $+x$ direction:

$$\psi(x,t) = A\,e^{i(kx - \omega t)}, \qquad p = \hbar k, \qquad E = \hbar\omega.$$

Differentiate once in $t$:

$$\frac{\partial\psi}{\partial t} = -i\omega\,\psi = -\frac{iE}{\hbar}\psi \implies i\hbar\frac{\partial\psi}{\partial t} = E\psi.$$

Differentiate twice in $x$:

$$\frac{\partial^2\psi}{\partial x^2} = -k^2\psi = -\frac{p^2}{\hbar^2}\psi \implies -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} = \frac{p^2}{2m}\psi.$$

For a free particle, $E = p^2/2m$. So the two sides of the last two equations must be equal, and you get the free-particle equation:

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}.$$

Add a potential energy $V(x,t)$ — kinetic plus potential equals total energy, the oldest story in classical mechanics — and you arrive at the *time-dependent Schrödinger equation*:

$$\boxed{\;i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x,t)\,\psi(x,t).\;}$$

In operator language, with the Hamiltonian $\hat{H} = \hat{p}^2/2m + V(\hat{x},t)$ and the momentum operator $\hat{p} = -i\hbar\,\partial_x$ from Unit 2:

$$i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi.$$

![Anatomy of the time-dependent Schrödinger equation ](../images/03-the-schrodinger-equation-fig-01.png)
*Figure 3.1 — Anatomy of the time-dependent Schrödinger equation *

Three features the argument assembles but does not *prove*:

The equation is **linear**: if $\psi_1$ and $\psi_2$ are solutions, then $\alpha\psi_1 + \beta\psi_2$ is a solution. This is the superposition principle, and it is the algebraic origin of interference. You do not get interference from nonlinear wave equations.

The equation is **first-order in time**: specifying $\psi$ at one instant determines it at all later times. The classical wave equation $\partial_t^2\psi = c^2\partial_x^2\psi$ is second-order in time and needs both $\psi$ and $\partial_t\psi$ at $t = 0$. The Schrödinger equation needs only $\psi$.

The equation has **the factor of $i$**: without it, the equation becomes $\partial_t\psi = (\hbar/2m)\partial_x^2\psi$ — the diffusion equation. Solutions spread irreversibly; a localized initial condition smooths out and never recovers. The $i$ turns diffusion into wave propagation, and it is what ensures the integral $\int|\psi|^2 dx$ stays constant over time. We will prove that shortly.

![Two side-by-side plots of an initially Gaussian wave](../images/03-the-schrodinger-equation-fig-02.png)
*Figure 3.2 — Two side-by-side plots of an initially Gaussian wave*

None of these is a consequence of the plausibility argument. They are properties of the equation that the equation itself carries. The plausibility argument motivates the *form* of the equation; experiment confirms that nature uses it.

To check the equation is at least self-consistent: verify that $\psi(x,t) = A\,e^{i(kx-\omega t)}$ with $\omega = \hbar k^2/2m$ is actually a solution. Left side: $i\hbar\,\partial_t\psi = i\hbar(-i\omega)\psi = \hbar\omega\psi$. Right side: $-(\hbar^2/2m)\partial_x^2\psi = (\hbar^2 k^2/2m)\psi$. Equal iff $\hbar\omega = \hbar^2 k^2/2m$, which is $E = p^2/2m$. The dispersion relation is the free-particle energy-momentum relation, as it should be.

---

## The Born rule: what $|\psi|^2$ means

Schrödinger himself proposed that $|\psi|^2$ was the *charge density* of the electron — the electron was a smeared-out matter wave. The interpretation lasted weeks. Max Born proposed in 1926 [Born, *Z. Phys.* 37, 863–867](https://doi.org/10.1007/BF01397477) that

$$|\psi(x,t)|^2\,dx = \text{probability of finding the particle in } [x,\, x+dx] \text{ at time } t.$$

$\psi$ itself is not observable. $|\psi|^2$ is a probability density. Born received the Nobel Prize for this in 1954 — 28 years after the paper, which tells you something about how controversial the probabilistic interpretation was through the twenties and thirties.

Schrödinger's matter-wave interpretation had two structural problems that Born's solved. First: $\psi$ is complex, and there is no classical notion of a complex matter density. You could try $\text{Re}(\psi)$ or $|\psi|$, but neither obeys a linear equation — you would lose superposition. Second: for two particles, $\psi$ is a function of *six* coordinates, $\psi(x_1, y_1, z_1, x_2, y_2, z_2, t)$, and a function on six-dimensional configuration space cannot be a physical wave propagating in three-dimensional space. Born's interpretation accommodated both: probabilities are real and non-negative, and a probability distribution on configuration space is a perfectly sensible object regardless of dimension.

For the Born rule to be a consistent probability assignment, three conditions must hold. The first is non-negativity: $|\psi|^2 \geq 0$ everywhere. This is automatic — it is a squared modulus. The second is normalization: $\int_{-\infty}^\infty |\psi(x,t)|^2\,dx = 1$. The particle has to be *somewhere*. The third is conservation: if normalization holds at $t = 0$, it must hold at all later times. That third condition is not automatic. It is a theorem — and proving it requires the Hermiticity of $\hat{H}$.

As a direct application, take the ground state of an infinite square well of width $L$:

$$\psi_1(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{\pi x}{L}\right),\quad 0 \leq x \leq L.$$

What is the probability of finding the particle in the left quarter of the well, $[0, L/4]$?

$$P = \frac{2}{L}\int_0^{L/4}\sin^2\!\left(\frac{\pi x}{L}\right)dx = \frac{1}{L}\int_0^{L/4}\left[1 - \cos\!\left(\frac{2\pi x}{L}\right)\right]dx = \frac{1}{4} - \frac{1}{2\pi} \approx 0.091.$$

About 9%, not 25%. The ground-state probability density has a single peak in the center of the well; the leftmost quarter is depleted. This number — $1/4 - 1/2\pi$ — comes entirely from the wave function's shape, not from the particle's history. There is no trajectory. There is only the amplitude, squared.

![Plot of |ψ₁(x)|² = (2/L)sin²(πx/L) over [0, L]](../images/03-the-schrodinger-equation-fig-03.png)
*Figure 3.3 — Plot of |ψ₁(x)|² = (2/L)sin²(πx/L) over [0, L]*

The two misconceptions to dispose of now, rather than later. First: "$\psi$ is the particle." No — $\psi$ is the probability amplitude. What registers in a detector is the particle. Before detection, what exists is the amplitude. Second: "$|\psi|^2$ is telling you what you don't know about the particle's actual position, which has some definite value you just haven't measured." No. Bell-inequality experiments — Aspect 1982, refined many times since, awarded the 2022 Nobel Prize to Aspect, Clauser, and Zeilinger — rule out local hidden-variable theories that would make this story work. The probability is irreducible. It is not a stand-in for incomplete classical knowledge.

---

## Normalization is preserved, and why Hermiticity is the reason

Differentiate the normalization integral under the integral sign:

$$\frac{d}{dt}\int_{-\infty}^\infty|\psi|^2\,dx = \int\left(\psi^{*}\frac{\partial\psi}{\partial t} + \frac{\partial\psi^{*}}{\partial t}\psi\right)dx.$$

From the Schrödinger equation: $\partial_t\psi = -(i/\hbar)\hat{H}\psi$. For real $V$, $\partial_t\psi^{*} = +(i/\hbar)(\hat{H}\psi)^{*}$. Substituting:

$$\frac{d}{dt}\int|\psi|^2\,dx = -\frac{i}{\hbar}\left[\int\psi^{*}\hat{H}\psi\,dx - \int(\hat{H}\psi)^{*}\psi\,dx\right] = -\frac{i}{\hbar}\left[\langle\psi|\hat{H}\psi\rangle - \langle\hat{H}\psi|\psi\rangle\right].$$

By Hermiticity of $\hat{H}$, $\langle\psi|\hat{H}\psi\rangle = \langle\hat{H}\psi|\psi\rangle$. The bracket is zero. Normalization is preserved.

Notice what the proof consumed: exactly one fact, Hermiticity of $\hat{H}$. This is the structural reason quantum mechanics postulates that observables are Hermitian operators. It is not a mathematical aesthetic preference. Without Hermiticity, the Born rule would fail to define a probability assignment that survives time evolution. The whole apparatus would collapse.

The same argument, looked at locally rather than globally, produces the *continuity equation*. Define the probability density $\rho(x,t) = |\psi|^2$ and the probability current

$$j(x,t) = \frac{\hbar}{2mi}\left(\psi^{*}\frac{\partial\psi}{\partial x} - \psi\frac{\partial\psi^{*}}{\partial x}\right) = \frac{\hbar}{m}\,\text{Im}\!\left(\psi^{*}\frac{\partial\psi}{\partial x}\right).$$

Then

$$\frac{\partial\rho}{\partial t} + \frac{\partial j}{\partial x} = 0.$$

This is the local statement of probability conservation. Probability does not disappear at one point and reappear somewhere else discontinuously — it flows. If probability is leaving a region, it is flowing across the boundary, and the rate of flow is $j$.

![Diagram of a 1D region [a, b] with](../images/03-the-schrodinger-equation-fig-04.png)
*Figure 3.4 — Diagram of a 1D region [a, b] with*

To derive it: compute $\partial_t(\psi^{*}\psi)$, substitute the Schrödinger equation for $\partial_t\psi$ and $\partial_t\psi^{*}$, watch the potential terms cancel because $V$ is real, and recognize the remaining structure as $\partial_x(\psi^{*}\partial_x\psi - \psi\partial_x\psi^{*})$ from the product rule. The derivation is a half-page exercise; each step is just the Schrödinger equation applied twice, once to $\psi$ and once to $\psi^{*}$.

For a plane wave $\psi = Ae^{i(kx-\omega t)}$, the current works out to $j = (\hbar k/m)|A|^2 = v|A|^2$ — density times velocity, exactly the classical expression for a moving fluid. In the limit where the wave picture should look classical, the probability current looks like a particle current. This is a sanity check that the formalism is internally consistent.

---

## Stationary states

If the potential $V$ does not depend on time, the Schrödinger equation admits solutions of a special separated form:

$$\psi(x,t) = \psi(x)\,e^{-iEt/\hbar}.$$

Substitute. The left side produces $E\psi(x)e^{-iEt/\hbar}$. The right side produces $\hat{H}\psi(x)$ times $e^{-iEt/\hbar}$. The time-dependent phase cancels throughout, and what remains is:

$$\boxed{\;\hat{H}\psi(x) = E\,\psi(x).\;}$$

This is the *time-independent Schrödinger equation* — an eigenvalue equation for the Hamiltonian. The function $\psi(x)$ is an energy eigenfunction; the real number $E$ is the allowed energy.

Why "stationary"? Because $|\psi(x,t)|^2 = |\psi(x)|^2$ — the probability density is time-independent. Every measurement probability, for any time-independent observable, is constant. The state does not evolve in any observable sense when you look at it one piece at a time.

Now here is the misconception that ruins everything, and it ruins it in a specific way: *stationary states are not static.* The *probability density* is constant. The *amplitude* $\psi(x,t) = \psi(x)\,e^{-iEt/\hbar}$ rotates in the complex plane at angular frequency $E/\hbar$. The magnitude at each $x$ is fixed. The phase advances at rate $E/\hbar$. For a single stationary state in isolation, this phase rotation has no observable consequence, because measurements depend only on $|\psi|^2$, and $|e^{-iEt/\hbar}| = 1$. You cannot see it. But the moment you put two stationary states together, you can see nothing else.

![A single phasor rotating invisibly. Two phasors beating visibly.](../images/03-the-schrodinger-equation-fig-05.png)
*Figure 3.5 — Diagram *

Form a superposition of states at energies $E_1$ and $E_2$:

$$\psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1 t/\hbar} + \psi_2(x)\,e^{-iE_2 t/\hbar}\right].$$

Compute $|\psi|^2$:

$$|\psi|^2 = \frac{1}{2}\left[|\psi_1|^2 + |\psi_2|^2 + 2\,\text{Re}\!\left(\psi_1^{*}\psi_2\,e^{-i(E_2 - E_1)t/\hbar}\right)\right].$$

The cross term oscillates. It has a factor of $\cos((E_2 - E_1)t/\hbar)$ — the *Bohr frequency* $(E_2 - E_1)/\hbar$. The probability density rocks back and forth at this frequency. The expectation value of position oscillates. When the atom in a higher energy state decays to a lower one, it emits a photon of exactly this energy $E_2 - E_1$, producing a spectral line at frequency $(E_2 - E_1)/h$. Every spectral line in atomic physics — every line in the Balmer series, the Lyman series, the Paschen series — exists because the phases of stationary states rotate, and their *relative* rotation at the Bohr frequency is physically observable the moment you superpose them.

To see this concretely, take the first two stationary states of a particle in an infinite square well of width $L$:

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right),\quad E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}.$$

In the equal-amplitude superposition $\psi = (1/\sqrt{2})[\psi_1 e^{-iE_1 t/\hbar} + \psi_2 e^{-iE_2 t/\hbar}]$, compute $\langle x\rangle(t)$. The time-independent piece is $(1/2)[\langle x\rangle_1 + \langle x\rangle_2] = L/2$, by symmetry. The time-dependent piece requires evaluating

$$\frac{2}{L}\int_0^L x\sin\!\left(\frac{\pi x}{L}\right)\sin\!\left(\frac{2\pi x}{L}\right)dx.$$

Use $\sin a\sin b = (1/2)[\cos(a-b) - \cos(a+b)]$ and integrate by parts. The result: this integral equals $-16L/(9\pi^2)$. So

$$\langle x\rangle(t) = \frac{L}{2} - \frac{16L}{9\pi^2}\cos(\omega t),\qquad \omega = \frac{E_2 - E_1}{\hbar} = \frac{3\pi^2\hbar}{2mL^2}.$$

The expectation value of position oscillates about the midpoint of the well with amplitude $16L/9\pi^2 \approx 0.18L$ at the Bohr frequency. The particle is not moving in any classical sense — there is no trajectory, no velocity, no definite position at any time. But the center of the probability distribution swings back and forth like a pendulum. This is a quantum state that radiates.

![Animation-ready sequence of three snapshots of |ψ(x,t)|² for](../images/03-the-schrodinger-equation-fig-06.png)
*Figure 3.6 — Animation-ready sequence of three snapshots of |ψ(x,t)|² for*

---

## The time-evolution algorithm

The spectral theorem from Unit 2 says the energy eigenfunctions of a Hermitian Hamiltonian form a complete orthonormal basis. So any initial state can be expanded:

$$\psi(x, 0) = \sum_n c_n\,\psi_n(x),\qquad c_n = \int\psi_n^{*}(x)\,\psi(x,0)\,dx.$$

Time evolution attaches a phase to each component:

$$\psi(x,t) = \sum_n c_n\,\psi_n(x)\,e^{-iE_n t/\hbar}.$$

That is the complete algorithm for time evolution under a time-independent Hamiltonian. Find the energy eigenstates. Expand the initial condition. Attach a phase to each term. Sum back. Almost every solvable problem in quantum mechanics — the infinite square well, the harmonic oscillator, hydrogen — runs this algorithm with a different choice of $V(x)$ and therefore a different set of eigenfunctions $\psi_n$ and energies $E_n$.

The probability that a measurement of energy yields $E_n$ is $|c_n|^2$, constant in time. The energy probabilities never change under Hamiltonian evolution — because each term's phase $e^{-iE_n t/\hbar}$ has modulus 1, so $|c_n e^{-iE_n t/\hbar}|^2 = |c_n|^2$. Only expectation values of other observables — position, momentum — can oscillate, and they oscillate because of the cross terms between energy eigenstates with different phases.

This approach requires a time-independent $V$. For time-dependent potentials, the eigenstates themselves shift with time, and you need time-dependent perturbation theory. That is Unit 9.

---

## The free particle and why plane waves are not states

When $V = 0$, the time-independent Schrödinger equation is $-(\hbar^2/2m)\,d^2\psi/dx^2 = E\psi$. Set $k = \sqrt{2mE}/\hbar$. The general solution is

$$\psi_k(x) = Ae^{ikx} + Be^{-ikx},$$

right-moving and left-moving plane waves at momentum $\pm\hbar k$. The full time-dependent solution carries the phase $e^{-iEt/\hbar}$ with $E = \hbar^2 k^2/2m$.

These plane waves are not normalizable. Compute $\int|Ae^{ikx}|^2\,dx = |A|^2\int_\infty^\infty 1\,dx = \infty$. They violate the Born rule: total probability cannot be infinite. They are not physical states.

This is not a failure of the formalism. Plane waves are generalized eigenfunctions in the sense flagged in Unit 2 — they live in the extended space beyond $L^2(\mathbb{R})$ and are useful as calculational tools, the same way position eigenstates $|x\rangle$ are. Physical states are *wave packets*: superpositions of plane waves with a normalizable weight function. Write

$$\psi(x, 0) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty \phi(k)\,e^{ikx}\,dk.$$

This is a Fourier expansion. $\phi(k)$ is the momentum-space wave function. If $\phi(k)$ is peaked near $k_0$ with spread $\Delta k$, then $\psi(x,0)$ is a localized wave packet whose position spread is of order $1/\Delta k$. That is the Heisenberg uncertainty relation: narrow in momentum, broad in position.

Time evolution: each component picks up its own phase, $e^{-i\omega(k)t}$ with $\omega(k) = \hbar k^2/2m$. So

$$\psi(x,t) = \frac{1}{\sqrt{2\pi}}\int\phi(k)\,e^{i(kx - \omega(k)t)}\,dk.$$

Because $\omega(k)$ is quadratic in $k$ — not linear — components at different momenta move at different speeds. The wave packet *spreads*. For a Gaussian initial packet of width $\sigma_0$, the position-space width grows as $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/2m\sigma_0^2)^2}$. At early times the spreading is slow; at late times the width grows linearly in $t$. This spreading is one of the first genuinely quantum predictions you can compute and check — and it has no classical analog for a particle. A baseball thrown in a definite direction stays on that trajectory. A quantum particle disperses.

![Plot of Gaussian wave-packet width σ(t) vs](../images/03-the-schrodinger-equation-fig-07.png)
*Figure 3.7 — Plot of Gaussian wave-packet width σ(t) vs*

---

## What the equation does and does not tell you

You now have the dynamical law. Here is an honest accounting of what it gives you and what it does not.

It gives you a precise algorithm: write down $\hat{H}$, find its eigenstates and eigenvalues, expand your initial condition, attach phases, sum. Predictions about every measurement outcome, at any later time, with any observable, follow from this. The predictions are probabilities — not because of any ignorance on our part, but because the theory is genuinely probabilistic at the level of individual outcomes (Bell's theorem makes this unavoidable). The equation is linear, first-order in time, and Hermitian; normalization is preserved and spectral lines come out right.

What it does not give you: an explanation of *why* this equation rather than its neighbors. The postulate status is honest, not evasive. Newton's second law has the same status inside classical mechanics. The Schrödinger equation is tested by its consequences, and its consequences include the hydrogen spectrum, tunneling, the laser, the transistor, and the MRI machine. That is its justification.

What it also does not give you, and this is worth sitting with: it does not tell you what $\psi$ *is*. Is it a real field in some physical sense? A representation of an observer's knowledge? A guiding wave for a hidden particle? The equation is agnostic on this question. All the interpretations of quantum mechanics — many-worlds, Copenhagen, Bohmian mechanics, relational QM, epistemic approaches — agree on the predictions of the Schrödinger equation and disagree on what that equation is describing. Unit 5 returns to this. For now: the formalism works regardless of which interpretation you hold, and the predictions are the same either way.

---

## What would change my mind

The Schrödinger equation's central claim — that state evolution under $i\hbar\partial_t\psi = \hat{H}\psi$ with $\hat{H}$ Hermitian gives the right probabilities via the Born rule — has survived a century of experimental tests in the non-relativistic regime. Spontaneous collapse models (GRW: Ghirardi, Rimini, Weber, 1986) propose a small violation of this evolution, and ongoing experiments — including searches for collapse-induced X-ray emission in solids — are testing this. To date, standard Schrödinger evolution has held. A confirmed deviation would force a different equation in this chapter. Absent one, the equation here is the right one for non-relativistic quantum mechanics.

---

## Still puzzling

**Why a postulate?** Students often feel cheated. The companion's position: every fundamental theory has a place where its laws stop having deeper explanations and become axioms. Newton's second law is in the same epistemic position. "Postulate" is not a confession of ignorance. It is the right description of where a theory begins. Why the Schrödinger equation has the form it does — why $i\hbar\partial_t$ and not something else — is a question that probably belongs to quantum field theory or to some still-undiscovered framework.

**The interpretation problem.** The Schrödinger equation gives you $\psi$. The Born rule tells you $|\psi|^2$ is a probability. Neither tells you what $\psi$ is. The formalism is silent on this question, and the silence is not a bug — all interpretations agree on the predictions. Unit 5 takes this up directly.

**The measurement problem.** The Schrödinger equation describes unitary, deterministic evolution. Measurement, in the standard formulation, is a non-unitary, stochastic update. These are in apparent tension. Decoherence (Zurek, 2003) gives a partial answer by showing that interactions with an environment suppress macroscopic superpositions rapidly, but it does not explain how a definite outcome emerges from unitary evolution. Open at the level of foundations. Closed at the level of computing predictions.

**The arrow of time.** The Schrödinger equation is time-reversal symmetric. Wave packets spread, but they don't have to — run the equation backward and a broad packet narrows. Physical experience seems to single out the spreading direction. The answer probably lies in thermodynamics and initial conditions, not in the equation itself.

---

## LLM exercises

The following exercises are designed to be worked interactively with a language model. Use the model to check your reasoning step by step — not to generate answers, but to test whether you can explain each step clearly enough that the model can follow and push back.

**L1.** Dictate the plausibility argument for the Schrödinger equation to the model, starting only from "a free particle is described by a wave $\psi = Ae^{i(kx-\omega t)}$" and the de Broglie and Einstein relations. Ask the model to identify every step that is a genuine logical consequence and every step that is an assumption or postulate. Count the postulates.

**L2.** Give the model a specific wave function — say $\psi(x,t) = A e^{-x^2/a^2} e^{-iEt/\hbar}$ for some constants $A$, $a$, $E$ you choose — and ask: is this a solution of the time-independent Schrödinger equation for some $V(x)$? If so, what is $V(x)$? Work out the answer yourself by computing $\hat{H}\psi/\psi$ and compare with the model.

**L3.** State in plain language, to the model, why the Hermiticity of $\hat{H}$ guarantees that $d/dt\int|\psi|^2 dx = 0$ — without writing any integrals. Ask the model to convert your verbal explanation into the mathematical proof and flag any steps you described imprecisely.

**L4.** Construct a normalized superposition of the first two infinite-square-well eigenstates. Ask the model to compute $\langle x\rangle(t)$ step by step. Do the calculation yourself first. Compare not just the final answer but each intermediate step — the expansion of $|\psi|^2$, the identification of the cross term, the integral of $x\psi_1\psi_2$, the Bohr frequency. Identify any step where your approach and the model's diverged.

**L5.** Ask the model to explain why a free-particle plane wave $\psi = Ae^{ikx}$ is not a physical state, even though it satisfies the Schrödinger equation. Then give your own explanation. Ask the model to compare the two explanations and identify which one is more physically precise — and whether "not normalizable" is a sufficient explanation or whether there is something deeper to say about the role of wave packets and the Fourier representation.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Schrödinger, E. "Quantisierung als Eigenwertproblem (Erste Mitteilung)." *Annalen der Physik* 79, 361–376 (1926). https://doi.org/10.1002/andp.19263840404
2. Born, M. "Zur Quantenmechanik der Stoßvorgänge." *Zeitschrift für Physik* 37, 863–867 (1926). https://doi.org/10.1007/BF01397477
3. The Nobel Prize in Physics 1954 — Max Born. https://www.nobelprize.org/prizes/physics/1954/born/facts/
4. Aspect, A., Grangier, P. & Roger, G. "Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment." *Physical Review Letters* 49, 91 (1982).
5. The Nobel Prize in Physics 2022 — Aspect, Clauser, Zeilinger. https://www.nobelprize.org/prizes/physics/2022/
6. Ghirardi, G. C., Rimini, A. & Weber, T. "Unified dynamics for microscopic and macroscopic systems." *Physical Review D* 34, 470–491 (1986).
7. Zurek, W. H. "Decoherence, einselection, and the quantum origins of the classical." *Reviews of Modern Physics* 75, 715–775 (2003). https://doi.org/10.1103/RevModPhys.75.715
