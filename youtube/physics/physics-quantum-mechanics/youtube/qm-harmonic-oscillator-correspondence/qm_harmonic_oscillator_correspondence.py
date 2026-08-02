#!/usr/bin/env python3
"""
qm_harmonic_oscillator_correspondence.py
Harmonic Oscillator: Eigenstates, Turning Points, and Classical Correspondence
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-harmonic-oscillator-correspondence
    manim -qh qm_harmonic_oscillator_correspondence.py HarmonicOscillatorScene

Verify:
    python3 qm_harmonic_oscillator_correspondence.py

Physics:
    H₂ molecule: ω = 8.0e13 rad/s, ℏω = 0.527 eV
    E₀ = ℏω/2 = 0.264 eV (zero-point energy)
    Classical turning points: x_tp = ±√(2E/mω²) = ±√(2n+1)/α
    where α = (mω/ℏ)^(1/4)
    |ψ_n|² → classical density ∝ 1/√(x_tp²−x²) as n→∞
"""
import sys
import numpy as np
from math import factorial

HBAR = 1.0545718e-34
M_H2 = 2.0 * 1.67262e-27   # reduced mass H₂ ≈ proton mass for diatomic
OMEGA_H2 = 8.0e13          # rad/s
EV   = 1.60218e-19


def hermite(n: int, x: np.ndarray) -> np.ndarray:
    """Physicists' Hermite polynomial H_n(x)."""
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 2.0 * x
    H_prev2, H_prev1 = np.ones_like(x), 2.0 * x
    for k in range(2, n + 1):
        H_curr = 2.0 * x * H_prev1 - 2.0 * (k - 1) * H_prev2
        H_prev2 = H_prev1
        H_prev1 = H_curr
    return H_prev1


def psi_n_sq(n: int, x: np.ndarray, alpha: float) -> np.ndarray:
    """|ψ_n(ξ)|² with ξ = α*x, normalised."""
    xi = alpha * x
    Hn  = hermite(n, xi)
    norm = (alpha / np.sqrt(np.pi)) / (2.0**n * factorial(n))
    return norm * Hn**2 * np.exp(-xi**2)


def classical_density(n: int, x: np.ndarray, alpha: float) -> np.ndarray:
    """Classical probability density ∝ 1/√(x_tp²−x²), normalised."""
    x_tp = np.sqrt(2.0 * n + 1.0) / alpha
    inside = x_tp**2 - x**2
    mask = inside > 1e-12
    rho = np.zeros_like(x)
    rho[mask] = 1.0 / (np.pi * np.sqrt(inside[mask]))
    return rho


