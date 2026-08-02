# Chapter 5 — Quantum Formalism

## TL;DR

- Two students sit in a library with two papers.
- The chapter moves through The five postulates, The uncertainty principle: what Robertson actually proved, Compatible observables and commutators, The measurement problem: what is actually unsettled, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Four Postulates Are Settled. One Is Not. The Difference Matters.*

---

Two students sit in a library with two papers. The first is Werner Heisenberg's 1927 paper in *Zeitschrift für Physik* — the one with the gamma-ray microscope thought experiment. The second is Howard P. Robertson's two-page note in *Physical Review*, 1929, titled simply "The Uncertainty Principle."

The first student says: uncertainty is about measurement. To find an electron's position, you bounce a photon off it. The photon kicks the electron and disturbs its momentum. That is the principle. Their popular-physics book says essentially the same thing with a balloon: to find a balloon in the dark you have to bump into it, and bumping moves it. That is what $\Delta x\,\Delta p \gtrsim \hbar$ means.

The second student says: read Robertson. The inequality is a property of the *state*. There is no measurement in the proof. The state itself has a width in position and a width in momentum, and the product of those widths is bounded below by $\hbar/2$. Nobody had to look at the particle. The balloon analogy gets the right answer for the wrong reason.

Both students are partially right. Heisenberg's microscope describes a real physical effect — now formalized as measurement-disturbance uncertainty by Masanao Ozawa in 2003. The Robertson bound is a *different* statement about state preparation. They are related but not identical, and conflating them is exactly the mistake the balloon analogy reproduces. The argument the students are having is the productive one — the one that ends with two different inequalities and one precise statement about what the principle actually says.

This chapter does three things: assembles the five postulates of quantum mechanics cleanly, derives the Robertson bound from scratch, and then tells the truth about the measurement problem — which is that working physicists do not agree about it, and that pretending otherwise would be dishonest.

---

## The five postulates

A theory is not its applications. It is the small set of statements from which the applications follow. Quantum mechanics has five postulates. Here they are, with the physical requirement each one enforces stated alongside.

**Postulate 1 (State).** Every isolated quantum system is associated with a complex Hilbert space $\mathcal{H}$. A pure state is a normalized vector $|\psi\rangle \in \mathcal{H}$, defined up to a global phase: $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ represent the same physical state.

**Postulate 2 (Observables).** Every physical observable $A$ corresponds to a Hermitian operator $\hat{A}$ on $\mathcal{H}$. The eigenvalues of $\hat{A}$ are the possible outcomes of measuring $A$.

Why Hermitian? Because measurement outcomes are real numbers. If $\hat{A}|a\rangle = a|a\rangle$, then $\langle a|\hat{A}|a\rangle = a$. Take the complex conjugate of both sides: $\overline{\langle a|\hat{A}|a\rangle} = \overline{a}$. But $\overline{\langle a|\hat{A}|a\rangle} = \langle a|\hat{A}^\dagger|a\rangle = \langle a|\hat{A}|a\rangle$ if $\hat{A} = \hat{A}^\dagger$. So $a = \overline{a}$, which means $a$ is real. Hermiticity is the algebraic encoding of "outcomes are real numbers." It is not arbitrary; it is forced.

**Postulate 3 (Born rule).** If the system is in state $|\psi\rangle$ and a measurement of $A$ is performed, the probability of obtaining eigenvalue $a_n$ is

$$P(a_n) = |\langle a_n | \psi \rangle|^2,$$

where $|a_n\rangle$ is the normalized eigenstate corresponding to $a_n$.

**Postulate 4 (Collapse).** Immediately after the measurement yields outcome $a_n$, the state of the system is $|a_n\rangle$. This postulate carries almost all the philosophical weight in quantum mechanics. The last section of this chapter is about what happens when you look at it directly.

**Postulate 5 (Time evolution).** Between measurements, the state evolves unitarily:

$$i\hbar\,\frac{\partial}{\partial t}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle.$$

Equivalently, $|\psi(t)\rangle = e^{-i\hat{H}t/\hbar}|\psi(0)\rangle$ for time-independent $\hat{H}$, and the evolution operator $\hat{U}(t) = e^{-i\hat{H}t/\hbar}$ is unitary: $\hat{U}^\dagger \hat{U} = \hat{1}$. Why unitary? Because probability must be conserved:

$$\langle \psi(t)|\psi(t)\rangle = \langle\psi(0)|\hat{U}^\dagger\hat{U}|\psi(0)\rangle = \langle\psi(0)|\psi(0)\rangle = 1$$

