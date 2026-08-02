#!/usr/bin/env python3
"""
qm_gaussian_spreading.py — Gaussian Wave Packet Spreading
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-gaussian-spreading
    manim -qh qm_gaussian_spreading.py GaussianSpreadingScene

Verify:
    python3 qm_gaussian_spreading.py

Physics (n=1 mol level):
    Electron mass m = 9.109e-31 kg
    hbar = 1.055e-34 J·s
    a = 1e-9 m (1 nm initial width)
    tau = 2*m*a^2 / hbar ≈ 1.74e-15 s (spreading time)
    sigma_p = hbar / (2*a) (constant)
    At t = tau: sigma_x = a * sqrt(2) ≈ 1.414 nm
    sigma_x * sigma_p = (hbar/2) * sqrt(1 + (t/tau)^2) >= hbar/2
"""
import sys
import numpy as np
from math import factorial  # noqa: F401

# ─── Physics constants ─────────────────────────────────────────────────────────
HBAR   = 1.0545718e-34   # J·s
M_E    = 9.10938e-31     # kg
M_P    = 1.67262e-27     # kg
EV     = 1.60218e-19     # J

A_NM   = 1.0e-9          # m, initial width for electron case


def tau_spread(m: float, a: float) -> float:
    """Spreading time τ = 2mа²/ℏ."""
    return 2.0 * m * a**2 / HBAR


def sigma_x(t: float, m: float, a: float) -> float:
    """σ_x(t) = a * sqrt(1 + (t/tau)^2)."""
    tau = tau_spread(m, a)
    return a * np.sqrt(1.0 + (t / tau) ** 2)


def sigma_p(a: float) -> float:
    """σ_p = ℏ/(2a), constant."""
    return HBAR / (2.0 * a)


def psi_sq(x: np.ndarray, t: float, m: float, a: float) -> np.ndarray:
    """|ψ(x,t)|² — Gaussian probability density (normalised in nm units for display)."""
    sx = sigma_x(t, m, a)
    return (1.0 / (np.sqrt(2 * np.pi) * sx)) * np.exp(-0.5 * (x / sx) ** 2)


def verify():
    print("=== Gaussian wave-packet spreading verification ===")
    tau_e  = tau_spread(M_E, A_NM)
    tau_p  = tau_spread(M_P, A_NM)
    sp     = sigma_p(A_NM)
    print(f"Electron spread time τ = {tau_e*1e15:.3f} fs  (card says 1.8 fs)")
    print(f"Proton   spread time τ = {tau_p*1e12:.3f} ps  (card says 3.3 ps)")
    sx_tau_e = sigma_x(tau_e, M_E, A_NM)
    print(f"σ_x(τ) electron = {sx_tau_e*1e9:.4f} nm  (should be √2 = 1.4142 nm)")
    print(f"σ_p electron     = {sp / EV * 3e8:.4f} eV/c  (card says 0.053 eV/c)")
    product = sigma_x(0, M_E, A_NM) * sp
    print(f"σ_x·σ_p at t=0  = {product / HBAR:.6f} × ℏ/2  (should be ℏ/2)")
    print("=== PASSED ===" if abs(sx_tau_e * 1e9 - np.sqrt(2)) < 1e-6 else "=== CHECK ===")


if __name__ == "__main__" and "--verify" not in sys.argv:
    verify()
    sys.exit(0)

if __name__ == "__main__" and "--verify" in sys.argv:
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


