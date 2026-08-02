# Chapter 2 — Mathematical Foundations


## TL;DR

- The language quantum mechanics is written in, and why no simpler language works.
- The chapter moves through The arithmetic of complex numbers, Vector spaces and inner products, Dirac notation, Operators and eigenvalues, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The language quantum mechanics is written in, and why no simpler language works.*

---

There is a single experiment that forces the whole mathematical structure on you. Not because physicists decided to make things complicated — because the experiment *insists*, and you either follow where it leads or you stop doing physics.

Run electrons, one at a time, through two slits. Each electron lands somewhere on the screen behind. After ten thousand electrons, a pattern appears: bright bands where many landed, dark bands where almost none did. The bands are interference fringes — the same pattern you get when water waves pass through two gaps.

But these are electrons. Single electrons. There is no other electron for each one to interfere *with*. Whatever is interfering is the electron interfering with itself.

Now here is the thing that forces the math. To get those dark bands, you need the contributions from the two slits to *cancel*. Not add to something small — cancel. If the two contributions are $\psi_1$ and $\psi_2$, and you add them as $\psi_1 + \psi_2$, and then you compute intensity as $|\psi_1 + \psi_2|^2$, you can get cancellation when $\psi_1 = -\psi_2$. Fine. But you need not just cancellation at one angle — you need alternating bright and dark bands across the whole screen. The contributions need to vary smoothly in sign and magnitude as the angle changes. They need a continuously varying *phase*.

Things with a continuously varying phase look like $e^{i\varphi}$. And $e^{i\varphi}$ requires $i = \sqrt{-1}$. Which requires complex numbers.

This is not a convenient choice. The experiment doesn't give you an alternative.

![Double-slit experiment diagram with single-electron sequential buildup ](../images/02-mathematical-foundations-fig-01.png)
*Figure 2.1 — Double-slit experiment diagram with single-electron sequential buildup *

---

## The arithmetic of complex numbers

A complex number is $z = a + bi$ where $a$ and $b$ are ordinary real numbers and $i^2 = -1$. The real part is $a$, the imaginary part is $b$. The *complex conjugate* of $z$ is $z^{*} = a - bi$ — you flip the sign on the imaginary part. The *modulus* is

$$|z| = \sqrt{z^{*} z} = \sqrt{a^2 + b^2}.$$

That is a non-negative real number. You can think of $a$ and $b$ as coordinates in a plane — the "complex plane" — where the real axis goes left-right and the imaginary axis goes up-down. The modulus is the distance from the origin.

Euler's formula is the fact that makes complex numbers useful in physics:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

If you want to see why, expand $e^{i\theta}$, $\cos\theta$, and $\sin\theta$ in their Taylor series and check that the real and imaginary parts match term by term. The point is this: every complex number can be written as $z = r\,e^{i\theta}$ where $r = |z|$ is its distance from the origin and $\theta$ is its angle. Multiplying two complex numbers multiplies their distances and *adds* their angles. Taking the conjugate flips the angle: $(re^{i\theta})^{*} = re^{-i\theta}$.

The three facts you will use over and over:

![The complex plane showing a point z =](../images/02-mathematical-foundations-fig-02.png)
*Figure 2.2 — The complex plane showing a point z =*

- $|e^{i\theta}| = 1$ for any real $\theta$. A pure phase factor doesn't change the size of anything.
- $e^{i\theta_1} \cdot e^{i\theta_2} = e^{i(\theta_1 + \theta_2)}$. Phases add when complex numbers multiply.
- $(z_1 z_2)^{*} = z_1^{*} z_2^{*}$. Conjugation distributes over multiplication.

Now back to the double slit. Label the two slits. The amplitude arriving at the screen from slit 1 is $\psi_1$; from slit 2, $\psi_2$. The rule of quantum mechanics — we will state it precisely in Unit 3, but use it here — is that you *add the amplitudes* and then *square the modulus* to get intensity. The total amplitude is $\psi = \psi_1 + \psi_2$, and the intensity is $|\psi|^2$.

Take a specific simple case: one slit is a distance $r$ from the screen point, the other is a distance $r + d\sin\theta$ away. Assign equal magnitudes $1/\sqrt{2}$ and phases determined by path length:

$$\psi_1 = \frac{1}{\sqrt{2}} e^{ikr}, \qquad \psi_2 = \frac{1}{\sqrt{2}} e^{ik(r + d\sin\theta)},$$

