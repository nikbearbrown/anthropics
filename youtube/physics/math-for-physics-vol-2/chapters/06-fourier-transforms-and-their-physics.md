# Fourier Transforms and Their Physics

*From the Fourier series of Volume 1 to the continuous transform — the transform pair, convolution, the bandwidth relation, and the Dirac delta — the analysis that connects position to momentum in quantum mechanics and an aperture to its diffraction pattern in optics.*

---

## 1. Cold open: a single slit, and a particle's momentum

Shine a laser through a narrow slit and look at the wall behind it. You do not see a bright line the shape of the slit. You see a broad central band flanked by fainter fringes — and, counterintuitively, the *narrower* you make the slit, the *wider* the pattern spreads. Squeeze the slit and the light fans out more.

Now a different experiment in a different subject. A quantum particle has a wavefunction $\psi(x)$ that says where it is likely to be found. The same particle also has a momentum, and there is a second wavefunction $\tilde\psi(p)$ that says what momentum it is likely to have. Localize the particle tightly in space — make $\psi(x)$ a narrow spike — and its momentum becomes wildly uncertain; $\tilde\psi(p)$ spreads out. Squeeze the position and the momentum fans out.

These are the same fact. The diffraction pattern is the Fourier transform of the slit; the momentum wavefunction is the Fourier transform of the position wavefunction; and "narrow here forces wide there" is a theorem about Fourier transform pairs, true of any conjugate pair whatever. Volume 1 taught you to expand a *periodic* function in a Fourier series. This chapter takes the period to infinity, watches the discrete spectrum melt into a continuum, and arrives at the single operation behind both experiments.

---

## 2. The tool, named

In Volume 1 a function $f(x)$ of period $L$ was written as a sum over discrete harmonics $e^{i k_n x}$ with $k_n = 2\pi n / L$:

$$
f(x) = \sum_{n=-\infty}^{\infty} c_n\, e^{i k_n x}, \qquad
c_n = \frac{1}{L}\int_{-L/2}^{L/2} f(x)\, e^{-i k_n x}\, dx.
$$

The spectrum is a comb of allowed wavenumbers spaced $\Delta k = 2\pi/L$ apart. The **Fourier transform** is what this becomes when the period grows without bound. As $L \to \infty$ the spacing $\Delta k \to 0$, the comb fills in, and the sum over $n$ becomes an integral over a continuous wavenumber $k$. A function need no longer be periodic; *any* well-behaved function on the whole line decomposes into a continuum of pure waves. The chapter's objects are the **transform pair** (forward and inverse), the **convolution theorem** (multiplication in one space is convolution in the other), the **bandwidth relation** (a function and its transform cannot both be narrow), and the **Dirac delta** (the limiting "spike" that makes continuous bases work).

---

## 3. Development & derivation

### The transform as the continuous limit of the series

Substitute the coefficient formula into the series and watch the limit. Write $c_n = \frac{1}{L}\int_{-L/2}^{L/2} f(x') e^{-ik_n x'}dx'$ and insert:

