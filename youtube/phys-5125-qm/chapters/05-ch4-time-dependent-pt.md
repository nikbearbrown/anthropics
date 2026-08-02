# Chapter 4 — Time-Dependent Perturbation Theory

*The clock sets the rule: how fast the Hamiltonian changes decides whether you reach for the sudden, the adiabatic, or the resonant approximation.*

<!-- Adapted from Prof. Feiguin's PHYS 5125 lecture notes. Prose lightly rewritten for original expression and clarity; all equations, derivations, and numbers are unchanged. Known slips listed in errata.md. -->

## Overview

Until now the Hamiltonian held still and we asked how its energies shifted. Here it moves, and the whole question changes: not "what are the corrected levels?" but "starting in state $|i\rangle$, what is the chance of landing in $|f\rangle$ later?" Energy is no longer conserved, so we stop tracking it and track amplitudes instead.

The honest organizing idea is that the clock picks the method. Compare how fast the perturbation changes against the system's own natural timescale, $1/\omega_{mn}$. Flip the Hamiltonian faster than the state can respond and the wave function is caught frozen — the sudden approximation, where the old state simply gets re-read in the new basis. Change it slowly enough and the state rides along, staying in the same instantaneous eigenstate — the adiabatic theorem, which carries a quiet surprise: a geometric (Berry) phase that remembers the path, not the clock. In between sits the driven middle ground, where a perturbation oscillating near a level spacing pumps probability back and forth — resonance, Rabi oscillations, and, taken to long times, Fermi's golden rule for steady transition rates.

Everything below is first- and second-order perturbation theory applied to one moving Hamiltonian. The trick is reading the clock before choosing the tool.

## 4. Time-dependent perturbation theory

We consider a Hamiltonian of the form

$$\hat{H} = \hat{H}_0 + \hat{V}(t) = \hat{H}_0 + \lambda f(t)\hat{V}$$

where the time profile of the perturbation lives in $f(t)$. We take the unperturbed problem $H_0$ to be already solved

$$\hat{H}_0 |n\rangle = E_n |n\rangle$$

No extra labels are needed here: energy is not conserved anymore, and we are not chasing energy corrections.

When $V=0$ the answer is immediate,

$$|\psi(t)\rangle = \sum_n C_n e^{-iE_n t/\hbar} |n\rangle$$

with the $C_n$ constant. Switch on the perturbation and these coefficients start to vary with time,

$$|\psi(t)\rangle = \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

*end lecture*

fixed by the Sch. eq.

$$i\hbar \frac{\partial}{\partial t} \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle = (\hat{H}_0 + \hat{V}(t)) \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

$$\rightarrow i\hbar \sum_n \dot{C}_n(t)\, e^{-iE_n t/\hbar} |n\rangle = \hat{V}(t) \sum_n C_n(t)\, e^{-iE_n t/\hbar} |n\rangle$$

Projecting onto the bra $\langle m | e^{\frac{iE_m t}{\hbar}}$

$$i\hbar \dot{C}_m = \sum_n \langle m | \hat{V}(t) | n \rangle\, C_n\, e^{i\omega_{mn} t} = \sum_n V_{mn}\, e^{i\omega_{mn} t}\, C_n$$

where $\omega_{mn} = \dfrac{E_m - E_n}{\hbar}$

This gives a coupled system of differential equations for the $C$'s

$$i\hbar \begin{pmatrix} \dot{C}_1 \\ \dot{C}_2 \\ \vdots \end{pmatrix} = \begin{pmatrix} V_{11} & V_{12}\, e^{i\omega_{12} t} & \cdots \\ V_{21}\, e^{i\omega_{21} t} & V_{22} & \\ \vdots & & V_{33} \end{pmatrix} \begin{pmatrix} C_1 \\ C_2 \\ \vdots \end{pmatrix}$$

Nothing has been approximated yet. As in the time-independent case, we now attack it order by order.

Suppose the system starts in some state $|i\rangle$ at $t=0$. We want the probability that, after evolving, it is found in a state $|f\rangle$.

Expand

