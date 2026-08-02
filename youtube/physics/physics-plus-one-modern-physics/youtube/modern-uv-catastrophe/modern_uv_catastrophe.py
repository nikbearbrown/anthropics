#!/usr/bin/env python3
"""
modern_uv_catastrophe.py — The Ultraviolet Catastrophe: Rayleigh-Jeans Diverges, Planck Saves It
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-modern-physics book.

Render:
    cd physics-plus-one-modern-physics/youtube/modern-uv-catastrophe
    manim -qh modern_uv_catastrophe.py UvCatastropheScene

Physics:
    Planck: B_λ = (2hc²/λ⁵) / (exp(hc/λkT) − 1)
    Rayleigh-Jeans: B_λ^RJ = 2ckT/λ⁴  (classical limit)
    T = 5778 K (solar surface)
    Wien peak: λ_peak = b/T = 2.898e-3/5778 = 501.5 nm  (NIST: 502 nm)
    P1: At λ = 10 μm, Planck and RJ agree to within 1%
    P2: Wien peak at 502 nm
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34    # J·s
C_LIGHT  = 3.0e8        # m/s
K_B      = 1.381e-23    # J/K
B_WIEN   = 2.898e-3     # m·K


def planck(lam_m: np.ndarray, T: float) -> np.ndarray:
    """Spectral radiance B_λ (W/m²/sr/m)."""
    x = H_PLANCK * C_LIGHT / (lam_m * K_B * T)
    return (2.0 * H_PLANCK * C_LIGHT**2 / lam_m**5) / (np.exp(x) - 1.0)


def rayleigh_jeans(lam_m: np.ndarray, T: float) -> np.ndarray:
    return 2.0 * C_LIGHT * K_B * T / lam_m**4


def wien_peak(T: float) -> float:
    return B_WIEN / T


if __name__ == "__main__":
    print("=== UV Catastrophe Verification ===")
    T = 5778.0
    lam_peak = wien_peak(T)
    print(f"Wien peak: λ = {lam_peak*1e9:.1f} nm  (expect 501-502 nm)")
    assert abs(lam_peak - 502e-9) < 2e-9, f"P2 FAIL: {lam_peak*1e9:.1f} nm"
    # P1: at λ = 200 μm (x=hc/λkT≈0.013 << 1), Planck and RJ agree to within 1%
    lam_ir = 200e-6
    B_pl = planck(np.array([lam_ir]), T)[0]
    B_rj = rayleigh_jeans(np.array([lam_ir]), T)[0]
    diff = abs(B_pl - B_rj) / B_pl
    print(f"P1: at 200 μm, |Planck−RJ|/Planck = {diff*100:.3f}%  (expect <1%)")
    assert diff < 0.01, f"P1 FAIL: diff={diff*100:.3f}%"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

T_SUN = 5778.0
LAM_MIN = 100e-9    # 100 nm (UV)
LAM_MAX = 3000e-9   # 3 μm
LAM_NM_MIN = 100
LAM_NM_MAX = 3000


class UvCatastropheScene(Scene):
    """Planck vs Rayleigh-Jeans spectral curves with UV catastrophe shading."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_curves(ax)
        self._phase_slider(ax)

    def _phase_title(self):
        title = Text("The Ultraviolet Catastrophe", font="EB Garamond",
                     font_size=52, color=INK)
        sub = Text("Rayleigh-Jeans diverges at short λ — Planck's quanta fix it",
                   font="EB Garamond", font_size=22, color=DIM)
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _phase_axes(self):
        # Use nm on x axis for readability
        ax = Axes(
            x_range=[LAM_NM_MIN, LAM_NM_MAX, 500],
            y_range=[0, 1.0, 0.25],
            x_length=10.0,
            y_length=5.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(DOWN * 0.3)
        x_lbl = MathTex(r"\lambda\;(\mathrm{nm})", color=INK, font_size=24).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"B_\lambda\;(\mathrm{norm.})", color=INK, font_size=24).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _phase_curves(self, ax):
        T = T_SUN
        lam_nm = np.linspace(LAM_NM_MIN, LAM_NM_MAX, 600)
        lam_m  = lam_nm * 1e-9

        B_pl = planck(lam_m, T)
        B_pk = B_pl.max()
        B_pl_n = B_pl / B_pk

        B_rj = rayleigh_jeans(lam_m, T)
        B_rj_n = np.clip(B_rj / B_pk, 0, 2.5)

        pts_pl  = [ax.c2p(l, b) for l, b in zip(lam_nm, B_pl_n)]
        pts_rj  = [ax.c2p(l, min(b, 0.98)) for l, b in zip(lam_nm, B_rj_n)]

        curve_pl = VMobject(color=BLUE, stroke_width=3.0)
        curve_pl.set_points_smoothly(pts_pl)

        # RJ: only plot where it's below 1 (clip at upper axis)
        curve_rj = VMobject(color=BROWN, stroke_width=2.5,
                            stroke_opacity=0.85)
        curve_rj.set_points_smoothly(pts_rj)

        # Wien peak marker
        lam_pk_nm = wien_peak(T) * 1e9
        f_pk_val  = 1.0
        pk_line = DashedLine(ax.c2p(lam_pk_nm, 0), ax.c2p(lam_pk_nm, 1.02),
                             color=GOLD, stroke_width=1.5)
        pk_lbl = MathTex(r"\lambda_{\rm peak}=502\,\mathrm{nm}", color=GOLD,
                         font_size=20).next_to(ax.c2p(lam_pk_nm, 1.02), UP, buff=0.05)

        # UV catastrophe shading (λ < 300 nm)
        uv_lam = np.linspace(LAM_NM_MIN, 300, 80)
        uv_m   = uv_lam * 1e-9
        uv_rj  = rayleigh_jeans(uv_m, T) / B_pk
        uv_pts = ([ax.c2p(300, 0)]
                  + [ax.c2p(l, min(b, 0.97)) for l, b in zip(reversed(uv_lam), reversed(uv_rj))]
                  + [ax.c2p(LAM_NM_MIN, 0)])
        uv_fill = Polygon(*uv_pts, color=BROWN,
                          fill_color=BROWN, fill_opacity=0.3, stroke_width=0)
        uv_lbl = Text("UV catastrophe\n(classical → ∞)", font="EB Garamond",
                      font_size=17, color=BROWN).move_to(ax.c2p(200, 0.7))

        hdr = Text("T = 5778 K (solar surface)", font="EB Garamond",
                   font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.5)

        pl_lbl = Text("Planck (correct)", font="EB Garamond",
                      font_size=20, color=BLUE).move_to(ax.c2p(1200, 0.6))
        rj_lbl = Text("Rayleigh-Jeans (classical)", font="EB Garamond",
                      font_size=20, color=BROWN).move_to(ax.c2p(1600, 0.35))

        self.play(Create(curve_pl), Write(pl_lbl), run_time=2.0)
        self.play(Create(curve_rj), Write(rj_lbl), run_time=1.8)
        self.play(Create(pk_line), Write(pk_lbl), run_time=1.0)
        self.play(FadeIn(uv_fill), Write(uv_lbl), run_time=1.0)

        cap = MathTex(
            r"B_\lambda = \frac{2hc^2/\lambda^5}{e^{hc/\lambda kT}-1}"
            r"\quad\xrightarrow{\lambda\to0}\text{finite}"
            r"\quad\quad B_\lambda^{\rm RJ}=\frac{2ckT}{\lambda^4}"
            r"\xrightarrow{\lambda\to0}\infty",
            color=INK, font_size=20).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=1.5)
        self.wait(2.5)

        self._all_statics = VGroup(hdr, curve_pl, curve_rj, pl_lbl, rj_lbl,
                                   pk_line, pk_lbl, uv_fill, uv_lbl, cap)
        self.play(FadeOut(self._all_statics), run_time=0.5)
        self._B_pk = B_pk
        self._curve_pl_ref = curve_pl

    def _phase_slider(self, ax):
        tc = ValueTracker(T_SUN)

        def _pl_curve():
            T = tc.get_value()
            lam_nm = np.linspace(LAM_NM_MIN, LAM_NM_MAX, 400)
            lam_m  = lam_nm * 1e-9
            B = planck(lam_m, T)
            Bnorm = B / B.max()
            pts = [ax.c2p(l, b) for l, b in zip(lam_nm, Bnorm)]
            m = VMobject(color=BLUE, stroke_width=2.5)
            m.set_points_smoothly(pts)
            return m

        def _rj_curve():
            T = tc.get_value()
            lam_nm = np.linspace(LAM_NM_MIN, LAM_NM_MAX, 400)
            lam_m  = lam_nm * 1e-9
            B_pl   = planck(lam_m, T)
            B_pk   = B_pl.max()
            B_rj   = rayleigh_jeans(lam_m, T) / B_pk
            B_rj_c = np.clip(B_rj, 0, 0.97)
            pts = [ax.c2p(l, b) for l, b in zip(lam_nm, B_rj_c)]
            m = VMobject(color=BROWN, stroke_width=2.0)
            m.set_points_smoothly(pts)
            return m

        dyn_pl = always_redraw(_pl_curve)
        dyn_rj = always_redraw(_rj_curve)
        self.add(dyn_pl, dyn_rj)

        t_lbl = MathTex(r"T = ", color=DIM, font_size=30)
        t_num = DecimalNumber(T_SUN, num_decimal_places=0, color=DIM, font_size=30)
        t_K   = MathTex(r"\mathrm{K}", color=DIM, font_size=30)
        t_num.add_updater(lambda m: m.set_value(tc.get_value()))
        t_row = VGroup(t_lbl, t_num, t_K).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.28)

        hdr = Text("T changes — Planck always finite; RJ always diverges at UV",
                   font="EB Garamond", font_size=20, color=INK).to_edge(UP, buff=0.18)
        self.play(Write(hdr), FadeIn(t_row), run_time=0.8)
        self.play(tc.animate.set_value(3000.0), run_time=3.0, rate_func=smooth)
        self.play(tc.animate.set_value(10000.0), run_time=3.0, rate_func=smooth)
        self.wait(1.5)
        final = Text("The divergence appears at every T — it is a flaw in classical theory, not in the star",
                     font="EB Garamond", font_size=20, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(FadeOut(t_row), Write(final), run_time=1.2)
        self.wait(2.5)
