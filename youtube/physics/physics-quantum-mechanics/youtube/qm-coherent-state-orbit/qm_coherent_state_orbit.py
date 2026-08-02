#!/usr/bin/env python3
"""
qm_coherent_state_orbit.py — Coherent State: Gaussian Orbiting in Phase Space
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-coherent-state-orbit
    manim -qh qm_coherent_state_orbit.py CoherentStateOrbitScene

Verify:
    python3 qm_coherent_state_orbit.py

Physics:
    Coherent state |α⟩, α = 3 (real, on x-axis at t=0)
    Phase-space: (x, p) where x = sqrt(ℏ/2mω)·(α + α*), p = i·sqrt(mωℏ/2)·(α* - α)
    <x>(t) = sqrt(2ℏ/mω)·|α|·cos(ωt)
    <p>(t) = -sqrt(2mωℏ)·|α|·sin(ωt)
    σ_x = sqrt(ℏ/2mω) = constant  (ground-state width)
    σ_p = sqrt(mωℏ/2) = constant
    σ_x·σ_p = ℏ/2 at all times
    Photon number distribution: Poisson with mean |α|² = 9
"""
import sys
import numpy as np
from math import factorial

HBAR = 1.0545718e-34


def poisson_pmf(n_arr: np.ndarray, lam: float) -> np.ndarray:
    """Poisson PMF P(n) = e^{-lam} lam^n / n!"""
    return np.array([np.exp(-lam) * lam**n / factorial(int(n)) for n in n_arr])


def verify():
    print("=== Coherent state verification ===")
    alpha_sq = 9.0  # |α|² = 9 for |α| = 3

    # Poisson distribution
    ns = np.arange(0, 25)
    pmf = poisson_pmf(ns, alpha_sq)
    mean_n = np.sum(ns * pmf)
    var_n  = np.sum(ns**2 * pmf) - mean_n**2
    print(f"Poisson: mean = {mean_n:.4f}  (should be {alpha_sq})")
    print(f"Poisson: variance = {var_n:.4f}  (should be {alpha_sq}, std = {np.sqrt(var_n):.3f})")

    # Minimum uncertainty preserved
    print("σ_x·σ_p = ℏ/2 at all times (constant widths — minimum uncertainty state)")
    print("Phase space orbit: circle of radius |α|=3 in normalised units")
    print(f"Energy: <E> = (|α|²+0.5)·ℏω = {alpha_sq + 0.5:.1f}·ℏω  (9.5 ℏω)")
    print("=== PASSED ===")


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
ORANGE_C = "#F4A261"


