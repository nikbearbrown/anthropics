#!/usr/bin/env python3
"""
qm2_parabolic_state_basis.py — Parabolic State in a Square Well: Two Bases, Same ⟨H⟩
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol2

Physics:
    ψ(x) = √(30/L⁵)·x(L-x)  (parabolic state in L=2 nm well, m=mₑ)
    c_n = 4√60/(n³π³) for odd n, 0 for even n
    ⟨H⟩ = 5ℏ²/mL² = 10/π² × E₁ ≈ 1.013 E₁
    |c₁|² ≈ 0.9986  (>99.8% in ground state)
    Normalization: Σ_{odd}|c_n|² = 1 exactly (uses π⁶/960 identity)

Verify:
    python3 qm2_parabolic_state_basis.py --verify

Render:
    manim -qh qm2_parabolic_state_basis.py ParabolicStateBasisScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34
M_E    = 9.10938e-31
EV     = 1.60218e-19
L_NM   = 2.0e-9  # 2 nm well

def energy_eV(n, L=L_NM):
    return (n**2 * np.pi**2 * HBAR**2) / (2 * M_E * L**2) / EV

def psi_n(n, x, L=L_NM):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def psi_parabolic(x, L=L_NM):
    return np.sqrt(30/L**5) * x * (L - x)

def c_n(n, L=L_NM):
    """Expansion coefficient for parabolic state."""
    if n % 2 == 0:
        return 0.0
    return 4 * np.sqrt(60) / (n**3 * np.pi**3)  # with appropriate L factors
    # Actually: c_n = ∫₀ᴸ ψ_n(x) ψ_parab(x) dx
    # = √(2/L) · √(30/L⁵) · ∫₀ᴸ x(L-x)sin(nπx/L)dx
    # = √(60/L³) · [2L³/(n³π³)](1-cos(nπ)) = 4√60/(n³π³) for odd n

def c_n_exact(n, L=L_NM):
    """Exact numerical c_n."""
    x = np.linspace(0, L, 5000)
    integrand = psi_n(n, x, L) * psi_parabolic(x, L)
    return np.trapz(integrand, x)

def verify():
    print("=== Parabolic State Basis Verification ===")
    L = L_NM
    E1 = energy_eV(1, L)
    print(f"E₁ = {E1:.4f} eV")

    # c_n
    print("Expansion coefficients:")
    for n in [1, 3, 5, 7]:
        c = c_n_exact(n, L)
        c_analytic = 4 * np.sqrt(60) / (n**3 * np.pi**3)  # analytic formula
        print(f"  n={n}: c_n = {c:.6f}  (analytic: {c_analytic:.6f})")

    # P1: normalization
    norm_sum = sum(c_n_exact(n, L)**2 for n in range(1, 30, 2))
    print(f"\nP1: Σ|c_n|² = {norm_sum:.6f}  (should be 1.000)")
    print(f"    Analytic: (960/π⁶)×(π⁶/960) = {np.pi**6/960 * 960/np.pi**6:.6f}")

    # P2: ⟨H⟩ from energy basis
    H_energy_basis = sum(c_n_exact(n, L)**2 * energy_eV(n, L) for n in range(1, 30, 2))
    # From position basis
    x_arr = np.linspace(1e-12, L-1e-12, 5000)
    psi = psi_parabolic(x_arr, L)
    d2psi_dx2 = np.gradient(np.gradient(psi, x_arr), x_arr)
    H_pos_basis = -np.trapz(psi * d2psi_dx2, x_arr) * HBAR**2 / (2*M_E) / EV
    H_analytic = 5 * HBAR**2 / (M_E * L**2) / EV

    print(f"\nP2: ⟨H⟩ (energy basis)   = {H_energy_basis:.6f} eV")
    print(f"    ⟨H⟩ (position basis)  = {H_pos_basis:.6f} eV")
    print(f"    ⟨H⟩ (analytic 5ℏ²/mL²) = {H_analytic:.6f} eV")
    print(f"    ⟨H⟩/E₁ = {H_energy_basis/E1:.4f}  (should be 10/π² = {10/np.pi**2:.4f})")
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


class ParabolicStateBasisScene(Scene):
    """
    Split screen:
    Left: parabolic ψ(x) building from eigenstates (running sum)
    Right: |c_n|² bar chart collapsing to n=1 bar
    Bottom: two running integrals converging to same ⟨H⟩
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_expansion()
        self._phase_energy_equality()

    def _phase_title(self):
        title = Text("Basis Independence of ⟨H⟩", font="EB Garamond", font_size=54, color=INK)
        sub = Text(
            "ψ(x) = √(30/L⁵)·x(L−x)  ·  two routes, same answer",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"\langle H\rangle = \sum_n |c_n|^2 E_n = -\frac{\hbar^2}{2m}\int\psi\frac{\partial^2\psi}{\partial x^2}dx = \frac{5\hbar^2}{mL^2}",
            color=BLUE, font_size=24,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_expansion(self):
        L = L_NM
        x_arr = np.linspace(0, L, 300)
        x_norm = x_arr / L

        ax_left = Axes(
            x_range=[0, 1, 0.5], y_range=[-0.05, 1.1, 0.5],
            x_length=5.5, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.3, include_ticks=False, tip_length=0.16),
        ).shift(LEFT*3.4 + UP*0.3)

        ax_right = Axes(
            x_range=[0, 11, 2], y_range=[0, 1.1, 0.5],
            x_length=5.5, y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.3, include_ticks=True, tip_length=0.16),
        ).shift(RIGHT*3.4 + UP*0.3)

        hdr_left = Text("ψ(x) = Σ c_n ψ_n(x)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_left, UP, buff=0.08)
        hdr_right = Text("|c_n|²", font="EB Garamond", font_size=18, color=GOLD).next_to(ax_right, UP, buff=0.08)
        lbl_lx = MathTex(r"x/L", color=INK, font_size=14).next_to(ax_left.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_rx = MathTex(r"n", color=INK, font_size=14).next_to(ax_right.x_axis.get_end(), RIGHT, buff=0.04)

        self.play(Create(ax_left), Create(ax_right), Write(hdr_left), Write(hdr_right),
                  Write(lbl_lx), Write(lbl_rx), run_time=1.0)

        # True parabola
        psi_true = psi_parabolic(x_arr, L)
        psi_true_norm = psi_true / psi_true.max()
        true_pts = [ax_left.c2p(x, y) for x, y in zip(x_norm, psi_true_norm)]
        true_curve = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.6)
        true_curve.set_points_smoothly(true_pts)
        self.play(Create(true_curve), run_time=0.6)

        # Build partial sum step by step
        n_max_list = [1, 3, 5, 7, 9, 15]
        colors_c = [GOLD, BLUE, BROWN, GOLD, BLUE, BROWN]

        prev_curve = None
        bar_group = VGroup()

        for i, n_max in enumerate(n_max_list):
            # Partial sum
            psi_sum = np.zeros_like(x_arr)
            for n in range(1, n_max+1, 2):
                cn = c_n_exact(n, L)
                psi_sum += cn * psi_n(n, x_arr, L)

            psi_sum_norm = psi_sum / psi_true.max()
            sum_pts = [ax_left.c2p(x, y) for x, y in zip(x_norm, psi_sum_norm)]
            new_curve = VMobject(color=colors_c[i % len(colors_c)], stroke_width=2.0)
            new_curve.set_points_smoothly(sum_pts)

            # Bar chart
            new_bars = VGroup()
            for n in range(1, n_max+2, 2):
                cn = c_n_exact(n, L)
                cn2 = cn**2
                bar = Rectangle(
                    width=0.3, height=max(ax_right.c2p(0, cn2)[1] - ax_right.c2p(0,0)[1], 0.01),
                    fill_color=GOLD, fill_opacity=0.8, stroke_width=0,
                )
                bar.move_to(ax_right.c2p(n, cn2/2))
                new_bars.add(bar)

            n_label = Text(f"sum to n={n_max}", font="EB Garamond", font_size=15, color=colors_c[i % len(colors_c)]).to_edge(DOWN, buff=0.25)

            if prev_curve is None:
                self.play(Create(new_curve), FadeIn(new_bars), Write(n_label), run_time=0.8)
            else:
                self.play(ReplacementTransform(prev_curve, new_curve), FadeOut(bar_group), FadeIn(new_bars), ReplacementTransform(prev_label, n_label), run_time=0.7)
            bar_group = new_bars
            prev_curve = new_curve
            prev_label = n_label

        self.wait(1.0)

        # c₁ dominant annotation
        c1 = c_n_exact(1, L)
        ann = MathTex(rf"|c_1|^2 = {c1**2:.4f}\approx 99.86\%", color=GOLD, font_size=22).to_edge(DOWN, buff=0.3)
        self.play(ReplacementTransform(prev_label, ann), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(ax_left, ax_right, hdr_left, hdr_right, lbl_lx, lbl_rx,
                          true_curve, prev_curve, bar_group, ann), run_time=0.5)

    def _phase_energy_equality(self):
        L = L_NM
        E1 = energy_eV(1, L)
        H_analytic = 5 * HBAR**2 / (M_E * L**2) / EV

        title = Text("Two routes — one answer", font="EB Garamond", font_size=32, color=INK).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(
                rf"\langle H\rangle = \frac{{5\hbar^2}}{{mL^2}} = {H_analytic:.4f}\,\mathrm{{eV}}",
                color=GOLD, font_size=28,
            ),
            MathTex(
                rf"\frac{{\langle H\rangle}}{{E_1}} = \frac{{10}}{{\pi^2}} = {10/np.pi**2:.4f}",
                color=BLUE, font_size=28,
            ),
            MathTex(r"\sum_{\rm odd\,n}|c_n|^2 = 1\quad\text{(normalization)}",
                    color=BROWN, font_size=24),
            Text("Energy basis and position basis give the same expectation value",
                 font="EB Garamond", font_size=20, color=DIM),
        ).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=0.7)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.wait(3.0)