$$C_f(t) = \delta_{fi} + \lambda\, C_f^{(1)}(t) + \lambda^2\, C_f^{(2)}(t) + \cdots$$

Substituting this into $\circledast$ above gives

$$C_f^{(1)}(t) = -\frac{i}{\hbar}\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\,\langle f|\hat{V}|i\rangle$$

so

$$C_f(t) = \delta_{fi} - \frac{\lambda i}{\hbar}\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\, V_{fi}$$

The probability of ending up in $|f\rangle \neq |i\rangle$ is

$$|C_f(t)|^2 = \frac{\lambda^2}{\hbar^2}|V_{fi}|^2\left|\int_0^t dt'\, f(t')\, e^{i\omega_{fi} t'}\right|^2$$

This estimate is reliable only when the transition probability stays small. Pushing to the next order gives the second-order correction.

$$C_n^{(2)} = \left(\frac{-i\lambda}{\hbar}\right)^2\sum_m \int_0^t dt'\int_0^{t'} dt''\, e^{i\omega_{mn} t'}\, V_{mn}\, f(t')\times e^{i\omega_{mi} t''}\, V_{mi}\, f(t'')$$

### Example: Kicking an oscillator

Take a harmonic oscillator sitting in its ground state at $t=-\infty$, and hit it with a weak potential

$$\hat{V}(t) = -eE\hat{x}\, e^{-t^2/\tau^2}$$

What is the chance of finding it in the first excited state $|1\rangle$ at $t=+\infty$?

**Solution:** $\quad V_{fi}(t) = -eE\langle 1|\hat{x}|0\rangle\, e^{-t^2/\tau^2}$

with $\hat{x} = \sqrt{\dfrac{\hbar}{2m\omega}}\,(a + a^\dagger)$

$$\to V_{fi}(t) = -eE\sqrt{\frac{\hbar}{2m\omega}}\, e^{-t^2/\tau^2}$$

$$\to C_f(\infty) = -eE\sqrt{\frac{\hbar}{2m\omega}}\int_{-\infty}^{\infty} dt'\, e^{-t^2/\tau^2}\, e^{-i\hbar\omega t'}$$

We finally obtain

$$|C_f(\infty)|^2 = \frac{e^2 E^2}{\hbar^2}\frac{\hbar}{2m\omega}\,\pi\tau^2\, e^{-\omega^2\tau^2/2}$$

### Example: two-level system

$$|\psi(t)\rangle = C_1(t)\, e^{-iE_1 t/\hbar}|1\rangle + C_2(t)\, e^{-iE_2 t/\hbar}|2\rangle$$

Apply a perturbation

$$\hat{V}(t) = V e^{i\omega t}|1\rangle\langle 2| + V e^{-i\omega t}|2\rangle\langle 1|$$

$$\to i\hbar\begin{pmatrix}\dot{C}_1\\[2pt]\dot{C}_2\end{pmatrix} = \begin{pmatrix} 0 & V e^{i\omega t} e^{i\omega_{12} t}\\[4pt] V e^{-i\omega t} e^{-i\omega_{12} t} & 0\end{pmatrix}\begin{pmatrix}C_1\\[2pt]C_2\end{pmatrix}$$

Abbreviate $\omega + \omega_{12} = \alpha$. Then,

$$i\hbar\dot{C}_1 = V e^{i\alpha t}\, C_2$$
$$i\hbar\dot{C}_2 = V e^{-i\alpha t}\, C_1$$

Differentiating the second equation and substituting $\dot{C}_1$ from the first yields

$$\ddot{C}_2 = -i\alpha\dot{C}_2 - \frac{V^2}{\hbar^2}C_2$$

which admits a solution of the form $C_2 = C_2(0)e^{i\Omega t}$

$$\Omega = -\frac{\alpha}{2}\pm\sqrt{\frac{\alpha^2}{4} + \frac{V^2}{\hbar^2}}$$

Hence, the final solution is

$$C_2(t) = e^{-i\frac{(\omega-\omega_{21})}{2}t}\left(A\, e^{i\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t} + B\, e^{-i\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t}\right)$$

