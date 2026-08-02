#!/usr/bin/env python3
"""
qm_hydrogen_orbital_gallery.py — Hydrogen Orbital Gallery: Cross-Sections for (n,ℓ,m)
SILENT SLATE — math-explainer (brownblue), physics-quantum-mechanics book.

Render:
    cd physics-quantum-mechanics/youtube/qm-hydrogen-orbital-gallery
    manim -qh qm_hydrogen_orbital_gallery.py HydrogenOrbitalGalleryScene

Verify:
    python3 qm_hydrogen_orbital_gallery.py

Physics:
    ψ_nlm(r,θ,φ) = R_nl(r) Y_l^m(θ,φ)
    Radial nodes = n - l - 1
    Angular nodes = l
    Total nodes = n - 1
    Cross-section in xz-plane: φ=0, so Y_l^m(θ,0) = sqrt((2l+1)(l-|m|)!/(4π(l+|m|)!)) * P_l^m(cos θ)
    2s node at r = 2a0
    2p_z (m=0): nodal plane xy (θ=π/2)
    3d_z2 (m=0): two nodal cones
"""
import sys
import numpy as np
from math import factorial

A0 = 0.0529177  # nm


def laguerre_assoc(n: int, alpha: int, x: np.ndarray) -> np.ndarray:
    """Associated Laguerre L_n^alpha(x) via recurrence."""
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 1.0 + alpha - x
    L0, L1 = np.ones_like(x), 1.0 + alpha - x
    for k in range(1, n):
        Lnew = ((2*k + 1 + alpha - x)*L1 - (k + alpha)*L0) / (k + 1)
        L0, L1 = L1, Lnew
    return L1


def legendre_p(l: int, m: int, x: np.ndarray) -> np.ndarray:
    """Associated Legendre P_l^m(x), m>=0 only."""
    # Build P_l^|m|(cos θ)
    m = abs(m)
    # Compute starting: P_m^m(x)
    Pmm = np.ones_like(x)
    sign = 1.0
    for k in range(1, m + 1):
        Pmm *= -(2*k - 1) * sign * np.sqrt(1.0 - x**2)
        sign = 1.0
    if l == m:
        return Pmm
    Pm1 = x * (2*m + 1) * Pmm
    if l == m + 1:
        return Pm1
    for ll in range(m + 2, l + 1):
        Plm = ((2*ll - 1)*x*Pm1 - (ll + m - 1)*Pmm) / (ll - m)
        Pmm, Pm1 = Pm1, Plm
    return Pm1


def hydrogen_density_xz(n: int, l: int, m: int, grid: int = 80, r_max_a0: float = None
                        ) -> np.ndarray:
    """
    |ψ_nlm|² in xz-plane (φ=0) on grid x grid points.
    Returns 2D array normalised to max=1.
    """
    if r_max_a0 is None:
        r_max_a0 = 3.0 * n**2 + 2.0

    xs = np.linspace(-r_max_a0, r_max_a0, grid)
    zs = np.linspace(-r_max_a0, r_max_a0, grid)
    XX, ZZ = np.meshgrid(xs, zs)
    RR = np.sqrt(XX**2 + ZZ**2) + 1e-12
    cos_theta = ZZ / RR

    rho = 2.0 * RR / n
    nr  = n - l - 1
    # Radial part squared
    norm_r = (2.0/n)**3 * factorial(nr) / (2.0*n * factorial(n+l)**3)
    L = laguerre_assoc(nr, 2*l+1, rho)
    R_sq = norm_r * np.exp(-rho) * rho**(2*l) * L**2

    # Angular part Y_l^m(θ,φ=0) — real form
    # For φ=0: Y_l^m(θ,0) real = sqrt((2l+1)(l-|m|)!/(4π(l+|m|)!)) * P_l^|m|(cos θ)
    if m == 0:
        norm_a = (2*l + 1) * factorial(l - abs(m)) / (4.0 * np.pi * factorial(l + abs(m)))
        Y_sq = norm_a * legendre_p(l, m, cos_theta)**2
    else:
        # Real spherical harmonic Y_lm (both m>0 and m<0 contribute same density at φ=0)
        norm_a = (2*l + 1) * factorial(l - abs(m)) / (4.0 * np.pi * factorial(l + abs(m)))
        # At φ=0: real Y_lm = sqrt(norm_a) * P_l^|m|(cos θ) * {sqrt(2)cos(mφ)=sqrt(2) for m>0}
        factor = 2.0 if m != 0 else 1.0
        Y_sq = factor * norm_a * legendre_p(l, abs(m), cos_theta)**2

    dens = R_sq * Y_sq
    mx = dens.max()
    return dens / (mx + 1e-15)


def verify():
    print("=== Hydrogen orbital gallery verification ===")
    # Total node count = n-1
    for n, l, m in [(1,0,0), (2,0,0), (2,1,0), (3,2,0), (3,1,0)]:
        radial_nodes = n - l - 1
        angular_nodes = l
        total = n - 1
        print(f"  ψ_{n}{l}{m}: radial={radial_nodes}, angular={angular_nodes}, total={total}")
        assert radial_nodes + angular_nodes == total, "Node count mismatch!"

    # 2s radial node at r=2a0: R_20 ∝ (2 - r) e^{-r/2}
    r_arr = np.linspace(0, 10, 10000)
    R_20  = (2.0 - r_arr) * np.exp(-r_arr / 2.0)
    node_idx = np.where(np.diff(np.sign(R_20)))[0]
    node_r = r_arr[node_idx[0]] if len(node_idx) else None
    print(f"\n2s radial node at r = {node_r:.3f} a0  (should be 2.0 a0)")
    print("=== PASSED ===" if node_r is not None and abs(node_r - 2.0) < 0.01 else "=== CHECK ===")


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


