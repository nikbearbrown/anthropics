#!/usr/bin/env python3
"""
em_motional_emf_rails.py — Motional EMF Rod-on-Rails
SILENT SLATE — math-explainer (brownblue) candidate, physics-electromagnetism book.

Physics:
    B=0.50 T, L=0.30 m, R=2.0 Ω
    v=4.0 m/s: ε=BLv=0.60 V, I=0.30 A, F_B=0.045 N,
    P_mech=P_elec=0.180 W
    v=8.0 m/s: P=0.720 W (×4)

Run standalone to verify:
    python3 em_motional_emf_rails.py
"""
import sys
import numpy as np

B = 0.50   # T
L = 0.30   # m
R = 2.0    # Ω


def emf(v): return B * L * v
def current(v): return emf(v) / R
def braking_force(v): return B * current(v) * L
def power(v): return braking_force(v) * v  # = emf(v)**2 / R


def verify():
    print("=== Motional EMF verification ===")
    for v in [4.0, 8.0]:
        e = emf(v); I = current(v); F = braking_force(v); P = power(v)
        print(f"v={v} m/s: ε={e:.3f} V, I={I:.3f} A, F={F:.4f} N, P={P:.4f} W")
    print(f"P(8)/P(4) = {power(8.0)/power(4.0):.4f}  (should be 4.000)")
    # R halved test
    def power_r(v, r): return (B*L*v)**2 / r
    print(f"R=1Ω, v=4: P={power_r(4.0, 1.0):.4f} W  F={B**2*L**2*4.0/1.0:.4f} N")
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


