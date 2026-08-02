#!/usr/bin/env python3
"""
cm_free_fall.py — Free Fall: Position Parabola and Velocity Line
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    y(t) = h - 0.5 * g * t^2  (drop from rest)
    v(t) = -g * t
    t_fall = sqrt(2*h/g)

Verify: python3 cm_free_fall.py --verify
Render: manim -qh cm_free_fall.py CmFreeFallScene
"""
import sys
import numpy as np

G_GRAV = 9.80    # m/s^2
H0     = 10.0    # m  — drop height

def t_fall(h=H0, g=G_GRAV):
    return np.sqrt(2 * h / g)

def y_of_t(t, h=H0, g=G_GRAV):
    return h - 0.5 * g * t**2

def v_of_t(t, g=G_GRAV):
    return -g * t

def verify():
    print("=== Free fall verification ===")
    tf = t_fall()
    print(f"P1: t_fall from 10 m = {tf:.3f} s  (expected 1.428 s) {'✓' if abs(tf - np.sqrt(20/9.80)) < 0.001 else '✗'}")
    v_impact = abs(v_of_t(tf))
    print(f"P2: v_impact = {v_impact:.3f} m/s  (expected sqrt(2gh)={np.sqrt(2*G_GRAV*H0):.3f} m/s) {'✓' if abs(v_impact - np.sqrt(2*G_GRAV*H0)) < 0.01 else '✗'}")
    # Apollo 15 Moon
    tf_moon = t_fall(H0, 1.62)
    v_moon  = abs(v_of_t(tf_moon, 1.62))
    print(f"Moon: t_fall = {tf_moon:.3f} s, v = {v_moon:.3f} m/s")
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

G_VALS = [
    (9.80, "Earth", BLUE),
    (1.62, "Moon",  GOLD),
    (3.72, "Mars",  BROWN),
]


class CmFreeFallScene(Scene):
    """
    Split screen: left y(t) parabola drawing, right v(t) linear.
    Object falls on left. g slider compares Earth/Moon/Mars.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax_y, ax_v = self._axes()
        self._earth_drop(ax_y, ax_v)
        self._g_comparison(ax_y, ax_v)
        self._finale()

    def _title(self):
        t = Text("Free Fall: Position Parabola and Velocity Line",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "Drop a hammer and a feather in vacuum — they hit simultaneously.\n"
            "Mass cancels out of every free-fall equation.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        tf = t_fall()
        ax_y = Axes(
            x_range=[0, tf + 0.2, 0.5],
            y_range=[0, H0 + 1, 2],
            x_length=5.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(LEFT * 3.2)
        lxy = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax_y.x_axis.get_end(), RIGHT, buff=0.08)
        lyy = MathTex(r"y\;(\mathrm{m})", color=INK, font_size=22).next_to(ax_y.y_axis.get_end(), UP, buff=0.08)
        hdr_y = Text("Position  y(t)", font="EB Garamond", font_size=20, color=DIM).next_to(ax_y, UP, buff=0.1)

        ax_v = Axes(
            x_range=[0, tf + 0.2, 0.5],
            y_range=[-15, 0.5, 5],
            x_length=5.5,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(RIGHT * 3.2)
        lxv = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax_v.x_axis.get_end(), RIGHT, buff=0.08)
        lyv = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=22).next_to(ax_v.y_axis.get_end(), UP, buff=0.08)
        hdr_v = Text("Velocity  v(t)", font="EB Garamond", font_size=20, color=DIM).next_to(ax_v, UP, buff=0.1)

        self.play(Create(ax_y), Create(ax_v),
                  Write(lxy), Write(lyy), Write(lxv), Write(lyv),
                  Write(hdr_y), Write(hdr_v), run_time=1.5)
        return ax_y, ax_v

    def _earth_drop(self, ax_y, ax_v):
        g = G_GRAV
        tf = t_fall(H0, g)
        t_vals = np.linspace(0, tf, 300)

        y_vals = y_of_t(t_vals, H0, g)
        v_vals = v_of_t(t_vals, g)

        y_pts = np.array([ax_y.c2p(t, y) for t, y in zip(t_vals, y_vals)])
        v_pts = np.array([ax_v.c2p(t, v) for t, v in zip(t_vals, v_vals)])

        y_curve = VMobject(color=BLUE, stroke_width=3)
        y_curve.set_points_smoothly(y_pts)
        v_curve = VMobject(color=GOLD, stroke_width=3)
        v_curve.set_points_smoothly(v_pts)

        # Slope annotation on v plot
        slope_lbl = MathTex(r"\mathrm{slope} = -g = -9.80\,\mathrm{m/s}^2", color=GOLD, font_size=20)
        slope_lbl.move_to(ax_v.c2p(0.5, -8))

        # Impact markers
        impact_y = Dot(ax_y.c2p(tf, 0), color=BLUE, radius=0.12)
        impact_v = Dot(ax_v.c2p(tf, -g * tf), color=GOLD, radius=0.12)
        tf_lbl = MathTex(rf"t_f = {tf:.2f}\,\mathrm{{s}}", color=INK, font_size=22)
        tf_lbl.next_to(ax_y.c2p(tf, 0), DR, buff=0.15)
        vi_lbl = MathTex(rf"v_f = {g*tf:.1f}\,\mathrm{{m/s}}", color=INK, font_size=22)
        vi_lbl.next_to(impact_v, DR, buff=0.15)

        self.play(Create(y_curve), Create(v_curve), run_time=2.2)
        self.play(Write(slope_lbl), FadeIn(impact_y), FadeIn(impact_v),
                  Write(tf_lbl), Write(vi_lbl), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(slope_lbl, impact_y, impact_v, tf_lbl, vi_lbl,
                          y_curve, v_curve), run_time=0.4)

    def _g_comparison(self, ax_y, ax_v):
        caption = Text(
            "Same height h = 10 m — different g:",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(caption), run_time=0.6)

        for g, name, col in G_VALS:
            tf = t_fall(H0, g)
            t_vals = np.linspace(0, tf, 200)
            y_vals = y_of_t(t_vals, H0, g)
            v_vals = v_of_t(t_vals, g)

            # Clip v_vals to axis range
            v_vals_clipped = np.clip(v_vals, -14.5, 0.4)
            t_v_clipped = t_vals[:len(v_vals_clipped)]

            y_pts = [ax_y.c2p(t, y) for t, y in zip(t_vals, y_vals) if 0 <= y <= H0 + 0.5]
            v_pts = [ax_v.c2p(t, v) for t, v in zip(t_vals, v_vals) if -14.5 <= v <= 0.4]

            if len(y_pts) > 2:
                yc = VMobject(color=col, stroke_width=2.5)
                yc.set_points_smoothly(np.array(y_pts))
                self.play(Create(yc), run_time=0.8)

            if len(v_pts) > 2:
                vc = VMobject(color=col, stroke_width=2.5)
                vc.set_points_smoothly(np.array(v_pts))
                self.play(Create(vc), run_time=0.5)

            lbl = Text(f"{name} g = {g} m/s²", font="EB Garamond",
                       font_size=18, color=col)
            lbl.next_to(ax_y.c2p(tf * 0.7, H0 * 0.5), RIGHT, buff=0.3)
            self.play(Write(lbl), run_time=0.4)
            self.wait(0.6)

        self.wait(2.0)
        self.play(FadeOut(caption), run_time=0.3)

    def _finale(self):
        eq = MathTex(
            r"y(t) = h - \tfrac{1}{2}g t^2",
            r"\quad v(t) = -gt",
            r"\quad t_f = \sqrt{2h/g}",
            color=INK, font_size=30,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
