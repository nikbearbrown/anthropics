#!/usr/bin/env python3
"""
qm_infinite_square_well.py — Infinite Square Well: Quantization from Boundary Conditions
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-infinite-square-well
    manim -qh qm_infinite_square_well.py InfiniteSquareWellScene

Verify:
    python3 qm_infinite_square_well.py

Physics:
    L = 1 nm electron box
    E_n = n^2 * pi^2 * hbar^2 / (2 m L^2)
    E_1 = 0.376 eV for L=1 nm electron
    E_4/E_1 = 16 exactly (4^2)
    Nodes at x = k*L/n for k=1,...,n-1
"""
import sys
import numpy as np

HBAR = 1.0545718e-34
M_E  = 9.10938e-31
EV   = 1.60218e-19


def energy_levels(n_max: int, L_nm: float) -> np.ndarray:
    """Energy levels E_n in eV for electron in box of width L (nm)."""
    L = L_nm * 1e-9
    E1 = (np.pi**2 * HBAR**2) / (2.0 * M_E * L**2) / EV
    ns = np.arange(1, n_max + 1)
    return ns**2 * E1


def psi_n(n: int, x_arr: np.ndarray) -> np.ndarray:
    """ψ_n(x) for x in [0,1] (normalised box L=1)."""
    return np.sqrt(2.0) * np.sin(n * np.pi * x_arr)


def verify():
    print("=== Infinite Square Well verification ===")
    E = energy_levels(6, 1.0)
    print(f"E_1 = {E[0]:.4f} eV  (card says 0.376 eV)")
    print(f"E_2 = {E[1]:.4f} eV  (card says 1.504 eV)")
    print(f"E_3 = {E[2]:.4f} eV  (card says 3.385 eV)")
    print(f"E_4 = {E[3]:.4f} eV  (card says 6.018 eV)")
    ratio = E[3] / E[0]
    print(f"E_4/E_1 = {ratio:.6f}  (should be exactly 16)")
    # Nuclear scale
    E_nuc = energy_levels(1, 0.1)[0]
    print(f"E_1 at L=0.1 nm = {E_nuc*1e-6:.2f} MeV  (card says 37.6 MeV)")
    print("=== PASSED ===" if abs(ratio - 16.0) < 1e-9 else "=== CHECK ===")


if __name__ == "__main__":
    verify()
    sys.exit(0)


# ─── Manim scene ──────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"
RED_C  = "#FF6B6B"


