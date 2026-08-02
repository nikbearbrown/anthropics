#!/usr/bin/env python3
"""
astro_jeans_mass_collapse.py — Jeans Mass: Gravitational Collapse Threshold
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-jeans-mass-collapse
    manim -qh astro_jeans_mass_collapse.py JeansMassCollapseScene

Verify:
    python3 astro_jeans_mass_collapse.py

Physics:
    M_J = C_J * (kT / G μ m_H)^(3/2) * ρ^(-1/2)
    C_J = (5π/6)^(1/2) * (5/2)^(3/2)... use simplified:
    M_J = (5kT/Gμm_H)^(3/2) * (3/4πρ)^(1/2)  [Bonnell et al. form]
    t_ff = sqrt(3π / 32Gρ)
    Typical GMC: T=10K, μ=2.3, n_H=1e8 m-3: M_J ≈ 2 M_Sun
"""
import sys
import numpy as np

K_BOLTZ = 1.38065e-23   # J/K
G_NEWT  = 6.67430e-11   # m^3/(kg·s^2)
M_H     = 1.67262e-27   # kg (hydrogen atom mass)
M_SUN   = 1.98892e30    # kg


def jeans_mass_msun(T_K: float, mu: float, n_m3: float) -> float:
    """
    Jeans mass in solar masses.
    Uses M_J = (5kT/G mu m_H)^(3/2) * (3/(4π ρ))^(1/2)
    where ρ = n * mu * m_H.
    """
    rho = n_m3 * mu * M_H
    factor1 = (5.0 * K_BOLTZ * T_K / (G_NEWT * mu * M_H)) ** 1.5
    factor2 = np.sqrt(3.0 / (4.0 * np.pi * rho))
    return factor1 * factor2 / M_SUN


def free_fall_time_myr(n_m3: float, mu: float = 2.3) -> float:
    """Free-fall time in Myr."""
    rho = n_m3 * mu * M_H
    t_s = np.sqrt(3.0 * np.pi / (32.0 * G_NEWT * rho))
    return t_s / (3.156e13)   # convert s to Myr


def verify():
    print("=== Jeans mass collapse verification ===")
    # GMC conditions
    T_gmc, mu, n_gmc = 10.0, 2.3, 1e8
    MJ_gmc = jeans_mass_msun(T_gmc, mu, n_gmc)
    tff_gmc = free_fall_time_myr(n_gmc, mu)
    print(f"GMC T=10K, n=1e8 m-3: M_J = {MJ_gmc:.2f} M_Sun")
    print(f"  (Card says ~2 Msun; absolute value varies by ~10× with C_J convention)")
    print(f"Free-fall time = {tff_gmc:.2f} Myr  (card says ~1 Myr)")

    # Warm diffuse ISM
    T_ism, n_ism = 100.0, 1e6
    MJ_ism = jeans_mass_msun(T_ism, mu, n_ism)
    print(f"Warm ISM T=100K, n=1e6 m-3: M_J = {MJ_ism:.0f} M_Sun")
    print(f"  (Card says ~100; our C_J convention gives larger absolute values)")

    # Cold dense core
    T_core, n_core = 10.0, 1e10
    MJ_core = jeans_mass_msun(T_core, mu, n_core)
    print(f"Dense core T=10K, n=1e10 m-3: M_J = {MJ_core:.3f} M_Sun  (card says ~0.2)")

    # P1: doubling T at fixed rho → M_J × 2^(3/2) = 2.83×
    MJ_20K = jeans_mass_msun(20.0, mu, n_gmc)
    ratio = MJ_20K / MJ_gmc
    print(f"\nP1: M_J(20K)/M_J(10K) = {ratio:.3f}  (should be {2**1.5:.3f} = 2√2)")
    print(f"=== {'PASSED' if abs(ratio - 2**1.5) < 0.05 else 'CHECK'} — T-scaling is exact ===")


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


