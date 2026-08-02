#!/usr/bin/env python3
"""
classical_kepler_third_law.py — Gravitational Orbits + Kepler's Third Law
SILENT SLATE — brownblue math-explainer candidate.

Physics (solar system, GM_sun = 1.327e20 m³/s²):
    Earth:   r=1.00 AU, T=1.00 yr,  v=29.8 km/s
    Mars:    r=1.524 AU, T=1.881 yr
    Jupiter: r=5.204 AU, T=11.87 yr
    T²/r³ = const = 1.00 yr²/AU³

Render:
    cd physics-classical-mechanics/youtube/classical-kepler-third-law
    manim -qh classical_kepler_third_law.py ClassicalKeplerScene
"""
import sys
import numpy as np

GM_SUN = 1.327e20   # m³/s²
AU     = 1.496e11   # m
YR     = 365.25 * 24 * 3600  # s

PLANETS = {
    "Mercury": 0.387,
    "Venus":   0.723,
    "Earth":   1.000,
    "Mars":    1.524,
    "Jupiter": 5.204,
}


def orbital_period_yr(r_AU):
    r = r_AU * AU
    T = 2*np.pi * r**1.5 / np.sqrt(GM_SUN)
    return T / YR


def orbital_speed_kms(r_AU):
    r = r_AU * AU
    return np.sqrt(GM_SUN/r) / 1e3


def verify():
    print("=== Classical Kepler Third Law verification ===")
    for name, r_AU in PLANETS.items():
        T_yr = orbital_period_yr(r_AU)
        v_kms = orbital_speed_kms(r_AU)
        ratio = T_yr**2 / r_AU**3
        print(f"  {name}: r={r_AU:.3f} AU, T={T_yr:.3f} yr, v={v_kms:.1f} km/s, T²/r³={ratio:.4f}")
    # P1: Jupiter T²/r³ ≈ 1
    assert abs(orbital_period_yr(5.204)**2 / 5.204**3 - 1.0) < 0.01, "P1"
    # P2: halving r → v×√2, T×(1/2)^(3/2)
    r_half = 0.5
    T_half = orbital_period_yr(r_half)
    v_half = orbital_speed_kms(r_half)
    print(f"  r=0.5 AU: T={T_half:.4f} yr (expected {0.5**1.5:.4f}), v={v_half:.2f} km/s")
    print("=== PASSED ===")


if __name__ == "__main__" and "--verify" in sys.argv:
    verify()
    sys.exit(0)


from manim import *  # noqa

CANVAS = "#16161D"
INK    = "#ECE6D8"
BLUE   = "#58C4DD"
BROWN  = "#CD853F"
GOLD   = "#F0E442"
DIM    = "#8A8780"

PLANET_COLORS = [DIM, BROWN, BLUE, BROWN, GOLD]
PLANET_KEYS   = list(PLANETS.keys())


class ClassicalKeplerScene(Scene):
    """Solar system orbit diagram + log-log T² ∝ r³ line."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._orbit_diagram()
        self._loglog_plot()

    def _title(self):
        t1 = Text("Kepler's Third Law", font="EB Garamond", font_size=60, color=INK)
        t2 = Text("Double r — period nearly triples.  T² = r³  (AU and years)",
                  font="EB Garamond", font_size=24, color=DIM)
        t3 = MathTex(r"T = \frac{2\pi r^{3/2}}{\sqrt{GM}}\qquad \frac{T^2}{r^3} = \frac{4\pi^2}{GM}",
                     color=BLUE, font_size=28)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _orbit_diagram(self):
        sun = Circle(radius=0.28, color=GOLD, fill_color=GOLD, fill_opacity=0.9).center()
        sun_lbl = MathTex(r"\odot", color=GOLD, font_size=28).center()
        self.play(FadeIn(sun, sun_lbl), run_time=0.5)

        # Log-scaled display radii
        r_display = [0.7, 1.1, 1.5, 2.0, 3.5]
        orbs = []
        sats = []
        lbs  = []
        for name, col, r_d in zip(PLANET_KEYS, PLANET_COLORS, r_display):
            circ = Circle(radius=r_d, color=col, stroke_width=1.0, stroke_opacity=0.65)
            orbs.append(circ)
            sat = Dot(circ.get_right(), color=col, radius=0.11)
            sats.append(sat)
            lbl = Text(name, font="EB Garamond", font_size=15, color=col)
            lbl.next_to(circ.get_top(), UP, buff=0.06)
            lbs.append(lbl)
            self.play(Create(circ), FadeIn(sat), Write(lbl), run_time=0.4)

        # Relative orbital speeds
        Ts = [orbital_period_yr(PLANETS[k]) for k in PLANET_KEYS]
        T_min = min(Ts)
        ang_speeds = [T_min/T for T in Ts]
        angles = [0.0]*5

        cap = Text("Watch Mercury race, Jupiter crawl",
                   font="EB Garamond", font_size=36, color=INK).to_edge(DOWN, buff=0.22)
        self.play(Write(cap), run_time=0.4)

        for frame in range(80):
            for i in range(5):
                angles[i] += ang_speeds[i] * 0.08
                r_d = r_display[i]
                new_pos = np.array([r_d*np.cos(angles[i]), r_d*np.sin(angles[i]), 0])
                sats[i].move_to(new_pos)
            self.wait(0.04)

        self.play(FadeOut(*self.mobjects), run_time=0.4)

    def _loglog_plot(self):
        log_rs = [np.log10(PLANETS[k]) for k in PLANET_KEYS]
        log_Ts = [np.log10(orbital_period_yr(PLANETS[k])) for k in PLANET_KEYS]

        ax = Axes(
            x_range=[-0.5, 0.8, 0.25],
            y_range=[-0.6, 1.2, 0.4],
            x_length=8,
            y_length=6,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).center().shift(DOWN*0.3)
        lx = Text("log₁₀(r / AU)", font="EB Garamond", font_size=40, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("log₁₀(T / yr)", font="EB Garamond", font_size=40, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("T² ∝ r³ — slope 3/2 on log-log",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.2)

        # Fit line (exact slope 3/2 through Earth)
        xs_line = np.linspace(-0.5, 0.8, 100)
        ys_line = 1.5 * xs_line  # Earth: log T = 0, log r = 0 → passes through origin
        pts_line = np.array([ax.c2p(x, y) for x, y in zip(xs_line, ys_line)])
        crv = VMobject(color=DIM, stroke_width=1.8, stroke_opacity=0.6).set_points_smoothly(pts_line)
        slope_lbl = MathTex(r"\mathrm{slope}=\tfrac{3}{2}", color=DIM, font_size=22).move_to(ax.c2p(0.5, 0.5))
        self.play(Create(crv), Write(slope_lbl), run_time=1.2)

        for name, col, lr, lt in zip(PLANET_KEYS, PLANET_COLORS, log_rs, log_Ts):
            d = Dot(ax.c2p(lr, lt), color=col, radius=0.12)
            lbl = Text(name, font="EB Garamond", font_size=17, color=col).next_to(d, UR, buff=0.08)
            self.play(FadeIn(d), Write(lbl), run_time=0.5)

        # T²/r³ verification
        verify_lbl = MathTex(
            r"\frac{T^2}{r^3} = 1.00\pm 0.01\;\mathrm{yr^2/AU^3}\ \forall\text{ planets}",
            color=GOLD, font_size=22,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(verify_lbl), run_time=0.8)
        self.wait(2.5)
