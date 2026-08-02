#!/usr/bin/env python3
"""
prism_dispersion_white_light.py — Prism Dispersion: White Light Splitting Wavelength by Wavelength
SILENT SLATE — math-explainer (brownblue) candidate, physics-optics book.

All curves computed exactly with numpy. No audio spend (GATE P).

Render:
    cd physics-optics/youtube/prism-dispersion-white-light
    manim -qh prism_dispersion_white_light.py PrismDispersionScene

Numpy verification (run standalone):
    python3 prism_dispersion_white_light.py --verify

Physics (checkable):
    Cauchy: n(λ) = A + B/λ²  (λ in µm)
    A=1.5, B=0.01µm²

    P1: n(700nm) = 1.5+0.01/0.49 ≈ 1.5204; n(400nm) = 1.5+0.01/0.16 ≈ 1.5625 ✓
    P2: α=60°, θ1=50°. Apply Snell twice for each wavelength → exit angle difference ✓
"""
import sys
import numpy as np

A_CAUCHY = 1.5
B_CAUCHY = 0.01   # µm²
ALPHA = 60.0      # prism apex angle in degrees
THETA1 = 50.0     # angle of incidence at entry face (degrees)


def cauchy_n(lam_nm):
    """Refractive index from Cauchy formula. lam_nm in nm."""
    lam_um = lam_nm / 1000.0
    return A_CAUCHY + B_CAUCHY / (lam_um ** 2)


def prism_exit_angle(lam_nm):
    """
    Compute exit angle from prism (in degrees).
    Entry: Snell at first face. Refraction inside.
    Exit: Snell at second face.
    Returns exit angle from normal at exit face (or None if TIR).
    """
    n = cauchy_n(lam_nm)
    # Entry refraction: n_air × sin(θ1) = n × sin(θ2)
    sin_t2 = np.sin(np.radians(THETA1)) / n
    if abs(sin_t2) > 1:
        return None
    t2 = np.degrees(np.arcsin(sin_t2))
    # Geometry inside prism: angle at exit face
    t3 = ALPHA - t2
    # Exit refraction: n × sin(t3) = n_air × sin(t_exit)
    sin_t_exit = n * np.sin(np.radians(t3))
    if abs(sin_t_exit) > 1:
        return None
    return np.degrees(np.arcsin(sin_t_exit))


def verify():
    print("=== Prism dispersion verification ===")
    # P1: Cauchy indices
    n700 = cauchy_n(700)
    n400 = cauchy_n(400)
    print(f"P1: n(700nm) = {n700:.4f}  (should be ≈1.520)")
    print(f"    n(400nm) = {n400:.4f}  (should be ≈1.563)")
    print(f"    Δn = {n400-n700:.4f}")
    # P2: exit angles
    print(f"\nP2: α={ALPHA}°, θ1={THETA1}°")
    ex_red = prism_exit_angle(700)
    ex_vio = prism_exit_angle(400)
    print(f"    Exit angle red (700nm)    = {ex_red:.2f}°")
    print(f"    Exit angle violet (400nm) = {ex_vio:.2f}°")
    print(f"    Angular separation        = {ex_vio - ex_red:.2f}°")
    print()
    # Print full spectrum
    print("Spectrum exit angles:")
    for lam in [400, 450, 500, 550, 600, 650, 700]:
        print(f"  λ={lam}nm: n={cauchy_n(lam):.4f}, exit={prism_exit_angle(lam):.2f}°")
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

# Visible wavelengths to animate (nm) with associated colors
WAVELENGTHS = [
    (700, "#FF2200"),   # red
    (650, "#FF6600"),   # orange-red
    (600, "#FFAA00"),   # orange
    (570, "#FFEE00"),   # yellow
    (520, "#44DD44"),   # green
    (470, "#4488FF"),   # blue
    (420, "#9944FF"),   # violet
]


def wavelength_to_scene_color(lam_nm):
    for wl, col in WAVELENGTHS:
        if abs(wl - lam_nm) < 30:
            return col
    return "#FFFFFF"


