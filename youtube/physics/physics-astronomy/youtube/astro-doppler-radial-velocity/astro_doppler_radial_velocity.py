#!/usr/bin/env python3
"""
astro_doppler_radial_velocity.py — Spectral Line Doppler Shift: Radial Velocity
SILENT SLATE — math-explainer (brownblue), physics-astronomy book.

Render:
    cd physics-astronomy/youtube/astro-doppler-radial-velocity
    manim -qh astro_doppler_radial_velocity.py DopplerRadialVelocityScene

Verify:
    python3 astro_doppler_radial_velocity.py

Physics:
    Δλ/λ0 = v_r/c (non-relativistic Doppler)
    Hα rest λ = 656.281 nm
    51 Peg b: K = 56 m/s, P = 4.23 days
    v_r = 300 km/s → Δλ = 0.66 nm → λ_obs = 656.94 nm
"""
import sys
import numpy as np

C_LIGHT = 2.99792458e8   # m/s

# Fraunhofer / key spectral lines (rest wavelengths in nm)
LINES = {
    r"H\alpha":   656.281,
    r"H\beta":    486.134,
    r"Na\,D":     589.292,
    r"Ca\,K":     393.368,
}


def obs_wavelength(lam0_nm: float, v_r_ms: float) -> float:
    """Observed wavelength in nm for radial velocity v_r (m/s)."""
    return lam0_nm * (1.0 + v_r_ms / C_LIGHT)


def verify():
    print("=== Doppler radial velocity verification ===")
    # P1: Hα at v=300 km/s
    lam_ha = LINES[r"H\alpha"]
    v_300 = 300.0e3
    lam_obs = obs_wavelength(lam_ha, v_300)
    dlam = lam_obs - lam_ha
    print(f"Hα at v=300 km/s: λ_obs = {lam_obs:.4f} nm  (card says 656.96 nm)")
    print(f"  Δλ = {dlam:.4f} nm  (card says 0.66 nm)")

    # P2: 51 Peg b K=56 m/s
    K_51peg = 56.0
    dlam_51peg = obs_wavelength(lam_ha, K_51peg) - lam_ha
    print(f"51 Peg b K=56 m/s: Δλ = {dlam_51peg*1000:.3f} pm  (card says 0.22 pm)")

    # Galaxy at v=40000 km/s (z=0.134)
    lam_CaK = LINES[r"Ca\,K"]
    v_gal   = 4.0e7  # m/s
    lam_gal = obs_wavelength(lam_CaK, v_gal)
    z_gal   = (lam_gal - lam_CaK) / lam_CaK
    print(f"Galaxy CaK shifted to {lam_gal:.1f} nm, z={z_gal:.4f}  (card says z=0.134)")
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
RED_C  = "#FF6B6B"


