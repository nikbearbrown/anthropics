# Chapter 3 — Commutators, Compatibility, and the Generalized Uncertainty Principle

When two observables are measured on a large ensemble of identically prepared systems, the spread in their outcomes is not simply a technical limitation — it is a property of the quantum state itself. If we prepare a million electrons in the same state $|\psi\rangle$, measure position on half of them and momentum on the other half (so no electron is disturbed twice), the standard deviations $\sigma_x$ and $\sigma_p$ computed from the two histograms always satisfy $\sigma_x\sigma_p \geq \hbar/2$.

This inequality is present before any measuring device turns on. It is built into the algebra of the operators during preparation. The correct statement is: *no quantum state has* $\sigma_x = 0$ *and* $\sigma_p = 0$ *simultaneously.* Robertson proved this in 1929 with a two-line application of the Cauchy-Schwarz inequality to the commutator $[\hat{x}, \hat{p}] = i\hbar$. We begin with that commutator and develop its consequences systematically.

---

## What a Commutator Measures

The **commutator** of two operators is:

$$[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}.$$

When $[\hat{A}, \hat{B}] = 0$, the operators are **compatible**. When it is nonzero, they are **incompatible**. These names carry a precise theorem.

**Compatible operators share a complete orthonormal eigenbasis.** The proof in the non-degenerate case is straightforward. Suppose $[\hat{A}, \hat{B}] = 0$ and $\hat{A}|a\rangle = a|a\rangle$. Apply $\hat{B}$ to the eigenvalue equation:

$$\hat{B}(\hat{A}|a\rangle) = a\hat{B}|a\rangle.$$

Since they commute, $\hat{B}\hat{A} = \hat{A}\hat{B}$, so $\hat{A}(\hat{B}|a\rangle) = a(\hat{B}|a\rangle)$. The vector $\hat{B}|a\rangle$ is itself an eigenvector of $\hat{A}$ with the same eigenvalue $a$. If the eigenspace at $a$ is one-dimensional, then $\hat{B}|a\rangle \propto |a\rangle$ — meaning $|a\rangle$ is simultaneously an eigenvector of $\hat{B}$. For degenerate eigenvalues, $\hat{B}$ maps the degenerate subspace into itself and can be diagonalized within it by Gram-Schmidt. In both cases, a simultaneous eigenbasis exists.

The physical consequence is direct: in a state $|a, b\rangle$ that is simultaneously an eigenstate of $\hat{A}$ with eigenvalue $a$ and of $\hat{B}$ with eigenvalue $b$, both observables take definite values. The **complete set of commuting observables (CSCO)** is the maximal collection of mutually commuting Hermitian operators whose joint eigenvalues uniquely label every state. For the hydrogen atom without spin, $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ forms such a set. The three quantum numbers $(n, \ell, m)$ simultaneously label every energy eigenstate not by assumption or convention, but because these three operators algebraically commute. Commutativity is the reason quantum numbers exist.

<!-- → [DIAGRAM: three-column visual — left column shows two commuting operators A, B with a shared eigenbasis |a,b⟩; middle column shows non-commuting operators with separate eigenbases that cannot coincide; right column shows the hydrogen CSCO {H, L², Lz} with the label triple (n,ℓ,m)] -->

![three-column visual — left column shows two commuting operators A, B with a shared eigenbasis |a,b⟩](../images/03-commutators-and-uncertainty-fig-01.png)
*Figure 3.1 — three-column visual — left column shows two commuting operators A, B with a shared eigenbasis |a,b⟩*

Conversely: if $[\hat{A}, \hat{B}] \neq 0$, no state is simultaneously an eigenstate of both. Any state sharp in $A$ (meaning $\sigma_A = 0$, i.e., an eigenstate of $\hat{A}$) necessarily has $\sigma_B > 0$. Robertson's theorem makes this quantitative.

---

## The Canonical Commutation Relation

The single most important commutator in quantum mechanics is $[\hat{x}, \hat{p}]$. We derive it by applying both orderings to a test function $\psi(x)$, keeping every step of the product rule visible.

$$[\hat{x}, \hat{p}]\,\psi = \hat{x}\bigl(-i\hbar\,\partial_x\psi\bigr) - (-i\hbar\,\partial_x)(x\psi).$$

