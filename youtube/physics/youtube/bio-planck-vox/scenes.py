import json
import numpy as np
from pathlib import Path
from manim import *

# ── voxbio / voxpaper palette ─────────────────────────────────────────────────
CANVAS  = "#F5F0E8"    # aged paper / warm cream
BLUE    = "#5B7B9C"    # dusty blue accent
BROWN   = "#D35F43"    # terracotta / warm
YELLOW  = "#F5D061"    # golden highlight
INK     = "#2C2B28"    # near-black serif ink
DIM     = "#9A9080"    # secondary / muted
FONT    = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs   = json.loads((HERE / "beat_sheet.json").read_text())
    DUR   = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 5)
             for b in _bs.get("beats", [])}
    TITLE = _bs["metadata"].get("title", "")
except Exception:
    DUR = {}; TITLE = ""

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CANVAS, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def blue_txt(t, size=36, color=BLUE, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def brown_txt(t, size=36, color=BROWN, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def dim_txt(t, size=28, color=DIM, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def highlight_bar(mobj, color=YELLOW, opacity=0.55):
    """Return a golden highlight rectangle behind mobj."""
    rect = BackgroundRectangle(mobj, color=color, fill_opacity=opacity, buff=0.06)
    return rect

# ── INTRO — title plate ────────────────────────────────────────────────────────
class INTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("INTRO")
        self.add(bg())

        series = dim_txt("Bear's Notes — Bios", size=24).move_to(UP * 3.2)
        name   = ink_txt("Max Planck", size=72, weight=BOLD).move_to(UP * 1.2)
        sub    = ink_txt("The Reluctant Revolutionary", size=36).next_to(name, DOWN, buff=0.28)
        rule   = Line(LEFT * 3.8, RIGHT * 3.8, stroke_width=1.2, color=BLUE).next_to(sub, DOWN, buff=0.25)
        dates  = dim_txt("1858 — 1947", size=28).next_to(rule, DOWN, buff=0.2)

        self.play(FadeIn(series), run_time=0.3)
        self.play(Write(name), run_time=0.65)
        self.play(Write(sub), run_time=0.5)
        self.play(Create(rule), run_time=0.3)
        self.play(FadeIn(dates, shift=DOWN * 0.15), run_time=0.3)
        self.wait(dur - 2.05)

# ── H01 — hook: Munich 1874, warning ─────────────────────────────────────────
class H01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H01")
        self.add(bg())

        # archival plate stand-in: a structured card with period typography
        plate_box = Rectangle(width=9.5, height=5.8, color=DIM, fill_color="#EDE8DC",
                              fill_opacity=1.0, stroke_width=1.5)
        plate_box.move_to(UP * 0.5)

        # interior "photograph" — hatched lines to suggest an archival image
        hatch = VGroup(*[
            Line(plate_box.get_left() + RIGHT * 0.3 + UP * (v - 2.5),
                 plate_box.get_right() + LEFT * 0.3 + UP * (v - 2.5),
                 stroke_width=0.4, color=DIM, stroke_opacity=0.3)
            for v in np.linspace(0, 5.2, 40)
        ])
        place_label = dim_txt("Munich · 1874", size=22).move_to(plate_box.get_top() + DOWN * 0.32)

        # warning card
        warn_rect = Rectangle(width=7.5, height=1.4, color=INK, fill_color=CANVAS,
                              fill_opacity=0.92, stroke_width=1.2)
        warn_rect.move_to(plate_box.get_bottom() + UP * 1.0)
        warn_txt  = ink_txt(
            '"Everything important has already been discovered."',
            size=25
        ).move_to(warn_rect.get_center())

        # young Planck label
        planck_label = dim_txt("— the professor's warning to young Planck", size=21)
        planck_label.next_to(warn_rect, DOWN, buff=0.12)

        self.play(FadeIn(plate_box), run_time=0.35)
        self.play(Create(hatch), FadeIn(place_label), run_time=0.5)
        # slow push simulation (scale up slightly)
        self.play(plate_box.animate.scale(1.04).shift(LEFT * 0.1),
                  hatch.animate.scale(1.04).shift(LEFT * 0.1),
                  run_time=2.5)
        self.play(FadeIn(warn_rect), Write(warn_txt), run_time=0.6)
        self.play(FadeIn(planck_label), run_time=0.35)
        self.wait(dur - 4.3)

# ── H02 — date card 1900, pivot ───────────────────────────────────────────────
class H02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H02")
        self.add(bg())

        # dim background plate
        plate_box = Rectangle(width=9.5, height=5.8, color=DIM, fill_color="#EDE8DC",
                              fill_opacity=0.4, stroke_width=1.0).move_to(UP * 0.5)
        self.add(plate_box)

        date_card = Rectangle(width=4.0, height=2.2, color=INK, fill_color=CANVAS,
                              fill_opacity=0.96, stroke_width=1.8)
        date_card.move_to(ORIGIN)
        year      = ink_txt("1900", size=88, weight=BOLD).move_to(date_card.get_center())
        underline = Line(LEFT * 1.5, RIGHT * 1.5, stroke_width=2.5, color=BROWN)
        underline.next_to(year, DOWN, buff=0.1)

        self.play(FadeIn(date_card), Write(year), run_time=0.55)
        self.play(Create(underline), run_time=0.35)
        self.play(
            plate_box.animate.set_opacity(0.15),
            run_time=0.4
        )
        self.wait(dur - 1.3)

# ── H03 — thesis card, "reluctant revolutionary" ─────────────────────────────
class H03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("H03")
        self.add(bg())

        # date card still present (dim)
        date_card = Rectangle(width=4.0, height=2.2, color=INK, fill_color=CANVAS,
                              fill_opacity=0.5, stroke_width=1.0).move_to(UP * 1.5).set_opacity(0.3)
        year      = ink_txt("1900", size=60, weight=BOLD, color=DIM).move_to(date_card.get_center())
        self.add(date_card, year)

        # thesis card
        thesis_rect = Rectangle(width=8.5, height=1.8, color=INK, fill_color=CANVAS,
                                fill_opacity=0.94, stroke_width=1.5)
        thesis_rect.move_to(DOWN * 0.8)
        the_word   = ink_txt("the reluctant revolutionary", size=38)
        the_word.move_to(thesis_rect.get_center())

        # highlight behind "reluctant"
        target_word = ink_txt("reluctant", size=38)
        target_word.align_to(the_word, LEFT)
        # compute approximate width
        hl_rect = Rectangle(
            width=3.5, height=0.58,
            fill_color=YELLOW, fill_opacity=0.55, stroke_width=0
        )
        hl_rect.align_to(thesis_rect.get_left() + RIGHT * 0.55, LEFT)
        hl_rect.align_to(thesis_rect, DOWN).shift(UP * 0.62)

        self.play(FadeIn(thesis_rect), run_time=0.35)
        self.play(Write(the_word), run_time=0.5)
        # sweep highlight bar
        self.play(FadeIn(hl_rect), run_time=0.4)
        self.wait(dur - 1.25)

# ── W01 — Berlin lab, spectral curve ─────────────────────────────────────────
class W01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("W01")
        self.add(bg())

        # axes for spectral curve
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.2, 0.5],
            x_length=8.5,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5, "include_tip": True,
                         "tip_length": 0.18, "tick_size": 0.07},
        ).shift(DOWN * 0.3)

        x_label = dim_txt("frequency  ν", size=24).next_to(ax.x_axis, DOWN, buff=0.25)
        y_label = dim_txt("intensity  B(ν,T)", size=24).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.2)

        # blackbody-shaped measured curve (Planck-like)
        def planck(x, scale=1.0):
            if x < 0.01:
                return 0
            return scale * (x ** 3) / (np.exp(2.0 * x) - 1 + 1e-9)

        measured = ax.plot(lambda x: planck(x), x_range=[0.05, 4.8],
                           color=BLUE, stroke_width=2.8)

        place_label = dim_txt("Berlin · Physikalisch-Technische Reichsanstalt · 1899", size=20)
        place_label.to_edge(UP, buff=0.35)

        self.play(FadeIn(ax), FadeIn(x_label), FadeIn(y_label), FadeIn(place_label), run_time=0.55)
        self.play(Create(measured), run_time=0.8)
        self.wait(dur - 1.35)

