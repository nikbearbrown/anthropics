#!/usr/bin/env python3
"""
physics_orbital_speed_vs_radius.py — Orbital Speed v = √(GM/r) vs Radius
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  v = √(GM/r)
  G = 6.674e-11, M = 1.989e30 kg (Sun)
  ISS (Earth): r = 6.77e6 m → 7.67 km/s, T = 92 min
  GPS:         r = 26.56e6 m → 3.87 km/s, T ≈ 12 h
  GEO:         r = 42.16e6 m → 3.07 km/s, T = 24 h
  Plus solar system: Earth 1 AU, Mars 1.52 AU, Jupiter 5.2 AU

Testable predictions:
  P1: ISS v=7.67 km/s, T=92 min at r=6.77e6 m
  P2: GPS/ISS speed ratio = 1.98 (not 3.93 as 1/r would give)

Run standalone verification:
  python3 physics_orbital_speed_vs_radius.py --verify

Render:
  manim -qh physics_orbital_speed_vs_radius.py OrbitalSpeedVsRadiusScene
"""
import sys
import numpy as np

G_EARTH = 6.674e-11   # N m²/kg²
M_SUN   = 1.989e30    # kg
M_EARTH = 5.972e24    # kg
AU      = 1.496e11    # m

# Earth-orbit objects (around Earth)
EARTH_ORBITS = {
    "ISS":  {"r_m": 6.77e6,    "label": "ISS"},
    "GPS":  {"r_m": 26.56e6,   "label": "GPS"},
    "GEO":  {"r_m": 42.16e6,   "label": "GEO"},
}

# Solar system planets
SOLAR_ORBITS = {
    "Mercury": {"r_AU": 0.387},
    "Venus":   {"r_AU": 0.723},
    "Earth":   {"r_AU": 1.000},
    "Mars":    {"r_AU": 1.524},
    "Jupiter": {"r_AU": 5.203},
    "Saturn":  {"r_AU": 9.537},
}

def v_orbit(r_m, M):
    return np.sqrt(G_EARTH * M / r_m)

def period_s(r_m, M):
    return 2 * np.pi * r_m / v_orbit(r_m, M)

def verify():
    print("=== Orbital speed verification ===")
    for name, d in EARTH_ORBITS.items():
        v = v_orbit(d["r_m"], M_EARTH)
        T = period_s(d["r_m"], M_EARTH)
        print(f"  {name}: r={d['r_m']:.3e} m, v={v/1000:.3f} km/s, T={T/60:.1f} min")
    v_iss = v_orbit(EARTH_ORBITS["ISS"]["r_m"], M_EARTH)
    v_gps = v_orbit(EARTH_ORBITS["GPS"]["r_m"], M_EARTH)
    print(f"  Ratio v_ISS/v_GPS = {v_iss/v_gps:.4f}  (expect ≈ 1.98)")
    print()
    print("  Solar system:")
    for name, d in SOLAR_ORBITS.items():
        r_m = d["r_AU"] * AU
        v = v_orbit(r_m, M_SUN) / 1000
        print(f"    {name}: r={d['r_AU']:.3f} AU, v={v:.2f} km/s")
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

PLANET_COLORS = {
    "Mercury": "#AAAAAA", "Venus": GOLD, "Earth": BLUE,
    "Mars": BROWN, "Jupiter": "#FF8C00", "Saturn": "#DAA520",
}


class OrbitalSpeedVsRadiusScene(Scene):
    """
    v = √(GM/r) curve from 0.3 to 10 AU + planet callouts.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Orbital Speed  v = √(GM/r)",
                     font="EB Garamond", font_size=56, color=INK)
        sub   = Text(
            "Speed falls as 1/√r — slower and slower with altitude",
            font="EB Garamond", font_size=24, color=DIM,
        )
        sub2  = Text(
            "Kepler III: T² ∝ r³  ↔  v ∝ r⁻¹/²",
            font="EB Garamond", font_size=22, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Axes (AU vs km/s for solar system) ────────────────────────────
        r_min_AU = 0.3
        r_max_AU = 10.5
        v_max_kms = 55.0

        ax = Axes(
            x_range=[r_min_AU, r_max_AU, 1.0],
            y_range=[0, v_max_kms, 10],
            x_length=9.5,
            y_length=5.2,
            axis_config=dict(color=INK, stroke_width=1.5, include_ticks=True, tip_length=0.15),
        ).shift(DOWN * 0.3)

        lbl_x = Text("r (AU)",    font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.1)
        lbl_y = Text("v (km/s)", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP,    buff=0.08)

        self.play(Create(ax), Write(lbl_x), Write(lbl_y), run_time=1.2)

        # ── v = √(GM/r) curve ─────────────────────────────────────────────
        r_AU_arr = np.linspace(r_min_AU, r_max_AU, 600)
        r_m_arr  = r_AU_arr * AU
        v_kms    = np.sqrt(G_EARTH * M_SUN / r_m_arr) / 1e3

        pts  = [ax.c2p(float(r), float(v)) for r, v in zip(r_AU_arr, v_kms)]
        curve = VMobject(color=BLUE, stroke_width=3.0)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=2.5)
        self.wait(0.5)

        # ── Planet markers ─────────────────────────────────────────────────
        planet_dots = VGroup()
        planet_lbls = VGroup()
        for pname, d in SOLAR_ORBITS.items():
            r_AU = d["r_AU"]
            v_km = np.sqrt(G_EARTH * M_SUN / (r_AU * AU)) / 1e3
            col  = PLANET_COLORS.get(pname, INK)
            dot  = Dot(ax.c2p(r_AU, v_km), color=col, radius=0.10)
            lbl  = Text(f"{pname}\n{v_km:.1f} km/s",
                        font="EB Garamond", font_size=14, color=col)
            # Offset labels to avoid overlap
            if r_AU < 2:
                lbl.next_to(dot, UP + RIGHT, buff=0.05)
            else:
                lbl.next_to(dot, UP, buff=0.06)
            planet_dots.add(dot)
            planet_lbls.add(lbl)

        self.play(FadeIn(planet_dots), Write(planet_lbls), run_time=1.2)
        self.wait(0.6)

        # ── 1/√r annotation ────────────────────────────────────────────────
        slope_anno = Text(
            "Slope on log-log: −1/2  (1/√r not 1/r)",
            font="EB Garamond", font_size=22, color=GOLD,
        ).to_edge(UP, buff=0.22)
        self.play(Write(slope_anno), run_time=0.9)
        self.wait(0.7)

        # ── Formula ────────────────────────────────────────────────────────
        eq = MathTex(
            r"v = \sqrt{\frac{GM}{r}}\;\;\;T = \frac{2\pi r}{v} = 2\pi\sqrt{\frac{r^3}{GM}}",
            color=INK, font_size=26,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.2)
        self.wait(3.0)
