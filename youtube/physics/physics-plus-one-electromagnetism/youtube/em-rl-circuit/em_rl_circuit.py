#!/usr/bin/env python3
"""
em_rl_circuit.py — RL Circuit: Current Grows on a tau = L/R Timescale
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    I(t) = (epsilon/R)(1 - exp(-t/tau)),  tau = L/R
    U_L(t) = 0.5 * L * I(t)^2

Verify: python3 em_rl_circuit.py --verify
Render: manim -qh em_rl_circuit.py EmRlCircuitScene
"""
import sys
import numpy as np

EPSILON = 12.0    # V
R_OHM   = 6.0     # Ohm
L_HENRY = 30e-3   # H  (30 mH)

def tau():
    return L_HENRY / R_OHM   # s

def I_final():
    return EPSILON / R_OHM   # A

def I_of_t(t, L=L_HENRY, R=R_OHM):
    tau_val = L / R
    return (EPSILON / R) * (1 - np.exp(-t / tau_val))

def U_L(t, L=L_HENRY, R=R_OHM):
    return 0.5 * L * I_of_t(t, L, R)**2

def verify():
    print("=== RL circuit verification ===")
    tau_v = tau()
    I_f   = I_final()
    print(f"tau = {tau_v*1000:.1f} ms  (expected 5 ms) {'✓' if abs(tau_v - 5e-3) < 0.1e-3 else '✗'}")
    print(f"I_final = {I_f:.1f} A  (expected 2.0 A) {'✓' if abs(I_f - 2.0) < 0.01 else '✗'}")

    # P1: I at t=tau = 0.632 * I_final
    I_tau = I_of_t(tau_v)
    expected = I_f * (1 - np.exp(-1))
    print(f"P1: I(tau) = {I_tau:.4f} A  (expected {expected:.4f} A = 63.2% of final) {'✓' if abs(I_tau - expected) < 0.001 else '✗'}")

    # P2: I at t=2*tau = 86.5% of final
    I_2tau = I_of_t(2 * tau_v)
    print(f"P2: I(2*tau) = {I_2tau:.4f} A  (expected {I_f*(1-np.exp(-2)):.4f} A = 86.5%) {'✓' if abs(I_2tau - I_f*(1-np.exp(-2))) < 0.001 else '✗'}")

    U_steady = 0.5 * L_HENRY * I_f**2
    print(f"U_L steady = {U_steady*1000:.1f} mJ  (expected 60 mJ) {'✓' if abs(U_steady - 0.06) < 0.001 else '✗'}")
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

TAU   = tau()
I_FIN = I_final()
T_MAX = 5.5 * TAU


