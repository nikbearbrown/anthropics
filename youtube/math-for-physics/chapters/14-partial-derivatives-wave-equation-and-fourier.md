# Partial Derivatives, the Wave Equation, and Fourier Analysis

*Two variables, one partial differential equation, and the idea that any sound is a sum of pure tones*

## A bump that travels 800 kilometers an hour while the water barely moves

On December 26, 2004, the seafloor west of Sumatra ruptured and shoved a column of ocean upward. The disturbance spread across the Indian Ocean at roughly 800 kilometers an hour in deep water — and yet the water itself did not travel across the ocean. Each parcel of water rose and fell by a few meters and stayed put. Something traveled at the speed of a jet airliner while the medium scarcely moved. What, exactly, was moving?

A guitar string poses the same puzzle in miniature. Pluck it and a shape runs down to the bridge, reflects, and runs back; the string's material goes nowhere, but a *pattern* races along it. And listen to that string: it does not produce a pure tone but a rich one, a fundamental pitch layered with overtones that let you tell a guitar from a violin playing the same note. Somehow a single vibrating string carries many frequencies at once.

To describe any of this we hit a wall the earlier chapters did not prepare us for. The displacement of the string is not a function of one variable but of *two*: it depends on **where** you are along the string ($x$) and **when** you look ($t$). Write it $y(x, t)$. A snapshot at fixed time is a curve in $x$; a movie of one point is a curve in $t$. Asking "how is $y$ changing" is now ambiguous — changing as you move along the string, or as time passes? We need a calculus of functions of several variables, an equation that couples the two kinds of change, and a way to decompose the resulting rich vibration into pure tones. That is **partial derivatives**, the **wave equation**, and **Fourier series** — the three tools of this capstone chapter, with **logarithms** (the decibel) as a closing coda. The tsunami and the guitar string are the doorways.

## The tool, named

A **function of several variables** assigns an output to each combination of inputs; $y(x,t)$ is the standard example. A **partial derivative** is the derivative with respect to *one* variable while *holding the others fixed*, written with a curly $\partial$ instead of the straight $d$:

$$\frac{\partial y}{\partial x} = \text{rate of change of } y \text{ with } x, \text{ with } t \text{ held fixed}; \qquad
\frac{\partial y}{\partial t} = \text{rate of change of } y \text{ with } t, \text{ with } x \text{ held fixed}.$$

A **partial differential equation** (PDE) relates a multivariable function to its partial derivatives. The star of the chapter is the **one-dimensional wave equation**

$$\frac{\partial^2 y}{\partial t^2} = v^2\,\frac{\partial^2 y}{\partial x^2},$$

which we will derive from Newton's second law on a string. The chapter then shows two things its linearity buys: **superposition** (sums of solutions are solutions, hence standing waves and interference) and **Fourier series** (any periodic signal is a sum of pure sinusoids). It ends with the **decibel**, a logarithm that rescales a trillion-fold range of loudness into a human 0-to-120.

The interpretive judgment this chapter demands — which no solver supplies — is connecting the two-variable mathematics to physical meaning: that $\partial y/\partial t$ is the *velocity* of a point on the string while $\partial y/\partial x$ is the *slope* of its snapshot, that a wave is a *solution shape* and not a substance, and that deciding how many Fourier harmonics are "enough" to capture a real tone is a modeling call.

## Development

### Partial derivatives: two questions, two answers

Take the sinusoidal wave $y(x, t) = A\sin(kx - \omega t)$, where $k = 2\pi/\lambda$ is the wave number and $\omega = 2\pi f$ the angular frequency. There are two distinct rates of change, and the curly $\partial$ keeps them apart.

Holding $t$ fixed and differentiating in $x$ gives the **slope** of the string's snapshot:

$$\frac{\partial y}{\partial x} = Ak\cos(kx - \omega t).$$

Holding $x$ fixed and differentiating in $t$ gives the **transverse velocity** of a single point on the string:

