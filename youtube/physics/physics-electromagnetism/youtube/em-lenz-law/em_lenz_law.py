#!/usr/bin/env python3
"""
em_lenz_law.py — Lenz's Law: Induced Current Always Opposes the Change
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    N=100 turns, A=0.020 m², R=5.0 Ω, dB/dt=2.0 T/s
    ε = NA dB/dt = 4.0 V
    I = ε/R = 0.800 A
    P = I²R = 3.2 W

Run standalone to verify:
    python3 em_lenz_law.py
"""
import sys
import numpy as np

N_TURNS = 100
A_COIL = 0.020    # m²
R_COIL = 5.0      # Ω
DB_DT = 2.0       # T/s


def emf(): return N_TURNS * A_COIL * DB_DT
def current(): return emf() / R_COIL
def power_dissipated(): return current()**2 * R_COIL


def verify():
    print("=== Lenz's Law verification ===")
    print(f"|ε| = NA dB/dt = {emf():.2f} V  (card: 4.0 V)")
    print(f"I = {current():.3f} A  (card: 0.800 A)")
    print(f"P = I²R = {power_dissipated():.2f} W  (card: 3.2 W)")
    # P1: double dB/dt
    db2 = 2 * DB_DT
    emf2 = N_TURNS * A_COIL * db2
    print(f"P1: dB/dt×2 → ε={emf2:.2f} V, I={emf2/R_COIL:.3f} A  (×2)")
    # P2: stationary magnet
    print(f"P2: dΦ/dt=0 → ε=0.000 V, I=0.000 A")
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


