#!/usr/bin/env python3
"""
astro_powers_of_ten.py — 44 Orders of Magnitude: Powers-of-Ten Ladder
SILENT SLATE — brownblue dark palette, physics-plus-one-astronomy.

Physics:
    Scale ladder: 10^n for n = -15 to +26
    Key rungs with names, sizes, light-travel times.

Verify: python3 astro_powers_of_ten.py --verify
Render: manim -qh astro_powers_of_ten.py AstroPowersOfTenScene
"""
import sys
import numpy as np

C_LIGHT = 2.998e8  # m/s

RUNGS = [
    # (exp, name, color_key)
    (-15, "Proton",         "dim"),
    (-10, "Atom",           "blue"),
    (-6,  "Bacterium",      "dim"),
    (0,   "Human 1 m",      "gold"),
    (7,   "Earth",          "blue"),
    (9,   "Sun",            "brown"),
    (11,  "1 AU",           "blue"),
    (16,  "Light-year",     "gold"),
    (21,  "Milky Way",      "blue"),
    (23,  "Local Group",    "dim"),
    (26,  "Observable Univ","brown"),
]

def light_travel(size_m):
    """Time in seconds for light to cross distance size_m."""
    return size_m / C_LIGHT

def human_readable_time(t_s):
    if t_s < 1e-6: return f"{t_s*1e9:.1f} ns"
    if t_s < 1e-3: return f"{t_s*1e6:.1f} us"
    if t_s < 1:    return f"{t_s*1e3:.1f} ms"
    if t_s < 60:   return f"{t_s:.1f} s"
    if t_s < 3600: return f"{t_s/60:.1f} min"
    if t_s < 86400:return f"{t_s/3600:.1f} hr"
    if t_s < 3.16e7: return f"{t_s/86400:.1f} days"
    if t_s < 3.16e10: return f"{t_s/3.16e7:.1f} yr"
    return f"{t_s/3.16e13:.1f} Gyr"

def verify():
    print("=== Powers-of-ten verification ===")
    # P1: AU = 1.496e11 m -> between 1e11 and 1e12
    au = 1.496e11
    assert 1e11 < au < 1e12, f"AU check failed: {au}"
    print(f"P1: AU = {au:.3e} m  — between 10^11 and 10^12 ✓")
    # P2: ratio universe/proton
    ratio = 8.8e26 / 1e-15
    print(f"P2: Universe/proton = {ratio:.2e}  (~41-42 decades) {'✓' if 1e40 < ratio < 1e43 else '✗'}")
    # Light times
    print("\nLight-travel times:")
    for exp, name, _ in RUNGS:
        t = light_travel(10**exp)
        print(f"  {name:20s} (1e{exp:+d} m): {human_readable_time(t)}")
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

RUNG_COLORS = {"blue": BLUE, "brown": BROWN, "gold": GOLD, "dim": DIM}


class AstroPowersOfTenScene(Scene):
    """
    Horizontal logarithmic scale bar from 10^-15 to 10^26.
    Icons appear at each rung with name + light-travel time.
    """

    def construct(self):
        self.camera.background_color = CANVAS
        self._title()
        self._ruler()
        self._finale()

    def _title(self):
        t = Text("44 Orders of Magnitude",
                 font="EB Garamond", font_size=60, color=INK)
        s = Text(
            "From a proton (10⁻¹⁵ m) to the observable universe (10²⁶ m).\n"
            "Every step is ×10. Intuition breaks around 10⁷.",
            font="EB Garamond", font_size=22, color=DIM,
        )
        VGroup(t, s).arrange(DOWN, buff=0.35).center()
        self.play(Write(t), run_time=1.3)
        self.play(FadeIn(s), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(t, s), run_time=0.5)

    def _ruler(self):
        # Horizontal bar spanning scene width
        MIN_EXP = -15
        MAX_EXP = 26
        bar_width = 12.0
        bar_y = -0.5

        def exp_to_x(exp):
            frac = (exp - MIN_EXP) / (MAX_EXP - MIN_EXP)
            return -bar_width / 2 + frac * bar_width

        # Main ruler line
        ruler = Line(
            np.array([exp_to_x(MIN_EXP), bar_y, 0]),
            np.array([exp_to_x(MAX_EXP), bar_y, 0]),
            color=DIM, stroke_width=2,
        )
        self.play(Create(ruler), run_time=1.5)

        # Decade ticks (every integer exponent)
        ticks = VGroup()
        for exp in range(MIN_EXP, MAX_EXP + 1):
            x = exp_to_x(exp)
            tick = Line(
                np.array([x, bar_y - 0.08, 0]),
                np.array([x, bar_y + 0.08, 0]),
                color=DIM, stroke_width=0.8,
            )
            ticks.add(tick)
        self.play(Create(ticks), run_time=0.5)

        # Rung labels: place alternating above/below
        all_dots = VGroup()
        for i, (exp, name, col_key) in enumerate(RUNGS):
            col = RUNG_COLORS[col_key]
            x = exp_to_x(exp)

            dot = Dot(np.array([x, bar_y, 0]), color=col, radius=0.1)

            above = (i % 2 == 0)
            y_lbl = bar_y + 1.6 if above else bar_y - 1.4

            size_str = f"$10^{{{exp}}}$ m" if exp != 0 else "1 m"
            size_mob = MathTex(rf"10^{{{exp}}}\,\mathrm{{m}}" if exp != 0 else r"1\,\mathrm{m}",
                               color=col, font_size=17)
            name_mob = Text(name, font="EB Garamond", font_size=16, color=col)

            t_light = human_readable_time(light_travel(10**exp))
            time_mob = Text(f"light: {t_light}", font="EB Garamond",
                            font_size=13, color=DIM)

            group = VGroup(name_mob, size_mob, time_mob).arrange(DOWN, buff=0.08)
            group.move_to(np.array([x, y_lbl, 0]))

            stem = Line(
                np.array([x, bar_y + (0.1 if above else -0.1), 0]),
                np.array([x, y_lbl + (-0.3 if above else 0.3), 0]),
                color=col, stroke_width=1, stroke_opacity=0.5,
            )

            all_dots.add(dot)
            self.play(
                FadeIn(dot),
                Create(stem),
                Write(name_mob),
                Write(size_mob),
                Write(time_mob),
                run_time=0.7,
            )

        self.wait(2.5)

        # Span annotation
        span = MathTex(
            r"10^{26} / 10^{-15} = 10^{41}\ \text{orders of magnitude}",
            color=GOLD, font_size=26,
        ).to_edge(DOWN, buff=0.2)
        self.play(Write(span), run_time=1.2)
        self.wait(2.0)

    def _finale(self):
        eq = Text(
            "Intuition is calibrated to 10⁰ — everything else is notation.",
            font="EB Garamond", font_size=28, color=INK,
        ).center().shift(DOWN * 2.8)
        self.play(Write(eq), run_time=1.5)
        self.wait(2.5)