def verify():
    print("=== Harmonic Oscillator verification ===")
    hbar_omega = HBAR * OMEGA_H2 / EV
    print(f"ℏω = {hbar_omega:.4f} eV  (card says 0.527 eV)")
    E0 = 0.5 * hbar_omega
    print(f"E₀ = {E0:.4f} eV  (card says 0.264 eV)")
    alpha = (M_H2 * OMEGA_H2 / HBAR) ** 0.25
    x_tp_n0 = np.sqrt(1.0) / alpha * 1e12  # pm
    print(f"α = {alpha:.4e} m^(-1/2)")
    print(f"Classical turning point n=0: x_tp = {x_tp_n0:.1f} pm")
    # Check |ψ₀|² integral
    x_arr = np.linspace(-5.0 / alpha, 5.0 / alpha, 10000)
    dx = x_arr[1] - x_arr[0]
    norm = np.trapz(psi_n_sq(0, x_arr, alpha), x_arr)
    print(f"∫|ψ₀|²dx = {norm:.6f}  (should be 1.0)")
    norm50 = np.trapz(psi_n_sq(50, x_arr, alpha), x_arr)
    print(f"∫|ψ₅₀|²dx = {norm50:.4f}  (should be ≈1.0)")
    print("=== PASSED ===" if abs(norm - 1.0) < 1e-4 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
ORANGE_C = "#F4A261"


class HarmonicOscillatorScene(Scene):
    """
    QHO eigenstates n=0,1,2,5,10,20,50 vs classical density.
    Shows parabola, energy levels, wavefunctions, classical correspondence.
    """

    # Use dimensionless x units: ξ = α*x, so α=1 for display
    ALPHA = 1.0

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_parabola_and_levels()
        self._phase_eigenstates_sequence()
        self._phase_zero_point()

    def _phase_title(self):
        title = Text("Quantum Harmonic Oscillator", font="EB Garamond",
                     font_size=54, color=INK)
        sub1 = Text(
            "Ground state peaks at center — classical ball peaks at edges.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"E_n = \left(n + \tfrac{1}{2}\right)\hbar\omega",
                       color=BLUE, font_size=30)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_parabola_and_levels(self):
        ax = Axes(
            x_range=[-5, 5, 2],
            y_range=[0, 13, 2],
            x_length=8.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.2)
        lbl_x = MathTex(r"\xi = \alpha x", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"E / (\hbar\omega)", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Energy levels + parabolic potential  (H₂, ω = 8×10¹³ rad/s)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        # Parabola V(ξ) = ξ²/2 in units of ℏω
        xi_arr = np.linspace(-5, 5, 300)
        V_arr  = 0.5 * xi_arr**2
        parabola_pts = [ax.c2p(xi, v) for xi, v in zip(xi_arr, V_arr)]
        parabola = VMobject(color=DIM, stroke_width=2.5)
        parabola.set_points_smoothly(parabola_pts)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), Create(parabola), run_time=1.8)

        for n in range(6):
            E_n = n + 0.5  # in units of ℏω
            x_tp = np.sqrt(2.0 * E_n)
            color = BLUE if n == 0 else (GOLD if n == 1 else DIM)
            lvl = DashedLine(
                ax.c2p(-x_tp, E_n), ax.c2p(x_tp, E_n),
                color=color, dash_length=0.1, stroke_width=2.0,
            )
            lbl = MathTex(f"n={n}", color=color, font_size=17).next_to(
                ax.c2p(x_tp, E_n), RIGHT, buff=0.06
            )
            self.play(Create(lvl), Write(lbl), run_time=0.5)

        self.wait(1.0)
        self.stored_ax = ax
        self.stored_parabola = parabola
        self.stored_ax_lbls = VGroup(lbl_x, lbl_y, hdr)

    def _phase_eigenstates_sequence(self):
        ax = self.stored_ax
        ns_show = [0, 1, 2, 5, 10, 20, 50]

        for n in ns_show:
            E_n    = n + 0.5
            x_tp   = np.sqrt(2.0 * E_n)
            x_range_disp = min(x_tp * 1.4, 4.8)
            xi_arr = np.linspace(-x_range_disp, x_range_disp, 500)

            # Quantum density
            psi2 = psi_n_sq(n, xi_arr, self.ALPHA)
            # Classical density
            cls  = classical_density(n, xi_arr, self.ALPHA)

            # Scale amplitude to fit between consecutive energy levels (amplitude ≈ 0.8 ℏω)
            scale_q = 0.8 / (psi2.max() + 1e-15)
            scale_c = 0.8 / (cls.max() + 1e-15) if cls.max() > 0 else 1.0

            pts_q = [ax.c2p(xi, E_n + y * scale_q) for xi, y in zip(xi_arr, psi2)]
            pts_c = [ax.c2p(xi, E_n + y * scale_c) for xi, y in zip(xi_arr, cls)]

            c_q = VMobject(color=BLUE, stroke_width=2.5)
            c_q.set_points_smoothly(pts_q)
            c_c = VMobject(color=ORANGE_C, stroke_width=2.0, stroke_opacity=0.7)
            c_c.set_points_smoothly(pts_c)

            caption_str = (
                f"n = {n}  —  {n} node{'s' if n != 1 else ''}; "
                f"{'center peak' if n==0 else 'converging to classical'}"
            )
            caption = Text(caption_str, font="EB Garamond", font_size=20, color=INK
                           ).to_edge(DOWN, buff=0.22)

            if n == 0:
                self.play(Create(c_q), Create(c_c), Write(caption), run_time=1.2)
            else:
                self.play(Transform(self._last_q, c_q),
                          Transform(self._last_c, c_c),
                          Transform(self._last_cap, caption), run_time=0.9)
                continue

            self._last_q   = c_q
            self._last_c   = c_c
            self._last_cap = caption
            self.wait(0.4)
            continue

        # For n>0, we need the first Transform set up
        self._last_q   = VGroup()
        self._last_c   = VGroup()
        self._last_cap = VGroup()
        for n in ns_show:
            E_n    = n + 0.5
            x_tp   = np.sqrt(2.0 * E_n)
            x_range_disp = min(x_tp * 1.4, 4.8)
            xi_arr = np.linspace(-x_range_disp, x_range_disp, 500)
            psi2 = psi_n_sq(n, xi_arr, self.ALPHA)
            cls  = classical_density(n, xi_arr, self.ALPHA)
            scale_q = 0.8 / (psi2.max() + 1e-15)
            scale_c = 0.8 / (cls.max() + 1e-15) if cls.max() > 0 else 1.0
            pts_q = [ax.c2p(xi, E_n + y * scale_q) for xi, y in zip(xi_arr, psi2)]
            pts_c = [ax.c2p(xi, E_n + y * scale_c) for xi, y in zip(xi_arr, cls)]
            c_q = VMobject(color=BLUE, stroke_width=2.5)
            c_q.set_points_smoothly(pts_q)
            c_c = VMobject(color=ORANGE_C, stroke_width=2.0, stroke_opacity=0.7)
            c_c.set_points_smoothly(pts_c)
            caption_str = (
                f"n = {n}  —  {n} node{'s' if n != 1 else ''}"
                f"{'  ← quantum' if n==0 else ''}"
            )
            caption = Text(caption_str, font="EB Garamond", font_size=20, color=INK
                           ).to_edge(DOWN, buff=0.22)
            if n == ns_show[0]:
                self.play(Create(c_q), Create(c_c), Write(caption), run_time=1.2)
            else:
                self.play(Transform(self._last_q, c_q),
                          Transform(self._last_c, c_c),
                          Transform(self._last_cap, caption), run_time=1.0)
            self._last_q   = c_q
            self._last_c   = c_c
            self._last_cap = caption
            self.wait(0.5)

        legend_q = Text("Quantum  |ψ_n|²", font="EB Garamond", font_size=20, color=BLUE
                        ).to_edge(DOWN, buff=0.55)
        legend_c = Text("Classical 1/v density", font="EB Garamond", font_size=20, color=ORANGE_C
                        ).to_edge(DOWN, buff=0.28)
        self.play(Transform(self._last_cap, VGroup()), Write(legend_q), Write(legend_c), run_time=0.8)
        self.wait(2.0)

    def _phase_zero_point(self):
        self.play(FadeOut(*self.mobjects), run_time=0.5)
        eq = MathTex(
            r"E_0 = \tfrac{1}{2}\hbar\omega = 0.264\,\mathrm{eV} \quad (\mathrm{H}_2)",
            color=INK, font_size=34,
        ).shift(UP * 0.5)
        note = Text(
            "Zero-point energy: the oscillator never stops — uncertainty principle forbids it.",
            font="EB Garamond", font_size=22, color=DIM,
        ).next_to(eq, DOWN, buff=0.45)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(note), run_time=0.9)
        self.wait(3.0)
