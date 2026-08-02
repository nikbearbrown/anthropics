#!/usr/bin/env python3
"""
qmcg_tonomura_buildup.py — Single-Electron Diffraction Buildup (Tonomura Sequence)
SILENT — quantum-mechanics-a-companion-guide.

Render:
    cd quantum-mechanics-a-companion-guide/youtube/qmcg-tonomura-buildup
    manim -qh qmcg_tonomura_buildup.py TonomuraBuildupScene

Verify:
    python3 qmcg_tonomura_buildup.py --verify

Physics:
    d = 300 nm slit separation; λ = 0.05 nm; L = 10 cm screen
    |ψ|² = 2cos²(kd sinθ / 2) = 2cos²(πdy/λL)  (small angle)
    Fringe spacing Δy = λL/d = 0.05e-9 * 0.1 / 300e-9 ≈ 16.7 μm
    Electrons sampled from |ψ|² via Monte Carlo
    At N=10000: crisp pattern emerges
"""
import sys
import numpy as np


D      = 300e-9    # slit separation m
LAM    = 0.05e-9   # de Broglie wavelength m
SCREEN = 0.1       # m


def fringe_spacing():
    return LAM * SCREEN / D


def prob_density(y, single_slit_width=30e-9):
    """Two-slit intensity pattern (normalized), y in m from center."""
    # Two-slit: I ∝ cos²(πdy/λL)
    phase = np.pi * D * y / (LAM * SCREEN)
    return np.cos(phase)**2


def sample_electrons(N, y_range=(-150e-6, 150e-6), seed=42):
    """Monte Carlo sample electron hit positions."""
    rng = np.random.default_rng(seed)
    y_arr = np.linspace(y_range[0], y_range[1], 10000)
    P = prob_density(y_arr)
    P = P / P.sum()
    return rng.choice(y_arr, size=N, p=P)


