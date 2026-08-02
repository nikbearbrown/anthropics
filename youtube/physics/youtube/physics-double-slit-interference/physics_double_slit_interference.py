#!/usr/bin/env python3
"""
physics_double_slit_interference.py — Young's Double-Slit: Fringe Pattern
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    λ = 633 nm, d = 0.10 mm, L = 2.00 m
    Δy = λL/d = 1.27 cm
    y_m = mλL/d

Render:
    cd physics/youtube/physics-double-slit-interference
    manim -qh physics_double_slit_interference.py DoubleSlitScene
"""
import sys
import numpy as np

LAM = 633e-9   # m (red laser)
D   = 1e-4     # m (slit separation)
L   = 2.00     # m (screen distance)


def fringe_spacing():
    return LAM * L / D


def fringe_pos(m):
    return m * LAM * L / D


def verify():
    print("=== Double-Slit Interference verification ===")
    dy = fringe_spacing()
    print(f"  Δy = λL/d = {dy*100:.4f} cm  (expected 1.2660 cm)")
    for m in [-2, -1, 0, 1, 2]:
        y = fringe_pos(m) * 100  # cm
        print(f"  m={m:+d}: y = {y:.4f} cm")
    # P1: Δy = 1.27 cm
    assert abs(dy - 0.01266) < 1e-5, f"P1: {dy}"
    # P2: violet λ=400 nm
    dy_v = 400e-9 * L / D * 100
    print(f"  Violet (400nm): Δy = {dy_v:.4f} cm")
    ratio = dy_v / (dy*100)
    print(f"  Ratio Δy_violet/Δy_red = {ratio:.4f}  (expected 0.6319 = 400/633)")
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


class DoubleSlitScene(Scene):
    """Wavefronts expand from two slits, interference pattern builds on screen."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._wave_diagram()
        self._screen_pattern()

    def _title(self):
        t1 = Text("Young's Double-Slit", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Interference emerges from path-difference geometry", font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"\Delta y = \frac{\lambda L}{d} = 1.27\,\mathrm{cm}", color=GOLD, font_size=34)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _wave_diagram(self):
        """Schematic: two slits + expanding circular arcs."""
        # Slit positions
        s1 = np.array([-4.5,  0.5, 0])
        s2 = np.array([-4.5, -0.5, 0])

        dot1 = Dot(s1, color=BLUE, radius=0.10)
        dot2 = Dot(s2, color=BLUE, radius=0.10)
        lbl1 = Text("slit 1", font="EB Garamond", font_size=16, color=DIM).next_to(dot1, LEFT, buff=0.1)
        lbl2 = Text("slit 2", font="EB Garamond", font_size=16, color=DIM).next_to(dot2, LEFT, buff=0.1)
        self.play(FadeIn(dot1, dot2, lbl1, lbl2), run_time=0.6)

        # Expanding arcs from each slit
        all_arcs = []
        for slit, col in [(s1, BLUE), (s2, BROWN)]:
            for r in [0.6, 1.1, 1.6, 2.1, 2.6]:
                arc = Arc(radius=r, start_angle=-PI/2.5, angle=PI/1.25,
                          color=col, stroke_width=1.5, stroke_opacity=0.6)
                arc.shift(slit)
                all_arcs.append(arc)

        self.play(*[Create(a) for a in all_arcs], run_time=2.0)

        # Screen on right
        screen = Line(UP*3.2, DOWN*3.2, color=DIM, stroke_width=3)
        screen.move_to(RIGHT*4.5)
        self.play(Create(screen), run_time=0.5)

        # Bright fringes on screen (schematic dots)
        dy_screen = 0.55  # scaled for display
        for m in range(-4, 5):
            y = m * dy_screen
            col = GOLD if abs(m) < 3 else DIM
            dot = Dot(np.array([4.5, y, 0]), color=col,
                      radius=0.09 if abs(m) < 3 else 0.06)
            self.play(FadeIn(dot), run_time=0.12)

        hdr = Text(
            "Bright fringes where path difference = 0, λ, 2λ …",
            font="EB Garamond", font_size=20, color=GOLD,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(hdr), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _screen_pattern(self):
        """Fringe-spacing formula + wavelength comparison."""
        ax = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.3],
            x_length=10,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.4)
        lx = MathTex(r"y\;(\mathrm{cm})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("Intensity", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Fringe intensity on screen  (λ=633 nm, d=0.1 mm, L=2 m)",
                   font="EB Garamond", font_size=18, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        def intensity(y_cm, lam_nm):
            lam = lam_nm * 1e-9
            dy = lam * L / D   # m
            y_m = y_cm * 0.01
            phase = np.pi * D * y_m / (lam * L)
            return np.cos(phase)**2

        ys_cm = np.linspace(-4, 4, 800)

        # Red
        I_red = intensity(ys_cm, 633)
        pts_red = np.array([ax.c2p(y, I) for y, I in zip(ys_cm, I_red)])
        crv_red = VMobject(color=BROWN, stroke_width=2.5).set_points_smoothly(pts_red)

        # Violet
        I_vio = intensity(ys_cm, 400)
        pts_vio = np.array([ax.c2p(y, I) for y, I in zip(ys_cm, I_vio)])
        crv_vio = VMobject(color=BLUE, stroke_width=2.5).set_points_smoothly(pts_vio)

        self.play(Create(crv_red), run_time=1.5)
        lbl_red = Text("λ = 633 nm  Δy = 1.27 cm", font="EB Garamond", font_size=18, color=BROWN)
        lbl_red.to_edge(DOWN, buff=0.50)
        self.play(Write(lbl_red), run_time=0.5)
        self.wait(1.0)

        self.play(Create(crv_vio), run_time=1.5)
        lbl_vio = Text("λ = 400 nm  Δy = 0.80 cm  (ratio 0.632 = 400/633)",
                       font="EB Garamond", font_size=18, color=BLUE)
        lbl_vio.to_edge(DOWN, buff=0.22)
        self.play(Write(lbl_vio), run_time=0.5)

        final = Text(
            "Fringe spacing scales linearly with wavelength — Young measured λ from geometry alone",
            font="EB Garamond", font_size=19, color=GOLD,
        ).to_edge(DOWN, buff=0.22)
        self.wait(1.5)
        self.play(FadeOut(lbl_red, lbl_vio), Write(final), run_time=1.0)
        self.wait(2.5)