With the initial state $C_1(0)=1;\ C_2(0)=0$ we find $A = -B$. To pin down its value, note that

$$\dot{C}_2(0) = \frac{V}{i\hbar}C_1(0) = \frac{V}{i\hbar}$$

$$\to |C_2(t)|^2 = \frac{V^2/\hbar^2}{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\sin^2\left(\sqrt{\left(\frac{\omega-\omega_{21}}{2}\right)^2 + \frac{V^2}{\hbar^2}}\, t\right)$$

Note that, in particular for $\omega = \omega_{21}$

$$|C_2(t)|^2 = \sin^2\left(\frac{Vt}{\hbar}\right)$$

So the system sloshes back and forth between $|1\rangle$ and $|2\rangle$ with period $\pi\hbar/2V$. This is the "resonance condition". Oscillations persist off resonance too, but once the freq. $\omega$ strays far from $2V/\hbar$ the transition probability becomes tiny.

*end lecture*

### Example: Spin magnetic resonance

Take a spin-$S=1/2$ particle in a B-field along $z$,

$$\hat{H}_0 = -\mu_B B_0\,\hat{\sigma}^z = -\frac{e}{m_e}B_0\,\hat{S}_z\ ;\quad \mu_B = \frac{e\hbar}{2m_e}$$

Now add a time-dependent B-field rotating in the $x$-$y$ plane,

$$\hat{V} = -\mu_B B_1\left(\cos\omega t\,\hat{\sigma}^x + \sin\omega t\,\hat{\sigma}^y\right)$$

The eigenstates of $\hat{H}_0$ are $|+\rangle$ and $|-\rangle$

$$\hat{H}_0|\pm\rangle = \mp\frac{e\hbar}{2m_e}B_0|\pm\rangle$$

The perturbation can be recast as

$$\hat{V} = \frac{eB_1}{2m_e}\left[e^{i\omega t}\sigma^- + e^{-i\omega t}S^+\right]$$

It follows that $\langle +|\hat{V}|+\rangle = \langle -|\hat{V}|-\rangle = 0$ and

$$\langle -|V|+\rangle = \langle +|V|-\rangle^* = \frac{e\hbar B_1}{2m_e}e^{i\omega t}$$

This maps directly onto the previous case, with $|1\rangle\to|+\rangle$, $|2\rangle\to|-\rangle$; $\omega_{21} = eB_0/m_e$, $V = e\hbar B_1/2m_e$

## 4.1 The sudden approximation

Consider a Hamiltonian that flips abruptly over a tiny time window

*(diagram: vertical dashed line with "before" on the left, "after" on the right, a small interval $\varepsilon$ marked at the transition, arrow labeled "time")*

As an example, suddenly widen a square potential well

*(diagram: a half-wave over the interval $[0,a]$, arrow to a half-wave over $[0,2a]$)*

As $\varepsilon\to 0$ the wave function is identical before and after; the system has no time to "react" to the switch. For the kicked oscillator with a gaussian pulse, taking the limit

*(diagram: gaussian pulse of width $2\tau$)*

$\tau\to 0$ makes the initial and final Hamiltonians coincide, so $P_{0\to 1} = 0$.

### Example: Beta decay

A Hydrogen atom carrying a 1s electron undergoes beta decay. A neutron in the nucleus turns into a proton, throwing off a relativistic electron and an antineutrino. The atom is left with charge $Z+1 = 2$. The 1s electron stays in the ground state belonging to nuclear charge $Z$ — which is no longer an eigenstate of the charge-$Z+1$ ion.

## 4.2 Energy shifts and decay widths

Switch on a perturbation gradually, starting at $t=-\infty$,

$$\hat{V}(t) = \exp(\gamma t)\,\hat{V}_0$$

with $\gamma$ small and positive and $\hat{V}_0$ time independent. Suppose that at $t\to-\infty$ the system sits in the initial state $|i\rangle\to C_i(t=-\infty)=1$, $C_{n\neq i}(t=-\infty)=0$. First-order t-d perturbation theory gives

$$C_n^{(0)}(t) = 0$$

$$C_n^{(1)}(t) = -\frac{i}{\hbar}V_{ni}\int_{-\infty}^t dt'\,\exp\left((\gamma + i\omega_{ni})t\right)$$

$$= -\frac{i}{\hbar}V_{ni}\,\frac{\exp\left((\gamma + i\omega_{ni})t\right)}{\gamma + i\omega_{ni}}$$

where $\omega_{ni} = \frac{1}{\hbar}(E_n - E_i)$ and $V_{ni} = \langle n|\hat{V}_0|i\rangle$

$$\to P_{n\to i} = |C_n^{(1)}|^2 = \frac{|V_{ni}|^2}{\hbar^2}\frac{e^{2\gamma t}}{\gamma^2 + \omega_{ni}^2}$$

The transition rate is

$$R_{i\to f} = \frac{dP_{i\to f}}{dt} = \frac{2|V_{ni}|^2}{\hbar^2}\frac{\gamma\, e^{2\gamma t}}{\gamma^2 + \omega_{ni}^2}$$

As $\gamma\to 0$ this reduces to a "sudden perturbation", since $e^{2\gamma t}\to 1$

$$\to \lim_{\gamma\to 0}\frac{\gamma}{\gamma^2 + \omega_n^2} = \pi\delta(\omega_{ni}) = \pi\hbar\,\delta(E_n - E_i)$$

$$\to R_{i\to f} = \frac{2\pi}{\hbar}|V_{ni}|^2\,\delta(E_n - E_i)$$

Now carry $C_i(t)$ to second order

$$C_i^{(0)}(t) = 1$$

$$C_i^{(1)}(t) = -\frac{i}{\hbar}V_{ii}\int_{-\infty}^t e^{\gamma t'}dt' = -\frac{i}{\hbar}V_{ii}\frac{e^{\gamma t}}{\gamma}$$

$$C_i^{(2)}(t) = \left(\frac{-i}{\hbar}\right)^2\sum_m |V_{mi}|^2\int_{-\infty}^t dt'\int_{-\infty}^{t'} dt''\, e^{(\gamma + i\omega_{im})t'}\, e^{(\gamma + i\omega_{mi})t''}$$

$$= \left(\frac{-i}{\hbar}\right)^2\sum_m |V_{mi}|^2\frac{e^{2\gamma t}}{2\gamma(\gamma + i\omega_{mi})}$$

Examine the ratio $\dot{C}_i/C_i$ as $\gamma\to 0$

$$\frac{\dot{C}_i}{C_i} \approx \left(\frac{-i}{\hbar}\right)V_{ii} + \lim_{\gamma\to 0}\left(\frac{-i}{\hbar}\right)\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m + i\hbar\gamma}$$

Notice the result carries no time dependence. Write it as

$$\frac{\dot{C}_i}{C_i} = \left(\frac{-i}{\hbar}\right)\Delta_i$$

where $\Delta_i = V_{ii} + \lim_{\gamma\to 0}\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m + i\hbar\gamma}$