First term: $\hat{x}$ multiplies by $x$:

$$-i\hbar\,x\,\partial_x\psi.$$

Second term: $\partial_x$ acts on the product $x\psi$ by the product rule:

$$\partial_x(x\psi) = \psi + x\,\partial_x\psi,$$

so the second term is $-(-i\hbar)(\psi + x\,\partial_x\psi) = i\hbar\psi + i\hbar\,x\,\partial_x\psi$.

Subtract first from second (with the sign from the commutator definition):

$$[\hat{x},\hat{p}]\psi = -i\hbar\,x\,\partial_x\psi - (i\hbar\psi + i\hbar\,x\,\partial_x\psi) \cdot(-1) = i\hbar\psi.$$

Wait — assemble it carefully. First term minus second term:

$$\bigl(-i\hbar\,x\,\partial_x\psi\bigr) - \bigl(i\hbar\psi + i\hbar\,x\,\partial_x\psi\bigr) = -i\hbar\,x\,\partial_x\psi - i\hbar\psi - i\hbar\,x\,\partial_x\psi.$$

The two $x\,\partial_x\psi$ terms cancel:

$$[\hat{x},\hat{p}]\psi = i\hbar\psi.$$

Since this holds for every $\psi$:

$$\boxed{[\hat{x}, \hat{p}] = i\hbar.}$$

<!-- → [DIAGRAM: side-by-side calculation showing the two orderings x̂p̂ψ and p̂(x̂ψ) with the product rule term highlighted in a different color, and the cancellation that leaves iℏψ] -->

![side-by-side calculation showing the two orderings x̂p̂ψ and p̂(x̂ψ) with the product rule term highlighted in a different color, and the…](../images/03-commutators-and-uncertainty-fig-02.png)
*Figure 3.2 — side-by-side calculation showing the two orderings x̂p̂ψ and p̂(x̂ψ) with the product rule term highlighted in a different color, and the…*

This is the **canonical commutation relation**. It is a theorem, not a postulate: it follows directly from the operator representations $\hat{x} = $ multiplication by $x$ and $\hat{p} = -i\hbar\partial_x$, which themselves follow from requiring that $\hat{p}$ generates translations and has real eigenvalues. Every statement about position-momentum incompatibility — including the uncertainty principle — is downstream of this three-line derivation.

Two quick extensions worth noting. In three dimensions: $[\hat{x}_i, \hat{p}_j] = i\hbar\delta_{ij}$, while coordinates along different axes commute. And $[\hat{x}^2, \hat{p}] = 2i\hbar\hat{x}$, the quantum version of the classical identity $\{x^2, p\}_\text{Poisson} = 2x$. The general pattern $[\hat{x}^n, \hat{p}] = i\hbar n\hat{x}^{n-1}$ points toward the Dirac quantization rule: replace the classical Poisson bracket $\{f, g\}$ with $[\hat{f}, \hat{g}]/i\hbar$.

---

## The Robertson Uncertainty Principle

**Theorem (Robertson, 1929).** For any two Hermitian operators $\hat{A}$, $\hat{B}$ and any normalized state $|\psi\rangle$:

$$\sigma_A\,\sigma_B \geq \frac{1}{2}\bigl|\langle[\hat{A}, \hat{B}]\rangle\bigr|,$$

where $\sigma_A^2 = \langle\hat{A}^2\rangle - \langle\hat{A}\rangle^2$ is the variance of $A$-outcomes across many identically prepared copies.

The proof has four named steps. Working through them once gives a solid grounding in the result.

**Step 1 — shift to zero mean.** Define $\hat{A}' = \hat{A} - \langle\hat{A}\rangle$ and $\hat{B}' = \hat{B} - \langle\hat{B}\rangle$. Then $\sigma_A^2 = \|\hat{A}'|\psi\rangle\|^2$ and $\sigma_B^2 = \|\hat{B}'|\psi\rangle\|^2$. Shifting by a constant does not change commutators: $[\hat{A}', \hat{B}'] = [\hat{A}, \hat{B}]$.