$$
f(x) = \sum_{n=-\infty}^{\infty} \left[\frac{1}{L}\int_{-L/2}^{L/2} f(x')\,e^{-ik_n x'}\,dx'\right] e^{i k_n x}.
$$

Because consecutive wavenumbers differ by $\Delta k = 2\pi/L$, we have $1/L = \Delta k/2\pi$. Factor it in:

$$
f(x) = \frac{1}{2\pi}\sum_{n} \Delta k \left[\int_{-L/2}^{L/2} f(x')\,e^{-ik_n x'}\,dx'\right] e^{ik_n x}.
$$

Now let $L \to \infty$. The spacing $\Delta k \to 0$, so the sum $\sum_n \Delta k\,(\cdots)$ becomes the integral $\int dk\,(\cdots)$ over the continuous variable $k$, and the inner integral runs over all of $\mathbb{R}$. Defining the **Fourier transform** as the inner integral,

$$
\boxed{\;\tilde f(k) = \int_{-\infty}^{\infty} f(x)\, e^{-ikx}\,dx,\;}
$$

the outer expression is the **inverse transform**:

$$
\boxed{\;f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \tilde f(k)\, e^{ikx}\,dk.\;}
$$

This is a derivation, not an assertion: the transform *is* the $L\to\infty$ limit of the Fourier series you already know. The continuous spectrum $\tilde f(k)$ replaces the discrete coefficients $c_n$, telling you how much of each wave $e^{ikx}$ the function contains.

**A word on conventions, because they cause real confusion.** The factor of $2\pi$ can sit on the inverse (as above), or split symmetrically as $1/\sqrt{2\pi}$ on each, or vanish if you use ordinary frequency $\nu$ with $e^{-2\pi i\nu x}$. The sign of the exponent can also flip. *No convention is more correct; they must merely be used consistently.* In quantum mechanics one uses the symmetric $1/\sqrt{2\pi\hbar}$ split with wavenumber rescaled to momentum, $p = \hbar k$. We will state the convention every time it matters.

### Plancherel: the transform conserves total weight

The transform preserves the $L^2$ norm. **Plancherel's theorem** (1910) states $\int|f(x)|^2 dx = \frac{1}{2\pi}\int|\tilde f(k)|^2 dk$ (with the asymmetric convention above). Physically, the total probability carried by a wavefunction is the same whether you compute it in position or momentum space — a normalized $\psi(x)$ stays normalized as $\tilde\psi(p)$. The transform is, up to the constant, a unitary change of basis. This is the analysis-level version of the resolution of the identity from Chapter 5.

### The convolution theorem

The **convolution** of two functions is the smeared overlap

$$
(f * g)(x) = \int_{-\infty}^{\infty} f(x')\,g(x - x')\,dx'.
$$

It is how a system's response blurs an input: a true spectrum convolved with an instrument's line shape, a sharp object convolved with a lens's point-spread. The **convolution theorem** says this messy operation becomes simple multiplication in Fourier space. Transform $f * g$:

$$
\widetilde{f*g}(k) = \int dx\, e^{-ikx}\int dx'\, f(x')\,g(x-x').
$$

Swap the order of integration and substitute $u = x - x'$ (so $x = x' + u$, $dx = du$):

$$
= \int dx'\, f(x')\int du\, e^{-ik(x'+u)} g(u)
= \left[\int dx'\, f(x')\,e^{-ikx'}\right]\left[\int du\, g(u)\,e^{-iku}\right] = \tilde f(k)\,\tilde g(k).
$$

So

$$
\boxed{\;\widetilde{f * g} = \tilde f \cdot \tilde g.\;}
$$

Convolution in real space is multiplication in Fourier space, and (by symmetry) multiplication in real space is convolution in Fourier space. This one line explains the double slit: two slits are a single slit *convolved* with two delta functions, so the diffraction amplitude is the single-slit transform *times* the transform of the two deltas — a sinc envelope multiplied by an interference cosine.

![A sharp two-line signal convolved with a bump-shaped instrument response gives a smoothed, blurred output. A banner notes that in Fourier space this messy real-space operation becomes the simple pointwise product of the two transforms.](images/06-fourier-transforms-and-their-physics-fig-03.png)
*Figure 6.3 — Convolution smears a signal with a response; by the convolution theorem it becomes multiplication, $\widetilde{f*g}=\tilde f\cdot\tilde g$, in Fourier space — and dividing back deconvolves.*

### The bandwidth relation

A function and its transform cannot both be arbitrarily narrow. Make this precise with widths. Define the spatial width $\Delta x$ as the root-mean-square spread of $|f|^2$ about its mean, and $\Delta k$ likewise for $|\tilde f|^2$. Then for any function,

$$
\boxed{\;\Delta x\,\Delta k \geq \tfrac12.\;}
$$

This is a pure theorem about Fourier pairs — sometimes called the Gabor limit — and it has nothing to do with quantum measurement per se. It is most transparent through scaling: if $f(x) \to f(ax)$ compresses the function by a factor $a$, its transform stretches by the same factor, $\tilde f(k) \to \frac{1}{a}\tilde f(k/a)$, so the product of widths is scale-invariant. Squeeze in $x$, spread in $k$ — exactly the slit and the wave packet.

> **Keep two relations distinct.** The bandwidth relation $\Delta x\,\Delta k \geq \frac12$ is a fact about *any* Fourier pair. The Robertson uncertainty principle $\sigma_A\sigma_B \geq \frac12|\langle[\hat A,\hat B]\rangle|$ (Chapter 5) is a fact about *operators and commutators* in an inner-product space. They are routinely conflated, but they are not the same statement. The quantum $\sigma_x\sigma_p \geq \hbar/2$ happens to follow from *either*: from Robertson via $[\hat x,\hat p]=i\hbar$, or from the bandwidth relation via the de Broglie rescaling $p = \hbar k$ (which turns $\Delta x\,\Delta k\geq\frac12$ into $\Delta x\,\Delta p \geq \hbar/2$). The energy–time relation $\Delta E\,\Delta t \sim \hbar$ is purely the bandwidth relation — time is not an operator in standard quantum mechanics, so Robertson does not apply to it. Distinguishing these prevents a stubborn category error.

### The Gaussian: its own transform, and the minimum

The Gaussian $f(x) = e^{-x^2/2a^2}$ transforms to another Gaussian, $\tilde f(k) \propto e^{-a^2 k^2/2}$ (completing the square in the exponent). It is the *unique* shape that saturates the bandwidth bound, $\Delta x\,\Delta k = \frac12$, which is why the Gaussian wave packet is the most classical-looking quantum state and the minimum-uncertainty state. Narrowing it in $x$ (small $a$) widens it in $k$ in exact proportion — the bandwidth relation made visible in a single family.

![Two Fourier transform pairs of Gaussians. In the top row a wide pulse in position transforms to a narrow spectrum; in the bottom row a narrow pulse transforms to a wide spectrum. The product of the widths is fixed, so squeezing in x spreads out in k.](images/06-fourier-transforms-and-their-physics-fig-01.png)
*Figure 6.1 — The bandwidth tradeoff: a function and its transform cannot both be narrow. The Gaussian saturates $\Delta x\,\Delta k = \tfrac12$; squeeze in $x$ and the spectrum spreads in $k$.*

### The Dirac delta

To handle continuous bases we need an object that picks out a single point. The **Dirac delta** $\delta(x)$ is defined entirely by its action under an integral:

$$
\int_{-\infty}^{\infty} \delta(x - x_0)\, f(x)\,dx = f(x_0).
$$

It is *not* an ordinary function — it is not a "very tall spike," and using it outside an integral leads to nonsense. (Rigorously it is a distribution, in the sense of Schwartz's *Théorie des distributions*, 1950–51; we use it operationally and flag the backstop.) The delta is the Fourier transform of a constant. From the inversion formula applied to $f$ and back:

$$
f(x) = \frac{1}{2\pi}\int dk\, e^{ikx}\int dx'\, f(x')\,e^{-ikx'}
= \int dx'\, f(x')\left[\frac{1}{2\pi}\int dk\, e^{ik(x-x')}\right],
$$

and comparing with the defining property identifies the bracket:

$$
\boxed{\;\delta(x - x') = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ik(x - x')}\,dk.\;}
$$

This is the continuous analogue of the Kronecker delta from orthonormal bases. It is what makes the continuous resolution of the identity $\int|x\rangle\langle x|\,dx = \hat I$ of Chapter 5 work, with $\langle x|x'\rangle = \delta(x-x')$.

---

## 4. Worked examples

### Example 1 — The top hat and the sinc

A single slit of width $a$ has aperture function $f(x) = 1$ for $|x| < a/2$ and $0$ otherwise (a top hat). Its transform:

$$
\tilde f(k) = \int_{-a/2}^{a/2} e^{-ikx}\,dx
= \frac{e^{-ika/2} - e^{ika/2}}{-ik}
= \frac{2\sin(ka/2)}{k}
= a\,\frac{\sin(ka/2)}{ka/2} = a\,\operatorname{sinc}\!\left(\frac{ka}{2}\right).
$$

The diffraction *intensity* is $|\tilde f(k)|^2 \propto \operatorname{sinc}^2(ka/2)$ — the familiar single-slit pattern with a broad central peak and decaying side lobes. Read off the cold open's paradox directly: the first zero sits at $ka/2 = \pi$, i.e. $k = 2\pi/a$, so the central peak's width in $k$ scales as $1/a$. Halve the slit width $a$ and the pattern doubles in width. Narrow slit, wide pattern — the bandwidth relation in one line.

![A top-hat aperture of width a on the left transforms to a sinc function on the right whose first zeros sit at k equals plus and minus two pi over a. The central peak's width scales as one over a, so a narrower slit gives a wider diffraction pattern.](images/06-fourier-transforms-and-their-physics-fig-02.png)
*Figure 6.2 — A slit (top hat of width $a$) transforms to $a\,\mathrm{sinc}(ka/2)$; the first zero at $k=2\pi/a$ makes the central peak width $\propto 1/a$ — the single-slit paradox.*

### Example 2 — The double slit by convolution

Two slits of width $a$ separated by distance $d$ are a single slit *convolved* with two deltas at $\pm d/2$: $g(x) = f(x) * [\delta(x - d/2) + \delta(x + d/2)]$. By the convolution theorem the transform is the *product*:

$$
\tilde g(k) = \tilde f(k)\cdot\big(e^{-ikd/2} + e^{ikd/2}\big) = a\,\operatorname{sinc}\!\left(\frac{ka}{2}\right)\cdot 2\cos\!\left(\frac{kd}{2}\right).
$$

The intensity $|\tilde g|^2 \propto \operatorname{sinc}^2(ka/2)\,\cos^2(kd/2)$ is the single-slit envelope modulating fast interference fringes — exactly the textbook two-slit pattern. The fringe spacing ($\propto 1/d$) comes from the slit separation; the envelope ($\propto 1/a$) from the slit width. Two physical scales, two reciprocal scales in the pattern, cleanly separated by convolution.

### Example 3 — Position to momentum: a Gaussian wave packet

Take a normalized Gaussian position wavefunction $\psi(x) = (\pi a^2)^{-1/4} e^{-x^2/2a^2}$. The momentum wavefunction is the transform (quantum convention $p=\hbar k$, symmetric factor):

$$
\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{\infty} \psi(x)\,e^{-ipx/\hbar}\,dx
\;\propto\; \exp\!\left(-\frac{a^2 p^2}{2\hbar^2}\right),
$$

another Gaussian, by completing the square. The position width is $\Delta x = a/\sqrt2$ and the momentum width is $\Delta p = \hbar/(a\sqrt2)$, so

$$
\Delta x\,\Delta p = \frac{a}{\sqrt 2}\cdot\frac{\hbar}{a\sqrt2} = \frac{\hbar}{2}.
$$

The Gaussian saturates the bound. Localize the particle (small $a$): $\Delta x$ shrinks, $\Delta p$ grows in exact reciprocal proportion. The same state, viewed in two bases, with widths forced apart by the transform.

---

## 5. Return to the cold open

Both opening experiments are now one calculation. The single slit: its diffraction amplitude in the far field is the Fourier transform of its aperture function (Fraunhofer diffraction — the far-field amplitude is literally $\tilde f(k)$ with $k$ proportional to the diffraction angle). By Example 1 a top-hat slit of width $a$ transforms to a sinc whose central peak has width $\propto 1/a$. A narrow slit *must* produce a wide pattern, because narrowing $f$ widens $\tilde f$ — the bandwidth relation, not an accident of geometry.

The particle: its momentum wavefunction is the Fourier transform of its position wavefunction, $\tilde\psi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int \psi(x)e^{-ipx/\hbar}dx$. By Example 3, localizing $\psi(x)$ widens $\tilde\psi(p)$ — same theorem. And here is the synthesis promised by Chapter 5: this transform *is* the change of basis between position and momentum eigenstates, with the kernel $\langle x | p\rangle = e^{ipx/\hbar}/\sqrt{2\pi\hbar}$. Inserting the continuous resolution of the identity $\int |x\rangle\langle x|\,dx = \hat I$ into $\langle p|\psi\rangle$ gives exactly the Fourier integral:

$$
\tilde\psi(p) = \langle p|\psi\rangle = \int \langle p|x\rangle\langle x|\psi\rangle\,dx = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\,\psi(x)\,dx.
$$

The diffraction pattern and the momentum wavefunction are the same operation because both are "express this thing in the basis of pure waves." The slit and the particle were never different problems.

---

## 6. Where it generalizes

- **Spectroscopy and deconvolution.** A measured spectrum is the true spectrum convolved with the instrument's line shape; by the convolution theorem, dividing in Fourier space deconvolves it. The natural-linewidth/lifetime relation $\Delta E\,\Delta t \sim \hbar$ is a time–frequency bandwidth statement, *not* a Robertson commutator.
- **Crystallography.** A crystal's diffraction pattern is the Fourier transform of its electron density; X-ray crystallography inverts the transform (up to the notorious phase problem). Bragg's law is the condition for the lattice's Fourier comb to constructively interfere.
- **Free-particle dynamics.** In momentum space the free Schrödinger equation is diagonal — each component $\tilde\psi(p)$ merely acquires a time-dependent phase $e^{-ip^2 t/2m\hbar}$ — so evolving a wave packet is trivial in $p$-space and the Fourier transform carries the answer back to $x$-space.
- **The Bessel hand-off.** A *circular* aperture transforms not to a sinc but to an Airy pattern built from a Bessel function $J_1$; the first zero of $J_1$ gives the $1.22$ in the Rayleigh resolution criterion $1.22\lambda/D$. The Fourier transform in cylindrical symmetry produces Bessel functions — which Chapter 7 derives as separated solutions.
- **The discrete return.** Sample a signal and the continuous transform becomes the discrete Fourier transform, computed by the FFT — the algorithm inside every spectrum analyzer, MRI reconstruction, and radio-astronomy correlator.

A solver computes transforms and FFTs instantly. It does not know that a narrow slit *must* give a broad pattern, that a double slit is one slit times an interference comb, that the Gaussian is special because it is its own transform, or that "position and momentum are conjugate" is the same sentence as "time and frequency are conjugate." The chapter builds the intuition to predict the qualitative answer before computing it.

---

## Exercises

1. **(Transform pair.)** Compute the Fourier transform of the two-sided exponential $f(x) = e^{-|x|/\tau}$. Sketch $f$ and $\tilde f$, and verify that narrowing $f$ (smaller $\tau$) widens $\tilde f$.

2. **(Derivation — required.)** Derive the convolution theorem $\widetilde{f*g} = \tilde f\,\tilde g$ from the definitions, justifying the change of integration variable and the interchange of integrals. Then use it to obtain the double-slit intensity from the single-slit result.

3. **(Bandwidth.)** Using the scaling property $f(x)\mapsto f(ax) \Rightarrow \tilde f(k) \mapsto \frac{1}{a}\tilde f(k/a)$, argue that the product $\Delta x\,\Delta k$ is independent of the scale $a$. Verify the Gaussian saturates the bound $\Delta x\,\Delta k = \frac12$.

4. **(Delta function.)** Starting from $\delta(x-x') = \frac{1}{2\pi}\int e^{ik(x-x')}dk$, show that $\int \delta(x-x_0)f(x)\,dx = f(x_0)$. Then show $\delta(ax) = \frac{1}{|a|}\delta(x)$ by changing variables under a test integral.

5. **(Conceptual — keep them distinct.)** In one short paragraph, explain why the Fourier bandwidth relation $\Delta x\,\Delta k\geq\frac12$ and the Robertson uncertainty principle $\sigma_A\sigma_B \geq \frac12|\langle[\hat A,\hat B]\rangle|$ are *different* statements, and why both nonetheless reproduce $\sigma_x\sigma_p \geq \hbar/2$. What does this say about the energy–time relation, where time is not an operator?

---

## Sources

- Fourier, J. *Théorie analytique de la chaleur* (Paris, 1822), building on the 1807 memoir to the Académie des Sciences. [The founding work: heat-equation solutions as trigonometric series and, on the infinite domain, the integral transform. The transform was born from a physics PDE. Available via Gallica, BnF.]
- Cauchy, A.-L. Integral (inversion) form of the Fourier theorem (1827). [The step from Fourier's physical argument toward analysis. *verify exact venue.*] <!-- FACT-CHECK FLAG: UNVERIFIED — Cauchy's 1820s contribution to the Fourier integral theorem is genuine, but the exact 1827 venue was not pinned to an authoritative source. See factchecks/06-fourier-transforms-and-their-physics-assertions.md -->
- Plancherel, M. "Contribution à l'étude de la représentation d'une fonction arbitraire par des intégrales définies." *Rendiconti del Circolo Matematico di Palermo* **30**, 289–335 (1910). [The Fourier transform is unitary on $L^2$: $\int|f|^2 = \int|\tilde f|^2$ — why a normalized wavefunction stays normalized. Pagination confirmed: vol. 30, pp. 289–335.]
- Dirac, P. A. M. *The Principles of Quantum Mechanics* (Oxford, 1930). [Introduced the delta function as the continuum analogue of the Kronecker delta.]
- Schwartz, L. *Théorie des distributions* (Hermann, 1950–51). [Made the Dirac delta a rigorous distribution — the backstop for the chapter's operational use.]
- Abbe, E. "Beiträge zur Theorie des Mikroskops und der mikroskopischen Wahrnehmung." *Archiv für mikroskopische Anatomie* **9**, 413–468 (1873). [Microscope image formation as a double Fourier transform; resolution as a spatial-bandwidth limit. The explicit diffraction-integral / Fourier formulation was supplied by M. Wolfke (1909), after Abbe died before publishing his promised mathematical paper. Wolfke 1909 attribution confirmed.]
- Gabor, D. "Theory of communication." *Journal of the IEE* **93**, 429–457 (1946). [The time–frequency bandwidth (Gabor) limit and the minimum-uncertainty Gaussian. *verify pagination.*] <!-- FACT-CHECK FLAG: UNVERIFIED — primary article is J. Inst. Electr. Eng. Part III, vol. 93, no. 26 (1946), pp. 429–441; the 429–457 range may overstate it. Substance confirmed. See factchecks/06-fourier-transforms-and-their-physics-assertions.md -->
- Singh, C., and E. Marshman. PER on the quantum state-space → position/momentum representation transition (arXiv:1509.04084, 2015); see also ERIC EJ1300062. [Documents the change-of-basis difficulty this chapter is built to address.]
