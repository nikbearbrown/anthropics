# Module M-17 — Units, Dimensions, and Estimation

The hydrogen atom has a characteristic radius. Classical electrodynamics predicts no such radius: a classically radiating electron spirals inward continuously, with no preferred stopping point, until it reaches zero. Quantum mechanics predicts one. The size of that radius follows from dimensional analysis alone — three constants, one length, no differential equation required. This module builds toward that argument.

Read it before Chapter I·1, which argues from the breakdown of classical predictions. Every argument there is at root a statement about scales. To see why classical physics fails at the atomic scale, we need to know what sets that scale.

---

## Dimensions as Algebra

Every physical quantity carries a dimension — a label for what kind of thing is being measured. In mechanics the three base dimensions are length $L$, mass $M$, and time $T$. We write $[q]$ for the dimension of $q$:

$$[\text{speed}] = LT^{-1}, \quad [\text{acceleration}] = LT^{-2}, \quad [\text{force}] = MLT^{-2}, \quad [\text{energy}] = ML^2T^{-2}.$$

Dimensions multiply and divide like algebraic symbols. The **principle of dimensional homogeneity**: only quantities of the same dimension can be added, subtracted, or equated. A dimensionally inconsistent equation is certainly wrong. A dimensionally consistent equation is merely allowed — consistency is necessary, not sufficient, for truth.

A pure number ($\tfrac{1}{2}$, $\pi$, $e$) carries no dimension and can never introduce a dimensional error. This matters: dimensional analysis can determine the *form* of an answer — which variables appear and with what powers — but it can never supply a numerical coefficient. The pendulum period scales as $\sqrt{\ell/g}$; the factor $2\pi$ requires solving the differential equation.

---

## The Method: Dimensional Analysis

**Worked derivation — the pendulum period.** The period $T_p$ plausibly depends on the length $\ell$, gravitational acceleration $g$, and bob mass $m$. We assume $T_p = C\ell^a g^b m^c$ and match dimensions (both sides must equal $T^1 L^0 M^0$):

- Mass: $c = 0$ — mass is irrelevant.
- Time: $-2b = 1 \implies b = -\tfrac{1}{2}$.
- Length: $a + b = 0 \implies a = \tfrac{1}{2}$.

$$T_p = C\sqrt{\frac{\ell}{g}}.$$

The dependence on $\ell$ and $g$ is determined without solving the equation of motion. The factor $C = 2\pi$ requires the full theory.

The general structure: any physically meaningful relation among $n$ dimensioned variables built from $k$ independent base dimensions can be rewritten as a relation among $n-k$ dimensionless groups. The dimensionless groups are the null space of the exponent matrix. This is the Buckingham $\Pi$-theorem. [verify: Buckingham, Physical Review 4 (1914)]

---

## $\hbar$ as the Quantum of Action

Planck's constant $h = 6.626\times10^{-34}$ J·s; $\hbar = h/2\pi = 1.055\times10^{-34}$ J·s. Its dimension:

$$[\hbar] = \text{J·s} = ML^2T^{-1} = \text{action} = \text{energy}\times\text{time} = \text{momentum}\times\text{length}.$$

$\hbar$ is an action, not an energy. It quantizes angular momentum (orbital angular momentum is $\ell$ in units of $\hbar$) and sets the scale of the uncertainty principle $\Delta x\,\Delta p\geq\hbar/2$.

Recognizing $\hbar$ as an action — not just "a small number" — is the conceptual step that makes quantization feel systematic. Whenever the relevant action in a physical problem is much larger than $\hbar$, quantum effects are negligible; when the action is comparable to $\hbar$, quantum effects dominate. This is the single comparison that separates classical from quantum physics, and it is dimensional.

---

## The Bohr Radius by Dimensional Analysis

The hydrogen ground state has a characteristic length set by the constants that appear in the problem: $\hbar$ (quantum of action), $m_e$ (electron mass), and $e^2/4\pi\epsilon_0$ (the electromagnetic coupling, with dimension $ML^3T^{-2}$). We want a length from these three. Assuming $a_0 = \hbar^\alpha m_e^\beta(e^2/4\pi\epsilon_0)^\gamma$ and matching dimensions:

- Mass $M$: $\beta + \gamma = 0$
- Length $L$: $2\alpha + 3\gamma = 1$
- Time $T$: $-\alpha - 2\gamma = 0$

Solving: $\gamma = -1$, $\beta = 1$, $\alpha = 2$. Therefore:

$$a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2} \approx 5.29\times10^{-11}\text{ m} = 0.529\text{ Å.}$$

No Schrödinger equation was solved. Dimensional analysis predicts the atomic size up to a pure numerical factor, which turns out to be 1. Classical electrodynamics has no analogous prediction — a classical electron spirals inward on a timescale of order $10^{-11}$ s with no preferred stopping radius. The existence of $a_0$ is quantum.

---

## The Compton Wavelength

The length scale where quantum and relativistic effects are both significant is set by $\hbar$, $m_e$, and $c$. The unique combination with dimension of length:

$$\lambda_C = \frac{\hbar}{m_e c}\approx3.86\times10^{-13}\text{ m.}$$

Above $\lambda_C$, non-relativistic QM is adequate. Below it, pair production and quantum field effects dominate. The Compton effect — the shift in X-ray wavelength upon scattering from electrons — is explained by treating photons as particles and using $\lambda_C$ as the relevant scale.

![Hierarchy of atomic length scales on a logarithmic ruler](../images/17-units-dimensions-and-estimation-fig-01.png)
*Figure 17.1 — Hierarchy of atomic length scales: the Bohr radius $a_0 \approx 0.529$ Å, the Compton wavelength $\lambda_C \approx 3.86 \times 10^{-3}$ Å, and the classical electron radius $r_e \approx 2.8 \times 10^{-5}$ Å are separated by equal factors of $\alpha^{-1} \approx 137$ on a logarithmic ruler.*

---

## Order-of-Magnitude Estimation

We decompose the unknown into factors each estimable to within a factor of ten, then combine. Only the exponent of the result is to be trusted; the leading digit is not. When we have a plausible low bound $x_\text{lo}$ and high bound $x_\text{hi}$, the natural midpoint on a log scale is the geometric mean $\sqrt{x_\text{lo}\cdot x_\text{hi}}$.

**De Broglie wavelength of a 1 eV electron.** Using $\lambda = h/p = h/\sqrt{2m_eE}$:

$$\lambda = \frac{6.626\times10^{-34}\text{ J·s}}{\sqrt{2\times9.11\times10^{-31}\text{ kg}\times1.602\times10^{-19}\text{ J}}}\approx1.23\text{ nm.}$$

This is atomic scale — consistent with why electron diffraction in crystals (Davisson-Germer, 1927) was decisive evidence for matter waves. The estimate required no QM: only dimensional combination of known constants.

**When classical physics fails.** At room temperature, $k_BT\approx25$ meV. For a macroscopic oscillator of frequency 1 kHz, the quantum $h\nu\approx6.6\times10^{-31}$ J. Ratio: $h\nu/k_BT\approx10^{-10}$ — classical physics is completely adequate.

For an atomic electron in hydrogen, the relevant energy is the Rydberg $\approx13.6$ eV. At room temperature, $k_BT\approx0.025$ eV, so $E_1/k_BT\approx540$ — quantum effects dominate entirely. The crossover between classical and quantum behavior is the dimensional comparison $k_BT$ vs. $\hbar\omega$. Chapter I·1 returns to this comparison repeatedly.

![Classical vs quantum crossover axis showing k_BT vs hbar-omega ratio](../images/17-units-dimensions-and-estimation-fig-02.png)
*Figure 17.2 — Classical-versus-quantum crossover: a logarithmic axis of the ratio $\hbar\omega/k_BT$ spanning from the macroscopic pendulum ($\approx 10^{-10}$, deep classical) to hydrogen at room temperature ($\approx 540$, deep quantum), with the threshold at ratio $= 1$ dividing the two regimes.*

---

## Significant Figures and Relative Uncertainty

Significant figures encode relative uncertainty. For a product or quotient $q = A^m B^n$, the relative uncertainties combine in quadrature:

$$\frac{\delta q}{q} = \sqrt{\left(m\frac{\delta A}{A}\right)^2 + \left(n\frac{\delta B}{B}\right)^2}.$$