**Step 2 — Cauchy-Schwarz.** For any two vectors $|u\rangle = \hat{A}'|\psi\rangle$ and $|v\rangle = \hat{B}'|\psi\rangle$:

$$\sigma_A^2\,\sigma_B^2 = \|u\|^2\|v\|^2 \geq |\langle u|v\rangle|^2 = |\langle\psi|\hat{A}'\hat{B}'|\psi\rangle|^2.$$

**Step 3 — decompose the inner product.** Write $\hat{A}'\hat{B}' = \tfrac{1}{2}\{\hat{A}',\hat{B}'\} + \tfrac{1}{2}[\hat{A}',\hat{B}']$. The anticommutator is Hermitian, so its expectation value is real. The commutator $[\hat{A}',\hat{B}'] = [\hat{A},\hat{B}]$ is anti-Hermitian when $\hat{A}$ and $\hat{B}$ are Hermitian, so its expectation value is purely imaginary. A real number and a purely imaginary number add in modulus without cross-terms:

$$|\langle\hat{A}'\hat{B}'\rangle|^2 = \frac{1}{4}\langle\{\hat{A}',\hat{B}'\}\rangle^2 + \frac{1}{4}|\langle[\hat{A},\hat{B}]\rangle|^2.$$

**Step 4 — drop the non-negative term.** The anticommutator term is $\geq 0$, so dropping it only weakens the bound:

$$\sigma_A^2\sigma_B^2 \geq \frac{1}{4}|\langle[\hat{A},\hat{B}]\rangle|^2.$$

Take the positive square root: $\sigma_A\sigma_B \geq \tfrac{1}{2}|\langle[\hat{A},\hat{B}]\rangle|$. $\square$

**Corollary.** Set $\hat{A} = \hat{x}$, $\hat{B} = \hat{p}$. Since $[\hat{x},\hat{p}] = i\hbar$ is an operator identity — a constant, not an operator with state-dependent expectation value — $|\langle[\hat{x},\hat{p}]\rangle| = \hbar$ for every state. Therefore:

$$\sigma_x\sigma_p \geq \frac{\hbar}{2}.$$

This bound is state-independent. It holds for every $|\psi\rangle$ without exception, because the commutator is a c-number rather than an observable that could average to zero.

---

## When the Bound Depends on the State

For operators whose commutator is itself an operator, the right-hand side of Robertson depends on the state through $|\langle[\hat{A},\hat{B}]\rangle|$. The standard example is spin.

The Pauli algebra gives $[\hat{S}_x, \hat{S}_z] = -i\hbar\hat{S}_y$, so:

$$\sigma_{S_x}\sigma_{S_z} \geq \frac{\hbar}{2}|\langle\hat{S}_y\rangle|.$$

At the north pole of the Bloch sphere — the state $|\!\uparrow\rangle$, an eigenstate of $\hat{S}_z$ — $\langle\hat{S}_y\rangle = 0$, the bound is zero, and there is no algebraic obstruction to $\sigma_{S_z} = 0$ (which is indeed the case). At the $\hat{S}_y$ eigenstate $|+y\rangle = (|\!\uparrow\rangle + i|\!\downarrow\rangle)/\sqrt{2}$: $\langle\hat{S}_y\rangle = \hbar/2$, the bound becomes $\hbar^2/4$, and both $\sigma_{S_x}$ and $\sigma_{S_z}$ are forced to $\hbar/2$, saturating the bound exactly.

A zero Robertson bound does not mean both observables can be simultaneously sharp — it means the inequality is not binding for that state. One observable might still be fully spread out. The state $(|+y\rangle + |-y\rangle)/\sqrt{2}$ has $\langle\hat{S}_y\rangle = 0$, giving a zero bound for $\hat{S}_x$ and $\hat{S}_z$; yet both $\sigma_{S_x}$ and $\sigma_{S_z}$ are nonzero. A zero bound is a silence from the theorem, not a guarantee.

<!-- → [CHART: Bloch sphere with color map showing the Robertson bound (ℏ/2)|⟨S_y⟩| as a function of position on the sphere — blue (zero) at the north/south poles and the x-eigenstates, red (maximum = ℏ²/4) at the y-eigenstates; shows the state-dependence of the bound visually] -->