requires $\hat{U}^\dagger\hat{U} = \hat{1}$. Unitarity is the algebraic encoding of "total probability is always one."

| postulate number | name | one-sentence statement | physical requirement enforced |
| --- | --- | --- | --- |
| 1 | State | A system is represented by a normalized vector $|\psi\rangle$ in Hilbert space. | Total probability is 1. |
| 2 | Observables | Measurable quantities are Hermitian operators. | Measurement outcomes are real eigenvalues. |
| 3 | Born rule | Outcome probabilities are squared projection amplitudes, $|\langle a_n|\psi\rangle|^2$. | Probabilities come from state expansion in an eigenbasis. |
| 4 | Collapse | After outcome $a_n$, the state is $|a_n\rangle$. | Repeat measurements give the same outcome. |
| 5 | Time evolution | Between measurements, states evolve by the Schrödinger equation. | Norm and total probability are conserved. |

One structural observation that matters: Postulates 1, 2, 3, and 5 are uncontroversial among working physicists. Every interpretation of quantum mechanics uses them unchanged. Postulate 4 is where the interpretations diverge. Copenhagen accepts collapse as a postulate. Many-Worlds denies collapse happens at all. Bohmian mechanics replaces it with a deterministic guidance equation. The mathematics is the same across all these views; the story about what the mathematics is describing is not. Hold that structure in mind from here on — four settled postulates, one contested postulate, and a century of literature trying to figure out what to do about the contested one.

---

## The uncertainty principle: what Robertson actually proved

Here is the correction the students in the library were working toward.

The balloon analogy captures Heisenberg's 1927 physical intuition: measuring position with precision $\Delta x$ requires a photon of wavelength $\lambda \lesssim \Delta x$, that photon carries momentum $\sim h/\Delta x$, the scattering transfers some of that to the electron, so $\Delta p \gtrsim h/\Delta x$, and the product $\Delta x\,\Delta p \gtrsim h$. The intuition is correct. But it is a story about what *one measurement does to a subsequent one*. The uncertainty is about measurement disturbance.

Robertson's 1929 paper proved a theorem — not a thought experiment, a theorem — that is about the state itself, before any measurement. For any two Hermitian operators $\hat{A}$ and $\hat{B}$ and any state $|\psi\rangle$:

$$\sigma_A\,\sigma_B \;\geq\; \tfrac{1}{2}\bigl|\langle[\hat{A}, \hat{B}]\rangle\bigr|$$

where $\sigma_A^2 = \langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2$ is the variance of $A$ in state $|\psi\rangle$, and $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ is the commutator. The derivation is short enough to do here. It uses nothing beyond linear algebra on a Hilbert space.

Define the shifted operators

$$\hat{A}' = \hat{A} - \langle\hat{A}\rangle, \qquad \hat{B}' = \hat{B} - \langle\hat{B}\rangle.$$

These are still Hermitian, have zero mean, and satisfy $\sigma_A^2 = \langle\hat{A}'^2\rangle$, $\sigma_B^2 = \langle\hat{B}'^2\rangle$. Define two vectors in the Hilbert space:

$$|f\rangle = \hat{A}'|\psi\rangle, \qquad |g\rangle = \hat{B}'|\psi\rangle.$$

Their squared norms are $\langle f|f\rangle = \sigma_A^2$ and $\langle g|g\rangle = \sigma_B^2$. The Cauchy–Schwarz inequality applied to these vectors says

$$\langle f|f\rangle\,\langle g|g\rangle \;\geq\; |\langle f|g\rangle|^2,$$

so $\sigma_A^2\sigma_B^2 \geq |\langle\psi|\hat{A}'\hat{B}'|\psi\rangle|^2$. For any complex number $z$, $|z|^2 \geq (\text{Im}\,z)^2$, so

$$\sigma_A^2\sigma_B^2 \;\geq\; \bigl(\text{Im}\,\langle\psi|\hat{A}'\hat{B}'|\psi\rangle\bigr)^2.$$

Now the imaginary part. For any complex number $z$, $\text{Im}\,z = (z - \overline{z})/(2i)$. The conjugate of $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ is $\langle\psi|\hat{B}'^\dagger\hat{A}'^\dagger|\psi\rangle = \langle\psi|\hat{B}'\hat{A}'|\psi\rangle$ (shifted operators are still Hermitian). So

$$\text{Im}\,\langle\psi|\hat{A}'\hat{B}'|\psi\rangle = \frac{1}{2i}\bigl(\langle\psi|\hat{A}'\hat{B}'|\psi\rangle - \langle\psi|\hat{B}'\hat{A}'|\psi\rangle\bigr) = \frac{1}{2i}\langle\psi|[\hat{A}', \hat{B}']|\psi\rangle.$$

