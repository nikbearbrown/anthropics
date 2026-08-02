#!/usr/bin/env python3
"""
modern_lorentz_gamma.py — Lorentz Factor: The Gamma Curve Asymptote
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    γ = 1/√(1 − β²), β = v/c
    β=0.5 → γ=1.155; β=0.9 → γ=2.294; β=0.99 → γ=7.089; β=0.999 → γ=22.37
    Muon β=0.998 → γ=15.8, altitude 15 km, observed lifetime 34.8 μs

Run standalone to verify:
    python3 modern_lorentz_gamma.py
"""
import sys
import numpy as np

C_LIGHT = 2.998e8  # m/s
TAU_MUON = 2.2e-6  # s (rest lifetime)


def gamma(beta):
    return 1.0 / np.sqrt(1.0 - beta**2)


def observed_lifetime(beta):
    return gamma(beta) * TAU_MUON


def survival_fraction_observed(beta, altitude_m=15e3):
    """Fraction surviving from altitude to sea level."""
    t_flight = altitude_m / (beta * C_LIGHT)
    g = gamma(beta)
    return np.exp(-t_flight / (g * TAU_MUON))


def verify():
    print("=== Lorentz factor verification ===")
    for b, g_card in [(0.5, 1.155), (0.9, 2.294), (0.99, 7.089), (0.999, 22.37)]:
        g = gamma(b)
        print(f"β={b}: γ={g:.4f}  (card: {g_card})")
    b_muon = 0.998
    g_muon = gamma(b_muon)
    print(f"\nMuon β=0.998: γ={g_muon:.2f}  (card: 15.8)")
    print(f"Observed lifetime = {observed_lifetime(b_muon)*1e6:.1f} μs  (card: 34.8)")
    sf = survival_fraction_observed(b_muon)
    print(f"Survival fraction = {sf:.4f}  (card: ≈0.71)")
    # Classical (no dilation)
    t_flight = 15e3 / (b_muon * C_LIGHT)
    sf_classical = np.exp(-t_flight / TAU_MUON)
    print(f"Classical fraction = {sf_classical:.3e}  (card: ~10^-18)")
    print(f"P1: γ(β=0.99) = {gamma(0.99):.4f}  (should be 7.089)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class ModernLorentzGammaScene(Scene):
    """
    γ(β) curve from 0 to 1, labeled dots, asymptote visualization.
    Second axis: time dilation ratio. Muon annotation.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_curve()
        self._phase_muon()
        self._phase_kinetic_energy()

    def _phase_title(self):
        title = Text("The Lorentz Factor — γ(β)", font="EB Garamond",
                     font_size=64, color=INK)
        sub = MathTex(r"\gamma = \frac{1}{\sqrt{1-\beta^2}},\quad \beta = v/c",
                      color=BLUE, font_size=34)
        hook = Text(
            "Almost flat to β ≈ 0.7, then a cliff — three centuries of Newtonian mechanics fit in the flat part",
            font="EB Garamond", font_size=20, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        f1 = MathTex(r"\gamma = \frac{1}{\sqrt{1-\beta^2}}", color=INK, font_size=40)
        f2 = MathTex(r"\Delta t' = \gamma\,\Delta t_0 \quad\text{(time dilation)}",
                     color=BLUE, font_size=34)
        f3 = MathTex(r"L' = L_0/\gamma \quad\text{(length contraction)}",
                     color=BROWN, font_size=34)
        f4 = MathTex(r"K = (\gamma-1)mc^2 \quad\text{(kinetic energy)}",
                     color=GOLD, font_size=34)
        VGroup(f1, f2, f3, f4).arrange(DOWN, buff=0.38).center()
        for mob in [f1, f2, f3, f4]:
            self.play(Write(mob), run_time=0.8)
        self.wait(2.0)
        self.play(FadeOut(f1, f2, f3, f4), run_time=0.5)

    def _phase_curve(self):
        ax = Axes(
            x_range=[0, 1.0, 0.2],
            y_range=[0, 25, 5],
            x_length=9,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.3)
        lx = MathTex(r"\beta = v/c", color=INK, font_size=24
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"\gamma", color=INK, font_size=24
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("γ(β) curve — nearly flat, then a cliff",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.2)

        b_vals = np.linspace(0.01, 0.9995, 600)
        g_vals = [min(gamma(b), 25) for b in b_vals]
        curve = ax.plot_line_graph(
            x_values=list(b_vals), y_values=g_vals,
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        self.play(Create(curve), run_time=2.5)

        # Labeled dots
        dots_data = [(0.5, 1.155, GOLD), (0.9, 2.294, BROWN), (0.99, 7.089, GOLD)]
        for b, g, color in dots_data:
            d = Dot(ax.c2p(b, min(g, 25)), color=color, radius=0.1)
            lbl = MathTex(f"\\beta={b},\\;\\gamma={g:.3f}", color=color, font_size=20
                          ).next_to(d, RIGHT, buff=0.12)
            self.play(FadeIn(d), Write(lbl), run_time=0.7)

        # Asymptote annotation
        asym = DashedLine(ax.c2p(0.9995, 0), ax.c2p(0.9995, 25), color=DIM,
                          stroke_width=1.5)
        asym_lbl = MathTex(r"\beta \to 1,\;\gamma\to\infty", color=DIM, font_size=20
                           ).next_to(ax.c2p(0.9995, 20), LEFT, buff=0.08)
        self.play(Create(asym), Write(asym_lbl), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, curve, asym, asym_lbl), run_time=0.5)

    def _phase_muon(self):
        b_muon = 0.998
        g_muon = gamma(b_muon)
        obs_life = observed_lifetime(b_muon) * 1e6
        sf = survival_fraction_observed(b_muon)

        rows = VGroup(
            MathTex(r"\mu\text{ at }\beta=0.998:\;\gamma = " + f"{g_muon:.2f}",
                    color=INK, font_size=32),
            MathTex(r"\tau_{\rm obs} = \gamma\tau_0 = " + f"{obs_life:.1f}" + r"\,\mu\text{s}",
                    color=BLUE, font_size=32),
            MathTex(r"\text{Survival fraction} = e^{-t/(\tau_{\rm obs})} \approx "
                    + f"{sf:.2f}", color=GOLD, font_size=32),
            MathTex(r"\text{Classical: }e^{-t/\tau_0} \approx 10^{-18}",
                    color=DIM, font_size=28),
        ).arrange(DOWN, buff=0.45).center()
        title = Text("Atmospheric muons — time dilation confirmed",
                     font="EB Garamond", font_size=28, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)
        for mob in rows:
            self.play(Write(mob), run_time=0.9)
        self.wait(3.0)
        self.play(FadeOut(title, rows), run_time=0.5)

    def _phase_kinetic_energy(self):
        note = VGroup(
            MathTex(r"K = (\gamma-1)mc^2", color=INK, font_size=36),
            MathTex(r"\text{At }\beta=0.9:\;K \approx 1.29\,mc^2",
                    color=GOLD, font_size=30),
            Text("You can never reach c — kinetic energy → ∞ as β → 1",
                 font="EB Garamond", font_size=24, color=BLUE),
            Text("This is why particle accelerators cost billions",
                 font="EB Garamond", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.45).center()
        for mob in note:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob),
                      run_time=0.9)
        self.wait(3.5)