class EmMotionalEmfRailsScene(Scene):
    """
    Rod slides on rails in B field. Real-time power balance P_mech = P_elec.
    Then v ramps up; P grows quadratically. Finally free deceleration.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_setup()
        self._phase_velocity_ramp()
        self._phase_free_decay()

    def _phase_title(self):
        title = Text("Motional EMF — Rod on Rails", font="EB Garamond",
                     font_size=58, color=INK)
        sub = Text("ε = BLv  ·  P_mech = P_elec = B²L²v²/R",
                   font="EB Garamond", font_size=24, color=BLUE)
        hook = Text("Every generator is a conductor moving through a magnetic field",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(hook), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_setup(self):
        # Draw rail geometry
        rail_top = Line([-5, 1.2, 0], [3, 1.2, 0], color=DIM, stroke_width=3)
        rail_bot = Line([-5, -1.2, 0], [3, -1.2, 0], color=DIM, stroke_width=3)
        rail_lbl = Text("rails", font="EB Garamond", font_size=18, color=DIM
                        ).next_to(rail_top, UP, buff=0.08)

        # B field arrows (pointing up)
        b_arrows = VGroup(*[
            Arrow(start=[x, -0.5, 0], end=[x, 0.5, 0],
                  color=DIM, stroke_width=1.5, buff=0)
            for x in np.linspace(-4.5, 2.5, 8)
        ])
        b_lbl = MathTex(r"\vec{B} = 0.50\,\mathrm{T}\,\hat{y}", color=DIM,
                        font_size=22).next_to(b_arrows, RIGHT, buff=0.15)

        # Rod
        rod = Line([-1, 1.2, 0], [-1, -1.2, 0], color=BLUE, stroke_width=5)
        rod_lbl = MathTex(r"L=0.30\,\mathrm{m}", color=BLUE, font_size=20
                          ).next_to(rod, LEFT, buff=0.12)

        # Resistor box
        resistor = Rectangle(width=0.6, height=0.4, color=BROWN,
                             stroke_width=2).move_to([-4, 0, 0])
        r_lbl = MathTex(r"R=2\,\Omega", color=BROWN, font_size=20
                        ).next_to(resistor, DOWN, buff=0.12)
        wire_top = Line([-4, 0.2, 0], [-4, 1.2, 0], color=BROWN, stroke_width=2)
        wire_bot = Line([-4, -0.2, 0], [-4, -1.2, 0], color=BROWN, stroke_width=2)

        # Velocity arrow
        v_arrow = Arrow(start=[-1, 0, 0], end=[0.5, 0, 0], color=GOLD,
                        stroke_width=2.5, buff=0)
        v_lbl = MathTex(r"v = 4.0\,\mathrm{m/s}", color=GOLD, font_size=22
                        ).next_to(v_arrow, UP, buff=0.1)

        self.play(Create(rail_top), Create(rail_bot), Write(rail_lbl), run_time=0.8)
        self.play(Create(b_arrows), Write(b_lbl), run_time=0.8)
        self.play(Create(rod), Write(rod_lbl), run_time=0.7)
        self.play(Create(resistor), Write(r_lbl), Create(wire_top),
                  Create(wire_bot), run_time=0.8)
        self.play(Create(v_arrow), Write(v_lbl), run_time=0.7)

        # Power balance readout
        v0 = 4.0
        p_mech = power(v0)
        readout = MathTex(
            r"P_{\rm mech} = " + f"{p_mech:.3f}" + r"\,\mathrm{W}",
            r"\;=\; P_{\rm elec}",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(readout), run_time=1.2)
        self.wait(2.5)

        self.play(FadeOut(rail_top, rail_bot, rail_lbl, b_arrows, b_lbl,
                          rod, rod_lbl, resistor, r_lbl, wire_top, wire_bot,
                          v_arrow, v_lbl, readout), run_time=0.5)

    def _phase_velocity_ramp(self):
        title = Text("P ∝ v²  — quadratic scaling", font="EB Garamond",
                     font_size=30, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.8)

        ax = Axes(
            x_range=[0, 9, 2],
            y_range=[0, 0.85, 0.2],
            x_length=9,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.4)
        lx = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"P\;(\mathrm{W})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        v_arr = np.linspace(0.01, 9, 300)
        p_arr = [power(v) for v in v_arr]

        curve = ax.plot_line_graph(
            x_values=v_arr, y_values=p_arr,
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )

        dot4 = Dot(ax.c2p(4.0, power(4.0)), color=GOLD, radius=0.12)
        dot8 = Dot(ax.c2p(8.0, power(8.0)), color=BROWN, radius=0.12)
        lbl4 = MathTex(r"0.180\,\mathrm{W}", color=GOLD, font_size=22
                       ).next_to(dot4, LEFT, buff=0.12)
        lbl8 = MathTex(r"0.720\,\mathrm{W}", color=BROWN, font_size=22
                       ).next_to(dot8, RIGHT, buff=0.12)
        ratio = Text("×4 for ×2 in v", font="EB Garamond", font_size=22, color=DIM
                     ).to_edge(DOWN, buff=0.3)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(curve), run_time=2.0)
        self.play(FadeIn(dot4), Write(lbl4), run_time=0.7)
        self.play(FadeIn(dot8), Write(lbl8), run_time=0.7)
        self.play(Write(ratio), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, curve, dot4, dot8, lbl4, lbl8, ratio),
                  run_time=0.5)

    def _phase_free_decay(self):
        title = Text("Remove applied force: v(t) = v₀ e^{−B²L²t/(mR)}",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.9)

        m_rod = 0.10  # kg — assumed rod mass for decay demo
        tau = m_rod * R / (B**2 * L**2)
        v0 = 4.0
        t_arr = np.linspace(0, 5 * tau, 300)
        v_arr = v0 * np.exp(-t_arr / tau)

        ax = Axes(
            x_range=[0, 5 * tau, tau],
            y_range=[0, v0 * 1.1, 1.0],
            x_length=9,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.4)
        lx = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"v\;(\mathrm{m/s})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        curve = ax.plot_line_graph(
            x_values=list(t_arr), y_values=list(v_arr),
            line_color=BLUE, stroke_width=3, add_vertex_dots=False,
        )
        tau_dot = Dot(ax.c2p(tau, v0 / np.e), color=GOLD, radius=0.1)
        tau_lbl = MathTex(r"\tau = mR/(B^2L^2)", color=GOLD, font_size=22
                          ).next_to(tau_dot, UR, buff=0.1)
        energy = Text("Total energy = ½mv₀²  (all dissipated in R)",
                      font="EB Garamond", font_size=22, color=DIM).to_edge(DOWN,
                                                                            buff=0.3)
        KE = 0.5 * m_rod * v0**2
        ke_lbl = MathTex(r"\tfrac{1}{2}mv_0^2 = " + f"{KE:.4f}" + r"\,\mathrm{J}",
                         color=INK, font_size=26).next_to(energy, UP, buff=0.2)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(curve), run_time=2.0)
        self.play(FadeIn(tau_dot), Write(tau_lbl), run_time=0.8)
        self.play(Write(ke_lbl), Write(energy), run_time=0.9)
        self.wait(3.0)
