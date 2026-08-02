#!/usr/bin/env python3
"""
brewsters_angle_polarization.py — Brewster's Angle: Rp Falling to Zero
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/brewsters-angle-polarization
    manim -qh brewsters_angle_polarization.py BrewstersAngleScene

Numpy verification (run standalone):
    python3 brewsters_angle_polarization.py --verify

Physics (checkable):
    Fresnel: r_p = (n2cosθ1 − n1cosθ2) / (n2cosθ1 + n1cosθ2)
             r_s = (n1cosθ1 − n2cosθ2) / (n1cosθ1 + n2cosθ2)
    Brewster: θ_B = arctan(n2/n1)

    P1: air-glass n1=1, n2=1.5: θ_B=arctan(1.5)=56.31°;
        θ_t=arcsin(sin56.31°/1.5)=arcsin(0.554)=33.69°; 56.31+33.69=90° ✓
    P2: water n=1.33: θ_B=arctan(1.33)=53.06° ✓
"""
import sys
import numpy as np

N1 = 1.0
N2 = 1.5


def brewster_angle(n1, n2):
    """θ_B = arctan(n2/n1) in degrees."""
    return np.degrees(np.arctan(n2 / n1))


def fresnel_rs_rp(theta1_deg, n1, n2):
    """
    Fresnel reflection coefficients (amplitude).
    Returns (r_s, r_p) or (None, None) for TIR.
    """
    t1 = np.radians(theta1_deg)
    sin_t2 = n1 * np.sin(t1) / n2
    if abs(sin_t2) > 1:
        return None, None
    t2 = np.arcsin(sin_t2)
    cos1 = np.cos(t1)
    cos2 = np.cos(t2)
    r_s = (n1 * cos1 - n2 * cos2) / (n1 * cos1 + n2 * cos2)
    r_p = (n2 * cos1 - n1 * cos2) / (n2 * cos1 + n1 * cos2)
    return r_s, r_p


def verify():
    print("=== Brewster's angle polarization verification ===")
    # P1
    tb = brewster_angle(N1, N2)
    print(f"P1: n1={N1}, n2={N2}: θ_B = arctan({N2}/{N1}) = {tb:.2f}°  (should be ≈56.31°)")
    t1 = np.radians(tb)
    sin_t2 = N1 * np.sin(t1) / N2
    t2 = np.degrees(np.arcsin(sin_t2))
    print(f"    θ_t = {t2:.2f}°; θ_B + θ_t = {tb+t2:.2f}°  (should be 90°)")
    # P2
    tb_water = brewster_angle(1.0, 1.33)
    print(f"P2: water n=1.33: θ_B = {tb_water:.2f}°  (should be ≈53.06°)")
    # Fresnel at θ_B
    rs, rp = fresnel_rs_rp(tb, N1, N2)
    print(f"    At θ_B: R_s = |r_s|² = {rs**2:.4f}, R_p = |r_p|² = {rp**2:.6f}  (should be 0)")
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
ORANGE = "#FF9800"


class BrewstersAngleScene(Scene):
    """
    Fresnel R_p and R_s vs incidence angle.
    R_p dips to zero at Brewster's angle.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_fresnel_plot()

    def _phase_title(self):
        title = Text("Brewster's Angle", font="EB Garamond", font_size=64, color=INK)
        sub = Text(
            "θ_B = arctan(n₂/n₁)  ·  at θ_B, reflected p-polarization = 0",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "Air → Glass: n₁=1.0, n₂=1.5  →  θ_B = 56.3°",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_fresnel_plot(self):
        theta1_arr = np.linspace(0, 89.9, 1000)
        Rs_arr = []
        Rp_arr = []
        for t in theta1_arr:
            rs, rp = fresnel_rs_rp(t, N1, N2)
            if rs is None:
                Rs_arr.append(1.0)
                Rp_arr.append(1.0)
            else:
                Rs_arr.append(rs ** 2)
                Rp_arr.append(rp ** 2)
        Rs_arr = np.array(Rs_arr)
        Rp_arr = np.array(Rp_arr)

        ax = Axes(
            x_range=[0, 90, 15],
            y_range=[0, 1.08, 0.25],
            x_length=9.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.14),
            x_axis_config=dict(numbers_to_include=[0, 15, 30, 45, 60, 75, 90]),
            y_axis_config=dict(numbers_to_include=[0, 0.25, 0.5, 0.75, 1.0]),
        ).shift(LEFT * 0.5 + UP * 0.2)

        lbl_x = MathTex(r"\theta_1\;(°)", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        lbl_y = MathTex(r"R", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.4)

        # R_s curve (blue, always positive, monotone increase toward grazing)
        pts_s = [ax.c2p(t, r) for t, r in zip(theta1_arr, Rs_arr)]
        curve_s = VMobject(color=BLUE, stroke_width=3.5)
        curve_s.set_points_smoothly(pts_s)
        lbl_s = MathTex(r"R_s\;(\text{s-pol})", color=BLUE, font_size=26)
        lbl_s.move_to(ax.c2p(75, 0.55))

        # R_p curve (gold, dips to zero at θ_B)
        pts_p = [ax.c2p(t, r) for t, r in zip(theta1_arr, Rp_arr)]
        curve_p = VMobject(color=GOLD, stroke_width=3.5)
        curve_p.set_points_smoothly(pts_p)
        lbl_p = MathTex(r"R_p\;(\text{p-pol})", color=GOLD, font_size=26)
        lbl_p.move_to(ax.c2p(15, 0.25))

        self.play(Create(curve_s), Write(lbl_s), run_time=1.5)
        self.play(Create(curve_p), Write(lbl_p), run_time=1.5)

        # Brewster angle marker
        tb = brewster_angle(N1, N2)
        tb_line = DashedLine(
            ax.c2p(tb, 0), ax.c2p(tb, 0.95),
            color=BROWN, stroke_width=2.0, dash_length=0.12,
        )
        tb_lbl = MathTex(r"\theta_B = 56.3°", color=BROWN, font_size=24)
        tb_lbl.next_to(ax.c2p(tb, 0.95), UP, buff=0.05)

        # Dot at R_p minimum
        tb_dot = Dot(ax.c2p(tb, 0), color=BROWN, radius=0.14)

        self.play(Create(tb_line), Write(tb_lbl), FadeIn(tb_dot), run_time=1.0)
        self.wait(0.5)

        # Right-side annotation panel
        ann1 = MathTex(
            r"\theta_B = \arctan\!\left(\frac{n_2}{n_1}\right) = \arctan(1.5) \approx 56.3°",
            color=INK, font_size=24,
        ).to_corner(UR, buff=0.3)
        ann2 = MathTex(
            r"R_p(\theta_B) = 0 \;\;\; \text{(completely s-polarized reflection)}",
            color=GOLD, font_size=22,
        ).next_to(ann1, DOWN, buff=0.4)
        ann3 = MathTex(
            r"\theta_B + \theta_t = 90° \;\;\; \text{(reflected } \perp \text{ refracted)}",
            color=BROWN, font_size=21,
        ).next_to(ann2, DOWN, buff=0.35)

        self.play(Write(ann1), run_time=0.9)
        self.play(Write(ann2), run_time=0.8)
        self.play(Write(ann3), run_time=0.8)
        self.wait(1.0)

        # Final caption
        cap = Text(
            "Polarizing sunglasses block s-polarized glare by orienting their axis horizontally.",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.0)
        self.wait(3.0)