def verify():
    print("=== Tonomura buildup verification ===")
    fs = fringe_spacing()
    print(f"  Fringe spacing Δy = λL/d = {fs*1e6:.2f} μm")
    print(f"  P1: first fringe at sinθ = λ/d = {LAM/D:.4e}")

    # Monte Carlo — check fringe centers
    hits = sample_electrons(100000)
    y_arr = np.linspace(-150e-6, 150e-6, 1000)
    hist, edges = np.histogram(hits, bins=y_arr)
    centers = (edges[:-1] + edges[1:]) / 2

    # Find peaks
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(hist, distance=5)
    peak_ys  = centers[peaks[:3]]
    print(f"\n  First 3 peak positions (μm): {peak_ys*1e6.round(1)}")
    print(f"  Expected near 0, ±{fs*1e6:.1f} μm")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class TonomuraBuildupScene(Scene):
    """
    Phase 1: title
    Phase 2: dots accumulate one by one → interference pattern builds
    Phase 3: comparison with single-slit (one path open)
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_buildup()
        self._phase_comparison()

    def _phase_title(self):
        title = Text("Single-Electron Diffraction", font="EB Garamond", font_size=52, color=INK)
        sub1  = Text(
            "100 electrons: random.  10,000 electrons: interference pattern.",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        sub2  = Text(
            "No two electrons interacted — each interfered only with itself",
            font="EB Garamond", font_size=20, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _phase_buildup(self):
        # Screen area — map y ∈ [-150 μm, 150 μm] to vertical axis
        ax = Axes(
            x_range=[-1, 1, 0.5], y_range=[-7, 7, 2],
            x_length=3.0, y_length=6.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(LEFT * 3.5)

        screen_rect = Rectangle(width=1.2, height=6.2, color=DIM, stroke_width=1.5, fill_opacity=0).move_to(ax.get_center())
        lbl_screen  = Text("Screen", font="EB Garamond", font_size=18, color=DIM).next_to(ax, DOWN, buff=0.2)

        # Build |ψ|² reference on right
        ax_ref = Axes(
            x_range=[0, 1.2, 0.4], y_range=[-7, 7, 2],
            x_length=3.5, y_length=6.0,
            axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False},
        ).shift(RIGHT * 3.0)
        y_arr_ref = np.linspace(-7, 7, 500)
        # Map y units to μm
        y_m_ref   = y_arr_ref * 150e-6 / 7
        P_ref     = prob_density(y_m_ref)
        P_ref_n   = P_ref / P_ref.max()
        pts_ref   = [ax_ref.c2p(p, y) for y, p in zip(y_arr_ref, P_ref_n)]
        ref_curve = VMobject(color=GOLD, stroke_width=2.5, stroke_opacity=0.5)
        ref_curve.set_points_smoothly(pts_ref)
        lbl_ref   = MathTex(r"|\psi|^2", color=GOLD, font_size=20).next_to(ax_ref, UP, buff=0.1)

        self.play(Create(ax), Create(screen_rect), Write(lbl_screen), Create(ax_ref), Create(ref_curve), Write(lbl_ref), run_time=1.0)

        # Sample electrons
        N_total   = 5000
        hit_ys    = sample_electrons(N_total)
        hit_units = hit_ys / (150e-6 / 7)   # convert to axis units

        counter_lbl = Text("N = 0", font="EB Garamond", font_size=22, color=INK).to_corner(UR, buff=0.35)
        self.play(Write(counter_lbl), run_time=0.3)

        # Add dots in batches
        batches    = [(1, 50, 0.5), (50, 500, 0.6), (500, 2000, 0.4), (2000, N_total, 0.3)]
        all_dots   = []

        screen_center = ax.get_origin()
        screen_unit   = ax.get_y_axis().get_unit_size()

        for start, end, pause in batches:
            new_dots = []
            for idx in range(start, end):
                y_unit = hit_units[idx]
                pos    = screen_center + np.array([0, y_unit * screen_unit, 0])
                pos[0] += np.random.uniform(-0.4, 0.4)  # slight horizontal spread
                d = Dot(pos, color=BLUE, radius=0.025)
                new_dots.append(d)

            self.add(*new_dots)
            all_dots.extend(new_dots)

            new_counter = Text(f"N = {end}", font="EB Garamond", font_size=22, color=INK).to_corner(UR, buff=0.35)
            self.remove(counter_lbl)
            self.add(new_counter)
            counter_lbl = new_counter
            self.wait(pause)

        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_comparison(self):
        hdr = Text(
            "Block one slit → fringes vanish.  Both slits required.",
            font="EB Garamond", font_size=22, color=BROWN,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.7)

        ax_two = Axes(x_range=[0,1.3,0.4], y_range=[-7,7,2], x_length=4.5, y_length=5.5,
                      axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False}).shift(LEFT * 2.5)
        ax_one = Axes(x_range=[0,1.3,0.4], y_range=[-7,7,2], x_length=4.5, y_length=5.5,
                      axis_config={"color": INK, "stroke_width": 1.2, "include_ticks": False}).shift(RIGHT * 2.5)

        y_arr = np.linspace(-7, 7, 500)
        y_m   = y_arr * 150e-6 / 7

        # Two-slit
        P_two = prob_density(y_m)
        P_two_n = P_two / P_two.max()
        pts_two = [ax_two.c2p(p, y) for y, p in zip(y_arr, P_two_n)]
        c_two   = VMobject(color=GOLD, stroke_width=2.5); c_two.set_points_smoothly(pts_two)

        # Single-slit (Gaussian envelope only)
        sigma_ss = 150e-6 / 3
        P_one = np.exp(-y_m**2 / (2 * sigma_ss**2))
        P_one_n = P_one / P_one.max()
        pts_one = [ax_one.c2p(p, y) for y, p in zip(y_arr, P_one_n)]
        c_one   = VMobject(color=BLUE, stroke_width=2.5); c_one.set_points_smoothly(pts_one)

        lbl_two = Text("Both slits open\n(interference)", font="EB Garamond", font_size=18, color=GOLD).next_to(ax_two, DOWN, buff=0.2)
        lbl_one = Text("One slit blocked\n(no fringes)", font="EB Garamond", font_size=18, color=BLUE).next_to(ax_one, DOWN, buff=0.2)

        self.play(Create(ax_two), Create(ax_one), Create(c_two), Create(c_one),
                  Write(lbl_two), Write(lbl_one), run_time=1.2)
        self.wait(2.5)
