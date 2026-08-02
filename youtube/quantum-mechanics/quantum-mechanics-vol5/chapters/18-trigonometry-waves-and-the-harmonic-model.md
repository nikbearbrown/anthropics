# Module M-18 — Trigonometry, Waves, and the Harmonic Model
*Refresher for QM chapters: I·2 (matter waves)*

Read this module before Chapter I·2. The sinusoidal wave $\psi(x,t) = Ae^{i(kx-\omega t)}$ appears in the first pages of that chapter, and every result — de Broglie's hypothesis, the double-slit interference pattern, the distinction between phase and group velocity — is a direct application of the wave model. Without fluency with $k$, $\omega$, phase, and superposition, matter waves remain a notational exercise rather than a physical picture. This module also builds the small-angle approximation ($\sin\theta \approx \theta$) that appears throughout the series in interference geometry.

---

## The Three Ratios and the Central Rule

In a right triangle, for an acute angle $\theta$:

$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}, \quad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}, \quad \tan\theta = \frac{\text{opposite}}{\text{adjacent}}.$$

These are dimensionless — pure numbers depending only on the angle, not the triangle's size. The component rule follows immediately: a vector of magnitude $F$ at angle $\theta$ measured from a chosen axis has $F_\text{along} = F\cos\theta$ and $F_\perp = F\sin\theta$. Check with extremes: at $\theta = 0$, the vector is purely along the axis and $F_\perp = 0$. Pythagorean identity: $\cos^2\theta + \sin^2\theta = 1$.

---

## The Unit Circle and the Radian

For any angle $\theta$ measured counterclockwise from the positive $x$-axis, the point on the unit circle is $(\cos\theta, \sin\theta)$. This extends the functions to all angles and makes periodicity manifest: period $2\pi$.

The **radian** measures angle by arc length on the unit circle: one radian subtends an arc equal to the radius. Radians are dimensionless (arc length divided by radius). The calculus identities $d\sin\theta/d\theta = \cos\theta$ and $d\cos\theta/d\theta = -\sin\theta$ hold only in radians — they depend on $\lim_{\theta\to 0}(\sin\theta)/\theta = 1$, which equals 1 only in radians (in degrees the limit is $\pi/180$). Always use radians in wave formulas and differential equations.

---

## Key Identities for Wave Physics

The addition formulas are the engine of interference calculations:

$$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta,$$
$$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta.$$

Double-angle forms ($\beta = \alpha$): $\sin 2\alpha = 2\sin\alpha\cos\alpha$; $\cos 2\alpha = 1 - 2\sin^2\alpha$.

The sum-to-product identity used in the interference derivation:

$$\cos A + \cos B = 2\cos\!\left(\frac{A+B}{2}\right)\cos\!\left(\frac{A-B}{2}\right).$$

---

## The Small-Angle Approximation

For small $\theta$ in radians:

$$\sin\theta \approx \theta, \qquad \tan\theta \approx \theta, \qquad \cos\theta \approx 1 - \tfrac{1}{2}\theta^2.$$

The geometric picture: for a small angle on the unit circle, the arc length $\theta$ and the vertical drop $\sin\theta$ are nearly the same short segment. The full Taylor series:

$$\sin\theta = \theta - \frac{\theta^3}{6} + \frac{\theta^5}{120} - \cdots, \qquad \cos\theta = 1 - \frac{\theta^2}{2} + \frac{\theta^4}{24} - \cdots.$$

The approximation $\sin\theta \approx \theta$ is good to $\sim 1\%$ for $|\theta| < 0.14$ rad ($\approx 8°$); to $\sim 10\%$ for $|\theta| < 0.45$ rad ($\approx 26°$). State the domain of validity when using it.

---

## The Sinusoidal Traveling Wave

A sinusoidal wave traveling in the $+x$ direction:

$$\psi(x,t) = A\cos(kx - \omega t + \varphi),$$