Using the result $\lim_{\varepsilon\to 0}\frac{1}{x + i\varepsilon} = P\frac{1}{x} - i\pi\delta(x)$

where $\varepsilon>0$ and $P$ denotes the principal part.

$$\to \Delta_i = V_{ii} + P\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m} - i\pi\sum_{m\neq i}|V_{mi}|^2\delta(E_i - E_m)$$

Normalizing so that $C_i(0)=1$

$$C_i(t) = \exp\left(\frac{i\Delta_i}{\hbar}t\right)$$

$$\to |i,t\rangle = \exp\left(-i(\Delta_i + E_i)t/\hbar\right)|i\rangle$$

Notice that $\Delta_i$ is complex:

$$|i,t\rangle = \exp\left(-i(E_i + \mathrm{Re}\,\Delta_i)t/\hbar\right)\exp\left(\mathrm{Im}\,\Delta_i\, t/\hbar\right)|i\rangle$$

or

$$|i,t\rangle = \exp\left(-i(E_i + \Delta E_i)t/\hbar\right)\exp\left(-\frac{\Gamma_i t}{2\hbar}\right)|i\rangle$$

where

$$\Delta E_i = \mathrm{Re}\,\Delta_i = V_{ii} + P\sum_{m\neq i}\frac{|V_{mi}|^2}{E_i - E_m}$$

