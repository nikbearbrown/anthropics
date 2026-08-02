#!/usr/bin/env python3
"""
qm_bohr_sommerfeld.py — Bohr-Sommerfeld: Phase-Space Ellipse Quantization ∮p dx = (n+½)h
SILENT SLATE — math-explainer (brownblue) candidate, physics-plus-one-quantum-mechanics book.

Render:
    cd physics-plus-one-quantum-mechanics/youtube/qm-bohr-sommerfeld
    manim -qh qm_bohr_sommerfeld.py BohrSommerfeldScene

Physics:
    ∮ p dx = (n + 1/2)h  (WKB quantization)
    Harmonic oscillator: phase-space ellipse area = (n+½)h
    n=0: area = h/2 = 3.313e-34 J·s
    n=1: area = 3h/2
    Area between consecutive levels: always h (one Planck unit)
"""
import sys
import numpy as np

H_PLANCK = 6.626e-34    # J·s
HBAR     = H_PLANCK / (2 * np.pi)
OMEGA    = 2 * np.pi * 1e12  # rad/s
MASS     = 1.67e-27      # kg


def ellipse_area(n, omega=OMEGA, mass=MASS):
    """Phase-space ellipse area = (n+1/2)h."""
    return (n + 0.5) * H_PLANCK


def ellipse_axes(n, omega=OMEGA, mass=MASS):
    """Semi-axes: x_max = sqrt(2E/mω²), p_max = sqrt(2mE)."""
    E = (n + 0.5) * HBAR * omega
    x_max = np.sqrt(2 * E / (mass * omega**2))
    p_max = np.sqrt(2 * mass * E)
    return x_max, p_max


if __name__ == "__main__":
    print("=== Bohr-Sommerfeld Verification ===")
    # P1: n=0, area = h/2
    a0 = ellipse_area(0)
    print(f"P1: n=0 area = {a0:.4e} J·s  (expect h/2 = {H_PLANCK/2:.4e})")
    assert abs(a0 - H_PLANCK / 2) < 1e-38, "P1 FAIL"
    # P2: spacing = h
    for n in range(4):
        delta = ellipse_area(n+1) - ellipse_area(n)
        print(f"  n={n}→{n+1}: Δarea = {delta:.4e}  (expect h={H_PLANCK:.4e})")
        assert abs(delta - H_PLANCK) < 1e-38, f"P2 FAIL at n={n}"
    # Verify ellipse area = π x_max p_max
    for n in range(4):
        x_max, p_max = ellipse_axes(n)
        area_geom = np.pi * x_max * p_max
        area_quant = ellipse_area(n)
        print(f"  n={n}: π*x*p = {area_geom:.4e}, (n+½)h = {area_quant:.4e}")
        assert abs(area_geom - area_quant) / area_quant < 1e-10, f"Geometry FAIL n={n}"
    print("=== PASSED ===")
    sys.exit(0)

# ─── Manim scene ─────────────────────────────────────────────────────────────
from manim import *  # noqa: E402

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"


