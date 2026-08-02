"""Portrait (9:16) Manim scenes for why-hot-ones-are-jerks Short.

Canvas: 1080x1920 (9:16). We set pixel_width=1080, pixel_height=1920 via
manim config so the scene units map to 9 wide × 16 tall. The scatter plot
is scaled down and centred in the portrait canvas.
"""
import json
import numpy as np
from pathlib import Path
from manim import *

# ── Colours ────────────────────────────────────────────────────────────────────
CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
ACCENT = "#5A5653"
RED    = "#C0392B"
FONT   = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs  = json.loads((HERE / "beat_sheet.json").read_text())
    DUR  = {b["beat_id"]: float(b.get("actual_duration_s") or
                                b.get("estimated_duration_s") or 5)
            for b in _bs.get("beats", [])}
    TITLE = _bs["metadata"].get("title", "")
except Exception:
    DUR = {}; TITLE = ""

def d(bid, default=5.0):
    return DUR.get(bid, default)

# ── Portrait config (applied per scene via config override) ─────────────────────
def _portrait_config():
    # Force portrait 4K: 2160×3840 pixels with 9:16 scene units.
    config.pixel_width  = 2160
    config.pixel_height = 3840
    config.frame_width  = 6.0                    # scene units wide
    config.frame_height = 6.0 * (3840 / 2160)   # ~10.67 scene units tall

# ── Axes box — fits portrait: narrower, centred ─────────────────────────────────
AX_W, AX_H = 4.5, 4.5          # equal aspect in portrait
AX_X0, AX_Y0 = -2.25, -3.5     # bottom-left corner (centred horizontally, shifted down)

def bg():
    return Rectangle(width=20, height=30).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=28, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def make_axes():
    x_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0 + AX_W, AX_Y0, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.18)
    y_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0, AX_Y0 + AX_H, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.18)
    return VGroup(x_axis, y_axis)

def _dot_positions(seed=42, n=80):
    rng = np.random.default_rng(seed)
    margin = 0.3
    xs = rng.uniform(AX_X0 + margin, AX_X0 + AX_W - margin, n)
    ys = rng.uniform(AX_Y0 + margin, AX_Y0 + AX_H - margin, n)
    return xs, ys

BAND_WIDTH = AX_W * 0.7

def make_dot_cloud(seed=42, n=80, color=INK, opacity=1.0):
    xs, ys = _dot_positions(seed, n)
    return VGroup(*[
        Dot([x, y, 0], radius=0.055, color=color).set_opacity(opacity)
        for x, y in zip(xs, ys)
    ])

def make_band_dots(seed=42, n=80):
    xs, ys = _dot_positions(seed, n)
    cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
    half = AX_W * 0.45
    accepted = [(x, y) for x, y in zip(xs, ys)
                if -half < (x - cx) + (y - cy) < half]
    return VGroup(*[Dot([x, y, 0], radius=0.055, color=INK) for x, y in accepted])

def make_cut_line(threshold, color=RED, stroke_w=3):
    cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
    x0 = AX_X0
    y0_raw = cy + threshold - (x0 - cx)
    y0 = np.clip(y0_raw, AX_Y0, AX_Y0 + AX_H)
    if y0 != y0_raw:
        y0 = AX_Y0 if y0_raw < AX_Y0 else AX_Y0 + AX_H
        x0 = cx + (y0 - cy) - threshold
        x0 = np.clip(x0, AX_X0, AX_X0 + AX_W)
    x1 = AX_X0 + AX_W
    y1_raw = cy + threshold - (x1 - cx)
    y1 = np.clip(y1_raw, AX_Y0, AX_Y0 + AX_H)
    if y1 != y1_raw:
        y1 = AX_Y0 if y1_raw < AX_Y0 else AX_Y0 + AX_H
        x1 = cx + (y1 - cy) - threshold
        x1 = np.clip(x1, AX_X0, AX_X0 + AX_W)
    return Line([x0, y0, 0], [x1, y1, 0], color=color, stroke_width=stroke_w)

