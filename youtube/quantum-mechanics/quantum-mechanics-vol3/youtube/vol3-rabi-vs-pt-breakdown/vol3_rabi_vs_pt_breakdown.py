#!/usr/bin/env python3
"""
vol3_rabi_vs_pt_breakdown.py — Rabi Oscillations vs. First-Order Perturbation Theory Breakdown
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    ℏω₀ = 2.00 eV, ℏΩ = 0.010 eV at resonance (Δ = 0)
    Exact:   P_exact(t) = sin²(Ωt/2)        [Rabi formula, bounded 0–1]
    PT:      P_pt(t)    = (Ωt/2)²            [first-order perturbation theory]
    π-pulse: t_π = π/Ω

Verify (run with --verify):
    python3 vol3_rabi_vs_pt_breakdown.py --verify
"""
import sys
import numpy as np

HBAR  = 6.582119569e-16   # eV·s
E0    = 2.00              # eV  (transition energy ℏω₀)
HOMEG = 0.010             # eV  (coupling ℏΩ)
OMEGA = HOMEG / HBAR      # rad/s  (Ω = ℏΩ / ℏ)

T_PI = np.pi / OMEGA      # s — π-pulse time

def P_exact(t):
    return np.sin(OMEGA * t / 2) ** 2

def P_pt(t):
    return (OMEGA * t / 2) ** 2

def verify():
    print("=== Rabi vs PT verification ===")
    print(f"ℏΩ = {HOMEG} eV,  ℏω₀ = {E0} eV,  Δ = 0 (resonance)")
    print(f"Ω = {OMEGA:.4e} rad/s")
    print(f"t_π = π/Ω = {T_PI:.4e} s  ≈ {T_PI*1e12:.3f} ps")
    print()

    t = T_PI
    pe  = P_exact(t)
    ppt = P_pt(t)
    print(f"At t = t_π (first π-pulse):")
    print(f"  P_exact = sin²(π/2)   = {pe:.6f}   (should be 1.000000)")
    print(f"  P_PT    = (π/2)²      = {ppt:.6f}   (should be {(np.pi/2)**2:.6f} ≈ 2.467)")
    assert abs(pe - 1.0) < 1e-10, "FAIL: exact P at t_π should be 1"
    assert abs(ppt - (np.pi/2)**2) < 1e-10, "FAIL: PT P at t_π should be (π/2)²"
    print()

    # P2: PT and exact agree to within 10% while Ωt < 0.55 rad
    threshold = 0.55  # rad
    t_thresh = threshold / OMEGA
    pe2  = P_exact(t_thresh)
    ppt2 = P_pt(t_thresh)
    ratio = abs(ppt2 - pe2) / pe2
    print(f"At Ωt = 0.55 rad (t = {t_thresh:.4e} s):")
    print(f"  P_exact = {pe2:.6f}")
    print(f"  P_PT    = {ppt2:.6f}")
    print(f"  Relative error = {ratio:.4f}  (should be < 0.10)")
    assert ratio < 0.10, f"FAIL: relative error {ratio:.4f} should be < 10%"
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
RED    = "#E05252"