![Bloch sphere with color map showing the Robertson bound (ℏ/2)|⟨S_y⟩| as a function of position on the sphere — blue (zero) at the…](../images/03-commutators-and-uncertainty-fig-03.png)
*Figure 3.3 — Bloch sphere with color map showing the Robertson bound (ℏ/2)|⟨S_y⟩| as a function of position on the sphere — blue (zero) at the…*

---

## A Worked Calculation: Spin-½ in an $\hat{x}$ Eigenstate

Take the state $|\!\uparrow_x\rangle = (|\!\uparrow\rangle + |\!\downarrow\rangle)/\sqrt{2}$ and evaluate the Robertson bound for $\hat{S}_x$ and $\hat{S}_z$.

**The commutator.** Using $\hat{S}_i = (\hbar/2)\sigma_i$ and the Pauli algebra $[\sigma_x,\sigma_z] = -2i\sigma_y$:

$$[\hat{S}_x, \hat{S}_z] = \frac{\hbar^2}{4}[\sigma_x,\sigma_z] = \frac{\hbar^2}{4}(-2i\sigma_y) = -i\hbar\hat{S}_y.$$

So the Robertson bound is $\sigma_{S_x}\sigma_{S_z} \geq \tfrac{\hbar}{2}|\langle\hat{S}_y\rangle|$.

**Evaluate** $\langle\hat{S}_y\rangle$. In matrix form, $|\!\uparrow_x\rangle = \tfrac{1}{\sqrt{2}}\bigl(\begin{smallmatrix}1\\1\end{smallmatrix}\bigr)$:

$$\langle\hat{S}_y\rangle = \frac{\hbar}{2}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1\end{pmatrix}\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{\hbar}{4}\begin{pmatrix}1&1\end{pmatrix}\begin{pmatrix}-i\\i\end{pmatrix} = \frac{\hbar}{4}(-i+i) = 0.$$

The bound is $\tfrac{\hbar}{2}\cdot 0 = 0$. Trivially satisfied.

**Actual spreads.** $|\!\uparrow_x\rangle$ is an eigenstate of $\hat{S}_x$ with eigenvalue $+\hbar/2$, so $\sigma_{S_x} = 0$. For $\hat{S}_z$: the state is the equal superposition of $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$, so $P(S_z = +\hbar/2) = P(S_z = -\hbar/2) = 1/2$, giving $\langle\hat{S}_z\rangle = 0$ and $\sigma_{S_z} = \hbar/2$.

Product: $\sigma_{S_x}\cdot\sigma_{S_z} = 0$. Consistent with the bound $\geq 0$. $\checkmark$

**Where saturation is revealed.** Repeat for $|+y\rangle = (|\!\uparrow\rangle + i|\!\downarrow\rangle)/\sqrt{2}$, the $\hat{S}_y$ eigenstate. Now $\langle\hat{S}_y\rangle = +\hbar/2$, so the bound becomes $\sigma_{S_x}\sigma_{S_z} \geq \hbar^2/4$. In $|+y\rangle$: $\langle\hat{S}_x\rangle = \langle\hat{S}_z\rangle = 0$ and $\langle\hat{S}_{x,z}^2\rangle = \hbar^2/4$ (since $\sigma_{x,z}^2 = I$), so $\sigma_{S_x} = \sigma_{S_z} = \hbar/2$ and $\sigma_{S_x}\sigma_{S_z} = \hbar^2/4$. Bound exactly saturated.

On the Bloch sphere: the state most constrained in the $y$-direction is maximally uncertain in both $x$ and $z$, and that is precisely the state that saturates the Robertson bound for those two observables. The saturation condition — that the anticommutator term dropped in Step 4 of the proof equals zero — is satisfied exactly at the $\hat{S}_y$ eigenstates.

---

## Compatible Observables: A Quick Diagnostic

The commutator $[\hat{L}^2, \hat{L}_z]$ is worth computing explicitly, because the result underpins the entire quantum number structure of the hydrogen atom.

$$[\hat{L}^2, \hat{L}_z] = [\hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2, \hat{L}_z] = [\hat{L}_x^2, \hat{L}_z] + [\hat{L}_y^2, \hat{L}_z].$$

