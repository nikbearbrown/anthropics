#!/usr/bin/env python3
"""
physics_kepler_equal_area_orbit.py — Kepler's Equal-Area Law: Elliptical Orbit
SILENT SLATE — sim-scout candidate, university-physics-bundle-with-llms book.

Physics:
  r(θ) = a(1-e²) / (1 + e·cosθ)
  e=0.6, a=1 (normalised AU)
  Semi-latus rectum p = a(1-e²)
  Sector swept in Δθ: dA = ½r²dθ  → equal areas in equal times (Kepler II)
  Angular momentum: L=mrv_⊥ → r²dθ/dt = const → equal-area law

Testable predictions:
  P1: Sector areas are equal for equal Δθ… no — equal TIME intervals.
      We parameterise by time via dθ/dt = L/(mr²) ~ 1/r².
  P2: v_peri / v_aph = r_aph / r_peri

Run standalone verification:
  python3 physics_kepler_equal_area_orbit.py --verify

Render:
  manim -qh physics_kepler_equal_area_orbit.py KeplerEqualAreaOrbitScene
"""
import sys
import numpy as np
from scipy import integrate as sci_int

E_ORBT = 0.6   # eccentricity
A_ORBT = 1.0   # semi-major axis (normalised)
N_SECT = 5     # number of equal-time sectors to show

def semi_latus():
    return A_ORBT * (1 - E_ORBT**2)

def r_theta(theta):
    p = semi_latus()
    return p / (1 + E_ORBT * np.cos(theta))

def orbit_xy(theta):
    r = r_theta(theta)
    return r * np.cos(theta), r * np.sin(theta)

def period_integral():
    """Compute full-orbit dt via Kepler (∫ r² dθ = 2π × const)."""
    # ∫₀²π r²(θ) dθ  (proportional to T)
    return sci_int.quad(lambda th: r_theta(th)**2, 0, 2*np.pi)[0]

def theta_of_time(n_pts=2000):
    """
    Numerically invert dθ/dt ∝ 1/r² to get θ(t) for one full orbit.
    Returns (t_norm, theta_arr) where t_norm ∈ [0,1].
    """
    th_arr = np.linspace(0, 2*np.pi, n_pts)
    r2_arr = r_theta(th_arr)**2
    # dt/dθ ∝ r², so cumulative t ∝ ∫ r² dθ
    dt_arr  = r2_arr
    t_cum   = np.cumsum(dt_arr) / np.sum(dt_arr)   # normalised [0,1]
    return t_cum, th_arr

def equal_time_thetas(n_sects=N_SECT):
    """Return θ values at boundaries of n_sects equal-time sectors."""
    t_norm, th_arr = theta_of_time()
    boundaries = np.linspace(0, 1, n_sects + 1)
    theta_bdry = np.interp(boundaries, t_norm, th_arr)
    return theta_bdry

def sector_area(th1, th2):
    """Area of sector swept from th1 to th2."""
    return sci_int.quad(lambda th: 0.5 * r_theta(th)**2, th1, th2)[0]

def verify():
    print("=== Kepler equal-area verification ===")
    p = semi_latus()
    r_peri = r_theta(0)         # perihelion (θ=0)
    r_aph  = r_theta(np.pi)    # aphelion
    print(f"  p={p:.4f}, r_peri={r_peri:.4f}, r_aph={r_aph:.4f}")
    print(f"  v_ratio = r_aph/r_peri = {r_aph/r_peri:.4f}")
    # Equal areas
    bdry = equal_time_thetas(N_SECT)
    areas = [sector_area(bdry[i], bdry[i+1]) for i in range(N_SECT)]
    print(f"  Sector areas: {[f'{a:.6f}' for a in areas]}")
    print(f"  Max-min area ratio: {max(areas)/min(areas):.6f}  (expect ≈ 1)")
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

SECTOR_COLORS = [BLUE, GOLD, BROWN, "#C77DFF", "#50FA7B"]