The commutator of the shifted operators equals the commutator of the originals: $[\hat{A}', \hat{B}'] = [\hat{A}, \hat{B}]$. And $[\hat{A}, \hat{B}]/i$ is Hermitian, so this imaginary part is real — consistent. Squaring:

$$\sigma_A^2\sigma_B^2 \;\geq\; \frac{1}{4}\bigl|\langle[\hat{A}, \hat{B}]\rangle\bigr|^2,$$

which is the Robertson bound. That is the whole proof: Cauchy–Schwarz on shifted operators, isolate the imaginary part, the commutator falls out.

![Proof structure flowchart ](../images/05-quantum-formalism-fig-01.png)
*Figure 5.1 — Proof structure flowchart *

For position and momentum, $[\hat{x}, \hat{p}] = i\hbar$ — a constant, independent of the state — so $|\langle[\hat{x}, \hat{p}]\rangle| = \hbar$ for every state, and

$$\sigma_x\,\sigma_p \;\geq\; \frac{\hbar}{2}.$$

Notice $\hbar/2$, not $\hbar$. The factor of two is part of the answer. Many popular treatments drop it. Dropping it is wrong.

Schrödinger in 1930 strengthened this by keeping both the real and imaginary parts of $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ in the inequality instead of discarding the real part. The result is

$$\sigma_A^2\sigma_B^2 \;\geq\; \left(\tfrac{1}{2}\langle\{\hat{A}', \hat{B}'\}\rangle\right)^2 + \left(\tfrac{1}{2i}\langle[\hat{A}, \hat{B}]\rangle\right)^2$$

where $\{\hat{A}', \hat{B}'\} = \hat{A}'\hat{B}' + \hat{B}'\hat{A}'$ is the anticommutator of the shifted operators (its expectation is twice the covariance). When the covariance is zero, Schrödinger's bound collapses to Robertson's. When it is not, Schrödinger's is tighter. The derivation is the same — just stop before throwing away the real part.

Now the balloon analogy correction, stated precisely. The Robertson bound is a statement about the state $|\psi\rangle$. It says: there is no quantum state for which $\sigma_A$ and $\sigma_B$ are simultaneously smaller than the right-hand side. That bound holds before anyone measures anything. There is no apparatus in the inequality. There is no photon, no kick, no bump in the dark. The uncertainty is intrinsic to the state, derived from the algebra of non-commuting operators on a Hilbert space.

The balloon analogy gets the order-of-magnitude answer right and is faithful to Heisenberg's 1927 pedagogical motivation. But it gives a wrong picture of what the inequality is. A student trained on the balloon will conflate state preparation with measurement disturbance — which is exactly the conflation physicists worked out of the theory by 1930. Masanao Ozawa, in 2003, formalized the measurement-disturbance version into its own separate inequality, one that mixes the state uncertainty with the apparatus noise and the disturbance the apparatus inflicts on subsequent measurements. Experimental tests (Erhart et al., *Nature Physics*, 2012) confirmed Ozawa's version and showed that the measurement-disturbance product can be made *smaller* than the naive Heisenberg microscope suggests. The Robertson bound is preparation uncertainty. Ozawa's is measurement-disturbance uncertainty. They are related but not the same inequality, and the balloon never told you there were two.

| paper | year | type of uncertainty | what varies | mathematical form |
| --- | --- | --- | --- | --- |
| Heisenberg | 1927 | Measurement-disturbance intuition | Apparatus resolution and recoil | $\Delta x\,\Delta p \sim h$ as an order-of-magnitude microscope argument |
| Robertson | 1929 | Preparation uncertainty | The quantum state | $\sigma_A\sigma_B \ge \frac{1}{2}|\langle[\hat A,\hat B]\rangle|$ |
| Schrödinger | 1930 | Preparation uncertainty with covariance | The quantum state | Robertson bound plus the anticommutator/covariance term |
| Ozawa | 2003 | Measurement noise and disturbance | Apparatus noise, disturbance, and state spread | $\epsilon(A)\eta(B)+\epsilon(A)\sigma_B+\sigma_A\eta(B)\ge\frac{1}{2}|\langle[\hat A,\hat B]\rangle|$ |

**The ground state saturates the bound.** This is the claim that ties the formalism back to Chapter 4. The harmonic-oscillator ground state is

$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\exp\!\left(-\frac{m\omega x^2}{2\hbar}\right).$$

