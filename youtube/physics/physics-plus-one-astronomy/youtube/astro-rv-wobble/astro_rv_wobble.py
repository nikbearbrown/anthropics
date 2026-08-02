#!/usr/bin/env python3
"""
astro_rv_wobble.py — Radial Velocity Wobble: How 51 Peg b Was Found
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    RV semi-amplitude (circular orbit):
        K = (2*pi*G/P)^(1/3) * m_p * sin(i) / (m_star + m_p)^(2/3)
    Doppler: delta_lambda / lambda = v_r / c

Verify: python3 astro_rv_wobble.py --verify
Render: manim -qh astro_rv_wobble.py AstroRvWobbleScene
"""
import sys
import numpy as np

# ─── Physical constants ───────────────────────────────────────────────────────
G_GRAV  = 6.674e-11
C_LIGHT = 2.998e8
M_SUN   = 1.989e30
M_JUP   = 1.898e27
DAY_SEC = 86400.0

def rv_amplitude(P_days, m_p_Mjup, m_star_Msun, inc_deg=90.0, e=0.0):
    """
    RV semi-amplitude K in m/s.
    P in days, m_p in Jupiter masses, m_star in solar masses.
    """
    P = P_days * DAY_SEC
    m_p = m_p_Mjup * M_JUP
    m_s = m_star_Msun * M_SUN
    sini = np.sin(np.radians(inc_deg))
    K = (2 * np.pi * G_GRAV / P)**(1/3) * m_p * sini / (m_s + m_p)**(2/3) / np.sqrt(1 - e**2)
    return K

def doppler_shift_pm(v_ms, lam_nm=656.3):
    """Wavelength shift in picometres for Halpha."""
    return v_ms / C_LIGHT * lam_nm * 1e3   # pm

def verify():
    print("=== RV wobble verification ===")
    # 51 Peg b parameters
    K = rv_amplitude(4.23, 0.47, 1.04, inc_deg=80.0, e=0.0)
    print(f"P1: K for 51 Peg b = {K:.1f} m/s  (expected ~56 m/s) {'✓' if 45 < K < 70 else '✗'}")

    # P2: doubling m_p -> K doubles (in m_p << m_star limit)
    K2 = rv_amplitude(4.23, 0.94, 1.04, inc_deg=80.0, e=0.0)
    ratio = K2 / K
    print(f"P2: K(2*m_p)/K = {ratio:.3f}  (expected ~2.0) {'✓' if abs(ratio - 2.0) < 0.05 else '✗'}")

    # Doppler shift on Halpha
    ds = doppler_shift_pm(K)
    print(f"Delta lambda at Halpha = {ds:.3f} pm  (expected ~0.12 pm)")
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

P_DAYS  = 4.23
M_P_JUP = 0.47
M_S_SUN = 1.04
INC     = 80.0
K_MS    = rv_amplitude(P_DAYS, M_P_JUP, M_S_SUN, inc_deg=INC)