$$\frac{\partial y}{\partial t} = -A\omega\cos(kx - \omega t).$$

These are physically different things — a slope (dimensionless) and a velocity (meters per second) — and the most common error in all of multivariable calculus is to forget that the *other* variable is being held fixed, treating $\partial/\partial x$ as though $t$ were not there. It is there; it is just frozen. Differentiate again to get the two second partials we will need, the **curvature** and the **transverse acceleration**:

$$\frac{\partial^2 y}{\partial x^2} = -Ak^2\sin(kx - \omega t), \qquad \frac{\partial^2 y}{\partial t^2} = -A\omega^2\sin(kx - \omega t).$$

### Deriving the wave equation from a string element

The wave equation is not handed down; it falls out of Newton's second law applied to a tiny piece of string. Consider a short element of string between $x$ and $x + \Delta x$, with mass $\Delta m = \mu\,\Delta x$ where $\mu$ is the mass per unit length. The string is under tension $F_T$, pulling tangentially at each end of the element. When the string is curved, the two end-tensions do not quite cancel, and their small vertical mismatch is the net transverse force.

If the slope is small, the vertical component of tension at a point is approximately $F_T\,(\partial y/\partial x)$. The net upward force on the element is the difference of this quantity at the two ends:

$$F_{\text{net}} \approx F_T\left[\left(\frac{\partial y}{\partial x}\right)_{x + \Delta x} - \left(\frac{\partial y}{\partial x}\right)_{x}\right].$$

The bracket is the change in slope across the element — which, divided by $\Delta x$, *is* the second spatial derivative (the definition of a derivative). So

$$F_{\text{net}} \approx F_T\,\frac{\partial^2 y}{\partial x^2}\,\Delta x.$$

Now apply $F = ma$ to the element. Its mass is $\mu\,\Delta x$ and its transverse acceleration is $\partial^2 y/\partial t^2$:

$$\mu\,\Delta x\,\frac{\partial^2 y}{\partial t^2} = F_T\,\frac{\partial^2 y}{\partial x^2}\,\Delta x.$$

The $\Delta x$ cancels, and rearranging gives the **wave equation**:

$$\boxed{\frac{\partial^2 y}{\partial t^2} = \frac{F_T}{\mu}\,\frac{\partial^2 y}{\partial x^2} = v^2\,\frac{\partial^2 y}{\partial x^2}, \qquad v = \sqrt{\frac{F_T}{\mu}}.}$$

Read it physically: the **curvature** of the string ($\partial^2 y/\partial x^2$) drives the **transverse acceleration** ($\partial^2 y/\partial t^2$). Where the string is sharply bent, the tension mismatch is large, so the acceleration is large — the string snaps back hardest where it is most curved. This is why we needed two variables at all: the physics couples a derivative in space to a derivative in time, and no single-variable calculus can express that coupling. The wave speed $v = \sqrt{F_T/\mu}$ emerges as a property of the medium — tighter string (more $F_T$) or lighter string (less $\mu$) means faster waves.

### The traveling-wave solution

d'Alembert showed in 1747 that the wave equation has a general solution of remarkable simplicity [verify]:

$$y(x, t) = f(x - vt) + g(x + vt),$$

where $f$ and $g$ are *any* (twice-differentiable) functions. The first term is a fixed shape sliding to the right at speed $v$; the second is any shape sliding left. To see that $f(x - vt)$ solves the equation, let $u = x - vt$ and use the chain rule: $\partial y/\partial x = f'(u)$ and $\partial y/\partial t = -v f'(u)$, so $\partial^2 y/\partial x^2 = f''(u)$ and $\partial^2 y/\partial t^2 = v^2 f''(u)$. Substituting, $v^2 f'' = v^2 f''$. ✓ It works for *any* $f$ — which is precisely the point that touched off a famous quarrel. Euler insisted $f$ could be any shape at all, even the sharp corner of a plucked string; d'Alembert wanted it restricted to smooth formulas. Settling what counts as a legitimate "function" was a *consequence* of the wave equation, not a prerequisite [verify]. The sinusoidal wave $A\sin(kx - \omega t)$ we differentiated above is just the special periodic case, with $\omega = vk$.