or in complex exponential form — the working form in QM:

$$\psi(x,t) = A\,e^{i(kx - \omega t)}.$$

<!-- → [TABLE: wave parameters — Symbol, Name, Dimension, Definition — rows for A (amplitude), k (wavenumber, L⁻¹, k=2π/λ), λ (wavelength, L, spatial period), ω (angular frequency, T⁻¹, ω=2πf), φ (phase offset, dimensionless), v_ph (phase velocity, LT⁻¹, v_ph=ω/k)] -->

The argument $kx - \omega t + \varphi$ must be dimensionless — a good dimensional check. A leftward-traveling wave has $kx + \omega t$ in the argument (equivalently, $k \to -k$).

**Euler's formula** bridges real and complex forms:

$$e^{i\theta} = \cos\theta + i\sin\theta.$$

The physical wave is the real part of the complex exponential. QM wavefunctions are genuinely complex, not just notational convenience — the imaginary part carries phase information that determines interference. The intensity (probability density) is $|\psi|^2 = \psi^*\psi$, not $\psi^2$.

---

## Superposition and Interference

The superposition principle: the total wave is the sum of its components. For two waves of equal amplitude differing only by a constant phase $\delta$, the sum-to-product identity gives:

$$\psi_1 + \psi_2 = A\cos(kx-\omega t) + A\cos(kx-\omega t+\delta) = 2A\cos(\delta/2)\cos(kx-\omega t+\delta/2).$$

The resultant is a wave at the same frequency with amplitude $2A|\cos(\delta/2)|$:

- $\delta = 0$ (in phase): amplitude $2A$ — constructive interference.
- $\delta = \pi$ (anti-phase): amplitude $0$ — destructive interference.
- General $\delta$: amplitude interpolates between 0 and $2A$.

![Three superposition cases showing constructive, destructive, and partial interference](../images/18-trigonometry-waves-and-the-harmonic-model-fig-01.png)
*Figure 18.1 — Wave superposition: $\delta = 0$ gives amplitude $2A$ (constructive), $\delta = \pi$ gives amplitude $0$ (destructive), and $\delta = \pi/2$ gives amplitude $A\sqrt{2}$ (partial), all consistent with the formula $2A|\cos(\delta/2)|$.*

---

## Group Velocity and Beats

Two waves of slightly different frequency and wavenumber: $(\omega, k)$ and $(\omega + d\omega, k + dk)$. Their sum:

$$\psi_1 + \psi_2 = 2A\cos\!\left(\frac{dk}{2}x - \frac{d\omega}{2}t\right)\cos\!\left(kx - \omega t\right).$$

The fast carrier oscillates at $k$, $\omega$; the slow envelope moves at:

$$v_g = \frac{d\omega}{dk}.$$

The **group velocity** $v_g$ is the speed of the envelope — the speed at which energy and information travel. For a non-dispersive medium, $\omega \propto k$ and $v_g = v_\text{ph}$. For a dispersive medium (like matter waves), $v_g \neq v_\text{ph}$, and a wave packet spreads as it travels.

![Group velocity vs phase velocity: carrier and envelope at two time snapshots](../images/18-trigonometry-waves-and-the-harmonic-model-fig-03.png)
*Figure 18.3 — Group versus phase velocity: the fast carrier advances at phase velocity $v_\text{ph} = v/2$ while the slow envelope travels at group velocity $v_g = v$ (twice as fast for a non-relativistic matter wave), shown at two successive times with a reference line anchored at the initial envelope peak.*

---

## Where These Methods Appear in the Quantum Series

### Matter Waves (I·2)

De Broglie's hypothesis assigns every particle of momentum $p$ a wavelength:

$$\lambda = \frac{h}{p}, \qquad k = \frac{p}{\hbar}, \qquad \omega = \frac{E}{\hbar}.$$

The quantum matter wave is then exactly the sinusoidal wave of this module:

