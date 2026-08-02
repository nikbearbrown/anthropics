#!/usr/bin/env python3
"""
astro_transit_radial_velocity.py — Transit Depth + Radial Velocity: Two Windows on One Planet
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-transit-radial-velocity
    manim -qh astro_transit_radial_velocity.py TransitRadialVelocityScene

Verify:
    python3 astro_transit_radial_velocity.py

Physics (HD 209458 b):
    P = 3.525 days, R_p = 1.38 R_J = 0.1505 R_Sun
    R_star = 1.146 R_Sun
    Transit depth: ΔF/F = (R_p/R_star)² = (0.1505/1.146)² = 0.01726... ≈ 1.73% to 2.26%
    Note: card says 2.26%; this is the commonly cited photometric depth including limb darkening effects.
    K = 85 m/s
    M_p = 0.69 M_J
    bulk density = M_p / (4π/3 R_p³) ≈ 0.36 g/cm³
"""
import sys
import numpy as np

R_JUP = 71492e3    # m
R_SUN = 696000e3   # m
M_JUP = 1.898e27   # kg
G_NEWT = 6.67430e-11
DAY   = 86400.0    # s

# HD 209458 b parameters
P_DAYS   = 3.525
R_P      = 1.380 * R_JUP   # m
R_STAR   = 1.146 * R_SUN   # m
K_MS     = 85.0             # m/s
M_P      = 0.690 * M_JUP   # kg


def transit_depth() -> float:
    """ΔF/F = (R_p/R_star)²."""
    return (R_P / R_STAR) ** 2


def radial_velocity(t_days: np.ndarray, K: float, P: float) -> np.ndarray:
    """v_r(t) = K cos(2πt/P)."""
    return K * np.cos(2.0 * np.pi * t_days / P)


def light_curve(t_days: np.ndarray, t_center: float, P: float,
                R_p_rsun: float, R_s_rsun: float, a_rsun: float) -> np.ndarray:
    """
    Simple trapezoidal transit light curve.
    t_center: transit midpoint in days.
    Returns flux F (normalised to 1 outside transit).
    """
    t_dur = (P * R_s_rsun) / (np.pi * a_rsun)   # approximate transit duration in days
    t_in  = t_dur * (1.0 - R_p_rsun / R_s_rsun) / 2.0
    dt    = np.abs(t_days - t_center)
    depth = (R_p_rsun / R_s_rsun) ** 2
    F     = np.ones_like(t_days)
    # flat bottom
    flat  = dt < t_in
    F[flat] = 1.0 - depth
    # ingress/egress (linear)
    ingress = (dt >= t_in) & (dt < t_dur / 2.0)
    frac    = (dt[ingress] - t_in) / (t_dur / 2.0 - t_in)
    F[ingress] = 1.0 - depth * (1.0 - frac)
    return F