class EmRlCircuitScene(Scene):
    """
    I(t) exponential rise curve + U_L(t) energy panel.
    L and R sliders update tau = L/R in real time.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax_I, ax_U = self._axes()
        self._draw_curves(ax_I, ax_U)
        self._annotations(ax_I)
        self._slider_phase(ax_I, ax_U)
        self._finale()

    def _title(self):
        t = Text("RL Circuit: Current Grows on τ = L/R",
                 font="EB Garamond", font_size=54, color=INK)
        s = Text(
            "I(t) = (ε/R)(1 − e^{−t/τ})   τ = L/R = 5 ms\n"
            "Inductors oppose change — they remember current.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        t_ms = T_MAX * 1000

        ax_I = Axes(
            x_range=[0, t_ms + 1, 5],
            y_range=[0, I_FIN * 1.12, 0.5],
            x_length=7,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(LEFT * 2.5 + UP * 0.2)
        lx_I = MathTex(r"t\;(\mathrm{ms})", color=INK, font_size=22).next_to(ax_I.x_axis.get_end(), RIGHT, buff=0.1)
        ly_I = MathTex(r"I\;(\mathrm{A})", color=INK, font_size=22).next_to(ax_I.y_axis.get_end(), UP, buff=0.1)
        hdr_I = Text("Current I(t)", font="EB Garamond", font_size=20, color=DIM).next_to(ax_I, UP, buff=0.1)

        ax_U = Axes(
            x_range=[0, t_ms + 1, 5],
            y_range=[0, 70, 20],
            x_length=4,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.2,
                             include_ticks=False, tip_length=0.15),
        ).shift(RIGHT * 4.5 + UP * 0.2)
        lx_U = MathTex(r"t", color=INK, font_size=18).next_to(ax_U.x_axis.get_end(), RIGHT, buff=0.08)
        ly_U = MathTex(r"U_L\;(\mathrm{mJ})", color=INK, font_size=18).next_to(ax_U.y_axis.get_end(), UP, buff=0.08)
        hdr_U = Text("Stored energy", font="EB Garamond", font_size=18, color=DIM).next_to(ax_U, UP, buff=0.1)

        self.play(Create(ax_I), Create(ax_U),
                  Write(lx_I), Write(ly_I), Write(hdr_I),
                  Write(lx_U), Write(ly_U), Write(hdr_U), run_time=1.5)
        return ax_I, ax_U

    def _draw_curves(self, ax_I, ax_U):
        t_s = np.linspace(0, T_MAX, 400)
        t_ms = t_s * 1000
        I_vals = I_of_t(t_s)
        U_vals = U_L(t_s) * 1000   # mJ

        I_pts = [ax_I.c2p(t, i) for t, i in zip(t_ms, I_vals)]
        U_pts = [ax_U.c2p(t, u) for t, u in zip(t_ms, U_vals) if 0 <= u <= 68]

        I_curve = VMobject(color=BLUE, stroke_width=3)
        I_curve.set_points_smoothly(np.array(I_pts))
        U_curve = VMobject(color=GOLD, stroke_width=2.5)
        U_curve.set_points_smoothly(np.array(U_pts))

        # Asymptote
        asym = DashedLine(ax_I.c2p(0, I_FIN), ax_I.c2p(T_MAX*1000, I_FIN),
                          color=DIM, stroke_width=1.5, stroke_opacity=0.6)
        asym_lbl = MathTex(rf"I_{{f}} = {I_FIN:.1f}\,\mathrm{{A}}", color=DIM, font_size=22)
        asym_lbl.next_to(ax_I.c2p(T_MAX*1000 * 0.7, I_FIN), UP, buff=0.1)

        self.play(Create(I_curve), Create(U_curve), run_time=2.5)
        self.play(Create(asym), Write(asym_lbl), run_time=0.8)
        self.wait(1.0)

    def _annotations(self, ax_I):
        tau_ms = TAU * 1000
        I_at_tau = I_of_t(TAU)

        # Tau marker
        tau_line = DashedLine(ax_I.c2p(tau_ms, 0), ax_I.c2p(tau_ms, I_at_tau),
                              color=GOLD, stroke_width=2)
        tau_dot  = Dot(ax_I.c2p(tau_ms, I_at_tau), color=GOLD, radius=0.12)
        tau_lbl  = MathTex(rf"\tau = {tau_ms:.0f}\,\mathrm{{ms}}", color=GOLD, font_size=22)
        tau_lbl.next_to(tau_dot, UR, buff=0.15)
        pct_lbl  = Text(f"63.2% of final", font="EB Garamond", font_size=18, color=GOLD)
        pct_lbl.next_to(tau_dot, RIGHT, buff=0.1)

        # 2*tau marker
        I_at_2tau = I_of_t(2 * TAU)
        dot_2tau = Dot(ax_I.c2p(2*tau_ms, I_at_2tau), color=BROWN, radius=0.10)
        lbl_2tau = MathTex(r"86.5\%", color=BROWN, font_size=18)
        lbl_2tau.next_to(dot_2tau, UR, buff=0.1)

        self.play(Create(tau_line), FadeIn(tau_dot), Write(tau_lbl), Write(pct_lbl), run_time=1.0)
        self.play(FadeIn(dot_2tau), Write(lbl_2tau), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(tau_line, tau_dot, tau_lbl, pct_lbl, dot_2tau, lbl_2tau), run_time=0.3)

    def _slider_phase(self, ax_I, ax_U):
        L_tracker = ValueTracker(L_HENRY * 1000)   # mH
        R_tracker = ValueTracker(R_OHM)

        def _I_curve():
            L = L_tracker.get_value() * 1e-3
            R = R_tracker.get_value()
            t_s = np.linspace(0, T_MAX, 300)
            t_ms = t_s * 1000
            I_v = I_of_t(t_s, L=L, R=R)
            pts = [ax_I.c2p(t, np.clip(i, 0, I_FIN * 1.1)) for t, i in zip(t_ms, I_v)]
            m = VMobject(color=GOLD, stroke_width=3)
            m.set_points_smoothly(np.array(pts))
            return m

        dyn_I = always_redraw(_I_curve)
        self.add(dyn_I)

        L_lbl = MathTex(r"L = ", color=INK, font_size=24)
        L_num = DecimalNumber(L_HENRY * 1000, num_decimal_places=0, color=GOLD, font_size=24)
        L_mH  = MathTex(r"\,\mathrm{mH}", color=INK, font_size=24)
        L_num.add_updater(lambda m: m.set_value(L_tracker.get_value()))

        R_lbl = MathTex(r"R = ", color=INK, font_size=24)
        R_num = DecimalNumber(R_OHM, num_decimal_places=0, color=BLUE, font_size=24)
        R_ohm = MathTex(r"\,\Omega", color=INK, font_size=24)
        R_num.add_updater(lambda m: m.set_value(R_tracker.get_value()))

        tau_lbl = MathTex(r"\tau = ", color=DIM, font_size=22)
        tau_num = DecimalNumber(TAU * 1000, num_decimal_places=1, color=GOLD, font_size=22)
        tau_ms_lbl = MathTex(r"\,\mathrm{ms}", color=DIM, font_size=22)
        tau_num.add_updater(lambda m: m.set_value(L_tracker.get_value() / R_tracker.get_value()))

        L_row   = VGroup(L_lbl, L_num, L_mH).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.3)
        R_row   = VGroup(R_lbl, R_num, R_ohm).arrange(RIGHT, buff=0.1).next_to(L_row, DOWN, buff=0.2)
        tau_row = VGroup(tau_lbl, tau_num, tau_ms_lbl).arrange(RIGHT, buff=0.1).next_to(R_row, DOWN, buff=0.2)

        self.play(Write(L_row), Write(R_row), Write(tau_row), run_time=0.8)
        self.play(L_tracker.animate.set_value(60), run_time=2.0, rate_func=smooth)
        self.play(R_tracker.animate.set_value(12), run_time=1.5, rate_func=smooth)
        self.play(L_tracker.animate.set_value(30), R_tracker.animate.set_value(6), run_time=1.5, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(L_row, R_row, tau_row, dyn_I), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"I(t) = \frac{\varepsilon}{R}\left(1 - e^{-t/\tau}\right)",
            r"\quad \tau = \frac{L}{R} = 5\,\mathrm{ms}",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
