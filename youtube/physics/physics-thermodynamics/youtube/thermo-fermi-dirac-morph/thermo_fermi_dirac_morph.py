#!/usr/bin/env python3
"""
thermo_fermi_dirac_morph.py — Fermi-Dirac Step Function: T=0 Cliff Softening
SILENT SLATE — math-explainer (brownblue) candidate, physics-thermodynamics book.

Physics (verified at module level):
    f_FD(E) = 1/(exp((E-μ)/k_BT) + 1)
    Copper: E_F = 7.0 eV, k_BT = 0.025 eV at 300 K
    f(E_F) = 1/2 exactly at any T > 0
    Blur width ≈ 2k_BT at 300 K = 0.05 eV = 0.71% of E_F

Render:
    cd physics-thermodynamics/youtube/thermo-fermi-dirac-morph
    manim -qh thermo_fermi_dirac_morph.py FermiDiracMorphScene
"""
import sys
import numpy as np

# ─── Constants ────────────────────────────────────────────────────────────────
K_B_EV  = 8.617333e-5   # eV/K
E_F_CU  = 7.0           # eV  — Fermi energy of copper
E_MAX   = 14.0          # eV  — plot range


def fermi_dirac(E: np.ndarray, mu: float, T: float) -> np.ndarray:
    """Fermi-Dirac distribution. Returns f(E) in [0,1]."""
    if T < 1.0:
        T = 1.0   # avoid div-by-zero; at T=1 K looks like step
    x = (E - mu) / (K_B_EV * T)
    # Clamp to avoid overflow
    x = np.clip(x, -500, 500)
    return 1.0 / (np.exp(x) + 1.0)


def boltzmann_approx(E: np.ndarray, mu: float, T: float) -> np.ndarray:
    """Classical Boltzmann occupation (wrong for metals)."""
    x = (E - mu) / (K_B_EV * T)
    x = np.clip(x, -500, 500)
    return np.exp(-x)


# ─── Verification ─────────────────────────────────────────────────────────────
def _verify():
    print("=== Fermi-Dirac verification ===")
    T = 300.0
    kT = K_B_EV * T
    print(f"Copper E_F = {E_F_CU:.1f} eV, k_BT at {T:.0f} K = {kT:.4f} eV")
    print(f"Blur = 2k_BT = {2*kT:.4f} eV = {2*kT/E_F_CU*100:.2f}% of E_F")
    f_at_EF = fermi_dirac(np.array([E_F_CU]), E_F_CU, T)[0]
    print(f"f(E_F) at {T:.0f} K = {f_at_EF:.6f}  (expected exactly 0.5)")
    # Fraction of electrons within k_BT of E_F
    frac = kT / E_F_CU
    print(f"Fraction within k_BT of E_F ≈ {frac:.4f} = {frac*100:.2f}%")
    print(f"  → electronic C_V ≈ {frac:.4f} × classical C_V")
    # Boltzmann comparison at E = E_F + 0.5 eV
    E_test = E_F_CU + 0.5
    fFD = fermi_dirac(np.array([E_test]), E_F_CU, T)[0]
    fBol = boltzmann_approx(np.array([E_test]), E_F_CU, T)[0]
    print(f"At E = E_F + 0.5 eV: f_FD = {fFD:.4f}, f_Boltzmann = {fBol:.2f}  (Boltzmann > 1 is unphysical!)")
    print("=== PASSED ===")

_verify()
if __name__ == "__main__":
    sys.exit(0)


# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"