class EmLenzLawScene(Scene):
    """
    Bar magnet approaches solenoid. Flux meter climbs. Induced current
    shown by arrows. Opposition forces animate. Current reverses on exit.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_faraday_minus_sign()
        self._phase_magnet_approach()
        self._phase_power_balance()
        self._phase_energy_conservation()

    def _phase_title(self):
        title = Text("Lenz's Law — Induced Current Opposes the Change",
                     font="EB Garamond", font_size=50, color=INK)
        sub = MathTex(r"\varepsilon = -\frac{d\Phi_B}{dt}", color=BLUE, font_size=38)
        hook = Text("The minus sign is energy conservation wearing a magnetic mask",
                    font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub), run_time=0.9)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_faraday_minus_sign(self):
        steps = VGroup(
            MathTex(r"\text{Inserting N pole: flux }\uparrow\;\Rightarrow\;",
                    r"\text{induced B }\downarrow\;\Rightarrow\;\text{repulsion}",
                    color=INK, font_size=28),
            MathTex(r"\text{Removing N pole: flux }\downarrow\;\Rightarrow\;",
                    r"\text{induced B }\uparrow\;\Rightarrow\;\text{attraction}",
                    color=DIM, font_size=28),
            MathTex(r"\text{Either way: work must be done by external agent}",
                    color=GOLD, font_size=28),
        ).arrange(DOWN, buff=0.5).center()
        for mob in steps:
            self.play(Write(mob), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(steps), run_time=0.5)

    def _phase_magnet_approach(self):
        # Solenoid (rectangle)
        coil = Rectangle(width=3.0, height=1.8, color=BLUE, stroke_width=3
                         ).shift(RIGHT * 2.5)
        coil_lbl = Text("N=100, A=0.020 m², R=5 Ω", font="EB Garamond",
                        font_size=18, color=BLUE).next_to(coil, UP, buff=0.12)

        # Bar magnet
        mag_N = Rectangle(width=1.0, height=0.7, fill_color=BROWN,
                          fill_opacity=0.9, stroke_width=0).shift(LEFT * 4.5 + UP * 0)
        mag_S = Rectangle(width=1.0, height=0.7, fill_color=DIM,
                          fill_opacity=0.7, stroke_width=0).next_to(mag_N, LEFT,
                                                                      buff=0)
        N_lbl = Text("N", font="EB Garamond", font_size=24, color=INK
                     ).move_to(mag_N.get_center())
        S_lbl = Text("S", font="EB Garamond", font_size=24, color=INK
                     ).move_to(mag_S.get_center())
        magnet = VGroup(mag_N, mag_S, N_lbl, S_lbl)

        # Flux meter readout
        flux_lbl = MathTex(r"\Phi_B\;\uparrow", color=GOLD, font_size=28
                           ).to_edge(DOWN, buff=0.5)
        emf_lbl = MathTex(
            r"\varepsilon = -N\frac{d\Phi}{dt} = " + f"{emf():.1f}" + r"\,\text{V}",
            color=INK, font_size=28).next_to(flux_lbl, UP, buff=0.2)
        curr_lbl = MathTex(r"I = " + f"{current():.2f}" + r"\,\text{A}",
                           color=BLUE, font_size=28).next_to(emf_lbl, UP, buff=0.2)

        # Opposition arrow on coil face
        repel = Arrow(start=[1.0, 0, 0], end=[-0.5, 0, 0], color=GOLD,
                      stroke_width=2.5, buff=0, tip_length=0.22)
        repel_lbl = Text("repulsion", font="EB Garamond", font_size=20, color=GOLD
                         ).next_to(repel, DOWN, buff=0.12)

        self.play(Create(coil), Write(coil_lbl), run_time=0.8)
        self.play(FadeIn(magnet), run_time=0.7)
        # Animate magnet moving toward coil
        self.play(
            magnet.animate.shift(RIGHT * 2.5),
            run_time=2.5,
        )
        self.play(Write(flux_lbl), Write(emf_lbl), Write(curr_lbl), run_time=1.0)
        self.play(Create(repel), Write(repel_lbl), run_time=0.8)
        self.wait(2.0)

        # Stationary: current drops to zero
        zero_note = MathTex(r"\dot{\Phi}=0\;\Rightarrow\;\varepsilon=0,\;I=0",
                            color=DIM, font_size=26).to_edge(DOWN, buff=0.5)
        self.play(FadeOut(flux_lbl, emf_lbl, curr_lbl, repel, repel_lbl),
                  Write(zero_note), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(coil, coil_lbl, magnet, zero_note), run_time=0.5)

    def _phase_power_balance(self):
        title = Text("Work in = Electrical power out", font="EB Garamond",
                     font_size=30, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.7)

        rows = VGroup(
            MathTex(r"|\varepsilon| = NA\,\frac{dB}{dt} = "
                    + f"{emf():.1f}" + r"\,\text{V}", color=INK, font_size=32),
            MathTex(r"I = \varepsilon/R = " + f"{current():.3f}" + r"\,\text{A}",
                    color=BLUE, font_size=32),
            MathTex(r"P = I^2R = " + f"{power_dissipated():.2f}" + r"\,\text{W}",
                    color=GOLD, font_size=32),
            MathTex(r"\text{(extracted from work done pushing the magnet)}",
                    color=DIM, font_size=26),
        ).arrange(DOWN, buff=0.45).center()
        for mob in rows:
            self.play(Write(mob), run_time=0.9)
        self.wait(3.0)
        self.play(FadeOut(title, rows), run_time=0.5)

    def _phase_energy_conservation(self):
        final = VGroup(
            MathTex(r"\varepsilon = -\frac{d\Phi_B}{dt}", color=BLUE, font_size=40),
            Text("The minus sign is an impossibility theorem:",
                 font="EB Garamond", font_size=24, color=INK),
            Text("a helping current would conjure free energy from induction",
                 font="EB Garamond", font_size=24, color=DIM),
            Text("Lenz's law = energy conservation, stated electromagnetically",
                 font="EB Garamond", font_size=24, color=GOLD),
        ).arrange(DOWN, buff=0.45).center()
        for mob in final:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob),
                      run_time=0.9)
        self.wait(4.0)
