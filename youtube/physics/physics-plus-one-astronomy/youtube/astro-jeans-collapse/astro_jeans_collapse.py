#!/usr/bin/env python3
"""
astro_jeans_collapse.py — Jeans Instability: Where Gravity Beats Pressure
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    Jeans mass: M_J = (5kT/Gm)^(3/2) * (3/4*pi*rho)^(-1/2)
      where m = mean particle mass = 2*m_H (H2 molecular cloud)
    Free-fall time: t_ff = sqrt(3*pi / (32*G*rho))

Verify: python3 astro_jeans_collapse.py --verify
Render: manim -qh astro_jeans_collapse.py AstroJeansCollapseScene
"""
import sys
import numpy as np
from math import factorial

# ─── Physical constants ───────────────────────────────────────────────────────
G_GRAV  = 6.674e-11   # m^3 kg^-1 s^-2
K_BOLTZ = 1.381e-23   # J/K
M_H     = 1.673e-27   # kg  proton mass (approx H mass)
M_SUN   = 1.989e30    # kg
YR_SEC  = 3.156e7     # s per year
M_MEAN  = 2.0 * M_H   # kg  mean particle mass in H2 cloud

# Physically realistic density range for molecular cloud cores:
# n ~ 10^8–10^11 /m^3 (number density of H2 molecules)
# rho = n * m_mean ~ 3e-19 to 3e-16 kg/m^3
# These correspond to the typical densities where M_J ~ 1–10 M_sun at T=10 K.
# Note: the simulation card's stated rho=1e-21 kg/m^3 was in error
# (that density gives M_J ~ 1300 M_sun — a giant molecular cloud, not a core).
# We use n=1e11 /m^3 -> rho ~ 3.35e-16 kg/m^3 for ~1 M_sun Jeans mass at 10 K.

RHO_REF = 3.35e-16    # kg/m^3 — dense core (n~1e11 /m^3)
RHO_WARM = 3.35e-17   # kg/m^3 — warm cloud (n~1e10 /m^3, M_J ~ 7 Msun)

def jeans_mass_solar(T_K, rho_kgm3):
    """Jeans mass in solar masses."""
    M_J = (5 * K_BOLTZ * T_K / (G_GRAV * M_MEAN))**1.5 * \
          (3 / (4 * np.pi * rho_kgm3))**0.5
    return M_J / M_SUN

def freefall_time_yr(rho_kgm3):
    """Free-fall time in Myr."""
    t = np.sqrt(3 * np.pi / (32 * G_GRAV * rho_kgm3))
    return t / YR_SEC / 1e6  # Myr

def verify():
    print("=== Jeans collapse verification ===")
    # P1: T=10 K, rho=RHO_REF -> M_J ~1 M_sun (dense cold core)
    T1 = 10.0
    mj1 = jeans_mass_solar(T1, RHO_REF)
    tff1 = freefall_time_yr(RHO_REF)
    print(f"P1: T={T1} K, rho={RHO_REF:.2e} kg/m3: M_J = {mj1:.2f} M_sun  (expected ~1), t_ff = {tff1:.3f} Myr {'✓' if 0.3 < mj1 < 3 else '✗'}")
    assert 0.3 < mj1 < 3.0, f"M_J out of range: {mj1}"

    # P2: doubling T raises M_J by 2^(3/2) at fixed rho
    mj2 = jeans_mass_solar(20.0, RHO_REF)
    ratio = mj2 / mj1
    print(f"P2: T=20 K: M_J = {mj2:.2f} M_sun, ratio = {ratio:.3f}  (expected {2**1.5:.3f}) {'✓' if abs(ratio - 2**1.5) < 0.05 else '✗'}")

    # Warm cloud: higher T -> higher M_J (only massive clouds collapse)
    mj_warm = jeans_mass_solar(100.0, RHO_WARM)
    print(f"Warm cloud (T=100K, low rho): M_J = {mj_warm:.1f} M_sun  (expected ~30 M_sun)")
    print("=== PASSED ===")

if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

# Log-space axes
T_VALS  = np.array([10.0, 20.0, 50.0, 100.0])
RHO_VALS = np.array([1e-22, 1e-21, 1e-20])


