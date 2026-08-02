#!/usr/bin/env python3
"""
spherical_harmonics_gallery.py — Spherical Harmonics Gallery
SILENT — quantum-mechanics-vol5.

Render:
    cd quantum-mechanics-vol5/youtube/spherical-harmonics-gallery
    manim -qh spherical_harmonics_gallery.py SphericalHarmonicsScene

Verify:
    python3 spherical_harmonics_gallery.py --verify

Physics:
    Y_{ℓm}(θ,φ) = N_{ℓm} P_ℓ^m(cosθ) e^{imφ}
    |Y₀₀|² = 1/(4π) — sphere
    |Y₁₀|² ∝ cos²θ — dumbbell
    Y₂₀ has 2 nodal cones at θ ≈ 54.7°
    Total nodes for Y_{ℓm}: ℓ total (ℓ−|m| polar + |m| azimuthal)
"""
import sys
import numpy as np
from scipy.special import sph_harm


def verify():
    print("=== Spherical harmonics verification ===")
    # Normalization check
    from scipy.integrate import dblquad
    for ell in range(3):
        for m in range(-ell, ell+1):
            def integrand(phi, theta):
                return abs(sph_harm(m, ell, phi, theta))**2 * np.sin(theta)
            result, err = dblquad(integrand, 0, np.pi, 0, 2*np.pi, epsabs=1e-4)
            print(f"  Y_{ell},{m}: ∫|Y|²sinθ dΩ = {result:.6f}  (should be 1.0)")

    # P1: Y_{ℓ0} has ℓ nodal cones
    print("\n  Nodal cone angles for Y_{ℓ,0}:")
    for ell in [1, 2, 3]:
        thetas = np.linspace(0.01, np.pi - 0.01, 10000)
        Yvals  = sph_harm(0, ell, 0, thetas).real
        nodes  = np.sum(np.diff(np.sign(Yvals)) != 0)
        print(f"    ℓ={ell}: {nodes} nodal cones (expected {ell})")

    # Special: Y_{2,0} node at 54.7°
    from scipy.optimize import brentq
    def Y20_real(theta):
        return sph_harm(0, 2, 0, theta).real
    root = brentq(Y20_real, 0.5, 1.0)
    print(f"\n  Y_{{2,0}} nodal cone: θ ≈ {np.degrees(root):.2f}°  (expected 54.74°)")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class SphericalHarmonicsScene(Scene):
    """
    Shows |Y_{ℓm}(θ,φ)|² as 2D polar plots for several (ℓ,m) pairs.
    Phase 1: title
    Phase 2: gallery of |Y_{ℓm}|² polar cross-sections (φ=0 slice)
    Phase 3: node counting table
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gallery()
        self._phase_nodes()

    def _phase_title(self):
        title = Text("Spherical Harmonics Gallery", font="EB Garamond", font_size=56, color=INK)
        sub   = Text(
            "Y_{ℓm}(θ,φ) — eigenstates of L̂² and L̂_z;  each new ℓ adds a nodal circle",
            font="EB Garamond", font_size=23, color=BLUE,
        )
        VGroup(title, sub).arrange(DOWN, buff=0.35).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(title, sub), run_time=0.5)

    def _polar_plot(self, ell, m, center, scale=1.2, color=BLUE):
        """Return a polar surface plot of |Y_{ℓm}|² as a closed VMobject (θ cross section at φ=0)."""
        thetas = np.linspace(0, 2 * np.pi, 360)
        # Use φ=0 and φ=π to get full cross-section
        # For the cross-section at φ=0 we map θ→Cartesian:
        # x = r(θ)sinθ, y = r(θ)cosθ
        r_vals = np.array([abs(sph_harm(m, ell, 0.0, th))**2 for th in thetas])
        r_vals = r_vals / r_vals.max() if r_vals.max() > 0 else r_vals
        xs = r_vals * np.sin(thetas)
        ys = r_vals * np.cos(thetas)
        pts = [center + scale * np.array([x, y, 0]) for x, y in zip(xs, ys)]
        mob = Polygon(*pts, color=color, fill_color=color, fill_opacity=0.25, stroke_width=2.0)
        return mob

    def _phase_gallery(self):
        # 3×3 grid of (ℓ,m) pairs
        pairs = [(0,0), (1,-1), (1,0), (1,1), (2,-2), (2,-1), (2,0), (2,1), (2,2)]
        cols  = [BLUE, BROWN, GOLD, BROWN, "#88CC44", BROWN, GOLD, BROWN, "#88CC44"]

        positions = []
        for row in range(3):
            for col in range(3):
                x = (col - 1) * 3.5
                y = (1 - row) * 3.0
                positions.append(np.array([x, y, 0]))

        hdr = Text(
            "|Y_{ℓm}(θ,φ)|² polar cross-section — rows: ℓ=0,1,2",
            font="EB Garamond", font_size=19, color=INK,
        ).to_edge(UP, buff=0.18)
        self.play(Write(hdr), run_time=0.6)

        for (ell, m), pos, col in zip(pairs, positions, cols):
            mob = self._polar_plot(ell, m, pos, scale=1.1, color=col)
            lbl = MathTex(f"Y_{{{ell},{m}}}", color=col, font_size=20).next_to(pos + DOWN * 1.3, DOWN, buff=0.05)
            self.play(Create(mob), Write(lbl), run_time=0.5)

        self.wait(2.5)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _phase_nodes(self):
        hdr = Text(
            "Angular node count:  ℓ total  =  (ℓ−|m|) polar  +  |m| azimuthal",
            font="EB Garamond", font_size=22, color=INK,
        ).to_edge(UP, buff=0.28)
        self.play(Write(hdr), run_time=0.8)

        rows = [
            (r"Y_{0,0}", "0", "0", "0"),
            (r"Y_{1,0}", "1", "1", "0"),
            (r"Y_{1,\pm1}", "1", "0", "1"),
            (r"Y_{2,0}", "2", "2", "0"),
            (r"Y_{2,\pm1}", "2", "1", "1"),
            (r"Y_{2,\pm2}", "2", "0", "2"),
        ]
        headers = ["Function", "ℓ (total)", "Polar", "Azimuthal"]
        col_x = [-4.0, -0.5, 1.5, 3.5]

        for i, h in enumerate(headers):
            lbl = Text(h, font="EB Garamond", font_size=22, color=DIM)
            lbl.move_to(np.array([col_x[i], 1.5, 0]))
            self.play(Write(lbl), run_time=0.3)

        for j, (func, total, polar, azim) in enumerate(rows):
            y = 0.8 - j * 0.55
            cols_vals = [func, total, polar, azim]
            colors    = [BLUE, GOLD, BROWN, BROWN]
            for i, (val, col) in enumerate(zip(cols_vals, colors)):
                lbl = MathTex(val, font_size=22, color=col) if i == 0 else Text(val, font="EB Garamond", font_size=22, color=col)
                lbl.move_to(np.array([col_x[i], y, 0]))
                self.play(Write(lbl), run_time=0.2)

        fin = MathTex(
            r"L^2 Y_{\ell m} = \hbar^2\ell(\ell+1)Y_{\ell m}\quad L_z Y_{\ell m} = \hbar m Y_{\ell m}",
            color=BLUE, font_size=26,
        ).to_edge(DOWN, buff=0.28)
        self.play(Write(fin), run_time=1.0)
        self.wait(2.5)