# ══════════════════════════════════════════════════════════════════════════════
# SCENE 1 — Axes buildup  (A02 portrait)
# ══════════════════════════════════════════════════════════════════════════════

class A02_Axes(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        self.play(Create(axes), run_time=d("A02", 2.64) * 0.8)
        self.wait(d("A02", 2.64) * 0.2)

# ══════════════════════════════════════════════════════════════════════════════
# SCENE 2 — Dating pool + cuts  (A07 → A12 portrait)
# ══════════════════════════════════════════════════════════════════════════════

def _scene2_base():
    axes = make_axes()
    dots = make_dot_cloud()
    return axes, dots

class A07_CloudAgain(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        self.play(Create(axes), LaggedStartMap(FadeIn, dots, lag_ratio=0.01),
                  Write(pool_lbl), run_time=d("A07", 2.93) * 0.9)
        self.wait(d("A07", 2.93) * 0.1)

class A08_LowerCut(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        self.add(axes, dots, pool_lbl)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        self.play(Create(lo_cut), run_time=d("A08", 2.53) * 0.85)
        self.wait(d("A08", 2.53) * 0.15)

class A09_FadeLoLeft(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        self.add(axes, all_dots, pool_lbl, lo_cut)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        anims = []
        for dot in all_dots:
            p = dot.get_center()
            if (p[0] - cx) + (p[1] - cy) < -BAND_WIDTH / 2:
                anims.append(dot.animate.set_opacity(0.12).set_color(RED))
        if anims:
            self.play(*anims, run_time=d("A09", 2.35) * 0.85)
        self.wait(d("A09", 2.35) * 0.15)

class A10_UpperCut(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            p = dot.get_center()
            if (p[0] - cx) + (p[1] - cy) < -BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, pool_lbl, lo_cut)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED)
        self.play(Create(hi_cut), run_time=d("A10", 3.89) * 0.85)
        self.wait(d("A10", 3.89) * 0.15)

class A11_FadeUpRight(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            p = dot.get_center()
            if (p[0] - cx) + (p[1] - cy) < -BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, pool_lbl, lo_cut, hi_cut)
        anims = []
        for dot in all_dots:
            p = dot.get_center()
            if (p[0] - cx) + (p[1] - cy) > BAND_WIDTH / 2:
                anims.append(dot.animate.set_opacity(0.12).set_color(RED))
        if anims:
            self.play(*anims, run_time=d("A11", 2.22) * 0.85)
        self.wait(d("A11", 2.22) * 0.15)

class A12_BandHalo(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=22).move_to([0, AX_Y0 + AX_H + 0.5, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            p = dot.get_center()
            s = (p[0] - cx) + (p[1] - cy)
            if s < -BAND_WIDTH / 2 or s > BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, pool_lbl, lo_cut, hi_cut)
        bw = BAND_WIDTH / 2
        halo_pts = [
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 + bw - AX_W / 2 + 0.3, 0],
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 - bw - AX_W / 2 + 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 - bw + AX_W / 2 - 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 + bw + AX_W / 2 - 0.3, 0],
        ]
        halo = Polygon(*halo_pts, fill_color=ACCENT, fill_opacity=0.18,
                       stroke_color=ACCENT, stroke_width=2, stroke_opacity=0.5)
        self.play(FadeIn(halo), run_time=d("A12", 4.49) * 0.85)
        self.wait(d("A12", 4.49) * 0.15)

# ══════════════════════════════════════════════════════════════════════════════
# SCENE 3 — Band only  (A13 → A17 portrait)
# ══════════════════════════════════════════════════════════════════════════════

class A13_BandOnly(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        self.play(Create(axes), LaggedStartMap(FadeIn, band_dots, lag_ratio=0.02),
                  run_time=d("A13", 1.67) * 0.9)
        self.wait(d("A13", 1.67) * 0.1)

class A14_DownwardTrend(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        self.add(axes, band_dots)
        x_start = AX_X0 + 0.25; x_end = AX_X0 + AX_W - 0.25
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.25)
        y_end   = mid_y + slope * (AX_W / 2 - 0.25)
        trend = Line([x_start, y_start, 0], [x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        self.play(Create(trend), run_time=d("A14", 3.29) * 0.85)
        self.wait(d("A14", 3.29) * 0.15)

class A15_Annotation(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.25; x_end = AX_X0 + AX_W - 0.25
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.25)
        y_end   = mid_y + slope * (AX_W / 2 - 0.25)
        trend = Line([x_start, y_start, 0], [x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        self.add(axes, band_dots, trend)
        ann = ink_txt("in YOUR pool", size=22, color=INK).move_to([1.0, AX_Y0 + AX_H / 2 + 1.0, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.4, AX_Y0 + AX_H / 2 + 0.25, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.13)
        self.play(Write(ann), Create(arrow), run_time=d("A15", 3.11) * 0.85)
        self.wait(d("A15", 3.11) * 0.15)

class A16_GhostFilters(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.25; x_end = AX_X0 + AX_W - 0.25
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.25)
        y_end   = mid_y + slope * (AX_W / 2 - 0.25)
        trend = Line([x_start, y_start, 0], [x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=22, color=INK).move_to([1.0, AX_Y0 + AX_H / 2 + 1.0, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.4, AX_Y0 + AX_H / 2 + 0.25, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.13)
        self.add(axes, band_dots, trend, ann, arrow)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2,  color=RED, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.play(FadeIn(lo_cut), FadeIn(hi_cut), run_time=d("A16", 4.44) * 0.85)
        self.wait(d("A16", 4.44) * 0.15)

class A17_BerksonLabel(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.25; x_end = AX_X0 + AX_W - 0.25
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.25)
        y_end   = mid_y + slope * (AX_W / 2 - 0.25)
        trend = Line([x_start, y_start, 0], [x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=22, color=INK).move_to([1.0, AX_Y0 + AX_H / 2 + 1.0, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.4, AX_Y0 + AX_H / 2 + 0.25, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.13)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2,  color=RED, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.add(axes, band_dots, trend, ann, arrow, lo_cut, hi_cut)
        label = ink_txt("Berkson's paradox", size=30).move_to([0, AX_Y0 - 0.7, 0])
        underline = Line(label.get_left() + DOWN * 0.1,
                         label.get_right() + DOWN * 0.1,
                         color=INK, stroke_width=2)
        self.play(Write(label), Create(underline), run_time=d("A17", 2.95) * 0.85)
        self.wait(d("A17", 2.95) * 0.15)

# ══════════════════════════════════════════════════════════════════════════════
# SCENE 4 — Google trophy example  (A18 → A21 portrait)
# ══════════════════════════════════════════════════════════════════════════════

def make_trophy_portrait():
    """Trophy centred for portrait layout."""
    cup = Arc(radius=0.6, start_angle=0, angle=PI, color=INK, stroke_width=4)
    cup.move_to([0, 1.5, 0])
    cup_base = Line(cup.get_left(), cup.get_right(), color=INK, stroke_width=4)
    stem = Line([cup.get_center()[0], cup.get_bottom()[1], 0],
                [cup.get_center()[0], cup.get_bottom()[1] - 0.5, 0],
                color=INK, stroke_width=4)
    base = Line([cup.get_center()[0] - 0.45, cup.get_bottom()[1] - 0.5, 0],
                [cup.get_center()[0] + 0.45, cup.get_bottom()[1] - 0.5, 0],
                color=INK, stroke_width=5)
    brace_l = ink_txt("{ }", size=24).move_to(cup.get_center() + UP * 0.15)
    return VGroup(cup, cup_base, stem, base, brace_l)

def mini_scatter_portrait(with_trend=False, with_cut=False):
    """Small scatter below trophy in portrait layout."""
    rng = np.random.default_rng(7)
    cx, cy, w, h = 0.0, -1.2, 2.5, 1.8
    xs = rng.uniform(cx - w/2, cx + w/2, 30)
    ys = rng.uniform(cy - h/2, cy + h/2, 30)
    dots = VGroup(*[Dot([x, y, 0], radius=0.05, color=INK) for x, y in zip(xs, ys)])
    ax_x = Arrow([cx - w/2, cy - h/2, 0], [cx + w/2 + 0.1, cy - h/2, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.11)
    ax_y = Arrow([cx - w/2, cy - h/2, 0], [cx - w/2, cy + h/2 + 0.1, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.11)
    grp = VGroup(ax_x, ax_y, dots)
    if with_trend:
        trend = Line([cx - w/2 + 0.1, cy + h/2 - 0.15, 0],
                     [cx + w/2 - 0.1, cy - h/2 + 0.15, 0],
                     color=ACCENT, stroke_width=3)
        grp.add(trend)
    if with_cut:
        cut = Line([cx - w/2 + 0.1, cy - h/2 + 0.6, 0],
                   [cx + w/2 - 0.8, cy - h/2 + 0.1, 0],
                   color=RED, stroke_width=2.5)
        grp.add(cut)
    return grp

class A18_Trophy(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        trophy = make_trophy_portrait()
        lbl = ink_txt("Google", size=22).move_to([0, 0.4, 0])
        self.play(Create(trophy), Write(lbl), run_time=d("A18", 3.19) * 0.85)
        self.wait(d("A18", 3.19) * 0.15)

class A19_MiniScatter(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        trophy = make_trophy_portrait()
        lbl = ink_txt("Google", size=22).move_to([0, 0.4, 0])
        self.add(trophy, lbl)
        mini = mini_scatter_portrait(with_trend=True)
        self.play(Create(mini), run_time=d("A19", 4.41) * 0.85)
        self.wait(d("A19", 4.41) * 0.15)

class A20_MiniCut(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        trophy = make_trophy_portrait()
        lbl = ink_txt("Google", size=22).move_to([0, 0.4, 0])
        mini_base = mini_scatter_portrait(with_trend=True)
        self.add(trophy, lbl, mini_base)
        cx, cy, w, h = 0.0, -1.2, 2.5, 1.8
        cut = Line([cx - w/2 + 0.1, cy - h/2 + 0.6, 0],
                   [cx + w/2 - 0.8, cy - h/2 + 0.1, 0],
                   color=RED, stroke_width=2.5)
        self.play(Create(cut), run_time=d("A20", 3.79) * 0.85)
        self.wait(d("A20", 3.79) * 0.15)

class A21_Funnel(Scene):
    def construct(self):
        _portrait_config()
        self.add(bg())
        trophy = make_trophy_portrait()
        lbl = ink_txt("Google", size=22).move_to([0, 0.4, 0])
        mini = mini_scatter_portrait(with_trend=True, with_cut=True)
        self.add(trophy, lbl, mini)
        fx, fy = 0, -3.2
        funnel_top_l = Line([fx - 0.7, fy, 0], [fx - 0.12, fy - 0.65, 0],
                             color=INK, stroke_width=3)
        funnel_top_r = Line([fx + 0.7, fy, 0], [fx + 0.12, fy - 0.65, 0],
                             color=INK, stroke_width=3)
        funnel_bot = Line([fx - 0.12, fy - 0.65, 0], [fx + 0.12, fy - 0.65, 0],
                          color=INK, stroke_width=3)
        in_dots = VGroup(*[Dot([fx - 0.4 + 0.2 * i, fy + 0.2, 0],
                               radius=0.05, color=INK) for i in range(5)])
        out_dot = Dot([fx, fy - 0.88, 0], radius=0.05, color=ACCENT)
        funnel_grp = VGroup(funnel_top_l, funnel_top_r, funnel_bot, in_dots, out_dot)
        self.play(Create(funnel_grp), run_time=d("A21", 4.62) * 0.85)
        self.wait(d("A21", 4.62) * 0.15)
