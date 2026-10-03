"""scenes_std.py — GRAPHIC beats for claude-liam-vox-emitter-range.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Scenes: B02_AlphaIntro, B03_BetaIntro, B05_EmitterRanges, B06_Crossfire,
        B07_TumorGeometry, B08_AlphaFail, B09_BetaWin, B11_Example

Render each scene:
  manim -qh --fps 24 scenes_std.py B02_AlphaIntro
  mv media/videos/scenes_std/1080p24/B02_AlphaIntro.mp4 manim/B02.mp4
  (repeat for each scene)

Or use the batch script at the bottom of this file:
  python3 scenes_std.py
"""
import json
import os
import pathlib
import subprocess
import sys

from manim import *

# ── Palette (newsprint — matches beat_sheet color_semantics) ────────────────
GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"   # beta / crossfire / correct geometry match
CRIMSON  = "#BF3339"   # alpha / confined / geometry mismatch
GOLD     = "#F5D061"   # highlight fill only — never text
SLATE    = "#3E5559"   # structural / neutral cell fill
HAIRLINE = "#D4D4D4"

# Font roles (EB Garamond editorial register)
DISPLAY = "Montserrat"
SERIF   = "EB Garamond"
MONO    = "PT Mono"

# ── Duration loader ──────────────────────────────────────────────────────────
_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 15)}


# ── Minimal helpers ──────────────────────────────────────────────────────────
class SerifLabel(VGroup):
    """Italic serif text with a terracotta accent underline (optional)."""
    def __init__(self, text, accent=TEAL, size=18, underline=False):
        super().__init__()
        t = Text(text, font=SERIF, color=INK, font_size=int(size * 1.15), slant=ITALIC)
        self.add(t)
        if underline:
            u = Line(t.get_corner(DL) + DOWN * 0.05,
                     t.get_corner(DR) + DOWN * 0.05,
                     color=accent, stroke_width=1.2)
            self.add(u)


class LabelChip(VGroup):
    """Small pill label: colored rectangle + white uppercase text."""
    def __init__(self, text, accent=CRIMSON, size=15):
        super().__init__()
        t = Text(text.upper(), font=DISPLAY, color=WHITE, font_size=int(size))
        bg = Rectangle(width=t.width + 0.25, height=t.height + 0.15)
        bg.set_fill(accent, 0.9).set_stroke(width=0, opacity=0)
        bg.move_to(t)
        self.add(bg, t)


def _bg(scene):
    """Apply cream ground to a scene's camera."""
    scene.camera.background_color = GROUND


