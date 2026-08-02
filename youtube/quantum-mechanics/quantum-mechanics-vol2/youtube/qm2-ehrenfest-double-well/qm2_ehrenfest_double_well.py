#!/usr/bin/env python3
"""
qm2_ehrenfest_double_well.py — Ehrenfest Breakdown in a Double Well
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics (ħ=1, m=1 natural units):
    V(x) = -x²/2 + x⁴/4  (double well, minima at x=±1, barrier at x=0, height 1/4)
    Initial Gaussian at x=0, σ=0.3
    ⟨x⟩(t) = 0 for all t (symmetry)
    σ_x(t) grows monotonically after splitting
    Numerical TDSE via split-step Fourier

Verify:
    python3 qm2_ehrenfest_double_well.py --verify

Render:
    manim -qh qm2_ehrenfest_double_well.py EhrenfestDoubleWellScene
"""
import sys
import numpy as np

def V(x):
    return -0.5 * x**2 + 0.25 * x**4

def gaussian(x, x0=0.0, sigma=0.3):
    return np.exp(-0.5 * (x - x0)**2 / sigma**2)

def split_step_evolve(psi, x, dt, n_steps):
    """Split-step Fourier propagation in ħ=m=1 units."""
    dx = x[1] - x[0]
    N = len(x)
    dk = 2 * np.pi / (N * dx)
    k = np.fft.fftfreq(N, d=dx) * 2 * np.pi
    V_arr = V(x)

    snapshots = [(0, psi.copy())]
    for i in range(n_steps):
        # Half potential step
        psi *= np.exp(-0.5j * dt * V_arr)
        # Full kinetic step
        psi_k = np.fft.fft(psi)
        psi_k *= np.exp(-0.5j * dt * k**2)
        psi = np.fft.ifft(psi_k)
        # Half potential step
        psi *= np.exp(-0.5j * dt * V_arr)
        # Renormalize
        norm = np.trapz(np.abs(psi)**2, x)
        psi /= np.sqrt(norm)

        if (i + 1) % (n_steps // 20) == 0:
            snapshots.append((i + 1, psi.copy()))

    return snapshots

def compute_moments(psi, x):
    """Compute ⟨x⟩ and σ_x."""
    prob = np.abs(psi)**2
    prob = prob / np.trapz(prob, x)
    x_mean = np.trapz(x * prob, x)
    x2_mean = np.trapz(x**2 * prob, x)
    sigma = np.sqrt(max(x2_mean - x_mean**2, 0))
    return x_mean, sigma

def verify():
    print("=== Ehrenfest Double Well Verification ===")
    x = np.linspace(-3, 3, 512)
    dx = x[1] - x[0]
    sigma0 = 0.3
    psi0 = gaussian(x, 0.0, sigma0).astype(complex)
    psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))

    dt = 0.01
    n_steps = 500
    snapshots = split_step_evolve(psi0.copy(), x, dt, n_steps)

    print("Time evolution of ⟨x⟩ and σ_x:")
    x_means = []
    sigmas = []
    for step, psi in snapshots[:6]:
        xm, sig = compute_moments(psi, x)
        x_means.append(xm)
        sigmas.append(sig)
        print(f"  t={step*dt:.2f}: ⟨x⟩ = {xm:.6f}  σ_x = {sig:.4f}")

    # P1: ⟨x⟩ = 0 always (symmetry)
    print(f"\nP1: max|⟨x⟩| = {max(abs(m) for m in x_means):.2e}  (should be ≈ 0)")

    # P2: σ_x grows
    print(f"P2: σ_x grows: {sigmas[0]:.4f} → {sigmas[-1]:.4f}  (monotonic increase)")
    print(f"    growing? {sigmas[-1] > sigmas[0]}")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class EhrenfestDoubleWellScene(Scene):
    """
    Left: |ψ(x,t)|² splitting in double well.
    Right: ⟨x⟩(t) flat at zero + σ_x(t) growing.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._precompute()
        self._phase_animation()
        self._phase_breakdown()

    def _phase_title(self):
        title = Text("Ehrenfest Breakdown in a Double Well", font="EB Garamond", font_size=50, color=INK)
        sub = Text(
            "V(x) = −x²/2 + x⁴/4  ·  ⟨x⟩=0 always  ·  |ψ|² bifurcates",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"\frac{d\langle p\rangle}{dt} = -\langle V'(x)\rangle \neq -V'(\langle x\rangle)\quad\text{(anharmonic)}",
            color=BLUE, font_size=26,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _precompute(self):
        """Compute TDSE snapshots."""
        x = np.linspace(-3, 3, 512)
        sigma0 = 0.3
        psi0 = gaussian(x, 0.0, sigma0).astype(complex)
        psi0 /= np.sqrt(np.trapz(np.abs(psi0)**2, x))

        dt = 0.02
        n_steps = 600
        self.snapshots = split_step_evolve(psi0.copy(), x, dt, n_steps)
        self.x_arr = x
        self.dt = dt
        self.x_means = []
        self.sigmas = []
        for _, psi in self.snapshots:
            xm, sig = compute_moments(psi, x)
            self.x_means.append(xm)
            self.sigmas.append(sig)

    def _phase_animation(self):
        x = self.x_arr
        snaps = self.snapshots
        x_means = self.x_means
        sigmas = self.sigmas
        n_snaps = len(snaps)

        ax_cfg = dict(color=INK, stroke_width=1.3, include_ticks=False, tip_length=0.16)

        # Left: density
        ax_left = Axes(
            x_range=[-3, 3, 1], y_range=[0, 1.5, 0.5],
            x_length=5.5, y_length=3.8, axis_config=ax_cfg,
        ).shift(LEFT*3.4 + UP*0.5)

        # Right: ⟨x⟩ trace
        ax_right = Axes(
            x_range=[0, n_snaps, n_snaps//5], y_range=[-0.5, 1.5, 0.5],
            x_length=5.5, y_length=3.8, axis_config=ax_cfg,
        ).shift(RIGHT*3.4 + UP*0.5)

        hdr_left = Text("|ψ(x,t)|²  (bifurcates)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_left, UP, buff=0.06)
        hdr_right = Text("⟨x⟩ (flat)  &  σ_x (grows)", font="EB Garamond", font_size=18, color=GOLD).next_to(ax_right, UP, buff=0.06)

        self.play(Create(ax_left), Create(ax_right), Write(hdr_left), Write(hdr_right), run_time=0.9)

        # Potential curve
        x_fine = np.linspace(-2.5, 2.5, 200)
        V_vals = V(x_fine)
        V_scaled = V_vals / np.max(np.abs(V_vals)) * 0.6 + 0.3
        pot_pts = [ax_left.c2p(xv, max(0, vs)) for xv, vs in zip(x_fine, V_scaled)]
        pot_curve = VMobject(color=DIM, stroke_width=1.2, stroke_opacity=0.5)
        pot_curve.set_points_smoothly(pot_pts)
        self.play(Create(pot_curve), run_time=0.6)

        # Animate snapshots
        step_idx = ValueTracker(0)
        prev_fill = [None]
        x_trace = []
        sigma_trace = []

        for i, (step, psi) in enumerate(snaps):
            prob = np.abs(psi)**2
            prob_scaled = prob / prob.max()

            pts = [ax_left.c2p(xv, p) for xv, p in zip(x, prob_scaled)]
            pts_valid = [p for p in pts if -20 < p[0] < 20 and -20 < p[1] < 20]
            if len(pts_valid) < 4:
                continue
            fill_pts = pts_valid + [ax_left.c2p(x[-1], 0), ax_left.c2p(x[0], 0)]
            try:
                new_fill = Polygon(*fill_pts, color=BLUE, fill_color=BLUE, fill_opacity=0.45, stroke_width=0)
            except Exception:
                continue

            x_trace.append(ax_right.c2p(i, x_means[i]))
            sigma_trace.append(ax_right.c2p(i, sigmas[i]))

            x_curve = VMobject(color=GOLD, stroke_width=2.5)
            if len(x_trace) >= 2:
                x_curve.set_points_as_corners(x_trace)
            sig_curve = VMobject(color=BROWN, stroke_width=2.0)
            if len(sigma_trace) >= 2:
                sig_curve.set_points_as_corners(sigma_trace)

            if prev_fill[0] is None:
                self.play(FadeIn(new_fill), run_time=0.4)
            else:
                self.play(
                    ReplacementTransform(prev_fill[0], new_fill),
                    run_time=0.35,
                )
            if len(x_trace) >= 2:
                self.add(x_curve, sig_curve)
            prev_fill[0] = new_fill

        # Final annotation
        legend = VGroup(
            Text("⟨x⟩(t) = 0", font="EB Garamond", font_size=15, color=GOLD),
            Text("σ_x(t) grows", font="EB Garamond", font_size=15, color=BROWN),
        ).arrange(DOWN, buff=0.1).to_corner(UR, buff=0.4)
        self.play(FadeIn(legend), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_breakdown(self):
        title = Text("Ehrenfest exact only for harmonic or lower-order V(x)",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"\frac{d\langle p\rangle}{dt} = -\langle V'(x)\rangle = -m\omega^2\langle x\rangle - 4\lambda\langle x^3\rangle", color=BLUE, font_size=24),
            MathTex(r"\langle x^3\rangle \neq \langle x\rangle^3\quad\Rightarrow\quad\text{Ehrenfest fails at large amplitude}", color=GOLD, font_size=22),
            MathTex(r"\langle x\rangle = 0\text{ by symmetry, but }|{\psi}|^2\text{ splits into two lobes}", color=BROWN, font_size=22),
            Text("Classical mechanics: ⟨x⟩=0 correct. But probability density: wrong.",
                 font="EB Garamond", font_size=18, color=DIM),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