# ── W02 — classical curve diverges ───────────────────────────────────────────
class W02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("W02")
        self.add(bg())

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.2, 0.5],
            x_length=8.5,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5, "include_tip": False,
                         "tick_size": 0.0},
        ).shift(DOWN * 0.3)
        x_label = ink_txt("frequency", size=52).next_to(ax.x_axis, DOWN, buff=0.25)
        y_label = ink_txt("intensity", size=52).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.2)

        def planck(x):
            if x < 0.01:
                return 0
            return (x ** 3) / (np.exp(2.0 * x) - 1 + 1e-9)

        measured = ax.plot(planck, x_range=[0.05, 4.8], color=BLUE, stroke_width=2.5)

        # classical Rayleigh-Jeans: diverges as x²
        def classical(x):
            return min(0.04 * (x ** 2), 1.15)   # capped for frame

        classical_curve = ax.plot(classical, x_range=[0.05, 5.0],
                                   color=INK, stroke_width=2.5)

        # word "infinite" on highlight bar — floats top of frame
        inf_word = ink_txt("infinite", size=52)
        inf_word.to_edge(UP, buff=0.5)
        hl = BackgroundRectangle(inf_word, color=YELLOW, fill_opacity=0.5, buff=0.1)

        self.add(ax, x_label, y_label, measured)
        self.play(Create(classical_curve), run_time=0.7)
        # curve bends off top
        self.play(
            classical_curve.animate.shift(UP * 0.6).set_stroke(opacity=0.7),
            run_time=0.5
        )
        self.play(FadeIn(hl), FadeIn(inf_word), run_time=0.4)
        self.wait(dur - 1.6)

