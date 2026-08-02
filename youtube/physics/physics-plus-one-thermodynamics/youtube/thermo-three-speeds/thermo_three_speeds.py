#!/usr/bin/env python3
"""
thermo_three_speeds.py — Three Speeds: v_mp, v_avg, v_rms on the Maxwell-Boltzmann Curve
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-thermodynamics book.

Render:
    cd physics-plus-one-thermodynamics/youtube/thermo-three-speeds
    manim -qh thermo_three_speeds.py ThreeSpeedsScene

Physics:
    v_mp  = sqrt(2kT/m)
    v_avg = sqrt(8kT/πm) = v_mp * sqrt(4/π)
    v_rms = sqrt(3kT/m)  = v_mp * sqrt(3/2)
    Ratios: 1 : 1.1284 : 1.2247  (independent of T and m)
"""
import sys
import numpy as np

K_B  = 1.381e-23
M_N2 = 4.65e-26


def mb(v, m, T):
    A = 4 * np.pi * (m / (2 * np.pi * K_B * T))**1.5
    return A * v**2 * np.exp(-m * v**2 / (2 * K_B * T))


def three_speeds(m, T):
    v_mp  = np.sqrt(2 * K_B * T / m)
    v_avg = np.sqrt(8 * K_B * T / (np.pi * m))
    v_rms = np.sqrt(3 * K_B * T / m)
    return v_mp, v_avg, v_rms


if __name__ == "__main__":
    print("=== Three Speeds Verification ===")
    v_mp, v_avg, v_rms = three_speeds(M_N2, 293.0)
    print(f"N2 T=293K: v_mp={v_mp:.0f}, v_avg={v_avg:.0f}, v_rms={v_rms:.0f} m/s")
    print(f"Ratios: 1 : {v_avg/v_mp:.4f} : {v_rms/v_mp:.4f}")
    # P1: ratio check
    assert abs(v_rms / v_mp - np.sqrt(1.5)) < 1e-4, "P1 FAIL"
    # P2: √T scaling at 4T
    v_mp2, _, _ = three_speeds(M_N2, 4 * 293.0)
    assert abs(v_mp2 / v_mp - 2.0) < 1e-4, "P2 FAIL"
    print("P2: 4T → v_mp doubles  ✓")
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


class ThreeSpeedsScene(Scene):
    """Maxwell-Boltzmann with v_mp, v_avg, v_rms and T slider."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_static(ax)
        self._phase_slider(ax)

    def _phase_title(self):
        title = Text("Three Characteristic Speeds", font="EB Garamond",
                     font_size=54, color=INK)
        sub = Text(r"v_mp < v_avg < v_rms — three answers to three different questions",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[0, 900, 200],
            y_range=[0, 3.0e-3, 1e-3],
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
        return ax

    def _phase_static(self, ax):
        T0 = 293.0
        v_arr = np.linspace(1, 850, 500)
        f_arr = mb(v_arr, M_N2, T0)

        pts = [ax.c2p(v, f) for v, f in zip(v_arr, f_arr)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)

        v_mp, v_avg, v_rms = three_speeds(M_N2, T0)
        f_pk = mb(np.array([v_mp]), M_N2, T0)[0]

        lines_data = [
            (v_mp,  BLUE,  r"v_{\rm mp}=\sqrt{2kT/m}",     r"417\;\mathrm{m/s}",  UP),
            (v_avg, GOLD,  r"v_{\rm avg}=\sqrt{8kT/\pi m}", r"471\;\mathrm{m/s}",  UP * 1.2),
            (v_rms, BROWN, r"v_{\rm rms}=\sqrt{3kT/m}",     r"511\;\mathrm{m/s}",  UP),
        ]

        hdr = Text("N₂ at T = 293 K", font="EB Garamond",
                   font_size=22, color=BLUE).to_edge(UP, buff=0.22)
        self.play(Write(hdr), Create(curve), run_time=1.8)

        vline_grp = VGroup()
        for v, col, formula, numval, dir_ in lines_data:
            top = ax.c2p(v, f_pk * 1.15)
            bot = ax.c2p(v, 0)
            ln  = DashedLine(bot, top, color=col, stroke_width=2)
            lbl = MathTex(formula, color=col, font_size=20).next_to(top, dir_, buff=0.05)
            nv  = MathTex(numval,  color=col, font_size=19).next_to(
                ax.c2p(v, f_pk * 0.35), RIGHT, buff=0.05)
            self.play(Create(ln), Write(lbl), Write(nv), run_time=0.9)
            vline_grp.add(ln, lbl, nv)

        ratio_eq = MathTex(
            r"1 : \sqrt{4/\pi} : \sqrt{3/2}\;=\;1:1.128:1.225",
            color=INK, font_size=26).to_edge(DOWN, buff=0.28)
        self.play(Write(ratio_eq), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(hdr, curve, vline_grp, ratio_eq), run_time=0.5)

    def _phase_slider(self, ax):
        tc = ValueTracker(293.0)

        def _curve():
            T = tc.get_value()
            v_arr = np.linspace(1, 900, 400)
            f_arr = mb(v_arr, M_N2, T)
            pts = [ax.c2p(v, f) for v, f in zip(v_arr, f_arr)]
            m = VMobject(color=BLUE, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        def _vlines():
            T = tc.get_value()
            vmp, vav, vrms = three_speeds(M_N2, T)
            fpk = mb(np.array([vmp]), M_N2, T)[0]
            grp = VGroup()
            for v, col in [(vmp, BLUE), (vav, GOLD), (vrms, BROWN)]:
                if v < 900:
                    grp.add(DashedLine(ax.c2p(v, 0), ax.c2p(v, fpk * 1.1),
                                       color=col, stroke_width=1.5))
            return grp

        dyn_curve  = always_redraw(_curve)
        dyn_vlines = always_redraw(_vlines)
        self.add(dyn_curve, dyn_vlines)

        t_lbl = MathTex(r"T = ", color=DIM, font_size=30)
        t_num = DecimalNumber(293.0, num_decimal_places=0, color=DIM, font_size=30)
        t_K   = MathTex(r"\mathrm{K}", color=DIM, font_size=30)
        t_num.add_updater(lambda m: m.set_value(tc.get_value()))
        t_row = VGroup(t_lbl, t_num, t_K).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.25)

        hdr = Text("All three speeds scale as √T — ratios stay constant",
                   font="EB Garamond", font_size=21, color=INK).to_edge(UP, buff=0.18)
        self.play(Write(hdr), FadeIn(t_row), run_time=0.8)
        self.play(tc.animate.set_value(1172.0), run_time=5.0, rate_func=smooth)
        self.wait(1.0)
        final = Text("At 4T, all peaks double — confirming the √T law",
                     font="EB Garamond", font_size=24, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(t_row), Write(final), run_time=1.2)
        self.wait(2.5)
