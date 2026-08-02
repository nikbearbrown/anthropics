#!/usr/bin/env python3
"""
physics_kepler_third_law_orbits.py — Orbital Speed + Kepler T² ∝ r³
SILENT SLATE — brownblue math-explainer candidate.

Physics (Earth orbits, GM_E = 3.986e14 m³/s²):
    LEO  r=6.628e6 m  T=89.5 min   v=7755 m/s
    ISS  r=6.778e6 m  T=92.7 min   v=7660 m/s
    GPS  r=2.656e7 m  T=718 min    v=3874 m/s
    GEO  r=4.216e7 m  T=1436 min   v=3070 m/s

Render:
    cd physics/youtube/physics-kepler-third-law-orbits
    manim -qh physics_kepler_third_law_orbits.py KeplerThirdLawScene
"""
import sys
import numpy as np

GM_E = 3.986e14  # m³/s²


def orbital_speed(r): return np.sqrt(GM_E/r)
def orbital_period(r): return 2*np.pi*r / orbital_speed(r)  # seconds


ORBITS = {
    "LEO": 6.628e6,
    "ISS": 6.778e6,
    "GPS": 2.656e7,
    "GEO": 4.216e7,
    "Moon": 3.84e8,
}


def verify():
    print("=== Kepler Third Law verification ===")
    for name, r in ORBITS.items():
        v  = orbital_speed(r)
        T  = orbital_period(r)/60  # min
        print(f"  {name}: r={r:.3e} m  v={v:.1f} m/s  T={T:.1f} min")
    # P1: T_GEO/T_LEO ratio
    T_GEO = orbital_period(ORBITS["GEO"])
    T_LEO = orbital_period(ORBITS["LEO"])
    ratio = T_GEO/T_LEO
    expected = (ORBITS["GEO"]/ORBITS["LEO"])**1.5
    print(f"  T_GEO/T_LEO = {ratio:.3f}  (from r^3/2 = {expected:.3f})")
    # P2: Kepler T²/r³ = const check
    for name, r in ORBITS.items():
        T_yr  = orbital_period(r) / (365.25*24*3600)
        r_AU  = r / 1.496e11
        const = T_yr**2 / r_AU**3
        print(f"    {name}: T²/r³ = {const:.6f} yr²/AU³  (should be ~1 for solar system)")
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

ORB_COLORS = [BLUE, GOLD, BROWN, DIM]
ORB_KEYS   = ["LEO", "GPS", "GEO", "Moon"]