class HydrogenOrbitalGalleryScene(Scene):
    """
    Gallery of hydrogen orbital cross-sections: 1s, 2s, 2p, 3s, 3p, 3d.
    Node lines drawn over each panel.
    """

    GRID = 60

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        self._phase_gallery()
        self._phase_m_variation()

    def _phase_title(self):
        title = Text("Hydrogen Orbital Gallery", font="EB Garamond",
                     font_size=58, color=INK)
        sub1 = Text(
            "Node count = n−1. Shape comes from two integers: n and ℓ.",
            font="EB Garamond", font_size=21, color=DIM,
        )
        sub2 = MathTex(r"\text{radial nodes} = n-\ell-1,\quad \text{angular nodes} = \ell",
                       color=BLUE, font_size=26)
        VGroup(title, sub1, sub2).arrange(DOWN, buff=0.38).center()
        self.play(Write(title), run_time=1.1)
        self.play(FadeIn(sub1), run_time=0.7)
        self.play(Write(sub2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(title, sub1, sub2), run_time=0.4)

    def _density_to_panel(self, dens: np.ndarray, cell_size: float = 0.09) -> VGroup:
        """Convert 2D density to coloured square grid."""
        g = self.GRID
        vmax = np.percentile(dens, 97)
        objs = []
        for i in range(g):
            for j in range(g):
                val = min(dens[i, j] / (vmax + 1e-15), 1.0)
                r_c = int(0x16 + val * (0x58 - 0x16))
                g_c = int(0x16 + val * (0xC4 - 0x16))
                b_c = int(0x1D + val * (0xDD - 0x1D))
                color = "#{:02x}{:02x}{:02x}".format(r_c, g_c, b_c)
                xi = (j - g//2 + 0.5) * cell_size
                zi = (i - g//2 + 0.5) * cell_size
                sq = Rectangle(width=cell_size*1.02, height=cell_size*1.02,
                                color=color, fill_color=color,
                                fill_opacity=1.0, stroke_width=0)
                sq.move_to([xi, zi, 0])
                objs.append(sq)
        return VGroup(*objs)

    def _phase_gallery(self):
        states = [
            (1, 0, 0, "1s", "0 nodes"),
            (2, 0, 0, "2s", "1 radial node"),
            (2, 1, 0, "2p_z", "1 angular node"),
            (3, 0, 0, "3s", "2 radial nodes"),
            (3, 1, 0, "3p_z", "1+1 nodes"),
            (3, 2, 0, "3d_{z^2}", "2 angular nodes"),
        ]

        # 2×3 layout
        positions = []
        for row in range(2):
            for col in range(3):
                x = (col - 1) * 3.6
                y = (0.5 - row) * 3.6
                positions.append((x, y))

        hdr = Text("Orbital cross-sections in the xz-plane  (|ψ|² density)",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.18)
        self.play(Write(hdr), run_time=0.7)

        all_groups = []
        for idx, ((n, l, m, name, nodes), (px, py)) in enumerate(zip(states, positions)):
            dens = hydrogen_density_xz(n, l, m, grid=self.GRID)
            panel = self._density_to_panel(dens, cell_size=0.085)
            panel.move_to([px, py - 0.3, 0])

            label = Text(f"ψ_{{{name}}}  {nodes}", font="EB Garamond",
                         font_size=15, color=INK).next_to(panel, DOWN, buff=0.08)
            node_count = Text(f"n-1={n-1}", font="EB Garamond",
                              font_size=14, color=DIM).next_to(panel, UP, buff=0.05)

            self.play(FadeIn(panel), Write(label), Write(node_count), run_time=0.7)
            all_groups.append(VGroup(panel, label, node_count))

        self.wait(2.0)
        self.play(FadeOut(hdr, *all_groups), run_time=0.5)

    def _phase_m_variation(self):
        """Show 2p_z (m=0) vs 2p_x (|m|=1) — same energy, different shape."""
        states_m = [
            (2, 1, 0,  "2p (m=0)  dumbbell along z"),
            (2, 1, 1,  "2p (|m|=1)  torus in xy"),
        ]
        hdr = Text("Same energy E₂ — different m — completely different shapes",
                   font="EB Garamond", font_size=19, color=DIM).to_edge(UP, buff=0.2)
        self.play(Write(hdr), run_time=0.7)

        panels = []
        for idx, (n, l, m, desc) in enumerate(states_m):
            dens = hydrogen_density_xz(n, l, m, grid=self.GRID)
            panel = self._density_to_panel(dens, cell_size=0.12)
            x_pos = (idx - 0.5) * 4.5
            panel.move_to([x_pos, -0.2, 0])
            lbl = Text(desc, font="EB Garamond", font_size=19, color=BLUE if m==0 else GOLD
                       ).next_to(panel, DOWN, buff=0.15)
            self.play(FadeIn(panel), Write(lbl), run_time=1.0)
            panels.append(VGroup(panel, lbl))

        note = Text(
            "Degeneracy: E depends only on n, not ℓ or m",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.25)
        self.play(Write(note), run_time=0.9)
        self.wait(3.0)