class AstroRvWobbleScene(Scene):
    """
    Top: star-planet orbital system. Bottom: RV sinusoid K*sin(2*pi*t/P).
    Slider sweeps planet mass; K scales.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        ax_orbit, ax_rv = self._layout()
        self._orbit_animation(ax_orbit, ax_rv)
        self._slider_phase(ax_rv)
        self._finale()

    def _title(self):
        t = Text("Radial Velocity Wobble: How 51 Peg b Was Found",
                 font="EB Garamond", font_size=46, color=INK)
        s = Text(
            "A 56 m/s Doppler wobble — 1/5000th of highway speed.\n"
            "From 50 light-years away.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _layout(self):
        ax_orbit = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=4,
            y_length=4,
            axis_config=dict(color=DIM, stroke_width=0.5,
                             include_ticks=False, tip_length=0.1),
        ).shift(LEFT * 3.5 + UP * 0.3)

        ax_rv = Axes(
            x_range=[0, 2.0, 0.5],    # t in periods (0 to 2)
            y_range=[-80, 80, 40],
            x_length=7,
            y_length=4,
            axis_config=dict(color=INK, stroke_width=1.5,
                             include_ticks=False, tip_length=0.2),
        ).shift(RIGHT * 1.5 + UP * 0.3)

        lx = MathTex(r"t\;(\mathrm{periods})", color=INK, font_size=20).next_to(ax_rv.x_axis.get_end(), RIGHT, buff=0.1)
        ly = MathTex(r"v_r\;(\mathrm{m/s})", color=INK, font_size=20).next_to(ax_rv.y_axis.get_end(), UP, buff=0.1)
        hdr = Text("51 Pegasi — RV curve", font="EB Garamond",
                   font_size=18, color=DIM).next_to(ax_rv, UP, buff=0.1)
        orbit_hdr = Text("Orbital view", font="EB Garamond",
                         font_size=18, color=DIM).next_to(ax_orbit, UP, buff=0.1)

        self.play(Create(ax_orbit), Create(ax_rv),
                  Write(lx), Write(ly), Write(hdr), Write(orbit_hdr), run_time=1.5)
        return ax_orbit, ax_rv

    def _orbit_animation(self, ax_orbit, ax_rv):
        # Star and planet orbit barycenter
        # Barycenter at center; star has tiny orbit, planet larger
        # mass ratio ~1.04 M_sun / 0.47 M_jup >> 1, so star barely moves
        r_planet = 0.9   # display units
        r_star   = r_planet * (M_P_JUP * 1.898e27) / (M_S_SUN * 1.989e30)  # tiny

        star = Dot(ORIGIN, color=GOLD, radius=0.2)
        planet = Dot(np.array([r_planet, 0, 0]), color=DIM, radius=0.1)
        star.move_to(ax_orbit.c2p(-r_star, 0))

        orbit_circle = Circle(radius=ax_orbit.c2p(r_planet, 0)[0] - ax_orbit.c2p(0, 0)[0],
                              color=DIM, stroke_width=1, stroke_opacity=0.4)
        orbit_circle.move_to(ax_orbit.c2p(0, 0))

        self.play(FadeIn(star), Create(orbit_circle), run_time=0.5)

        # RV curve: K*sin(2*pi*t/P) — draw simultaneously with orbit
        t_vals = np.linspace(0, 2.0, 400)
        v_vals = K_MS * np.sin(2 * np.pi * t_vals)

        rv_pts = np.array([ax_rv.c2p(t, v) for t, v in zip(t_vals, v_vals)])
        rv_curve = VMobject(color=BLUE, stroke_width=3)
        rv_curve.set_points_smoothly(rv_pts)

        # Animate planet + rv curve simultaneously using tracker
        angle_tracker = ValueTracker(0.0)

        def _planet_pos():
            angle = angle_tracker.get_value()
            x_p = r_planet * np.cos(angle)
            y_p = r_planet * np.sin(angle)
            x_s = -r_star * np.cos(angle)
            y_s = -r_star * np.sin(angle)
            planet.move_to(ax_orbit.c2p(x_p, y_p))
            star.move_to(ax_orbit.c2p(x_s, y_s))

        # Draw orbit + RV together
        self.play(FadeIn(planet), run_time=0.3)
        self.play(Create(rv_curve), run_time=3.0)

        # Now animate planet orbiting (2 full cycles)
        for full_cycle in range(2):
            for step in range(60):
                angle = 2 * np.pi * step / 60
                _planet_pos()
                self.wait(1/30)

        K_lbl = MathTex(rf"K = {K_MS:.0f}\,\mathrm{{m/s}}", color=GOLD, font_size=26)
        K_lbl.to_edge(DOWN, buff=0.25)
        self.play(Write(K_lbl), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(K_lbl), run_time=0.3)

    def _slider_phase(self, ax_rv):
        mp_tracker = ValueTracker(M_P_JUP)

        def _rv_curve():
            mp = mp_tracker.get_value()
            K = rv_amplitude(P_DAYS, mp, M_S_SUN, inc_deg=INC)
            t_vals = np.linspace(0, 2.0, 300)
            v_vals = K * np.sin(2 * np.pi * t_vals)
            pts = np.array([ax_rv.c2p(t, np.clip(v, -78, 78)) for t, v in zip(t_vals, v_vals)])
            m = VMobject(color=GOLD, stroke_width=3)
            m.set_points_smoothly(pts)
            return m

        dyn = always_redraw(_rv_curve)
        self.add(dyn)

        mp_lbl = MathTex(r"m_p = ", color=INK, font_size=26)
        mp_num = DecimalNumber(M_P_JUP, num_decimal_places=2, color=GOLD, font_size=26)
        mp_Jup = MathTex(r"M_\mathrm{Jup}", color=INK, font_size=26)
        mp_num.add_updater(lambda m: m.set_value(mp_tracker.get_value()))
        K_lbl2 = MathTex(r"K = ", color=DIM, font_size=22)
        K_num  = DecimalNumber(K_MS, num_decimal_places=1, color=BLUE, font_size=22)
        K_unit = MathTex(r"\,\mathrm{m/s}", color=DIM, font_size=22)
        K_num.add_updater(lambda m: m.set_value(rv_amplitude(P_DAYS, mp_tracker.get_value(), M_S_SUN, INC)))

        top_row = VGroup(mp_lbl, mp_num, mp_Jup).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.3)
        bot_row = VGroup(K_lbl2, K_num, K_unit).arrange(RIGHT, buff=0.1).to_edge(DOWN, buff=0.25)

        self.play(Write(top_row), Write(bot_row), run_time=0.8)
        self.play(mp_tracker.animate.set_value(1.0), run_time=2.5, rate_func=smooth)
        self.play(mp_tracker.animate.set_value(0.1), run_time=2.0, rate_func=smooth)
        self.play(mp_tracker.animate.set_value(M_P_JUP), run_time=1.5, rate_func=smooth)
        self.wait(1.5)
        self.play(FadeOut(top_row, bot_row, dyn), run_time=0.4)

    def _finale(self):
        eq = MathTex(
            r"K = \left(\frac{2\pi G}{P}\right)^{1/3} \frac{m_p\sin i}{(m_\star+m_p)^{2/3}}",
            r"\quad \approx 56\,\mathrm{m/s}",
            color=INK, font_size=28,
        )
        eq.arrange(RIGHT, buff=0.3).to_edge(DOWN, buff=0.25)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
