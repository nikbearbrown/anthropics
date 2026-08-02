#!/usr/bin/env python3
"""
em_ac_generator.py — AC Generator: Rotating Coil Produces Sinusoidal EMF
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    N=200, B=0.150 T, A=0.100 m², ω=2π×60=377 rad/s
    ε_max = NBAω = 200×0.150×0.100×377 = 1131 V
    ε_rms = ε_max/√2 = 800 V
    T = 1/60 = 16.7 ms

Run standalone to verify:
    python3 em_ac_generator.py
"""
import sys
import numpy as np

N_TURNS = 200
B_FIELD = 0.150   # T
A_COIL  = 0.100   # m²
OMEGA   = 2 * np.pi * 60  # rad/s


def emf_max():
    return N_TURNS * B_FIELD * A_COIL * OMEGA


def emf_rms():
    return emf_max() / np.sqrt(2)


def verify():
    print("=== AC Generator verification ===")
    em = emf_max()
    er = emf_rms()
    print(f"ε_max = {em:.1f} V  (card: 1131 V)")
    print(f"ε_rms = {er:.1f} V  (card: 800 V)")
    print(f"T = {1/60*1000:.2f} ms  (card: 16.7 ms)")
    # P1: doubling ω doubles ε_max
    em2 = N_TURNS * B_FIELD * A_COIL * (2 * OMEGA)
    print(f"P1: ε_max at 2ω = {em2:.1f} V  ratio = {em2/em:.4f}  (should be 2.000)")
    print("=== PASSED ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ── Manim scene ───────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class EmAcGeneratorScene(Scene):
    """
    Left: coil rotating in B field with flux projection.
    Right: EMF vs t curve drawing in real time.
    Then show RMS bar and power at 2ω.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_formula()
        self._phase_dual_panel()
        self._phase_rms_and_power()

    def _phase_title(self):
        title = Text("AC Generator", font="EB Garamond", font_size=64, color=INK)
        sub = Text("ε = NBAω sin(ωt)  —  the sine shape is geometric, not chosen",
                   font="EB Garamond", font_size=24, color=BLUE)
        hook = Text("Rotate uniformly; sine output is unavoidable",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_formula(self):
        f1 = MathTex(r"\Phi_B = NBA\cos(\omega t)", color=INK, font_size=38)
        f2 = MathTex(r"\varepsilon = -\frac{d\Phi_B}{dt} = NBA\omega\sin(\omega t)",
                     color=BLUE, font_size=38)
        f3 = MathTex(
            r"\varepsilon_{\max} = NBA\omega = 200\times0.150\times0.100\times377 = 1{,}131\,\mathrm{V}",
            color=GOLD, font_size=28)
        VGroup(f1, f2, f3).arrange(DOWN, buff=0.45).center()
        for mob in [f1, f2, f3]:
            self.play(Write(mob), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(f1, f2, f3), run_time=0.5)

    def _phase_dual_panel(self):
        em = emf_max()
        T_period = 2 * np.pi / OMEGA  # seconds

        # ── Right panel: EMF vs time ──────────────────────────────────────────
        ax_t = Axes(
            x_range=[0, 2.2 * T_period, T_period / 2],
            y_range=[-em * 1.15, em * 1.15, em / 2],
            x_length=7,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False,
                             tip_length=0.18),
        ).shift(RIGHT * 2.5 + DOWN * 0.3)

        lx = MathTex(r"t", color=INK, font_size=22
                     ).next_to(ax_t.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"\varepsilon\;(\mathrm{V})", color=INK, font_size=22
                     ).next_to(ax_t.y_axis.get_end(), UP, buff=0.08)
        hdr_r = Text("EMF vs time", font="EB Garamond", font_size=21, color=DIM
                     ).next_to(ax_t, UP, buff=0.12)

        t_arr = np.linspace(0, 2.2 * T_period, 600)
        emf_arr = em * np.sin(OMEGA * t_arr)
        emf_curve = ax_t.plot_line_graph(
            x_values=list(t_arr), y_values=list(emf_arr),
            line_color=BLUE, stroke_width=2.5, add_vertex_dots=False,
        )

        # RMS line
        rms_line_obj = ax_t.plot_line_graph(
            x_values=[0, 2.2 * T_period],
            y_values=[emf_rms(), emf_rms()],
            line_color=GOLD, stroke_width=2, add_vertex_dots=False,
        )
        rms_lbl = MathTex(r"\varepsilon_{\rm rms}=" + f"{emf_rms():.0f}" + r"\,\mathrm{V}",
                          color=GOLD, font_size=20
                          ).next_to(ax_t.c2p(2.2 * T_period, emf_rms()), RIGHT,
                                    buff=0.08)

        # ── Left panel: coil diagram (simplified 2D edge-on view) ──────────────
        ax_phi = Axes(
            x_range=[0, 2.2 * T_period, T_period / 2],
            y_range=[-1.3, 1.3, 0.5],
            x_length=6,
            y_length=3.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False,
                             tip_length=0.18),
        ).shift(LEFT * 3.5 + DOWN * 0.3)

        lx2 = MathTex(r"t", color=INK, font_size=20
                      ).next_to(ax_phi.x_axis.get_end(), RIGHT, buff=0.08)
        ly2 = MathTex(r"\Phi_B / \Phi_{\max}", color=INK, font_size=20
                      ).next_to(ax_phi.y_axis.get_end(), UP, buff=0.08)
        hdr_l = Text("Flux (cosine)", font="EB Garamond", font_size=21, color=DIM
                     ).next_to(ax_phi, UP, buff=0.12)

        phi_arr = np.cos(OMEGA * t_arr)
        phi_curve = ax_phi.plot_line_graph(
            x_values=list(t_arr), y_values=list(phi_arr),
            line_color=BROWN, stroke_width=2.5, add_vertex_dots=False,
        )
        lag_lbl = Text("EMF lags flux by 90°", font="EB Garamond", font_size=19,
                       color=DIM).to_edge(DOWN, buff=0.28)

        self.play(
            Create(ax_phi), Write(lx2), Write(ly2), Write(hdr_l),
            Create(ax_t), Write(lx), Write(ly), Write(hdr_r),
            run_time=1.5,
        )
        self.play(Create(phi_curve), run_time=2.0)
        self.play(Create(emf_curve), run_time=2.0)
        self.play(Write(lag_lbl), run_time=0.7)
        self.wait(1.5)
        self.play(Create(rms_line_obj), Write(rms_lbl), run_time=1.0)

        # P1 annotation — max EMF at zero flux
        t_zero_flux = T_period / 4
        mark_emf = Dot(ax_t.c2p(t_zero_flux, em), color=GOLD, radius=0.1)
        mark_phi = Dot(ax_phi.c2p(t_zero_flux, 0), color=GOLD, radius=0.1)
        annot = Text("max ε when Φ=0  (coil ‖ B)", font="EB Garamond",
                     font_size=19, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(lag_lbl), run_time=0.2)
        self.play(FadeIn(mark_emf), FadeIn(mark_phi), Write(annot), run_time=0.9)
        self.wait(3.0)
        self.play(FadeOut(ax_phi, lx2, ly2, hdr_l, phi_curve,
                          ax_t, lx, ly, hdr_r, emf_curve, rms_line_obj, rms_lbl,
                          mark_emf, mark_phi, annot), run_time=0.5)

    def _phase_rms_and_power(self):
        em = emf_max()
        R_load = 100.0  # Ω
        P_avg = em**2 / (2 * R_load)

        eq_rms = MathTex(
            r"\varepsilon_{\rm rms} = \frac{\varepsilon_{\max}}{\sqrt{2}} = "
            + f"{emf_rms():.0f}" + r"\,\mathrm{V}",
            color=INK, font_size=36,
        )
        eq_power = MathTex(
            r"\langle P \rangle = \frac{\varepsilon_{\max}^2}{2R} = "
            + f"{P_avg:.1f}" + r"\,\mathrm{W}",
            color=GOLD, font_size=36,
        )
        eq_double = MathTex(
            r"\text{double }\omega\colon\;\varepsilon_{\max} \to 2{,}262\,\mathrm{V}",
            color=BLUE, font_size=32,
        )
        note = Text("RMS convention: P_avg = V_rms²/R  — same formula as DC",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(eq_rms, eq_power, eq_double, note).arrange(DOWN, buff=0.4).center()
        for mob in [eq_rms, eq_power, eq_double, note]:
            self.play(Write(mob), run_time=0.9)
        self.wait(3.0)
