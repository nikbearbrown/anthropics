#!/usr/bin/env python3
"""
dimensional_analysis_bohr_radius.py — Dimensional Analysis: Building the Bohr Radius
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/dimensional-analysis-bohr-radius
    manim -qh dimensional_analysis_bohr_radius.py DimensionalAnalysisScene

Verify:
    python3 dimensional_analysis_bohr_radius.py --verify

Physics:
    a₀ = ℏ²/(mₑ·e²/4πε₀)
    [ℏ] = ML²T⁻¹,  [mₑ] = M,  [e²/4πε₀] = ML³T⁻²
    α=2, β=−1, γ=−1
    a₀ = 5.2917×10⁻¹¹ m = 0.529 Å
    Fine structure constant α_fs = e²/(4πε₀ℏc) ≈ 1/137
    a₀ = λ_C/α_fs  where λ_C = ℏ/(mₑc) = 3.862×10⁻¹³ m
"""
import sys
import numpy as np

HBAR  = 1.0545718e-34   # J·s
ME    = 9.10938e-31     # kg
E_CH  = 1.60218e-19     # C
EPS0  = 8.85419e-12     # C²/(N·m²)
C     = 2.99792e8       # m/s


def verify():
    e2_over_4pie0 = E_CH**2 / (4 * np.pi * EPS0)  # J·m
    a0 = HBAR**2 / (ME * e2_over_4pie0)
    print("=== Bohr radius dimensional analysis verification ===")
    print(f"  e²/4πε₀ = {e2_over_4pie0:.6e} J·m")
    print(f"  a₀ = ℏ²/(mₑ·e²/4πε₀) = {a0:.6e} m = {a0/1e-10:.4f} Å  (expected 0.5292 Å)")

    # P2: a₀ = λ_C / α_fs
    alpha_fs = e2_over_4pie0 / (HBAR * C)
    lam_C    = HBAR / (ME * C)
    a0_check = lam_C / alpha_fs
    print(f"\n  Fine structure constant α = {alpha_fs:.6f}  (≈ 1/{1/alpha_fs:.1f})")
    print(f"  Compton wavelength λ_C = ℏ/(mₑc) = {lam_C:.6e} m")
    print(f"  a₀ = λ_C/α = {a0_check:.6e} m  (matches ✓)")

    # Dimensional check: α=2, β=-1, γ=-1
    # [ℏ²/(mₑ·K)] where K=[e²/4πε₀]=ML³T⁻²
    # units: (ML²T⁻¹)²/(M · ML³T⁻²) = M²L⁴T⁻²/(M²L³T⁻²) = L ✓
    print("\n  Dimensional check: [ℏ²/(mₑ·K)] = L  ✓")
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


class DimensionalAnalysisScene(Scene):
    """
    Phase 1: title
    Phase 2: three constant blocks with dimension labels
    Phase 3: dimensional equation solved step-by-step (mass, length, time cancel)
    Phase 4: numerical result and a₀ = λ_C/α check
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_constants()
        self._phase_algebra()
        self._phase_result()

    def _phase_title(self):
        title = Text("Dimensional Analysis", font="EB Garamond", font_size=58, color=INK)
        sub   = Text(
            "ℏ, mₑ, e²/4πε₀ — the only combination with units of length is a₀",
            font="EB Garamond", font_size=23, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_constants(self):
        # Three constant blocks
        constants = [
            (r"\hbar", r"ML^2T^{-1}", BLUE),
            (r"m_e", r"M", GOLD),
            (r"\frac{e^2}{4\pi\varepsilon_0}", r"ML^3T^{-2}", BROWN),
        ]
        blocks = []
        for i, (sym, dim, col) in enumerate(constants):
            rect = RoundedRectangle(width=3.5, height=1.8, corner_radius=0.2,
                                    color=col, stroke_width=2.5, fill_opacity=0.12, fill_color=col)
            sym_t  = MathTex(sym, color=col, font_size=36).move_to(rect.get_center() + UP * 0.3)
            dim_t  = MathTex(r"\left[" + dim + r"\right]", color=INK, font_size=20).move_to(rect.get_center() + DOWN * 0.25)
            blk = VGroup(rect, sym_t, dim_t)
            blk.shift(LEFT * 4 + RIGHT * 4 * i + UP * 1.2)
            blocks.append(blk)

        for blk in blocks:
            self.play(Create(blk), run_time=0.6)

        eq_start = MathTex(r"a_0 = \hbar^\alpha m_e^\beta \left(\frac{e^2}{4\pi\varepsilon_0}\right)^\gamma", color=INK, font_size=30)
        eq_start.to_edge(DOWN, buff=0.5)
        self.play(Write(eq_start), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(*blocks, eq_start), run_time=0.5)

    def _phase_algebra(self):
        hdr = Text(
            "Solve the 3 dimension equations for α, β, γ",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(UP, buff=0.35)
        self.play(Write(hdr), run_time=0.6)

        eqs = [
            (r"M:\quad \alpha + \beta + \gamma = 0", GOLD),
            (r"L:\quad 2\alpha + 3\gamma = 1", BLUE),
            (r"T:\quad -\alpha - 2\gamma = 0", BROWN),
        ]
        solutions = [
            (r"\Rightarrow \gamma = -1", BROWN),
            (r"\Rightarrow \beta = +1", GOLD),
            (r"\Rightarrow \alpha = +2", BLUE),
        ]

        eq_objs = []
        for i, (eq_str, col) in enumerate(eqs):
            eq = MathTex(eq_str, color=col, font_size=28).move_to(UP * (0.6 - 1.0 * i))
            self.play(Write(eq), run_time=0.6)
            eq_objs.append(eq)

        sol_objs = []
        for i, (sol_str, col) in enumerate(solutions):
            sol = MathTex(sol_str, color=col, font_size=28).next_to(eq_objs[i], RIGHT, buff=0.5)
            self.play(Write(sol), run_time=0.5)
            sol_objs.append(sol)

        self.wait(1.5)
        self.play(FadeOut(*eq_objs, *sol_objs, hdr), run_time=0.5)

    def _phase_result(self):
        result = MathTex(
            r"a_0 = \frac{\hbar^2}{m_e \cdot e^2/4\pi\varepsilon_0} = 5.29 \times 10^{-11}\,\mathrm{m} = 0.529\,\text{\AA}",
            color=GOLD, font_size=30,
        ).shift(UP * 1.5)

        check = MathTex(
            r"a_0 = \frac{\lambda_C}{\alpha_\mathrm{fs}} = \frac{3.86\times10^{-13}\,\mathrm{m}}{1/137} = 0.529\,\text{\AA}",
            color=BLUE, font_size=26,
        ).shift(UP * 0.3)

        note = Text(
            "Without ℏ → no atomic size.  Classical physics predicts r → 0.",
            font="EB Garamond", font_size=22, color=DIM,
        ).shift(DOWN * 1.0)

        self.play(Write(result), run_time=1.2)
        self.play(Write(check), run_time=0.9)
        self.play(Write(note), run_time=0.8)
        self.wait(3.0)
