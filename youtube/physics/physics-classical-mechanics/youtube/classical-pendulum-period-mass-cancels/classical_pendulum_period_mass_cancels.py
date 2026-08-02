#!/usr/bin/env python3
"""
classical_pendulum_period_mass_cancels.py — Pendulum: Mass Cancels, Only L and g Survive
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    T = 2π√(L/g)  — mass m drops out identically
    L=1.0 m, g=9.80 m/s² → T=2.007 s
    Moon g=1.62 m/s² → T=4.934 s

Render:
    cd physics-classical-mechanics/youtube/classical-pendulum-period-mass-cancels
    manim -qh classical_pendulum_period_mass_cancels.py PendulumPeriodScene
"""
import sys
import numpy as np

G_EARTH = 9.80
G_MOON  = 1.62

def period(L, g=G_EARTH):
    return 2*np.pi*np.sqrt(L/g)

def pendulum_x(L, theta0, t, g=G_EARTH):
    """Small-angle x position of pendulum mass (x from pivot)."""
    omega = np.sqrt(g/L)
    return L * theta0 * np.cos(omega*t)

def pendulum_y(L, theta0, t, g=G_EARTH):
    x = pendulum_x(L, theta0, t, g)
    return -np.sqrt(L**2 - x**2)


def verify():
    print("=== Pendulum Period verification ===")
    for L in [0.25, 1.0, 4.0]:
        T = period(L)
        print(f"  L={L:.2f} m (Earth): T={T:.4f} s")
    # P1: quadrupling L → 2× period
    T1 = period(1.0)
    T4 = period(4.0)
    print(f"  T(4m)/T(1m) = {T4/T1:.6f}  (exact √4 = {np.sqrt(4):.6f})")
    assert abs(T4/T1 - 2.0) < 1e-10, "P1 failed"
    # P2: Moon
    T_moon = period(1.0, G_MOON)
    print(f"  Moon: T={T_moon:.4f} s")
    ratio = T_moon/period(1.0)
    print(f"  T_moon/T_earth = {ratio:.4f}  (expected {np.sqrt(G_EARTH/G_MOON):.4f})")
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

THETA0 = np.radians(10)
L_PEND = 1.0


def pend_pos(t, L=L_PEND, theta0=THETA0, g=G_EARTH, scale=2.0):
    """Manim position of pendulum mass (top = origin)."""
    omega = np.sqrt(g/L)
    theta = theta0 * np.cos(omega*t)
    return scale * np.array([np.sin(theta), -np.cos(theta), 0])


class PendulumPeriodScene(Scene):
    """Side-by-side pendulums: heavy vs light, same period; then Earth vs Moon."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._dual_pendulums()
        self._earth_vs_moon()

    def _title(self):
        t1 = Text("Pendulum Period", font="EB Garamond", font_size=62, color=INK)
        t2 = Text("Mass cancels — only length and g survive",
                  font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"T = 2\pi\sqrt{\frac{L}{g}}", color=BLUE, font_size=44)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _dual_pendulums(self):
        """Heavy ball (blue) vs light (brown), L=1.0 m — same period."""
        pivot_L = np.array([-3.0, 2.5, 0])
        pivot_R = np.array([3.0,  2.5, 0])

        dot_L = Dot(pivot_L, color=DIM, radius=0.08)
        dot_R = Dot(pivot_R, color=DIM, radius=0.08)
        self.play(FadeIn(dot_L, dot_R), run_time=0.3)

        lbl_heavy = Text("Steel ball (heavy)", font="EB Garamond", font_size=18, color=BLUE).next_to(pivot_L, UP, buff=0.1)
        lbl_light = Text("Ping-pong (light)", font="EB Garamond", font_size=18, color=BROWN).next_to(pivot_R, UP, buff=0.1)
        self.play(Write(lbl_heavy), Write(lbl_light), run_time=0.5)

        T = period(L_PEND)
        # Animate 5 full swings
        n_frames = 80
        for i in range(n_frames):
            t = i * (5*T) / n_frames
            pos_L = pivot_L + pend_pos(t, scale=2.0)
            pos_R = pivot_R + pend_pos(t, scale=2.0)
            if i == 0:
                rod_L = Line(pivot_L, pos_L, color=DIM, stroke_width=2)
                rod_R = Line(pivot_R, pos_R, color=DIM, stroke_width=2)
                ball_L = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.85).move_to(pos_L)
                ball_R = Circle(radius=0.15, color=BROWN, fill_color=BROWN, fill_opacity=0.85).move_to(pos_R)
                self.play(FadeIn(rod_L, rod_R, ball_L, ball_R), run_time=0.3)
            else:
                rod_L.put_start_and_end_on(pivot_L, pos_L)
                rod_R.put_start_and_end_on(pivot_R, pos_R)
                ball_L.move_to(pos_L)
                ball_R.move_to(pos_R)
            self.wait(0.04)

        period_lbl = MathTex(r"T = 2.007\,\mathrm{s}\text{ — identical for both}",
                              color=GOLD, font_size=26).to_edge(DOWN, buff=0.22)
        self.play(Write(period_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(rod_L, rod_R, ball_L, ball_R, dot_L, dot_R,
                          lbl_heavy, lbl_light, period_lbl), run_time=0.5)

    def _earth_vs_moon(self):
        """T vs L curve for Earth (blue) and Moon (gold)."""
        ax = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 12, 2],
            x_length=10,
            y_length=5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3)
        lx = MathTex(r"L\;(\mathrm{m})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"T\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Period vs length — Earth vs Moon",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.0)

        Ls = np.linspace(0.05, 4.4, 300)
        T_earth = [period(L) for L in Ls]
        T_moon  = [period(L, G_MOON) for L in Ls]

        pts_e = np.array([ax.c2p(L, T) for L, T in zip(Ls, T_earth)])
        pts_m = np.array([ax.c2p(L, T) for L, T in zip(Ls, T_moon)])

        crv_e = VMobject(color=BLUE, stroke_width=2.8).set_points_smoothly(pts_e)
        crv_m = VMobject(color=GOLD, stroke_width=2.8).set_points_smoothly(pts_m)

        lbl_e = Text("Earth  g=9.80 m/s²", font="EB Garamond", font_size=19, color=BLUE).move_to(ax.c2p(3.5, 4.5))
        lbl_m = Text("Moon   g=1.62 m/s²", font="EB Garamond", font_size=19, color=GOLD).move_to(ax.c2p(2.5, 10))

        self.play(Create(crv_e), Write(lbl_e), run_time=1.5)
        self.play(Create(crv_m), Write(lbl_m), run_time=1.5)

        # Mark L=1.0 m
        d_e = Dot(ax.c2p(1.0, period(1.0)), color=BLUE, radius=0.1)
        d_m = Dot(ax.c2p(1.0, period(1.0, G_MOON)), color=GOLD, radius=0.1)
        lbl_vals = MathTex(r"L=1\,\mathrm{m}:\;2.0\,\mathrm{s\ (Earth)},\;4.9\,\mathrm{s\ (Moon)}",
                           color=INK, font_size=20).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(d_e, d_m), Write(lbl_vals), run_time=0.8)
        self.wait(2.5)
