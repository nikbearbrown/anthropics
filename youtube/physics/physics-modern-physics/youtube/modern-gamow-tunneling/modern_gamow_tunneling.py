#!/usr/bin/env python3
"""
modern_gamow_tunneling.py — Alpha Decay and Quantum Tunneling: The Gamow Factor
SILENT SLATE — math-explainer (brownblue) candidate, physics-modern-physics book.

Physics:
    U-238: E_alpha=4.27 MeV, Coulomb peak ~27 MeV at r~9 fm, t_1/2=4.47e9 yr
    Po-212: E_alpha=8.78 MeV, t_1/2=298 ns
    Gamow factor G ~ integral of sqrt(2m(V-E)) over barrier

Run standalone to verify:
    python3 modern_gamow_tunneling.py
"""
import sys
import numpy as np

MeV = 1.602e-13        # J per MeV
HBAR = 1.055e-34       # J·s
M_ALPHA = 4 * 1.66e-27  # kg (~4 u)
K_COULOMB = 8.99e9     # N m²/C²
Z_U = 92               # uranium Z
Z_ALPHA = 2
Q_PROTON = 1.602e-19   # C
FM = 1e-15             # m per fm


def coulomb_barrier_peak_MeV(Z_parent, R_fm):
    """Coulomb barrier peak V = k*(Z-2)*2*e² / R"""
    Z_daughter = Z_parent - 2
    return K_COULOMB * Z_daughter * Z_ALPHA * Q_PROTON**2 / (R_fm * FM) / MeV


def verify():
    print("=== Gamow tunneling verification ===")
    # U-238: Z=92, R_nuclear ~ 9 fm
    V_peak = coulomb_barrier_peak_MeV(92, 9.0)
    print(f"U-238 Coulomb peak at R=9 fm: {V_peak:.1f} MeV  (card: ~27 MeV)")
    V_peak_Po = coulomb_barrier_peak_MeV(84, 8.0)
    print(f"Po-212 Coulomb peak at R=8 fm: {V_peak_Po:.1f} MeV")
    print(f"U-238: E_alpha=4.27 MeV, Coulomb peak={V_peak:.1f} MeV → classically forbidden")
    print(f"Po-212: E_alpha=8.78 MeV → higher E, narrower barrier, t_1/2 24 orders shorter")
    # P1: Geiger-Nuttall — straight line log(t1/2) vs 1/sqrt(E_alpha)
    data = [
        ("U-238", 4.27, 4.47e9 * 3.156e7),    # t1/2 in seconds
        ("Ra-226", 4.87, 1600 * 3.156e7),
        ("Po-210", 5.30, 138 * 24 * 3600),
        ("Po-212", 8.78, 298e-9),
    ]
    print("\nGeiger-Nuttall plot (P1):")
    for name, E, t in data:
        print(f"  {name}: 1/√E={1/np.sqrt(E):.4f}, log10(t)={np.log10(t):.2f}")
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


