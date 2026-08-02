"""scenes.py — claude-liam-why-hot-ones-are-jerks
Palette: claude (CREAM/INK/TERRA). Beat structure and Manim beats are
identical to why-hot-ones-are-jerks; only narration differs (Teardown register).
All A02–A21 Manim beats rendered here.
"""
import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
ACCENT = "#5A5653"
RED = "#C0392B"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', '')
except Exception:
    DUR = {}; TITLE = ''

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

# ── Axes / dot geometry ────────────────────────────────────────────────────────
AX_W, AX_H = 8.0, 5.5
AX_X0, AX_Y0 = -4.0, -2.5
BAND_WIDTH = AX_W * 0.7

def make_axes():
    x_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0 + AX_W, AX_Y0, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.2)
    y_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0, AX_Y0 + AX_H, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.2)
    return VGroup(x_axis, y_axis)

def _dot_positions(seed=42, n=120):
    rng = np.random.default_rng(seed)
    margin = 0.35
    xs = rng.uniform(AX_X0 + margin, AX_X0 + AX_W - margin, n)
    ys = rng.uniform(AX_Y0 + margin, AX_Y0 + AX_H - margin, n)
    return xs, ys

def make_dot_cloud(seed=42, n=120):
    xs, ys = _dot_positions(seed, n)
    return VGroup(*[
        Dot(point=[x, y, 0], radius=0.06, color=INK)
        for x, y in zip(xs, ys)
    ])

def make_band_dots(seed=42, n=120):
    xs, ys = _dot_positions(seed, n)
    cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
    half = BAND_WIDTH / 2
    accepted = [(x, y) for x, y in zip(xs, ys)
                if -half < (x - cx) + (y - cy) < half]
    return VGroup(*[Dot([x, y, 0], radius=0.06, color=INK) for x, y in accepted])

def make_cut_line(threshold, color=RED, stroke_w=3):
    """Diagonal line where (x-cx)+(y-cy) = threshold."""
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
# SCENE 1 — Axes buildup  A02 → A06
# ══════════════════════════════════════════════════════════════════════════════

class A01_Intro(Scene):
    def construct(self):
        self.add(bg())
        line1 = ink_txt("the more attractive,", size=40).move_to(UP * 0.6)
        line2 = terra_txt("the meaner.", size=40).move_to(DOWN * 0.1)
        line3 = ink_txt("— a pattern that feels true", size=26, color=ACCENT).move_to(DOWN * 0.85)
        self.play(FadeIn(line1), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(line2), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(line3), run_time=0.45)
        self.wait(d("A01") - 2.05)


class A02_Axes(Scene):
    def construct(self):
        self.add(bg())
        self.play(Create(make_axes()), run_time=d("A02", 3.33) * 0.85)
        self.wait(d("A02", 3.33) * 0.15)


class A03_XLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        self.add(axes)
        lbl = ink_txt("attractive →", size=30).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        self.play(Write(lbl), run_time=d("A03", 3.01) * 0.85)
        self.wait(d("A03", 3.01) * 0.15)


class A04_YLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=30).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        self.add(axes, x_lbl)
        y_lbl = ink_txt("nice ↑", size=30).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        self.play(Write(y_lbl), run_time=d("A04", 2.6) * 0.85)
        self.wait(d("A04", 2.6) * 0.15)


class A05_DotCloud(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=30).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        y_lbl = ink_txt("nice ↑", size=30).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        self.add(axes, x_lbl, y_lbl)
        dots = make_dot_cloud()
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.015),
                  run_time=d("A05", 4.22) * 0.85)
        self.wait(d("A05", 4.22) * 0.15)


class A06_FlatTrend(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=30).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        y_lbl = ink_txt("nice ↑", size=30).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        dots = make_dot_cloud()
        self.add(axes, x_lbl, y_lbl, dots)
        mid_y = AX_Y0 + AX_H / 2
        flat = Line([AX_X0 + 0.2, mid_y, 0], [AX_X0 + AX_W - 0.2, mid_y, 0],
                    color=TERRA, stroke_width=4)
        self.play(Create(flat), run_time=d("A06", 4.78) * 0.85)
        self.wait(d("A06", 4.78) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 2 — Cuts  A07 → A12
# ══════════════════════════════════════════════════════════════════════════════

class A07_CloudAgain(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        self.play(Create(axes),
                  LaggedStartMap(FadeIn, dots, lag_ratio=0.01),
                  Write(lbl), run_time=d("A07", 3.33) * 0.9)
        self.wait(d("A07", 3.33) * 0.1)


class A08_LowerCut(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        self.add(axes, dots, lbl)
        lo_cut = make_cut_line(-BAND_WIDTH / 2)
        self.play(Create(lo_cut), run_time=d("A08", 3.37) * 0.85)
        self.wait(d("A08", 3.37) * 0.15)


class A09_FadeLoLeft(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); all_dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2)
        self.add(axes, all_dots, lbl, lo_cut)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        anims = [dot.animate.set_opacity(0.12).set_color(RED)
                 for dot in all_dots
                 if (dot.get_center()[0] - cx) + (dot.get_center()[1] - cy) < -BAND_WIDTH / 2]
        if anims:
            self.play(*anims, run_time=d("A09", 3.09) * 0.85)
        self.wait(d("A09", 3.09) * 0.15)


class A10_UpperCut(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); all_dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            if (dot.get_center()[0] - cx) + (dot.get_center()[1] - cy) < -BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, lbl, lo_cut)
        hi_cut = make_cut_line(BAND_WIDTH / 2)
        self.play(Create(hi_cut), run_time=d("A10", 4.67) * 0.85)
        self.wait(d("A10", 4.67) * 0.15)


class A11_FadeUpRight(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); all_dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2)
        hi_cut = make_cut_line(BAND_WIDTH / 2)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            if (dot.get_center()[0] - cx) + (dot.get_center()[1] - cy) < -BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, lbl, lo_cut, hi_cut)
        anims = [dot.animate.set_opacity(0.12).set_color(RED)
                 for dot in all_dots
                 if (dot.get_center()[0] - cx) + (dot.get_center()[1] - cy) > BAND_WIDTH / 2]
        if anims:
            self.play(*anims, run_time=d("A11", 2.92) * 0.85)
        self.wait(d("A11", 2.92) * 0.15)