where $k = 2\pi/\lambda$ is the wavenumber. Now expand $|\psi_1 + \psi_2|^2$:

$$|\psi|^2 = \frac{1}{2}\left[e^{-ikr} + e^{-ik(r+d\sin\theta)}\right]\left[e^{ikr} + e^{ik(r+d\sin\theta)}\right]$$

$$= \frac{1}{2}\left[1 + e^{ikd\sin\theta} + e^{-ikd\sin\theta} + 1\right] = 1 + \cos(kd\sin\theta).$$

Using $1 + \cos x = 2\cos^2(x/2)$:

$$|\psi|^2 = 2\cos^2\!\left(\frac{kd\sin\theta}{2}\right).$$

Maxima where $d\sin\theta = n\lambda$; zeros where $d\sin\theta = (n + 1/2)\lambda$. Bright and dark bands, exactly as observed. The complex exponentials made this calculation work in four lines. Try it with real numbers: the cross term is $2\psi_1\psi_2$, a fixed sign, no oscillation. No dark bands. No double slit experiment.

![Plot of |ψ|² = 2cos²(kd sinθ / 2)](../images/02-mathematical-foundations-fig-03.png)
*Figure 2.3 — Plot of |ψ|² = 2cos²(kd sinθ / 2)*

Stueckelberg showed in 1960 that you can reformulate quantum mechanics with real numbers if you double the dimension of every space — one extra real dimension to replace each complex one. What you cannot do is reformulate it with real numbers *in the same dimension*. And Renou and collaborators published an experiment in 2021 that directly tested a whole class of real-amplitude reformulations using Bell inequalities — and ruled them out [Renou et al., *Nature* 600, 625–629 (2021), *verify pagination*]. The complex numbers are not a convention. They are measured.

---

## Vector spaces and inner products

A *vector space* over $\mathbb{C}$ is a set of objects — we will call them states and write them $|\psi\rangle$ — with two operations: you can add any two of them ($|\psi\rangle + |\phi\rangle$), and you can multiply any one by a complex number ($\alpha|\psi\rangle$). These operations satisfy the usual rules: addition is commutative and associative, scalar multiplication distributes. The simplest example is $\mathbb{C}^n$, columns of $n$ complex numbers.

An *inner product* is a way to measure the "angle" between two states. It is a map $\langle\cdot|\cdot\rangle: V \times V \to \mathbb{C}$ satisfying three conditions:

1. **Conjugate symmetry:** $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^{*}$.
2. **Linear in the second slot:** $\langle\phi|\alpha\psi + \beta\chi\rangle = \alpha\langle\phi|\psi\rangle + \beta\langle\phi|\chi\rangle$.
3. **Positive definite:** $\langle\psi|\psi\rangle \geq 0$, with equality only for the zero vector.

From (1) and (2) it follows that the inner product is *anti-linear* in the first slot — scalars come out conjugated: $\langle\alpha\phi|\psi\rangle = \alpha^{*}\langle\phi|\psi\rangle$. This is the physicist convention, followed here throughout.

The *norm* of a state is $\|\psi\| = \sqrt{\langle\psi|\psi\rangle}$. A *Hilbert space* is a complex vector space with an inner product that is also *complete* — meaning no sequences escape the space. In finite dimensions (like $\mathbb{C}^n$), completeness is automatic. For wave functions on the real line, the relevant Hilbert space is $L^2(\mathbb{R})$, the space of square-integrable functions, and completeness is a genuine theorem.

Concretely in $\mathbb{C}^n$: if $|\psi\rangle = (\alpha_1, \ldots, \alpha_n)^T$ and $|\phi\rangle = (\beta_1, \ldots, \beta_n)^T$, then

$$\langle\phi|\psi\rangle = \sum_{i=1}^n \beta_i^{*} \alpha_i.$$

Conjugate the first slot's entries; multiply; sum. Concretely on $L^2(\mathbb{R})$: if $\psi$ and $\phi$ are wave functions,

$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty \phi^{*}(x)\,\psi(x)\,dx.$$

Same idea, integral instead of sum.

---

## Dirac notation

P. A. M. Dirac introduced the bra-ket notation in 1939 [Dirac, *Math. Proc. Cambridge Phil. Soc.* 35, 416–418]. It looks like decoration. It is not. It packages four operations into a notation clean enough that calculations that would take a page in indexed components take three lines.

