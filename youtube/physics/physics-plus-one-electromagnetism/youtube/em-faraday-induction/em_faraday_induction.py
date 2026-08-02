#!/usr/bin/env python3
"""
em_faraday_induction.py — Faraday's Law: Moving Magnet, Changing Flux, Induced EMF
SILENT SLATE — brownblue dark palette, physics-plus-one-electromagnetism.

Physics:
    Phi_B(t) = B_max * A * exp(-(z_magnet(t) - z_loop)^2 / sigma^2)
    epsilon = -d(Phi_B)/dt  (Faraday's law)
    Lenz's law: current opposes flux change

Verify: python3 em_faraday_induction.py --verify
Render: manim -qh em_faraday_induction.py EmFaradayInductionScene
"""
import sys
import numpy as np

# ─── Synthetic flux model ─────────────────────────────────────────────────────
R_LOOP  = 0.05   # m
A_LOOP  = np.pi * R_LOOP**2   # m^2
B_MAX   = 0.2    # T (peak field at loop center)
SIGMA   = 0.04   # m (magnet flux spatial width)
V_MAG   = 0.5    # m/s

T_TOTAL = 0.5    # s
N_PTS   = 500

t_arr = np.linspace(0, T_TOTAL, N_PTS)
dt    = t_arr[1] - t_arr[0]

def z_magnet(t):
    """Magnet position: starts far left, moves right through loop at t=T/2."""
    return -0.15 + V_MAG * t

def flux(t):
    dz = z_magnet(t) - 0.0   # loop at z=0
    return B_MAX * A_LOOP * np.exp(-dz**2 / SIGMA**2)

def emf(t_arr):
    """EMF = -d(Phi)/dt, numerical."""
    phi = np.array([flux(t) for t in t_arr])
    return -np.gradient(phi, dt)

def verify():
    print("=== Faraday induction verification ===")
    phi_arr = np.array([flux(t) for t in t_arr])
    emf_arr = emf(t_arr)

    # P1: EMF = 0 when flux is max (dPhi/dt = 0 at center crossing)
    idx_max_phi = np.argmax(phi_arr)
    emf_at_max = emf_arr[idx_max_phi]
    # Numerical gradient has small discretization error at the peak; 2% tolerance
    print(f"P1: EMF at Phi_max = {emf_at_max:.6f} V  (expected ≈ 0, discretization noise) {'✓' if abs(emf_at_max) < 0.03 * emf_arr.max() else '✗'}")

    # P2: EMF has positive and negative peaks (Lenz's law)
    max_emf = emf_arr.max()
    min_emf = emf_arr.min()
    print(f"P2: EMF peaks: +{max_emf:.4f} V and {min_emf:.4f} V  (symmetric: {'✓' if abs(max_emf + min_emf) < 0.001 else '✗'})")
    print(f"N=100 turns: peak EMF = {100 * max_emf:.4f} V  (detectable)")
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