### Superposition and standing waves

Because the wave equation is **linear** — every term is first-degree in $y$ and its derivatives — if $y_1$ and $y_2$ each solve it, so does $y_1 + y_2$. The derivative is a linear operator: $\partial^2(y_1 + y_2)/\partial x^2 = \partial^2 y_1/\partial x^2 + \partial^2 y_2/\partial x^2$, and likewise in $t$, so the sum satisfies the same equation. This is **superposition**, the same property that made the harmonic oscillator tractable in Chapter 11, now operating on waves. It is why two ripples pass through each other undisturbed, and why a forward and a backward wave can combine into a standing pattern.

Add a right-mover and an equal left-mover:

$$y = A\sin(kx - \omega t) + A\sin(kx + \omega t).$$

Using the identity $\sin(\alpha - \beta) + \sin(\alpha + \beta) = 2\sin\alpha\cos\beta$ with $\alpha = kx$, $\beta = \omega t$:

$$y(x, t) = 2A\sin(kx)\cos(\omega t).$$

The space and time parts have *separated*. Every point oscillates in time as $\cos\omega t$, but its amplitude is $2A\sin(kx)$, fixed by position. Where $\sin(kx) = 0$ the string never moves — these are **nodes**; where $|\sin kx| = 1$ it swings maximally — **antinodes**. This is a **standing wave**. Pinning both ends of a string of length $L$ (nodes at $x = 0$ and $x = L$) forces $\sin(kL) = 0$, hence $kL = n\pi$, giving the allowed wavelengths $\lambda_n = 2L/n$ and frequencies

$$f_n = \frac{nv}{2L}, \qquad n = 1, 2, 3, \dots$$

The lowest, $f_1 = v/2L$, is the **fundamental**; the rest are its integer **harmonics**. A guitar string sounds a definite pitch because only these special frequencies survive on it. And the fact that the harmonics are exact integer multiples of the fundamental is the seed of the chapter's last big idea.

![Three stacked panels showing the first three standing-wave modes of a string fixed at both ends: one arch, two arches, three arches, with interior nodes marked.](images/14-partial-derivatives-wave-equation-and-fourier-fig-01.png)
*Figure 14.1 — Standing-wave modes of a fixed string. Nodes are forced at the ends, so only λₙ = 2L/n fit; mode n has n−1 interior nodes and frequency fₙ = nv/2L, an integer multiple of the fundamental.*

### Fourier series: any periodic signal is a sum of sines

A real plucked string does not vibrate in a single mode. It vibrates in *many* harmonics at once, in proportions set by how and where it was plucked, and that mixture is what gives the note its timbre. Daniel Bernoulli conjectured in 1753 that *every* possible vibration of the string is a superposition of the harmonic modes — a sum of sinusoids at the fundamental and its integer multiples [verify]. Euler did not believe an arbitrary shape could be built from smooth sines. Bernoulli was essentially right, and Joseph Fourier proved the general claim in 1822 (after Lagrange had blocked his earlier 1807 memoir) [verify; contested — see pantry]:

> Any periodic function — even one with corners or jumps — can be written as a sum of sines and cosines whose frequencies are integer multiples of the fundamental.

For a function $y(t)$ of period $T$ (fundamental angular frequency $\omega_0 = 2\pi/T$), the **Fourier series** is