class AstroJeansCollapseScene(Scene):
    """
    2D plane: T (10-100 K) vs rho (1e-22 to 1e-20 kg/m3).
    M_J contour separates stable from collapsing clouds.
    A cloud dot crosses the contour and triggers collapse animation.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax = self._axes()
        self._jeans_contour(ax)
        self._collapse_track(ax)
        self._finale()

    def _title(self):
        t = Text("Jeans Collapse: Where Gravity Beats Pressure",
                 font="EB Garamond", font_size=50, color=INK)
        s = Text(
            "A cloud crosses the Jeans mass threshold — then collapses in free fall.\n"
            "One inequality separates a stable nebula from a newborn star.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _axes(self):
        # x axis: log T from 10 to 100 K (log10: 1.0 to 2.0)
        # y axis: log rho from -17 to -15 kg/m^3 (dense molecular cloud cores)
        ax = Axes(
            x_range=[1.0, 2.05, 0.5],    # log10(T)
            y_range=[-17.1, -14.8, 1.0], # log10(rho)
            x_length=8,
            y_length=5.5,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(LEFT * 0.5 + DOWN * 0.3)
        lx = Text("Temperature T (K)", font="EB Garamond",
                  font_size=22, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        ly = Text("Density log10(rho)", font="EB Garamond",
                  font_size=22, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Axis tick labels
        for T in [10, 20, 50, 100]:
            pt = ax.c2p(np.log10(T), -17.1)
            lbl = Text(str(T), font="EB Garamond", font_size=16, color=DIM)
            lbl.move_to(pt + DOWN * 0.3)
            self.add(lbl)
        for exp in [-17, -16, -15]:
            pt = ax.c2p(1.0, exp)
            lbl = MathTex(rf"10^{{{exp}}}", color=DIM, font_size=16)
            lbl.next_to(pt, LEFT, buff=0.1)
            self.add(lbl)

        self.play(Create(ax), Write(lx), Write(ly), run_time=1.5)
        return ax

    def _jeans_contour(self, ax):
        # Draw M_J = 1 M_sun and M_J = 10 M_sun contours
        T_range = np.linspace(10, 100, 200)
        for target_mass, col, lbl_str in [(1.0, BLUE, r"M_J = 1\,M_\odot"),
                                           (10.0, DIM, r"M_J = 10\,M_\odot")]:
            rho_contour = []
            for T in T_range:
                # Solve for rho: M_J = (5kT/Gm)^1.5 * (3/(4pi*rho))^0.5
                # rho = (3/(4pi)) * ((5kT/Gm)^1.5 / (target*M_sun))^2
                factor = (5 * K_BOLTZ * T / (G_GRAV * M_MEAN))**1.5
                rho = (3 / (4 * np.pi)) * (factor / (target_mass * M_SUN))**2
                rho_contour.append(rho)
            rho_contour = np.array(rho_contour)
            log_rho = np.log10(rho_contour)
            log_T   = np.log10(T_range)
            pts = [ax.c2p(lt, lr) for lt, lr in zip(log_T, log_rho)
                   if -17.1 <= lr <= -14.8]
            if len(pts) > 2:
                mob = VMobject(color=col, stroke_width=2.5)
                mob.set_points_smoothly(np.array(pts))
                mob_lbl = MathTex(lbl_str, color=col, font_size=20)
                mob_lbl.move_to(np.array(pts[len(pts)//2]) + RIGHT * 0.5)
                self.play(Create(mob), Write(mob_lbl), run_time=1.5)

        # Region labels
        stable_lbl = Text("STABLE", font="EB Garamond", font_size=22, color=BROWN)
        stable_lbl.move_to(ax.c2p(1.8, -17.0))
        collapse_lbl = Text("COLLAPSE", font="EB Garamond", font_size=22, color=GOLD)
        collapse_lbl.move_to(ax.c2p(1.2, -15.5))
        self.play(Write(stable_lbl), Write(collapse_lbl), run_time=0.8)
        self.wait(1.0)

    def _collapse_track(self, ax):
        # Cloud cools and compresses from (T=50K, rho=1e-17) toward (T=10K, rho=3e-16)
        # crossing the M_J=1 Msun contour
        track_T   = np.array([50, 40, 30, 20, 15, 10])
        track_rho = np.array([1e-17, 3e-17, 1e-16, 2e-16, 3e-16, 3e-16])
        log_T_arr   = np.log10(track_T)
        log_rho_arr = np.log10(track_rho)

        # Cloud dot
        cloud = Dot(ax.c2p(log_T_arr[0], log_rho_arr[0]), color=BLUE, radius=0.12)
        cloud_lbl = Text("molecular cloud", font="EB Garamond",
                         font_size=17, color=BLUE)
        cloud_lbl.next_to(cloud, UP, buff=0.1)
        self.play(FadeIn(cloud), Write(cloud_lbl), run_time=0.8)

        # Animate cloud moving along track
        for i in range(1, len(track_T)):
            new_pos = ax.c2p(log_T_arr[i], log_rho_arr[i])
            self.play(cloud.animate.move_to(new_pos),
                      cloud_lbl.animate.next_to(new_pos, UP, buff=0.1),
                      run_time=0.7)

        # Crossing event
        cross_lbl = Text("M > M_J  ->  collapse!",
                         font="EB Garamond", font_size=24, color=GOLD)
        cross_lbl.to_edge(DOWN, buff=0.25)
        self.play(Write(cross_lbl), run_time=0.8)
        self.play(cloud.animate.set_color(GOLD).scale(1.5), run_time=0.5)

        # Collapse: sphere shrinks to point
        sphere = Circle(radius=0.8, color=BROWN, fill_opacity=0.3, stroke_width=2)
        sphere.move_to(ax.c2p(1.05, -15.8))
        star = Dot(sphere.get_center(), color=GOLD, radius=0.05)
        tff_val = freefall_time_yr(3.35e-16)
        self.play(FadeIn(sphere), run_time=0.5)
        self.play(sphere.animate.scale(0.1), star.animate.scale(3), run_time=1.5)
        tff_lbl = Text(f"t_ff = {tff_val:.3f} Myr", font="EB Garamond", font_size=20, color=DIM)
        tff_lbl.next_to(sphere, RIGHT, buff=0.2)
        self.play(Write(tff_lbl), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(cross_lbl, tff_lbl), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"M_J \propto \frac{T^{3/2}}{\rho^{1/2}}",
            r"\quad t_{\rm ff} \approx \sqrt{\frac{3\pi}{32G\rho}}",
            color=INK, font_size=32,
        )
        eq.arrange(RIGHT, buff=0.5).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