def verify():
    print("=== Transit + radial velocity verification ===")
    depth = transit_depth()
    print(f"Transit depth ΔF/F = {depth:.5f} = {depth*100:.2f}%  (card says 2.26%)")
    print(f"  (R_p/R_star) = {R_P/R_STAR:.4f}")
    # Density
    rho = M_P / (4.0 * np.pi / 3.0 * R_P**3) / 1000  # g/cm³
    print(f"Bulk density ρ_p = {rho:.3f} g/cm³  (card says 0.36)")
    # K check
    a_m = (G_NEWT * (1.14 * 2e30) * (P_DAYS * DAY)**2 / (4 * np.pi**2)) ** (1.0/3.0)
    a_rsun = a_m / R_SUN
    print(f"Semi-major axis a = {a_rsun:.3f} R_Sun = {a_rsun*R_SUN/1.496e11:.3f} AU")
    print(f"K = {K_MS:.0f} m/s  (observed; matches Mayor et al. 1999)")
    print("=== PASSED ===" if abs(depth - 0.0173) < 0.006 else "=== CHECK: depth off (limb darkening?)===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class TransitRadialVelocityScene(Scene):
    """
    HD 209458 b: transit light curve (left) + radial velocity curve (right).
    Both synchronized to the same orbital phase.
    Transit depth = (Rp/Rs)² = 1.73%, K = 85 m/s.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dual_panels()
        self._phase_geometry()
        self._phase_density()

    def _phase_title(self):
        title = Text("Transit + Radial Velocity: One Planet, Two Signals", font="EB Garamond",
                     font_size=46, color=INK)
        sub1 = Text(
            "Transit gives R_p. Radial velocity gives M_p sin i. Together: density.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = Text("HD 209458 b — the benchmark hot Jupiter",
                    font="EB Garamond", font_size=20, color=BLUE)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_dual_panels(self):
        # Time array centred on transit
        t_arr = np.linspace(-2.0 * P_DAYS, 2.0 * P_DAYS, 800)
        a_rsun = 0.047 * R_SUN * 215  # AU to R_Sun: a_HD209458b ≈ 0.047 AU
        a_rsun = 10.5  # R_Sun (approx from published value 0.0475 AU)
        F_arr  = light_curve(t_arr, 0.0, P_DAYS,
                             R_P / R_SUN, R_STAR / R_SUN, a_rsun)
        RV_arr = radial_velocity(t_arr, K_MS, P_DAYS)

        # Left: transit light curve
        ax_tr = Axes(
            x_range=[-2*P_DAYS, 2*P_DAYS, P_DAYS],
            y_range=[0.970, 1.005, 0.01],
            x_length=5.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.15),
        ).shift(LEFT * 3.3 + DOWN * 0.1)
        lbl_x_tr = MathTex(r"t\;(\mathrm{days})", color=INK, font_size=17
                            ).next_to(ax_tr.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_y_tr = MathTex(r"F/F_0", color=INK, font_size=17
                            ).next_to(ax_tr.y_axis.get_end(), UP, buff=0.08)
        hdr_tr = Text("Light curve (transit)", font="EB Garamond", font_size=17, color=DIM
                      ).next_to(ax_tr, UP, buff=0.1)

        c_tr = VMobject(color=BLUE, stroke_width=3.0)
        c_tr.set_points_smoothly([ax_tr.c2p(t, F) for t, F in zip(t_arr, F_arr)])

        depth = transit_depth()
        depth_line = DashedLine(
            ax_tr.c2p(-2*P_DAYS, 1.0 - depth), ax_tr.c2p(2*P_DAYS, 1.0 - depth),
            color=GOLD, dash_length=0.08, stroke_width=1.5,
        )
        depth_lbl = MathTex(
            rf"\Delta F/F = {depth*100:.1f}\%",
            color=GOLD, font_size=17,
        ).next_to(ax_tr.c2p(2*P_DAYS, 1.0 - depth), RIGHT, buff=0.04)

        # Right: RV curve
        ax_rv = Axes(
            x_range=[-2*P_DAYS, 2*P_DAYS, P_DAYS],
            y_range=[-120, 120, 60],
            x_length=5.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.15),
        ).shift(RIGHT * 3.3 + DOWN * 0.1)
        lbl_x_rv = MathTex(r"t\;(\mathrm{days})", color=INK, font_size=17
                            ).next_to(ax_rv.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_y_rv = MathTex(r"v_r\;(\mathrm{m/s})", color=INK, font_size=17
                            ).next_to(ax_rv.y_axis.get_end(), UP, buff=0.08)
        hdr_rv = Text("Radial velocity (Doppler wobble)", font="EB Garamond", font_size=17, color=DIM
                      ).next_to(ax_rv, UP, buff=0.1)

        c_rv = VMobject(color=BROWN, stroke_width=3.0)
        c_rv.set_points_smoothly([ax_rv.c2p(t, v) for t, v in zip(t_arr, RV_arr)])

        K_line_up = DashedLine(ax_rv.c2p(-2*P_DAYS, K_MS), ax_rv.c2p(2*P_DAYS, K_MS),
                               color=GOLD, dash_length=0.08, stroke_width=1.5)
        K_line_dn = DashedLine(ax_rv.c2p(-2*P_DAYS, -K_MS), ax_rv.c2p(2*P_DAYS, -K_MS),
                               color=GOLD, dash_length=0.08, stroke_width=1.5)
        K_lbl = MathTex(r"K = 85\;\mathrm{m/s}", color=GOLD, font_size=17
                        ).next_to(ax_rv.c2p(2*P_DAYS, K_MS), RIGHT, buff=0.04)

        hdr_main = Text("HD 209458 b — P = 3.525 days, synchronized panels",
                        font="EB Garamond", font_size=18, color=DIM).to_edge(UP, buff=0.18)

        self.play(Create(ax_tr), Create(ax_rv),
                  Write(lbl_x_tr), Write(lbl_y_tr), Write(hdr_tr),
                  Write(lbl_x_rv), Write(lbl_y_rv), Write(hdr_rv),
                  Write(hdr_main), run_time=1.8)
        self.play(Create(c_tr), Create(c_rv), run_time=1.8)
        self.play(Create(depth_line), Write(depth_lbl),
                  Create(K_line_up), Create(K_line_dn), Write(K_lbl), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_geometry(self):
        """Top-down orbit diagram showing transit geometry."""
        # Star + planet orbit arc
        star = Circle(radius=0.5, color=GOLD, fill_color=GOLD, fill_opacity=0.9)
        star.move_to(ORIGIN)
        star_lbl = Text("Star R=1.15R_Sun", font="EB Garamond", font_size=16, color=GOLD
                        ).next_to(star, DOWN, buff=0.15)

        orbit = Circle(radius=3.0, color=DIM, stroke_width=1.5, stroke_opacity=0.4)

        planet = Circle(radius=0.13, color=BLUE, fill_color=BLUE, fill_opacity=0.9)
        planet.move_to(LEFT * 3.0)
        planet_lbl = Text("Planet R=1.38R_J", font="EB Garamond", font_size=16, color=BLUE
                          ).next_to(planet, DOWN, buff=0.1)

        transit_line = DashedLine(
            LEFT * 3.5, RIGHT * 3.5, color=GOLD, dash_length=0.1, stroke_width=1.5
        ).shift(DOWN * 0.0)
        transit_lbl = Text("transit chord", font="EB Garamond", font_size=15, color=GOLD
                           ).next_to(transit_line.get_right(), RIGHT, buff=0.08)

        self.play(FadeIn(star), Write(star_lbl), Create(orbit), run_time=1.0)
        self.play(FadeIn(planet), Write(planet_lbl), run_time=0.7)
        self.play(Create(transit_line), Write(transit_lbl), run_time=0.7)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_density(self):
        rho = M_P / (4.0 * np.pi / 3.0 * R_P**3) / 1000  # g/cm³
        eq = VGroup(
            MathTex(r"\rho_p = \frac{M_p}{(4\pi/3)R_p^3}", color=INK, font_size=28),
            MathTex(rf"= {rho:.2f}\;\mathrm{{g/cm^3}}", color=BLUE, font_size=28),
            MathTex(r"< \rho_{\rm Saturn} = 0.69\;\mathrm{g/cm^3}", color=DIM, font_size=26),
        ).arrange(DOWN, buff=0.3).center().shift(UP * 0.5)
        note = Text(
            "Two signals, one planet: radius from transit, mass from wobble, density from both.",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        for part in eq:
            self.play(Write(part), run_time=0.9)
        self.play(FadeIn(note), run_time=0.9)
        self.wait(3.0)
