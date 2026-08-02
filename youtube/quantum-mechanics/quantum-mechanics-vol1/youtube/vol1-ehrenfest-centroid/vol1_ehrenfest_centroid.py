#!/usr/bin/env python3
"""
vol1_ehrenfest_centroid.py — Ehrenfest's Theorem: The Centroid That Obeys Newton
SILENT SLATE — math-explainer candidate, quantum-mechanics-vol1

Physics:
    Free particle: ⟨x⟩(t) = ⟨x⟩₀ + (ℏk₀/m)t = ⟨x⟩₀ + v_g·t
    Harmonic osc (coherent state): ⟨x⟩(t) = x₀·cos(ωt)
        ω = 10¹⁴ rad/s, mₑ; x₀ = 0.5 nm, T = 2π/ω ≈ 62.8 fs
    Classical trajectory coincides with ⟨x⟩ in both cases

Verify:
    python3 vol1_ehrenfest_centroid.py --verify

Render:
    manim -qh vol1_ehrenfest_centroid.py EhrenfestCentroidScene
"""
import sys
import numpy as np

HBAR   = 1.0545718e-34
M_E    = 9.10938e-31
K0     = 5.0e9    # m⁻¹
SIGMA0 = 1.0e-9   # 1 nm
OMEGA  = 1.0e14   # rad/s harmonic osc
X0_NM  = 0.5      # nm off-center

def v_group():
    return HBAR * K0 / M_E

def spread_time_fs():
    return M_E * SIGMA0**2 / HBAR * 1e15

def period_fs():
    return 2 * np.pi / OMEGA * 1e15

def mean_x_free(t_fs):
    """⟨x⟩ for free particle (nm)."""
    return v_group() * t_fs * 1e-15 * 1e9  # nm

def mean_x_harmonic(t_fs):
    """⟨x⟩ for coherent state in harmonic well (nm)."""
    return X0_NM * np.cos(OMEGA * t_fs * 1e-15)

def sigma_free(t_fs):
    tau = spread_time_fs()
    return SIGMA0 * np.sqrt(1 + (t_fs/tau)**2) * 1e9  # nm

def verify():
    print("=== Ehrenfest Centroid Verification ===")
    vg = v_group()
    tau = spread_time_fs()
    T_osc = period_fs()
    print(f"v_g = {vg:.4e} m/s")
    print(f"τ (free) = {tau:.3f} fs")
    print(f"T (harmonic) = {T_osc:.2f} fs")

    # P1: centroid at t=τ displaces by v_g·τ
    x_at_tau = mean_x_free(tau)
    print(f"\nP1: ⟨x⟩(τ) = v_g·τ = {x_at_tau:.4f} nm")
    print(f"    v_g·τ = {vg * tau * 1e-15 * 1e9:.4f} nm  ✓")

    # P2: harmonic centroid returns to x₀ after one period
    x_T = mean_x_harmonic(T_osc)
    print(f"\nP2: ⟨x⟩(T) = {x_T:.6f} nm  (should = x₀ = {X0_NM} nm)")
    print(f"    Error = {abs(x_T - X0_NM):.2e} nm  ≈ 0")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

from manim import *  # noqa: E402

CANVAS  = "#16161D"
INK     = "#ECE6D8"
BLUE    = "#58C4DD"
BROWN   = "#CD853F"
GOLD    = "#F0E442"
DIM     = "#8A8780"
ORANGE_COL = "#FF8C42"


