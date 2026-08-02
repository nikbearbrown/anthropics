#!/usr/bin/env python3
"""
vol3_geiger_nuttall_law.py — Geiger-Nuttall Law: 24 Decades from One Exponent
SILENT SLATE — MANIM-lane simulation, quantum-mechanics-vol3.

Physics (WKB Gamow factor for alpha decay):
    Gamow exponent γ ≈ πZ′e²√(2m_α) / (ℏ·√E_α)   (leading term)
    Half-life: log₁₀(τ) ≈ A(Z′) + B(Z′)/√E_α    (Geiger-Nuttall law)

Alpha-emitter data (NNDC / literature):
    Isotope   Z′   E_α(MeV)   τ₁/₂
    Po-212    82   8.78       3.0e-7 s
    Po-214    82   7.69       164e-6 s
    Po-218    82   6.00       186 s
    Ra-226    86   4.87       5.05e10 s
    U-238     90   4.27       1.41e17 s  (4.47 Gyr)
    Th-232    90   4.08       4.42e17 s  (14.0 Gyr)

Verify:
    python3 vol3_geiger_nuttall_law.py --verify
"""
import sys
import numpy as np

# Nuclide data: (symbol, Z_daughter, E_alpha_MeV, half_life_s)
NUCLIDES = [
    ("Po-212",  82,  8.78,  3.0e-7),
    ("Po-214",  82,  7.69,  1.64e-4),
    ("Po-218",  82,  6.00,  186.0),
    ("Ra-226",  86,  4.87,  5.05e10),
    ("U-238",   90,  4.27,  1.41e17),
    ("Th-232",  90,  4.08,  4.42e17),
]

def log10_halflife(data):
    return [(sym, z, e, np.log10(tau)) for sym, z, e, tau in data]

def verify():
    print("=== Geiger-Nuttall verification ===")
    data = log10_halflife(NUCLIDES)
    print(f"{'Isotope':<10} {'Z′':>4} {'E_α(MeV)':>10} {'log₁₀(τ/s)':>12} {'1/√E_α':>10}")
    for sym, z, e, lgtau in data:
        print(f"{sym:<10} {z:>4} {e:>10.2f} {lgtau:>12.2f} {1/np.sqrt(e):>10.4f}")

    # P1: Linear fit of log10(τ) vs 1/√E for each Z-series
    po_data  = [(e, lt) for s,z,e,lt in data if z == 82]
    u_th_data = [(e, lt) for s,z,e,lt in data if z in (90,)]

    xs_po  = np.array([1/np.sqrt(e) for e,lt in po_data])
    ys_po  = np.array([lt for e,lt in po_data])
    slope_po, intercept_po = np.polyfit(xs_po, ys_po, 1)
    print(f"\nPo-series (Z′=82) linear fit: slope = {slope_po:.2f}, intercept = {intercept_po:.2f}")
    print("  R² =", np.corrcoef(xs_po, ys_po)[0,1]**2)

    # P2: Po-212 vs U-238 half-life ratio
    tau_po212 = 10 ** [lt for s,z,e,lt in data if s=="Po-212"][0]
    tau_u238  = 10 ** [lt for s,z,e,lt in data if s=="U-238"][0]
    ratio = tau_u238 / tau_po212
    print(f"\nτ(U-238)/τ(Po-212) = {ratio:.2e}  (should be ~{1.41e17/3e-7:.1e})")
    assert ratio > 1e20, "FAIL: ratio should span many decades"
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


