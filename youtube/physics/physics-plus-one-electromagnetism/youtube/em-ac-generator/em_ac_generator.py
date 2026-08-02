#!/usr/bin/env python3
"""
em_ac_generator.py — AC Generator: epsilon(t) = NBAw sin(wt)
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    Phi(t) = N*B*A*cos(omega*t)
    epsilon(t) = N*B*A*omega * sin(omega*t) = epsilon_0 * sin(omega*t)
    epsilon_0 = N*B*A*omega
    epsilon_rms = epsilon_0 / sqrt(2)

Verify: python3 em_ac_generator.py --verify
Render: manim -qh em_ac_generator.py EmAcGeneratorScene
"""
import sys
import numpy as np

N_TURNS = 200
B_FIELD = 0.1    # T
A_COIL  = 0.01   # m^2
F_HZ    = 60.0   # Hz
OMEGA   = 2 * np.pi * F_HZ

def peak_emf():
    return N_TURNS * B_FIELD * A_COIL * OMEGA

def rms_emf(e0=None):
    if e0 is None:
        e0 = peak_emf()
    return e0 / np.sqrt(2)

def verify():
    print("=== AC generator verification ===")
    e0 = peak_emf()
    e_rms = rms_emf(e0)
    print(f"epsilon_0 = {e0:.2f} V  (expected 75.4 V) {'OK' if abs(e0 - 75.4) < 1.0 else 'FAIL'}")
    print(f"epsilon_rms = {e_rms:.2f} V  (expected ~53.3 V) {'OK' if abs(e_rms - 53.3) < 1.0 else 'FAIL'}")
    t_parallel = 0.0
    e_at_parallel = e0 * np.sin(OMEGA * t_parallel)
    print(f"P1: epsilon at theta=0 = {e_at_parallel:.4f} V  (expected 0) {'OK' if abs(e_at_parallel) < 1e-10 else 'FAIL'}")
    t_perp = (np.pi/2) / OMEGA
    e_at_perp = e0 * np.sin(OMEGA * t_perp)
    print(f"P2: epsilon at theta=pi/2 = {e_at_perp:.2f} V  (expected {e0:.2f} V) {'OK' if abs(e_at_perp - e0) < 0.01 else 'FAIL'}")
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

E0 = peak_emf()
T_PERIOD = 1.0 / F_HZ


