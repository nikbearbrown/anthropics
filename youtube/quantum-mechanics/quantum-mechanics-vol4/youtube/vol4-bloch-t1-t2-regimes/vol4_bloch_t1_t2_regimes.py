#!/usr/bin/env python3
"""
vol4_bloch_t1_t2_regimes.py — Bloch Equations: T₁ and T₂ Decay on One Sphere
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol4.

Physics (Bloch equations, ω₀ = 2π×1 MHz for visibility):
    ṙ_x = −ω₀r_y − r_x/T₂
    ṙ_y = +ω₀r_x − r_y/T₂
    ṙ_z = −(r_z + 1)/T₁

    Solution:
    r_x(t) = e^{−t/T₂} cos(ω₀t)
    r_y(t) = e^{−t/T₂} sin(ω₀t)
    r_z(t) = −1 + (1 + r_z₀) e^{−t/T₁}

Parameters: T₁ = 4 μs, T_φ = 4 μs → T₂ = 2 μs; ω₀ large for visible spirals

Verify:
    python3 vol4_bloch_t1_t2_regimes.py --verify
"""
import sys
import numpy as np

T1 = 4.0   # μs
TPHI = 4.0  # μs
T2 = 1.0 / (1.0/(2*T1) + 1.0/TPHI)  # = 2.0 μs

def bloch_trajectory(t_vals, r0=(1, 0, 0), omega0=5.0, T1=T1, T2=T2):
    """Exact Bloch trajectory; omega0 in rad/μs."""
    rx0, ry0, rz0 = r0
    # In rotating frame (ω₀ cancels), then rotate back
    # Solution in lab frame with initial (rx0, ry0, rz0):
    # Rotating frame: r_xy₀ = rx0 + i·ry0; decays as e^{-t/T2}
    # Lab frame: r_xy(t) = r_xy₀ · e^{-t/T2} · e^{i ω₀ t}
    r_xy0 = complex(rx0, ry0)
    r_xy  = r_xy0 * np.exp(-t_vals/T2) * np.exp(1j * omega0 * t_vals)
    rx    = r_xy.real
    ry    = r_xy.imag
    rz    = -1 + (1 + rz0) * np.exp(-t_vals/T1)
    return rx, ry, rz

def verify():
    print("=== Bloch T1/T2 verification ===")
    print(f"T1 = {T1} μs,  T_φ = {TPHI} μs,  T2 = {T2:.4f} μs")

    # P1: |ρ₀₁(T₂)| / |ρ₀₁(0)| = 1/e
    t_T2 = T2
    rx, ry, rz = bloch_trajectory(np.array([0.0, t_T2]), r0=(1, 0, 0))
    r_xy_0  = np.sqrt(rx[0]**2 + ry[0]**2)
    r_xy_T2 = np.sqrt(rx[1]**2 + ry[1]**2)
    ratio = r_xy_T2 / r_xy_0
    print(f"\nP1: |r_xy(T₂)| / |r_xy(0)| = {ratio:.6f}  (should be 1/e = {1/np.e:.6f})")
    assert abs(ratio - 1/np.e) < 1e-6, f"FAIL: ratio = {ratio:.6f}"

    # P2: T2 ≤ 2·T1
    print(f"\nP2: T₂ = {T2:.4f} μs,  2·T₁ = {2*T1:.4f} μs")
    print(f"    T₂ ≤ 2T₁?  {T2 <= 2*T1}")
    assert T2 <= 2*T1, "FAIL: T2 > 2T1"

    # Pure dephasing limit: T1 → ∞ → T2 = T_φ = 4 μs
    T2_pure_deph = TPHI
    print(f"\nPure dephasing (T1→∞): T₂ = T_φ = {T2_pure_deph} μs  (endpoint stays on z-axis)")
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