**Ket.** $|\psi\rangle$ is the state vector. In $\mathbb{C}^n$, think of it as a column.

**Bra.** $\langle\psi|$ is the *dual vector* — the linear functional that, given any ket $|\phi\rangle$, produces the number $\langle\psi|\phi\rangle$. In $\mathbb{C}^n$, if $|\psi\rangle = (\alpha_1, \alpha_2)^T$, then $\langle\psi| = (\alpha_1^{*}, \alpha_2^{*})$ as a row. *Both* conjugate the entries *and* transpose. These are not separate steps; they happen together. The operation that does both is Hermitian conjugation, written $\dagger$, so $\langle\psi| = |\psi\rangle^\dagger$.

**Inner product.** $\langle\phi|\psi\rangle$ is a complex number: row times column, or integral of $\phi^{*}\psi$, depending on the space.

**Outer product.** $|\psi\rangle\langle\phi|$ is an *operator*: it takes a ket $|\chi\rangle$ to the ket $|\psi\rangle\,(\langle\phi|\chi\rangle)$, which is a complex number times $|\psi\rangle$.

| name | symbol | what it is | concrete form in ℂ² |
| --- | --- | --- | --- |
| ket | $|\psi\rangle$ | state vector | $\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$ |
| bra | $\langle\psi|$ | dual vector | $\begin{pmatrix}\alpha^* & \beta^*\end{pmatrix}$ |
| inner product | $\langle\phi|\psi\rangle$ | complex number | $\phi_1^*\alpha+\phi_2^*\beta$ |
| outer product | $|\psi\rangle\langle\phi|$ | operator | $\begin{pmatrix}\alpha\phi_1^* & \alpha\phi_2^*\\ \beta\phi_1^* & \beta\phi_2^*\end{pmatrix}$ |

Two identities anchor everything that follows. The first is the *completeness relation*. Take any orthonormal basis $\{|n\rangle\}$ of the space — a set of mutually orthogonal unit vectors that spans the whole space, meaning $\langle m|n\rangle = \delta_{mn}$ and every state can be expanded in them. Then:

$$\sum_n |n\rangle\langle n| = \hat{I}.$$

Why? Take any $|\psi\rangle$. Expand it as $|\psi\rangle = \sum_n c_n|n\rangle$ where $c_n = \langle n|\psi\rangle$. Then $\sum_n |n\rangle\langle n|\psi\rangle = \sum_n c_n|n\rangle = |\psi\rangle$. The operator $\sum_n|n\rangle\langle n|$ acts as the identity. "Inserting the identity" — writing $\hat{I} = \sum_n|n\rangle\langle n|$ between two other operators — is the single most common calculational maneuver in quantum mechanics.

The second identity: the wave function $\psi(x)$ is the *position-basis component* of the abstract state $|\psi\rangle$. There exist generalized position eigenstates $|x\rangle$ (not normalizable; they live in an extended sense outside $L^2(\mathbb{R})$, but they are useful) with $\langle x|x'\rangle = \delta(x - x')$, and

$$\int dx\,|x\rangle\langle x| = \hat{I}, \qquad \langle x|\psi\rangle = \psi(x).$$

So $|\psi\rangle = \int dx\,\psi(x)|x\rangle$ — the wave function is the expansion coefficients of $|\psi\rangle$ in the position basis. Abstract Dirac notation and concrete wave-function notation are the same object written two ways. Insert $\int dx|x\rangle\langle x|$ to move from one to the other.

The single most common student error: computing a matrix element $\langle\phi|\hat{A}|\psi\rangle$ by writing $\phi$'s components as a row *without conjugating them*. The result is wrong — complex when it should be real, typically. Always conjugate when you turn a ket into a bra. If you get a complex expectation value for what you believe is an observable, look for the missing conjugation first.

---

## Operators and eigenvalues

A *linear operator* $\hat{A}$ on $V$ maps $V \to V$ and respects addition and scalar multiplication: $\hat{A}(\alpha|\psi\rangle + \beta|\phi\rangle) = \alpha\hat{A}|\psi\rangle + \beta\hat{A}|\phi\rangle$. In $\mathbb{C}^n$, every linear operator is an $n \times n$ matrix.

The *eigenvalue equation* is

$$\hat{A}|a\rangle = a|a\rangle.$$

A vector $|a\rangle$ that the operator leaves pointing in the same direction, scaled by a complex number $a$. The eigenvalues come from the characteristic polynomial $\det(\hat{A} - a\hat{I}) = 0$.