class EmAcGeneratorScene(Scene):
    """
    Left: rotating coil diagram (static schematic + angle label).
    Right: EMF(t) = epsilon_0 * sin(omega*t) full sinusoid curve.
    N slider scales amplitude. RMS annotation.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_emf_curve(ax)
        self._rms_annotation(ax)
        self._slider_phase(ax)
        self._finale()

    def _title(self):
        t = Text("AC Generator: Rotation Creates Sinusoidal Voltage",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "epsilon(t) = NBAo sin(ot)  — Faraday's law on a rotating loop.\n"
            "Peak at coil perpendicular to B; zero when coil is parallel.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0, 2 * T_PERIOD * 1000, T_PERIOD * 1000 / 2],  # ms
            y_range=[-E0 * 1.15, E0 * 1.15, E0 / 2],
            x_length=9,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(RIGHT * 0.8 + DOWN * 0.3)
        lx = MathTex(r"t\;(\mathrm{ms})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"\varepsilon(t)\;(\mathrm{V})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("EMF vs time  (60 Hz, N=200 turns)", font="EB Garamond",
                   font_size=18, color=DIM).next_to(ax, UP, buff=0.1)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.3)
        return ax

    def _coil_schematic(self):
        """Static coil schematic on the left side."""
        center = LEFT * 4.5 + DOWN * 0.3
        # B field arrows
        for dy in [-0.9, 0, 0.9]:
            fl = Arrow(center + LEFT * 1.5 + UP * dy,
                       center + RIGHT * 1.5 + UP * dy,
                       color=DIM, buff=0, max_tip_length_to_length_ratio=0.1,
                       stroke_width=1.5, stroke_opacity=0.4)
            self.add(fl)
        b_lbl = MathTex(r"\vec{B}", color=DIM, font_size=20).next_to(center + RIGHT * 1.5, RIGHT, buff=0.1)
        self.add(b_lbl)
        # Coil as ellipse (side view, ~45 degrees)
        coil = Ellipse(width=2.0, height=0.6, color=BLUE, stroke_width=3).move_to(center)
        self.add(coil)
        # Label
        n_lbl = MathTex(r"N = 200", color=BLUE, font_size=20).next_to(coil, DOWN, buff=0.5)
        self.add(n_lbl)
        return center

    def _draw_emf_curve(self, ax):
        center = self._coil_schematic()

        # Full EMF sinusoid
        t_ms = np.linspace(0, 2 * T_PERIOD * 1000, 500)
        e_vals = E0 * np.sin(OMEGA * t_ms / 1000)
        pts = np.array([ax.c2p(t, e) for t, e in zip(t_ms, e_vals)])
        emf_curve = VMobject(color=BLUE, stroke_width=3)
        emf_curve.set_points_smoothly(pts)

        # Peak annotation
        t_peak_ms = (np.pi / 2) / OMEGA * 1000
        peak_dot = Dot(ax.c2p(t_peak_ms, E0), color=GOLD, radius=0.12)
        peak_lbl = MathTex(rf"\varepsilon_0 = {E0:.0f}\,\mathrm{{V}}", color=GOLD, font_size=22)
        peak_lbl.next_to(peak_dot, UP, buff=0.15)

        # Zero crossings annotations
        t_zero1_ms = 0.0
        zero_lbl = Text("coil || B → ε = 0", font="EB Garamond", font_size=16, color=DIM)
        zero_lbl.next_to(ax.c2p(t_zero1_ms, 0), UR, buff=0.15)
        perp_lbl = Text("coil perpendicular → ε = max", font="EB Garamond", font_size=16, color=GOLD)
        perp_lbl.next_to(ax.c2p(t_peak_ms, E0), DR, buff=0.1)

        self.play(Create(emf_curve), run_time=2.0)
        self.play(FadeIn(peak_dot), Write(peak_lbl), run_time=0.8)
        self.play(Write(zero_lbl), Write(perp_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(zero_lbl, perp_lbl), run_time=0.3)

    def _rms_annotation(self, ax):
        e_rms = rms_emf(E0)
        t_ms_end = 2 * T_PERIOD * 1000
        rms_line = DashedLine(ax.c2p(0, e_rms), ax.c2p(t_ms_end, e_rms),
                              color=BROWN, stroke_width=2)
        rms_lbl = MathTex(
            rf"\varepsilon_{{\rm rms}} = \varepsilon_0/\sqrt{{2}} = {e_rms:.1f}\,\mathrm{{V}}",
            color=BROWN, font_size=22,
        )
        rms_lbl.next_to(ax.c2p(1.3 * T_PERIOD * 1000, e_rms), UR, buff=0.1)

        # Shade area between 0 and e_rms to illustrate RMS
        shade_x = np.linspace(0, t_ms_end, 200)
        shade_e = E0 * np.sin(OMEGA * shade_x / 1000)
        shade_pts_top = [ax.c2p(t, np.clip(e, 0, e_rms)) for t, e in zip(shade_x, shade_e)]
        shade_pts_bot = [ax.c2p(t, 0) for t in shade_x]

        self.play(Create(rms_line), Write(rms_lbl), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(rms_line, rms_lbl), run_time=0.3)

    def _slider_phase(self, ax):
        N_tracker = ValueTracker(float(N_TURNS))
        t_ms = np.linspace(0, 2 * T_PERIOD * 1000, 400)

        def _emf_curve():
            N = N_tracker.get_value()
            e0 = N * B_FIELD * A_COIL * OMEGA
            e_v = np.clip(e0 * np.sin(OMEGA * t_ms / 1000), -E0 * 1.12, E0 * 1.12)
            pts = np.array([ax.c2p(t, e) for t, e in zip(t_ms, e_v)])
            m = VMobject(color=GOLD, stroke_width=3)
            m.set_points_smoothly(pts)
            return m

        dyn = always_redraw(_emf_curve)
        self.add(dyn)

        n_lbl = MathTex(r"N = ", color=INK, font_size=26)
        n_num = DecimalNumber(N_TURNS, num_decimal_places=0, color=GOLD, font_size=26)
        n_num.add_updater(lambda m: m.set_value(N_tracker.get_value()))

        e0_lbl = MathTex(r"\varepsilon_0 = ", color=DIM, font_size=22)
        e0_num = DecimalNumber(E0, num_decimal_places=1, color=BLUE, font_size=22)
        e0_V   = MathTex(r"\,\mathrm{V}", color=DIM, font_size=22)
        e0_num.add_updater(lambda m: m.set_value(N_tracker.get_value() * B_FIELD * A_COIL * OMEGA))

        row1 = VGroup(n_lbl, n_num).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.3)
        row2 = VGroup(e0_lbl, e0_num, e0_V).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.25)

        self.play(Write(row1), Write(row2), run_time=0.8)
        self.play(N_tracker.animate.set_value(100), run_time=2.0, rate_func=smooth)
        self.play(N_tracker.animate.set_value(400), run_time=2.0, rate_func=smooth)
        self.play(N_tracker.animate.set_value(N_TURNS), run_time=1.5, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(row1, row2, dyn), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"\varepsilon(t) = NBA\omega\sin(\omega t)",
            r"\quad \varepsilon_{\rm rms} = \frac{\varepsilon_0}{\sqrt{2}}",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