$$\psi(x,t) = A\,e^{i(px/\hbar - Et/\hbar)} = A\,e^{i(kx - \omega t)}.$$

Every concept from above — wavenumber, angular frequency, phase, superposition — now has a quantum interpretation. The key new facts are the relations $k = p/\hbar$ and $\omega = E/\hbar$; the wave algebra is unchanged.

**Phase velocity of a de Broglie wave (non-relativistic).** For a free particle with $E = p^2/2m$:

$$\omega = \frac{\hbar k^2}{2m}, \qquad v_\text{ph} = \frac{\omega}{k} = \frac{\hbar k}{2m} = \frac{p}{2m} = \frac{v}{2}.$$

The phase velocity is half the particle's speed. The phase pattern moves at half-speed — it is not the particle.

**Group velocity of a de Broglie wave.** $v_g = d\omega/dk = \hbar k/m = p/m = v$. The group velocity equals the particle's classical speed. The envelope of the wave packet is what moves with the particle. Without the beats analysis, $v_\text{ph} = v/2$ seems surprising; with it, there is no paradox.

### Worked Example: De Broglie Double-Slit Interference

**Setup.** Electrons of momentum $p$ (hence $\lambda = h/p$, $k = p/\hbar$) pass through two slits separated by $d$. A detector screen is placed far enough away that rays from the two slits to a point at angle $\theta$ are nearly parallel.

**Path-length difference.** For a point at angle $\theta$ on the screen, the path lengths from the two slits differ by $\Delta = d\sin\theta$.

**Phase difference.** Each unit of path length contributes phase $k$ per unit length:

$$\delta = k\Delta = \frac{2\pi}{\lambda}d\sin\theta = \frac{pd\sin\theta}{\hbar}.$$

**Intensity.** From the superposition formula:

$$I(\theta) = 4A^2\cos^2\!\left(\frac{\delta}{2}\right) = 4A^2\cos^2\!\!\left(\frac{pd\sin\theta}{2\hbar}\right).$$

Constructive interference ($I = 4A^2$) when $\delta = 2\pi n$:

$$d\sin\theta = n\lambda, \qquad n = 0, \pm 1, \pm 2, \ldots$$

This is the standard double-slit condition — exactly the same as for light, with the de Broglie wavelength $\lambda = h/p$.

**Small-angle approximation.** For $\theta \ll 1$ rad, $\sin\theta \approx \theta$, and with screen distance $L$, the transverse position is $y = L\tan\theta \approx L\theta$. The fringe spacing is:

$$\Delta y = \frac{\lambda L}{d} = \frac{hL}{pd}.$$

The faster the electrons (larger $p$, smaller $\lambda$), the finer the fringes.

![Double-slit fringe intensity pattern for two de Broglie wavelengths](../images/18-trigonometry-waves-and-the-harmonic-model-fig-02.png)
*Figure 18.2 — Double-slit intensity $I(\theta) = 4A^2\cos^2(\pi d\sin\theta/\lambda)$ showing seven peaks for wavelength $\lambda$ (solid) and twice as many peaks for $\lambda/2$ (dashed), illustrating that higher particle momentum produces finer fringes.*

**Historical note.** The electron double-slit experiment was first performed with a biprism by Jönsson (1961); later with actual double slits by Merli, Missiroli, and Pozzi (1976); and, in the single-electron regime, by Tonomura et al. (1989). The buildup of the interference pattern one electron at a time — a particle landing at one spot, yet the ensemble forming a wave pattern — remains one of the most striking demonstrations in physics.

---

## Conventions and Pitfalls

**Radians are not optional in wave formulas.** The argument of $e^{i(kx-\omega t)}$ is in radians. $k$ has units rad/m; $x$ in meters; $kx$ is dimensionless. If you work with frequency $f$ (in Hz) rather than $\omega = 2\pi f$ (in rad/s), you must write $2\pi(x/\lambda - ft)$ or you lose a factor of $2\pi$.