Computing $\sigma_x$ and $\sigma_p$ directly: the Gaussian $e^{-\alpha x^2/2}$ with $\alpha = m\omega/\hbar$ gives

$$\sigma_x^2 = \langle x^2\rangle = \frac{1}{2\alpha} = \frac{\hbar}{2m\omega}, \qquad \sigma_p^2 = \langle p^2\rangle = \frac{\hbar^2\alpha}{2} = \frac{\hbar m\omega}{2}.$$

The product:

$$\sigma_x\,\sigma_p = \sqrt{\frac{\hbar}{2m\omega}}\cdot\sqrt{\frac{\hbar m\omega}{2}} = \frac{\hbar}{2}.$$

Exactly the floor. The ground state achieves equality in the Robertson bound — it is a minimum-uncertainty state. For the $n$-th excited state, the same computation (using ladder operators to evaluate $\langle\hat{x}^2\rangle$ and $\langle\hat{p}^2\rangle$) gives $\sigma_x\sigma_p = (n + 1/2)\hbar$, which exceeds $\hbar/2$ for all $n \geq 1$. Only the ground state saturates.

The zero-point energy and the saturation of the Robertson bound are the same fact, seen from two angles. The state's product-of-widths floor and the state's energy floor are two faces of one constraint: a confined quantum state cannot have zero kinetic energy and cannot be simultaneously sharp in $x$ and $p$. These are not two separate properties of the harmonic oscillator. They are one property.

---

## Compatible observables and commutators

The Robertson bound says what happens when operators do not commute. The natural next question is: what happens when they do?

Two Hermitian operators $\hat{A}$ and $\hat{B}$ are compatible if $[\hat{A}, \hat{B}] = 0$. The Robertson bound then gives $\sigma_A\sigma_B \geq 0$, which is trivially satisfied — there is no joint-uncertainty floor. More than that: compatible operators admit a common eigenbasis. There exists a basis $\{|n\rangle\}$ such that every $|n\rangle$ is simultaneously an eigenstate of both $\hat{A}$ and $\hat{B}$, labeled by both eigenvalues $(a_n, b_n)$. The state can be sharp in both observables simultaneously, because the measurements of $A$ and $B$ do not interfere with each other.

Some examples. $[\hat{x}, \hat{p}_y] = 0$: position along one axis and momentum along a perpendicular axis are compatible. $[\hat{x}, \hat{p}_x] = i\hbar$: position and momentum along the same axis are incompatible. $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ (Chapter 7): components of angular momentum along different axes are incompatible. $[\hat{L}^2, \hat{L}_z] = 0$: the squared magnitude of angular momentum and one component are compatible.

That last pair matters because it explains why hydrogen orbitals are labeled the way they are. The operators $\hat{H}$, $\hat{L}^2$, $\hat{L}_z$ all commute with each other. They share a common eigenbasis. Their eigenvalues — $n$, $\ell$, $m$ — label the states, which is why those particular quantum numbers appear and not others. The label set is exactly the set of commuting operators whose eigenvalues uniquely specify every basis state. This structure has a name: a complete set of commuting observables, or CSCO.

A CSCO is a maximal set of mutually commuting Hermitian operators whose joint eigenvalues uniquely identify every state in the eigenbasis. For hydrogen the CSCO is $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$, yielding the labels $(n, \ell, m, m_s)$. The periodic table's quantum numbers are the CSCO's joint eigenvalues. The reason there are exactly these labels, arranged this way, is that this is the largest set of operators that all commute.

There is a connection to conservation laws that is worth naming. In the Heisenberg picture (where operators evolve and states stay fixed), the time derivative of any observable $\hat{O}$ with no explicit time dependence is

$$\frac{d\hat{O}}{dt} = \frac{i}{\hbar}[\hat{H}, \hat{O}].$$

If $[\hat{H}, \hat{O}] = 0$, then $d\hat{O}/dt = 0$ — the observable is a constant of the motion, conserved. Operators that commute with the Hamiltonian are conserved quantities. The connection between symmetry, commuting operators, and conservation laws runs from here all the way through Chapters 6 and 7. The CSCO structure is the quantum version of that connection.

One misconception to correct before moving on. Non-commuting does not mean unmeasurable. You can measure $\hat{x}$ and then measure $\hat{p}$ in sequence. Each measurement is well-defined individually. What you cannot do is prepare a state that is simultaneously sharp in both, because the Robertson bound forbids it. The cost of sequential measurement is that the second disturbs the first: after measuring $\hat{x}$ and obtaining $x_0$, the state is (approximately) $|x_0\rangle$, which is completely uncertain in $p$. Measuring $\hat{p}$ then collapses to some $|p_0\rangle$, which is completely uncertain in $x$. Re-measuring $\hat{x}$ gives a random result. Non-commuting observables have no simultaneous values. That is the statement.