class GeigerNuttallLawScene(Scene):
    """
    Semi-log Geiger-Nuttall plot: log₁₀(τ₁/₂) vs 1/√E_α.
    Points appear one by one; best-fit line appears; inset shows Coulomb barrier.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._plot_points(ax)
        self._barrier_inset()
        self._payoff()

    def _title(self):
        t = Text("Geiger-Nuttall Law", font="EB Garamond",
                 font_size=60, color=INK)
        s = Text(
            "24 decades of half-lives — one straight line, one exponent",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.3).center()
        self.play(Write(t), run_time=1.2)
        self.play(FadeIn(s), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        ax = Axes(
            x_range=[0.33, 0.50, 0.04],
            y_range=[-8, 20, 5],
            x_length=8.5,
            y_length=5.8,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=True, tip_length=0.18),
        ).shift(LEFT * 0.5 + DOWN * 0.3)

        xl = MathTex(r"1/\sqrt{E_\alpha}\;\;(\mathrm{MeV}^{-1/2})",
                     color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        yl = MathTex(r"\log_{10}(\tau_{1/2}/\mathrm{s})",
                     color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Geiger-Nuttall plot", font="EB Garamond",
                   font_size=20, color=DIM).next_to(ax, UP, buff=0.12)

        self.play(Create(ax), Write(xl), Write(yl), Write(hdr), run_time=1.5)
        return ax

    def _plot_points(self, ax):
        data = log10_halflife(NUCLIDES)

        po_pts  = [(1/np.sqrt(e), lt, sym, BLUE)
                   for sym,z,e,lt in data if z == 82]
        oth_pts = [(1/np.sqrt(e), lt, sym, BROWN)
                   for sym,z,e,lt in data if z != 82]

        all_pts = po_pts + oth_pts

        dots = []
        for x, y, sym, col in all_pts:
            dot = Dot(ax.c2p(x, y), radius=0.10, color=col)
            lbl = Text(sym, font="EB Garamond", font_size=16, color=col
                       ).next_to(dot, UR, buff=0.06)
            self.play(FadeIn(dot), Write(lbl), run_time=0.4)
            dots.append((x, y, col))

        self.wait(0.8)

        # Best-fit lines per Z-series
        def fit_line(pts_list, color):
            xs = np.array([p[0] for p in pts_list])
            ys = np.array([p[1] for p in pts_list])
            m, b = np.polyfit(xs, ys, 1)
            x0, x1 = xs.min() - 0.01, xs.max() + 0.01
            line = Line(ax.c2p(x0, m*x0+b), ax.c2p(x1, m*x1+b),
                        color=color, stroke_width=2.5)
            return line, m, b

        po_data_xy = [(x,y) for x,y,c in dots if c == BLUE]
        oth_data_xy = [(x,y) for x,y,c in dots if c == BROWN]

        if len(po_data_xy) >= 2:
            line_po, m_po, b_po = fit_line(po_data_xy, BLUE)
            self.play(Create(line_po), run_time=0.8)

        # Span annotation
        span = MathTex(r"\Delta\log_{10}\tau \approx 24\;\text{decades}",
                       color=GOLD, font_size=22).to_corner(DR, buff=0.3)
        self.play(Write(span), run_time=0.8)
        self.wait(1.5)

    def _barrier_inset(self):
        # Simple Coulomb barrier diagram in the corner
        ax_b = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 8, 2],
            x_length=3.8,
            y_length=2.8,
            axis_config=dict(color=DIM, stroke_width=1.0,
                             include_ticks=False, tip_length=0.12),
        ).to_corner(UR, buff=0.3)

        # Coulomb barrier shape: V(r) = k/r for r > R_nuc
        r_vals = np.linspace(0.8, 10, 200)
        v_vals = np.clip(5.5 / r_vals, 0, 8)
        barrier_pts = [ax_b.c2p(r, v) for r, v in zip(r_vals, v_vals)]
        barrier = VMobject(color=BROWN, stroke_width=2.5)
        barrier.set_points_smoothly(barrier_pts)

        # E_alpha line
        e_line = DashedLine(ax_b.c2p(0, 2.5), ax_b.c2p(10, 2.5),
                            color=GOLD, stroke_width=1.5, dash_length=0.1)
        e_lbl = MathTex(r"E_\alpha", color=GOLD, font_size=16
                        ).next_to(ax_b.c2p(10, 2.5), RIGHT, buff=0.05)

        # Shaded forbidden zone (classically forbidden)
        # Between r_c (classical turning pt) and r_nuc
        r_c = 5.5 / 2.5   # = 2.2
        shield_pts = [
            ax_b.c2p(0.8, 2.5), ax_b.c2p(r_c, 2.5),
        ] + [ax_b.c2p(r, np.clip(5.5/r, 2.5, 8)) for r in np.linspace(0.8, r_c, 30)]
        forbidden = Polygon(
            *shield_pts,
            color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=0,
        )

        hdr_b = Text("Coulomb barrier", font="EB Garamond",
                     font_size=14, color=DIM).next_to(ax_b, UP, buff=0.05)

        self.play(
            Create(ax_b), Create(barrier), Create(e_line),
            Write(e_lbl), FadeIn(forbidden), Write(hdr_b),
            run_time=1.2,
        )
        self.wait(1.5)

    def _payoff(self):
        gn = MathTex(
            r"\log_{10}\tau_{1/2} = A(Z') + \frac{B(Z')}{\sqrt{E_\alpha}}",
            color=INK, font_size=30,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(gn), run_time=1.2)
        self.wait(3.0)
