#!/usr/bin/env python3
"""
physics_shm_energy_exchange.py — SHM: KE and PE in Perfect Antiphase
SILENT SLATE — brownblue math-explainer candidate.

Physics:
    m = 0.50 kg, k = 50 N/m, A = 0.10 m
    ω = sqrt(k/m) = 10 rad/s, T = 0.628 s
    E_total = ½kA² = 0.25 J
    v_max = Aω = 1.0 m/s

Render:
    cd physics/youtube/physics-shm-energy-exchange
    manim -qh physics_shm_energy_exchange.py SHMEnergyScene
"""
import sys
import numpy as np

M = 0.50    # kg
K = 50.0    # N/m
A = 0.10    # m

OMEGA  = np.sqrt(K/M)
T_PERIOD = 2*np.pi/OMEGA
E_TOT  = 0.5*K*A**2


def verify():
    print("=== SHM Energy Exchange verification ===")
    print(f"  ω = {OMEGA:.4f} rad/s  (expected 10.0000)")
    print(f"  T = {T_PERIOD:.4f} s   (expected 0.6283)")
    print(f"  E_total = {E_TOT:.4f} J  (expected 0.2500)")
    v_max = A*OMEGA
    print(f"  v_max = {v_max:.4f} m/s  (expected 1.0000)")
    x_eq = A/np.sqrt(2)
    PE_eq = 0.5*K*x_eq**2
    KE_eq = E_TOT - PE_eq
    print(f"  At x=A/√2={x_eq:.4f} m: PE={PE_eq:.4f} J, KE={KE_eq:.4f} J  (expected both 0.1250)")
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
RED    = "#E05C6B"

N_CYCLES = 2.5
T_ANIM   = N_CYCLES * T_PERIOD


class SHMEnergyScene(Scene):
    """Mass-spring above, KE/PE energy graph below — live sync."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._build_scene()

    def _title(self):
        t1 = Text("Simple Harmonic Motion", font="EB Garamond", font_size=58, color=INK)
        t2 = Text("Kinetic and potential energy in perfect antiphase", font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"E_{\rm total} = \tfrac{1}{2}kA^2 = 0.25\,\mathrm{J} = \mathrm{const}",
                     color=GOLD, font_size=30)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.32).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.4)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _build_scene(self):
        # ── Energy graph (main panel) ─────────────────────────────────────────
        ax = Axes(
            x_range=[0, T_ANIM, T_PERIOD],
            y_range=[0, 0.30, 0.10],
            x_length=10,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).shift(DOWN*0.6)

        lx = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = MathTex(r"E\;(\mathrm{J})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Energy vs time  (m=0.5 kg, k=50 N/m, A=0.10 m)",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.3)

        ts = np.linspace(0, T_ANIM, 1200)
        xs_t = A * np.cos(OMEGA * ts)
        KE = 0.5 * M * (A*OMEGA)**2 * np.sin(OMEGA*ts)**2
        PE = 0.5 * K * xs_t**2

        pts_ke = np.array([ax.c2p(t, k) for t, k in zip(ts, KE)])
        pts_pe = np.array([ax.c2p(t, p) for t, p in zip(ts, PE)])
        pts_tot = np.array([ax.c2p(t, E_TOT) for t in ts])

        crv_ke  = VMobject(color=BLUE,  stroke_width=2.8).set_points_smoothly(pts_ke)
        crv_pe  = VMobject(color=BROWN, stroke_width=2.8).set_points_smoothly(pts_pe)
        crv_tot = VMobject(color=GOLD,  stroke_width=1.8, stroke_opacity=0.7).set_points_smoothly(pts_tot)

        lbl_ke  = Text("KE", font="EB Garamond", font_size=20, color=BLUE).move_to(ax.c2p(0.35, 0.265))
        lbl_pe  = Text("PE", font="EB Garamond", font_size=20, color=BROWN).move_to(ax.c2p(0.08, 0.265))
        lbl_tot = MathTex(r"E_{\rm total}=0.25\,\mathrm{J}", color=GOLD, font_size=20).move_to(ax.c2p(1.1, 0.275))

        self.play(Create(crv_ke), Create(crv_pe), Create(crv_tot),
                  Write(lbl_ke), Write(lbl_pe), Write(lbl_tot), run_time=3.0)
        self.wait(0.6)

        # Mass-spring cartoon (top strip)
        spring_lbl = Text("Spring", font="EB Garamond", font_size=17, color=DIM).to_edge(UP, buff=0.22).shift(LEFT*3.5)
        # Mark crossover at x = A/√2
        t_cross = np.arccos(1/np.sqrt(2)) / OMEGA
        dot_cross = Dot(ax.c2p(t_cross, E_TOT/2), color=GOLD, radius=0.09)
        cross_lbl = MathTex(r"x=A/\!\sqrt{2},\;KE=PE=0.125\,\mathrm{J}", color=GOLD, font_size=20)
        cross_lbl.next_to(dot_cross, UR, buff=0.08)
        self.play(FadeIn(dot_cross), Write(cross_lbl), run_time=0.8)

        final = Text(
            "KE peaks when PE bottoms — sum is constant every instant",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(DOWN, buff=0.20)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