$$\frac{\Gamma_i}{\hbar} = -\frac{2}{\hbar}\mathrm{Im}(\Delta_i) = \frac{2\pi}{\hbar}\sum_{m\neq i}|V_{mi}|^2\delta(E_i - E_m)$$

The first term is an energy shift, matching the one from stationary perturbation theory. The second exponential controls whether the state grows or decays. The probability of still observing $|i\rangle$ is

$$P_{i\to i}(t) = |C_i|^2 = \exp\left(-\Gamma_i t/\hbar\right)$$

where $\frac{\Gamma_i}{\hbar} = \sum_{m\neq i}\omega_{i\to m}$

Probability is conserved through second order, since

$$|C_i|^2 + \sum_{m\neq i}|C_m|^2 \approx 1 - \frac{\Gamma_i t}{\hbar} + \sum_{m\neq i}\omega_{i\to m}t = 1$$

The quantity $\Gamma_i$ is the "decay width". The state's "lifetime" is

$$\tau_i = \hbar/\Gamma_i$$

and

$$P_{i\to i} = \exp(-t/\tau_i)$$

So the amplitude of $|i\rangle$ both oscillates and decays as time goes on.

Because the state changes in time, its energy cannot be sharp. The energy is smeared over a band of width $\Gamma_i$ centered on the shifted value $E_i + \mathrm{Re}\,\Delta_i$. The quicker the decay, the broader the spread.

In spectroscopy this shows up directly: weak lines are narrow, set by slow transitions, while strong lines are broad and smeared out, set by fast ones.

## 4.3 Harmonic perturbations

Take an oscillating potential. If the system starts in $|i\rangle$, what is the probability of finding it in $|f\rangle$ later on?

The initial condition gives $C_i = 1$; $C_j = 0$ for $j \neq i$.

Recall the differential eqs.

$$i\hbar\begin{pmatrix}\dot{C}_1\\\dot{C}_2\\\vdots\end{pmatrix} = \begin{pmatrix} V_{11} & V_{12}e^{i\omega_{12} t} & \cdots\\ V_{21}e^{i\omega_{21} t} & V_{22} & \\ \vdots & & V_{33}\end{pmatrix}\begin{pmatrix}C_1\\C_2\\\vdots\end{pmatrix}$$

To first order we substitute $C_i = 1$; $C_{j\neq i} = 0\ \ j\neq i$ on the right-hand side, which amounts to solving

$$i\hbar\dot{C}_f(t) = V_{fi}\, e^{i\omega_{fi} t}$$

Integrating gives

