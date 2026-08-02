import json
import numpy as np
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
ACCENT = "#5A5653"  # warm slate accent from beat_sheet
RED = "#C0392B"    # forbidden_color used as cutoff lines
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

# ── Shared helpers ─────────────────────────────────────────────────────────────

# Axes extent in scene units (mapped to a 10×6 region centred at origin)
AX_W, AX_H = 8.0, 5.5
AX_X0, AX_Y0 = -4.0, -2.5   # bottom-left corner of the axes box

def make_axes():
    """Return the two axis lines + arrowheads."""
    x_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0 + AX_W, AX_Y0, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.2)
    y_axis = Arrow(start=[AX_X0, AX_Y0, 0], end=[AX_X0, AX_Y0 + AX_H, 0],
                   color=INK, stroke_width=3, buff=0, tip_length=0.2)
    return VGroup(x_axis, y_axis)

def _dot_positions(seed=42, n=120):
    """Reproducible uncorrelated cloud.  Returns (xs, ys) in scene units."""
    rng = np.random.default_rng(seed)
    margin = 0.35
    xs = rng.uniform(AX_X0 + margin, AX_X0 + AX_W - margin, n)
    ys = rng.uniform(AX_Y0 + margin, AX_Y0 + AX_H - margin, n)
    return xs, ys

# Berkson band filter: a point (x, y) is *accepted* iff
#   x + y  > threshold_lo  (below-left cut removed)
#   x + y  < threshold_hi  (above-right cut removed)
# We choose thresholds so roughly ⅓ of dots survive.
BAND_LO = (AX_X0 + AX_X0 + AX_W) / 2 - 0.5   # sum of coords threshold low
BAND_HI = (AX_X0 + AX_X0 + AX_W) / 2 + 0.5   # sum of coords threshold high

# Diagonal cut lines in scene coords:
# Lower-left cut: x + y = BAND_LO  (anything below this removed)
# Upper-right cut: x + y = BAND_HI (anything above this removed)
def _cut_endpoints(threshold):
    """Return (start, end) world coords of the diagonal x+y = threshold."""
    x0, y0 = AX_X0, threshold - AX_X0
    x1, y1 = threshold - AX_Y0, AX_Y0
    # clamp to axis box
    x0 = np.clip(x0, AX_X0, AX_X0 + AX_W)
    y0 = np.clip(threshold - x0, AX_Y0, AX_Y0 + AX_H)
    x1 = np.clip(x1, AX_X0, AX_X0 + AX_W)
    y1 = np.clip(threshold - x1, AX_Y0, AX_Y0 + AX_H)
    return [x0, y0, 0], [x1, y1, 0]

def make_dot_cloud(seed=42, n=120, color=INK, opacity=1.0):
    xs, ys = _dot_positions(seed, n)
    dots = VGroup(*[
        Dot(point=[x, y, 0], radius=0.06, color=color).set_opacity(opacity)
        for x, y in zip(xs, ys)
    ])
    return dots

def make_band_dots(seed=42, n=120):
    """Only the dots that survive both Berkson cuts."""
    xs, ys = _dot_positions(seed, n)
    band_thresh = (AX_X0 + AX_X0 + AX_W) / 2  # midpoint of total x range
    # Use sum x+y relative to the centre of the plot
    cx = AX_X0 + AX_W / 2
    cy = AX_Y0 + AX_H / 2
    half = AX_W * 0.45  # half-width of the surviving band in (x+y) space
    accepted = [(x, y) for x, y in zip(xs, ys)
                if -half < (x - cx) + (y - cy) < half]
    dots = VGroup(*[
        Dot(point=[x, y, 0], radius=0.06, color=INK)
        for x, y in accepted
    ])
    return dots

def make_cut_line(threshold, color=RED, stroke_w=3):
    """Diagonal cutoff line for x+y = threshold (in centred coords)."""
    cx = AX_X0 + AX_W / 2
    cy = AX_Y0 + AX_H / 2
    # In (u,v)=(x-cx, y-cy) space: u+v = threshold; map back
    # At u = -AX_W/2: v = threshold + AX_W/2, so y = cy + threshold + AX_W/2
    # Clamp
    x0 = AX_X0
    y0_raw = cy + threshold - (x0 - cx)
    y0 = np.clip(y0_raw, AX_Y0, AX_Y0 + AX_H)
    # Solve for x when y hits boundary
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
    return Line(start=[x0, y0, 0], end=[x1, y1, 0],
                color=color, stroke_width=stroke_w)