$$y(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\big[a_n\cos(n\omega_0 t) + b_n\sin(n\omega_0 t)\big].$$

The constant $a_0/2$ is the average; each $n$ contributes a pure tone at frequency $n\omega_0$ with amplitude set by the coefficients $a_n, b_n$. (Those coefficients are computed by integrals — the integral picks out "how much" of each frequency is present — which we state rather than belabor; the integral machinery is Chapters 8 and 9, and the general non-periodic version, the **Fourier transform**, is **Volume 2**.) The crucial idea for now is qualitative and constructive: *you build a complicated periodic waveform by adding pure sinusoids.* This is the exact analogue of Chapter 13's Taylor series — there you approximated a function by adding powers of $x$; here you approximate it by adding sines of increasing frequency.

Concretely, a square wave of period $T$ is the sum

$$y(t) = \frac{4}{\pi}\left[\sin\omega_0 t + \frac{1}{3}\sin 3\omega_0 t + \frac{1}{5}\sin 5\omega_0 t + \cdots\right],$$

odd harmonics with amplitudes falling off as $1/n$. Add just the first term and you get a lone sine; add the third harmonic and the top flattens; add the fifth, seventh, and the shape squares up, the corners sharpening with each term (a small persistent overshoot at the jump, the Gibbs phenomenon, is the one place the smooth sines protest a sharp corner — Euler's old doubt, made quantitative). This is *why a clarinet and a violin sound different* on the same pitch: same fundamental frequency, different recipe of harmonic amplitudes.

![A dashed square wave with three Fourier partial sums overlaid: one sine term, two terms beginning to flatten, three terms squaring up the corners.](images/14-partial-derivatives-wave-equation-and-fourier-fig-02.png)
*Figure 14.2 — A square wave built from summed Fourier sine terms. Each added odd harmonic squares up the shape; a small persistent overshoot at the jumps is the Gibbs phenomenon.*

### Coda: the decibel as a logarithm

A last tool, smaller but indispensable, and a clean example of a logarithm doing real work. The human ear responds to sound intensities from about $10^{-12}$ W/m² (barely audible) up to about $1$ W/m² (painful) — a range of a trillion to one. Writing those numbers linearly is hopeless. A logarithm compresses them. The **sound intensity level** in **decibels** is defined as

$$\beta = 10\log_{10}\!\left(\frac{I}{I_0}\right), \qquad I_0 = 10^{-12}\ \text{W/m}^2.$$

The logarithm turns the trillion-fold range into a comfortable 0 to 120. Its defining identity $\log(ab) = \log a + \log b$ gives the scale its useful behavior: *multiplying* the intensity by 10 *adds* 10 dB; doubling the intensity adds $10\log_{10}2 \approx 3$ dB (the "+3 dB" rule sound engineers use without thinking). The logarithm was not chosen for tidiness alone — the ear's own response is roughly logarithmic (the Weber–Fechner law), so the decibel scale matches perception. A worked instance: a pressure amplitude of $0.656$ Pa corresponds to an intensity of about $5.04\times10^{-4}$ W/m², so

$$\beta = 10\log_{10}\!\left(\frac{5.04\times10^{-4}}{10^{-12}}\right) = 10\log_{10}(5.04\times10^{8}) \approx 10(8.70) = 87\ \text{dB}.$$

A logarithm has translated a microscopic air-pressure wiggle into the number a sound meter reports.

## Worked examples

### Example 1 — Reading a wave function with partial derivatives

A wave on a string is $y(x,t) = (0.20\ \text{m})\sin\big[(6.28\ \text{m}^{-1})x - (1.57\ \text{s}^{-1})t\big]$. From the coefficients, $k = 6.28$ m$^{-1}$ so $\lambda = 2\pi/k = 1.0$ m, and $\omega = 1.57$ s$^{-1}$ so $T = 2\pi/\omega = 4.0$ s; the wave speed is $v = \omega/k = 0.25$ m/s. The two partial derivatives tell different physical stories. At the origin at $t = 0$: the slope is $\partial y/\partial x = (0.20)(6.28)\cos(0) = 1.26$ (dimensionless, a steep snapshot), while the transverse velocity of that point is $\partial y/\partial t = -(0.20)(1.57)\cos(0) = -0.31$ m/s (the point is moving downward). Same wave, same instant, two unrelated rates — that is what the curly $\partial$ is for.

### Example 2 — Harmonics of a guitar string

A guitar string of length $L = 0.65$ m, linear density $\mu = 3.09\times10^{-4}$ kg/m, under tension $F_T = 56.4$ N. The wave speed is

$$v = \sqrt{\frac{F_T}{\mu}} = \sqrt{\frac{56.4}{3.09\times10^{-4}}} \approx 427\ \text{m/s}.$$

The fundamental is $f_1 = v/2L = 427/1.30 \approx 329$ Hz — the note E4. The harmonics follow as integer multiples: $f_2 \approx 658$ Hz, $f_3 \approx 987$ Hz, and so on. When you pluck the open string all of these are excited at once; their *relative amplitudes* are the string's Fourier recipe, and that recipe is the timbre. Pluck near the center and you favor the odd harmonics; pluck near the bridge and the higher harmonics strengthen, brightening the tone — a Fourier fact every guitarist exploits by ear.

### Example 3 — Building a tone from harmonics, and a decibel

Suppose a tone is dominated by its first three odd harmonics in square-wave proportions, $\sin\omega_0 t + \tfrac13\sin3\omega_0 t + \tfrac15\sin5\omega_0 t$. Adding the fundamental alone gives a smooth sine; adding the third harmonic dimples the peaks toward a plateau; adding the fifth begins to square the corners. Three sinusoids already approximate a square wave recognizably — synthesis in action, the audible analogue of a Taylor partial sum hugging a curve. Now suppose this tone is played at two loudness levels differing by a factor of 100 in intensity. The decibel difference is $\Delta\beta = 10\log_{10}(100) = 20$ dB — a hundredfold change in physical intensity registering as a 20 dB step, which the ear hears as roughly "four times as loud." The logarithm is doing exactly its job: compressing a wide multiplicative range into a narrow additive one that matches perception.

## Back to the tsunami and the string

We began puzzled that a disturbance can cross an ocean at 800 km/h while the water barely moves, and that a single string can sound many frequencies at once. The wave equation answers the first puzzle: a wave is *not* a substance in transit but a **solution shape** — $f(x - vt)$ — that the medium passes along by exerting forces between neighboring parts. The water never travels; only the pattern does, at a speed $v$ fixed by the medium's stiffness and inertia ($\sqrt{F_T/\mu}$ for a string, $\sqrt{gh}$ for shallow-water gravity waves, which correctly gives the tsunami's deep-ocean speed and its slowing toward shore). The math is the wave; the wave is a solution of a partial differential equation in two variables, and we needed partial derivatives precisely because the physics couples curvature in space to acceleration in time.

Fourier answers the second puzzle: the string's rich tone is a *sum* of its harmonic standing waves, and the proportions of that sum — the Fourier coefficients — are what distinguish a guitar from a violin. Superposition, which is just the linearity of the wave equation, is what permits both the standing waves and their summation. And the decibel coda makes the quieter point that even loudness is a mathematical choice: a logarithm picked to fold a trillion-fold range into a perceptual scale. A wave is a PDE solution; a timbre is a Fourier spectrum; a loudness is a log ratio. The physics, all the way down, is the mathematics.

## Where it generalizes

The wave equation is one of the most universal equations in physics. The same $\partial^2/\partial t^2 = v^2\,\partial^2/\partial x^2$ — extended to two and three space dimensions with the **Laplacian** — governs sound in air, light and all electromagnetic radiation (with $v = c$), seismic waves through rock, ripples on a drumhead, and, in its quantum form (the Schrödinger equation), the wavefunctions of matter itself. Standing waves in reflecting cavities are the principle behind lasers and microwave ovens; the allowed-frequency condition $f_n = nv/2L$ becomes the quantized energy levels of an electron in an atom. Fourier analysis is even broader: it is the mathematical heart of audio compression (MP3 keeps the audible harmonics, discards the rest), image formats (JPEG), spectroscopy, signal processing, and the analysis of any periodic or quasi-periodic data, from heartbeats to climate cycles. Logarithmic scales like the decibel recur as the Richter scale, stellar magnitudes, and pH.

Three layers of this chapter point explicitly forward to **Volume 2**: the full multivariable and vector calculus (gradient, divergence, curl, and the Laplacian in three dimensions); the continuous **Fourier transform** that generalizes Fourier *series* from periodic signals to arbitrary ones; and the deeper PDE theory (heat, Laplace, and Schrödinger equations) of which the wave equation is one member. Here we have built the essential foundations: a function can depend on two variables, a partial derivative isolates one of them, a wave is a solution of a PDE that couples them, superposition is linearity, and any periodic signal is a sum of pure tones.

What a computer cannot supply is the two-variable modeling judgment. A machine evaluates $\partial^2 y/\partial t^2$ and computes Fourier coefficients flawlessly, but it cannot decide that $y$ depends on both $x$ and $t$ and that the physics couples curvature to acceleration; cannot recognize that "a plucked string" sets an initial *shape* $f(x)$ (d'Alembert's arbitrary function, the very thing Euler and d'Alembert fought over); cannot judge how many harmonics are enough to capture a real instrument; and cannot know that a decibel is a logarithm chosen to match the ear. The eighteenth-century quarrel over what counts as a function is the historical proof that this conceptual work — not the computation — is the hard and human part.

## Exercises

1. **Partial derivatives, two meanings.** For $y(x,t) = 0.05\sin(2x - 8t)$ (SI units), compute $\partial y/\partial x$ and $\partial y/\partial t$ as functions of $x$ and $t$. Evaluate both at $x = 0,\ t = 0$, and state in words what each number physically represents (slope vs. transverse velocity). Find the wave speed.

2. **Standing-wave frequencies.** A string fixed at both ends has length $0.80$ m and wave speed $240$ m/s. Find the first three standing-wave (harmonic) frequencies. Sketch the string's shape for each, marking the nodes and antinodes.

3. **Derive the wave equation (derivation).** Reproduce the derivation of $\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2$ from Newton's second law on a string element of mass $\mu\,\Delta x$ under tension $F_T$. State clearly where the small-slope approximation enters and identify $v = \sqrt{F_T/\mu}$.

4. **A traveling-wave check.** Show, using the chain rule with $u = x + vt$, that $g(x + vt)$ satisfies the wave equation for any twice-differentiable $g$. Then explain what kind of wave (left- or right-moving) this term represents and why.

5. **Decibels (log practice).** (a) A sound of intensity $10^{-6}$ W/m² — find its level in dB. (b) Two identical machines each produce 80 dB; what is the combined level when both run? (c) Explain, using $\log(ab) = \log a + \log b$, why the answer to (b) is not 160 dB.

## Sources

- Jean le Rond d'Alembert, "Recherches sur la courbe que forme une corde tendue mise en vibration" (1747; Berlin Academy *Mémoires*, 1749) — the wave equation and its traveling-wave solution $f(x-vt)+g(x+vt)$. [verify]
- Leonhard Euler (1748–1755) — the dispute over "arbitrary functions" in the string's solution. [verify]
- Daniel Bernoulli, "Réflexions et éclaircissements sur les nouvelles vibrations des cordes" (1753) — every string motion as a superposition of harmonics. [verify]
- Joseph Fourier, *Théorie analytique de la chaleur* (1822; earlier 1807 memoir blocked by Lagrange) — any periodic function as a sum of sines and cosines. [verify; contested — see pantry]
- Source physics: *Waves* (string-element derivation of the wave equation, standing waves, superposition) and *Sound* (decibel $\beta = 10\log_{10}(I/I_0)$, Weber–Fechner basis, the 0.656 Pa → 87 dB example), retained physics chapters 18 and 19. Back-references to Chapters 11 and 13 of this book.
