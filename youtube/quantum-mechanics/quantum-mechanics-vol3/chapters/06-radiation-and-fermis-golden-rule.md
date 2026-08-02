# Chapter 6 — Radiation and Fermi's Golden Rule

On October 4, 1947, Lamb and Retherford published their result in *Physical Review*: the $2s_{1/2}$ and $2p_{1/2}$ levels of hydrogen, predicted by Dirac's equation to be degenerate, are separated by about 1,060 MHz. The shift is small — four parts in $10^7$ of the $n=2$ binding energy — but clean, sharp, and reproducible. It showed that Dirac's equation alone was not sufficient. Something was missing.

What was missing was the quantized electromagnetic field. The vacuum is not empty; it fluctuates. Those fluctuations shift the $2s$ level relative to $2p$ because the $2s$ electron, with its nonzero probability density at the nucleus, samples the vacuum field differently from the $2p$ electron. The Lamb shift is a QED effect, and computing it correctly requires renormalization — machinery that would not be complete for another two years.

This chapter develops the tools just below that boundary. We derive Fermi's golden rule. We compute the density of states needed to use it. We derive the electric-dipole selection rules that govern which hydrogen transitions are fast and which are slow. We compute the rate and lifetime for the $2p \to 1s$ transition, obtaining 1.6 ns in agreement with experiment.

At each stage we identify where the semiclassical framework ends and points toward QED. That boundary is not a failure of the semiclassical approach; the formula works. The mechanism behind it requires a separate framework.

---

## From Sinc-Squared to Fermi's Golden Rule

Chapter 5 gave the first-order transition probability for a sinusoidal perturbation near resonance:

$$P_{i\to f}(t) = \frac{|V_{fi}|^2}{\hbar^2}\cdot\frac{\sin^2\!\left[\frac{(\omega_{fi}-\omega)\,t}{2}\right]}{\left(\frac{\omega_{fi}-\omega}{2}\right)^2}.$$

This is for a single discrete final state $|f\rangle$. The population bounces coherently between $|i\rangle$ and $|f\rangle$ — Rabi oscillations. We now consider the opposite extreme: the final state is not a single level but a continuum, a dense spectrum of states near $E_f = E_i + \hbar\omega$.

An electron ionizing from a hydrogen atom, a photon emitted into the many electromagnetic modes of the vacuum, a nucleus decaying into a continuum of recoil states — all of these are transitions to a continuum. There is no single $|f\rangle$ to bounce back from. The population leaks out irreversibly.

**Step 1: Sum over final states.** Let $\rho(E_f)$ be the density of final states — the number of states per unit energy near $E_f$. We sum the transition probability:

$$P_{\mathrm{total}}(t) = \int P_{i\to f}(t)\,\rho(E_f)\,dE_f = \frac{|V_{fi}|^2}{\hbar^2}\int_{-\infty}^{+\infty}\frac{\sin^2(\alpha t/2)}{\alpha^2}\,\rho(E_f)\,dE_f,$$

where $\alpha = (E_f - E_i)/\hbar - \omega$, and we assumed $|V_{fi}|^2$ and $\rho(E_f)$ vary slowly compared to the sinc-squared peak.

**Step 2: Sharpen the sinc-squared.** At large $t$, the function $\sin^2(\alpha t/2)/\alpha^2$ is a narrow spike of width $\sim 2\pi/t$ centered at $\alpha = 0$. Its total area:

$$\int_{-\infty}^{+\infty}\frac{\sin^2(\alpha t/2)}{\alpha^2}\,d\alpha = \frac{\pi t}{2}.$$

As $t \to \infty$, this becomes $(\pi t/2)\,\delta(\alpha)$. Converting to energy variables and using $d\alpha = dE_f/\hbar$:

$$\frac{\sin^2(\alpha t/2)}{\alpha^2} \;\to\; \frac{\pi t\hbar}{2}\,\delta(E_f - E_i - \hbar\omega).$$

**Step 3: Pull out the rate.** Substituting into the sum and using the delta function to evaluate the integral:

$$P_{\mathrm{total}}(t) = \frac{\pi |V_{fi}|^2}{\hbar}\,\rho(E_f)\,t.$$

Since $P_{\mathrm{total}} \propto t$, the transition rate — probability per unit time — is constant:

$$\boxed{W_{i\to f} = \frac{2\pi}{\hbar}\,|\langle f|\hat{H}'|i\rangle|^2\,\rho(E_f).}$$

This is **Fermi's golden rule**.

<!-- → [DIAGRAM: two-panel illustration — left: discrete two-level Rabi oscillation P(t) bouncing between 0 and 1; right: continuum case P_total(t) growing linearly with golden-rule slope W, sinc-squared sharpening into a delta function shown as an inset] -->

![two-panel illustration — left: discrete two-level Rabi oscillation P(t) bouncing between 0 and 1](../images/06-radiation-and-fermis-golden-rule-fig-01.png)
*Figure 6.1 — two-panel illustration — left: discrete two-level Rabi oscillation P(t) bouncing between 0 and 1*

**Historical attribution.** P.A.M. Dirac derived this formula in 1927 in "The Quantum Theory of the Emission and Absorption of Radiation." This paper is the foundational document of quantum electrodynamics. Enrico Fermi called it "Golden Rule No. 2" in his 1950 Chicago lecture notes on nuclear physics because it was useful — not because he derived it. The name stuck. Dirac got there first, by twenty-three years.

**Validity window.** The golden rule requires $t$ large enough that the sinc-squared has sharpened into a delta function ($t \gg 2\pi/\Delta\omega$, where $\Delta\omega$ is the continuum bandwidth), but small enough that first-order perturbation theory still holds ($W \cdot t \ll 1$). For an atom emitting into the electromagnetic vacuum, this window spans many orders of magnitude: Bohr oscillation periods are femtoseconds, spontaneous emission lifetimes are nanoseconds, and the golden rule governs the entire middle range.

---

## The Density of States

The density of states $\rho(E)$ — the number of quantum states per unit energy — follows from a counting argument.

**Setup.** A free particle in a cubic box of side $L$, volume $V = L^3$, with periodic boundary conditions. Allowed wavevectors: $\vec{k} = (2\pi/L)(n_x, n_y, n_z)$ for integers $(n_x, n_y, n_z)$. Each such $\vec{k}$ is one state per spin.

**Count states in a shell.** States in the range $[k, k+dk]$ occupy a spherical shell in $k$-space of volume $4\pi k^2\,dk$. The volume per state is $(2\pi/L)^3 = (2\pi)^3/V$. So:

$$dn = \frac{4\pi k^2\,dk}{(2\pi)^3/V} = \frac{V\,k^2\,dk}{2\pi^2}.$$

**Convert to energy.** For a non-relativistic particle, $E = \hbar^2 k^2/(2m)$, so $dk/dE = m/(\hbar^2 k)$:

$$\boxed{\rho(E) = \frac{Vmk}{2\pi^2\hbar^2}, \qquad k = \frac{\sqrt{2mE}}{\hbar}.}$$

For **photons** (two polarization states, $E = \hbar\omega$, $k = \omega/c$):

$$\rho(\omega) = \frac{V\omega^2}{\pi^2 c^3} \quad\text{(per unit angular frequency, summed over polarizations).}$$

This is the quantity that enters the spontaneous emission rate and that Planck needed in 1900 to obtain the correct blackbody spectrum. More available final states per unit energy means a faster rate — the system decays faster because there are more places to go. The density of states is not supplementary information; it is what converts a Rabi oscillation into an irreversible exponential decay.

<!-- → [CHART: ρ(E) ∝ √E for a 3D free particle, shown as a smooth curve with the k-space spherical shell shown as an inset; annotation showing the 3D result vs. the constant 2D result for comparison] -->

![ρ(E) ∝ √E for a 3D free particle, shown as a smooth curve with the k-space spherical shell shown as an inset](../images/06-radiation-and-fermis-golden-rule-fig-02.png)
*Figure 6.2 — ρ(E) ∝ √E for a 3D free particle, shown as a smooth curve with the k-space spherical shell shown as an inset*

---

## The Electric-Dipole Approximation

The coupling between an atom and an electromagnetic field involves the vector potential evaluated at the electron position:

$$\hat{H}' = -\frac{e}{mc}\hat{\vec{A}}(\vec{r},t)\cdot\hat{\vec{p}}.$$

For optical and UV transitions in hydrogen, the photon wavelength $\lambda \sim 100$–$500$ nm greatly exceeds the atomic size $a_0 \approx 0.053$ nm. The dimensionless product $ka_0 \approx 2\pi a_0/\lambda \sim 0.001$. The vector potential barely varies over the extent of the atom, so:

$$\hat{\vec{A}}(\vec{r},t) \approx \hat{\vec{A}}(\vec{0},t).$$

This is the **electric-dipole approximation**. Using $\hat{\vec{E}} = -(1/c)\partial_t\hat{\vec{A}}$ and the commutator identity that connects $\hat{\vec{A}}\cdot\hat{\vec{p}}$ to $e\hat{\vec{r}}\cdot\hat{\vec{E}}$, the coupling reduces to:

$$\hat{H}'_{\mathrm{dip}} = e\hat{\vec{r}}\cdot\hat{\vec{\mathcal{E}}}(t).$$

The transition matrix element is now $\langle f|e\hat{\vec{r}}|i\rangle$ — the dipole matrix element.

The approximation fails when $ka_0 \sim 1$, i.e., $E_{\mathrm{photon}} \sim \hbar c/a_0 \approx 3.7$ keV — hard X-rays and above. For X-ray transitions, magnetic-dipole (M1) and electric-quadrupole (E2) corrections become important, suppressed relative to E1 by additional powers of $ka_0$.

![Electric-dipole approximation validity: two panels — left shows a small atom sitting inside a long-wavelength EM wave (λ≫a₀, nearly flat over the atom), right shows the same atom with a short-wavelength hard X-ray photon (λ≈a₀, completing a full oscillation across the atom)](../images/06-radiation-and-fermis-golden-rule-fig-06.png)
*Figure 6.6 — Long-wavelength limit and its breakdown: the dipole approximation A(r,t)≈A(0,t) holds when the photon wavelength greatly exceeds the atomic size; it fails for hard X-rays above ~3.7 keV where ka₀≈1.*

---

## Selection Rules Are Calculations

The electric-dipole matrix element for hydrogen is:

$$\langle n'\ell'm'|e\hat{\vec{r}}|n\ell m\rangle = e\int\psi^*_{n'\ell'm'}\,\vec{r}\,\psi_{n\ell m}\,d^3r.$$