class DopplerRadialVelocityScene(Scene):
    """
    Spectral line Doppler shift demo.
    1. Spectrum strip with key lines at rest.
    2. v_r slider: lines shift red/blueward.
    3. 51 Peg b: tiny Hα oscillation at 4.23-day period.
    4. Galaxy example: CaK shifted to 450 nm → z=0.134.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_spectrum_and_slider()
        self._phase_51peg()
        self._phase_galaxy()

    def _phase_title(self):
        title = Text("Spectral Line Doppler Shift", font="EB Garamond",
                     font_size=54, color=INK)
        sub1 = Text(
            "Astronomers measure stellar speeds without leaving Earth — via wavelength shifts.",
            font="EB Garamond", font_size=20, color=DIM,
        )
        sub2 = MathTex(r"\frac{\Delta\lambda}{\lambda_0} = \frac{v_r}{c}",
                       color=BLUE, font_size=36)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _phase_spectrum_and_slider(self):
        # Spectrum bar: 380–700 nm displayed as a colored rectangle
        ax_spec = Axes(
            x_range=[380, 700, 100],
            y_range=[0, 1, 1],
            x_length=9.5,
            y_length=1.0,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.1),
        ).shift(UP * 1.5)
        lbl_spec = MathTex(r"\lambda\;(\mathrm{nm})", color=INK, font_size=19
                           ).next_to(ax_spec.x_axis.get_end(), RIGHT, buff=0.05)
        hdr = Text("Spectral lines shift together — same v_r for all",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)

        self.play(Create(ax_spec), Write(lbl_spec), Write(hdr), run_time=1.0)

        v_tracker = ValueTracker(0.0)   # m/s

        def _line_group():
            v = v_tracker.get_value()
            grp = VGroup()
            for name, lam0 in LINES.items():
                lam_obs = obs_wavelength(lam0, v)
                if 380 <= lam_obs <= 700:
                    c = BLUE if v < 0 else (RED_C if v > 0 else GOLD)
                    seg = DashedLine(
                        ax_spec.c2p(lam_obs, 0.05),
                        ax_spec.c2p(lam_obs, 0.95),
                        color=c, dash_length=0.05, stroke_width=3.0,
                    )
                    grp.add(seg)
            return grp

        dyn_lines = always_redraw(_line_group)

        # Initial rest-frame labels
        rest_labels = VGroup()
        for name, lam0 in LINES.items():
            lbl = MathTex(name, color=GOLD, font_size=15).next_to(
                ax_spec.c2p(lam0, 0.95), UP, buff=0.04)
            rest_labels.add(lbl)

        self.add(dyn_lines)
        self.play(FadeIn(rest_labels), run_time=0.8)

        # v_r readout
        v_lbl = MathTex(r"v_r = ", color=INK, font_size=26)
        v_num = DecimalNumber(0.0, num_decimal_places=0, color=INK, font_size=26)
        v_num.add_updater(lambda m: m.set_value(v_tracker.get_value() / 1000))
        v_km  = MathTex(r"\;\mathrm{km/s}", color=INK, font_size=26)
        v_row = VGroup(v_lbl, v_num, v_km).arrange(RIGHT, buff=0.08).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(v_row), run_time=0.5)

        # Sweep: 0 → +300 km/s (redshift) → 0 → -200 km/s (blueshift) → 0
        self.play(v_tracker.animate.set_value(300e3), run_time=2.5, rate_func=smooth)
        self.wait(0.3)
        self.play(v_tracker.animate.set_value(-200e3), run_time=3.0, rate_func=smooth)
        self.wait(0.3)
        self.play(v_tracker.animate.set_value(0.0), run_time=1.5, rate_func=smooth)
        self.wait(0.5)
        self.play(FadeOut(ax_spec, lbl_spec, hdr, rest_labels, v_row, dyn_lines), run_time=0.4)

    def _phase_51peg(self):
        """51 Peg b: Hα oscillates at 4.23-day period with K=56 m/s."""
        lam_ha = LINES[r"H\alpha"]
        K = 56.0   # m/s
        P_days = 4.23
        t_arr  = np.linspace(0, 2 * P_days, 300)
        v_arr  = K * np.cos(2 * np.pi * t_arr / P_days)
        lam_arr = np.array([obs_wavelength(lam_ha, v) for v in v_arr])

        ax = Axes(
            x_range=[0, 2 * P_days, P_days],
            y_range=[lam_ha - 0.00005, lam_ha + 0.00005, 0.00002],
            x_length=8.5,
            y_length=3.5,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=False, tip_length=0.18),
        ).shift(UP * 0.5)
        lbl_x = MathTex(r"t\;(\mathrm{days})", color=INK, font_size=20
                        ).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = MathTex(r"\lambda_{H\alpha}\;(\mathrm{nm})", color=INK, font_size=20
                        ).next_to(ax.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("51 Peg: stellar Hα oscillates at 4.23-day period, K=56 m/s",
                   font="EB Garamond", font_size=18, color=DIM).to_edge(UP, buff=0.18)

        c_rv = VMobject(color=BLUE, stroke_width=3.0)
        c_rv.set_points_smoothly([ax.c2p(t, lam) for t, lam in zip(t_arr, lam_arr)])

        cap = Text("Δλ = 0.22 pm — the measurement that discovered the first hot Jupiter.",
                   font="EB Garamond", font_size=19, color=GOLD).to_edge(DOWN, buff=0.28)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), Write(hdr), run_time=1.2)
        self.play(Create(c_rv), run_time=1.5)
        self.play(Write(cap), run_time=0.9)
        self.wait(2.5)
        self.play(FadeOut(ax, lbl_x, lbl_y, hdr, c_rv, cap), run_time=0.5)

    def _phase_galaxy(self):
        lam_CaK = LINES[r"Ca\,K"]
        v_gal   = 4.0e7   # 40,000 km/s
        lam_obs = obs_wavelength(lam_CaK, v_gal)
        z       = (lam_obs - lam_CaK) / lam_CaK

        eq = VGroup(
            MathTex(
                rf"\mathrm{{Ca\,K}}\;{lam_CaK:.1f}\;\mathrm{{nm}} \to {lam_obs:.1f}\;\mathrm{{nm}}",
                color=INK, font_size=26,
            ),
            MathTex(
                rf"z = \frac{{{lam_obs:.1f} - {lam_CaK:.1f}}}{{{lam_CaK:.1f}}} = {z:.3f}",
                color=BLUE, font_size=26,
            ),
            MathTex(
                r"v_r = z c \approx 40{,}000\;\mathrm{km/s}",
                color=GOLD, font_size=26,
            ),
        ).arrange(DOWN, buff=0.35).center().shift(UP * 0.3)
        note = Text(
            "The spectrum is the thermometer, speedometer, and distance ladder for astronomy.",
            font="EB Garamond", font_size=19, color=DIM,
        ).to_edge(DOWN, buff=0.3)
        for part in eq:
            self.play(Write(part), run_time=0.9)
        self.play(FadeIn(note), run_time=0.8)
        self.wait(3.0)