class BohrSommerfeldScene(Scene):
    """Nested phase-space ellipses with quantization condition."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._phase_title()
        ax = self._phase_axes()
        self._phase_ellipses(ax)
        self._phase_quantization()

    def _phase_title(self):
        title = Text("Bohr-Sommerfeld Quantization", font="EB Garamond",
                     font_size=48, color=INK)
        sub = MathTex(r"\oint p\,dx=(n+\tfrac{1}{2})h\quad n=0,1,2,\ldots",
                      color=BLUE, font_size=30)
        sub2 = Text("Phase-space area is quantized in units of Planck's constant",
                    font="EB Garamond", font_size=21, color=DIM)
        VGroup(title, sub, sub2).arrange(DOWN, buff=0.3).center()
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub), run_time=0.7)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(title, sub, sub2), run_time=0.5)

    def _phase_axes(self):
        ax = Axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=8.0,
            y_length=8.0,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        )
        x_lbl = MathTex(r"x\;(x_{\rm max}\text{ units})", color=INK, font_size=22).next_to(
            ax.x_axis.get_end(), RIGHT, buff=0.08)
        y_lbl = MathTex(r"p\;(p_{\rm max}\text{ units})", color=INK, font_size=22).next_to(
            ax.y_axis.get_end(), UP, buff=0.08)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl), run_time=1.5)
        return ax

    def _phase_ellipses(self, ax):
        colors_n = [BLUE, GOLD, BROWN, DIM]
        n_max = 4

        # In normalized units, ellipse n has axes sqrt(2n+1)
        ellipse_mobs = []
        for n in range(n_max):
            r = np.sqrt(2 * n + 1)   # normalized semi-axis (same in x and p in normalized units)
            t = np.linspace(0, 2 * np.pi, 300)
            x = r * np.cos(t)
            p = r * np.sin(t)
            pts = [ax.c2p(xi, pi) for xi, pi in zip(x, p)]
            ellipse = VMobject(color=colors_n[n], stroke_width=2.5)
            ellipse.set_points_smoothly(pts)

            area_lbl = MathTex(rf"n={n}:\;(n+\tfrac{{1}}{{2}})h={(2*n+1)/2:.1f}h",
                               color=colors_n[n], font_size=18
                               ).move_to(ax.c2p(r * 0.7, r * 0.5))
            self.play(Create(ellipse), Write(area_lbl), run_time=0.8)
            ellipse_mobs.append((ellipse, area_lbl))

        # Shade annular ring between n=0 and n=1 (area = h)
        r0 = np.sqrt(1)
        r1 = np.sqrt(3)
        t  = np.linspace(0, 2 * np.pi, 200)
        inner = [ax.c2p(r0 * np.cos(t_), r0 * np.sin(t_)) for t_ in t]
        outer = [ax.c2p(r1 * np.cos(t_), r1 * np.sin(t_)) for t_ in reversed(t)]
        ring  = Polygon(*(inner + outer),
                        color=GOLD, fill_color=GOLD, fill_opacity=0.25, stroke_width=0)
        ring_lbl = MathTex(r"\Delta\text{area}=h", color=GOLD, font_size=22
                           ).move_to(ax.c2p(1.6, 0))

        self.play(FadeIn(ring), Write(ring_lbl), run_time=1.0)
        self.wait(2.5)

        # Animate a classical trajectory dot on n=2 ellipse
        r2 = np.sqrt(5)
        traj_dot = Dot(ax.c2p(r2, 0), color=INK, radius=0.12)
        self.add(traj_dot)
        steps = 60
        for i in range(1, steps + 1):
            angle = i * 2 * np.pi / steps
            self.play(traj_dot.animate.move_to(
                ax.c2p(r2 * np.cos(angle), r2 * np.sin(angle))),
                run_time=0.05, rate_func=linear)

        self.wait(1.5)
        for e, l in ellipse_mobs:
            self.remove(e, l)
        self.remove(ring, ring_lbl, traj_dot)

    def _phase_quantization(self):
        rows = [
            MathTex(r"\oint p\,dx=\pi x_{\rm max}p_{\rm max}=(n+\tfrac{1}{2})h",
                    color=BLUE, font_size=30),
            MathTex(r"E_n=\tfrac{1}{2}m\omega^2 x_{\rm max}^2=(n+\tfrac{1}{2})\hbar\omega",
                    color=GOLD, font_size=28),
            MathTex(r"\text{Old Bohr: }nh\quad\text{WKB correction: }+\tfrac{1}{2}h\;\text{(Maslov index)}",
                    color=BROWN, font_size=24),
            MathTex(r"\text{Area between levels} = h\;\text{exactly}",
                    color=INK, font_size=28),
        ]
        VGroup(*rows).arrange(DOWN, buff=0.45).center()
        hdr = Text("Quantization = counting phase-space area in units of h",
                   font="EB Garamond", font_size=22, color=INK).to_edge(UP, buff=0.22)
        self.play(Write(hdr), run_time=0.5)
        for r in rows:
            self.play(Write(r), run_time=1.0)
            self.wait(0.5)
        self.wait(2.0)
        final = Text("Bohr missed the ½ — WKB gets it from the two classical turning points",
                     font="EB Garamond", font_size=22, color=GOLD).to_edge(DOWN, buff=0.28)
        self.play(Write(final), run_time=1.2)
        self.wait(2.5)