The exponent amplifies the relative uncertainty of its factor. An exponent of 3 amplifies threefold. For the Bohr radius $a_0\propto\hbar^2/m_e$: a 1% error in $\hbar$ produces a 2% error in $a_0$.

The least precise input dominates in a chain of multiplications. A result quoted to three significant figures is known to $\pm0.5\%$. Quoting more digits than the inputs justify does not add precision.

---

## Natural Units ($\hbar = c = 1$)

In particle physics and advanced QM, it is conventional to set $\hbar = c = 1$ (and sometimes $k_B = 1$). In these units, mass, energy, momentum, and inverse length all share the same dimension. Energies are quoted in eV or MeV; lengths are in $\text{eV}^{-1}$ via the conversion:

$$\hbar c\approx197.3\text{ MeV·fm.}$$

To restore SI factors from a natural-units result: count the powers of $\hbar$ and $c$ needed to give the right dimension. A cross-section $\sigma$ has dimension $L^2 = (\hbar c)^2/\text{energy}^2$; a lifetime $\tau$ has dimension $T = \hbar/\text{energy}$.

Natural units are a precision tool, not a shortcut. A student who sets $\hbar = c = 1$ without being able to restore the factors is not working with full understanding. Practice the restoration: if you compute a length in natural units and get a number in $\text{MeV}^{-1}$, multiply by $\hbar c\approx197$ MeV·fm to recover meters.

One notational hazard: $\hbar$ vs. $h$. The de Broglie relation is $\lambda = h/p$; written with wavenumber $k = 2\pi/\lambda$, this is $k = p/\hbar$. Confusing $h$ and $\hbar$ introduces a factor of $2\pi$ — a silent error with no dimensional signal.

<!-- → [TABLE: key quantum-physics constants in SI and natural units — rows for ħ, c, m_e, k_B, e²/4πε₀, a₀, λ_C; columns for SI value with units, natural-units value, and the dimensional combination they set; this is the reference table students will check every time they need to restore SI factors] -->

---

## Quick Practice

1. **Dimensional derivation.** A mass $m$ on a spring of stiffness $k$ (units N/m = kg/s²) oscillates with period $T$. Using only dimensional analysis, derive how $T$ depends on $m$ and $k$. Why can the amplitude of oscillation not appear in the result?

2. **Bohr radius check.** Verify that $\hbar^2/(m_e e^2/4\pi\epsilon_0)$ has units of length. Use SI values: $[\hbar] = \text{J·s}$, $[m_e] = \text{kg}$, $[e^2/4\pi\epsilon_0] = \text{N·m}^2 = \text{kg·m}^3\text{s}^{-2}$. Show every cancellation explicitly.

3. **Natural units restoration.** In natural units ($\hbar = c = 1$), the lifetime of an excited hydrogen state is $\tau = A/(m_e\alpha^5)$, where $\alpha\approx1/137$ is the fine-structure constant. What dimensions must $A$ carry in natural units? Restore $\hbar$ and $m_ec^2$ to express $\tau$ in seconds, given $m_ec^2 = 511$ keV and $\hbar\approx6.6\times10^{-16}$ eV·s.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests dimensional homogeneity.*
   Each of the following expressions contains a dimensional error. Identify the error in each case and state what corrected form would be dimensionally consistent: (a) $v = at^2$ (where $v$ is speed, $a$ is acceleration, $t$ is time); (b) $E = p/m$ (where $E$ is energy, $p$ is momentum, $m$ is mass); (c) $\omega = \sqrt{k}$ (where $\omega$ is angular frequency in rad/s and $k$ is spring stiffness in N/m).
   *Tests: dimensional homogeneity as a consistency check; identifying and correcting dimensional errors.*

2. *Difficulty: Warm-up — tests the* $\hbar$ *vs.* $h$ *distinction.*
   The de Broglie wavelength is $\lambda = h/p$ and the Bohr radius is $a_0 = \hbar^2/(m_ee^2/4\pi\epsilon_0)$. (a) Write the de Broglie relation using $\hbar$ and wavenumber $k = 2\pi/\lambda$; verify dimensional consistency. (b) A student accidentally uses $h$ instead of $\hbar$ in the Bohr radius formula. By what factor does their answer differ from the correct one? (c) Compute the de Broglie wavelength of an electron with kinetic energy 10 eV in nm.
   *Tests: the h vs. ħ distinction; propagation of the error; a numerical calculation.*

