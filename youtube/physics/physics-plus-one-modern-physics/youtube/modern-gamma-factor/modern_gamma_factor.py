#!/usr/bin/env python3
"""
modern_gamma_factor.py — The Gamma Factor γ(v): The Relativistic Rise Toward c
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-gamma-factor
    manim -qh modern_gamma_factor.py GammaFactorScene

Physics:
    γ = 1/sqrt(1 - β²)   β = v/c
    β=0.5:  γ=1.155
    β=0.9:  γ=2.294
    β=0.99: γ=7.089
    β=0.9994: γ=28.9 (muon)
    LHC: β≈1, γ≈7461, E=7 TeV
"""
import sys
import numpy as np


def gamma(beta):
    return 1.0 / np.sqrt(1.0 - beta**2)


if __name__ == "__main__":
    print("=== Gamma Factor Verification ===")
    for beta, expected in [(0.5, 1.155), (0.9, 2.294), (0.99, 7.089)]:
        g = gamma(beta)
        print(f"  β={beta}: γ={g:.4f}  (expect {expected})")
        assert abs(g - expected) < 0.002, f"FAIL at β={beta}"
    # Muon
    g_muon = gamma(0.9994)
    print(f"  Muon β=0.9994: γ={g_muon:.2f}  (expect 28.9)")
    assert abs(g_muon - 28.9) < 0.5, "Muon FAIL"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class GammaFactorScene(Scene):
    """γ(β) curve with labeled points + relativistic momentum/energy add-on."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_curve(ax)
        self._phase_extra(ax)

    def _phase_title(self):
        title = Text("The Lorentz Factor γ", font="EB Garamond", font_size=60, color=INK)
        sub = Text("γ → ∞ as v → c — the mathematical asymptote that is the speed limit",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0, 1.0, 0.2],
            y_range=[1, 11, 2],
            x_length=8.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.1)
        x_lbl = MathTex(r"\beta=v/c", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\gamma", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _phase_curve(self, ax):
        beta = np.linspace(0, 0.995, 800)
        gam  = gamma(beta)
        gam_c = np.clip(gam, 1, 10.5)
        pts = [ax.c2p(b, g) for b, g in zip(beta, gam_c)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)

        # Key labeled points
        key_pts = [
            (0.5,    1.155, "β=0.5,  γ=1.155"),
            (0.9,    2.294, "β=0.9,  γ=2.29"),
            (0.99,   7.089, "β=0.99, γ=7.09"),
            (0.9994, 10.5,  "β=0.9994  (muon γ=28.9 off chart)"),
        ]

        # Newtonian region shading (β < 0.1, γ within 0.5% of 1)
        newt_pts = ([ax.c2p(0, 1)]
                    + [ax.c2p(b, g) for b, g in zip(beta[:60], gam_c[:60])]
                    + [ax.c2p(beta[59], 1)])
        newt_fill = Polygon(*newt_pts, color=DIM,
                            fill_color=DIM, fill_opacity=0.18, stroke_width=0)
        newt_lbl = Text("Newtonian regime", font="EB Garamond",
                        font_size=16, color=DIM).move_to(ax.c2p(0.055, 1.6))

        # γ = 1 reference
        newtonian = DashedLine(ax.c2p(0, 1), ax.c2p(0.995, 1),
                               color=DIM, stroke_width=1.2)

        hdr = MathTex(r"\gamma=\frac{1}{\sqrt{1-v^2/c^2}}", color=INK,
                      font_size=34).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(newtonian), run_time=0.8)
        self.play(Create(curve), run_time=2.5)
        self.play(FadeIn(newt_fill), Write(newt_lbl), run_time=0.8)

        for b, g, label in key_pts[:3]:
            g_plot = min(g, 10.5)
            dot = Dot(ax.c2p(b, g_plot), color=GOLD, radius=0.1)
            lbl = Text(label, font="EB Garamond",
                       font_size=16, color=GOLD).next_to(ax.c2p(b, g_plot), RIGHT, buff=0.08)
            self.play(FadeIn(dot), Write(lbl), run_time=0.7)

        muon_dot = Dot(ax.c2p(0.9994, 10.5), color=BROWN, radius=0.1)
        muon_lbl = Text("Muon  γ = 28.9", font="EB Garamond",
                        font_size=16, color=BROWN).next_to(muon_dot, LEFT, buff=0.1)
        self.play(FadeIn(muon_dot), Write(muon_lbl), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(hdr, newt_fill, newt_lbl, muon_dot, muon_lbl,
                          newtonian), run_time=0.5)
        # Keep curve
        self._curve = curve

    def _phase_extra(self, ax):
        # Relativistic momentum p = γmv and KE = (γ-1)mc²
        beta = np.linspace(0.01, 0.995, 600)
        gam  = gamma(beta)
        p_norm = np.clip(gam * beta, 0, 10.5)      # γβ (normalized)
        ke_norm = np.clip(gam - 1, 0, 10.5)         # (γ-1)

        pts_p  = [ax.c2p(b, p) for b, p in zip(beta, p_norm)]
        pts_ke = [ax.c2p(b, k) for b, k in zip(beta, ke_norm)]

        curve_p  = VMobject(color=GOLD, stroke_width=2.0)
        curve_p.set_points_smoothly(pts_p)
        curve_ke = VMobject(color=BROWN, stroke_width=2.0)
        curve_ke.set_points_smoothly(pts_ke)

        lbl_p  = Text("p/mc = γβ", font="EB Garamond",
                      font_size=18, color=GOLD).move_to(ax.c2p(0.75, 4.5))
        lbl_ke = Text("KE/mc² = γ−1", font="EB Garamond",
                      font_size=18, color=BROWN).move_to(ax.c2p(0.55, 2.5))
        hdr = Text("All relativistic quantities share the same γ",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.22)

        self.play(Write(hdr), Create(curve_p), Create(curve_ke),
                  Write(lbl_p), Write(lbl_ke), run_time=2.0)
        self.wait(2.5)
        final = Text("The asymptote at β = 1 is the speed of light — not an engineering limit",
                     font="EB Garamond", font_size=22, color=INK).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.2)
        self.wait(2.5)