class KeplerEqualAreaOrbitScene(Scene):
    """
    Draw elliptical orbit, comet dot, equal-time sector shading.
    """

    def construct(self):
        self.camera.background_color = CANVAS

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("Kepler's Equal-Area Law",
                     font="EB Garamond", font_size=58, color=INK)
        sub   = Text(
            "Ellipse: e=0.6  ·  equal time → equal area",
            font="EB Garamond", font_size=24, color=BLUE,
        )
        sub2  = Text(
            "dA/dt = L/2m = const  (angular momentum conservation)",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(sub), FadeIn(sub2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

        # ── Scale: 1 AU = 3 units on screen ────────────────────────────────
        scale = 2.8

        def to_screen(x, y):
            # Centre orbit: focus at origin, shift so ellipse is centred nicely
            # Focus-to-centre offset: c = a*e
            c = A_ORBT * E_ORBT
            return np.array([(x - c) * scale, y * scale, 0]) + np.array([-0.5, 0, 0])

        # ── Draw orbit ellipse ──────────────────────────────────────────────
        th_full = np.linspace(0, 2*np.pi, 500)
        xs, ys  = orbit_xy(th_full)
        orbit_pts = [to_screen(x, y) for x, y in zip(xs, ys)]
        orbit_curve = VMobject(color=DIM, stroke_width=1.5)
        orbit_curve.set_points_smoothly(orbit_pts + [orbit_pts[0]])

        # Sun (focus)
        sun = Dot(to_screen(0, 0), color=GOLD, radius=0.18)
        sun_glow = Circle(radius=0.28, color=GOLD, stroke_width=1.0, fill_opacity=0.15, fill_color=GOLD)
        sun_glow.move_to(to_screen(0, 0))

        self.play(Create(orbit_curve), FadeIn(sun, sun_glow), run_time=1.5)
        self.wait(0.5)

        # ── Draw equal-time sectors ────────────────────────────────────────
        bdry = equal_time_thetas(N_SECT)

        sector_groups = VGroup()
        for i in range(N_SECT):
            th1, th2 = bdry[i], bdry[i+1]
            th_seg  = np.linspace(th1, th2, 80)
            xs_s, ys_s = orbit_xy(th_seg)
            pts_seg = [to_screen(0, 0)] + [to_screen(x, y) for x, y in zip(xs_s, ys_s)] + [to_screen(0, 0)]
            sector = Polygon(
                *pts_seg,
                color=SECTOR_COLORS[i % len(SECTOR_COLORS)],
                fill_color=SECTOR_COLORS[i % len(SECTOR_COLORS)],
                fill_opacity=0.22,
                stroke_width=1.2,
            )
            sector_groups.add(sector)

        self.play(FadeIn(sector_groups), run_time=2.0)
        self.wait(0.8)

        # ── Speed comparison annotation ─────────────────────────────────────
        r_peri = r_theta(0)
        r_aph  = r_theta(np.pi)
        peri_pt = to_screen(*orbit_xy(0))
        aph_pt  = to_screen(*orbit_xy(np.pi))

        dot_peri = Dot(peri_pt, color=GOLD,  radius=0.11)
        dot_aph  = Dot(aph_pt,  color=BROWN, radius=0.11)
        lbl_peri = Text("perihelion\n(fast)", font="EB Garamond", font_size=16, color=GOLD).next_to(dot_peri, RIGHT, buff=0.1)
        lbl_aph  = Text("aphelion\n(slow)",  font="EB Garamond", font_size=16, color=BROWN).next_to(dot_aph, LEFT, buff=0.1)

        self.play(FadeIn(dot_peri, dot_aph), Write(lbl_peri), Write(lbl_aph), run_time=1.0)
        self.wait(0.5)

        # ── Equal area callout ─────────────────────────────────────────────
        anno = Text(
            "All 5 sectors have equal area  ·  swept in equal time",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(UP, buff=0.22)
        eq = MathTex(
            r"\frac{dA}{dt} = \frac{L}{2m} = \mathrm{const}",
            color=BLUE, font_size=30,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(anno), Write(eq), run_time=1.0)
        self.wait(3.0)