# ── B02  Alpha particle introduction ────────────────────────────────────────
class B02_AlphaIntro(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B02", 10.65)
        cell = Circle(0.4).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        cell.move_to(LEFT * 3.0 + UP * 0.2)
        track = Line(cell.get_right(), cell.get_right() + RIGHT * 0.6,
                     color=CRIMSON, stroke_width=7)
        lbl_top = Text("Alpha particle", font=DISPLAY, color=CRIMSON,
                       font_size=22, weight=BOLD)
        lbl_top.move_to(LEFT * 3.0 + UP * 1.4)
        lbl_range = Text("range: 0.05 - 0.1 mm", font=MONO, font_size=16, color=CRIMSON)
        lbl_range.move_to(LEFT * 3.0 + DOWN * 1.1)
        lbl_let = Text("High LET  |  dense damage", font=DISPLAY, font_size=16, color=INK)
        lbl_let.move_to(LEFT * 3.0 + DOWN * 1.55)
        bound_dot = Dot(radius=0.1, color=CRIMSON).move_to(cell.get_center())
        self.play(GrowFromCenter(cell), run_time=0.5)
        self.play(GrowFromCenter(bound_dot), run_time=0.3)
        self.play(Create(track), run_time=0.6)
        self.play(FadeIn(lbl_top), run_time=0.4)
        self.play(FadeIn(lbl_range), FadeIn(lbl_let), run_time=0.5)
        self.wait(max(0.3, total - 2.3))


# ── B03  Beta particle introduction ─────────────────────────────────────────
class B03_BetaIntro(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B03", 10.20)
        cell = Circle(0.4).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        cell.move_to(LEFT * 3.5 + UP * 0.2)
        track = Line(cell.get_right(), cell.get_right() + RIGHT * 3.0,
                     color=TEAL, stroke_width=2.5)
        nb1 = Circle(0.3).set_fill(TEAL, 0.18).set_stroke(TEAL, 1.0)
        nb1.move_to(LEFT * 1.5 + UP * 0.2)
        nb2 = Circle(0.3).set_fill(TEAL, 0.12).set_stroke(TEAL, 0.7)
        nb2.move_to(LEFT * 0.2 + UP * 0.2)
        lbl_top = Text("Beta particle", font=DISPLAY, color=TEAL,
                       font_size=22, weight=BOLD)
        lbl_top.move_to(LEFT * 1.5 + UP * 1.4)
        lbl_range = Text("range: 1 - 2 mm", font=MONO, font_size=16, color=TEAL)
        lbl_range.move_to(LEFT * 1.5 + DOWN * 1.1)
        lbl_let = Text("Low LET  |  sparse damage", font=DISPLAY, font_size=16, color=INK)
        lbl_let.move_to(LEFT * 1.5 + DOWN * 1.55)
        bound_dot = Dot(radius=0.1, color=TEAL).move_to(cell.get_center())
        self.play(GrowFromCenter(cell), run_time=0.5)
        self.play(GrowFromCenter(bound_dot), run_time=0.3)
        self.play(Create(track), run_time=0.8)
        self.play(GrowFromCenter(nb1), GrowFromCenter(nb2), run_time=0.5)
        self.play(FadeIn(lbl_top), run_time=0.4)
        self.play(FadeIn(lbl_range), FadeIn(lbl_let), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ── B05  Emitter range split panel ──────────────────────────────────────────
class B05_EmitterRanges(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 11.01)
        title = Text("Emitter range determines crossfire", font=DISPLAY,
                     font_size=20, color=INK).move_to(UP * 3.2)
        # Alpha panel (LEFT)
        alpha_cell = Circle(0.38).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        alpha_cell.move_to(LEFT * 3.8 + UP * 0.4)
        alpha_bound = Dot(radius=0.09, color=CRIMSON).move_to(alpha_cell.get_center())
        alpha_track = Line(alpha_cell.get_right(),
                           alpha_cell.get_right() + RIGHT * 0.55,
                           color=CRIMSON, stroke_width=6)
        alpha_dash = DashedLine(
            alpha_cell.get_right() + RIGHT * 0.55 + UP * 0.5,
            alpha_cell.get_right() + RIGHT * 0.55 + DOWN * 0.5,
            color=CRIMSON, stroke_width=1.5, dash_length=0.08)
        alpha_lbl = Text("Alpha", font=DISPLAY, font_size=18, color=CRIMSON, weight=BOLD)
        alpha_lbl.move_to(LEFT * 3.8 + DOWN * 1.0)
        alpha_range = Text("0.05 - 0.1 mm", font=MONO, font_size=13, color=CRIMSON)
        alpha_range.move_to(LEFT * 3.8 + DOWN * 1.45)
        alpha_nb = Circle(0.3).set_fill(SLATE, 0.15).set_stroke(SLATE, 0.5)
        alpha_nb.move_to(LEFT * 2.5 + UP * 0.4)
        # Beta panel (RIGHT)
        beta_cell = Circle(0.38).set_fill(SLATE, 0.85).set_stroke(INK, 1.5)
        beta_cell.move_to(RIGHT * 1.2 + UP * 0.4)
        beta_bound = Dot(radius=0.09, color=TEAL).move_to(beta_cell.get_center())
        beta_track = Line(beta_cell.get_right(),
                          beta_cell.get_right() + RIGHT * 2.6,
                          color=TEAL, stroke_width=2.5)
        beta_dash = DashedLine(
            beta_cell.get_right() + RIGHT * 2.6 + UP * 0.5,
            beta_cell.get_right() + RIGHT * 2.6 + DOWN * 0.5,
            color=TEAL, stroke_width=1.5, dash_length=0.08)
        beta_nb1 = Circle(0.32).set_fill(TEAL, 0.20).set_stroke(TEAL, 1.2)
        beta_nb1.move_to(RIGHT * 2.6 + UP * 0.4)
        beta_nb2 = Circle(0.32).set_fill(TEAL, 0.13).set_stroke(TEAL, 0.8)
        beta_nb2.move_to(RIGHT * 3.5 + UP * 0.4)
        beta_lbl = Text("Beta", font=DISPLAY, font_size=18, color=TEAL, weight=BOLD)
        beta_lbl.move_to(RIGHT * 2.5 + DOWN * 1.0)
        beta_range = Text("1 - 2 mm", font=MONO, font_size=13, color=TEAL)
        beta_range.move_to(RIGHT * 2.5 + DOWN * 1.45)
        divider = Line(UP * 3.0, DOWN * 2.5, color=INK, stroke_width=0.8)
        divider.move_to(LEFT * 0.5 + UP * 0.25)
        gold_bar = Rectangle(width=title.width + 0.4, height=title.height + 0.16)
        gold_bar.set_fill(GOLD, 0.3).set_stroke(width=0, opacity=0).move_to(title)
        self.play(Write(title), FadeIn(gold_bar), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(GrowFromCenter(alpha_cell), GrowFromCenter(beta_cell), run_time=0.6)
        self.play(GrowFromCenter(alpha_bound), GrowFromCenter(beta_bound), run_time=0.3)
        self.play(Create(alpha_track), Create(beta_track), run_time=0.7)
        self.play(Create(alpha_dash), Create(beta_dash), run_time=0.4)
        self.play(GrowFromCenter(alpha_nb), run_time=0.4)
        self.play(GrowFromCenter(beta_nb1), GrowFromCenter(beta_nb2), run_time=0.5)
        self.play(FadeIn(alpha_lbl), FadeIn(beta_lbl), run_time=0.4)
        self.play(FadeIn(alpha_range), FadeIn(beta_range), run_time=0.4)
        self.wait(max(0.3, total - 4.5))


# ── B06  Crossfire mechanism ─────────────────────────────────────────────────
class B06_Crossfire(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 11.95)
        n_cells = 5
        cells = VGroup()
        bound_dots = VGroup()
        cell_positions = [LEFT * 4.0 + UP * 0.5 + RIGHT * i * 1.5 for i in range(n_cells)]
        for i, pos in enumerate(cell_positions):
            c = Circle(0.38).set_fill(SLATE, 0.80).set_stroke(INK, 1.5)
            c.move_to(pos)
            cells.add(c)
            if i == 0 or i == 2:
                d = Dot(radius=0.09, color=TEAL).move_to(pos)
                bound_dots.add(d)
        track_0 = Line(cell_positions[0] + RIGHT * 0.38,
                       cell_positions[3] + LEFT * 0.38,
                       color=TEAL, stroke_width=2.5)
        track_2 = Line(cell_positions[2] + RIGHT * 0.38,
                       cell_positions[4] + RIGHT * 0.1,
                       color=TEAL, stroke_width=2.5)
        glow_1 = Circle(0.38).set_fill(TEAL, 0.22).set_stroke(TEAL, 1.0)
        glow_1.move_to(cell_positions[1])
        glow_3 = Circle(0.38).set_fill(TEAL, 0.22).set_stroke(TEAL, 1.0)
        glow_3.move_to(cell_positions[3])
        glow_4 = Circle(0.38).set_fill(TEAL, 0.15).set_stroke(TEAL, 0.8)
        glow_4.move_to(cell_positions[4])
        bound_lbl = Text("receptor-positive (bound)", font=SERIF, color=INK,
                         font_size=15, slant=ITALIC)
        bound_lbl.next_to(cells, DOWN, buff=0.9)
        bound_lbl.shift(LEFT * 1.5)
        cf_lbl = Text("crossfire", font=DISPLAY, font_size=24, color=TEAL, weight=BOLD)
        cf_lbl.move_to(UP * 2.4)
        sub_lbl = Text("beta radiation irradiates neighbors that never bound the drug",
                       font=DISPLAY, font_size=14, color=INK)
        sub_lbl.next_to(cf_lbl, DOWN, buff=0.18)
        self.play(AnimationGroup(*[GrowFromCenter(c) for c in cells],
                                 lag_ratio=0.08), run_time=0.8)
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in bound_dots],
                                 lag_ratio=0.1), run_time=0.4)
        self.play(Create(track_0), Create(track_2), run_time=0.8)
        self.play(GrowFromCenter(glow_1), GrowFromCenter(glow_3),
                  GrowFromCenter(glow_4), run_time=0.6)
        self.play(Write(cf_lbl), run_time=0.4)
        self.play(FadeIn(sub_lbl), run_time=0.4)
        self.wait(max(0.3, total - 3.4))


# ── B07  Heterogeneous tumor cross-section (NEW) ─────────────────────────────
class B07_TumorGeometry(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 13.35)
        import numpy as np
        # Tumor cross-section: outer ring = receptor-positive (teal-tinted),
        # inner core = receptor-negative (muted/gray)
        outer_ring = Annulus(inner_radius=1.3, outer_radius=2.1,
                             color=TEAL, fill_opacity=0.35, stroke_width=0)
        outer_ring.move_to(UP * 0.2)
        outer_stroke = Circle(2.1).set_fill(opacity=0).set_stroke(INK, 1.5)
        outer_stroke.move_to(UP * 0.2)
        core = Circle(1.3).set_fill(SLATE, 0.20).set_stroke(SLATE, 1.0)
        core.move_to(UP * 0.2)
        # Labels
        rim_lbl = Text("receptor-positive", font=SERIF, color=TEAL,
                       font_size=16, slant=ITALIC)
        rim_lbl.move_to(RIGHT * 3.5 + UP * 1.4)
        rim_arrow = Arrow(rim_lbl.get_left(), outer_ring.get_right() + LEFT * 0.1,
                          buff=0.05, stroke_width=1.2, color=TEAL,
                          max_tip_length_to_length_ratio=0.12)
        core_lbl = Text("receptor-negative", font=SERIF, color=INK,
                        font_size=16, slant=ITALIC)
        core_lbl.move_to(RIGHT * 3.5 + UP * 0.5)
        core_arrow = Arrow(core_lbl.get_left(), core.get_right() + LEFT * 0.15,
                           buff=0.05, stroke_width=1.2, color=INK,
                           max_tip_length_to_length_ratio=0.12)
        # Title
        title = Text("Geometry problem: heterogeneous receptor expression",
                     font=DISPLAY, font_size=17, color=INK)
        title.move_to(UP * 3.1)
        # Diameter annotation
        diam_line = DoubleArrow(LEFT * 2.1 + DOWN * 2.0, RIGHT * 2.1 + DOWN * 2.0,
                                color=INK, stroke_width=1.2,
                                max_tip_length_to_length_ratio=0.05)
        diam_line.move_to(outer_stroke.get_bottom() + DOWN * 0.4)
        diam_lbl = Text("~ 3 cm", font=MONO, font_size=14, color=INK)
        diam_lbl.next_to(diam_line, DOWN, buff=0.1)
        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(outer_ring), GrowFromCenter(outer_stroke),
                  GrowFromCenter(core), run_time=0.8)
        self.play(FadeIn(rim_lbl), GrowArrow(rim_arrow), run_time=0.6)
        self.play(FadeIn(core_lbl), GrowArrow(core_arrow), run_time=0.5)
        self.play(GrowFromCenter(diam_line), FadeIn(diam_lbl), run_time=0.5)
        self.wait(max(0.3, total - 2.9))