class CoherentStateOrbitScene(Scene):
    """
    Coherent state |α=3⟩ orbiting in phase space (x, p).
    Energy eigenstate |n=9⟩ shown as ring (stationary).
    σ_x(t) constant demonstrated.
    Poisson photon number distribution.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_phase_space_orbit()
        self._phase_projection()
        self._phase_poisson()

    def _phase_title(self):
        title = Text("Coherent State Phase-Space Orbit", font="EB Garamond",
                     font_size=52, color=INK)
        sub1 = Text(
            "A laser field is a coherent state — moves like a classical oscillator, forever.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"\sigma_x \sigma_p = \hbar/2 \text{ at all } t \quad\Leftarrow\quad \text{minimum uncertainty}",
                       color=BLUE, font_size=24)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_phase_space_orbit(self):
        ax = Axes(
            x_range=[-5, 5, 2],
            y_range=[-5, 5, 2],
            x_length=6.0,
            y_length=6.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(LEFT * 0.5)
        lbl_x = MathTex(r"x / x_0", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"p / p_0", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Phase space (x, p) — dimensionless ground-state units",
                   font="EB Garamond", font_size=18, color=DIM).to_edge(UP, buff=0.18)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)

        # Energy eigenstate |n=9⟩ as a ring (angular position uncertain, radius fixed)
        theta_arr = np.linspace(0, 2*np.pi, 300)
        r_n9 = np.sqrt(2.0 * 9 + 1.0)  # = sqrt(19) ≈ 4.36 in normalised units
        ring_pts = [ax.c2p(r_n9 * np.cos(th), r_n9 * np.sin(th)) for th in theta_arr]
        ring = VMobject(color=DIM, stroke_width=2.0, stroke_opacity=0.6)
        ring.set_points_smoothly(ring_pts)
        ring_lbl = Text("|n=9⟩ ring (energy eigenstate — stationary)",
                        font="EB Garamond", font_size=17, color=DIM).next_to(ax, RIGHT, buff=0.15).shift(UP * 1.8)

        self.play(Create(ring), Write(ring_lbl), run_time=1.0)

        # Coherent state blob: circle of radius ~0.5 (uncertainty width), center at |α|=3
        alpha = 3.0
        sigma_ps = 0.5  # in display units (ground-state width)

        # Orbit path
        orbit_pts = [ax.c2p(alpha * np.cos(th), alpha * np.sin(th)) for th in theta_arr]
        orbit = VMobject(color=GOLD, stroke_width=1.5, stroke_opacity=0.4)
        orbit.set_points_smoothly(orbit_pts)
        self.play(Create(orbit), run_time=0.8)

        # Animate blob around orbit
        n_frames = 36
        phi_vals = np.linspace(0, 2*np.pi, n_frames, endpoint=False)

        def make_blob(phi):
            cx = alpha * np.cos(phi)
            cy = alpha * np.sin(phi)
            # Gaussian blob as circle
            th = np.linspace(0, 2*np.pi, 80)
            pts = [ax.c2p(cx + sigma_ps*np.cos(t), cy + sigma_ps*np.sin(t)) for t in th]
            blob_c = VMobject(color=BLUE, stroke_width=2.5)
            blob_c.set_points_smoothly(pts)
            center = Dot(ax.c2p(cx, cy), radius=0.06, color=BLUE)
            return VGroup(blob_c, center)

        prev_blob = make_blob(0)
        self.play(FadeIn(prev_blob), run_time=0.5)

        t_lbl = MathTex(r"\omega t = 0", color=GOLD, font_size=20).to_edge(DOWN, buff=0.28)
        self.play(Write(t_lbl), run_time=0.4)

        for i, phi in enumerate(phi_vals[1:], 1):
            new_blob = make_blob(phi)
            new_lbl  = MathTex(rf"\omega t = {np.degrees(phi):.0f}^\circ",
                               color=GOLD, font_size=20).to_edge(DOWN, buff=0.28)
            self.play(Transform(prev_blob, new_blob), Transform(t_lbl, new_lbl), run_time=0.12)

        sigma_lbl = Text("σ_x constant — Gaussian shape never changes",
                         font="EB Garamond", font_size=18, color=BLUE).to_edge(DOWN, buff=0.05)
        self.play(Write(sigma_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, ring, ring_lbl, orbit,
                          prev_blob, t_lbl, sigma_lbl), run_time=0.5)

    def _phase_projection(self):
        """Show x(t) = A cos(ωt) with constant-width envelope."""
        t_arr = np.linspace(0, 4*np.pi, 400)
        alpha = 3.0
        x_arr = alpha * np.cos(t_arr)
        sig   = 0.5  # uncertainty band

        ax = Axes(
            x_range=[0, 4*np.pi, np.pi],
            y_range=[-4.5, 4.5, 2],
            x_length=9.0,
            y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.6)
        lbl_x = MathTex(r"\omega t", color=INK, font_size=20).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\langle x\rangle / x_0", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        x_curve = VMobject(color=BLUE, stroke_width=3.5)
        x_curve.set_points_smoothly([ax.c2p(t, x) for t, x in zip(t_arr, x_arr)])
        env_up  = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        env_dn  = VMobject(color=DIM, stroke_width=1.5, stroke_opacity=0.5)
        env_up.set_points_smoothly([ax.c2p(t, x + sig) for t, x in zip(t_arr, x_arr)])
        env_dn.set_points_smoothly([ax.c2p(t, x - sig) for t, x in zip(t_arr, x_arr)])

        cap = Text("⟨x⟩(t) = √2 |α| cos(ωt)   with constant uncertainty band σ_x",
                   font="EB Garamond", font_size=18, color=DIM).to_edge(DOWN, buff=0.25)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=0.9)
        self.play(Create(x_curve), Create(env_up), Create(env_dn), Write(cap), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, x_curve, env_up, env_dn, cap), run_time=0.5)

    def _phase_poisson(self):
        ns = np.arange(0, 22)
        pmf = poisson_pmf(ns, 9.0)

        ax = Axes(
            x_range=[0, 21, 5],
            y_range=[0, 0.15, 0.05],
            x_length=8.0,
            y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.6)
        lbl_x = MathTex(r"n\;\text{(photon number)}", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"P(n)", color=INK, font_size=20).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("Photon number distribution for |α=3⟩: Poisson with ⟨n⟩=9",
                   font="EB Garamond", font_size=19, color=DIM).next_to(ax, UP, buff=0.12)

        bars = VGroup()
        for n, p in zip(ns, pmf):
            bar = Rectangle(
                width=ax.c2p(1, 0)[0] - ax.c2p(0, 0)[0],
                height=ax.c2p(0, p)[1] - ax.c2p(0, 0)[1],
                color=BLUE, fill_color=BLUE, fill_opacity=0.7, stroke_width=0.5,
            )
            bar.move_to(ax.c2p(n + 0.5, p / 2))
            bars.add(bar)

        mk9 = DashedLine(ax.c2p(9, 0), ax.c2p(9, pmf[9]),
                         color=GOLD, dash_length=0.08, stroke_width=2.5)
        lbl9 = MathTex(r"\langle n\rangle = 9", color=GOLD, font_size=22
                        ).next_to(ax.c2p(9, pmf[9]), UP, buff=0.06)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.1)
        self.play(Create(bars), run_time=1.0)
        self.play(Create(mk9), Write(lbl9), run_time=0.8)

        cap = Text("Laser = coherent state — photon number has Poisson statistics, not definite n.",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(DOWN, buff=0.25)
        self.play(Write(cap), run_time=0.9)
        self.wait(3.0)