3. *Difficulty: Warm-up — tests the Buckingham Π-theorem by counting.*
   A wave travels on the surface of a liquid. The wave speed $v$ could depend on the wavelength $\lambda$, the liquid density $\rho$, the gravitational acceleration $g$, and the surface tension $\gamma$ (dimension $MT^{-2}$). There are 5 variables and 3 base dimensions ($M$, $L$, $T$). (a) How many dimensionless groups does the Buckingham $\Pi$-theorem predict? (b) In the limit of long wavelengths (gravity waves), only $v$, $\lambda$, $g$ matter. Use dimensional analysis to derive $v$ as a function of $\lambda$ and $g$. (c) In the limit of short wavelengths (capillary waves), only $v$, $\lambda$, $\rho$, $\gamma$ matter. Derive $v$ as a function of these three.
   *Tests: counting dimensionless groups; solving dimensional analysis in two limiting cases.*

**Application**

4. *Difficulty: Application — Bohr radius and the Compton wavelength.*
   (a) Derive the Bohr radius $a_0 = 4\pi\epsilon_0\hbar^2/(m_ee^2)$ by dimensional analysis, matching dimensions explicitly as in the text. (b) The fine-structure constant is $\alpha = e^2/(4\pi\epsilon_0\hbar c)\approx1/137$; verify it is dimensionless. (c) Express $a_0$ in terms of $\alpha$, $\lambda_C = \hbar/(m_ec)$, and numerical constants only (no $m_e$, $e$, $\hbar$ separately). (d) The Compton wavelength $\lambda_C\approx3.86\times10^{-13}$ m; use your formula to compute $a_0$ and verify it matches $5.29\times10^{-11}$ m.
   *Tests: full dimensional analysis of the Bohr radius; the fine-structure constant as dimensionless; expressing atomic scales through α and λ_C.*

5. *Difficulty: Application — classical vs. quantum crossover.*
   (a) For a particle of mass $m$ in a harmonic oscillator of frequency $\omega$, the classical energy at temperature $T$ is $k_BT$ and the quantum ground-state energy is $\tfrac{1}{2}\hbar\omega$. Find the crossover temperature $T^*$ at which $k_BT^* = \hbar\omega/2$. (b) For a nitrogen molecule ($m\approx28$ u, bond vibration frequency $\omega/2\pi\approx7\times10^{13}$ Hz), compute $T^*$ in Kelvin. Is the vibrational mode classical or quantum at room temperature (300 K)? (c) For a macroscopic pendulum ($\omega/2\pi = 1$ Hz), compute $T^*$. At what temperature would the pendulum become quantum mechanical?
   *Tests: the k_BT vs. ħω crossover; applying it to molecular and macroscopic systems; physical interpretation.*

6. *Difficulty: Application — natural units and restoration.*
   In natural units ($\hbar = c = 1$), the electron-proton cross-section for Compton scattering at energy $E$ is $\sigma\approx\pi\alpha^2/E^2$ where $\alpha = 1/137$. (a) Verify $\sigma$ has the correct dimension $L^2$ in natural units (where $1/E$ has dimension $L$). (b) Restore factors of $\hbar$ and $c$ to express $\sigma$ in SI units. (c) Compute $\sigma$ numerically at $E = m_ec^2 = 511$ keV and express the result in cm². (d) Compare to the classical electron radius $r_e = e^2/(4\pi\epsilon_0 m_ec^2)\approx2.8\times10^{-13}$ cm by verifying that $\sigma\approx\pi r_e^2\alpha^0$ at this energy — this is the Thomson cross-section.
   *Tests: natural units with a real formula; dimensional restoration; numerical evaluation; connecting to a classical quantity.*

**Synthesis**