# ── W03 — quote: "act of desperation" ────────────────────────────────────────
class W03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("W03")
        self.add(bg())

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.2, 0.5],
            x_length=8.5,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.0, "include_tip": False,
                         "tick_size": 0.05},
        ).shift(DOWN * 0.3).set_opacity(0.2)

        def planck(x):
            if x < 0.01:
                return 0
            return (x ** 3) / (np.exp(2.0 * x) - 1 + 1e-9)
        measured_dim = ax.plot(planck, x_range=[0.05, 4.8], color=BLUE, stroke_width=1.5,
                               stroke_opacity=0.3)

        self.add(ax, measured_dim)

        quote_box = Rectangle(width=8.5, height=2.2, color=INK, fill_color=CANVAS,
                              fill_opacity=0.96, stroke_width=1.5)
        quote_box.move_to(ORIGIN)
        quote_text = ink_txt('"an act of desperation"', size=42)
        quote_text.move_to(quote_box.get_center())
        attribution = dim_txt("— letter to R. W. Wood, 1931", size=23)
        attribution.next_to(quote_box, DOWN, buff=0.18)

        self.play(FadeIn(quote_box), run_time=0.3)
        self.play(Write(quote_text), run_time=0.6)
        self.play(FadeIn(attribution, shift=DOWN * 0.1), run_time=0.4)
        self.wait(dur - 1.3)

