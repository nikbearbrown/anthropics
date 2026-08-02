#!/usr/bin/env python3
"""
thermo_mb_distribution.py — Maxwell-Boltzmann Distribution: The High-Speed Tail That Mars Loses
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-thermodynamics book.

Render:
    cd physics-plus-one-thermodynamics/youtube/thermo-mb-distribution
    manim -qh thermo_mb_distribution.py MbDistributionScene

Numpy verification:
    python3 thermo_mb_distribution.py

Physics:
    N2 molecule m = 4.65e-26 kg, T = 293 K
    v_mp = sqrt(2kT/m)  = 417 m/s
    v_avg = sqrt(8kT/πm) = 471 m/s
    v_rms = sqrt(3kT/m)  = 511 m/s
    Mars escape velocity: v_esc = sqrt(2*g*R) = sqrt(2*3.72*3.39e6) ≈ 5020 m/s
"""
import sys
import numpy as np

# ─── Physics constants ────────────────────────────────────────────────────────
K_B   = 1.381e-23    # J/K Boltzmann
M_N2  = 4.65e-26     # kg  N2 molecule
M_CO2 = 7.31e-26     # kg  CO2 molecule (Mars atmosphere)
G_MARS = 3.72        # m/s² Mars surface gravity
R_MARS = 3.39e6      # m   Mars radius


def mb_distribution(v: np.ndarray, m: float, T: float) -> np.ndarray:
    """Maxwell-Boltzmann speed distribution f(v)."""
    A = 4.0 * np.pi * (m / (2.0 * np.pi * K_B * T)) ** 1.5
    return A * v**2 * np.exp(-m * v**2 / (2.0 * K_B * T))


def characteristic_speeds(m: float, T: float):
    """Return (v_mp, v_avg, v_rms) in m/s."""
    v_mp  = np.sqrt(2.0 * K_B * T / m)
    v_avg = np.sqrt(8.0 * K_B * T / (np.pi * m))
    v_rms = np.sqrt(3.0 * K_B * T / m)
    return v_mp, v_avg, v_rms


def mars_escape_velocity():
    return np.sqrt(2.0 * G_MARS * R_MARS)


if __name__ == "__main__" and "--verify" not in sys.argv:
    print("=== Maxwell-Boltzmann Verification ===")
    v_mp, v_avg, v_rms = characteristic_speeds(M_N2, 293.0)
    print(f"N2 T=293K: v_mp={v_mp:.0f} m/s, v_avg={v_avg:.0f} m/s, v_rms={v_rms:.0f} m/s")
    print(f"  v_rms/v_mp = {v_rms/v_mp:.4f}  (expect {np.sqrt(3/2):.4f})")
    v_esc = mars_escape_velocity()
    print(f"Mars v_esc = {v_esc:.0f} m/s")
    # P1: ratio check
    assert abs(v_rms/v_mp - np.sqrt(1.5)) < 1e-4, "P1 FAIL"
    # P2: doubling T doubles v_mp (sqrt factor)
    v_mp2, _, _ = characteristic_speeds(M_N2, 4 * 293.0)
    assert abs(v_mp2 / v_mp - 2.0) < 1e-4, "P2 FAIL"
    print(f"P2: v_mp at 4T = {v_mp2:.0f} m/s (expect {2*v_mp:.0f})")
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