**Sign convention for direction.** $\psi = Ae^{i(kx-\omega t)}$ travels in the $+x$ direction. $\psi = Ae^{i(kx+\omega t)}$ travels in the $-x$ direction. Fix the convention at the start of any calculation.

$|\psi|^2$, **not** $\psi^2$. The probability density is $|\psi|^2 = \psi^*\psi$. For a complex wave $Ae^{ikx}$, $|Ae^{ikx}|^2 = A^2$ — a constant. Writing $\psi^2$ instead gives $A^2e^{2ikx}$, which is incorrect.

$\lambda = 2\pi/k$, **not** $1/k$. The factor of $2\pi$ is the source of most $\text{off-}\text{by-}2\pi$ errors. Wavenumber $k$ counts radians per unit length; one wavelength is $2\pi$ radians.

$\hbar$ **vs.** $h$ **in de Broglie relations.** $\lambda = h/p$ uses $h$. The wavenumber form $k = p/\hbar$ uses $\hbar = h/2\pi$. Both are correct. The confusion arises when one mixes the formulas: $k = p/h$ (wrong by $2\pi$) or $\lambda = \hbar/p$ (wrong by $2\pi$).

**Phase velocity is not the particle velocity.** For a non-relativistic matter wave, $v_\text{ph} = v/2$. The particle's physical speed equals the group velocity. Do not use $v_\text{ph}$ to predict where the particle is.

---

## Quick Practice

1. **Phase and group velocity.** A relativistic particle has energy $E = \sqrt{(pc)^2 + (m_0c^2)^2}$. Show that $\omega = E/\hbar$ and $k = p/\hbar$ give $v_\text{ph} = c^2/v$ and $v_g = v$, where $v$ is the particle's classical speed. What happens to $v_\text{ph}$ for a massless particle?

2. **Double-slit fringe spacing.** Electrons are accelerated through a potential difference $V = 100$ V. (a) Find the kinetic energy, momentum, and de Broglie wavelength. (b) If the slit separation is $d = 1\,\mu\text{m}$ and the screen is at $L = 1$ m, find the fringe spacing $\Delta y = \lambda L/d$ in the small-angle approximation.

3. **Superposition and phase.** Two quantum waves $\psi_1 = e^{ikx}$ and $\psi_2 = e^{i(kx+\pi/3)}$ are superposed. Find $|\psi_1 + \psi_2|^2$ and verify it equals $4\cos^2(\pi/6) = 3$. Then find the phase $\delta$ for (a) maximal constructive interference and (b) fully destructive interference.

---

## Go Deeper

The source chapter — *Mathematics for Physics* Vol 1, Ch 3 — covers trigonometry and geometry in full, including force resolution, projectile range, and the law of cosines. For the wave physics extension (sinusoidal waves, interference, group and phase velocity): French, *Vibrations and Waves* (MIT Introductory Physics Series, W. W. Norton, 1971), Chs. 7–8; and Crawford, *Waves* (Berkeley Physics Course Vol. 3, McGraw-Hill, 1968), Ch. 1. For the quantum context: Griffiths, *Introduction to Quantum Mechanics* (3rd ed., Cambridge, 2018), §1.3–1.4.

---

## References

de Broglie, L. (1925). Recherches sur la théorie des quanta. *Annales de Physique*, 10 (series 10), 22–128.

Jönsson, C. (1961). Elektroneninterferenzen an mehreren künstlich hergestellten Feinspalten. *Zeitschrift für Physik*, 161, 454–474.

Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T., & Ezawa, H. (1989). Demonstration of single-electron buildup of an interference pattern. *American Journal of Physics*, 57, 117.

French, A. P. (1971). *Vibrations and Waves*. MIT Introductory Physics Series. W. W. Norton.

Crawford, F. S. (1968). *Waves*. Berkeley Physics Course, Vol. 3. McGraw-Hill.

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §1.3–1.4.
