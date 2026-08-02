#!/usr/bin/env python3
"""
vol3_tight_binding_dispersion.py — Tight-Binding Cosine Band and Sign Flip of Effective Mass
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics:
    E(k) = E₀ − 2t·cos(ka),  k ∈ [−π/a, π/a]
    Group velocity: v_g = (1/ℏ)·dE/dk = (2ta/ℏ)·sin(ka)
    Effective mass: m* = ℏ²/(d²E/dk²) = ℏ²/(2ta²)
    Parameters: a = 3 Å, t = 0.5 eV

Verify:
    python3 vol3_tight_binding_dispersion.py --verify
"""
import sys
import numpy as np

HBAR  = 6.582119569e-16  # eV·s
A_LAT = 3e-10            # m (lattice constant)
T_HOP = 0.5              # eV (hopping integral)
M_E   = 9.10938e-31      # kg
EV    = 1.602176634e-19  # J/eV

def E_band(k_over_pi_a):
    """E(k) in eV; k in units of π/a."""
    ka = k_over_pi_a * np.pi
    return -2 * T_HOP * np.cos(ka)

def eff_mass_bottom():
    """m* at k=0 in units of m_e"""
    m_star_J = (HBAR * EV)**2 / (2 * T_HOP * EV * A_LAT**2)
    return m_star_J / M_E

def group_velocity(ka):
    """v_g = (2ta/ℏ)sin(ka)  in m/s"""
    return (2 * T_HOP * EV * A_LAT / (HBAR * EV)) * np.sin(ka)

def verify():
    print("=== Tight-Binding Dispersion verification ===")
    print(f"a = {A_LAT*1e10:.0f} Å,  t = {T_HOP} eV,  Bandwidth = 4t = {4*T_HOP:.1f} eV")

    # P1: group velocity at k=π/2a = maximum
    ka_mid = np.pi / 2
    vg_max = group_velocity(ka_mid)
    print(f"\nP1: v_g at ka=π/2 = {vg_max:.4e} m/s")
    print(f"    v_g at ka=0   = {group_velocity(0):.4f} (should be 0)")
    print(f"    v_g at ka=π   = {group_velocity(np.pi):.4e} (should be ~0)")
    assert abs(group_velocity(0)) < 1e-10, "FAIL: vg at k=0 should be 0"
    assert abs(group_velocity(np.pi)) < 1e-6, "FAIL: vg at k=π should be 0"

    # P2: m* at band bottom
    mstar_bot = eff_mass_bottom()
    mstar_top = -eff_mass_bottom()  # sign flip
    print(f"\nP2: m* at band bottom = +{mstar_bot:.4f} m_e")
    print(f"    m* at band top    = {mstar_top:.4f} m_e  (negative — sign flip!)")
    assert mstar_bot > 0, "FAIL: m* at bottom should be positive"

    # Bandwidth
    bw = 4 * T_HOP
    print(f"\nBandwidth = 4t = {bw:.1f} eV  ✓")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
TEAL   = "#58C4DD"
ORANGE = "#CD853F"