class BlochT1T2RegimesScene(Scene):
    """
    Bloch sphere with three trajectory segments:
    (1) Pure dephasing: equatorial spiral → z-axis
    (2) Pure T₁ decay: arc to south pole
    (3) Combined: diagonal spiral to south pole
    Side panel: |ρ₀₁(t)| decay curve.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._sphere_and_trajectories()
        self._side_panel()
        self._payoff()

    def _title(self):
        t = Text("Bloch Equations: T₁ and T₂ Regimes", font="EB Garamond",
                 font_size=50, color=INK)
        s = Text(
            "Pure dephasing ≠ relaxation to ground state  —  the endpoints differ",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.1)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _sphere_and_trajectories(self):
        # Draw a simple Bloch sphere using a circle in 3D-projected 2D
        SCALE = 2.2   # radius in Manim units

        sphere = Circle(radius=SCALE, color=DIM, stroke_width=1.5
                        ).shift(LEFT * 2.0)
        equator = Ellipse(width=SCALE*2, height=SCALE*0.65, color=DIM,
                          stroke_width=1.0, stroke_opacity=0.5).shift(LEFT * 2.0)
        # Axes
        z_ax = Arrow([LEFT*2.0 + DOWN*SCALE*1.1], [LEFT*2.0 + UP*(SCALE+0.4)],
                     color=INK, stroke_width=1.5, tip_length=0.18, buff=0)
        x_ax = Arrow([LEFT*2.0 + LEFT*SCALE*1.1], [LEFT*2.0 + RIGHT*(SCALE+0.3)],
                     color=INK, stroke_width=1.5, tip_length=0.18, buff=0)
        z_lbl = MathTex(r"|0\rangle", color=INK, font_size=20
                        ).next_to(z_ax.get_end(), UP, buff=0.05)
        neg_z = MathTex(r"|1\rangle", color=INK, font_size=20
                        ).next_to(z_ax.get_start(), DOWN, buff=0.05)

        north = Dot([LEFT*2.0 + UP*SCALE], color=GOLD, radius=0.08)
        south = Dot([LEFT*2.0 + DOWN*SCALE], color=GOLD, radius=0.08)

        self.play(Create(sphere), Create(equator),
                  Create(z_ax), Create(x_ax),
                  Write(z_lbl), Write(neg_z),
                  FadeIn(north), FadeIn(south), run_time=1.5)

        # ─── Trajectory 1: pure dephasing (equatorial spiral) ────────────
        t_vals = np.linspace(0, 3 * T2, 200)
        omega  = 5.0  # fast enough to show spirals in visual
        rx, ry, rz = bloch_trajectory(t_vals, r0=(1,0,0),
                                      omega0=omega, T1=1e6, T2=T2)
        # Project 3D → 2D (oblique): x → x + 0.3y, z → z
        def project(rx, ry, rz):
            px = SCALE * (rx + 0.3 * ry) + (-2.0)
            py = SCALE * rz
            return [px, py, 0]

        deph_pts = [project(rx[i], ry[i], rz[i]) for i in range(len(t_vals))]
        deph_curve = VMobject(color=BLUE, stroke_width=2.5)
        deph_curve.set_points_smoothly(deph_pts)
        deph_lbl = Text("Pure dephasing (T₁→∞)\nEndpoint: z-axis, not south pole",
                        font="EB Garamond", font_size=15, color=BLUE
                        ).to_edge(RIGHT, buff=0.3).shift(UP * 1.5)

        self.play(Create(deph_curve), Write(deph_lbl), run_time=1.5)
        self.wait(0.5)

        # ─── Trajectory 2: pure T₁ decay (no dephasing, r_xy→0, rz→−1) ─
        t_T1 = np.linspace(0, 3 * T1, 100)
        # Start from equator (0,0,0) projected
        rz_T1 = -1 + (1 + 0) * np.exp(-t_T1/T1)
        r_xy_T1 = np.exp(-t_T1/(2*T1))   # T2=2T1 in T1-only limit
        T1_pts = [project(r_xy_T1[i], 0, rz_T1[i]) for i in range(len(t_T1))]
        T1_curve = VMobject(color=BROWN, stroke_width=2.5)
        T1_curve.set_points_smoothly(T1_pts)
        T1_lbl = Text("Pure T₁ decay\nEndpoint: south pole |1⟩",
                      font="EB Garamond", font_size=15, color=BROWN
                      ).next_to(deph_lbl, DOWN, buff=0.25)

        self.play(Create(T1_curve), Write(T1_lbl), run_time=1.2)
        self.wait(0.5)

        # ─── Trajectory 3: combined ───────────────────────────────────────
        t_comb = np.linspace(0, 3 * T2, 300)
        rx_c, ry_c, rz_c = bloch_trajectory(t_comb, r0=(1,0,0),
                                             omega0=omega, T1=T1, T2=T2)
        comb_pts = [project(rx_c[i], ry_c[i], rz_c[i]) for i in range(len(t_comb))]
        comb_curve = VMobject(color=GOLD, stroke_width=2.5)
        comb_curve.set_points_smoothly(comb_pts)
        comb_lbl = Text("Combined (T₁=4μs, T₂=2μs)\nSpiral to south pole",
                        font="EB Garamond", font_size=15, color=GOLD
                        ).next_to(T1_lbl, DOWN, buff=0.25)

        self.play(Create(comb_curve), Write(comb_lbl), run_time=1.5)
        self.wait(1.5)

    def _side_panel(self):
        ax = Axes(
            x_range=[0, 6*T2, T2],
            y_range=[0, 1.1, 0.25],
            x_length=4.5,
            y_length=2.8,
            axis_config=dict(color=DIM, stroke_width=1.0,
                             include_ticks=True, tip_length=0.12),
        ).to_corner(DR, buff=0.4)

        xl = MathTex(r"t\;(\mu\mathrm{s})", color=DIM, font_size=16
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        yl = MathTex(r"|\rho_{01}|", color=DIM, font_size=16
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.05)

        t_s = np.linspace(0, 6*T2, 300)
        decay = np.exp(-t_s / T2)
        pts = [ax.c2p(t, d) for t, d in zip(t_s, decay)]
        decay_curve = VMobject(color=BLUE, stroke_width=2.5)
        decay_curve.set_points_smoothly(pts)

        # Mark T2 point
        dot_T2 = Dot(ax.c2p(T2, 1/np.e), radius=0.07, color=GOLD)
        T2_lbl  = MathTex(r"t=T_2:\;1/e", color=GOLD, font_size=14
                          ).next_to(dot_T2, UR, buff=0.05)

        hdr = Text("Off-diagonal decay", font="EB Garamond",
                   font_size=14, color=DIM).next_to(ax, UP, buff=0.05)

        self.play(Create(ax), Write(xl), Write(yl), Write(hdr), run_time=0.8)
        self.play(Create(decay_curve), FadeIn(dot_T2), Write(T2_lbl), run_time=0.8)
        self.wait(1.5)

    def _payoff(self):
        eqs = VGroup(
            MathTex(r"\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\varphi}",
                    color=INK, font_size=28),
            MathTex(r"T_2 \leq 2T_1\;\text{always}", color=GOLD, font_size=26),
            MathTex(r"T_1=4\mu\mathrm{s},\;T_\varphi=4\mu\mathrm{s}\;\Rightarrow\;T_2=2\mu\mathrm{s}",
                    color=BLUE, font_size=24),
        ).arrange(DOWN, buff=0.35).center()
        for eq in eqs:
            self.play(Write(eq), run_time=0.8)
        self.wait(3.0)
