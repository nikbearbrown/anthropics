#!/usr/bin/env python3
"""
thermo_carnot_efficiency_surface.py — Carnot Efficiency vs Temperature Ratio with Real Benchmarks
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-thermodynamics book.

Render:
    cd physics-plus-one-thermodynamics/youtube/thermo-carnot-efficiency-surface
    manim -qh thermo_carnot_efficiency_surface.py CarnotEfficiencySurfaceScene

Physics:
    η_C = 1 - T_C/T_H = 1 - r   where r = T_C/T_H ∈ (0,1)
    η_C = 0 at r = 1 (equal temps)
    η_C = 0.5 at r = 0.5 (T_H = 2T_C)
"""
import sys
import numpy as np


def eta_carnot(r):
    return 1.0 - r


ENGINES = [
    ("Coal plant",   823,  298, 0.40),
    ("Natural gas", 1100,  310, 0.60),
    ("Nuclear PWR",  600,  310, 0.33),
    ("Car engine",   800,  310, 0.25),
]

if __name__ == "__main__":
    print("=== Carnot Efficiency Surface Verification ===")
    for name, TH, TC, real in ENGINES:
        r = TC / TH
        eta_c = eta_carnot(r)
        print(f"  {name}: r={r:.3f}, η_C={eta_c*100:.1f}%, real={real*100:.0f}%")
    # P1: η_C = 0 at r = 1
    assert eta_carnot(1.0) == 0.0, "P1 FAIL"
    # P2: η_C = 0.5 at r = 0.5
    assert abs(eta_carnot(0.5) - 0.5) < 1e-10, "P2 FAIL"
    print("P1: η_C(r=1) = 0  ✓")
    print("P2: η_C(r=0.5) = 0.5  ✓")
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


class CarnotEfficiencySurfaceScene(Scene):
    """η_C = 1 - r line with real engine data points below the ceiling."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_carnot_line(ax)
        self._phase_engines(ax)
        self._phase_slider(ax)

    def _phase_title(self):
        title = Text("Carnot Efficiency Ceiling", font="EB Garamond",
                     font_size=54, color=INK)
        sub = Text("η_C = 1 − T_C/T_H — one curve, every heat engine ever built",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0, 1.05, 0.2],
            y_range=[0, 1.05, 0.2],
            x_length=7.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(LEFT * 0.5 + DOWN * 0.2)
        x_lbl = MathTex(r"r = T_C/T_H", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"\eta_C", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _phase_carnot_line(self, ax):
        r_arr = np.linspace(0.01, 1.0, 300)
        eta_arr = eta_carnot(r_arr)
        pts = [ax.c2p(r, e) for r, e in zip(r_arr, eta_arr)]
        line = VMobject(color=BLUE, stroke_width=3.0)
        line.set_points_smoothly(pts)

        # Forbidden region (above line)
        forbidden_pts = ([ax.c2p(0, 1)] +
                         [ax.c2p(r, e) for r, e in zip(r_arr, eta_arr)] +
                         [ax.c2p(1, 0), ax.c2p(1, 1)])
        forbidden = Polygon(*forbidden_pts, color=BROWN,
                            fill_color=BROWN, fill_opacity=0.15, stroke_width=0)
        forbidden_lbl = Text("Forbidden\n(2nd Law)", font="EB Garamond",
                             font_size=18, color=BROWN).move_to(ax.c2p(0.35, 0.85))

        achievable_lbl = Text("Achievable", font="EB Garamond",
                               font_size=18, color=DIM).move_to(ax.c2p(0.7, 0.2))

        self.play(Create(line), run_time=2.0)
        self.play(FadeIn(forbidden), Write(forbidden_lbl), Write(achievable_lbl),
                  run_time=1.2)
        eq = MathTex(r"\eta_C = 1 - r", color=BLUE, font_size=30).move_to(
            ax.c2p(0.2, 0.6))
        self.play(Write(eq), run_time=0.8)
        self.wait(1.5)
        self._carnot_line = line
        self._forbidden = forbidden
        self._forbidden_lbl = forbidden_lbl
        self._achievable_lbl = achievable_lbl
        self._eq = eq

    def _phase_engines(self, ax):
        dots = VGroup()
        lbls = VGroup()
        gaps = VGroup()

        for name, TH, TC, real in ENGINES:
            r = TC / TH
            eta_c = eta_carnot(r)
            dot = Dot(ax.c2p(r, real), color=GOLD, radius=0.1)
            lbl = Text(name, font="EB Garamond", font_size=16, color=DIM).next_to(
                ax.c2p(r, real), RIGHT, buff=0.08)
            gap_line = DashedLine(ax.c2p(r, real), ax.c2p(r, eta_c),
                                  color=DIM, stroke_width=1.2)
            dots.add(dot)
            lbls.add(lbl)
            gaps.add(gap_line)

        self.play(Create(gaps), run_time=0.8)
        self.play(Create(dots), Write(lbls), run_time=1.2)
        irr_lbl = Text("gap = irreversibility", font="EB Garamond",
                       font_size=18, color=DIM).to_edge(DOWN, buff=0.3)
        self.play(Write(irr_lbl), run_time=0.7)
        self.wait(2.5)
        self.play(FadeOut(dots, lbls, gaps, irr_lbl), run_time=0.5)

    def _phase_slider(self, ax):
        # Animate a moving point along η_C = 1-r as r sweeps 0→1
        r_track = ValueTracker(0.01)

        def _pt():
            r = r_track.get_value()
            return Dot(ax.c2p(r, eta_carnot(r)), color=GOLD, radius=0.12)

        dyn_pt = always_redraw(_pt)

        eta_lbl = MathTex(r"\eta_C = ", color=GOLD, font_size=32)
        eta_num = DecimalNumber(eta_carnot(0.01) * 100,
                                num_decimal_places=1, color=GOLD, font_size=32)
        eta_pct = MathTex(r"\%", color=GOLD, font_size=32)
        eta_num.add_updater(lambda m: m.set_value(eta_carnot(r_track.get_value()) * 100))

        r_lbl = MathTex(r"r = ", color=DIM, font_size=28)
        r_num  = DecimalNumber(0.01, num_decimal_places=3, color=DIM, font_size=28)
        r_num.add_updater(lambda m: m.set_value(r_track.get_value()))

        row1 = VGroup(eta_lbl, eta_num, eta_pct).arrange(RIGHT, buff=0.08)
        row2 = VGroup(r_lbl, r_num).arrange(RIGHT, buff=0.08)
        VGroup(row2, row1).arrange(DOWN, buff=0.2).to_edge(RIGHT, buff=0.5)

        hdr = Text("r → 1  means  T_H → T_C  →  η → 0",
                   font="EB Garamond", font_size=21, color=INK).to_edge(UP, buff=0.18)
        self.add(dyn_pt)
        self.play(Write(hdr), FadeIn(row1), FadeIn(row2), run_time=0.8)
        self.play(r_track.animate.set_value(0.99), run_time=6.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("Equal temperatures → zero net work → second law enforced",
                     font="EB Garamond", font_size=22, color=INK).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(hdr, row1, row2), Write(final), run_time=1.2)
        self.wait(2.5)