The wave functions $\psi_{n\ell m} = R_{n\ell}(r)Y_\ell^m(\theta,\phi)$ separate. The operator $\vec{r}$ in spherical coordinates has components proportional to $r\,Y_1^q(\theta,\phi)$ for $q = 0, \pm 1$:

$$z = r\cos\theta \propto r\,Y_1^0, \qquad x \pm iy \propto r\,Y_1^{\pm 1}.$$

The matrix element factorizes into a radial integral and an angular integral:

$$\langle n'\ell'm'|e\hat{z}|n\ell m\rangle = e\underbrace{\int_0^\infty R_{n'\ell'}\,r^3\,R_{n\ell}\,dr}_{\text{radial}} \times \underbrace{\int Y_{\ell'}^{m'*}\,Y_1^0\,Y_\ell^m\,d\Omega}_{\text{angular}}.$$

If either integral vanishes, the transition is forbidden.

**Why** $\Delta\ell = \pm 1$. Under parity ($\vec{r} \to -\vec{r}$), spherical harmonics transform as $Y_\ell^m \to (-1)^\ell Y_\ell^m$. The operator $\hat{z}$ is parity-odd: it picks up a factor of $-1$. The angular integral is nonzero only when the integrand has even overall parity:

$$(-1)^{\ell'}\times(-1)^1\times(-1)^\ell = (-1)^{\ell+\ell'+1} = +1 \implies \ell + \ell' \text{ is odd.}$$

So $\ell'$ and $\ell$ must have opposite parity: $\Delta\ell \neq 0$. The triangle rule for coupling angular momenta $\ell$, 1, and $\ell'$ (from the Gaunt coefficient structure of the integral) further requires $|\ell - \ell'| \leq 1$. Combined with the parity requirement, the only possibility is:

$$\Delta\ell = \pm 1.$$

**Why** $\Delta m = 0$ **or** $\pm 1$. The $\phi$-dependence of $Y_\ell^m$ is $e^{im\phi}$. The azimuthal part of the angular integral is:

$$\int_0^{2\pi}e^{-im'\phi}\,e^{iq\phi}\,e^{im\phi}\,d\phi = 2\pi\,\delta_{m',\,m+q}.$$

For $z$-polarized light ($q = 0$): $\Delta m = 0$. For $\sigma^+$ circularly polarized light ($q = +1$): $\Delta m = +1$. For $\sigma^-$ ($q = -1$): $\Delta m = -1$.

<!-- → [DIAGRAM: angular momentum coupling diagram showing a photon (L=1, q=0,±1) absorbed by an atom with initial (ℓ,m) → final (ℓ',m'), illustrating all allowed combinations as a 3×3 grid] -->

![angular momentum coupling diagram showing a photon (L=1, q=0,±1) absorbed by an atom with initial (ℓ,m) → final (ℓ',m'), illustrating all…](../images/06-radiation-and-fermis-golden-rule-fig-03.png)
*Figure 6.3 — angular momentum coupling diagram showing a photon (L=1, q=0,±1) absorbed by an atom with initial (ℓ,m) → final (ℓ',m'), illustrating all…*

The electric-dipole operator acts only on the orbital part of the wave function, so $\Delta s = 0$.

The full selection rules are:

$$\boxed{\Delta\ell = \pm 1, \qquad \Delta m = 0, \pm 1, \qquad \Delta s = 0.}$$

These results follow from two calculations — a parity argument and an azimuthal integral — and can be reproduced from the structure of spherical harmonics alone.

**Forbidden means slow, not impossible.** The $2s \to 1s$ transition has $\Delta\ell = 0$ and is electric-dipole forbidden. It occurs via two-photon decay, with both photons carrying angular momentum, and has lifetime $\approx 0.12$ s — eight orders of magnitude longer than the allowed $2p \to 1s$ transition. The 21-cm hydrogen hyperfine line (magnetic dipole, $\Delta\ell = 0$) has a lifetime of $\sim 10^7$ years. Both transitions occur; they are slow.

![Hydrogen electric-dipole transitions from n=1,2,3: energy levels arranged by n (vertical) and ℓ (horizontal, s left to d right), with solid arrows for allowed Δℓ=±1 transitions (2p→1s, 3p→1s, 3p→2s, 3d→2p) and no arrows for forbidden transitions, with the 2s level marked as metastable](../images/06-radiation-and-fermis-golden-rule-fig-04.png)
*Figure 6.4 — Hydrogen electric-dipole transition diagram: solid arrows connect levels satisfying Δℓ=±1; the absence of an arrow from 2s to 1s marks it as metastable, with no E1 decay path available.*

---

## The Einstein A and B Coefficients

In 1917 — a decade before quantum mechanics was complete — Einstein derived the relationship between spontaneous emission, stimulated emission, and absorption from thermodynamic equilibrium alone. The argument does not require knowing any matrix elements.

Let $N_1$ and $N_2$ be the populations of the lower and upper levels, $u(\omega)$ the spectral energy density of the radiation field at the transition frequency. Three processes: absorption ($N_1 B_{12}\,u(\omega)$), stimulated emission ($N_2 B_{21}\,u(\omega)$), and spontaneous emission ($N_2 A_{21}$). At thermal equilibrium, $N_2/N_1 = e^{-\hbar\omega/k_BT}$ and $u(\omega)$ is the Planck distribution. Setting upward and downward rates equal and requiring consistency gives:

$$B_{12} = B_{21}, \qquad \frac{A_{21}}{B_{21}} = \frac{\hbar\omega^3}{\pi^2 c^3}.$$

The $A/B$ ratio grows as $\omega^3$. At optical frequencies and room temperature, $A_{21} \gg B_{21}\,u(\omega)$ — spontaneous emission dominates. At radio frequencies (NMR, microwave), $B_{21}\,u(\omega)$ dominates — which is why NMR signal is detectable and why laser gain requires population inversion.

Using the golden rule with the photon density of states $\rho_{\mathrm{photon}}(\omega) = V\omega^2/(\pi^2 c^3)$ and averaging over all photon polarizations and emission directions:

$$\boxed{A_{21} = \frac{\omega^3}{3\pi\epsilon_0\hbar c^3}\,|\langle 1|e\hat{\vec{r}}|2\rangle|^2.}$$

The factor of 3 comes from the isotropic average over polarizations: $\langle|\hat{z}|^2\rangle_{\mathrm{avg}} = |\langle\vec{r}\rangle|^2/3$.

![Einstein A/B triptych: three side-by-side two-level diagrams — absorption (one photon in, population moves up), stimulated emission (one photon in, two out, population moves down), spontaneous emission (no photon in, one photon out in a random direction) — with rate indicators showing field-density dependence for the first two and field-independence for the third](../images/06-radiation-and-fermis-golden-rule-fig-05.png)
*Figure 6.5 — Three radiative processes: absorption and stimulated emission both scale with the field energy density u(ω); spontaneous emission proceeds at rate A₂₁ independent of the field, explaining why lasers require population inversion.*

---

## Computing the 2p → 1s Lifetime

**Which transitions are allowed?** From the $n=2$ manifold to $n=1$:

- $2s \to 1s$: $\Delta\ell = 0 - 0 = 0$. Forbidden.
- $2p \to 1s$: $\Delta\ell = 0 - 1 = -1$. Allowed.

All three $2p$ substates ($m = -1, 0, +1$) connect to $1s$ ($m=0$) with $\Delta m = 0, -1, +1$ respectively — all allowed.

**The dipole matrix element.** We take the $2p_0$ state ($m=0$) with $z$-polarized light. The matrix element factorizes:

$$\langle 1s|\hat{z}|2p_0\rangle = \int_0^\infty R_{10}(r)\,r^3\,R_{21}(r)\,dr \times \int Y_0^{0*}\cos\theta\,Y_1^0\,d\Omega.$$

**Radial integral.** The hydrogen radial functions are:

$$R_{10}(r) = 2\,a_0^{-3/2}\,e^{-r/a_0}, \qquad R_{21}(r) = \frac{1}{\sqrt{24}}\,a_0^{-3/2}\,\frac{r}{a_0}\,e^{-r/2a_0}.$$

Setting $u = 3r/(2a_0)$ and using $\int_0^\infty u^n e^{-u}\,du = n!$:

$$\mathcal{R} = \int_0^\infty R_{10}\,r^3\,R_{21}\,dr = \frac{256}{81\sqrt{6}}\,a_0.$$

**Angular integral.** With $Y_0^0 = (4\pi)^{-1/2}$ and $Y_1^0 = \sqrt{3/(4\pi)}\cos\theta$:

$$\int Y_0^{0*}\cos\theta\,Y_1^0\,d\Omega = \frac{\sqrt{3}}{4\pi}\cdot 2\pi\int_0^\pi\cos^2\theta\,\sin\theta\,d\theta = \frac{\sqrt{3}}{4\pi}\cdot 2\pi\cdot\frac{2}{3} = \frac{1}{\sqrt{3}}.$$

**Full matrix element:**

$$\langle 1s|\hat{z}|2p_0\rangle = \frac{256}{81\sqrt{6}}\cdot\frac{1}{\sqrt{3}}\,a_0 = \frac{256}{243\sqrt{2}}\,a_0.$$

For the spontaneous emission rate, we average over all $2p$ substates and photon polarizations (the standard result from summing over $m = -1, 0, +1$ with spherical symmetry):

$$|\langle 1s|e\hat{\vec{r}}|2p\rangle|^2_{\mathrm{avg}} = \frac{e^2 \times 2^{15}}{3^{10}}\,a_0^2.$$

<!-- → [TABLE: hydrogen radial integrals |ℛ_{n'ℓ', nℓ}|² in units of a₀² for transitions 2p→1s, 3p→1s, 3p→2s, 3d→2p — three columns: transition, |ℛ|², angular factor] -->

**The emission rate and lifetime.** The photon energy for $2p \to 1s$: $\hbar\omega = 13.6\,(1 - 1/4)$ eV $= 10.2$ eV, so $\omega = 1.55\times10^{16}$ rad/s. Applying the Einstein $A$-coefficient formula:

$$A_{21} = \frac{\omega^3}{3\pi\epsilon_0\hbar c^3}\,|\langle 1s|e\hat{\vec{r}}|2p\rangle|^2_{\mathrm{avg}} \approx 6.3\times10^8\,\text{s}^{-1}.$$

$$\tau = \frac{1}{A_{21}} \approx 1.6\,\text{ns}.$$

The measured value is $\tau = 1.596$ ns. Agreement to the accuracy of the approximations made — chiefly the dipole approximation, which introduces negligible error since $ka_0 \ll 1$.

**The limit of the derivation.** This calculation assumed the electromagnetic field is classical. An atom in its excited eigenstate, with no photons present, should remain there indefinitely under this framework — there is no time-dependent perturbation. Yet excited atoms decay. They decay because the electromagnetic field is quantum, and the vacuum carries zero-point fluctuations. The mechanism for why $A_{21} \neq 0$ in the first place requires quantizing the field — which Dirac did in the same 1927 paper in which he derived the golden rule. The semiclassical calculation gives the correct number via the $A/B$ ratio argument, but not the correct mechanism. That boundary is visible from here.

---

## Exercises

**Warm-up**

1. *[Density of states in 2D]* Repeat the density-of-states derivation for a 2D gas (electrons in a plane, area $A$). (a) Show $\rho_{2D}(E) = Am/(2\pi\hbar^2)$, independent of energy. (b) Compare to the 3D result $\rho_{3D}(E) \propto \sqrt{E}$. (c) At what 2D electron density does the Fermi energy equal $1$ eV?
*What this tests: extending the counting argument to lower dimension; recognizing that the flat 2D density of states is the physics behind quantum well devices.*

2. *[Selection rules, case by case]* For each hydrogen transition, state allowed or forbidden; if forbidden, which rule kills it; if allowed, which light polarization drives it. (a) $3d_{m=0} \to 2p_{m=0}$. (b) $3d_{m=+2} \to 2p_{m=+1}$. (c) $3s \to 2s$. (d) $4f_{m=-1} \to 3d_{m=0}$. (e) $2p_{m=0} \to 1s$.
*What this tests: applying the two calculations (parity and azimuthal integral) without memorization.*

3. *[Einstein coefficients for sodium]* The sodium D-line ($3p \to 3s$, $\lambda = 589$ nm) has lifetime $\tau = 16$ ns. (a) Compute $A_{21}$. (b) Compute $B_{21}$ using $A_{21}/B_{21} = \hbar\omega^3/(\pi^2 c^3)$. (c) At what spectral energy density does stimulated emission equal spontaneous emission? (d) At what temperature does thermal radiation produce this energy density? Comment on whether thermal light can efficiently drive stimulated optical emission.
*What this tests: connecting the abstract Einstein relations to numbers; appreciating why optical lasers require population inversion rather than thermal driving.*

**Application**

4. *[Golden rule for ionization]* An electron in a 1D box ($L = 10$ nm) in its ground state is exposed to a weak time-independent perturbation $V_0 = 10^{-3}$ eV. (a) Compute $E_1 = \pi^2\hbar^2/(2mL^2)$ in eV. (b) Evaluate the 1D free-particle density of states $\rho_{1D}(E) = L\sqrt{m/(2E)}/(2\pi\hbar)$ at $E = E_1$. (c) Using $|\langle k_f|V_0|1\rangle|^2 = V_0^2 L/2$, apply the golden rule to find the ionization rate $W$. (d) Is $W \cdot t \ll 1$ satisfied for $t = 1\,\mu\text{s}$?
*What this tests: applying the golden rule with the 1D density of states; verifying the validity condition.*

5. [*Radial integral for* $3p \to 1s$] (a) Write out $R_{10}(r)$ and $R_{31}(r)$ explicitly. (b) Set up the integral $\mathcal{R} = \int_0^\infty R_{10}\,r^3\,R_{31}\,dr$. (c) Evaluate using the substitution $u = 4r/(3a_0)$ and the Gamma function. (d) Compute the ratio $|\mathcal{R}_{10,31}|^2/|\mathcal{R}_{10,21}|^2$ and determine the ratio of rates $A(3p\to 1s)/A(2p\to 1s)$ including the $\omega^3$ factor.
*What this tests: extending the radial integral calculation to a different transition; seeing that the* $\omega^3$ *factor is not negligible.*

6. [*Branching ratios for* $3p$] The $3p$ state decays to both $1s$ and $2s$. (a) Compute $\hbar\omega$ for each branch. (b) Using $|\langle 2s|\hat{r}|3p\rangle|^2 \approx 0.093\,a_0^2$ and the $3p\to 1s$ result from exercise 5, compute both $A$-coefficients. (c) Find the branching fractions to each lower state. (d) Compute the total decay rate $\Gamma_{\mathrm{total}} = A(3p\to 1s) + A(3p\to 2s)$ and the observed lifetime $\tau = 1/\Gamma_{\mathrm{total}}$. Compare to the measured value $\tau_{3p} \approx 5.3$ ns.
*What this tests: combining multiple* $A$-*coefficients into a total decay rate; the* $\omega^3$ *factor's role in determining which branch dominates.*

**Synthesis**

7. *[Purcell effect]* In a $\text{high-}Q$ electromagnetic cavity resonant with an atomic transition, the photon density of states at the atomic frequency is modified. The Purcell factor $F_P = (3/4\pi^2)(\lambda/n)^3(Q/V)$ gives the emission rate enhancement relative to free space. (a) For a cavity with $Q = 10^5$, mode volume $V = (\lambda/2)^3$, $n = 1$: compute $F_P$. (b) For hydrogen $2p \to 1s$ with $A_{\mathrm{free}} \approx 6\times10^8$ $\text{s}^{-1}$, compute the enhanced rate. (c) In one sentence: is the enhancement from the matrix element, the density of states, or both? (d) If the cavity is detuned so the photon density of states at the atomic frequency is suppressed by $10^{-3}$, compute the inhibited lifetime and explain why inhibited spontaneous emission is useful for quantum memory.
*What this tests: applying the golden rule to an engineered density of states; connecting the Purcell factor to the three-ingredient structure of the formula.*

8. *[Wigner–Weisskopf and the validity window]* The golden rule requires $2\pi/\Delta\omega \ll t \ll \hbar/|V_{fi}|$. (a) For hydrogen $2p \to 1s$: estimate the lower bound using $\Delta\omega \sim \omega_{21}$ (the photon continuum bandwidth available). (b) Estimate the upper bound using $|V_{fi}| \sim eE_0 a_0$ for a field $E_0 = 1$ V/m. (c) How many orders of magnitude wide is the valid window? (d) Wigner–Weisskopf theory derives $P(t) = e^{-\Gamma t}$ by resumming all orders of perturbation theory. At $t \gg 1/\Gamma$, the first-order result $P \approx \Gamma t$ clearly fails (probability exceeds 1). Explain in one sentence how the resummation resolves this: what does the geometric series $\sum_n (-\Gamma t)^n / n!$ converge to?
*What this tests: honest confrontation with the logical seam in the derivation; understanding what Wigner–Weisskopf adds.*

**Challenge**

9. *[Electromagnetic vacuum and the Lamb shift — scaling argument]* The Lamb shift arises because the $2s$ electron, with $|\psi_{2s}(0)|^2 \neq 0$, couples differently to vacuum fluctuations than the $2p$ electron, with $|\psi_{2p}(0)|^2 = 0$. (a) The rms fluctuation of the vacuum electric field at frequency $\omega$ in a volume $V$ is $\delta E_\omega \sim \sqrt{\hbar\omega/\epsilon_0 V}$. The electron's position fluctuates under this field by $\delta r_\omega \sim e\delta E_\omega/(m\omega^2)$. Show that the mean-square position fluctuation integrated over all photon modes is $\langle(\delta r)^2\rangle \sim (\alpha/\pi)(a_0^2)\ln(\omega_{\mathrm{max}}/\omega_{\mathrm{min}})$ where $\alpha = e^2/(4\pi\epsilon_0\hbar c)$ is the fine-structure constant. (b) The energy shift from this fluctuation is $\delta E \approx (1/6)\langle(\delta r)^2\rangle\nabla^2 V$. For a Coulomb potential, $\nabla^2(-e^2/4\pi\epsilon_0 r) = (e^2/\epsilon_0)|\psi(0)|^2$. Use this to estimate the Lamb shift as an energy scale. (c) The $2s$ state has $|\psi_{2s}(0)|^2 = 1/(\pi a_0^3)$; the $2p$ state has $|\psi_{2p}(0)|^2 = 0$. What does this predict for the sign of the $2s$ shift relative to $2p$?
*What this tests: connecting the semiclassical framework of this chapter to QED at the level of dimensional analysis; seeing why the* $2s$ *and not the* $2p$ *is shifted.*

---

## References

Dirac, P. A. M. (1927). The quantum theory of the emission and absorption of radiation. *Proceedings of the Royal Society of London A*, 114, 243–265.

Einstein, A. (1917). Zur Quantentheorie der Strahlung. *Physikalische Zeitschrift*, 18, 121–128.

Lamb, W. E., & Retherford, R. C. (1947). Fine structure of the hydrogen atom by a microwave method. *Physical Review*, 72, 241–243.

Ewen, H. I., & Purcell, E. M. (1951). Observation of a line in the galactic radio spectrum. *Nature*, 168, 356.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §11.2–11.3.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §5.7–5.8.

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Chapter 14.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. II. Wiley. Chapter XIII.

Haroche, S., & Kleppner, D. (1989). Cavity quantum electrodynamics. *Physics Today*, 42(1), 24–30.