Now here is where Hermitian operators become the central object. An operator is *Hermitian* if $\hat{A}^\dagger = \hat{A}$, where $\hat{A}^\dagger$ is defined by the requirement that $\langle\phi|\hat{A}\psi\rangle = \langle\hat{A}^\dagger\phi|\psi\rangle$ for all $|\phi\rangle$, $|\psi\rangle$. In matrix form, $\hat{A}^\dagger$ is the conjugate transpose: $(A^\dagger)_{ij} = A_{ji}^{*}$. Hermitian means $A_{ij} = A_{ji}^{*}$.

The *spectral theorem* for Hermitian operators says three things:

1. All eigenvalues are real.
2. Eigenvectors for different eigenvalues are orthogonal.
3. The eigenvectors form an orthonormal basis.

The proof of (1) is one line: if $\hat{A}|a\rangle = a|a\rangle$ and $\hat{A} = \hat{A}^\dagger$, take the inner product of both sides with $|a\rangle$:

$$\langle a|\hat{A}|a\rangle = a\langle a|a\rangle.$$

But also $\langle a|\hat{A}|a\rangle = \langle \hat{A}a|a\rangle = \langle a|a\rangle\, a^{*}$. So $a\langle a|a\rangle = a^{*}\langle a|a\rangle$. Since $\langle a|a\rangle > 0$, we get $a = a^{*}$, so $a$ is real.

These three properties are why every observable in quantum mechanics is a Hermitian operator: real eigenvalues because measurement outcomes are real numbers; orthogonal eigenstates because distinct outcomes correspond to distinguishable results; a complete eigenbasis because the measurement must have *some* outcome with probability 1.

---

## The three Pauli matrices

The spin-1/2 system is the cleanest possible quantum system: two-dimensional Hilbert space $\mathbb{C}^2$, three Hermitian observables, all the essential features visible in $2 \times 2$ matrix arithmetic.

The three Pauli matrices are the spin observables along the $x$, $y$, and $z$ axes:

$$\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

All three are Hermitian — check $(A^\dagger)_{ij} = A_{ji}^{*}$ for each. All three have eigenvalues $\pm 1$. Their eigenvectors are different, and that difference is the substance of quantum measurement.

$\sigma_z$ is already diagonal. Eigenvectors:

$$|\!\uparrow\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad |\!\downarrow\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}.$$

These are spin-up and spin-down along the $z$-axis.

For $\sigma_x$: characteristic polynomial $\lambda^2 - 1 = 0$, eigenvalues $\pm 1$. For $\lambda = +1$, the eigenvector equation $(\sigma_x - I)|v\rangle = 0$ gives equal components. Normalized:

$$|+_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + |\!\downarrow\rangle), \qquad |-_x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - |\!\downarrow\rangle).$$

For $\sigma_y$: same eigenvalues. For $\lambda = +1$, the equation $(\sigma_y - I)|v\rangle = 0$ gives $-v_1 - iv_2 = 0$, so $v_2 = iv_1$. Normalized:

$$|+_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle + i|\!\downarrow\rangle), \qquad |-_y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix} = \frac{1}{\sqrt{2}}(|\!\uparrow\rangle - i|\!\downarrow\rangle).$$

That $i$ in the component of $|+_y\rangle$ is the whole point. There is no real-coefficient basis that diagonalizes $\sigma_y$. Try to write a real $2\times 2$ symmetric matrix with eigenvalues $\pm 1$ that is physically equivalent to $\sigma_y$ — you cannot, because the chirality of $\sigma_y$ is encoded in the complex structure. $\sigma_y$ is the place in the introductory course where you cannot look at the $i$ and tell yourself it is just notation.

Now consider what it means for measurements to be non-commuting. Start with the state $|\!\uparrow\rangle$. Apply $\sigma_x$:

$$\sigma_x|\!\uparrow\rangle = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = |\!\downarrow\rangle.$$

The spin-$z$-up state is not a spin-$x$ eigenstate; acting with $\sigma_x$ takes it to the orthogonal state. To find the measurement probabilities, expand $|\!\uparrow\rangle$ in the $\sigma_x$ eigenbasis. Inverting the relations above: $|\!\uparrow\rangle = (1/\sqrt{2})(|+_x\rangle + |-_x\rangle)$. The probability of measuring $\sigma_x = +1$ in the state $|\!\uparrow\rangle$ is $|\langle +_x|\!\uparrow\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$. Fifty-fifty. A particle known to be spin-up along $z$ is completely undetermined along $x$. That is the Stern–Gerlach experiment, written in basis-change arithmetic.