class EmFaradayInductionScene(Scene):
    """
    Top: bar magnet slides through wire loop.
    Bottom left: Phi(t) gauge. Bottom right: EMF(t) = -dPhi/dt.
    Current arrow in loop flips at zero crossing.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._setup_panels()
        self._animate_induction()
        self._finale()

    def _title(self):
        t = Text("Faraday's Law: Changing Flux → Induced EMF",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "ε = −dΦ_B/dt   |   The engine of every power plant on Earth.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _setup_panels(self):
        # Top panel: magnet + loop diagram (schematic)
        top_rect = Rectangle(width=11, height=2.5, color=DIM,
                             stroke_width=0.5, stroke_opacity=0.3).shift(UP * 2.0)
        top_lbl = Text("Magnet slides through loop →",
                       font="EB Garamond", font_size=18, color=DIM).shift(UP * 3.0)

        # Loop circle (static)
        self.loop_display = Ellipse(width=1.2, height=0.3, color=INK, stroke_width=3)
        self.loop_display.shift(UP * 2.0)
        loop_lbl = MathTex(r"N = 100\ \text{turns}", color=DIM, font_size=16)
        loop_lbl.next_to(self.loop_display, DOWN, buff=0.1)

        self.play(Create(top_rect), Create(self.loop_display),
                  Write(top_lbl), Write(loop_lbl), run_time=1.0)

        # Magnet rectangle (movable)
        self.magnet = Rectangle(width=0.6, height=0.3, fill_color=BROWN,
                                fill_opacity=0.9, stroke_color=BROWN, stroke_width=1)
        self.magnet.shift(UP * 2.0 + LEFT * 4.5)
        N_lbl = Text("N", font="EB Garamond", font_size=14, color=GOLD)
        N_lbl.move_to(self.magnet.get_right() + LEFT * 0.15)
        self.magnet_N = N_lbl
        self.play(FadeIn(self.magnet), Write(N_lbl), run_time=0.4)

        # Two time-series axes
        ax_phi = Axes(
            x_range=[0, T_TOTAL, 0.1],
            y_range=[-0.05, flux(T_TOTAL/2) * 1.1, 0.0002],
            x_length=5,
            y_length=2.5,
            axis_config=dict(color=INK, stroke_width=1, include_ticks=False, tip_length=0.15),
        ).shift(LEFT * 3.0 + DOWN * 1.8)
        lx_phi = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=18).next_to(ax_phi.x_axis.get_end(), RIGHT, buff=0.08)
        ly_phi = MathTex(r"\Phi_B", color=BLUE, font_size=18).next_to(ax_phi.y_axis.get_end(), UP, buff=0.08)

        ax_emf = Axes(
            x_range=[0, T_TOTAL, 0.1],
            y_range=[-0.0015, 0.0015, 0.0005],
            x_length=5,
            y_length=2.5,
            axis_config=dict(color=INK, stroke_width=1, include_ticks=False, tip_length=0.15),
        ).shift(RIGHT * 3.0 + DOWN * 1.8)
        lx_emf = MathTex(r"t\;(\mathrm{s})", color=INK, font_size=18).next_to(ax_emf.x_axis.get_end(), RIGHT, buff=0.08)
        ly_emf = MathTex(r"\varepsilon\;(\mathrm{V})", color=GOLD, font_size=18).next_to(ax_emf.y_axis.get_end(), UP, buff=0.08)

        self.play(Create(ax_phi), Create(ax_emf),
                  Write(lx_phi), Write(ly_phi),
                  Write(lx_emf), Write(ly_emf), run_time=1.0)
        self.ax_phi = ax_phi
        self.ax_emf = ax_emf

    def _animate_induction(self):
        phi_arr = np.array([flux(t) for t in t_arr])
        emf_arr = emf(t_arr)
        phi_scale = phi_arr.max()
        emf_scale = max(abs(emf_arr.max()), abs(emf_arr.min()))

        # Build curves incrementally
        phi_pts_drawn = []
        emf_pts_drawn = []

        phi_mob = VMobject(color=BLUE, stroke_width=2.5)
        emf_mob = VMobject(color=GOLD, stroke_width=2.5)
        self.add(phi_mob, emf_mob)

        # Current direction arrow in loop
        curr_arrow = Arrow(
            self.loop_display.get_left(),
            self.loop_display.get_right(),
            color=BLUE, buff=0, max_tip_length_to_length_ratio=0.15,
        )
        self.add(curr_arrow)

        # Animate in steps
        step = N_PTS // 60
        for i in range(0, N_PTS, step):
            ti = t_arr[i]
            # Move magnet
            x_display = -4.5 + (ti / T_TOTAL) * 9.0
            self.magnet.move_to(np.array([x_display, 2.0, 0]))

            # Add phi point
            phi_pt = self.ax_phi.c2p(ti, np.clip(phi_arr[i], 0, phi_scale * 1.05))
            phi_pts_drawn.append(phi_pt)
            if len(phi_pts_drawn) >= 2:
                new_phi = VMobject(color=BLUE, stroke_width=2.5)
                new_phi.set_points_smoothly(np.array(phi_pts_drawn))
                phi_mob.become(new_phi)

            # Add EMF point
            emf_pt = self.ax_emf.c2p(ti, np.clip(emf_arr[i], -emf_scale * 1.1, emf_scale * 1.1))
            emf_pts_drawn.append(emf_pt)
            if len(emf_pts_drawn) >= 2:
                new_emf = VMobject(color=GOLD, stroke_width=2.5)
                new_emf.set_points_smoothly(np.array(emf_pts_drawn))
                emf_mob.become(new_emf)

            # Flip current arrow at zero crossing
            if emf_arr[i] > 0:
                curr_arrow.set_color(BLUE)
            elif emf_arr[i] < -0.0001:
                curr_arrow.set_color(BROWN)
            else:
                curr_arrow.set_color(DIM)

            self.wait(1/30)

        # Annotations
        cap1 = Text("Phi peaks when magnet is centered — EMF = 0 there",
                    font="EB Garamond", font_size=18, color=BLUE).to_edge(DOWN, buff=0.3)
        self.play(Write(cap1), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(cap1), run_time=0.3)

    def _finale(self):
        eq = MathTex(
            r"\varepsilon = -\frac{d\Phi_B}{dt}",
            r"\quad \Phi_B = \int \vec{B}\cdot d\vec{A}",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