class FermiDiracMorphScene(Scene):
    """
    Phase 1: Title.
    Phase 2: Draw T=0 step function (perfect cliff at E_F).
    Phase 3: T sweep 1 K → 10000 K — cliff softens to sigmoid.
    Phase 4: Blur brace tracking 2k_BT width.
    Phase 5: Boltzmann comparison.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._build_axes()
        self._phase_step(ax)
        self._phase_sweep(ax)
        self._phase_boltzmann(ax)

    def _phase_title(self):
        title = Text("Fermi-Dirac Distribution", font="EB Garamond", font_size=60, color=INK)
        sub1 = MathTex(
            r"f(E) = \frac{1}{e^{(E-\mu)/k_BT}+1}",
            color=BLUE, font_size=34,
        )
        sub2 = Text(
            "T=0: perfect cliff at E_F  ·  T>0: the cliff blurs to a sigmoid",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(Write(sub1), run_time=0.9)
        self.play(FadeIn(sub2), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    def _build_axes(self):
        ax = Axes(
            x_range=[0, E_MAX, 2.0],
            y_range=[0, 1.2, 0.25],
            x_length=10.0,
            y_length=5.2,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(DOWN * 0.5)
        lbl_x = MathTex(r"E\;(\mathrm{eV})", color=INK, font_size=24).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"f(E)", color=INK, font_size=24).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        # E_F vertical dashed
        ef_line = DashedLine(ax.c2p(E_F_CU, 0), ax.c2p(E_F_CU, 1.15),
                             color=DIM, stroke_width=1.5)
        ef_lbl = MathTex(r"E_F = 7.0\,\mathrm{eV}", color=DIM, font_size=20).next_to(
            ax.c2p(E_F_CU, 1.1), UP, buff=0.06)
        hdr = Text("Copper — Fermi-Dirac occupation function",
                   font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)
        self.play(Create(ef_line), Write(ef_lbl), run_time=0.6)
        self._ef_line = ef_line
        self._ef_lbl  = ef_lbl
        self._hdr     = hdr
        return ax

    def _phase_step(self, ax):
        """T=0 step function."""
        # Filled area below E_F = f=1, above = f=0
        E_left  = 0.0
        E_right = E_MAX
        pts_top = [ax.c2p(E_left, 1), ax.c2p(E_F_CU, 1), ax.c2p(E_F_CU, 0)]
        fill_step = Polygon(
            ax.c2p(E_left, 0), ax.c2p(E_left, 1),
            ax.c2p(E_F_CU, 1), ax.c2p(E_F_CU, 0),
            color=BLUE, fill_color=BLUE, fill_opacity=0.25, stroke_width=0,
        )
        step_line = VMobject(color=BLUE, stroke_width=3.5)
        step_line.set_points_as_corners([
            ax.c2p(0, 0),
            ax.c2p(0, 1),
            ax.c2p(E_F_CU, 1),
            ax.c2p(E_F_CU, 0),
            ax.c2p(E_MAX, 0),
        ])
        lbl_T0 = Text("T → 0:  perfect step — all states below E_F filled",
                      font="EB Garamond", font_size=22, color=BLUE).to_edge(DOWN, buff=0.25)
        self.play(Create(step_line), FadeIn(fill_step), Write(lbl_T0), run_time=2.0)
        self.wait(1.0)
        self._step_line = step_line
        self._fill_step = fill_step
        self.play(FadeOut(lbl_T0), run_time=0.3)

    def _phase_sweep(self, ax):
        """T sweep from 1 K to 10000 K."""
        T_tracker = ValueTracker(1.0)
        Es = np.linspace(0.01, E_MAX, 500)

        def make_fd_curve():
            T = T_tracker.get_value()
            fs = fermi_dirac(Es, E_F_CU, T)
            pts = [ax.c2p(e, f) for e, f in zip(Es, fs)]
            c = VMobject(color=BLUE, stroke_width=3.5)
            c.set_points_smoothly(pts)
            return c

        def make_fd_fill():
            T = T_tracker.get_value()
            fs = fermi_dirac(Es, E_F_CU, T)
            bnd = list(zip(Es, fs)) + [(Es[-1], 0.0), (Es[0], 0.0)]
            coords = [ax.c2p(e, f) for e, f in bnd]
            return Polygon(*coords, color=BLUE, fill_color=BLUE, fill_opacity=0.18, stroke_width=0)

        def make_blur_brace():
            T = T_tracker.get_value()
            kT = K_B_EV * T
            # blur region: E_F ± k_BT
            E_lo = max(E_F_CU - kT, 0.1)
            E_hi = min(E_F_CU + kT, E_MAX - 0.1)
            line = DoubleArrow(
                ax.c2p(E_lo, 0.5), ax.c2p(E_hi, 0.5),
                color=GOLD, stroke_width=2.0, tip_length=0.15,
            )
            return line

        self.remove(self._step_line, self._fill_step)
        dyn_curve  = always_redraw(make_fd_curve)
        dyn_fill   = always_redraw(make_fd_fill)
        dyn_blur   = always_redraw(make_blur_brace)
        self.add(dyn_fill, dyn_curve, dyn_blur)

        # Temperature readout
        T_lbl = MathTex(r"T = ", color=INK, font_size=30)
        T_num = DecimalNumber(1.0, num_decimal_places=0, color=GOLD, font_size=30)
        T_K   = MathTex(r"\mathrm{K}", color=INK, font_size=30)
        kT_lbl= MathTex(r"k_BT = ", color=DIM, font_size=24)
        kT_num= DecimalNumber(K_B_EV * 1.0, num_decimal_places=4, color=DIM, font_size=24)
        kT_eV = MathTex(r"\mathrm{eV}", color=DIM, font_size=24)
        half_lbl = MathTex(r"f(E_F) = \tfrac{1}{2}\;\forall T>0", color=GOLD, font_size=24)

        T_num.add_updater(lambda m: m.set_value(T_tracker.get_value()))
        kT_num.add_updater(lambda m: m.set_value(K_B_EV * T_tracker.get_value()))

        T_row  = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.08)
        kT_row = VGroup(kT_lbl, kT_num, kT_eV).arrange(RIGHT, buff=0.08)
        VGroup(T_row, kT_row, half_lbl).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.28)

        hdr2 = Text("Raise temperature — cliff softens to sigmoid",
                    font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.25)
        self.play(FadeOut(self._hdr), Write(hdr2), FadeIn(T_row), FadeIn(kT_row), FadeIn(half_lbl), run_time=0.8)

        # Sweep to 300 K (copper at room temp)
        self.play(T_tracker.animate.set_value(300.0), run_time=3.0, rate_func=smooth)
        self.wait(1.0)

        # Annotate 300 K blur
        kT_300 = K_B_EV * 300.0
        ann_300 = Text(
            f"300 K: blur = 2k_BT = {2*kT_300:.3f} eV = {2*kT_300/E_F_CU*100:.1f}% of E_F",
            font="EB Garamond", font_size=20, color=DIM,
        ).to_edge(UP, buff=0.55)
        self.play(Write(ann_300), run_time=0.8)
        self.wait(1.2)

        # Continue to 10000 K
        self.play(FadeOut(ann_300), run_time=0.2)
        self.play(T_tracker.animate.set_value(10000.0), run_time=5.0, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(hdr2, T_row, kT_row, half_lbl, dyn_blur), run_time=0.4)
        self._dyn_curve = dyn_curve
        self._dyn_fill  = dyn_fill
        self._T_tracker = T_tracker

    def _phase_boltzmann(self, ax):
        """Overlay Boltzmann distribution to show it breaks f ≤ 1."""
        T = 5000.0
        self._T_tracker.set_value(T)
        Es = np.linspace(0.01, E_MAX, 400)
        fFD  = fermi_dirac(Es, E_F_CU, T)
        fBol = boltzmann_approx(Es, E_F_CU, T)
        # Clip Boltzmann for display (it diverges)
        fBol_clip = np.clip(fBol, 0, 1.2)

        pts_bol = [ax.c2p(e, f) for e, f in zip(Es, fBol_clip)]
        curve_bol = VMobject(color=BROWN, stroke_width=3.0, stroke_opacity=0.8)
        curve_bol.set_points_smoothly(pts_bol)

        hdr3 = Text("Boltzmann vs Fermi-Dirac at 5000 K",
                    font="EB Garamond", font_size=24, color=INK).to_edge(UP, buff=0.25)

        lbl_fd  = Text("Fermi-Dirac  f ≤ 1  (Pauli exclusion enforced)",
                       font="EB Garamond", font_size=21, color=BLUE).to_edge(DOWN, buff=0.5)
        lbl_bol = Text("Boltzmann  f → ∞ near E_F  (unphysical without exclusion)",
                       font="EB Garamond", font_size=21, color=BROWN).to_edge(DOWN, buff=0.25)

        self.play(FadeOut(self._hdr), Write(hdr3), run_time=0.5)
        self.play(Create(curve_bol), run_time=1.5)
        self.play(Write(lbl_fd), Write(lbl_bol), run_time=1.0)
        self.wait(1.5)

        final = Text(
            "Pauli exclusion locks 99.3% of copper electrons in frozen states\n"
            "— that is why metals have 100× lower electronic C_V than classical physics predicts",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeOut(lbl_fd, lbl_bol), Write(final), run_time=1.2)
        self.wait(3.0)