![Stern-Gerlach apparatus diagram showing sequential measurements ](../images/02-mathematical-foundations-fig-04.png)
*Figure 2.4 — Stern-Gerlach apparatus diagram showing sequential measurements *

---

## Hermitian operators in infinite dimensions: checking $\hat{p}$

The momentum operator in the position representation is $\hat{p} = -i\hbar\,d/dx$. Let us verify it is Hermitian on the space of square-integrable functions vanishing at infinity.

We need to confirm $\langle\phi|\hat{p}\psi\rangle = \langle\hat{p}\phi|\psi\rangle$, i.e.,

$$\int_{-\infty}^\infty \phi^{*}(x)\left(-i\hbar\frac{d\psi}{dx}\right)dx = \int_{-\infty}^\infty \left(-i\hbar\frac{d\phi}{dx}\right)^{*}\psi(x)\,dx.$$

The right side is $\int (+i\hbar\,d\phi^{*}/dx)\,\psi\,dx$. Integrate the left side by parts:

$$\int \phi^{*}\frac{d\psi}{dx}\,dx = \left[\phi^{*}\psi\right]_{-\infty}^\infty - \int\frac{d\phi^{*}}{dx}\psi\,dx.$$

The boundary term $[\phi^{*}\psi]_{-\infty}^\infty$ vanishes because both $\phi$ and $\psi$ are square-integrable — if they didn't go to zero at infinity, $\int|\psi|^2\,dx$ would diverge. So

$$\int\phi^{*}\frac{d\psi}{dx}\,dx = -\int\frac{d\phi^{*}}{dx}\psi\,dx.$$

Multiply both sides by $-i\hbar$:

$$-i\hbar\int\phi^{*}\frac{d\psi}{dx}\,dx = +i\hbar\int\frac{d\phi^{*}}{dx}\psi\,dx. \checkmark$$

Two things to notice. First: the $-i$ in $\hat{p} = -i\hbar\,d/dx$ is load-bearing. Without it, $d/dx$ is *anti-Hermitian* ($\hat{A}^\dagger = -\hat{A}$) by the same argument; the $-i$ rotates anti-Hermitian to Hermitian. Every basic QM operator carries these factors of $i$ for exactly this reason. Second: the proof used the boundary conditions. On a finite interval with states that don't vanish at the endpoints, the boundary term does not necessarily vanish, and $\hat{p}$ may not be Hermitian on that domain. The domain is part of the definition of the operator. In infinite dimensions, *Hermitian* and *self-adjoint* are not the same thing — a Hermitian operator might have eigenstates but lack a complete eigenbasis, or fail to admit a unique unambiguous extension to its full domain. Griffiths' footnotes acknowledge this; Reed and Simon *Methods of Modern Mathematical Physics* Vol. 2 is the reference for when it matters. It will matter again in Unit 4 when half-line problems first appear.

![Integration-by-parts steps for the momentum Hermiticity proof ](../images/02-mathematical-foundations-fig-05.png)
*Figure 2.5 — Integration-by-parts steps for the momentum Hermiticity proof *

---

## What the formalism looks like in one picture

Quantum states are vectors in a complex Hilbert space. Observables are Hermitian operators on that space. The eigenvalues of an observable are the possible measurement outcomes. A state $|\psi\rangle$ expanded in the eigenbasis of $\hat{A}$ as $|\psi\rangle = \sum_n c_n|a_n\rangle$ has probability $|c_n|^2$ of yielding outcome $a_n$. The expectation value is

$$\langle\hat{A}\rangle = \langle\psi|\hat{A}|\psi\rangle = \sum_n a_n|c_n|^2.$$

Five tools: complex numbers, vector spaces with inner products, Dirac notation, eigenvalue equations, Hermitian operators. That is the complete mathematical vocabulary of quantum mechanics. Everything in the units that follow — the Schrödinger equation, spin, identical particles, entanglement, scattering — is this vocabulary applied to particular problems.

---

## What would change my mind

The claim that quantum mechanics requires complex amplitudes is settled at the operational level by a century of experiments. Renou et al. (2021) tightened it further, ruling out a broad class of real-amplitude reformulations on Bell-inequality grounds. What would force a revision: a reproducible experiment showing that a real-amplitude theory in the same Hilbert-space dimension reproduces the measured probabilities — specifically, surviving the Bell test Renou designed. None has appeared.