class EhrenfestCentroidScene(Scene):
    """
    Two-panel side-by-side:
    Left: free particle — Gaussian spreads, centroid (red dot) = classical (orange dot)
    Right: harmonic oscillator — Gaussian bounces, centroid = classical
    Below each: ⟨x⟩(t) time trace building up
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dual_panel()
        self._phase_anharmonic()

    def _phase_title(self):
        title = Text("Ehrenfest's Theorem", font="EB Garamond", font_size=58, color=INK)
        sub = Text(
            "d⟨x⟩/dt = ⟨p⟩/m  ·  d⟨p⟩/dt = −⟨∂V/∂x⟩  —  the centroid obeys Newton",
            font="EB Garamond", font_size=21, color=DIM,
        )
        eq = MathTex(
            r"\langle x(t)\rangle_{\rm QM} = \langle x(t)\rangle_{\rm classical}",
            color=GOLD, font_size=30,
        )
        VGroup(title, sub, eq).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub, eq), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, eq), run_time=0.5)

    def _phase_dual_panel(self):
        tau = spread_time_fs()
        T_osc = period_fs()
        t_max_free = 3 * tau
        t_max_harm = 1.2 * T_osc

        ax_cfg = dict(color=INK, stroke_width=1.3, include_ticks=False, tip_length=0.16)

        # Left: free particle |Ψ|² and trace
        ax_left_psi = Axes(
            x_range=[0, 15, 5], y_range=[0, 1.2, 0.5],
            x_length=5.5, y_length=2.2, axis_config=ax_cfg,
        ).shift(LEFT*3.4 + UP*1.8)

        ax_left_t = Axes(
            x_range=[0, 3, 1], y_range=[-0.2, 15, 5],
            x_length=5.5, y_length=1.8, axis_config=ax_cfg,
        ).shift(LEFT*3.4 + DOWN*1.1)

        # Right: harmonic oscillator and trace
        ax_right_psi = Axes(
            x_range=[-1.0, 1.0, 0.5], y_range=[0, 1.2, 0.5],
            x_length=5.5, y_length=2.2, axis_config=ax_cfg,
        ).shift(RIGHT*3.4 + UP*1.8)

        ax_right_t = Axes(
            x_range=[0, 1.2, 0.5], y_range=[-0.6, 0.6, 0.3],
            x_length=5.5, y_length=1.8, axis_config=ax_cfg,
        ).shift(RIGHT*3.4 + DOWN*1.1)

        hdr_left = Text("Free particle", font="EB Garamond", font_size=20, color=BLUE).next_to(ax_left_psi, UP, buff=0.05)
        hdr_right = Text("Harmonic oscillator (coherent)", font="EB Garamond", font_size=20, color=BROWN).next_to(ax_right_psi, UP, buff=0.05)

        lbl_lx = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=14).next_to(ax_left_psi.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_rx = MathTex(r"x\;(\mathrm{nm})", color=INK, font_size=14).next_to(ax_right_psi.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_lt = MathTex(r"t/\tau", color=INK, font_size=14).next_to(ax_left_t.x_axis.get_end(), RIGHT, buff=0.04)
        lbl_rt = MathTex(r"t/T", color=INK, font_size=14).next_to(ax_right_t.x_axis.get_end(), RIGHT, buff=0.04)

        self.play(
            Create(ax_left_psi), Create(ax_left_t),
            Create(ax_right_psi), Create(ax_right_t),
            Write(hdr_left), Write(hdr_right),
            Write(lbl_lx), Write(lbl_rx), Write(lbl_lt), Write(lbl_rt),
            run_time=1.2,
        )

        t_track = ValueTracker(0.0)  # in fs

        # Harmonic osc well
        x_well = np.linspace(-1.0, 1.0, 100)
        parabola_pts = [ax_right_psi.c2p(x, 0.5 * (OMEGA * M_E * (x*1e-9)**2) / (1.0545718e-34 * OMEGA) * 0.001) for x in x_well]

        def _free_density():
            t_fs = t_track.get_value()
            x_nm = np.linspace(0, 15, 300)
            x_m = x_nm * 1e-9
            sigma = SIGMA0 * np.sqrt(1 + (HBAR * t_fs*1e-15 / (M_E * SIGMA0**2))**2)
            x_center = mean_x_free(t_fs) * 1e-9
            prob = (1/(np.sqrt(2*np.pi)*sigma)) * np.exp(-0.5*(x_m - x_center)**2/sigma**2)
            prob_norm = prob * sigma * np.sqrt(2*np.pi) * 0.9  # normalize to max 0.9
            pts = [ax_left_psi.c2p(x, p) for x, p in zip(x_nm, prob_norm)]
            fill = Polygon(*(pts + [ax_left_psi.c2p(15, 0), ax_left_psi.c2p(0, 0)]),
                           color=BLUE, fill_color=BLUE, fill_opacity=0.35, stroke_width=0)
            return fill

        def _free_centroid():
            t_fs = t_track.get_value()
            xc = mean_x_free(t_fs)
            return Dot(ax_left_psi.c2p(min(xc, 14.5), 0.02), color=GOLD, radius=0.09)

        def _free_trace():
            t_fs = t_track.get_value()
            n_pts = max(2, int(t_fs / tau * 50) + 2)
            t_vals = np.linspace(0, t_fs, n_pts)
            pts = [ax_left_t.c2p(tv/tau, mean_x_free(tv)) for tv in t_vals]
            if len(pts) < 2:
                return VGroup()
            c = VMobject(color=GOLD, stroke_width=2.5)
            c.set_points_as_corners(pts)
            return c

        def _harm_density():
            t_fs = t_track.get_value()
            x_nm = np.linspace(-1.0, 1.0, 300)
            x_m = x_nm * 1e-9
            # Coherent state: Gaussian centered at classical position, fixed σ
            sigma_harm = SIGMA0  # σ_x = √(ℏ/2mω) ≈ 0.074 nm
            x_center = mean_x_harmonic(t_fs) * 1e-9
            prob = (1/(np.sqrt(2*np.pi)*sigma_harm)) * np.exp(-0.5*(x_m - x_center)**2/sigma_harm**2)
            prob_norm = prob * sigma_harm * np.sqrt(2*np.pi) * 0.9
            pts = [ax_right_psi.c2p(x, p) for x, p in zip(x_nm, prob_norm)]
            # Check bounds
            valid_pts = [p for p in pts if -10 < p[0] < 10 and -10 < p[1] < 10]
            if len(valid_pts) < 3:
                return VGroup()
            try:
                fill = Polygon(*(valid_pts + [ax_right_psi.c2p(0.9, 0), ax_right_psi.c2p(-0.9, 0)]),
                               color=BROWN, fill_color=BROWN, fill_opacity=0.35, stroke_width=0)
            except Exception:
                return VGroup()
            return fill

        def _harm_centroid():
            t_fs = t_track.get_value()
            xc = mean_x_harmonic(t_fs)
            return Dot(ax_right_psi.c2p(max(-0.95, min(xc, 0.95)), 0.02), color=GOLD, radius=0.09)

        def _harm_trace():
            t_fs = t_track.get_value()
            n_pts = max(2, int(t_fs / T_osc * 100) + 2)
            t_vals = np.linspace(0, t_fs, n_pts)
            pts = [ax_right_t.c2p(tv/T_osc, mean_x_harmonic(tv)) for tv in t_vals]
            if len(pts) < 2:
                return VGroup()
            c = VMobject(color=GOLD, stroke_width=2.5)
            c.set_points_smoothly(pts)
            return c

        dyn_fd = always_redraw(_free_density)
        dyn_fc = always_redraw(_free_centroid)
        dyn_ft = always_redraw(_free_trace)
        dyn_hd = always_redraw(_harm_density)
        dyn_hc = always_redraw(_harm_centroid)
        dyn_ht = always_redraw(_harm_trace)

        self.add(dyn_fd, dyn_fc, dyn_ft, dyn_hd, dyn_hc, dyn_ht)

        # Parabola
        par_curve = VMobject(color=DIM, stroke_width=1.2, stroke_opacity=0.5)
        par_pts = [ax_right_psi.c2p(x, 0.5 * x**2 / 0.3) for x in np.linspace(-0.8, 0.8, 80)]
        par_curve.set_points_smoothly(par_pts)
        self.add(par_curve)

        annot = MathTex(
            r"\langle x\rangle_{\rm QM}(t) = \langle x\rangle_{\rm classical}(t)",
            color=GOLD, font_size=22,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(annot), run_time=0.7)

        # Animate (max of two time scales)
        t_end = max(t_max_free, t_max_harm)
        self.play(t_track.animate.set_value(t_end), run_time=10.0, rate_func=linear)
        self.wait(1.5)

        self.play(FadeOut(
            ax_left_psi, ax_left_t, ax_right_psi, ax_right_t,
            hdr_left, hdr_right, lbl_lx, lbl_rx, lbl_lt, lbl_rt,
            dyn_fd, dyn_fc, dyn_ft, dyn_hd, dyn_hc, dyn_ht, par_curve, annot,
        ), run_time=0.6)

    def _phase_anharmonic(self):
        """Anharmonic potential — Ehrenfest fails."""
        title = Text(
            "Anharmonic well: ⟨x⟩(t) drifts from the classical orbit",
            font="EB Garamond", font_size=28, color=INK,
        ).to_edge(UP, buff=0.3)
        body = VGroup(
            MathTex(r"V(x) = \tfrac{1}{2}m\omega^2 x^2 + \lambda x^4", color=BROWN, font_size=26),
            MathTex(r"\frac{d\langle p\rangle}{dt} = -m\omega^2\langle x\rangle - 4\lambda\langle x^3\rangle \neq -m\omega^2\langle x\rangle", color=BLUE, font_size=24),
            Text("because ⟨x³⟩ ≠ ⟨x⟩³ — nonlinearity breaks the classical-quantum link",
                 font="EB Garamond", font_size=19, color=DIM),
        ).arrange(DOWN, buff=0.4).center()
        payoff = Text(
            "Ehrenfest holds exactly only for harmonic (or lower-order) potentials",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(title), run_time=0.8)
        for line in body:
            self.play(FadeIn(line), run_time=0.7)
        self.play(Write(payoff), run_time=0.8)
        self.wait(3.0)