# Band thresholds (centred coords): -bw/2 < u+v < bw/2
BAND_WIDTH = AX_W * 0.7


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 1 — Axes buildup  (A02 → A06)
# ══════════════════════════════════════════════════════════════════════════════

class A02_Axes(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        self.play(Create(axes), run_time=d("A02", 2.64) * 0.8)
        self.wait(d("A02", 2.64) * 0.2)


class A03_XLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        self.add(axes)
        x_lbl = ink_txt("attractive →", size=44).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        self.play(Write(x_lbl), run_time=d("A03", 2.12) * 0.85)
        self.wait(d("A03", 2.12) * 0.15)


class A04_YLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=44).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        self.add(axes, x_lbl)
        y_lbl = ink_txt("nice ↑", size=44).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        self.play(Write(y_lbl), run_time=d("A04", 2.04) * 0.85)
        self.wait(d("A04", 2.04) * 0.15)


class A05_DotCloud(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=44).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        y_lbl = ink_txt("nice ↑", size=44).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        self.add(axes, x_lbl, y_lbl)
        dots = make_dot_cloud()
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.015),
                  run_time=d("A05", 3.29) * 0.85)
        self.wait(d("A05", 3.29) * 0.15)


class A06_FlatTrendLine(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        x_lbl = ink_txt("attractive →", size=44).next_to(
            [AX_X0 + AX_W, AX_Y0, 0], DOWN, buff=0.1)
        y_lbl = ink_txt("nice ↑", size=44).rotate(PI / 2).next_to(
            [AX_X0, AX_Y0 + AX_H, 0], LEFT, buff=0.1)
        dots = make_dot_cloud()
        self.add(axes, x_lbl, y_lbl, dots)
        # Flat trend line at mid-height of the axes box
        mid_y = AX_Y0 + AX_H / 2
        flat = Line(start=[AX_X0 + 0.2, mid_y, 0],
                    end=[AX_X0 + AX_W - 0.2, mid_y, 0],
                    color=ACCENT, stroke_width=4)
        self.play(Create(flat), run_time=d("A06", 4.08) * 0.85)
        self.wait(d("A06", 4.08) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 2 — Dating pool + cuts  (A07 → A12)
# ══════════════════════════════════════════════════════════════════════════════

def _scene2_base():
    """axes + full dot cloud, no labels."""
    axes = make_axes()
    dots = make_dot_cloud()
    return axes, dots

class A07_CloudAgain(Scene):
    def construct(self):
        self.add(bg())
        axes, dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        self.play(Create(axes), LaggedStartMap(FadeIn, dots, lag_ratio=0.01),
                  Write(pool_lbl), run_time=d("A07", 2.93) * 0.9)
        self.wait(d("A07", 2.93) * 0.1)


class A08_LowerCut(Scene):
    def construct(self):
        self.add(bg())
        axes, dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        self.add(axes, dots, pool_lbl)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        self.play(Create(lo_cut), run_time=d("A08", 2.53) * 0.85)
        self.wait(d("A08", 2.53) * 0.15)


class A09_FadeLoLeft(Scene):
    def construct(self):
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        self.add(axes, all_dots, pool_lbl, lo_cut)
        # Fade dots below the lower cut
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
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        # Apply lower fade
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
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
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
        self.add(bg())
        axes, all_dots = _scene2_base()
        pool_lbl = ink_txt("your dating pool", size=28).move_to([0, AX_Y0 + AX_H + 0.4, 0])
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED)
        cx = AX_X0 + AX_W / 2; cy = AX_Y0 + AX_H / 2
        for dot in all_dots:
            p = dot.get_center()
            s = (p[0] - cx) + (p[1] - cy)
            if s < -BAND_WIDTH / 2 or s > BAND_WIDTH / 2:
                dot.set_opacity(0.12).set_color(RED)
        self.add(axes, all_dots, pool_lbl, lo_cut, hi_cut)
        # Halo: a parallelogram band highlight
        bw = BAND_WIDTH / 2
        halo_pts = [
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 + bw - AX_W / 2 + 0.3, 0],
            [AX_X0 + AX_W, AX_Y0 + AX_H / 2 - bw - AX_W / 2 + 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 - bw + AX_W / 2 - 0.3, 0],
            [AX_X0, AX_Y0 + AX_H / 2 + bw + AX_W / 2 - 0.3, 0],
        ]
        halo = Polygon(*halo_pts,
                       fill_color=ACCENT, fill_opacity=0.18,
                       stroke_color=ACCENT, stroke_width=2, stroke_opacity=0.5)
        self.play(FadeIn(halo), run_time=d("A12", 4.49) * 0.85)
        self.wait(d("A12", 4.49) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 3 — Band only  (A13 → A17)
# ══════════════════════════════════════════════════════════════════════════════

class A13_BandOnly(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        self.play(Create(axes),
                  LaggedStartMap(FadeIn, band_dots, lag_ratio=0.02),
                  run_time=d("A13", 1.67) * 0.9)
        self.wait(d("A13", 1.67) * 0.1)


class A14_DownwardTrend(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        self.add(axes, band_dots)
        # Downward trend line across the band
        x_start = AX_X0 + 0.3
        x_end = AX_X0 + AX_W - 0.3
        mid_y = AX_Y0 + AX_H / 2
        slope = -0.7   # negative slope showing correlation
        y_start = mid_y - slope * (AX_W / 2 - 0.3)
        y_end = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line(start=[x_start, y_start, 0], end=[x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        self.play(Create(trend), run_time=d("A14", 3.29) * 0.85)
        self.wait(d("A14", 3.29) * 0.15)


class A15_Annotation(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.3; x_end = AX_X0 + AX_W - 0.3
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.3)
        y_end = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line(start=[x_start, y_start, 0], end=[x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        self.add(axes, band_dots, trend)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        self.play(Write(ann), Create(arrow), run_time=d("A15", 3.11) * 0.85)
        self.wait(d("A15", 3.11) * 0.15)


class A16_GhostFilters(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.3; x_end = AX_X0 + AX_W - 0.3
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.3)
        y_end = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line(start=[x_start, y_start, 0], end=[x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        self.add(axes, band_dots, trend, ann, arrow)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.play(FadeIn(lo_cut), FadeIn(hi_cut), run_time=d("A16", 4.44) * 0.85)
        self.wait(d("A16", 4.44) * 0.15)


class A17_BerksonLabel(Scene):
    def construct(self):
        self.add(bg())
        axes = make_axes()
        band_dots = make_band_dots()
        x_start = AX_X0 + 0.3; x_end = AX_X0 + AX_W - 0.3
        mid_y = AX_Y0 + AX_H / 2; slope = -0.7
        y_start = mid_y - slope * (AX_W / 2 - 0.3)
        y_end = mid_y + slope * (AX_W / 2 - 0.3)
        trend = Line(start=[x_start, y_start, 0], end=[x_end, y_end, 0],
                     color=ACCENT, stroke_width=5)
        ann = ink_txt("in YOUR pool", size=28, slant=ITALIC).move_to([1.8, AX_Y0 + AX_H / 2 + 1.1, 0])
        arrow = Arrow(start=ann.get_bottom() + DOWN * 0.05,
                      end=[0.8, AX_Y0 + AX_H / 2 + 0.3, 0],
                      color=INK, stroke_width=2, buff=0.05, tip_length=0.15)
        lo_cut = make_cut_line(-BAND_WIDTH / 2, color=RED, stroke_w=2)
        hi_cut = make_cut_line(BAND_WIDTH / 2, color=RED, stroke_w=2)
        lo_cut.set_opacity(0.4); hi_cut.set_opacity(0.4)
        self.add(axes, band_dots, trend, ann, arrow, lo_cut, hi_cut)
        label = ink_txt("Berkson's paradox", size=38).move_to([0, AX_Y0 - 0.85, 0])
        underline = Line(label.get_left() + DOWN * 0.1,
                         label.get_right() + DOWN * 0.1,
                         color=INK, stroke_width=2)
        self.play(Write(label), Create(underline), run_time=d("A17", 2.95) * 0.85)
        self.wait(d("A17", 2.95) * 0.15)


# ══════════════════════════════════════════════════════════════════════════════
# SCENE 4 — Google trophy example  (A18 → A21)
# ══════════════════════════════════════════════════════════════════════════════

def make_trophy():
    """Simple Manim trophy: cup + base + code brackets."""
    cup = Arc(radius=0.7, start_angle=0, angle=PI,
              color=INK, stroke_width=4)
    cup.move_to([-2.5, 0.5, 0])
    # Cup bottom line
    cup_base = Line(cup.get_left(), cup.get_right(), color=INK, stroke_width=4)
    # Stem
    stem = Line([cup.get_center()[0], cup.get_bottom()[1], 0],
                [cup.get_center()[0], cup.get_bottom()[1] - 0.6, 0],
                color=INK, stroke_width=4)
    # Base plate
    base = Line([cup.get_center()[0] - 0.5, cup.get_bottom()[1] - 0.6, 0],
                [cup.get_center()[0] + 0.5, cup.get_bottom()[1] - 0.6, 0],
                color=INK, stroke_width=5)
    # Code brackets inside cup
    brace_l = ink_txt("{ }", size=28).move_to(cup.get_center() + UP * 0.2)
    return VGroup(cup, cup_base, stem, base, brace_l)


def mini_scatter_group(with_trend=False, with_cut=False):
    """Small scatter beside the trophy, right side of frame."""
    rng = np.random.default_rng(7)
    # Mini scatter in a small box around (2.0, 0.0)
    cx, cy, w, h = 2.0, 0.0, 2.8, 2.0
    xs = rng.uniform(cx - w/2, cx + w/2, 40)
    ys = rng.uniform(cy - h/2, cy + h/2, 40)
    dots = VGroup(*[Dot([x, y, 0], radius=0.05, color=INK) for x, y in zip(xs, ys)])
    # Mini axes
    ax_x = Arrow([cx - w/2, cy - h/2, 0], [cx + w/2 + 0.1, cy - h/2, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.12)
    ax_y = Arrow([cx - w/2, cy - h/2, 0], [cx - w/2, cy + h/2 + 0.1, 0],
                 color=INK, stroke_width=2, buff=0, tip_length=0.12)
    grp = VGroup(ax_x, ax_y, dots)
    if with_trend:
        trend = Line([cx - w/2 + 0.1, cy + h/2 - 0.15, 0],
                     [cx + w/2 - 0.1, cy - h/2 + 0.15, 0],
                     color=ACCENT, stroke_width=3)
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
        self.play(Create(trophy), Write(lbl), run_time=d("A18", 3.19) * 0.85)
        self.wait(d("A18", 3.19) * 0.15)


class A19_MiniScatter(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        self.add(trophy, lbl)
        mini = mini_scatter_group(with_trend=True)
        self.play(Create(mini), run_time=d("A19", 4.41) * 0.85)
        self.wait(d("A19", 4.41) * 0.15)


class A20_MiniCut(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        mini_base = mini_scatter_group(with_trend=True)
        self.add(trophy, lbl, mini_base)
        # Add only the cut line
        cx, cy, w, h = 2.0, 0.0, 2.8, 2.0
        cut = Line([cx - w/2 + 0.1, cy - h/2 + 0.7, 0],
                   [cx + w/2 - 0.9, cy - h/2 + 0.1, 0],
                   color=RED, stroke_width=2.5)
        self.play(Create(cut), run_time=d("A20", 3.79) * 0.85)
        self.wait(d("A20", 3.79) * 0.15)


class A21_Funnel(Scene):
    def construct(self):
        self.add(bg())
        trophy = make_trophy()
        lbl = ink_txt("Google", size=26).move_to([-2.5, -1.6, 0])
        mini = mini_scatter_group(with_trend=True, with_cut=True)
        self.add(trophy, lbl, mini)
        # Funnel below trophy: centred at (-2.5, -2.2)
        fx, fy = -2.5, -2.1
        funnel_top_l = Line([fx - 0.8, fy, 0], [fx - 0.15, fy - 0.7, 0],
                             color=INK, stroke_width=3)
        funnel_top_r = Line([fx + 0.8, fy, 0], [fx + 0.15, fy - 0.7, 0],
                             color=INK, stroke_width=3)
        funnel_bot = Line([fx - 0.15, fy - 0.7, 0], [fx + 0.15, fy - 0.7, 0],
                          color=INK, stroke_width=3)
        # A few dots entering the top
        in_dots = VGroup(*[Dot([fx - 0.5 + 0.3 * i, fy + 0.2, 0],
                               radius=0.055, color=INK) for i in range(5)])
        out_dot = Dot([fx, fy - 0.95, 0], radius=0.055, color=ACCENT)
        funnel_grp = VGroup(funnel_top_l, funnel_top_r, funnel_bot, in_dots, out_dot)
        self.play(Create(funnel_grp), run_time=d("A21", 4.62) * 0.85)
        self.wait(d("A21", 4.62) * 0.15)