# ── W04 — E=hν card, classical curve snaps down ──────────────────────────────
class W04(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("W04")
        self.add(bg())

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.2, 0.5],
            x_length=8.5,
            y_length=4.5,
            axis_config={"color": INK, "stroke_width": 1.5, "include_tip": True,
                         "tip_length": 0.18, "tick_size": 0.07},
        ).shift(DOWN * 0.3)
        x_label = ink_txt("frequency  ν", size=36).next_to(ax.x_axis, DOWN, buff=0.25)

        def planck(x):
            if x < 0.01:
                return 0
            return (x ** 3) / (np.exp(2.0 * x) - 1 + 1e-9)

        measured = ax.plot(planck, x_range=[0.05, 4.8], color=BLUE, stroke_width=2.5)

        # classical starting position = diverged upward
        def classical_start(x):
            return min(0.04 * (x ** 2) + 0.6, 1.15)

        classical_before = ax.plot(classical_start, x_range=[0.05, 5.0],
                                    color=DIM, stroke_width=2.0, stroke_opacity=0.7)

        self.add(ax, x_label, measured, classical_before)

        # equation card
        eq_box = Rectangle(width=4.2, height=1.8, color=INK, fill_color=CANVAS,
                           fill_opacity=0.95, stroke_width=1.8)
        eq_box.to_edge(RIGHT, buff=1.2).shift(UP * 1.5)
        eq      = MathTex(r"E = h\nu", color=INK, font_size=64).move_to(eq_box.get_center())
        eq_note = ink_txt("Planck, 1900", size=36).next_to(eq_box, DOWN, buff=0.1)

        self.play(FadeIn(eq_box), Write(eq), run_time=0.55)
        self.play(FadeIn(eq_note), run_time=0.25)

        # classical curve snaps down onto measured
        def planck_approx(x):
            if x < 0.01:
                return 0
            return (x ** 3) / (np.exp(2.0 * x) - 1 + 1e-9)

        classical_after = ax.plot(planck_approx, x_range=[0.05, 4.8],
                                   color=BLUE, stroke_width=2.5)
        self.play(Transform(classical_before, classical_after), run_time=0.9)
        self.wait(dur - 1.7)