class A12_BandHalo(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); all_dots = make_dot_cloud()
        lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2)
        hi_cut = make_cut_line(BAND_WIDTH / 2)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            s = (dot.get_center()[0] - cx) + (dot.get_center()[1] - cy)
            if s < -BAND_WIDTH / 2 or s > BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, lbl, lo_cut, hi_cut)
        bw = BAND_WIDTH / 2
        halo_pts = [
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 + bw - AX_W / 2 + 0.3, 0],
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 - bw - AX_W / 2 + 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 - bw + AX_W / 2 - 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 + bw + AX_W / 2 - 0.3, 0],
        ]
        halo = Polygon(*halo_pts,
                       fill_color=TERRA, fill_opacity=0.15,
                       stroke_color=TERRA, stroke_width=2, stroke_opacity=0.5)
        self.play(FadeIn(halo), run_time=d("A12", 5.08) * 0.85)
        self.wait(d("A12", 5.08) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 3 — Band only  A13 → A17
# ══════════════════════════════════════════════════════════════════════════════

class A13_BandOnly(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        self.play(Create(axes),
                  LaggedStartMap(FadeIn, band_dots, lag_ratio=0.02),
                  run_time=d("A13", 2.22) * 0.9)
        self.wait(d("A13", 2.22) * 0.1)


class A14_DownwardTrend(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); band_dots = make_band_dots()
        self.add(axes, band_dots)
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        x_s = AX_X0 + 0.3; x_e = AX_X0 + AX_W - 0.3
        y_s = mid_y - slope * (AX_W / 2 - 0.3)
        y_e = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line([x_s, y_s, 0], [x_e, y_e, 0], color=TERRA, stroke_width=5)
        self.play(Create(trend), run_time=d("A14", 3.9) * 0.85)
        self.wait(d("A14", 3.9) * 0.15)


class A15_Annotation(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); band_dots = make_band_dots()
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        x_s = AX_X0 + 0.3; x_e = AX_X0 + AX_W - 0.3
        y_s = mid_y - slope * (AX_W / 2 - 0.3)
        y_e = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line([x_s, y_s, 0], [x_e, y_e, 0], color=TERRA, stroke_width=5)
        self.add(axes, band_dots, trend)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(ann.get_bottom() + DOWN * 0.05,
                      [0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        self.play(Write(ann), Create(arrow), run_time=d("A15", 3.52) * 0.85)
        self.wait(d("A15", 3.52) * 0.15)


class A16_GhostFilters(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); band_dots = make_band_dots()
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        x_s = AX_X0 + 0.3; x_e = AX_X0 + AX_W - 0.3
        y_s = mid_y - slope * (AX_W / 2 - 0.3)
        y_e = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line([x_s, y_s, 0], [x_e, y_e, 0], color=TERRA, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(ann.get_bottom() + DOWN * 0.05,
                      [0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        self.add(axes, band_dots, trend, ann, arrow)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.play(FadeIn(lo_cut), FadeIn(hi_cut), run_time=d("A16", 4.99) * 0.85)
        self.wait(d("A16", 4.99) * 0.15)


class A17_BerksonLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes(); band_dots = make_band_dots()
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        x_s = AX_X0 + 0.3; x_e = AX_X0 + AX_W - 0.3
        y_s = mid_y - slope * (AX_W / 2 - 0.3)
        y_e = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line([x_s, y_s, 0], [x_e, y_e, 0], color=TERRA, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(ann.get_bottom() + DOWN * 0.05,
                      [0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.add(axes, band_dots, trend, ann, arrow, lo_cut, hi_cut)
        label = ink_txt("Berkson's paradox", size=38).move_to([0, AX_Y0 - 0.85, 0])
        uline = Line(label.get_left() + DOWN * 0.1, label.get_right() + DOWN * 0.1,
                     color=INK, stroke_width=2)
        self.play(Write(label), Create(uline), run_time=d("A17", 3.58) * 0.85)
        self.wait(d("A17", 3.58) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 4 — Google example  A18 → A21
# ══════════════════════════════════════════════════════════════════════════════

def make_trophy():
    cup = Arc(radius=0.7, start_angle=0, angle=PI, color=INK, stroke_width=4)
    cup.move_to([-2.5, 0.5, 0])
    cup_base = Line(cup.get_left(), cup.get_right(), color=INK, stroke_width=4)
    stem = Line([cup.get_center()[0], cup.get_bottom()[1], 0],
                [cup.get_center()[0], cup.get_bottom()[1] - 0.6, 0],
                color=INK, stroke_width=4)
    base = Line([cup.get_center()[0] - 0.5, cup.get_bottom()[1] - 0.6, 0],
                [cup.get_center()[0] + 0.5, cup.get_bottom()[1] - 0.6, 0],
                color=INK, stroke_width=5)
    brace = ink_txt("{ }", size=28).move_to(cup.get_center() + UP * 0.2)
    return VGroup(cup, cup_base, stem, base, brace)


def mini_scatter(with_trend=False, with_cut=False):
    rng = np.random.default_rng(7)
    cx, cy, w, h = 2.0, 0.0, 2.8, 2.0
    xs = rng.uniform(cx - w/2, cx + w/2, 40)
    ys = rng.uniform(cy - h/2, cy + h/2, 40)
    dots = VGroup(*[Dot([x, y, 0], radius=0.05, color=INK) for x, y in zip(xs, ys)])
    ax_x = Arrow([cx - w/2, cy - h/2, 0], [cx + w/2 + 0.1, cy - h/2, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.12)
    ax_y = Arrow([cx - w/2, cy - h/2, 0], [cx - w/2, cy + h/2 + 0.1, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.12)
    grp = VGroup(ax_x, ax_y, dots)
    if with_trend:
        trend = Line([cx - w/2 + 0.1, cy + h/2 - 0.15, 0],
                     [cx + w/2 - 0.1, cy - h/2 + 0.15, 0],
                     color=TERRA, stroke_width=3)
        grp.add(trend)
    if with_cut:
        cut = Line([cx - w/2 + 0.1, cy - h/2 + 0.7, 0],
                   [cx + w/2 - 0.9, cy - h/2 + 0.1, 0],
                   color=RED, stroke_width=2.5)
        grp.add(cut)
    return grp


class A18_Trophy(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        self.play(Create(trophy), Write(lbl), run_time=d("A18", 3.65) * 0.85)
        self.wait(d("A18", 3.65) * 0.15)


class A19_MiniScatter(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        self.add(trophy, lbl)
        ms = mini_scatter(with_trend=True)
        self.play(Create(ms), run_time=d("A19", 5.4) * 0.85)
        self.wait(d("A19", 5.4) * 0.15)


class A20_MiniCut(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        self.add(trophy, lbl, mini_scatter(with_trend=True))
        cx, cy, w, h = 2.0, 0.0, 2.8, 2.0
        cut = Line([cx - w/2 + 0.1, cy - h/2 + 0.7, 0],
                   [cx + w/2 - 0.9, cy - h/2 + 0.1, 0],
                   color=RED, stroke_width=2.5)
        self.play(Create(cut), run_time=d("A20", 4.31) * 0.85)
        self.wait(d("A20", 4.31) * 0.15)


class A21_Funnel(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        ms = mini_scatter(with_trend=True, with_cut=True)
        self.add(trophy, lbl, ms)
        fx, fy = -2.5, -2.1
        funnel = VGroup(
            Line([fx - 0.8, fy, 0], [fx - 0.15, fy - 0.7, 0], color=INK, stroke_width=3),
            Line([fx + 0.8, fy, 0], [fx + 0.15, fy - 0.7, 0], color=INK, stroke_width=3),
            Line([fx - 0.15, fy - 0.7, 0], [fx + 0.15, fy - 0.7, 0], color=INK, stroke_width=3),
            *[Dot([fx - 0.5 + 0.3 * i, fy + 0.2, 0], radius=0.055, color=INK) for i in range(5)],
            Dot([fx, fy - 0.95, 0], radius=0.055, color=TERRA),
        )
        self.play(Create(funnel), run_time=d("A21", 4.95) * 0.85)
        self.wait(d("A21", 4.95) * 0.15)


class A22_Conclusion(Scene):
    def construct(self):
        self.add(bg())
        ask_lbl = ink_txt("Ask:", size=36, color=ACCENT).move_to(UP * 1.2)
        q_lbl = ink_txt('"Who got filtered out?"', size=44, weight=BOLD).move_to(ORIGIN)
        bias_lbl = terra_txt("— Berkson's bias", size=28).move_to(DOWN * 0.9)
        self.play(FadeIn(ask_lbl), run_time=0.4)
        self.play(FadeIn(q_lbl), run_time=0.5)
        self.play(FadeIn(bias_lbl), run_time=0.4)
        self.wait(d("A22") - 1.3)