---

## The measurement problem: what is actually unsettled

Here the chapter must be honest. The previous sections — postulates, Robertson bound, commutators — are well-settled. The content below is not. The distinction matters, and the chapter refuses to paper over it.

Postulate 4 says that upon measurement, the state collapses to the corresponding eigenstate. The problem is that a measurement is itself a physical interaction between a quantum system and a physical apparatus. The apparatus is made of atoms, which are quantum. So why is the apparatus described classically? Why are there two laws of evolution — unitary Schrödinger evolution between measurements, discontinuous collapse during them — with the switching rule being "when a measurement occurs"? And what counts as a measurement?

John Bell, writing in *Physics World* in 1990 in a piece titled "Against 'Measurement'": a fundamental theory should not have the word "measurement" in its postulates. The apparatus is made of quantum constituents; it should evolve by the same dynamics as the system. If collapse is real, it should follow from the dynamics, not be inserted by hand. Bell wrote that sixty-two years after Schrödinger, the field deserved an exact formulation. As of now it does not have one that physicists agree on.

The live interpretations diverge here. The chapter names them; it does not adjudicate.

**Copenhagen** (Bohr, Heisenberg, circa 1927). Quantum systems are described by $|\psi\rangle$; the apparatus is described classically; collapse is a postulate. This is the textbook version, the one working physicists default to for calculation. Its strength is operational clarity. Its weakness is the unspecified quantum-classical boundary and the unspecified definition of "measurement."

**Many-Worlds / Everett** (Hugh Everett III, *Reviews of Modern Physics*, 1957). There is no collapse. The combined system-plus-apparatus-plus-observer evolves unitarily; what looks like collapse is the observer becoming correlated with one branch of a larger superposition. All outcomes occur in different branches. Strength: removes the postulate Bell objected to. Weakness: probabilities now refer to branches — what does it mean to assign probability $|\langle a_n|\psi\rangle|^2$ to outcome $a_n$ when all outcomes occur somewhere? Decision-theoretic derivations (Deutsch 1999, Wallace 2010) attempt an answer; critics dispute whether the derivation is circular.

**Bohmian / pilot-wave** (de Broglie 1927, Bohm 1952). Particles have definite positions at all times, guided by a pilot wave $\psi$ that evolves by Schrödinger's equation. Collapse follows from the dynamics. Strength: deterministic, no measurement problem. Weakness: explicitly nonlocal in a way that is technically consistent with quantum-mechanical predictions but uncomfortable for extension to relativistic quantum field theory.

**QBism** (Caves, Fuchs, Schack, circa 2002). The wave function is the agent's degree of belief about future measurement outcomes. The Born rule is a normative rule for updating those beliefs. Collapse is a Bayesian update. Strength: the measurement problem dissolves because $|\psi\rangle$ was never a physical thing in the first place. Weakness: many physicists find the anti-realist reading of $|\psi\rangle$ unacceptable — it seems to say that quantum mechanics is not about the world but about what we should believe about the world.

**Dynamical collapse models** (Ghirardi, Rimini, Weber, 1986; Continuous Spontaneous Localization, Pearle 1989). The Schrödinger equation is modified by a small nonlinear stochastic term that causes spontaneous localization at a rate proportional to mass. For a single particle, the modification is negligible. For a macroscopic object, the collective effect forces the system into a definite classical state. Collapse is now a real physical process, not a postulate. Strength: testable — the models predict small deviations from standard quantum mechanics. Weakness: no positive experimental signal has yet appeared. Cantilever and matter-wave experiments have been tightening upper bounds on the GRW/CSL parameters without confirming the models.

**Decoherence** (Zurek and others, circa 1970s onward). Not strictly an interpretation — a mechanism. Interaction with the environment rapidly suppresses interference between macroscopically distinct states, producing apparent classical behavior. Decoherence explains why you do not see superpositions of a live cat and a dead cat. It does not explain which specific outcome you observe — it eliminates the off-diagonal coherences but leaves the diagonal terms, and the question of which diagonal term you got is exactly the measurement problem restated. Decoherence is part of the answer every interpretation must incorporate. It is not a complete answer by itself.