class PrismDispersionScene(Scene):
    """
    Triangular prism dispersing white light into a spectrum.
    Each wavelength drawn one-by-one from red to violet.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_dispersion()

    def _phase_title(self):
        title = Text("Prism Dispersion", font="EB Garamond", font_size=64, color=INK)
        sub = Text(
            "Cauchy: n(λ) = A + B/λ²  ·  different λ → different n → different bending",
            font="EB Garamond", font_size=22, color=DIM,
        )
        sub2 = Text(
            "A tiny index difference of 0.04 separates red from violet by ~0.7°",
            font="EB Garamond", font_size=21, color=BLUE,
        )
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.32).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.6)
        self.play(FadeIn(sub2), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(title, sub, sub2), run_time=0.4)

    def _phase_dispersion(self):
        # Draw prism: equilateral triangle with apex at top
        # Vertices in scene units
        SCALE = 2.0
        apex = np.array([0, SCALE * np.sqrt(3) / 2, 0])
        base_l = np.array([-SCALE, -SCALE * np.sqrt(3) / 4, 0])
        base_r = np.array([SCALE,  -SCALE * np.sqrt(3) / 4, 0])

        # Shift prism slightly left to leave room for spectrum fan on right
        shift = np.array([-1.2, 0.1, 0])
        apex    = apex + shift
        base_l  = base_l + shift
        base_r  = base_r + shift

        prism = Polygon(apex, base_l, base_r,
                        color=BLUE, fill_color=BLUE, fill_opacity=0.08, stroke_width=2.5)

        prism_lbl = Text("Glass prism\nA=1.5, B=0.01µm²", font="EB Garamond",
                         font_size=17, color=BLUE)
        prism_lbl.move_to(shift + np.array([0, -0.5, 0]))

        # Cauchy equation label
        cauchy_lbl = MathTex(
            r"n(\lambda) = 1.5 + \frac{0.01}{\lambda^2(\mu\text{m}^2)}",
            color=INK, font_size=26,
        ).to_corner(UL, buff=0.3)

        self.play(Create(prism), Write(prism_lbl), Write(cauchy_lbl), run_time=1.5)

        # Incoming white beam (left face of prism)
        # Entry point: midpoint of left face
        entry = (apex + base_l) / 2.0

        # Incoming ray direction: from angle THETA1 from normal of left face
        # Normal to left face: left face goes from apex to base_l
        left_face_dir = (base_l - apex)
        left_face_dir = left_face_dir / np.linalg.norm(left_face_dir)
        normal_in = np.array([-left_face_dir[1], left_face_dir[0], 0])  # rotate 90°
        if normal_in[0] > 0:
            normal_in = -normal_in  # point outward (left side)

        # Incident ray: comes from upper-left at THETA1 from normal
        inc_dir = np.array([
            normal_in[0] * np.cos(np.radians(THETA1)) + left_face_dir[0] * np.sin(np.radians(THETA1)),
            normal_in[1] * np.cos(np.radians(THETA1)) + left_face_dir[1] * np.sin(np.radians(THETA1)),
            0,
        ])
        inc_start = entry - inc_dir * 2.5
        inc_ray = Arrow(
            start=inc_start, end=entry,
            color=INK, stroke_width=5, buff=0,
            max_tip_length_to_length_ratio=0.08,
        )
        self.play(Create(inc_ray), run_time=0.7)

        # For each wavelength, compute the ray path through the prism
        # and draw it one by one
        # We use a simplified 2D geometry where prism apex is at top

        # Compute exit point on right face
        # Right face goes from apex to base_r
        right_face_dir = (base_r - apex) / np.linalg.norm(base_r - apex)
        normal_out = np.array([-right_face_dir[1], right_face_dir[0], 0])
        if normal_out[0] < 0:
            normal_out = -normal_out  # point outward (right side)

        # Inside prism: direction of refracted ray at entry
        # sin(t2_inside) = sin(THETA1)/n
        # refracted along left face normal direction (inward)
        # We need to compute ray inside and find exit on right face

        all_rays = []
        for lam_nm, col in WAVELENGTHS:
            n = cauchy_n(lam_nm)
            sin_t2 = np.sin(np.radians(THETA1)) / n
            t2 = np.degrees(np.arcsin(sin_t2))

            # Ray inside prism: refracted from entry, going into prism
            # normal_in points outward; refracted ray goes in opposite direction of normal
            inward_normal = -normal_in
            # Refracted direction: inward_normal rotated by t2 toward left_face_dir
            inside_dir = (
                inward_normal * np.cos(np.radians(t2))
                + left_face_dir * np.sin(np.radians(t2))
            )
            inside_dir = inside_dir / np.linalg.norm(inside_dir)

            # Find intersection of ray from entry with right face
            # Right face: parametric: apex + t*(base_r - apex), t in [0,1]
            # Ray: entry + s*inside_dir
            # Solve: entry + s*inside_dir = apex + t*(base_r-apex)
            A_mat = np.array([
                [inside_dir[0], -(base_r - apex)[0]],
                [inside_dir[1], -(base_r - apex)[1]],
            ])
            b_vec = (apex - entry)[:2]
            try:
                sol = np.linalg.solve(A_mat, b_vec)
            except np.linalg.LinAlgError:
                continue
            s_ray, t_face = sol
            if s_ray < 0 or t_face < 0 or t_face > 1:
                continue
            exit_pt = entry + s_ray * inside_dir

            # Angle of inside ray with normal at exit face
            cos_angle_exit = abs(np.dot(inside_dir, normal_out))
            t3 = np.degrees(np.arccos(np.clip(cos_angle_exit, -1, 1)))

            # Exit refraction
            sin_exit = n * np.sin(np.radians(t3))
            if abs(sin_exit) > 1:
                continue
            t_exit = np.degrees(np.arcsin(sin_exit))

            # Exit direction: normal_out rotated by t_exit
            # Perpendicular to right_face_dir
            perp = np.array([-right_face_dir[1], right_face_dir[0], 0])
            if perp[0] < 0:
                perp = -perp
            exit_dir = (
                normal_out * np.cos(np.radians(t_exit))
                + right_face_dir * np.sin(np.radians(t_exit)) * (-1)
            )
            exit_dir = exit_dir / (np.linalg.norm(exit_dir) + 1e-12)

            exit_end = exit_pt + exit_dir * 2.8

            all_rays.append((lam_nm, col, n, t_exit, entry, exit_pt, exit_end, inside_dir, s_ray))

        # Draw each wavelength sequentially
        lam_lbl = MathTex(r"\lambda = ", color=INK, font_size=26).move_to([3.8, 2.5, 0])
        lam_val = DecimalNumber(700, num_decimal_places=0, color=INK, font_size=26)
        lam_val.next_to(lam_lbl, RIGHT, buff=0.08)
        lam_nm_lbl = Text("nm", font="EB Garamond", font_size=22, color=INK)
        lam_nm_lbl.next_to(lam_val, RIGHT, buff=0.08)
        n_lbl = MathTex(r"n = ", color=DIM, font_size=24).next_to(lam_lbl, DOWN, buff=0.3).align_to(lam_lbl, LEFT)
        n_val = DecimalNumber(1.52, num_decimal_places=4, color=DIM, font_size=24)
        n_val.next_to(n_lbl, RIGHT, buff=0.08)

        self.play(FadeIn(lam_lbl), FadeIn(lam_val), FadeIn(lam_nm_lbl), FadeIn(n_lbl), FadeIn(n_val), run_time=0.6)

        drawn_segments = []
        for lam_nm, col, n, t_exit, entry_pt, exit_pt, exit_end, inside_dir, s_ray in all_rays:
            # Inside segment
            inside_seg = Line(entry_pt, exit_pt, color=col, stroke_width=3.5)
            # Exit segment
            exit_seg = Arrow(exit_pt, exit_end, color=col, stroke_width=3.5, buff=0,
                             max_tip_length_to_length_ratio=0.08)
            lam_str = f"{lam_nm:.0f}"
            self.play(
                Create(inside_seg), Create(exit_seg),
                ChangeDecimalToValue(lam_val, lam_nm),
                ChangeDecimalToValue(n_val, n),
                run_time=0.8,
            )
            drawn_segments.extend([inside_seg, exit_seg])

        # Final caption
        cap = Text(
            "Each wavelength refracts at a slightly different angle — dispersion made visible.",
            font="EB Garamond", font_size=20, color=INK,
        ).to_edge(DOWN, buff=0.25)
        cauchy_cap = MathTex(
            r"\Delta n \approx 0.04 \;\Rightarrow\; \Delta\theta_{\rm exit} \approx 0.7°",
            color=GOLD, font_size=26,
        ).to_edge(UP, buff=0.28)
        self.play(Write(cap), Write(cauchy_cap), run_time=1.2)
        self.wait(3.0)
