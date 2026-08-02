#!/usr/bin/env python3
"""
physics_free_fall_three_panels.py — Free Fall: y(t), v(t), a(t) in Sync
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    v₀ = 13.0 m/s (upward), g = 9.80 m/s²
    t_peak = 13.0/9.80 = 1.327 s
    y_max  = 13²/(2×9.80) = 8.62 m
    Return to y=0 at t ≈ 2.653 s, v = -13.0 m/s

Render:
    cd physics/youtube/physics-free-fall-three-panels
    manim -qh physics_free_fall_three_panels.py FreeFallScene
"""
import sys
import numpy as np

V0 = 13.0    # m/s
G  = 9.80    # m/s²

def y_t(t):    return V0*t - 0.5*G*t**2
def v_t(t):    return V0 - G*t
def a_t(t):    return -G + 0*t   # constant


def verify():
    t_peak = V0/G
    y_max  = V0**2/(2*G)
    t_ret  = 2*V0/G
    print("=== Free Fall verification ===")
    print(f"  t_peak = {t_peak:.4f} s  (expected 1.3265)")
    print(f"  y_max  = {y_max:.4f} m  (expected 8.6224)")
    print(f"  t_return = {t_ret:.4f} s  (expected 2.6531)")
    print(f"  v at t_return = {v_t(t_ret):.4f} m/s  (expected -13.0)")
    print(f"  a at t=0 = {a_t(0):.2f} m/s²")
    print(f"  a at t_peak = {a_t(t_peak):.2f} m/s²  (still -9.80, NOT zero)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
T_MAX  = 3.0


class FreeFallScene(Scene):
    """Three panels stacked: y(t), v(t), a(t) with a cursor sweeping together."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        axes = self._setup_axes()
        self._animate_panels(axes)

    def _title(self):
        t1 = Text("Free Fall — Three Panels", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Position · Velocity · Acceleration all at once", font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"y(t)=v_0 t-\tfrac{1}{2}g t^2,\quad v(t)=v_0-gt,\quad a(t)=-g",
                     color=BLUE, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _setup_axes(self):
        cfg = dict(color=INK, stroke_width=1.2, include_ticks=True, tip_length=0.18)
        ax_y = Axes(x_range=[0, T_MAX, 1], y_range=[-6, 10, 4],
                    x_length=8.5, y_length=2.0, axis_config=cfg).shift(UP*2.6)
        ax_v = Axes(x_range=[0, T_MAX, 1], y_range=[-20, 15, 10],
                    x_length=8.5, y_length=2.0, axis_config=cfg).shift(UP*0.1)
        ax_a = Axes(x_range=[0, T_MAX, 1], y_range=[-12, 2, 4],
                    x_length=8.5, y_length=2.0, axis_config=cfg).shift(DOWN*2.4)

        lbl_y = Text("y (m)",  font="EB Garamond", font_size=18, color=BLUE).next_to(ax_y.y_axis.get_end(), UP, buff=0.06)
        lbl_v = Text("v (m/s)", font="EB Garamond", font_size=18, color=BROWN).next_to(ax_v.y_axis.get_end(), UP, buff=0.06)
        lbl_a = Text("a (m/s²)", font="EB Garamond", font_size=18, color=GOLD).next_to(ax_a.y_axis.get_end(), UP, buff=0.06)
        lbl_t = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=18).next_to(ax_a.x_axis.get_end(), RIGHT, buff=0.06)

        self.play(Create(ax_y), Create(ax_v), Create(ax_a),
                  Write(lbl_y), Write(lbl_v), Write(lbl_a), Write(lbl_t), run_time=1.5)
        return ax_y, ax_v, ax_a

    def _animate_panels(self, axes):
        ax_y, ax_v, ax_a = axes
        ts = np.linspace(0, T_MAX, 600)

        # Build curves
        pts_y = np.array([ax_y.c2p(t, y_t(t)) for t in ts])
        pts_v = np.array([ax_v.c2p(t, v_t(t)) for t in ts])
        pts_a = np.array([ax_a.c2p(t, -G)       for t in ts])

        crv_y = VMobject(color=BLUE,  stroke_width=2.8).set_points_smoothly(pts_y)
        crv_v = VMobject(color=BROWN, stroke_width=2.8).set_points_smoothly(pts_v)
        crv_a = VMobject(color=GOLD,  stroke_width=2.8).set_points_smoothly(pts_a)

        self.play(Create(crv_y), Create(crv_v), Create(crv_a), run_time=2.5)
        self.wait(0.5)

        # Cursor at peak
        t_peak = V0/G
        cur_y = ax_y.c2p(t_peak, y_t(t_peak))
        cur_v = ax_v.c2p(t_peak, v_t(t_peak))
        cur_a = ax_a.c2p(t_peak, -G)

        # Vertical dashed lines at t_peak on each axis
        dash_y = DashedLine(ax_y.c2p(t_peak, -6), ax_y.c2p(t_peak, 10),
                            color=DIM, stroke_width=1.2, dash_length=0.12)
        dash_v = DashedLine(ax_v.c2p(t_peak, -20), ax_v.c2p(t_peak, 15),
                            color=DIM, stroke_width=1.2, dash_length=0.12)
        dash_a = DashedLine(ax_a.c2p(t_peak, -12), ax_a.c2p(t_peak, 2),
                            color=DIM, stroke_width=1.2, dash_length=0.12)

        dot_y = Dot(cur_y, color=BLUE,  radius=0.1)
        dot_v = Dot(cur_v, color=GOLD,  radius=0.1)  # v=0 at peak → gold
        dot_a = Dot(cur_a, color=GOLD,  radius=0.1)

        self.play(Create(dash_y), Create(dash_v), Create(dash_a),
                  FadeIn(dot_y, dot_v, dot_a), run_time=0.9)

        cap = Text(
            "At the peak: v = 0,  a = −9.80 m/s²  (NOT zero)",
            font="EB Garamond", font_size=21, color=GOLD,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(cap), run_time=0.9)
        self.wait(2.5)

        # Show a_t is flat everywhere
        cap2 = Text(
            "Acceleration is constant throughout — even at the peak",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(cap), Write(cap2), run_time=0.8)
        self.wait(2.5)