| name | what replaces collapse | what ψ represents | strength | weakness |
| --- | --- | --- | --- | --- |
| Copenhagen | Collapse as a postulate | A state used to predict measurement outcomes | Clear operational recipe | Vague measurement boundary |
| Many-Worlds / Everett | Branching under unitary evolution | A real universal wave function | Removes collapse postulate | Probability in branching worlds is contested |
| Bohmian / pilot-wave | Deterministic particle trajectories guided by $\psi$ | A real guiding field | Definite ontology | Explicit nonlocality and difficult QFT extension |
| QBism | Bayesian updating by an agent | Personal degrees of belief | Dissolves the measurement problem | Anti-realist reading is controversial |
| Dynamical collapse | Stochastic physical localization | A physical state subject to modified dynamics | Testable deviations from standard QM | No confirmed signal |
| Decoherence | Environmental suppression of interference | Standard quantum state of system plus environment | Explains classical-looking records | Does not select a single outcome |

In 2013, Maximilian Schlosshauer, Johannes Kofler, and Anton Zeilinger surveyed 33 physicists at a specialist foundations conference. The most popular position was Copenhagen-flavored (around 42%), followed by information-based or QBism-adjacent views (around 24%), then Many-Worlds (around 18%), with smaller minorities for Bohm, collapse models, and others. The sample is small and self-selected — these were foundations specialists, not a random draw of physicists — but the headline is robust: *there is no consensus*. Working physicists disagree about what their own most successful theory is describing.

One misconception the chapter corrects explicitly: "the observer's consciousness causes wave function collapse." This is the von Neumann–Wigner interpretation, sketched by Wigner in a 1961 essay and largely abandoned even by him afterward. The 2013 survey found essentially no support for it. The pop-science framing of "the observer creates reality" trades on this idea and should be pushed back on. There is a genuine measurement problem; consciousness is not the mainstream answer; decoherence is the mainstream mechanism for the quantum-to-classical transition; the interpretive disagreement is about whether decoherence plus something — and which something — closes the problem.

One recent result that sharpened the debate. Daniela Frauchiger and Renato Renner, writing in *Nature Communications* in 2018, constructed a thought experiment in which different observers, each reasoning consistently within quantum mechanics, reach contradictory conclusions about a measurement outcome. Every interpretation resolves the apparent paradox by giving up a different assumption: Copenhagen by restricting which observers count, Many-Worlds by clarifying what "outcome" means across branches. Vilasini and Renner's 2024 follow-up ([*Nature Communications* 15, 7155](https://doi.org/10.1038/s41467-024-47170-2)) examined which assumption each interpretation must drop. The point is not that any interpretation failed — each survives by making its choice explicit. The point is that the choice is forced. The foundations are still under active construction.

---

## Where the postulates stand

Let me state the situation clearly at the end, because it is the kind of clarity that textbooks sometimes sacrifice for tidiness.

The five postulates work. They predict experimental outcomes to many decimal places across every domain where they have been tested. Postulates 1, 2, 3, and 5 are not in serious dispute. Every computation in this course rests on them, and there is no credible challenge to any of them from experiment. Postulate 4 — collapse — has a well-defined mathematical content that all physicists use and no physicist seriously proposes discarding. What is in dispute is what it *means*, what it *describes*, and whether it should be derivable from the other four rather than postulated separately.

A working physicist can compute with all five postulates without committing to an interpretation. The calculation is interpretation-independent; the prediction is the same under Copenhagen, Many-Worlds, Bohm, and QBism. The interpretation question matters for what we think the theory is *about* — whether the wave function describes reality, our beliefs, a branching multiverse, or a pilot field. That question is open. The chapter that ends here does not pretend it is closed, because it is not.

---

## Exercises

**Warm-up**

**W1.** State the five postulates from memory in one sentence each. For each, identify the physical requirement it enforces — "real measurement outcomes," "conserved probability," and so on. Then identify which single postulate every interpretation of quantum mechanics modifies, replaces, or reinterprets, and state in one sentence what each of the six interpretations surveyed in this chapter does to it. *(The first part is recall; the second part tests whether the student has absorbed the settled/contested distinction.)*

**W2.** Prove in two lines that the eigenvalues of any Hermitian operator are real. Then prove in two lines that eigenvectors corresponding to distinct eigenvalues are orthogonal. Both are the same style of calculation as the Hermiticity argument in the postulate discussion — start from $\hat{A}|a\rangle = a|a\rangle$, take an inner product, use $\hat{A} = \hat{A}^\dagger$. *(Direct application of the Hermitian machinery; a student who cannot do these two proofs does not yet own Postulate 2.)*