Using the identity $[\hat{A}^2, \hat{B}] = \hat{A}[\hat{A},\hat{B}] + [\hat{A},\hat{B}]\hat{A}$ and the angular momentum commutators $[\hat{L}_x,\hat{L}_z] = -i\hbar\hat{L}_y$ and $[\hat{L}_y,\hat{L}_z] = i\hbar\hat{L}_x$:

$$[\hat{L}_x^2, \hat{L}_z] = -i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x), \qquad [\hat{L}_y^2, \hat{L}_z] = i\hbar(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x).$$

They cancel: $[\hat{L}^2, \hat{L}_z] = 0$. The operators $\hat{L}^2$ and $\hat{L}_z$ are compatible. This algebraic fact is why $\ell$ and $m$ can simultaneously label states — why the spherical harmonics $Y_\ell^m$ are eigenfunctions of both operators at once. The quantum numbers are not a labeling choice; they are forced by commutativity.

![Two side-by-side panels: left shows two operator eigenbasis fans aligned into a single shared set (compatible); right shows two fans at different angles with a conflict marker between them (incompatible)](../images/03-commutators-and-uncertainty-fig-04.png)
*Figure 3.4 — Compatible observables share a complete simultaneous eigenbasis (left); incompatible observables have eigenbases that cannot coincide (right).*

---

## Exercises

**Warm-up**

1. *[Canonical commutation relation]* Derive $[\hat{x},\hat{p}] = i\hbar$ by applying both operators to a test function $\psi(x)$. Show every step of the product rule explicitly. (a) At which step does $i\hbar$ emerge? (b) What would the commutator be if $\hat{p}$ were defined as $\hbar\partial_x$ (no factor of $-i$), and what would be physically wrong with that definition?
*What this tests: mechanical fluency with the commutator derivation and understanding why the* $-i$ *is required.*

2. *[Matrix commutator for Pauli matrices]* Verify by direct matrix multiplication that $[\sigma_x,\sigma_z] = -2i\sigma_y$. Before computing, verify that your $\sigma_y$ is Hermitian ($\sigma_y^\dagger = \sigma_y$). A wrong sign in $\sigma_y$ is the most common error in this calculation.
*What this tests: executing a matrix commutator and catching the canonical sign trap.*

3. *[Commutator of a composite operator]* The harmonic oscillator Hamiltonian is $\hat{H} = \hat{p}^2/2m + m\omega^2\hat{x}^2/2$. Compute $[\hat{H}, \hat{x}]$ using $[\hat{p}^2, \hat{x}] = \hat{p}[\hat{p},\hat{x}] + [\hat{p},\hat{x}]\hat{p}$ and $[\hat{p},\hat{x}] = -i\hbar$. State what the result implies about whether $\hat{x}$ is a constant of motion.
*What this tests: computing commutators of composite operators and connecting the result to dynamics.*

**Application**

4. *[Compatibility diagnostic for three pairs]* For each pair, state compatible or incompatible and justify with the commutator: (a) $\hat{L}^2$ and $\hat{L}_z$; (b) $\hat{L}_x$ and $\hat{L}_y$; (c) $\hat{H}$ and $\hat{L}^2$ for the hydrogen atom. For each incompatible pair, write the Robertson bound and identify which quantity on the right-hand side determines whether the bound is binding for a particular state.
*What this tests: identifying compatible vs. incompatible pairs and applying Robertson without rerunning the full proof.*