class TightBindingDispersionScene(Scene):
    """
    Cosine E(k) band; parabola overlays at bottom (m*>0) and top (m*<0).
    Particle slides along curve; arrow shows group velocity.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._draw_band(ax)
        self._effective_mass_overlays(ax)
        self._sliding_particle(ax)
        self._payoff()

    def _title(self):
        t = Text("Tight-Binding Cosine Band", font="EB Garamond",
                 font_size=58, color=INK)
        s = Text(
            "Band bottom: m* > 0.  Band top: m* < 0.  The sign flip is a cosine.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[-1.1, 1.1, 0.5],
            y_range=[-1.15, 1.15, 0.5],
            x_length=9.0,
            y_length=6.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=True, tip_length=0.18),
        ).shift(DOWN * 0.2)

        xl = MathTex(r"k\;(\pi/a)", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        yl = MathTex(r"E(k) - E_0\;(\mathrm{eV})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)

        # BZ boundary lines
        bz_left  = DashedLine(ax.c2p(-1, -1.15), ax.c2p(-1, 1.15),
                              color=DIM, stroke_width=1.0, dash_length=0.1)
        bz_right = DashedLine(ax.c2p(1, -1.15), ax.c2p(1, 1.15),
                              color=DIM, stroke_width=1.0, dash_length=0.1)
        bz_lbl = Text("Brillouin Zone", font="EB Garamond", font_size=16, color=DIM
                      ).to_edge(UP, buff=0.18)

        self.play(Create(ax), Write(xl), Write(yl),
                  Create(bz_left), Create(bz_right), Write(bz_lbl), run_time=1.5)
        return ax

    def _draw_band(self, ax):
        k_vals = np.linspace(-1.0, 1.0, 400)
        E_vals = -2 * T_HOP * np.cos(k_vals * np.pi)   # eV, E₀=0
        pts = [ax.c2p(k, e) for k, e in zip(k_vals, E_vals)]
        curve = VMobject(color=GOLD, stroke_width=4)
        curve.set_points_smoothly(pts)
        lbl = MathTex(r"E(k) = E_0 - 2t\cos(ka)", color=GOLD, font_size=22
                      ).to_corner(UL, buff=0.35)
        self.play(Create(curve), Write(lbl), run_time=2.0)
        self.wait(0.8)
        return curve

    def _effective_mass_overlays(self, ax):
        # Parabola near band bottom (k≈0): E ≈ E_min + ℏ²k²/(2m*)
        # In our units: E_min = -2t = -1 eV; curvature = 2t
        k_bot = np.linspace(-0.45, 0.45, 200)
        E_bot = -2*T_HOP + 2*T_HOP * (k_bot*np.pi)**2  # small-angle cos expansion
        pts_bot = [ax.c2p(k, e) for k, e in zip(k_bot, E_bot)]
        para_bot = VMobject(color=BLUE, stroke_width=3)
        para_bot.set_points_smoothly(pts_bot)

        # Parabola near band top (k≈±1): E ≈ E_max − 2t(π(k∓1))²
        k_top = np.linspace(0.55, 1.0, 200)
        E_top_vals = 2*T_HOP - 2*T_HOP * ((k_top-1)*np.pi)**2
        pts_top = [ax.c2p(k, e) for k, e in zip(k_top, E_top_vals)]
        para_top = VMobject(color=BROWN, stroke_width=3)
        para_top.set_points_smoothly(pts_top)

        lbl_bot = Text("m* > 0 (bottom)", font="EB Garamond",
                       font_size=18, color=BLUE).next_to(ax.c2p(0, -0.7), DOWN, buff=0.05)
        lbl_top = Text("m* < 0 (top)", font="EB Garamond",
                       font_size=18, color=BROWN).next_to(ax.c2p(0.8, 0.7), UP, buff=0.05)

        mstar_val = eff_mass_bottom()
        mstar_lbl = MathTex(
            r"m^* = \pm " + f"{mstar_val:.2f}" + r"\,m_e",
            color=INK, font_size=22,
        ).to_corner(UR, buff=0.35)

        self.play(Create(para_bot), Write(lbl_bot), run_time=0.8)
        self.play(Create(para_top), Write(lbl_top), run_time=0.8)
        self.play(Write(mstar_lbl), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(para_bot, para_top, lbl_bot, lbl_top, mstar_lbl), run_time=0.4)

    def _sliding_particle(self, ax):
        # Slide particle from k=-1 to k=+1
        t_tracker = ValueTracker(-1.0)

        def particle_pos():
            k = t_tracker.get_value()
            E = -2 * T_HOP * np.cos(k * np.pi)
            return ax.c2p(k, E)

        dot = always_redraw(lambda: Dot(particle_pos(), radius=0.12, color=GOLD))

        def vg_arrow():
            k = t_tracker.get_value()
            ka = k * np.pi
            vg = np.sin(ka)   # proportional; sign determines direction
            start = particle_pos()
            end = np.array(start) + np.array([vg * 0.7, 0, 0])
            col = BLUE if vg >= 0 else BROWN
            if abs(vg) < 0.05:
                return VGroup()
            return Arrow(start, end, color=col, buff=0,
                         stroke_width=2.5, tip_length=0.18)

        arrow = always_redraw(vg_arrow)

        lbl = Text("Arrow = group velocity v_g = (1/ℏ)dE/dk",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(DOWN, buff=0.25)

        self.add(dot, arrow)
        self.play(Write(lbl), run_time=0.5)
        self.play(
            t_tracker.animate.set_value(1.0),
            run_time=5.0, rate_func=linear,
        )
        self.wait(1.0)
        self.play(FadeOut(dot, arrow, lbl), run_time=0.4)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"E(k) = E_0 - 2t\cos(ka)", color=GOLD, font_size=28),
            MathTex(r"m^* = \frac{\hbar^2}{2ta^2}\;\Rightarrow\;"
                    r"m^*_{\rm top} = -m^*_{\rm bot}",
                    color=INK, font_size=26),
            MathTex(r"\text{Bandwidth} = 4t = " + f"{4*T_HOP:.1f}" + r"\;\mathrm{eV}",
                    color=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.35).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.8)
        self.wait(3.0)