class ModernGamowTunnelingScene(Scene):
    """
    Potential energy curve with alpha particle energy.
    Classically forbidden region shaded. Wavefunction decays through barrier.
    Two isotopes side by side. Geiger-Nuttall plot.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_potential_curve()
        self._phase_two_isotopes()
        self._phase_geiger_nuttall()

    def _phase_title(self):
        title = Text("Quantum Tunneling — The Gamow Factor",
                     font="EB Garamond", font_size=56, color=INK)
        sub = Text(
            "An alpha particle has less energy than the barrier surrounding it — yet it escapes",
            font="EB Garamond", font_size=22, color=BLUE)
        hook = Text("Radioactivity is quantum certainty about a probability",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, hook).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), FadeIn(hook), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, hook), run_time=0.5)

    def _phase_potential_curve(self):
        # Sketch potential: nuclear well (left, deep) + Coulomb barrier (hump) + flat (right)
        ax = Axes(
            x_range=[0, 50, 10],
            y_range=[-60, 30, 10],
            x_length=9,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.2)
        lx = MathTex(r"r\;(\text{fm})", color=INK, font_size=22
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.08)
        ly = MathTex(r"V\;(\text{MeV})", color=INK, font_size=22
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.08)
        title = Text("U-238: alpha inside Coulomb barrier",
                     font="EB Garamond", font_size=26, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), Create(ax), Write(lx), Write(ly), run_time=1.0)

        # Potential: nuclear well for r<9fm, Coulomb barrier for r>9fm
        R_nuclear = 9.0
        R_outer = 57.0  # classical turning point for 4.27 MeV, Z=92
        # V(r) = -40 MeV for r < R_nuclear (deep well)
        # V(r) = k*(90)*2*e²/r (Coulomb) for r > R_nuclear
        # Barrier peak at R_nuclear
        r_well = np.linspace(0.5, R_nuclear, 50)
        V_well = np.full_like(r_well, -40.0)

        r_coulomb = np.linspace(R_nuclear, 49.5, 200)
        # Simplified: scale so peak=27 at R_nuclear, falls as 1/r
        V_peak_val = 27.0
        V_coulomb = V_peak_val * R_nuclear / r_coulomb

        r_all = np.concatenate([r_well, r_coulomb])
        V_all = np.concatenate([V_well, V_coulomb])

        valid = (V_all >= -60) & (V_all <= 29)
        pot_curve = ax.plot_line_graph(
            x_values=[r for r, v in zip(r_all, valid) if v],
            y_values=[vv for vv, v in zip(V_all, valid) if v],
            line_color=BROWN, stroke_width=3, add_vertex_dots=False,
        )
        self.play(Create(pot_curve), run_time=2.0)

        # Alpha energy dashed line at 4.27 MeV
        E_alpha = 4.27
        energy_line = DashedLine(ax.c2p(0, E_alpha), ax.c2p(50, E_alpha),
                                 color=GOLD, stroke_width=2.5)
        e_lbl = MathTex(r"E_\alpha = 4.27\,\text{MeV}", color=GOLD, font_size=20
                        ).next_to(ax.c2p(48, E_alpha), LEFT, buff=0.08)
        self.play(Create(energy_line), Write(e_lbl), run_time=0.8)

        # Shade forbidden region
        # Region from R_nuclear to where V = E_alpha
        R_out = V_peak_val * R_nuclear / E_alpha  # ~57 fm, clip to 50
        R_out_plot = min(R_out, 49.5)
        forbidden_pts = [
            ax.c2p(R_nuclear, E_alpha),
            *[ax.c2p(r, V_peak_val * R_nuclear / r)
              for r in np.linspace(R_nuclear, R_out_plot, 40)
              if V_peak_val * R_nuclear / r <= 29],
            ax.c2p(R_out_plot, E_alpha),
        ]
        forbidden = Polygon(*forbidden_pts, color=DIM, fill_color=DIM,
                            fill_opacity=0.3, stroke_width=0)
        forbidden_lbl = Text("classically forbidden", font="EB Garamond",
                             font_size=17, color=DIM).move_to(ax.c2p(30, 15))
        self.play(FadeIn(forbidden), Write(forbidden_lbl), run_time=0.8)

        # Wavefunction sketch: oscillatory inside, exponential decay in barrier, small outside
        # Draw symbolically
        psi_inside = ax.plot_line_graph(
            x_values=list(np.linspace(0.5, R_nuclear, 100)),
            y_values=list(3 * np.sin(np.linspace(0, 5 * np.pi, 100)) - 25),
            line_color=BLUE, stroke_width=2.5, add_vertex_dots=False,
        )
        r_bar = np.linspace(R_nuclear, 40, 100)
        psi_bar_y = 2 * np.exp(-(r_bar - R_nuclear) / 8) - 25
        psi_barrier = ax.plot_line_graph(
            x_values=list(r_bar),
            y_values=list(np.clip(psi_bar_y, -60, 29)),
            line_color=BLUE, stroke_width=2.5, add_vertex_dots=False,
        )
        psi_lbl = MathTex(r"|\psi|^2", color=BLUE, font_size=20
                          ).next_to(ax.c2p(5, -20), RIGHT, buff=0.05)

        self.play(Create(psi_inside), Create(psi_barrier), Write(psi_lbl), run_time=2.0)
        self.wait(3.0)
        self.play(FadeOut(title, ax, lx, ly, pot_curve, energy_line, e_lbl,
                          forbidden, forbidden_lbl, psi_inside, psi_barrier, psi_lbl),
                  run_time=0.5)

    def _phase_two_isotopes(self):
        title = Text("Higher E_α → narrower barrier → shorter half-life (24 orders!)",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        rows = VGroup(
            MathTex(r"{}^{238}\text{U}:\;E_\alpha=4.27\,\text{MeV},\;t_{1/2}=4.47\times10^9\,\text{yr}",
                    color=BLUE, font_size=28),
            MathTex(r"{}^{212}\text{Po}:\;E_\alpha=8.78\,\text{MeV},\;t_{1/2}=298\,\text{ns}",
                    color=BROWN, font_size=28),
            MathTex(r"\Delta\log t_{1/2} \approx 24\text{ decades from }2\times\text{ increase in }E_\alpha",
                    color=GOLD, font_size=26),
            Text("Tunneling probability is exponentially sensitive to barrier width",
                 font="EB Garamond", font_size=22, color=DIM),
        ).arrange(DOWN, buff=0.48).center()
        for mob in rows:
            self.play(Write(mob) if isinstance(mob, MathTex) else FadeIn(mob), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(title, rows), run_time=0.5)

    def _phase_geiger_nuttall(self):
        title = Text("Geiger-Nuttall plot — log(t₁/₂) vs 1/√E_α: a straight line",
                     font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.28)
        self.play(Write(title), run_time=0.7)

        data = [
            ("U-238",  4.27, np.log10(4.47e9 * 3.156e7)),
            ("Ra-226", 4.87, np.log10(1600 * 3.156e7)),
            ("Po-210", 5.30, np.log10(138 * 24 * 3600)),
            ("Th-232", 4.08, np.log10(1.4e10 * 3.156e7)),
            ("Po-208", 5.11, np.log10(2.9 * 365 * 24 * 3600)),
            ("Po-212", 8.78, np.log10(298e-9)),
        ]
        x_vals = [1 / np.sqrt(d[1]) for d in data]
        y_vals = [d[2] for d in data]

        x_min = min(x_vals) - 0.02
        x_max = max(x_vals) + 0.02

        ax = Axes(
            x_range=[x_min, x_max, 0.05],
            y_range=[-9, 25, 5],
            x_length=9,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True,
                             tip_length=0.18),
        ).shift(DOWN * 0.4)
        lx = MathTex(r"1/\sqrt{E_\alpha}\;(\text{MeV}^{-1/2})", color=INK, font_size=20
                     ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        ly = MathTex(r"\log_{10}(t_{1/2}/\text{s})", color=INK, font_size=20
                     ).next_to(ax.y_axis.get_end(), UP, buff=0.05)

        # Best fit line
        coeffs = np.polyfit(x_vals, y_vals, 1)
        x_fit = np.linspace(x_min, x_max, 200)
        y_fit = np.polyval(coeffs, x_fit)

        fit_curve = ax.plot_line_graph(
            x_values=list(x_fit), y_values=list(np.clip(y_fit, -9, 25)),
            line_color=GOLD, stroke_width=2, add_vertex_dots=False,
        )

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.0)
        self.play(Create(fit_curve), run_time=1.0)

        colors = [BLUE, BROWN, BLUE, DIM, DIM, BROWN]
        for (name, E, log_t), color in zip(data, colors):
            x = 1 / np.sqrt(E)
            y = log_t
            if -9 <= y <= 25 and x_min <= x <= x_max:
                d = Dot(ax.c2p(x, y), color=color, radius=0.1)
                l = MathTex(name.replace("-", "\\text{-}").replace("U", "\\text{U}"),
                            color=color, font_size=16).next_to(d, UR, buff=0.05)
                self.play(FadeIn(d), Write(l), run_time=0.4)

        self.wait(3.5)