**W3.** Compute $[\hat{x}, \hat{p}]$ explicitly by acting on an arbitrary test function $f(x)$, using $\hat{x}f = xf$ and $\hat{p}f = -i\hbar\,\partial_x f$. Verify that $[\hat{x}, \hat{p}]f = i\hbar f$ for all $f$, so $[\hat{x}, \hat{p}] = i\hbar\hat{1}$. *(The commutation relation is used throughout the rest of the course; this exercise ensures the student can derive it rather than just cite it.)*

**Application**

**A1.** For the $n = 1$ infinite-square-well state $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$, compute $\sigma_x$ and $\sigma_p$ explicitly. Confirm that $\sigma_x\sigma_p > \hbar/2$, so the Robertson bound is satisfied but not saturated. Compute the ratio $\sigma_x\sigma_p\,/\,(\hbar/2)$ numerically and compare to the harmonic-oscillator ground state (ratio = 1) and the harmonic-oscillator $n = 1$ state (ratio = 3). Which state comes closest to saturating the bound, and why does the box ground state not saturate it? *(The Gaussian shape is the key — the box wave function is not Gaussian, and that is why equality fails.)*

**A2.** Use the ladder operators to compute $\sigma_x$ and $\sigma_p$ for the $n$-th harmonic-oscillator eigenstate. Write $\hat{x}$ and $\hat{p}$ in terms of $\hat{a}_\pm$, apply $\hat{a}_-|n\rangle = \sqrt{n}\,|n-1\rangle$ and $\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle$, and show that $\sigma_x\sigma_p = (n + 1/2)\hbar$. Confirm that only $n = 0$ saturates the Robertson bound. *(Builds ladder-operator fluency while revisiting the Chapter 4 ground-state result from the formalism angle.)*

**A3.** A beam of spin-1/2 particles is prepared in state $|\uparrow_z\rangle$. It passes through three Stern–Gerlach magnets oriented $z$, then $x$, then $z$. Using $|\uparrow_x\rangle = (|\uparrow_z\rangle + |\downarrow_z\rangle)/\sqrt{2}$ and the Born rule, compute the probability that a particle emerges from the final $z$-magnet in state $|\uparrow_z\rangle$. Then explain in two sentences why the final $z$-measurement gives a 50/50 split even though the beam started as pure $|\uparrow_z\rangle$. *(Tests the Born rule and Postulate 4 together; the explanation requires the student to name what the intermediate $x$-measurement did to the state.)*

**Synthesis**

**S1.** The Robertson derivation in this chapter discards the real part of $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ at the step $|z|^2 \geq (\text{Im}\,z)^2$. Schrödinger's 1930 strengthening keeps it. (a) Write down the Schrödinger bound explicitly, identifying the anticommutator term. (b) For the harmonic-oscillator ground state, compute $\tfrac{1}{2}\langle\{\hat{x}', \hat{p}'\}\rangle$ (the covariance term) and show it vanishes, so the Robertson and Schrödinger bounds coincide for this state. (c) Identify a state for which the covariance would not vanish — what does a nonzero covariance mean physically in terms of the joint distribution of $x$ and $p$? *(Ties the algebraic structure of the proof to the geometry of phase-space distributions; the covariance question is the one Schrödinger's paper was actually answering.)*

**S2.** Pick one interpretation of quantum mechanics from this chapter. State clearly what it says about Postulate 4 — whether it retains collapse as a postulate, replaces it with something else, or reinterprets what collapse means. Then identify one specific experimental scenario — not a thought experiment, a real class of laboratory experiment — for which your chosen interpretation gives the same prediction as Copenhagen, and one for which the predictions would differ (even if the difference is currently unmeasurable). Conclude with whether you find the interpretation more or less satisfying than Copenhagen and name your reason precisely. *(The student must engage the physics, not just describe the interpretation; the instruction to name a real experiment forces them off pure philosophy. There is no right answer — only honest ones.)*

**Challenge**

**C1.** The Robertson bound states $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$. For most observables, the right-hand side depends on the state $|\psi\rangle$ through the expectation value of the commutator. For position and momentum, $[\hat{x},\hat{p}] = i\hbar$ is a *c*-number — it does not depend on the state — so the bound is the same for every state: $\sigma_x\sigma_p \geq \hbar/2$ always. (a) Find a pair of observables for which the commutator is *not* a *c*-number (i.e., it depends on the state), and write down their commutator. (b) Show that for eigenstates of $\hat{L}_z$ with eigenvalue $m\hbar$, the Robertson bound for $\hat{L}_x$ and $\hat{L}_y$ is $\sigma_{L_x}\sigma_{L_y} \geq \tfrac{1}{2}|m|\hbar^2$. (c) For $m = 0$ the bound gives zero — does this mean you can simultaneously know $L_x$ and $L_y$ exactly? Explain using the commutation relations $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$. *(The $m = 0$ case is a subtlety that Griffiths §4.3 addresses and that trips up most students; the Robertson bound can be zero even when the operators do not commute, if the state is special enough.)*