5. *[Robertson bound for spin on the Bloch sphere]* Apply Robertson to $\hat{S}_x$ and $\hat{S}_y$ for a general qubit state with Bloch vector $(\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$. (a) Compute $[\hat{S}_x,\hat{S}_y]$. (b) Evaluate the Robertson bound $\tfrac{\hbar}{2}|\langle\hat{S}_z\rangle| = \tfrac{\hbar^2}{4}|\cos\theta|$. (c) Find the Bloch-sphere locus where the bound is maximized. (d) Find the locus where the bound is zero.
*What this tests: applying Robertson to spin and understanding the bound's geometric dependence on the state.*

6. *[Cauchy-Schwarz from first principles]* Verify the Cauchy-Schwarz inequality $\|u\|^2\|v\|^2 \geq |\langle u|v\rangle|^2$ by expanding $\|\hat{A}'|\psi\rangle - \lambda\hat{B}'|\psi\rangle\|^2 \geq 0$ for all complex $\lambda$, then choosing $\lambda = \langle v|u\rangle/\|v\|^2$ optimally. This is the only assumption the Robertson proof makes.
*What this tests: deriving Cauchy-Schwarz from the positivity of norms and seeing that it is the single load-bearing step in the Robertson proof.*

**Synthesis**

7. *[Robertson for angular momentum]* The orbital angular momentum commutators include $[\hat{L}_x,\hat{L}_y] = i\hbar\hat{L}_z$. (a) Write the Robertson bound for $\hat{L}_x$ and $\hat{L}_y$ in terms of $\langle\hat{L}_z\rangle$. (b) For the state $|\ell=1, m=1\rangle$: compute $\langle\hat{L}_z\rangle = \hbar$ and evaluate the bound $\sigma_{L_x}\sigma_{L_y} \geq \hbar^2/2$. Verify this is consistent with $\sigma_{L_x}^2 = \sigma_{L_y}^2 = \hbar^2/2$ (using $\langle\hat{L}_x\rangle = \langle\hat{L}_y\rangle = 0$ in this state). (c) Is the bound saturated?
*What this tests: applying Robertson to orbital angular momentum and connecting to the eigenvalue structure.*

8. *[The CSCO and quantum number labeling]* The CSCO for the hydrogen atom without spin is $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$. (a) Sketch the argument that $[\hat{L}^2,\hat{L}_z] = 0$ using the angular momentum commutation relations. (b) Explain in words why the CSCO concept is the reason three quantum numbers $(n,\ell,m)$ simultaneously label each eigenstate. (c) Is $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$ still a CSCO? Justify.
*What this tests: connecting commutativity to the existence of simultaneous quantum numbers — synthesis, not just calculation.*

**Challenge**

9. *[The Schrödinger uncertainty relation]* (a) Show explicitly that the anticommutator term $\tfrac{1}{4}\langle\{\hat{A}',\hat{B}'\}\rangle^2$ dropped in Step 4 is non-negative. (b) Retain it to derive the Schrödinger bound: $\sigma_A^2\sigma_B^2 \geq \tfrac{1}{4}|\langle\{\hat{A}',\hat{B}'\}\rangle|^2 + \hbar^2/4$. (c) For the Gaussian wave packet, compute $\langle\{\hat{x}',\hat{p}'\}\rangle$ directly and show it vanishes — confirming that Robertson and Schrödinger agree for the Gaussian. (d) Argue (without full computation) that for the infinite-square-well ground state, the anticommutator term is nonzero, making the Schrödinger bound strictly tighter.
*What this tests: understanding the hierarchy of uncertainty bounds and seeing where Robertson is loose.*

---

## References

Robertson, H. P. (1929). The uncertainty principle. *Physical Review*, 34, 163. The original one-page proof, readable by an undergraduate with one hour of effort.

Kennard, E. H. (1927). Zur Quantenmechanik einfacher Bewegungstypen. *Zeitschrift für Physik*, 44, 326. First proof of $\sigma_x\sigma_p \geq \hbar/2$, two years before Robertson's general theorem.

Schrödinger, E. (1930). Zum Heisenbergschen Unschärfeprinzip. *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, Physikalisch-mathematische Klasse, 296–303.

Ozawa, M. (2003). Universally valid reformulation of the Heisenberg uncertainty principle on noise and disturbance in measurement. *Physical Review A*, 67, 042105.

Busch, P., Lahti, P., & Werner, R. F. (2013). Proof of Heisenberg's error-disturbance relation. *Physical Review Letters*, 111, 160405.

Maassen, H., & Uffink, J. B. M. (1988). Generalized entropic uncertainty relations. *Physical Review Letters*, 60, 1103.

Coles, P. J., Berta, M., Tomamichel, M., & Wehner, S. (2017). Entropic uncertainty relations and their applications. *Reviews of Modern Physics*, 89, 015002.

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §3.5.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.4.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §3.5.

