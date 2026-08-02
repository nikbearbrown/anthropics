#!/usr/bin/env python3
"""
vol4_surface_code_threshold.py — Surface Code Threshold: Logical vs. Physical Error Rate
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics:
    p_L ≈ A·(p/p_th)^⌈(d+1)/2⌉
    p_th = 0.01, A = 0.1
    d = 3 → exponent = 2
    d = 5 → exponent = 3
    d = 7 → exponent = 4

Verify:
    python3 vol4_surface_code_threshold.py --verify
"""
import sys
import numpy as np

P_TH = 0.01
A    = 0.1

def exponent(d):
    return (d + 1) // 2   # ceiling((d+1)/2) for odd d

def p_logical(p, d):
    return A * (p / P_TH) ** exponent(d)

def verify():
    print("=== Surface Code Threshold verification ===")
    distances = [3, 5, 7]
    p_vals = [0.002, P_TH, 0.02]

    print(f"{'p':>8}  {'d=3':>12}  {'d=5':>12}  {'d=7':>12}")
    for p in p_vals:
        row = [f"{p_logical(p, d):.4e}" for d in distances]
        print(f"{p:>8.4f}  " + "  ".join(f"{r:>12}" for r in row))

    # P1: at p = p_th, all curves = A exactly
    for d in distances:
        pL = p_logical(P_TH, d)
        assert abs(pL - A) < 1e-12, f"FAIL: p_L(p_th, d={d}) = {pL} ≠ {A}"
    print(f"\nP1: at p = p_th = {P_TH}, all p_L = A = {A}  ✓")

    # P2: suppression factor Λ = p_L(d)/p_L(d+2) = p_th/p
    p_test = 0.002
    for d in [3, 5]:
        lam = p_logical(p_test, d) / p_logical(p_test, d+2)
        expected = P_TH / p_test
        print(f"P2: Λ(d={d}→{d+2}) at p={p_test} = {lam:.2f}  (should be {expected:.1f})")
        assert abs(lam - expected) < 0.01, f"FAIL: Λ = {lam}"

    # Below threshold: d=7 is best
    p_below = 0.002
    pL3 = p_logical(p_below, 3)
    pL7 = p_logical(p_below, 7)
    print(f"\nBelow threshold (p={p_below}):")
    print(f"  p_L(d=3) = {pL3:.4e},  p_L(d=7) = {pL7:.4e}")
    print(f"  Improvement = {pL3/pL7:.0f}×  (should be ≈ 250)")
    assert pL7 < pL3, "FAIL: d=7 should be better below threshold"
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class SurfaceCodeThresholdScene(Scene):
    """
    Log-log plot: three p_L curves for d=3,5,7.
    They meet at p_th=1% (threshold); fan apart below and above.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_curves(ax)
        self._threshold_line(ax)
        self._payoff()

    def _title(self):
        t = Text("Surface Code Threshold", font="EB Garamond",
                 font_size=58, color=INK)
        s = Text(
            "Below 1%: bigger code = better.  Above 1%: bigger code = worse.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        # Log10(p) x-axis; Log10(p_L) y-axis
        ax = Axes(
            x_range=[-3.0, -1.3, 0.5],   # log10(p) from 0.001 to 0.05
            y_range=[-6.0, 0.5, 1.5],
            x_length=9.5,
            y_length=5.8,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.2)

        # Custom axis labels for log scale
        xl = MathTex(r"\log_{10}(p)", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        yl = MathTex(r"\log_{10}(p_L)", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        hdr = Text("Surface code: p_L ≈ 0.1·(p/0.01)^[(d+1)/2]",
                   font="EB Garamond", font_size=18, color=DIM).to_edge(UP, buff=0.25)

        self.play(Create(ax), Write(xl), Write(yl), Write(hdr), run_time=1.2)
        return ax

    def _draw_curves(self, ax):
        p_vals = np.logspace(-3, -1.3, 400)
        configs = [
            (3, BLUE,  r"d=3\;(\text{exp}=2)"),
            (5, BROWN, r"d=5\;(\text{exp}=3)"),
            (7, GOLD,  r"d=7\;(\text{exp}=4)"),
        ]

        for d, color, label in configs:
            pL_vals = np.array([p_logical(p, d) for p in p_vals])
            log_p   = np.log10(p_vals)
            log_pL  = np.log10(pL_vals)

            pts = [ax.c2p(lp, lpL) for lp, lpL in zip(log_p, log_pL)]
            curve = VMobject(color=color, stroke_width=3.5)
            curve.set_points_smoothly(pts)

            # Label at far left
            lbl = MathTex(label, color=color, font_size=20).next_to(
                ax.c2p(-3.0, np.log10(p_logical(1e-3, d))), LEFT, buff=0.08)
            if np.log10(p_logical(1e-3, d)) > -6.5:
                self.play(Create(curve), Write(lbl), run_time=0.9)
            else:
                self.play(Create(curve), run_time=0.9)

        self.wait(0.8)

    def _threshold_line(self, ax):
        log_pth = np.log10(P_TH)
        log_A   = np.log10(A)
        # Vertical threshold line
        vl = DashedLine(
            ax.c2p(log_pth, -6.0), ax.c2p(log_pth, log_A),
            color=INK, stroke_width=2.0, dash_length=0.12,
        )
        # Mark crossing point (all curves = A at p_th)
        dot = Dot(ax.c2p(log_pth, log_A), radius=0.12, color=INK)
        th_lbl = MathTex(r"p_{\rm th} = 1\%", color=INK, font_size=20
                         ).next_to(ax.c2p(log_pth, -5.5), RIGHT, buff=0.1)
        cross_lbl = Text("All curves cross here", font="EB Garamond",
                         font_size=16, color=DIM).next_to(dot, UR, buff=0.1)

        self.play(Create(vl), FadeIn(dot), Write(th_lbl), Write(cross_lbl), run_time=1.2)
        self.wait(1.5)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"p_L \approx A\!\left(\frac{p}{p_{\rm th}}\right)^{\!(d+1)/2}",
                    color=INK, font_size=30),
            MathTex(r"p_{\rm th} = 1\%,\quad A = 0.1",
                    color=GOLD, font_size=26),
            MathTex(r"\Lambda = \frac{p_{\rm th}}{p}\;"
                    r"\Rightarrow\;\text{Willow: }\Lambda=2.14\;\Rightarrow\;p_{\rm eff}=0.47\%",
                    color=BLUE, font_size=23),
        ).arrange(DOWN, buff=0.4).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.9)
        self.wait(3.0)