---

## LLM Exercises

**LLM-E1.** Ask a language model to state the five postulates of quantum mechanics. Evaluate the response: does it give exactly five, and are they the right five? Does it correctly identify which postulate encodes conservation of probability (Postulate 5 / unitarity) and which encodes real measurement outcomes (Postulate 2 / Hermiticity)? Does it include Postulate 4 (collapse) without noting that it is the contested one?

**LLM-E2.** Ask a language model to explain the uncertainty principle using an analogy. Then ask it whether the analogy describes preparation uncertainty, measurement-disturbance uncertainty, or both. Evaluate whether it can distinguish Robertson 1929 from Heisenberg 1927. Ask it to state the Robertson bound with the correct factor of $\hbar/2$ (not $\hbar$). Does it get the factor right on the first try?

**LLM-E3.** Paste the Robertson derivation from this chapter into a language model — from "Define the shifted operators..." through the final Robertson bound — and ask it to verify every step. Where does it confirm the algebra, where does it flag a real error, and where does it hallucinate a problem that does not exist? Pay particular attention to the step where the imaginary part is extracted from $\langle\psi|\hat{A}'\hat{B}'|\psi\rangle$ — this is the step most often glossed over.

**LLM-E4.** Ask a language model: "Which interpretation of quantum mechanics is correct?" Evaluate whether the response honestly represents the lack of consensus, or whether it picks a winner. A strong response names the major interpretations, states what each one says about collapse, and acknowledges that working physicists disagree. A weak response quietly endorses Copenhagen (or Many-Worlds) without flagging the disagreement. Compare the response to the Schlosshauer-Kofler-Zeilinger 2013 survey result.

**LLM-E5.** Give a language model this sentence from a popular-physics book: "The act of observation causes the wave function to collapse — the observer creates reality." Ask it to evaluate the claim carefully. A strong response will distinguish the measurement problem (genuine, unresolved) from the consciousness-causes-collapse interpretation (not the mainstream answer), invoke decoherence as the standard mechanism for the quantum-to-classical transition, and identify what is misleading about the "observer creates reality" framing without dismissing the underlying question as trivial.

---

## References

*Added by fact-check pass 2026-05-14.*

1. Robertson, H. P. "The Uncertainty Principle." *Physical Review* 34, 163–164 (1929). https://journals.aps.org/pr/abstract/10.1103/PhysRev.34.163
2. Ozawa, M. "Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement." *Physical Review A* 67, 042105 (2003). https://doi.org/10.1103/PhysRevA.67.042105
3. Erhart, J., Sponar, S., Sulyok, G., Badurek, G., Ozawa, M. & Hasegawa, Y. "Experimental demonstration of a universally valid error–disturbance uncertainty relation in spin measurements." *Nature Physics* 8, 185–189 (2012). https://doi.org/10.1038/nphys2194
4. Schrödinger, E. "Zum Heisenbergschen Unschärfeprinzip." *Sitzungsber. Preuss. Akad. Wiss.* 14, 296–303 (1930).
5. Bell, J. S. "Against 'measurement.'" *Physics World* 3 (8), 33–40 (1990).
6. Everett, H., III. "'Relative State' Formulation of Quantum Mechanics." *Reviews of Modern Physics* 29, 454–462 (1957). https://doi.org/10.1103/RevModPhys.29.454
7. Bohm, D. "A Suggested Interpretation of the Quantum Theory in Terms of 'Hidden' Variables." *Physical Review* 85, 166, 180 (1952).
8. Schlosshauer, M., Kofler, J. & Zeilinger, A. "A Snapshot of Foundational Attitudes Toward Quantum Mechanics." *Studies in History and Philosophy of Modern Physics* 44, 222–230 (2013). https://doi.org/10.1016/j.shpsb.2013.04.004
9. Frauchiger, D. & Renner, R. "Quantum theory cannot consistently describe the use of itself." *Nature Communications* 9, 3711 (2018). https://doi.org/10.1038/s41467-018-05739-8
10. Wigner, E. P. "Remarks on the Mind-Body Question," in *The Scientist Speculates*, ed. I. J. Good, Heinemann (1961), pp. 284–302.