class KeplerThirdLawScene(Scene):
    """Orbital rings, speed comparison, then log-log T² ∝ r³ plot."""

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._orbital_diagram()
        self._loglog_plot()

    def _title(self):
        t1 = Text("Kepler's Third Law", font="EB Garamond", font_size=62, color=INK)
        t2 = Text("T² ∝ r³ — the half-power you didn't expect", font="EB Garamond", font_size=26, color=DIM)
        t3 = MathTex(r"T = \frac{2\pi r^{3/2}}{\sqrt{GM}}\qquad v = \sqrt{\frac{GM}{r}}", color=BLUE, font_size=30)
        VGroup(t1, t2, t3).arrange(DOWN, buff=0.3).center()
        self.play(Write(t1), run_time=1.0)
        self.play(FadeIn(t2, t3), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t1, t2, t3), run_time=0.4)

    def _orbital_diagram(self):
        earth = Circle(radius=0.25, color=BLUE, fill_color=BLUE, fill_opacity=0.8).center()
        self.play(FadeIn(earth), run_time=0.5)

        # Log-scaled orbit radii for display
        r_display = [0.8, 2.0, 2.8, 4.5]
        orbit_circles = []
        sats = []
        for i, (key, r_d, col) in enumerate(zip(ORB_KEYS, r_display, ORB_COLORS)):
            circ = Circle(radius=r_d, color=col, stroke_width=1.2, stroke_opacity=0.5)
            orbit_circles.append(circ)
            sat = Dot(circ.get_right(), color=col, radius=0.12)
            sats.append(sat)
            lbl = Text(key, font="EB Garamond", font_size=18, color=col)
            lbl.next_to(circ.get_top(), UP, buff=0.06)
            self.play(Create(circ), FadeIn(sat), Write(lbl), run_time=0.5)

        # Animate orbital speeds (LEO fastest)
        T_leos = [orbital_period(ORBITS[k]) for k in ORB_KEYS]
        T_min  = min(T_leos)
        speeds = [T_min/T for T in T_leos]  # relative angular speed

        cap = Text("Outer satellites move slower — watch the race",
                   font="EB Garamond", font_size=20, color=INK).to_edge(DOWN, buff=0.22)
        self.play(Write(cap), run_time=0.6)

        angles = [0.0]*4
        for _ in range(60):
            new_mobs = []
            for i in range(4):
                angles[i] += speeds[i] * 0.1
                r_d = r_display[i]
                new_pos = np.array([r_d*np.cos(angles[i]), r_d*np.sin(angles[i]), 0])
                new_mobs.append(sats[i].animate.move_to(new_pos))
            self.play(*new_mobs, run_time=0.08, rate_func=linear)

        self.play(FadeOut(cap), run_time=0.3)
        # Speed readout table
        rows = []
        for key, col in zip(ORB_KEYS, ORB_COLORS):
            r = ORBITS[key]
            v = orbital_speed(r)
            T = orbital_period(r)/60
            lbl = Text(f"{key}: v = {v:.0f} m/s, T = {T:.0f} min",
                       font="EB Garamond", font_size=18, color=col)
            rows.append(lbl)
        VGroup(*rows).arrange(DOWN, buff=0.18).to_edge(RIGHT, buff=0.3)
        self.play(*[Write(r) for r in rows], run_time=1.0)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

    def _loglog_plot(self):
        # r in AU, T in years for clarity (solar system scaling)
        r_AU_vals = {k: ORBITS[k]/1.496e11 for k in ORB_KEYS}
        T_yr_vals = {k: orbital_period(ORBITS[k])/(365.25*24*3600) for k in ORB_KEYS}

        log_r = [np.log10(r_AU_vals[k]) for k in ORB_KEYS]
        log_T = [np.log10(T_yr_vals[k]) for k in ORB_KEYS]

        ax = Axes(
            x_range=[-5, 1, 1],
            y_range=[-5, 1, 1],
            x_length=8,
            y_length=6,
            axis_config=dict(color=INK, stroke_width=1.4, include_ticks=True, tip_length=0.18),
        ).center().shift(DOWN*0.3)
        lx = Text("log₁₀(r / AU)", font="EB Garamond", font_size=20, color=INK).next_to(ax.x_axis.get_end(), RIGHT, buff=0.06)
        ly = Text("log₁₀(T / yr)", font="EB Garamond", font_size=20, color=INK).next_to(ax.y_axis.get_end(), UP, buff=0.06)
        hdr = Text("Kepler's Third Law — log-log: slope = 3/2",
                   font="EB Garamond", font_size=20, color=DIM).next_to(ax, UP, buff=0.12)
        self.play(Create(ax), Write(lx), Write(ly), Write(hdr), run_time=1.3)

        # T² ∝ r³ line: log T = 3/2 log r + const
        xs_line = np.linspace(-5, 1, 100)
        # From GEO: offset
        off = log_T[2] - 1.5*log_r[2]
        ys_line = 1.5*xs_line + off
        mask = (ys_line >= -5) & (ys_line <= 1)
        pts_line = np.array([ax.c2p(x, y) for x, y in zip(xs_line[mask], ys_line[mask])])
        crv = VMobject(color=DIM, stroke_width=1.8, stroke_opacity=0.6).set_points_smoothly(pts_line)
        slope_lbl = MathTex(r"\mathrm{slope}=\frac{3}{2}", color=DIM, font_size=22).move_to(ax.c2p(-2, -2))
        self.play(Create(crv), Write(slope_lbl), run_time=1.5)

        for key, col, lr, lt in zip(ORB_KEYS, ORB_COLORS, log_r, log_T):
            d = Dot(ax.c2p(lr, lt), color=col, radius=0.12)
            lbl = Text(key, font="EB Garamond", font_size=18, color=col).next_to(d, UR, buff=0.08)
            self.play(FadeIn(d), Write(lbl), run_time=0.6)

        final = Text(
            "One line — from LEO to the Moon — four orders of magnitude",
            font="EB Garamond", font_size=21, color=INK,
        ).to_edge(DOWN, buff=0.22)
        self.play(Write(final), run_time=1.0)
        self.wait(2.5)