# ── B08  Alpha fails on heterogeneous tumor ──────────────────────────────────
class B08_AlphaFail(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B08", 11.35)
        import numpy as np
        outer_ring = Annulus(inner_radius=1.2, outer_radius=2.0,
                             color=SLATE, fill_opacity=0.6, stroke_width=0)
        outer_ring.move_to(UP * 0.3)
        inner_core = Circle(1.2).set_fill(SLATE, 0.25).set_stroke(SLATE, 1.0)
        inner_core.move_to(UP * 0.3)
        rim_tracks = VGroup()
        for angle_deg in [0, 45, 90, 135, 180, 225, 270, 315]:
            a = np.radians(angle_deg)
            rim_pos = outer_ring.get_center() + np.array([np.cos(a) * 1.6,
                                                           np.sin(a) * 1.6, 0])
            track_end = rim_pos + np.array([np.cos(a) * 0.35, np.sin(a) * 0.35, 0])
            t = Line(rim_pos, track_end, color=CRIMSON, stroke_width=5)
            rim_tracks.add(t)
        reach_circle = Circle(1.2 + 0.4).set_stroke(CRIMSON, 1.5)
        reach_circle.move_to(UP * 0.3)
        rim_lbl = LabelChip("Rim: bound", accent=CRIMSON, size=15)
        rim_lbl.move_to(RIGHT * 3.5 + UP * 1.2)
        core_lbl = Text("Core: no drug reaches", font=SERIF, color=INK,
                        font_size=15, slant=ITALIC)
        core_lbl.move_to(RIGHT * 3.5 + UP * 0.4)
        fail_lbl = Text("core survives", font=DISPLAY, font_size=18,
                        color=CRIMSON, weight=BOLD)
        fail_lbl.move_to(UP * 0.3)
        title_lbl = Text("Alpha: confined track cannot reach the core",
                         font=DISPLAY, font_size=18, color=CRIMSON)
        title_lbl.move_to(UP * 3.0)
        self.play(GrowFromCenter(outer_ring), GrowFromCenter(inner_core), run_time=0.7)
        self.play(FadeIn(title_lbl), run_time=0.4)
        self.play(AnimationGroup(*[Create(t) for t in rim_tracks], lag_ratio=0.05),
                  run_time=0.8)
        self.play(Create(reach_circle), run_time=0.5)
        self.play(FadeIn(rim_lbl), FadeIn(core_lbl), run_time=0.4)
        self.play(FadeIn(fail_lbl), run_time=0.5)
        self.wait(max(0.3, total - 3.3))


# ── B09  Beta wins on heterogeneous tumor ────────────────────────────────────
class B09_BetaWin(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 12.14)
        import numpy as np
        outer_ring = Annulus(inner_radius=1.2, outer_radius=2.0,
                             color=SLATE, fill_opacity=0.6, stroke_width=0)
        outer_ring.move_to(UP * 0.3)
        inner_core = Circle(1.2).set_fill(SLATE, 0.25).set_stroke(SLATE, 1.0)
        inner_core.move_to(UP * 0.3)
        beta_tracks = VGroup()
        for angle_deg in [30, 90, 150, 210, 270, 330]:
            a = np.radians(angle_deg)
            rim_pos = outer_ring.get_center() + np.array([np.cos(a) * 1.6,
                                                           np.sin(a) * 1.6, 0])
            inward_dir = -np.array([np.cos(a), np.sin(a), 0])
            track_end = rim_pos + inward_dir * 1.9
            t = Line(rim_pos, track_end, color=TEAL, stroke_width=2.5)
            beta_tracks.add(t)
        core_glow = Circle(1.2).set_fill(TEAL, 0.28).set_stroke(TEAL, 1.5)
        core_glow.move_to(UP * 0.3)
        cf_title = Text("Beta crossfire reaches the core", font=DISPLAY,
                        font_size=18, color=TEAL, weight=BOLD)
        cf_title.move_to(UP * 3.0)
        win_lbl = Text("core irradiated", font=DISPLAY, font_size=18,
                       color=WHITE, weight=BOLD)
        win_lbl.move_to(UP * 0.3)
        self.play(GrowFromCenter(outer_ring), GrowFromCenter(inner_core), run_time=0.7)
        self.play(FadeIn(cf_title), run_time=0.4)
        self.play(AnimationGroup(*[Create(t) for t in beta_tracks], lag_ratio=0.06),
                  run_time=1.0)
        self.play(GrowFromCenter(core_glow), run_time=0.6)
        self.play(FadeIn(win_lbl), run_time=0.4)
        self.wait(max(0.3, total - 3.1))


# ── B11  Worked example — Lu-177 vs Ac-225 ───────────────────────────────────
class B11_Example(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B11", 19.03)
        header = Text("Heterogeneous neuroendocrine tumor  |  illustrative numbers",
                      font=DISPLAY, font_size=14, color=INK)
        header.move_to(UP * 3.1)
        # Lu-177 panel (LEFT)
        lu_card = Rectangle(width=3.4, height=3.2)
        lu_card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        lu_card.move_to(LEFT * 2.7 + UP * 0.2)
        lu_title = Text("Lu-177", font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
        lu_title.move_to(lu_card.get_top() + DOWN * 0.45)
        lu_sub = Text("beta emitter", font=DISPLAY, color=WHITE, font_size=14)
        lu_sub.next_to(lu_title, DOWN, buff=0.12)
        lu_num = Text("78%", font=MONO, color=TEAL, font_size=52, weight=BOLD)
        lu_num.move_to(lu_card.get_center() + UP * 0.15)
        lu_stat = Text("tumor cell kill", font=DISPLAY, color=WHITE, font_size=13)
        lu_stat.next_to(lu_num, DOWN, buff=0.12)
        lu_why = Text("crossfire reaches core", font=DISPLAY, color=TEAL, font_size=12)
        lu_why.move_to(lu_card.get_bottom() + UP * 0.45)
        lu_group = VGroup(lu_card, lu_title, lu_sub, lu_num, lu_stat, lu_why)
        # Ac-225 panel (RIGHT)
        ac_card = Rectangle(width=3.4, height=3.2)
        ac_card.set_fill(SLATE, 1).set_stroke(width=0, opacity=0)
        ac_card.move_to(RIGHT * 2.7 + UP * 0.2)
        ac_title = Text("Ac-225", font=DISPLAY, color=WHITE, font_size=22, weight=BOLD)
        ac_title.move_to(ac_card.get_top() + DOWN * 0.45)
        ac_sub = Text("alpha emitter", font=DISPLAY, color=WHITE, font_size=14)
        ac_sub.next_to(ac_title, DOWN, buff=0.12)
        ac_num = Text("41%", font=MONO, color=CRIMSON, font_size=52, weight=BOLD)
        ac_num.move_to(ac_card.get_center() + UP * 0.15)
        ac_stat = Text("tumor cell kill", font=DISPLAY, color=WHITE, font_size=13)
        ac_stat.next_to(ac_num, DOWN, buff=0.12)
        ac_why = Text("core untouched", font=DISPLAY, color=CRIMSON, font_size=12)
        ac_why.move_to(ac_card.get_bottom() + UP * 0.45)
        ac_group = VGroup(ac_card, ac_title, ac_sub, ac_num, ac_stat, ac_why)
        vs_lbl = Text("vs", font=SERIF, font_size=22, color=INK, slant=ITALIC)
        vs_lbl.move_to(ORIGIN + UP * 0.2)
        self.play(FadeIn(header), run_time=0.4)
        self.play(GrowFromCenter(lu_card), GrowFromCenter(ac_card), run_time=0.7)
        self.play(FadeIn(lu_title), FadeIn(lu_sub), FadeIn(ac_title), FadeIn(ac_sub),
                  run_time=0.4)
        self.play(FadeIn(lu_num), FadeIn(ac_num), run_time=0.6)
        self.play(FadeIn(lu_stat), FadeIn(ac_stat), FadeIn(vs_lbl), run_time=0.4)
        self.play(FadeIn(lu_why), FadeIn(ac_why), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ── Batch render helper ──────────────────────────────────────────────────────
SCENES = [
    ("B02_AlphaIntro",    "B02"),
    ("B03_BetaIntro",     "B03"),
    ("B05_EmitterRanges", "B05"),
    ("B06_Crossfire",     "B06"),
    ("B07_TumorGeometry", "B07"),
    ("B08_AlphaFail",     "B08"),
    ("B09_BetaWin",       "B09"),
    ("B11_Example",       "B11"),
]

if __name__ == "__main__":
    reel = pathlib.Path(__file__).resolve().parent
    manim_dir = reel / "manim"
    manim_dir.mkdir(exist_ok=True)
    failed = []
    for scene_cls, bid in SCENES:
        print(f"[render] {scene_cls} → manim/{bid}.mp4")
        out_dir = reel / "media" / "videos" / "scenes_std" / "1080p24"
        mp4_src = out_dir / f"{scene_cls}.mp4"
        mp4_dst = manim_dir / f"{bid}.mp4"
        # Render
        result = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  FAIL: {result.stderr[-500:]}")
            failed.append(scene_cls)
            continue
        if mp4_src.exists():
            import shutil
            shutil.copy2(mp4_src, mp4_dst)
            print(f"  OK → {mp4_dst}")
        else:
            print(f"  ERROR: output not found at {mp4_src}")
            failed.append(scene_cls)
    if failed:
        print(f"\nFailed scenes: {failed}")
        sys.exit(1)
    else:
        print(f"\nAll {len(SCENES)} scenes rendered to manim/")