# ── W05 — E=hν highlight pulse ────────────────────────────────────────────────
class W05(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("W05")
        self.add(bg())

        eq = MathTex(r"E = h\nu", color=INK, font_size=60).move_to(ORIGIN)
        date_lbl = dim_txt("1900 — Max Planck", size=24).next_to(eq, DOWN, buff=0.45)

        self.add(eq, date_lbl)

        hl = highlight_bar(eq, color=YELLOW, opacity=0.55)
        self.play(FadeIn(hl), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(hl), run_time=0.4)
        self.wait(dur - 1.3)

# ── S01 — Einstein portrait, two positions ────────────────────────────────────
class S01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("S01")
        self.add(bg())

        # portrait box — left side
        portrait_box = Rectangle(width=3.8, height=4.8, color=DIM, fill_color="#E8E2D8",
                                 fill_opacity=1.0, stroke_width=1.5)
        portrait_box.move_to(LEFT * 3.5)
        portrait_lbl = dim_txt("Einstein · 1905", size=22).next_to(portrait_box, DOWN, buff=0.15)

        # hatch interior (archival feel)
        hatch = VGroup(*[
            Line(portrait_box.get_left() + RIGHT * 0.2 + UP * (v - 2.0),
                 portrait_box.get_right() + LEFT * 0.2 + UP * (v - 2.0),
                 stroke_width=0.35, color=DIM, stroke_opacity=0.25)
            for v in np.linspace(0, 4.4, 32)
        ])

        # contrast card — right side
        contrast_box = Rectangle(width=5.2, height=4.8, color=INK, fill_color=CANVAS,
                                 fill_opacity=0.95, stroke_width=1.5)
        contrast_box.move_to(RIGHT * 2.2)

        wall_lbl  = blue_txt("Planck's walls vibrate", size=25).move_to(contrast_box.get_center() + UP * 1.2)
        arrow_down = Arrow(wall_lbl.get_bottom(), contrast_box.get_center() + DOWN * 0.2,
                           stroke_width=1.5, color=DIM, buff=0.12,
                           max_tip_length_to_length_ratio=0.12)
        light_lbl = brown_txt("Einstein: light itself\nis discrete quanta", size=25)
        light_lbl.move_to(contrast_box.get_center() + DOWN * 1.0)
        resist_note = dim_txt("(Planck resisted this for years)", size=19)
        resist_note.next_to(contrast_box, DOWN, buff=0.12)

        self.play(
            FadeIn(portrait_box), Create(hatch), FadeIn(portrait_lbl),
            run_time=0.5
        )
        self.play(
            FadeIn(contrast_box),
            run_time=0.35
        )
        self.play(
            Write(wall_lbl), Create(arrow_down), Write(light_lbl),
            run_time=0.65
        )
        self.play(FadeIn(resist_note), run_time=0.3)
        self.wait(dur - 1.8)

# ── S02 — Nobel isotype grid ──────────────────────────────────────────────────
class S02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("S02")
        self.add(bg())

        title = ink_txt("Nobel Prizes in Physics — 1901 to 1918", size=28).to_edge(UP, buff=0.45)
        self.add(title)

        # 17 prizes in 18 years (none 1916), Planck is prize #17
        n_other = 16
        n_planck = 1
        cols = 6
        dot_r = 0.22
        spacing = 0.70

        def grid_pos(i):
            row = i // cols
            col = i % cols
            return np.array([
                -2.5 + col * spacing,
                1.2 - row * spacing,
                0.0
            ])

        other_dots  = [Dot(radius=dot_r, color=BLUE).move_to(grid_pos(i)) for i in range(n_other)]
        planck_dot  = Dot(radius=dot_r, color=BROWN).move_to(grid_pos(n_other))

        legend_other  = VGroup(Dot(radius=dot_r * 0.75, color=BLUE), dim_txt("other prizes", size=22))
        legend_other.arrange(RIGHT, buff=0.22).to_edge(DOWN, buff=0.6).shift(LEFT * 2.0)
        legend_planck = VGroup(Dot(radius=dot_r * 0.75, color=BROWN), dim_txt("Planck, 1918", size=22))
        legend_planck.arrange(RIGHT, buff=0.22).next_to(legend_other, RIGHT, buff=0.85)

        self.play(FadeIn(legend_other), FadeIn(legend_planck), run_time=0.35)
        self.play(
            LaggedStart(*[GrowFromCenter(dt) for dt in other_dots], lag_ratio=0.07),
            run_time=1.4
        )
        self.play(GrowFromCenter(planck_dot), run_time=0.45)
        self.wait(dur - 2.2)

# ── S03 — Nobel 1918 date card ────────────────────────────────────────────────
class S03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("S03")
        self.add(bg())

        year_lbl = ink_txt("1918", size=80, weight=BOLD).move_to(ORIGIN + UP * 0.6)
        nobel_lbl = dim_txt("Nobel Prize in Physics", size=32).next_to(year_lbl, DOWN, buff=0.3)
        dot = Dot(color=BROWN, radius=0.3).next_to(nobel_lbl, DOWN, buff=0.45)

        self.add(year_lbl, nobel_lbl, dot)
        self.play(Indicate(dot, scale_factor=1.5, color=BROWN), run_time=0.6)
        self.wait(dur - 0.6)

# ── P01 — Berlin ruins, date 1945 ─────────────────────────────────────────────
class P01(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("P01")
        self.add(bg())

        # archival plate card — restrained, no dramatization
        plate_box = Rectangle(width=10.0, height=5.5, color=DIM, fill_color="#DDD8CE",
                              fill_opacity=1.0, stroke_width=1.2)
        plate_box.move_to(ORIGIN)
        hatch = VGroup(*[
            Line(plate_box.get_left() + RIGHT * 0.35 + UP * (v - 2.5),
                 plate_box.get_right() + LEFT * 0.35 + UP * (v - 2.5),
                 stroke_width=0.35, color=DIM, stroke_opacity=0.22)
            for v in np.linspace(0, 5.1, 38)
        ])
        place_label = dim_txt("Berlin · 1945", size=22).move_to(plate_box.get_top() + DOWN * 0.32)

        date_card = Rectangle(width=2.8, height=1.4, color=INK, fill_color=CANVAS,
                              fill_opacity=0.88, stroke_width=1.2)
        date_card.to_corner(DR, buff=0.6)
        date_txt  = ink_txt("1945", size=48, weight=BOLD).move_to(date_card.get_center())

        self.play(FadeIn(plate_box), run_time=0.35)
        self.play(Create(hatch), FadeIn(place_label), run_time=0.5)
        self.play(FadeIn(date_card), FadeIn(date_txt), run_time=0.45)
        self.wait(dur - 1.3)

# ── P02 — quote card, Planck's famous line ────────────────────────────────────
class P02(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("P02")
        self.add(bg())

        # long quote — split into 3 lines
        line1 = ink_txt('"A new scientific truth does not triumph', size=28)
        line2 = ink_txt("by convincing its opponents,", size=28)
        line3 = ink_txt('but because its opponents eventually die."', size=28)
        lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.28).move_to(UP * 0.6)

        attribution = dim_txt("— Scientific Autobiography, 1948", size=22)
        attribution.next_to(lines, DOWN, buff=0.38)

        # golden highlight on "a new scientific truth"
        hl = BackgroundRectangle(line1, color=YELLOW, fill_opacity=0.52, buff=0.08)

        self.play(Write(line1), run_time=0.6)
        self.play(Write(line2), run_time=0.5)
        self.play(Write(line3), run_time=0.6)
        self.play(FadeIn(hl), run_time=0.35)
        self.play(FadeIn(attribution, shift=DOWN * 0.1), run_time=0.35)
        self.wait(dur - 2.4)

# ── P03 — closing portrait + E=hν ────────────────────────────────────────────
class P03(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("P03")
        self.add(bg())

        # portrait box — center, older Planck
        portrait_box = Rectangle(width=4.0, height=5.0, color=DIM, fill_color="#E2DDD5",
                                 fill_opacity=1.0, stroke_width=1.5)
        portrait_box.move_to(UP * 0.5)
        portrait_lbl = dim_txt("Max Planck · c. 1930", size=22).next_to(portrait_box, UP, buff=0.2)
        hatch = VGroup(*[
            Line(portrait_box.get_left() + RIGHT * 0.25 + UP * (v - 2.3),
                 portrait_box.get_right() + LEFT * 0.25 + UP * (v - 2.3),
                 stroke_width=0.4, color=DIM, stroke_opacity=0.22)
            for v in np.linspace(0, 4.6, 32)
        ])

        eq      = MathTex(r"E = h\nu", color=INK, font_size=56)
        eq.next_to(portrait_box, DOWN, buff=0.32)

        self.play(FadeIn(portrait_box), Create(hatch), FadeIn(portrait_lbl), run_time=0.55)
        self.play(FadeIn(eq, shift=DOWN * 0.12), run_time=0.4)
        # slow settle to stillness
        self.wait(dur - 0.95)

# ── OUTRO — outro plate ────────────────────────────────────────────────────────
class OUTRO(Scene):
    def construct(self):
        self.camera.background_color = CANVAS
        dur = d("OUTRO")
        self.add(bg())

        series  = dim_txt("Bear's Notes — Bios", size=26).move_to(UP * 1.6)
        rule    = Line(LEFT * 2.5, RIGHT * 2.5, stroke_width=1.0, color=BLUE).next_to(series, DOWN, buff=0.22)
        thanks  = ink_txt("Thanks for watching.", size=34).next_to(rule, DOWN, buff=0.28)
        channel = dim_txt("youtube.com/@NikBearBrown", size=22).next_to(thanks, DOWN, buff=0.22)

        self.play(FadeIn(series), Create(rule), run_time=0.4)
        self.play(Write(thanks), run_time=0.45)
        self.play(FadeIn(channel), run_time=0.3)
        self.wait(dur - 1.15)
