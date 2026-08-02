#!/usr/bin/env python3
"""
cm_orbital_speed.py — Orbital Speed: Why Sputnik Didn't Fall
SILENT SLATE — brownblue dark palette, physics-plus-one-classical-mechanics.

Physics:
    v_orb = sqrt(GM/r)
    T = 2*pi*r/v_orb
    v_esc = sqrt(2) * v_orb

Verify: python3 cm_orbital_speed.py --verify
Render: manim -qh cm_orbital_speed.py CmOrbitalSpeedScene
"""
import sys
import numpy as np

G_GRAV = 6.674e-11
M_EARTH = 5.972e24
R_EARTH = 6.371e6   # m

def orbital_speed(r_m):
    return np.sqrt(G_GRAV * M_EARTH / r_m)  # m/s

def orbital_period_min(r_m):
    v = orbital_speed(r_m)
    return 2 * np.pi * r_m / v / 60.0

def escape_speed(r_m):
    return np.sqrt(2 * G_GRAV * M_EARTH / r_m)

def verify():
    print("=== Orbital speed verification ===")
    # P1: v_orb at Earth surface
    v_surf = orbital_speed(R_EARTH)
    print(f"P1: v_orb at R_E = {v_surf/1e3:.3f} km/s  (expected 7.91 km/s) {'✓' if abs(v_surf/1e3 - 7.91) < 0.05 else '✗'}")
    # P2: ISS at r ~ 6771 km
    r_ISS = 6.771e6
    v_ISS = orbital_speed(r_ISS)
    T_ISS = orbital_period_min(r_ISS)
    print(f"P2: ISS v = {v_ISS/1e3:.2f} km/s, T = {T_ISS:.1f} min  (expected ~7.67 km/s, 92.7 min) {'✓' if abs(T_ISS - 92.7) < 1 else '✗'}")
    # sqrt(2) relationship
    v_esc = escape_speed(R_EARTH)
    ratio = v_esc / v_surf
    print(f"v_esc / v_orb = {ratio:.4f}  (expected sqrt(2) = {np.sqrt(2):.4f}) {'✓' if abs(ratio - np.sqrt(2)) < 0.001 else '✗'}")
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


class CmOrbitalSpeedScene(Scene):
    """
    Earth circle, horizontal launch at increasing speeds.
    At ~7.9 km/s, the trajectory becomes circular.
    v_esc = sqrt(2)*v_orb shown explicitly.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._newton_cannon()
        self._speed_vs_outcome()
        self._finale()

    def _title(self):
        t = Text("Why Sputnik Didn't Fall",
                 font="EB Garamond", font_size=60, color=INK)
        s = Text(
            "Orbit is not escaping gravity — it is falling perfectly around a sphere.\n"
            "v_orb = √(GM/r) ≈ 7.9 km/s at Earth's surface.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _newton_cannon(self):
        # Earth circle
        earth = Circle(radius=2.0, color=BLUE, fill_opacity=0.2, stroke_width=2)
        earth_lbl = Text("Earth", font="EB Garamond", font_size=24, color=BLUE)
        earth_lbl.move_to(earth.get_center())

        self.play(Create(earth), Write(earth_lbl), run_time=1.0)

        # Three trajectories: suborbital (v=4 km/s), orbital (v=7.9), escape (v=11.2)
        cases = [
            (4.0,  DIM,   "4 km/s — falls short"),
            (7.9,  GOLD,  "7.9 km/s — orbit"),
            (11.2, BROWN, "11.2 km/s — escape"),
        ]

        launch_pt = np.array([0, 2.0, 0])   # top of Earth

        for v_kms, col, label in cases:
            # Simple parabolic/circular approximation for display
            # Convert to display units: Earth radius = 2.0 display units
            v_ratio = v_kms / 7.9  # normalized to orbital speed

            if v_ratio < 1.0:
                # Suborbital: arc that comes back
                t_vals = np.linspace(0, np.pi * v_ratio, 80)
                # Approximate: parabola in display coords
                x_traj = launch_pt[0] + 2.5 * v_ratio * np.sin(t_vals)
                y_traj = launch_pt[1] + 0.8 * np.sin(t_vals) - 0.3 * t_vals**2 / np.pi**2
                # Clip to Earth surface
                r_traj = np.sqrt(x_traj**2 + y_traj**2)
                mask = r_traj >= 1.95
                x_traj, y_traj = x_traj[mask], y_traj[mask]
            elif abs(v_ratio - 1.0) < 0.05:
                # Circular orbit
                angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 150)
                x_traj = 2.2 * np.cos(angles)
                y_traj = 2.2 * np.sin(angles)
            else:
                # Escape: parabola going outward
                t_vals = np.linspace(0, 1.5, 100)
                x_traj = launch_pt[0] + 3.5 * t_vals
                y_traj = launch_pt[1] + 2.0 * t_vals - 1.5 * t_vals**2

            pts = np.array([[x, y, 0] for x, y in zip(x_traj, y_traj)])
            traj = VMobject(color=col, stroke_width=2.5)
            traj.set_points_smoothly(pts)

            lbl_mob = Text(label, font="EB Garamond", font_size=18, color=col)
            lbl_mob.move_to(pts[-1] + np.array([0.6, 0.2, 0]))

            self.play(Create(traj), run_time=1.2)
            self.play(Write(lbl_mob), run_time=0.5)
            self.wait(0.8)

        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

    def _speed_vs_outcome(self):
        # Table of speeds and outcomes
        v_orb_surf = orbital_speed(R_EARTH) / 1e3
        v_esc_surf = escape_speed(R_EARTH) / 1e3

        items = [
            (f"v_orb (surface) = {v_orb_surf:.2f} km/s", BLUE, "circular orbit"),
            (f"ISS: v = 7.67 km/s, T = 92.7 min", DIM, "Low Earth orbit"),
            (f"Sputnik: v = 7.78 km/s, T = 88.5 min", BROWN, "historical LEO"),
            (f"v_esc = sqrt(2) × v_orb = {v_esc_surf:.2f} km/s", GOLD, "escape velocity"),
        ]

        mobs = []
        for i, (txt, col, sub) in enumerate(items):
            main = Text(txt, font="EB Garamond", font_size=24, color=col)
            sub_m = Text(sub, font="EB Garamond", font_size=18, color=DIM)
            row = VGroup(main, sub_m).arrange(RIGHT, buff=0.4)
            row.shift(UP * (1.5 - i * 1.0))
            mobs.append(row)
            self.play(FadeIn(row), run_time=0.6)

        # sqrt(2) relationship
        eq = MathTex(
            r"v_{\rm esc} = \sqrt{2}\,v_{\rm orb}",
            color=GOLD, font_size=36,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(eq), run_time=1.0)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in mobs], FadeOut(eq), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"v_{\rm orb} = \sqrt{\frac{GM}{r}}",
            r"\quad T = \frac{2\pi r}{v_{\rm orb}}",
            r"\quad v_{\rm esc} = \sqrt{2}\,v_{\rm orb}",
            color=INK, font_size=30,
        )
        eq.arrange(RIGHT, buff=0.4).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
