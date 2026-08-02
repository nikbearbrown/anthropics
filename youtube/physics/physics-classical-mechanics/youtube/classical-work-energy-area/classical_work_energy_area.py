#!/usr/bin/env python3
"""
classical_work_energy_area.py — Work-Energy Theorem: Area Under F-x = KE Gain
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    F(x) = 10 + 5x  N, m=2.0 kg, starts at rest
    W = ∫₀⁴(10+5x)dx = 80 J → v_f = 8.94 m/s
    At x=2.0 m: W=30 J, v=5.48 m/s

Render:
    cd physics-classical-mechanics/youtube/classical-work-energy-area
    manim -qh classical_work_energy_area.py WorkEnergyAreaScene
"""
import sys
import numpy as np

M  = 2.0   # kg
X_MAX = 4.0

def F(x): return 10 + 5*x

def work(x): return 10*x + 2.5*x**2

def vel(x): return np.sqrt(2*work(x)/M)


def verify():
    print("=== Work-Energy Area verification ===")
    for x in [0, 1, 2, 3, 4]:
        W = work(x)
        v = vel(x) if x > 0 else 0.0
        print(f"  x={x:.1f} m: F={F(x):.1f} N, W={W:.2f} J, v={v:.4f} m/s")
    # P1: x=2.0 m
    assert abs(work(2.0) - 30.0) < 1e-8, "P1 W(2m)"
    assert abs(vel(2.0) - np.sqrt(30)) < 1e-8, "P1 v(2m)"
    print(f"  P1: W(2m)={work(2.0):.2f} J, v(2m)={vel(2.0):.4f} m/s  (expected {np.sqrt(30):.4f})")
    # Spring: k=200, x=0.30 m → W=9 J → v=3 m/s
    k, xs = 200, 0.30
    W_s = 0.5*k*xs**2
    v_s = np.sqrt(2*W_s/M)
    print(f"  Spring: W={W_s:.2f} J, v={v_s:.4f} m/s  (expected 3.0000)")
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


class WorkEnergyAreaScene(Scene):
    """F(x) graph with filling area + live KE gauge."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._variable_force()
        self._spring_comparison()

    def _title(self):
        t1 = Text("Work-Energy Theorem", font="EB Garamond", font_size=58, color=INK)
        t2 = Text("Area under the F-x curve IS the kinetic energy gained",
                  font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"W_{\rm net} = \int F\,dx = \Delta KE", color=GOLD, font_size=36)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _variable_force(self):
        ax = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 35, 10],
            x_length=8,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3).shift(LEFT*1.5)

        ax_ke = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 90, 20],
            x_length=3.5,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.2, include_ticks=True, tip_length=0.15),
        ).shift(DOWN*0.3).shift(RIGHT*4.2)

        lx = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"F\;(\mathrm{N})", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        lx2 = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=18).next_to(ax_ke.x_axis.get_end(), RIGHT, buff=0.05)
        ly2 = MathTex(r"KE\;(\mathrm{J})", color=INK, font_size=18).next_to(ax_ke.y_axis.get_end(), UP, buff=0.05)
        hdr = Text("F(x) = 10 + 5x  N  (m = 2.0 kg)",
                   font="EB Garamond", font_size=18, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Create(ax_ke), Write(lx), Write(ly), Write(lx2), Write(ly2), Write(hdr), run_time=1.2)

        # F curve
        xs = np.linspace(0, X_MAX, 200)
        Fs = F(xs)
        pts_F = np.array([ax.c2p(x, f) for x, f in zip(xs, Fs)])
        crv_F = VMobject(color=BLUE, stroke_width=2.8).set_points_smoothly(pts_F)
        self.play(Create(crv_F), run_time=1.5)

        # Fill area progressively
        xs_fill = np.linspace(0, X_MAX, 80)
        fill_pts = (
            [ax.c2p(0, 0)]
            + [ax.c2p(x, F(x)) for x in xs_fill]
            + [ax.c2p(X_MAX, 0)]
        )
        fill = Polygon(*fill_pts, color=GOLD, fill_color=GOLD, fill_opacity=0.3, stroke_width=0)
        self.play(FadeIn(fill), run_time=1.5)

        # KE curve
        ws = work(xs)
        pts_ke = np.array([ax_ke.c2p(x, w) for x, w in zip(xs, ws)])
        crv_ke = VMobject(color=GOLD, stroke_width=2.5).set_points_smoothly(pts_ke)
        self.play(Create(crv_ke), run_time=1.5)

        # Mark x=2 m
        d_F  = Dot(ax.c2p(2.0, F(2.0)),   color=BROWN, radius=0.1)
        d_ke = Dot(ax_ke.c2p(2.0, work(2.0)), color=BROWN, radius=0.1)
        lbl2 = MathTex(r"x=2\,\mathrm{m}:\;W=30\,\mathrm{J},\;v=5.48\,\mathrm{m/s}",
                       color=BROWN, font_size=18).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(d_F, d_ke), Write(lbl2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _spring_comparison(self):
        ax = Axes(
            x_range=[0, 0.35, 0.1],
            y_range=[0, 65, 20],
            x_length=8,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3)
        lx = MathTex(r"x\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"F=kx\;(\mathrm{N})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Spring F = kx = 200x  (triangular area = ½kx²)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        xs = np.linspace(0, 0.30, 200)
        Fs = 200*xs
        pts_F = np.array([ax.c2p(x, f) for x, f in zip(xs, Fs)])
        crv_F = VMobject(color=BLUE, stroke_width=2.8).set_points_smoothly(pts_F)

        fill_pts = [ax.c2p(0,0)] + [ax.c2p(x,200*x) for x in xs] + [ax.c2p(0.30, 0)]
        fill = Polygon(*fill_pts, color=GOLD, fill_color=GOLD, fill_opacity=0.3, stroke_width=0)

        self.play(Create(crv_F), FadeIn(fill), run_time=1.5)

        W_spring = 0.5*200*0.30**2
        v_spring = np.sqrt(2*W_spring/M)
        ann = MathTex(
            r"W = \tfrac{1}{2}kx^2 = 9.0\,\mathrm{J}\quad v = 3.0\,\mathrm{m/s}",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(ann), run_time=0.8)
        self.wait(2.5)
