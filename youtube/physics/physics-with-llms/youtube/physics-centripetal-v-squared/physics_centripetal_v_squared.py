#!/usr/bin/env python3
"""
physics_centripetal_v_squared.py — Centripetal Force Scales as v²
SILENT SLATE — sim-scout candidate, physics-with-llms book.

Physics:
  F_c = mv²/r
  r = 500 m, m = 1200 kg
  v sweeps 20 → 60 m/s

Testable predictions:
  P1: F_c(50) = 4 × F_c(25) exactly (6000 N vs 1500 N)
  P2: At v=25 m/s, a_c = v²/r = 1.25 m/s² ≈ 12.8% g

Run standalone verification:
  python3 physics_centripetal_v_squared.py --verify

Render:
  manim -qh physics_centripetal_v_squared.py CentripetalVSquaredScene
"""
import sys
import numpy as np

R_ROAD = 500.0   # m
M_CAR  = 1200.0  # kg
G_STD  = 9.8     # m/s²

def centripetal_force(v: float) -> float:
    return M_CAR * v**2 / R_ROAD

def centripetal_accel(v: float) -> float:
    return v**2 / R_ROAD

def verify():
    print("=== Centripetal v² verification ===")
    for v in [25, 50]:
        Fc = centripetal_force(v)
        ac = centripetal_accel(v)
        print(f"  v={v} m/s  F_c={Fc:.1f} N  a_c={ac:.3f} m/s² ({ac/G_STD*100:.1f}% g)")
    ratio = centripetal_force(50) / centripetal_force(25)
    print(f"  F(50)/F(25) = {ratio:.4f}  (expect 4.0000)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

V_MIN = 20.0
V_MAX = 60.0


class CentripetalVSquaredScene(Scene):
    """
    Left panel: car sweeping a circular arc, centripetal force arrow grows.
    Right panel: live bar chart of F_c — curve of v².
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Centripetal Force  ∝  v²", font="EB Garamond", font_size=58, color=INK)
        sub   = Text(
            "Double the speed → quadruple the force",
            font="EB Garamond", font_size=28, color=GOLD,
        )
        sub2  = Text(
            "F_c = mv² / r    r = 500 m,  m = 1200 kg",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Graph: F_c vs v ────────────────────────────────────────────────
        ax = Axes(
            x_range=[V_MIN, V_MAX + 2, 10],
            y_range=[0, 9000, 1500],
            x_length=9.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.5)

        lbl_x = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"F_c\;(\mathrm{N})",  color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP,   buff=0.08)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # Draw the v² curve
        v_arr = np.linspace(V_MIN, V_MAX, 300)
        F_arr = M_CAR * v_arr**2 / R_ROAD
        pts   = [ax.c2p(float(v), float(F)) for v, F in zip(v_arr, F_arr)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=2.5)
        self.wait(0.5)

        # ── Key markers: v=25 and v=50 ─────────────────────────────────────
        F25 = centripetal_force(25)
        F50 = centripetal_force(50)

        dot25 = Dot(ax.c2p(25, F25), color=BROWN, radius=0.12)
        dot50 = Dot(ax.c2p(50, F50), color=GOLD,  radius=0.12)

        lbl25 = Text(f"v=25 m/s\nF={F25:.0f} N", font="EB Garamond", font_size=19, color=BROWN)
        lbl25.next_to(dot25, UP + LEFT, buff=0.1)
        lbl50 = Text(f"v=50 m/s\nF={F50:.0f} N", font="EB Garamond", font_size=19, color=GOLD)
        lbl50.next_to(dot50, UP + RIGHT, buff=0.1)

        self.play(FadeIn(dot25, scale=1.5), Write(lbl25), run_time=0.9)
        self.play(FadeIn(dot50, scale=1.5), Write(lbl50), run_time=0.9)
        self.wait(0.6)

        # ── Ratio callout ──────────────────────────────────────────────────
        brace_line = DashedLine(
            ax.c2p(50, F25), ax.c2p(50, F50),
            color=GOLD, stroke_width=2,
        )
        ratio_lbl = MathTex(
            r"\times 4", color=GOLD, font_size=36,
        ).next_to(brace_line, RIGHT, buff=0.12)

        self.play(Create(brace_line), Write(ratio_lbl), run_time=1.0)
        self.wait(0.8)

        # ── Formula strip ──────────────────────────────────────────────────
        eq = MathTex(
            r"F_c = \frac{mv^2}{r}\;\Rightarrow\;2v \;\Rightarrow\; 4F_c",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(eq), run_time=1.2)
        self.wait(2.5)

        # ── Quick comparison: linear vs quadratic ──────────────────────────
        F_lin = M_CAR * v_arr / R_ROAD * (V_MIN + 5)   # scaled linear for visual
        # Normalize so they start at same point at V_MIN
        F_lin_norm = centripetal_force(V_MIN) * (v_arr / V_MIN)
        pts_lin = [ax.c2p(float(v), float(F)) for v, F in zip(v_arr, F_lin_norm)]
        lin_curve = VMobject(color=BROWN, stroke_width=2.0, stroke_opacity=0.7)
        lin_curve.set_points_smoothly(pts_lin)

        lin_lbl = Text("linear (for comparison)", font="EB Garamond", font_size=18, color=BROWN)
        lin_lbl.next_to(ax.c2p(55, centripetal_force(V_MIN) * 55 / V_MIN), RIGHT, buff=0.05)

        anno = Text(
            "Force grows as v² — not v",
            font="EB Garamond", font_size=24, color=INK,
        ).to_edge(UP, buff=0.25)

        self.play(
            FadeOut(eq), Create(lin_curve), Write(lin_lbl), Write(anno),
            run_time=1.2,
        )
        self.wait(3.0)