The Hermitian-operator postulate rests on the spectral theorem and the requirement that measurement outcomes be real. If an open quantum system requires non-Hermitian operators — as in $\mathcal{PT}$-symmetric theories (Bender and Boettcher, 1998) — the story becomes more complicated. This is an active research area and is not the framework assumed here. The unit's claims are restricted to closed systems.

---

## Still puzzling

**Why $\mathbb{C}$ and not $\mathbb{H}$?** The Stueckelberg argument rules out real QM in fixed dimension; the Renou result sharpens it experimentally. But the quaternions $\mathbb{H}$ also give a sensible-looking inner-product structure (Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995). Why does nature prefer $\mathbb{C}$? The conventional answer is that no experiment has required $\mathbb{H}$. That is not the same as an argument.

**The rigged Hilbert space.** Position eigenstates $|x\rangle$ are not in $L^2(\mathbb{R})$. They live in a strictly larger space — the "rigged Hilbert space" or Gelfand triple construction. Undergraduate courses elide this. Ballentine *Quantum Mechanics: A Modern Development* Ch. 1 handles it carefully.
<!-- FACT-CHECK FLAG: UNVERIFIED — see factchecks/02-mathematical-foundations-assertions.md -->

**Why is the state space projective?** The state $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ make identical physical predictions for every observable. The "real" state space is normalized vectors modulo global phase — projective Hilbert space. The formalism carries a redundancy the physics doesn't need. One answer: the redundancy is the price of linearity, which you need for superposition. Whether there is a deeper structural reason remains open.

---

## LLM exercises

The following exercises are designed to be worked interactively with a language model. Use the model to check your reasoning step by step — not to generate answers, but to test whether you can explain each step clearly enough that the model can follow and push back.

**L1.** Ask the model to give you a random normalized state in $\mathbb{C}^2$ with complex coefficients. Compute its bra by hand. Then compute the norm $\langle\psi|\psi\rangle$ step by step and verify it equals 1. Have the model check each arithmetic step and explain where you are applying the conjugation rule.

**L2.** Give the model any $2 \times 2$ Hermitian matrix you construct. Ask it to compute the eigenvalues and eigenvectors. Then do the same computation yourself from scratch using the characteristic polynomial. Compare the results and ask the model to explain any discrepancy in terms of the steps in the derivation.

**L3.** Dictate a proof to the model that $\hat{p} = -i\hbar\,d/dx$ is Hermitian, in natural language — no formulas allowed in your explanation. Ask the model to translate your words into the integral calculation and identify any step you described incorrectly or imprecisely.

**L4.** Construct the operator $|\!\uparrow\rangle\langle\!\downarrow|$ as a $2 \times 2$ matrix. Ask the model: is this operator Hermitian? What are its eigenvalues? Can you use it as an observable? Walk through each question yourself before asking. Then ask the model whether your conclusions about Hermitian, non-Hermitian, and anti-Hermitian operators were correct.

**L5.** Ask the model to generate a state $|\psi\rangle \in \mathbb{C}^2$ and then walk you through computing $\langle\sigma_z\rangle$, $\langle\sigma_x\rangle$, and $\langle\sigma_y\rangle$ in sequence. After each calculation, check that the result is real. If any result is not real, identify the error before asking the model where it is.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Stueckelberg, E. C. G. "Quantum theory in real Hilbert space." *Helvetica Physica Acta* 33, 727–752 (1960).
2. Renou, M.-O. et al. "Quantum theory based on real numbers can be experimentally falsified." *Nature* 600, 625–629 (2021). https://doi.org/10.1038/s41586-021-04160-4
3. Dirac, P. A. M. "A new notation for quantum mechanics." *Mathematical Proceedings of the Cambridge Philosophical Society* 35, 416–418 (1939). https://doi.org/10.1017/S0305004100021162
4. Reed, M. & Simon, B. *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness*. Academic Press, 1975.
5. Bender, C. M. & Boettcher, S. "Real Spectra in Non-Hermitian Hamiltonians Having PT Symmetry." *Physical Review Letters* 80, 5243 (1998). https://doi.org/10.1103/PhysRevLett.80.5243
6. Adler, S. L. *Quaternionic Quantum Mechanics and Quantum Fields*. Oxford University Press, 1995.