class RabiVsPtBreakdownScene(Scene):
    """
    Two curves: exact Rabi sin²(Ωt/2) and PT parabola (Ωt/2)².
    PT bursts through the P=1 ceiling; Rabi turns back.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._title()
        ax = self._axes()
        self._draw_curves(ax)
        self._payoff()

    def _title(self):
        t = Text("Rabi vs. Perturbation Theory", font="EB Garamond",
                 font_size=60, color=INK)
        s = Text(
            "First-order PT predicts P = 247%  —  the exact formula says otherwise",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.2)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0, 3.5 * np.pi, np.pi],
            y_range=[0, 3.2, 0.5],
            x_length=10.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
            x_axis_config=dict(tick_size=0.07),
            y_axis_config=dict(tick_size=0.07),
        ).shift(DOWN * 0.3)

        # Axis labels
        xl = MathTex(r"\Omega t \;(\mathrm{rad})", color=INK, font_size=24
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        yl = MathTex(r"P_{\uparrow}(t)", color=INK, font_size=24
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Custom x-tick labels
        for k, label in [(np.pi, r"\pi"), (2*np.pi, r"2\pi"), (3*np.pi, r"3\pi")]:
            lbl = MathTex(label, color=DIM, font_size=20).next_to(
                ax.c2p(k, 0), DOWN, buff=0.18)
            self.add(lbl)

        # P = 1 line
        p1 = DashedLine(
            ax.c2p(0, 1), ax.c2p(3.5 * np.pi, 1),
            color=GOLD, stroke_width=1.5, dash_length=0.12,
        )
        p1_lbl = MathTex(r"P = 1", color=GOLD, font_size=20).next_to(
            ax.c2p(0, 1), LEFT, buff=0.05)

        # INVALID zone (P > 1) — shaded
        invalid_pts = [
            ax.c2p(0, 1), ax.c2p(3.5 * np.pi, 1),
            ax.c2p(3.5 * np.pi, 3.2), ax.c2p(0, 3.2),
        ]
        invalid_zone = Polygon(*invalid_pts, color=RED, fill_color=RED,
                               fill_opacity=0.12, stroke_width=0)
        invalid_lbl = Text("INVALID", font="EB Garamond", font_size=18,
                           color=RED).move_to(ax.c2p(2.0 * np.pi, 2.6))

        self.play(Create(ax), Write(xl), Write(yl), run_time=1.5)
        self.play(Create(p1), Write(p1_lbl), run_time=0.7)
        self.play(FadeIn(invalid_zone), Write(invalid_lbl), run_time=0.8)
        return ax

    def _draw_curves(self, ax):
        # Sample Ωt from 0 to 3.5π
        t_vals = np.linspace(0, 3.5 * np.pi, 600)   # Ωt in rad

        # Exact Rabi — bounded
        exact_pts = [ax.c2p(ot, np.sin(ot / 2) ** 2) for ot in t_vals]
        exact_curve = VMobject(color=BLUE, stroke_width=3.5)
        exact_curve.set_points_smoothly(exact_pts)

        # PT parabola — clips at plot top
        pt_vals = np.clip((t_vals / 2) ** 2, 0, 3.2)
        pt_pts = [ax.c2p(ot, pv) for ot, pv in zip(t_vals, pt_vals)]
        pt_curve = VMobject(color=BROWN, stroke_width=3.5)
        pt_curve.set_points_smoothly(pt_pts)

        # Legend
        exact_leg = Line(ORIGIN, RIGHT * 0.5, color=BLUE, stroke_width=3)
        exact_txt = MathTex(r"P_{\rm exact} = \sin^2(\Omega t/2)",
                            color=BLUE, font_size=22)
        pt_leg    = Line(ORIGIN, RIGHT * 0.5, color=BROWN, stroke_width=3)
        pt_txt    = MathTex(r"P_{\rm PT} = (\Omega t/2)^2",
                            color=BROWN, font_size=22)
        leg = VGroup(
            VGroup(exact_leg, exact_txt).arrange(RIGHT, buff=0.15),
            VGroup(pt_leg,    pt_txt).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(UL, buff=0.4)

        lbl_draw = Text(
            "Exact Rabi (blue) turns back. PT (brown) climbs past P = 1.",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.22)

        self.play(Create(exact_curve), Create(pt_curve), run_time=3.0)
        self.play(FadeIn(leg), Write(lbl_draw), run_time=0.8)
        self.wait(1.5)

        # Annotate π-pulse
        arrow = Arrow(ax.c2p(np.pi, 1.6), ax.c2p(np.pi, 1.02),
                      color=GOLD, buff=0.05, stroke_width=2.5)
        ann = MathTex(r"t_\pi: P_{\rm exact}=1,\;P_{\rm PT}\approx2.47",
                      color=GOLD, font_size=20).next_to(
                          ax.c2p(np.pi, 1.7), UP, buff=0.05)
        self.play(GrowArrow(arrow), Write(ann), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(arrow, ann, lbl_draw), run_time=0.4)

    def _payoff(self):
        eq = MathTex(
            r"\text{Breakdown when}\;\Omega t \gtrsim 1",
            r"\quad\Rightarrow\quad",
            r"P_{\rm PT} > 1 \;\;\text{(unphysical)}",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(eq), run_time=1.5)
        self.wait(3.0)