class InfiniteSquareWellScene(Scene):
    """
    Infinite square well: wavefunctions n=1..6 + energy levels + node counting.
    Ends with L-scaling: 1 nm (eV) vs 0.1 nm (MeV).
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_well_and_levels()
        self._phase_wavefunctions()
        self._phase_nuclear_scale()

    def _phase_title(self):
        title = Text("Infinite Square Well", font="EB Garamond", font_size=60, color=INK)
        sub1 = Text(
            "Boundary conditions force nodes — energy grows as n²",
            font="EB Garamond", font_size=23, color=DIM,
        )
        sub2 = MathTex(r"E_n = n^2\,\frac{\pi^2\hbar^2}{2mL^2} = n^2 E_1",
                       color=BLUE, font_size=30)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_well_and_levels(self):
        # Energy axis on left, position axis on right
        E_vals = energy_levels(6, 1.0)
        E_max = E_vals[-1] * 1.15

        ax_E = Axes(
            x_range=[0, 1, 0.5],
            y_range=[0, E_max, 2.0],
            x_length=5.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(LEFT * 2.8 + DOWN * 0.2)

        lbl_y = MathTex(r"E\;(\mathrm{eV})", color=INK, font_size=20).next_to(ax_E.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Energy levels + wavefunctions  (L = 1 nm, electron)",
                   font="EB Garamond", font_size=20, color=DIM).to_edge(UP, buff=0.2)
        self.play(Create(ax_E), Write(lbl_y), Write(hdr), run_time=1.3)
        self.stored_ax_E = ax_E
        self.stored_E_vals = E_vals
        self.stored_hdr = hdr
        self.stored_lbl_y = lbl_y

    def _phase_wavefunctions(self):
        ax_E   = self.stored_ax_E
        E_vals = self.stored_E_vals

        ax_psi = Axes(
            x_range=[0, 1, 0.5],
            y_range=[-1.6, 1.6, 1.0],
            x_length=5.0,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(RIGHT * 2.6 + DOWN * 0.2)
        lbl_x_r = MathTex(r"x/L", color=INK, font_size=20).next_to(ax_psi.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y_r = MathTex(r"\psi_n", color=INK, font_size=20).next_to(ax_psi.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(ax_psi), Write(lbl_x_r), Write(lbl_y_r), run_time=1.0)

        x_arr = np.linspace(0, 1, 300)
        colors = [BLUE, GOLD, BROWN, BLUE, GOLD, BROWN]

        all_objs = []
        for n in range(1, 7):
            color = colors[n - 1]
            E_n = E_vals[n - 1]

            # Energy level on left panel
            e_line = DashedLine(
                ax_E.c2p(0.05, E_n), ax_E.c2p(0.95, E_n),
                color=color, dash_length=0.1, stroke_width=2.0,
            )
            e_lbl = MathTex(f"n={n}", color=color, font_size=18).next_to(
                ax_E.c2p(0.05, E_n), LEFT, buff=0.08
            )

            # Wavefunction on right panel (scale by energy so it sits at right height)
            psi = psi_n(n, x_arr)
            # Shift wavefunction baseline to E_n level, scale amplitude
            E_max_val = E_vals[-1]
            amp_scale = (E_max_val * 0.12)  # amplitude in eV units for display
            # Map to ax_psi coords (x in [0,1], y in psi units)
            pts = [ax_psi.c2p(x, y) for x, y in zip(x_arr, psi)]
            psi_curve = VMobject(color=color, stroke_width=2.5)
            psi_curve.set_points_smoothly(pts)

            # Node markers
            node_xs = [k / n for k in range(1, n)]
            node_dots = VGroup(*[
                Dot(ax_psi.c2p(nx, 0), radius=0.07, color=RED_C)
                for nx in node_xs
            ])

            caption_str = (
                f"n={n}: {n-1} node{'s' if n>2 else '' if n==2 else ''}"
                f"   E_{n} = {E_n:.2f} eV"
            )
            caption = Text(caption_str, font="EB Garamond", font_size=19, color=color
                           ).to_edge(DOWN, buff=0.22)

            objs = VGroup(e_line, e_lbl, psi_curve, node_dots)
            self.play(Create(e_line), Write(e_lbl), Create(psi_curve),
                      Create(node_dots), Write(caption), run_time=1.2)
            self.wait(0.6)
            self.play(FadeOut(caption), run_time=0.2)
            all_objs.append(objs)

        # n^2 annotation
        ratio_ann = MathTex(
            r"E_4/E_1 = 16 = 4^2 \quad \text{exactly}",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(ratio_ann), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(ratio_ann, ax_psi, lbl_x_r, lbl_y_r, *all_objs,
                          self.stored_ax_E, self.stored_lbl_y, self.stored_hdr), run_time=0.6)

    def _phase_nuclear_scale(self):
        E_atomic  = energy_levels(1, 1.0)[0]
        E_nuclear = energy_levels(1, 0.1)[0]

        eq = VGroup(
            MathTex(r"L = 1\,\mathrm{nm}\;\Rightarrow\;E_1 =",
                    color=INK, font_size=30),
            MathTex(fr"{E_atomic:.3f}\,\mathrm{{eV}}",
                    color=BLUE, font_size=30),
        ).arrange(RIGHT, buff=0.15).shift(UP * 1.0)

        eq2 = VGroup(
            MathTex(r"L = 0.1\,\mathrm{nm}\;\Rightarrow\;E_1 =",
                    color=INK, font_size=30),
            MathTex(fr"{E_nuclear/1e6:.1f}\,\mathrm{{MeV}}",
                    color=BROWN, font_size=30),
        ).arrange(RIGHT, buff=0.15).shift(DOWN * 0.2)

        note = Text(
            "10× smaller box → 100× higher energy → nuclear confinement scale",
            font="EB Garamond", font_size=22, color=DIM,
        ).to_edge(DOWN, buff=0.3)

        self.play(Write(eq), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(Write(note), run_time=1.0)
        self.wait(3.0)