$$C_f(t) = -\frac{i}{\hbar}\int_0^t \langle f|V|i\rangle\, e^{i(\omega_{fi} - \omega)t'}dt'$$

$$= -\frac{i}{\hbar}\langle f|V|i\rangle\,\frac{e^{i(\omega_{fi} - \omega)t} - 1}{i(\omega_{fi} - \omega)}$$

The transition probability is

$$P_{i\to f}(t) = |C_f|^2 = \frac{|\langle f|V|i\rangle|^2}{\hbar^2}\frac{\sin^2((\omega_{fi} - \omega)t/2)}{\left(\frac{\omega_{fi} - \omega}{2}\right)^2}$$

The oscillating term has the form $\frac{\sin^2\alpha t}{\alpha^2}$

*(plot: a tall central peak of $\frac{\sin^2\alpha t}{\alpha^2}$ at $\alpha t = 0$, with smaller side lobes at $\pm\pi$, $\pm 2\pi$ along the $\alpha t$ axis)*

In the large $t$ limit

$$\lim_{t\to\infty}\frac{\sin^2\alpha t}{\alpha^2} = \pi\delta(\alpha)t$$

$\to$ The transition probability grows linearly in time, so we define a "transition rate"

$$R_{i\to f}(t) = \lim_{t\to\infty}\frac{dP_{i\to f}(t)}{dt} = \frac{\pi}{\hbar^2}|\langle f|V|i\rangle|^2\,\delta\left(\frac{\omega_{fi} - \omega}{2}\right)$$

$$= \frac{2\pi}{\hbar^2}|\langle f|V|i\rangle|^2\,\delta(\omega_{fi} - \omega)$$

"Fermi's Golden Rule"

How can the transition probability diverge? The catch is that "long time" here means $(\omega_{fi} - \omega)t \gg 1$, which can happen at a genuinely short clock time.

**Validity:** Rewrite $P_{i\to f} = \frac{|V_{fi}|^2}{\hbar^2}\frac{\sin^2(\alpha t)}{\alpha^2}$

with $\alpha = \frac{\omega_{fi} - \omega}{2}$

Multiplying and dividing by $t^2$,

$$P_{i\to f} = \frac{|V_{fi}|^2 t^2}{\hbar^2}\frac{\sin^2(\alpha t)}{\alpha^2 t^2} = \frac{|V_{fi}|^2 t^2}{\hbar^2}\eta(\alpha t)$$

with $\eta(x) = \frac{\sin^2 x}{x^2}\in[0,1]$

$$\to \text{we want}\quad \frac{|V_{fi}|^2 t^2}{\hbar^2}\ll 1,\quad\text{or}$$

$$\boxed{\,t \ll \frac{\hbar}{|V_{fi}|}\,}$$

On top of that, viewed as a function of $\alpha t$, the approximation holds when

$$\boxed{\,|t|\,|\omega_{fi}| > 2\pi\,}$$

Putting both together, we arrive at

$$\boxed{\,\frac{2\pi}{|\omega_{fi}|} \lesssim t \ll \frac{\hbar}{|V_{fi}|}\,}$$

## 4.4 The adiabatic theorem

Suppose the Hamiltonian drifts slowly from $H(t=0)$ to $H(t=T)$. The adiabatic theorem says that if the system begins in the $n^{th}$ eigenstate of $H(0)$, it ends in the $n^{th}$ eigenstate of $H(T)$. The proof requires a discrete, non-degenerate spectrum.

### Example: particle in an infinite well

*(diagram: at $t=0$, a half-wave over $[0,a]$; arrow to $t=T$, a half-wave over $[0,2a]$)*

Even though we demand the process be slow, energy is not conserved.

**Proof:** $\quad H\psi_n = E_n\psi_n$

For a time-independent Hamiltonian, the wave function merely acquires a phase

$$\psi_n(t) = e^{-iE_n t/\hbar}\psi_n(t=0)$$

Once the Hamiltonian varies in time, both eigenvalues and eigenfunctions become time dependent

$$H(t)\psi_n(t) = E_n(t)\psi_n(t)\quad\circledast$$

with $\langle\psi_n(t)|\psi_m(t)\rangle = \delta_{nm}$

The general solution of the Schrödinger eq. can be written

$$\psi(t) = \sum_n C_n(t)\psi_n(t)\, e^{i\theta_n(t)}$$

where

$$\theta_n(t) = -\frac{1}{\hbar}\int_0^t E_n(t')\, dt'$$

generalizes the phase factor to the time-dependent setting.

Substituting into the t-d Schrödinger eq. gives

$$i\hbar\sum_n\left(\dot{C}_n\psi_n + C_n\dot{\psi}_n - \frac{i}{\hbar}C_n\psi_n\dot{\theta}_n\right)e^{i\theta_n} = \sum_n C_n\hat{H}\psi_n e^{i\theta_n}$$

$$\underbrace{C_n\psi_n E_n}\qquad\qquad\underbrace{C_n E_n\psi_n}$$

$$\to \sum_n \dot{C}_n\psi_n e^{i\theta_n} = -\sum_n C_n\dot{\psi}_n e^{i\theta_n}$$

Taking the inner product with $\psi_m$ and invoking the orthogonality of the instantaneous wave functions:

$$\sum_n \dot{C}_n\delta_{mn}e^{i\theta_n} = -\sum_n C_n\langle m|\dot{n}\rangle e^{i\theta_n}$$

or

$$\dot{C}_m(t) = -\sum_n C_n\langle m|\dot{n}\rangle e^{i(\theta_n - \theta_m)}\quad\circledast$$

Differentiating $\circledast$ in time,

$$\dot{H}\psi_n + H\dot{\psi}_n = \dot{E}_n\psi_n + E_n\dot{\psi}_n$$

$$\overset{\langle\psi_m|}{\longrightarrow}\ \langle m|\dot{H}|n\rangle + \langle m|H|\dot{n}\rangle = \dot{E}_n\delta_{mn} + E_n\langle m|\dot{n}\rangle$$

$$\underbrace{E_m\langle m|\dot{n}\rangle}$$

$$\to \langle m|\dot{H}|n\rangle = (E_n - E_m)\langle m|\dot{n}\rangle$$

Inserting into $\circledast$

$$\dot{C}_m(t) = -C_n\langle m|\dot{m}\rangle - \sum_{n\neq m}C_n\frac{\langle m|\dot{H}|n\rangle}{E_n - E_m}e^{-\frac{i}{\hbar}\int_0^t(E_n(t') - E_m(t'))dt'}$$

This is exact. Now invoke the adiabatic assumption — $\dot{H}$ is very small — and drop the second term.

$$\dot{c}_m(t) = -c_m \langle m | \dot{m} \rangle$$

$$\rightarrow c_m(t) = c_m(0)\, e^{i\gamma_m(t)}$$

where

$$\gamma_m(t) = i \int_0^t \left\langle \psi_m(t') \,\Big|\, \frac{\partial}{\partial t'} \psi_m(t') \right\rangle dt'$$

In particular, if the system starts out in the $n^{\text{th}}$ eigenstate, $c_n(0)=1$, $c_m(0)=0$ for $n \neq m$,

$$\psi(t) = e^{i\theta_n(t)}\, e^{i\gamma_n(t)}\, \psi_n(t)$$

so it stays in the $n^{\text{th}}$ eigenstate of the evolving Hamiltonian, apart from phase factors.

## 4.5 Berry's phase

In that last expression, $\theta_n(t)$ is the "dynamic phase" and $\gamma_n(t)$ is the "geometric phase". Suppose the time-dependence enters through a single time-varying parameter in the Hamiltonian, $R(t)$.

$$\frac{\partial \psi_n}{\partial t} = \frac{\partial \psi_n}{\partial R} \cdot \frac{dR}{dt}$$

$$\rightarrow \gamma_n(t) = i \int_0^t \left\langle \psi_n \Big| \frac{\partial \psi_n}{\partial R} \right\rangle \frac{dR}{dt'}\, dt' = i \int_{R_i}^{R_f} \left\langle \psi_n \Big| \frac{\partial \psi_n}{\partial R} \right\rangle dR$$

where $R_i$ and $R_f$ are the starting and ending values of $R(t)$. In particular, if the system comes back to its original configuration after $t = T$

$$\rightarrow R_i = R_f \rightarrow \gamma_n(T) = 0$$

But now let several parameters vary together in time.

$$\frac{\partial \psi_n}{\partial t} = \frac{\partial \psi_n}{\partial R_1}\frac{dR_1}{dt} + \cdots + \frac{\partial \psi_n}{\partial R_N}\frac{dR_N}{dt} = (\vec{\nabla}_R \psi_n) \cdot \frac{d\vec{R}}{dt}$$

where $\vec{R} = (R_1, \ldots R_N)$; $\vec{\nabla}_R = \left(\frac{\partial}{\partial R_1}, \ldots \frac{\partial}{\partial R_N}\right)$.

Now we have

$$\gamma_n(t) = i \int_{R_i}^{R_f} \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \cdot d\vec{R}$$

if $\vec{R}_i = \vec{R}_f$, this becomes

$$\gamma_n(T) = i \oint \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \cdot d\vec{R} \qquad \text{``Berry's phase''}$$

a loop integral in parameter space that, in general, does not vanish.

Notice that $\gamma_n$ depends on the path traced through parameter space, whereas $\theta_n$ depends only on the elapsed time.

**Example:** A beam of particles in state $\psi_0$ is split in two, with one arm sent through a slowly varying potential. Once the beams recombine, the total wave function reads

$$\psi = \tfrac{1}{2}\psi_0 + \tfrac{1}{2}\psi_0 e^{i\Gamma}$$

where the geometric and dynamic phases are included in $\Gamma$

$$|\psi|^2 = \tfrac{1}{4}|\psi_0|^2 \left(1 + e^{i\Gamma}\right)\left(1 + e^{-i\Gamma}\right)$$

$$= \tfrac{1}{2}|\psi_0|^2 (1 + \cos\Gamma) = |\psi_0|^2 \cos^2(\Gamma/2)$$

So $\Gamma$ is read off directly from the interference pattern.

When parameter space is 3-dimensional, $\vec{R} = (R_1, R_2, R_3)$, Berry's formula mirrors the expression for magnetic flux in terms of the vector potential $\vec{A}$.

$$\Phi = \int_S \vec{B} \cdot d\vec{a} = \int_S (\vec{\nabla} \times \vec{A}) \cdot da = \oint \vec{A} \cdot d\vec{r}$$

*(diagram: a closed loop $C$ enclosing a surface with area element $d\vec{a}$)*

The Berry's phase can be thought of as the "flux" of a "magnetic field"

$$\vec{\Omega}_R \equiv \vec{B} = i\, \vec{\nabla}_R \times \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \qquad \text{(Berry curvature)}$$

through the closed-loop trajectory in parameter space. Equivalently, Berry's phase becomes a surface integral

$$\gamma_n(T) = i \int \left( \vec{\nabla}_R \times \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \right) \cdot d\vec{a}$$

The equivalent "vector potential"

$$\vec{A} = \langle \psi_n | \vec{\nabla}_R \psi_n \rangle \qquad \text{(Berry connection)}$$

is called "Berry connection".

**Example:** two-level system. Spin in a magnetic field.

Take a spin-$\tfrac{1}{2}$ in a magnetic field pointing in an arbitrary direction relative to the $z$-axis.

$$H = \mu \vec{J} \cdot \vec{B}$$

The eigenenergies are $\pm \mu B$ and the eigenvectors are

$$|-\rangle = \sin\tfrac{\theta}{2} e^{-i\varphi} |1\rangle - \cos\tfrac{\theta}{2}|2\rangle$$

$$|+\rangle = \cos\tfrac{\theta}{2} e^{-i\varphi}|1\rangle + \sin\tfrac{\theta}{2}|2\rangle$$

Focus on the $|-\rangle$ state.

$$A_\theta = \langle - | i\tfrac{\partial}{\partial\theta} | - \rangle = 0 \quad;\quad A_\varphi = \langle - | i\tfrac{\partial}{\partial\varphi} | - \rangle = \sin^2\tfrac{\theta}{2}$$

The Berry curvature is

$$\Omega_{\theta\varphi} = \frac{\partial}{\partial\theta}A_\varphi - \frac{\partial}{\partial\varphi}A_\theta = \tfrac{1}{2}\sin\theta$$


---

## References and Further Reading

*Editorial addition mapping the notes to their source text. The two-level system is cited in the text as Townsend Example 4.2.*

**Primary source.** Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed.: Ch. 14 (Photons and Atoms) for time-dependent perturbation theory and Fermi's golden rule; Ch. 4 (Time Evolution) for two-level dynamics (Example 4.2).

**Further reading.** Sakurai & Napolitano, the "Approximation Methods" chapter (time-dependent perturbation theory, the sudden and adiabatic approximations, Berry's phase); Griffiths & Schroeter, the "Time-Dependent Perturbation Theory" and "The Adiabatic Approximation" chapters; Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XIII.