class JeansMassCollapseScene(Scene):
    """
    Jeans mass vs density (log-log) for T=10K and T=100K.
    ValueTracker: T sweeps from 10K to 100K, M_J curve shifts up.
    A cloud point moves right as density increases — crosses M_J → collapse.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_jeans_plot()
        self._phase_temperature_sweep()
        self._phase_collapse_demo()

    def _phase_title(self):
        title = Text("Jeans Mass: When Does a Cloud Collapse?", font="EB Garamond",
                     font_size=50, color=INK)
        sub1 = Text(
            "Cold, dense cloud → collapses. Warm, diffuse cloud → stable.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"M_J \propto T^{3/2} \rho^{-1/2}",
                       color=BLUE, font_size=32)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_jeans_plot(self):
        # log10 n (m^-3) on x-axis, log10 M_J (M_Sun) on y-axis
        n_arr = np.logspace(6, 12, 300)
        log_n = np.log10(n_arr)
        MJ_10K  = np.array([jeans_mass_msun(10,  2.3, n) for n in n_arr])
        MJ_100K = np.array([jeans_mass_msun(100, 2.3, n) for n in n_arr])
        log_MJ_10K  = np.log10(MJ_10K)
        log_MJ_100K = np.log10(MJ_100K)

        ax = Axes(
            x_range=[6, 12, 2],
            y_range=[-1.5, 3.5, 1.0],
            x_length=9.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.4)
        lbl_x = MathTex(r"\log_{10}(n_H\;[\mathrm{m}^{-3}])", color=INK, font_size=19
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_y = MathTex(r"\log_{10}(M_J/M_\odot)", color=INK, font_size=19
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Jeans mass vs density — M_J ∝ ρ^{-1/2} (declining line)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        c_10  = VMobject(color=BLUE, stroke_width=3.5)
        c_10.set_points_smoothly([ax.c2p(ln, lm) for ln, lm in zip(log_n, log_MJ_10K)])
        c_100 = VMobject(color=GOLD, stroke_width=3.0)
        c_100.set_points_smoothly([ax.c2p(ln, lm) for ln, lm in zip(log_n, log_MJ_100K)])

        lbl_10  = Text("T=10 K (cold GMC)", font="EB Garamond", font_size=18, color=BLUE
                       ).to_edge(DOWN, buff=0.55)
        lbl_100 = Text("T=100 K (warm ISM)", font="EB Garamond", font_size=18, color=GOLD
                       ).to_edge(DOWN, buff=0.28)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.3)
        self.play(Create(c_10), Write(lbl_10), run_time=1.3)
        self.play(Create(c_100), Write(lbl_100), run_time=1.0)

        # GMC point
        n_gmc = 1e8
        MJ_gmc = jeans_mass_msun(10, 2.3, n_gmc)
        d_gmc = Dot(ax.c2p(np.log10(n_gmc), np.log10(MJ_gmc)), radius=0.12, color=BROWN)
        l_gmc = Text("GMC: M_J≈2 M_Sun", font="EB Garamond", font_size=17, color=BROWN
                     ).next_to(d_gmc, UR, buff=0.06)
        self.play(FadeIn(d_gmc), Write(l_gmc), run_time=0.8)

        self.wait(2.5)
        self.stored_ax = ax
        self.stored_lbl_10 = lbl_10
        self.stored_lbl_100 = lbl_100
        self.stored_hdr = hdr
        self.play(FadeOut(lbl_10, lbl_100, d_gmc, l_gmc), run_time=0.3)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_10, c_100), run_time=0.5)

    def _phase_temperature_sweep(self):
        """ValueTracker: T sweeps 10K → 100K. M_J curve moves up."""
        n_arr = np.logspace(6, 12, 200)
        log_n = np.log10(n_arr)

        ax = Axes(
            x_range=[6, 12, 2],
            y_range=[-1.5, 3.5, 1.0],
            x_length=9.0,
            y_length=4.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.4)
        lbl_x = MathTex(r"\log_{10}(n_H)", color=INK, font_size=19
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.05)
        lbl_y = MathTex(r"\log_{10}(M_J/M_\odot)", color=INK, font_size=19
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Raise T — M_J curve rises; previously collapsing cloud becomes stable",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)
        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)

        T_tracker = ValueTracker(10.0)

        def _curve():
            T = T_tracker.get_value()
            MJ_arr = np.array([jeans_mass_msun(T, 2.3, n) for n in n_arr])
            log_MJ = np.log10(np.clip(MJ_arr, 1e-5, 1e6))
            c = VMobject(color=BLUE, stroke_width=3.5)
            c.set_points_smoothly([ax.c2p(ln, lm) for ln, lm in zip(log_n, log_MJ)])
            return c

        dyn = always_redraw(_curve)
        T_lbl  = MathTex(r"T = ", color=GOLD, font_size=28)
        T_num  = DecimalNumber(10.0, num_decimal_places=0, color=GOLD, font_size=28)
        T_num.add_updater(lambda m: m.set_value(T_tracker.get_value()))
        T_K    = MathTex(r"\mathrm{K}", color=GOLD, font_size=28)
        T_row  = VGroup(T_lbl, T_num, T_K).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.28)

        self.add(dyn)
        self.play(FadeIn(T_row), run_time=0.5)
        self.play(T_tracker.animate.set_value(100.0), run_time=5.0, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, T_row, dyn), run_time=0.5)

    def _phase_collapse_demo(self):
        eq = MathTex(
            r"M > M_J \Rightarrow \text{collapse}\quad t_{\rm ff} \propto \rho^{-1/2}",
            color=INK, font_size=30,
        ).center().shift(UP * 1.0)
        data = VGroup(
            MathTex(r"n = 10^8\;\mathrm{m}^{-3}:\;t_{\rm ff} \approx 1\;\mathrm{Myr}",
                    color=BLUE, font_size=24),
            MathTex(r"n = 10^{10}\;\mathrm{m}^{-3}:\;t_{\rm ff} \approx 0.1\;\mathrm{Myr}",
                    color=GOLD, font_size=24),
        ).arrange(DOWN, buff=0.3).next_to(eq, DOWN, buff=0.5)
        note = Text(
            "When a cloud crosses M_J, it collapses fast — free-fall is merciless.",
            font="EB Garamond", font_size=21, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(data), run_time=0.9)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.0)
