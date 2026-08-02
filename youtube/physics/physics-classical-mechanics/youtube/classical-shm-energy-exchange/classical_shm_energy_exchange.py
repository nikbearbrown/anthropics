#!/usr/bin/env python3
"""
classical_shm_energy_exchange.py — SHM Energy Exchange (Classical Mechanics variant)
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    m=0.5 kg, k=50 N/m, A=0.20 m
    ω=10 rad/s, T=0.628 s, E_total=1.00 J
    At x=A/√2=0.141 m: KE=PE=0.500 J

Render:
    cd physics-classical-mechanics/youtube/classical-shm-energy-exchange
    manim -qh classical_shm_energy_exchange.py ClassicalSHMEnergyScene
"""
import sys
import numpy as np

M = 0.5
K = 50.0
A = 0.20
OMEGA = np.sqrt(K/M)
T_P   = 2*np.pi/OMEGA
E_TOT = 0.5*K*A**2


def verify():
    print("=== Classical SHM Energy Exchange verification ===")
    print(f"  ω = {OMEGA:.4f} rad/s  (expected 10)")
    print(f"  T = {T_P:.4f} s  (expected 0.6283)")
    print(f"  E_total = {E_TOT:.4f} J  (expected 1.00)")
    x_eq = A/np.sqrt(2)
    PE_eq = 0.5*K*x_eq**2
    KE_eq = E_TOT - PE_eq
    print(f"  At x=A/√2={x_eq:.4f} m: KE={KE_eq:.4f} J, PE={PE_eq:.4f} J  (both 0.5000)")
    # P1
    assert abs(KE_eq - 0.5) < 1e-8 and abs(PE_eq - 0.5) < 1e-8, "P1"
    # P2: energy frequency = 2ω
    print(f"  Energy oscillation frequency = 2ω = {2*OMEGA:.4f} rad/s (period = T/2 = {T_P/2:.4f} s)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

N_CYCLES = 3.0
T_ANIM = N_CYCLES * T_P


class ClassicalSHMEnergyScene(Scene):
    """Mass-spring + KE/PE energy curves; crossover and total-energy flat line."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._energy_scene()

    def _title(self):
        t1 = Text("SHM Energy Exchange", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Energy sloshes between spring and motion — sum never changes",
                  font="EB Garamond", font_size=23, color=DIM)
        t3 = MathTex(r"E_{\rm total} = \tfrac{1}{2}kA^2 = 1.00\,\mathrm{J}",
                     color=GOLD, font_size=32)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.4)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _energy_scene(self):
        ax = Axes(
            x_range=[0, T_ANIM, T_P],
            y_range=[0, 1.15, 0.25],
            x_length=10.5,
            y_length=4.8,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.3)
        lx = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"E\;(\mathrm{J})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Energy vs time  (m=0.5 kg, k=50 N/m, A=0.20 m)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        ts = np.linspace(0, T_ANIM, 1500)
        xs = A * np.cos(OMEGA*ts)
        KE = 0.5*K*A**2 * np.sin(OMEGA*ts)**2
        PE = 0.5*K*xs**2

        pts_ke  = np.array([ax.c2p(t,k) for t,k in zip(ts,KE)])
        pts_pe  = np.array([ax.c2p(t,p) for t,p in zip(ts,PE)])
        pts_tot = np.array([ax.c2p(t, E_TOT) for t in ts])

        crv_ke  = VMobject(color=BLUE,  stroke_width=2.8).set_points_smoothly(pts_ke)
        crv_pe  = VMobject(color=BROWN, stroke_width=2.8).set_points_smoothly(pts_pe)
        crv_tot = VMobject(color=GOLD,  stroke_width=1.8, stroke_opacity=0.75).set_points_smoothly(pts_tot)

        lbl_ke  = Text("KE (kinetic)", font="EB Garamond", font_size=19, color=BLUE).move_to(ax.c2p(0.55, 1.08))
        lbl_pe  = Text("PE (spring)", font="EB Garamond", font_size=19, color=BROWN).move_to(ax.c2p(0.15, 1.08))
        lbl_tot = MathTex(r"E_{\rm total}=1.00\,\mathrm{J}", color=GOLD, font_size=19).move_to(ax.c2p(1.5, 1.08))

        self.play(Create(crv_ke), Create(crv_pe), Create(crv_tot),
                  Write(lbl_ke), Write(lbl_pe), Write(lbl_tot), run_time=3.0)

        # Crossover at x = A/√2
        t_cross = np.arccos(1/np.sqrt(2)) / OMEGA
        cross_dot = Dot(ax.c2p(t_cross, 0.5), color=GOLD, radius=0.1)
        cross_lbl = MathTex(r"x=\frac{A}{\sqrt{2}}:\;KE=PE=0.50\,\mathrm{J}",
                             color=GOLD, font_size=20).next_to(cross_dot, UR, buff=0.1)
        self.play(FadeIn(cross_dot), Write(cross_lbl), run_time=0.8)

        # Two KE humps per PE hump
        two_hump = Text(
            "Two KE peaks per period — energy oscillates at 2ω",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(two_hump), run_time=0.8)
        self.wait(2.5)