class MbDistributionScene(Scene):
    """Maxwell-Boltzmann distribution with T slider and Mars escape tail."""

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        ax = self._phase_axes()
        self._phase_curve(ax)
        self._phase_slider(ax)

    def _phase_title(self):
        title = Text("Maxwell-Boltzmann Distribution", font="EB Garamond",
                     font_size=56, color=INK)
        sub = Text("The high-speed tail that Mars loses — one molecule at a time",
                   font="EB Garamond", font_size=23, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0, 1800, 300],
            y_range=[0, 2.8e-3, 1e-3],
            x_length=9.5,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)

        x_lbl = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"f(v)", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        self._ax = ax
        return ax

    def _phase_curve(self, ax):
        T0 = 293.0
        v_arr = np.linspace(1, 1700, 600)
        f_arr = mb_distribution(v_arr, M_N2, T0)

        pts = [ax.c2p(v, f) for v, f in zip(v_arr, f_arr)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)

        v_mp, v_avg, v_rms = characteristic_speeds(M_N2, T0)
        f_at_mp = mb_distribution(np.array([v_mp]), M_N2, T0)[0]

        def vline(v, col, lbl_tex, side=RIGHT):
            top = ax.c2p(v, f_at_mp * 1.05)
            bot = ax.c2p(v, 0)
            line = DashedLine(bot, top, color=col, stroke_width=1.5)
            lbl = MathTex(lbl_tex, color=col, font_size=22).next_to(
                ax.c2p(v, f_at_mp * 1.12), side, buff=0.05)
            return VGroup(line, lbl)

        ln_mp  = vline(v_mp,  BLUE,  r"v_{\rm mp}")
        ln_avg = vline(v_avg, GOLD,  r"v_{\rm avg}", UP)
        ln_rms = vline(v_rms, BROWN, r"v_{\rm rms}")

        # Mars escape line
        v_esc = mars_escape_velocity()
        esc_line = DashedLine(
            ax.c2p(v_esc, 0), ax.c2p(v_esc, f_at_mp * 0.8),
            color=BROWN, stroke_width=1.2,
        )
        esc_lbl = Text("Mars v_esc = 5020 m/s", font="EB Garamond",
                       font_size=18, color=BROWN).next_to(
            ax.c2p(v_esc, f_at_mp * 0.82), UP, buff=0.05)

        # Shade escape tail
        v_tail = np.linspace(v_esc, 1700, 200)
        f_tail = mb_distribution(v_tail, M_N2, T0)
        tail_pts = ([ax.c2p(v_esc, 0)]
                    + [ax.c2p(v, f) for v, f in zip(v_tail, f_tail)]
                    + [ax.c2p(1700, 0)])
        tail_fill = Polygon(*tail_pts, color=BROWN,
                            fill_color=BROWN, fill_opacity=0.35, stroke_width=0)

        hdr = Text("N₂ at T = 293 K", font="EB Garamond",
                   font_size=22, color=BLUE).to_edge(UP, buff=0.2)

        self.play(Write(hdr), run_time=0.5)
        self.play(Create(curve), run_time=2.0)
        self.play(Create(ln_mp), Create(ln_avg), Create(ln_rms), run_time=1.5)
        self.play(Create(esc_line), Write(esc_lbl), run_time=1.0)
        self.play(FadeIn(tail_fill), run_time=0.8)
        cap = MathTex(
            r"f(v)=4\pi\!\left(\tfrac{m}{2\pi kT}\right)^{3/2}v^2\,e^{-mv^2/2kT}",
            color=INK, font_size=26).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(hdr, curve, ln_mp, ln_avg, ln_rms,
                          esc_line, esc_lbl, tail_fill, cap), run_time=0.5)
        self._f_at_mp_ref = f_at_mp

    def _phase_slider(self, ax):
        tc = ValueTracker(293.0)

        def _curve():
            T = tc.get_value()
            v_arr = np.linspace(1, 1700, 400)
            f_arr = mb_distribution(v_arr, M_N2, T)
            pts = [ax.c2p(v, f) for v, f in zip(v_arr, f_arr)]
            m = VMobject(color=BLUE, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        def _vlines():
            T = tc.get_value()
            v_mp, v_avg, v_rms = characteristic_speeds(M_N2, T)
            f_pk = mb_distribution(np.array([v_mp]), M_N2, T)[0]
            grp = VGroup()
            for v, col in [(v_mp, BLUE), (v_avg, GOLD), (v_rms, BROWN)]:
                if v < 1700:
                    ln = DashedLine(ax.c2p(v, 0), ax.c2p(v, f_pk * 1.05),
                                    color=col, stroke_width=1.5)
                    grp.add(ln)
            return grp

        dyn_curve  = always_redraw(_curve)
        dyn_vlines = always_redraw(_vlines)

        t_lbl = MathTex(r"T = ", color=DIM, font_size=30)
        t_num = DecimalNumber(293.0, num_decimal_places=0, color=DIM, font_size=30)
        t_K   = MathTex(r"\mathrm{K}", color=DIM, font_size=30)
        t_num.add_updater(lambda m: m.set_value(tc.get_value()))
        t_row = VGroup(t_lbl, t_num, t_K).arrange(RIGHT, buff=0.08)
        t_row.to_edge(DOWN, buff=0.28)

        hdr = Text("Raise T — the tail grows, escape fraction rises",
                   font="EB Garamond", font_size=20, color=INK).to_edge(UP, buff=0.18)

        self.add(dyn_curve, dyn_vlines)
        self.play(Write(hdr), FadeIn(t_row), run_time=0.8)
        self.play(tc.animate.set_value(1200.0), run_time=5.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("Hotter Mars → bigger escape tail → faster atmosphere loss",
                     font="EB Garamond", font_size=24, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(t_row), Write(final), run_time=1.2)
        self.wait(2.5)