7. *Difficulty: Synthesis — dimensional analysis and scale separation.*
   The hydrogen atom has three characteristic lengths: the Bohr radius $a_0\approx0.53$ Å (atomic scale), the Compton wavelength $\lambda_C\approx3.86\times10^{-3}$ Å (relativistic-quantum scale), and the classical electron radius $r_e = \alpha\lambda_C\approx2.8\times10^{-5}$ Å (classical electromagnetic scale). (a) Show that $a_0 = \lambda_C/\alpha$ and $r_e = \alpha\lambda_C$ using only the definitions $\alpha = e^2/(4\pi\epsilon_0\hbar c)$ and $\lambda_C = \hbar/(m_ec)$. (b) Arrange the three lengths in order and compute the ratios $a_0/\lambda_C$ and $\lambda_C/r_e$. (c) The separation $a_0\gg\lambda_C\gg r_e$ means non-relativistic QM is adequate for atomic structure. Explain in one sentence what physical effect becomes important when $r\sim\lambda_C$ and what becomes important when $r\sim r_e$.
   *Tests: deriving relations between scales using α; the hierarchy of length scales in atomic physics; physical interpretation of each scale.*

8. *Difficulty: Synthesis — estimation chain with uncertainty propagation.*
   Estimate the energy of the first excited state of the hydrogen atom using only dimensional analysis and order-of-magnitude reasoning (no Bohr model). (a) The only relevant length scale is $a_0$; the only relevant energy scale is built from $\hbar$, $m_e$, $a_0$, or equivalently from $\hbar$, $m_e$, and $e^2/4\pi\epsilon_0$. Use dimensional analysis to show the natural energy unit is $E_0 = \hbar^2/(m_ea_0^2) = m_ee^4/(4\pi\epsilon_0)^2\hbar^2$. (b) Compute $E_0$ in eV. (c) The actual ground state energy is $-13.6$ eV and the first excited state is at $-3.4$ eV, giving an excitation of $10.2$ eV. How does this compare to $E_0$? (d) Identify the pure numerical factor connecting $E_0$ to the Rydberg energy $13.6$ eV and explain where it comes from in the full Bohr-model calculation.
   *Tests: dimensional analysis gives the energy scale; connecting to the Rydberg; the pure numerical factor and its origin.*

**Challenge**

9. *Difficulty: Challenge — deriving the black-body scale from dimensional analysis.*
   Planck's radiation law contains a characteristic frequency set by the temperature $T$ and the fundamental constants. (a) The energy of a photon at thermal equilibrium is set by $k_BT$; its frequency by $E = h\nu$. What is the characteristic frequency $\nu^*$ in terms of $k_B$, $T$, and $h$? Compute $\nu^*$ at $T = 5778$ K (the Sun's surface temperature) in Hz and in eV. (b) The Wien displacement law states that the peak wavelength of black-body radiation is $\lambda_\text{max} = b/T$ where $b\approx2.898\times10^{-3}$ m·K. Use $\lambda\nu = c$ and your expression for $\nu^*$ to estimate the numerical coefficient $b$ in terms of $h$, $k_B$, and $c$. (c) The ultraviolet catastrophe of classical physics: the Rayleigh-Jeans law gives spectral energy density $u(\nu)\propto\nu^2 k_BT/c^3$, which diverges as $\nu\to\infty$. Dimensional analysis cannot fix this — it only tells you the combination $k_BT\nu^2/c^3$ has the right dimension. What additional constant must enter the full Planck formula to cure the divergence, and what dimension does it carry? (d) This is historically how Planck introduced $h$ in 1900: he needed a constant of action to cut off the high-frequency divergence. Identify $h$ in your dimensional analysis and state what quantum assumption Planck made to justify its introduction.
   *Tests: dimensional analysis of thermal radiation; the Wien law; the Rayleigh-Jeans divergence; the historical introduction of Planck's constant.*

---

## References

Buckingham, E. (1914). On physically similar systems; illustrations of the use of dimensional equations. *Physical Review*, 4, 345–376.

Griffiths, D. J. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. Section 1.2.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (2019). *Quantum Mechanics*, 2 vols. Wiley-VCH. Complement A-I.

NIST CODATA 2018 recommended values: $\hbar = 1.054571817\times10^{-34}$ J·s; $m_e = 9.1093837015\times10^{-31}$ kg; $a_0 = 5.29177210903\times10^{-11}$ m; $\lambda_C = 3.8615926796\times10^{-13}$ m.

NASA. (1999). *Mars Climate Orbiter Mishap Investigation Board Phase I Report*. (Unit conversion failure leading to spacecraft loss — the canonical engineering example of dimensional discipline.)