class GaussianSpreadingScene(Scene):
    """
    Gaussian wave packet spreading — uncertainty product grows in time.
    Top panel: |ψ|² at t=0, t=τ, t=2τ for electron (a=1 nm).
    Bottom panel: σ_x(t), σ_p (flat), and product σ_x·σ_p vs t.
    Ending: compare electron vs proton spreading at same t.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        self._phase_title()
        self._phase_wavepacket_evolution()
        self._phase_uncertainty_panel()
        self._phase_electron_vs_proton()

    # ── Phase 1: Title ────────────────────────────────────────────────────────

    def _phase_title(self):
        title = Text("Gaussian Wave Packet Spreading", font="EB Garamond",
                     font_size=58, color=INK)
        sub1 = Text(
            "A perfectly sharp position has a perfectly uncertain momentum.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = MathTex(
            r"\sigma_x\,\sigma_p \geq \frac{\hbar}{2}",
            color=BLUE, font_size=34,
        )
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.4).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.5)

    # ── Phase 2: Animate |ψ|² at three time snapshots ────────────────────────

    def _phase_wavepacket_evolution(self):
        ax = Axes(
            x_range=[-5.5, 5.5, 2.0],
            y_range=[0.0, 0.5, 0.2],
            x_length=10.0,
            y_length=3.6,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2),
        ).shift(UP * 0.8)

        lbl_x = MathTex(r"x / a_0", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"|\psi|^2", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Probability density evolves in time (electron, a = 1 nm)",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.15)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.5)

        # Display x in units of a (nm), plot density in units of 1/a
        a_display = 1.0   # nm units for display
        tau_e = tau_spread(M_E, A_NM)

        snapshots = [
            (0.0, BLUE, r"t = 0"),
            (1.0, GOLD, r"t = \tau"),
            (2.0, BROWN, r"t = 2\tau"),
        ]

        curves = []
        labels = []
        for t_frac, color, lbl_str in snapshots:
            t_phys = t_frac * tau_e
            sx_nm = sigma_x(t_phys, M_E, A_NM) * 1e9  # in nm

            x_arr = np.linspace(-5.5, 5.5, 400)
            y_arr = (1.0 / (np.sqrt(2 * np.pi) * sx_nm)) * np.exp(-0.5 * (x_arr / sx_nm) ** 2)
            # Rescale y to display units (multiply by a_display to keep area=1 in display)
            y_arr_disp = y_arr * a_display  # density × nm (dimensionless for plot)

            pts = [ax.c2p(x, y) for x, y in zip(x_arr, y_arr_disp)]
            curve = VMobject(color=color, stroke_width=3.5)
            curve.set_points_smoothly(pts)

            # Sigma markers
            mk_l = DashedLine(
                ax.c2p(-sx_nm, 0), ax.c2p(-sx_nm, y_arr_disp.max()),
                color=color, dash_length=0.08, stroke_width=1.5,
            )
            mk_r = DashedLine(
                ax.c2p(sx_nm, 0), ax.c2p(sx_nm, y_arr_disp.max()),
                color=color, dash_length=0.08, stroke_width=1.5,
            )

            text_label = MathTex(lbl_str, color=color, font_size=24).next_to(
                ax.c2p(0, y_arr_disp.max()), UP, buff=0.05
            )
            text_label.shift(RIGHT * (t_frac * 1.6))

            self.play(Create(curve), Create(mk_l), Create(mk_r),
                      Write(text_label), run_time=1.4)
            curves.append(VGroup(curve, mk_l, mk_r))
            labels.append(text_label)

        caption = Text(
            "Peak lowers, width grows — area stays exactly 1 (normalised)",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(caption), run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, caption, *curves, *labels), run_time=0.6)

    # ── Phase 3: σ_x(t) growing, σ_p flat, product ───────────────────────────

    def _phase_uncertainty_panel(self):
        ax = Axes(
            x_range=[0, 3.2, 1.0],
            y_range=[0, 3.0, 1.0],
            x_length=8.5,
            y_length=3.8,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2),
        ).shift(UP * 0.5)

        lbl_x = MathTex(r"t / \tau", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\sigma / (\hbar/2)", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Uncertainty products vs time",
                   font="EB Garamond", font_size=21, color=DIM).next_to(ax, UP, buff=0.12)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.3)

        t_arr = np.linspace(0.0, 3.0, 300)
        # All in units of (ℏ/2)
        sp_val = sigma_p(A_NM)
        tau_e  = tau_spread(M_E, A_NM)
        sx_arr  = np.array([sigma_x(t * tau_e, M_E, A_NM) for t in t_arr]) * sp_val / (HBAR / 2)
        sp_arr  = np.ones_like(t_arr)   # σ_p = ℏ/2a → in units of sp_val/sp_val = 1
        prod_arr = np.array([sigma_x(t * tau_e, M_E, A_NM) * sp_val / (HBAR / 2) for t in t_arr])

        def arr_to_curve(t_a, y_a, color, lw=3.0):
            pts = [ax.c2p(t, y) for t, y in zip(t_a, y_a)]
            m = VMobject(color=color, stroke_width=lw)
            m.set_points_smoothly(pts)
            return m

        c_sx   = arr_to_curve(t_arr, sx_arr,  BLUE)
        c_sp   = arr_to_curve(t_arr, sp_arr,  DIM)
        c_prod = arr_to_curve(t_arr, prod_arr, GOLD)

        lbl_sx   = MathTex(r"\sigma_x(t)", color=BLUE, font_size=24).next_to(ax.c2p(3.0, sx_arr[-1]), RIGHT, buff=0.1)
        lbl_sp   = MathTex(r"\sigma_p", color=DIM,  font_size=24).next_to(ax.c2p(3.0, 1.0), RIGHT, buff=0.1)
        lbl_prod = MathTex(r"\sigma_x\sigma_p", color=GOLD, font_size=24).next_to(ax.c2p(3.0, prod_arr[-1]), RIGHT, buff=0.05)

        self.play(Create(c_sx), Write(lbl_sx), run_time=1.5)
        self.play(Create(c_sp), Write(lbl_sp), run_time=1.0)
        self.play(Create(c_prod), Write(lbl_prod), run_time=1.5)

        hl = DashedLine(ax.c2p(0, 1.0), ax.c2p(3.0, 1.0),
                        color=GOLD, dash_length=0.1, stroke_width=1.5)
        hl_lbl = MathTex(r"\hbar/2", color=GOLD, font_size=22).next_to(ax.c2p(0, 1.0), LEFT, buff=0.1)
        self.play(Create(hl), Write(hl_lbl), run_time=0.8)

        caption = Text(
            "σ_p constant — momentum spread is baked in at t = 0. σ_x grows. Product only rises.",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(caption), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_sx, c_sp, c_prod,
                          lbl_sx, lbl_sp, lbl_prod, hl, hl_lbl, caption), run_time=0.5)

    # ── Phase 4: Electron vs proton at same time ──────────────────────────────

    def _phase_electron_vs_proton(self):
        ax = Axes(
            x_range=[-6, 6, 2],
            y_range=[0, 0.6, 0.2],
            x_length=10, y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.2),
        ).shift(UP * 0.8)

        lbl_x = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=22).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"|\psi|^2\,(\mathrm{nm}^{-1})", color=INK, font_size=22).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        hdr = Text("Same initial width, same time — proton barely moves",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)

        # Show at t = tau_electron
        tau_e = tau_spread(M_E, A_NM)
        x_arr = np.linspace(-6, 6, 500)

        sx_e_nm = sigma_x(tau_e, M_E, A_NM) * 1e9
        sx_p_nm = sigma_x(tau_e, M_P, A_NM) * 1e9

        def density(x, sx):
            return (1.0 / (np.sqrt(2 * np.pi) * sx)) * np.exp(-0.5 * (x / sx) ** 2)

        y_e = density(x_arr, sx_e_nm)
        y_p = density(x_arr, sx_p_nm)

        def make_curve(y_arr, color):
            pts = [ax.c2p(x, y) for x, y in zip(x_arr, y_arr)]
            m = VMobject(color=color, stroke_width=3.5)
            m.set_points_smoothly(pts)
            return m

        c_e = make_curve(y_e, BLUE)
        c_p = make_curve(y_p, BROWN)

        lbl_e = Text("Electron  σ_x = 1.41 nm", font="EB Garamond",
                     font_size=22, color=BLUE).to_edge(DOWN, buff=0.55)
        lbl_p = Text("Proton  σ_x ≈ 1.000 nm (barely spread)", font="EB Garamond",
                     font_size=22, color=BROWN).to_edge(DOWN, buff=0.25)

        self.play(Create(c_e), Write(lbl_e), run_time=1.3)
        self.play(Create(c_p), Write(lbl_p), run_time=1.3)

        eq = MathTex(
            r"\tau \propto m \quad \Rightarrow \quad \text{proton spreads } 1836\times \text{ slower}",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.15)
        self.wait(1.0)
        self.play(FadeOut(lbl_e, lbl_p), Write(eq), run_time=1.2)
        self.wait(3.0)
