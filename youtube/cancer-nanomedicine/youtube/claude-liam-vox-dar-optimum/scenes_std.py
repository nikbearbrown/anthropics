"""scenes_std.py — GRAPHIC beats for claude-liam-vox-dar-optimum.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Scenes: B02_LoadingLogic, B04_DARScale, B05_UnderKill, B06_HydrophobicLoad,
        B07_ClearanceTrap, B09_OptimumCurve, B10_ExamplePharma, B11_TumorQuote

Render each scene individually:
  manim -qh --fps 24 scenes_std.py B02_LoadingLogic
  mv media/videos/scenes_std/1080p24/B02_LoadingLogic.mp4 manim/B02.mp4

Or batch at the bottom:
  python3 scenes_std.py
"""
import json
import pathlib
import subprocess
import sys

from manim import *

# ── Palette ──────────────────────────────────────────────────────────────────
GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"   # optimal / survives in blood / reaches tumor
CRIMSON  = "#BF3339"   # overloaded / cleared fast / toxic
GOLD     = "#F5D061"   # highlight fill only — never text
SLATE    = "#3E5559"   # structural / neutral cell fill
HAIRLINE = "#D4D4D4"

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
    scene.camera.background_color = GROUND


def _antibody_Y(center, arm_color=INK, stroke=3.5):
    """Y-shaped antibody at `center` — returns a VGroup with arms + hinge."""
    hinge = center
    left_arm_end  = hinge + LEFT  * 0.55 + UP * 0.9
    right_arm_end = hinge + RIGHT * 0.55 + UP * 0.9
    stem_end      = hinge + DOWN  * 0.7
    arms = VGroup(
        Line(hinge, left_arm_end,  color=arm_color, stroke_width=stroke),
        Line(hinge, right_arm_end, color=arm_color, stroke_width=stroke),
        Line(hinge, stem_end,      color=arm_color, stroke_width=stroke),
    )
    return arms, [left_arm_end, right_arm_end, stem_end]


# ── B02  Loading logic (accumulate 1 → 4 → 8) ────────────────────────────────
class B02_LoadingLogic(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B02", 13.99)
        title = Text("Antibody + payload — the naive logic",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.1)
        arms, endpoints = _antibody_Y(ORIGIN + UP * 0.1)
        counter = Text("1", font=MONO, font_size=42, color=TEAL, weight=BOLD)
        counter.move_to(RIGHT * 4.2 + UP * 1.2)
        counter_lbl = Text("warheads", font=DISPLAY, font_size=14, color=INK)
        counter_lbl.next_to(counter, DOWN, buff=0.12)

        # 8 candidate dot positions distributed along the two upper arms
        dot_positions = []
        for arm_end in endpoints[:2]:
            for f in (0.35, 0.55, 0.75, 0.95):
                p = interpolate(ORIGIN + UP * 0.1, arm_end, f) + RIGHT * 0.0
                dot_positions.append(p)

        dots = [Dot(radius=0.14, color=TEAL).move_to(p) for p in dot_positions]

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(arms), run_time=0.7)
        self.play(FadeIn(counter), FadeIn(counter_lbl), run_time=0.4)
        # Accumulate first four
        for i in range(4):
            new_counter = Text(str(i + 1), font=MONO, font_size=42,
                               color=TEAL, weight=BOLD).move_to(counter)
            self.play(GrowFromCenter(dots[i]),
                      Transform(counter, new_counter), run_time=0.35)
        pause_lbl = Text("DAR 4", font=MONO, font_size=18, color=TEAL, weight=BOLD)
        pause_lbl.move_to(DOWN * 2.4 + LEFT * 2.5)
        self.play(FadeIn(pause_lbl), run_time=0.3)
        self.wait(0.4)
        # Accumulate next four
        for i in range(4, 8):
            new_counter = Text(str(i + 1), font=MONO, font_size=42,
                               color=TEAL, weight=BOLD).move_to(counter)
            self.play(GrowFromCenter(dots[i]),
                      Transform(counter, new_counter), run_time=0.35)
        dar8_lbl = Text("DAR 8", font=MONO, font_size=18, color=TEAL, weight=BOLD)
        dar8_lbl.move_to(DOWN * 2.4 + RIGHT * 2.5)
        self.play(FadeIn(dar8_lbl), run_time=0.3)
        naive = Text('"kill 8× harder"  ← the intuition', font=SERIF,
                     font_size=17, color=INK, slant=ITALIC)
        naive.move_to(DOWN * 3.0)
        self.play(FadeIn(naive), run_time=0.4)
        self.wait(max(0.3, total - 6.8))


# ── B04  DAR scale (0-10, sweet spot 4-8) ────────────────────────────────────
class B04_DARScale(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B04", 13.91)
        title = Text("DAR — drug-to-antibody ratio",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)
        # Number line
        line = NumberLine(x_range=[0, 10, 1], length=9, color=INK,
                          include_numbers=True,
                          font_size=22,
                          decimal_number_config={"num_decimal_places": 0,
                                                 "color": INK})
        line.move_to(UP * 0.1)
        # Sweet-spot bracket (teal, spans 4-8)
        p4 = line.number_to_point(4)
        p8 = line.number_to_point(8)
        bracket = Rectangle(width=(p8[0] - p4[0]), height=0.55,
                            color=TEAL, fill_opacity=0.28, stroke_width=1.5)
        bracket.move_to((p4 + p8) / 2 + UP * 0.35)
        # Bracket label sits WELL above the bracket so failure-mode labels beneath
        # the crimson arrows never collide with it (Gate V fix 2026-08-28)
        bracket_lbl = Text("clinical ADCs (DAR 4–8)", font=DISPLAY,
                           font_size=17, color=TEAL, weight=BOLD)
        bracket_lbl.move_to((p4 + p8) / 2 + UP * 2.0)
        # Failure arrows (short, close to the bracket edges — labels go BELOW them)
        left_arrow  = Arrow(p4 + UP * 1.35, p4 + UP * 0.70,
                            color=CRIMSON, stroke_width=3,
                            max_tip_length_to_length_ratio=0.35)
        right_arrow = Arrow(p8 + UP * 1.35, p8 + UP * 0.70,
                            color=CRIMSON, stroke_width=3,
                            max_tip_length_to_length_ratio=0.35)
        left_lbl  = Text("under-kill",     font=DISPLAY, font_size=15,
                         color=CRIMSON).next_to(left_arrow,  UP, buff=0.10)
        right_lbl = Text("over-aggregate", font=DISPLAY, font_size=15,
                         color=CRIMSON).next_to(right_arrow, UP, buff=0.10)
        # Domain endpoint labels
        zero_lbl = Text("no killing", font=SERIF, font_size=14,
                        color=INK, slant=ITALIC).move_to(
                        line.number_to_point(0) + DOWN * 0.7)
        ten_lbl  = Text("aggregates + cleared", font=SERIF, font_size=14,
                        color=INK, slant=ITALIC).move_to(
                        line.number_to_point(10) + DOWN * 0.7)
        caption = Text("A trade-off running in both directions",
                       font=SERIF, font_size=17, color=INK, slant=ITALIC)
        caption.move_to(DOWN * 2.6)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(line), run_time=0.9)
        self.play(FadeIn(zero_lbl), FadeIn(ten_lbl), run_time=0.4)
        self.play(GrowFromCenter(bracket), FadeIn(bracket_lbl), run_time=0.7)
        self.play(GrowArrow(left_arrow), GrowArrow(right_arrow),
                  FadeIn(left_lbl), FadeIn(right_lbl), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(max(0.3, total - 3.4))


# ── B05  Under-kill (payload below threshold, cell survives) ─────────────────
class B05_UnderKill(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 12.76)
        title = Text("Too little payload — cell survives",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)
        # Cell
        cell = Circle(1.5).set_fill(SLATE, 0.20).set_stroke(INK, 1.5)
        cell.move_to(LEFT * 3.0 + DOWN * 0.2)
        cell_lbl = Text("cancer cell (internalized ADC)", font=SERIF,
                        font_size=14, color=INK, slant=ITALIC)
        cell_lbl.next_to(cell, DOWN, buff=0.25)
        # A few small teal payload dots inside cell (delivered payload = low)
        payload_dots = VGroup(*[
            Dot(radius=0.11, color=TEAL).move_to(cell.get_center() + shift)
            for shift in (LEFT * 0.4, RIGHT * 0.4 + UP * 0.2,
                          DOWN * 0.5 + RIGHT * 0.1)
        ])
        # Threshold gauge on the right
        gauge_bar = Rectangle(width=0.9, height=4.0)
        gauge_bar.set_fill(WHITE, 0.6).set_stroke(INK, 1.5)
        gauge_bar.move_to(RIGHT * 3.0 + DOWN * 0.2)
        gauge_lbl = Text("payload dose", font=DISPLAY, font_size=13, color=INK)
        gauge_lbl.next_to(gauge_bar, UP, buff=0.15)
        # Threshold line (GOLD)
        thr_y = gauge_bar.get_center()[1] + 0.6   # threshold at 65% of gauge
        thr_line = Line(gauge_bar.get_left() + UP * 0.6,
                        gauge_bar.get_right() + UP * 0.6,
                        color=GOLD, stroke_width=6)
        thr_line.move_to([gauge_bar.get_center()[0], thr_y, 0])
        thr_lbl = Text("killing threshold", font=DISPLAY, font_size=13,
                       color=INK, weight=BOLD)
        thr_lbl.next_to(thr_line, RIGHT, buff=0.15)
        # Delivered fill (teal, sits BELOW threshold)
        fill_h = 1.2   # fill height BELOW threshold
        fill_bottom = gauge_bar.get_bottom()[1]
        fill_top    = fill_bottom + fill_h
        delivered = Rectangle(width=0.88, height=fill_h)
        delivered.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
        delivered.move_to([gauge_bar.get_center()[0],
                           (fill_bottom + fill_top) / 2, 0])
        deliv_lbl = Text("delivered", font=DISPLAY, font_size=13, color=TEAL)
        deliv_lbl.next_to(delivered, LEFT, buff=0.15)
        gap_arrow = DoubleArrow(delivered.get_top(), thr_line.get_center(),
                                color=CRIMSON, stroke_width=2,
                                max_tip_length_to_length_ratio=0.15)
        gap_lbl = Text("gap", font=MONO, font_size=13, color=CRIMSON)
        gap_lbl.next_to(gap_arrow, RIGHT, buff=0.1)
        # Outcome
        survives = LabelChip("cell survives", accent=CRIMSON, size=16)
        survives.move_to(DOWN * 3.0)

        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(cell), FadeIn(cell_lbl), run_time=0.6)
        self.play(*[GrowFromCenter(d) for d in payload_dots], run_time=0.5)
        self.play(GrowFromCenter(gauge_bar), FadeIn(gauge_lbl), run_time=0.5)
        self.play(Create(thr_line), FadeIn(thr_lbl), run_time=0.5)
        self.play(GrowFromCenter(delivered), FadeIn(deliv_lbl), run_time=0.6)
        self.play(GrowArrow(gap_arrow), FadeIn(gap_lbl), run_time=0.5)
        self.play(FadeIn(survives), run_time=0.5)
        self.wait(max(0.3, total - 3.5))


# ── B06  Hydrophobic overload (aggregation) ──────────────────────────────────
class B06_HydrophobicLoad(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 13.4)
        title = Text("Overloaded — hydrophobic payload clumps",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.0)

        # Three antibodies side by side
        centers = [LEFT * 3.3, ORIGIN, RIGHT * 3.3]
        ab_arms = []
        ab_endpoints = []
        for c in centers:
            arms, endpoints = _antibody_Y(c + DOWN * 0.2)
            ab_arms.append(arms)
            ab_endpoints.append(endpoints)

        # Each antibody: 8 crimson payload dots (all overloaded)
        all_dots = []
        for endpoints in ab_endpoints:
            positions = []
            for arm_end in endpoints[:2]:
                for f in (0.35, 0.60, 0.85, 1.05):
                    p = interpolate(endpoints[-1] + UP * 0.9,
                                    arm_end, f)
                    positions.append(p)
            dots = [Dot(radius=0.12, color=CRIMSON).move_to(p) for p in positions]
            all_dots.append(dots)

        sticky_lbl = Text("sticky / hydrophobic", font=DISPLAY,
                          font_size=15, color=CRIMSON, weight=BOLD)
        sticky_lbl.move_to(UP * 1.5)
        # Aggregation cluster: the three antibodies drift toward each other
        aggregate_ring = Circle(2.4).set_stroke(CRIMSON, 2)
        aggregate_ring.set_fill(CRIMSON, 0.08)
        aggregate_ring.move_to(DOWN * 0.4)
        aggregate_lbl = Text("aggregation", font=DISPLAY, font_size=18,
                             color=CRIMSON, weight=BOLD)
        aggregate_lbl.move_to(DOWN * 2.6)

        self.play(FadeIn(title), run_time=0.4)
        self.play(*[Create(a) for a in ab_arms], run_time=0.7)
        # Accumulate first 4 dots on each (teal-ish OK region — actually still crimson to keep semantics)
        for i in range(4):
            self.play(*[GrowFromCenter(d[i]) for d in all_dots],
                      run_time=0.28)
        self.wait(0.2)
        # Past 4 — dots turn overload region
        for i in range(4, 8):
            self.play(*[GrowFromCenter(d[i]) for d in all_dots],
                      run_time=0.25)
        self.play(FadeIn(sticky_lbl), run_time=0.3)
        # Drift together, form aggregate
        drift = []
        for arms, c in zip(ab_arms, centers):
            drift.append(arms.animate.shift(-c * 0.35 + DOWN * 0.2))
        for dots, c in zip(all_dots, centers):
            grp = VGroup(*dots)
            drift.append(grp.animate.shift(-c * 0.35 + DOWN * 0.2))
        self.play(*drift, run_time=0.9)
        self.play(FadeIn(aggregate_ring), FadeIn(aggregate_lbl), run_time=0.6)
        self.wait(max(0.3, total - 6.0))


# ── B07  Clearance trap (liver / immune pulls out DAR-8) ─────────────────────
class B07_ClearanceTrap(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 11.52)
        title = Text("Liver / immune system clears aggregated ADCs — fast",
                     font=DISPLAY, font_size=18, color=INK).move_to(UP * 3.0)

        # Blood vessel channel (two horizontal lines)
        top = Line(LEFT * 6.0 + UP * 0.9, RIGHT * 3.5 + UP * 0.9,
                   color=INK, stroke_width=2)
        bot = Line(LEFT * 6.0 + DOWN * 0.9, RIGHT * 3.5 + DOWN * 0.9,
                   color=INK, stroke_width=2)
        vessel_lbl = Text("bloodstream", font=SERIF, font_size=14,
                          color=INK, slant=ITALIC)
        vessel_lbl.move_to(LEFT * 5.0 + UP * 1.5)

        # Cleared box on the right
        cleared_box = Rectangle(width=2.4, height=2.6)
        cleared_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2)
        cleared_box.move_to(RIGHT * 4.5 + DOWN * 0.1)
        cleared_title = Text("liver / immune", font=DISPLAY, font_size=16,
                             color=CRIMSON, weight=BOLD)
        cleared_title.move_to(cleared_box.get_top() + DOWN * 0.28)
        cleared_sub = Text("cleared", font=DISPLAY, font_size=13, color=CRIMSON)
        cleared_sub.next_to(cleared_title, DOWN, buff=0.10)

        # DAR-4 particles (teal circles, flow through)
        dar4 = VGroup(
            Circle(0.20).set_fill(TEAL, 0.85).set_stroke(TEAL, 1),
            Circle(0.20).set_fill(TEAL, 0.85).set_stroke(TEAL, 1),
            Circle(0.20).set_fill(TEAL, 0.85).set_stroke(TEAL, 1),
        )
        for c, x in zip(dar4, [LEFT * 5.0, LEFT * 4.2, LEFT * 3.4]):
            c.move_to(x + UP * 0.3)
        dar4_lbl = Text("DAR-4  flows through", font=DISPLAY, font_size=13, color=TEAL)
        dar4_lbl.move_to(LEFT * 4.2 + UP * 2.2)

        # DAR-8 aggregates (crimson clumps)
        dar8_pos = [LEFT * 5.5 + DOWN * 0.3, LEFT * 4.6 + DOWN * 0.4]
        dar8 = VGroup(*[Circle(0.32).set_fill(CRIMSON, 0.8).set_stroke(CRIMSON, 1)
                        .move_to(p) for p in dar8_pos])
        dar8_lbl = Text("DAR-8  aggregates", font=DISPLAY,
                        font_size=13, color=CRIMSON)
        dar8_lbl.move_to(LEFT * 4.8 + DOWN * 2.0)

        # Clock ticker (hours, not days)
        clock_lbl = Text("hours, not days", font=MONO, font_size=15,
                         color=INK, weight=BOLD)
        clock_lbl.move_to(RIGHT * 1.0 + UP * 2.4)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(top), Create(bot), FadeIn(vessel_lbl), run_time=0.6)
        self.play(FadeIn(cleared_box), FadeIn(cleared_title), FadeIn(cleared_sub),
                  run_time=0.5)
        self.play(*[GrowFromCenter(c) for c in dar4], FadeIn(dar4_lbl), run_time=0.5)
        # DAR-4 flow through past the cleared box
        self.play(dar4.animate.shift(RIGHT * 7.5), run_time=1.2)
        self.play(*[GrowFromCenter(c) for c in dar8], FadeIn(dar8_lbl), run_time=0.5)
        # DAR-8 pulled aside into the cleared box
        self.play(dar8.animate.move_to(cleared_box.get_center() + DOWN * 0.4),
                  run_time=1.0)
        self.play(FadeIn(clock_lbl), run_time=0.4)
        self.wait(max(0.3, total - 5.2))


# ── B09  Optimum curve (bell peak, both failure zones) ───────────────────────
class B09_OptimumCurve(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 14.76)
        import numpy as np

        axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 1.2, 0.2],
            x_length=8, y_length=4,
            axis_config={"color": INK, "stroke_width": 1.5,
                         "include_ticks": True},
            tips=False,
        ).move_to(DOWN * 0.3)
        x_lbl = Text("DAR", font=DISPLAY, font_size=15, color=INK)
        x_lbl.next_to(axes.x_axis, DOWN, buff=0.35).align_to(axes.x_axis, RIGHT).shift(LEFT * 0.6)
        y_lbl = Text("tumor drug delivery", font=DISPLAY, font_size=15, color=INK)
        y_lbl.rotate(PI / 2).next_to(axes.y_axis, LEFT, buff=0.30)

        # Bell curve peaking at DAR 6, falling steeply past 8
        def curve_fn(x):
            return np.exp(-((x - 6) ** 2) / 3.0) * (1.0 if x <= 8 else np.exp(-(x - 8) ** 2))

        curve = axes.plot(curve_fn, x_range=[0, 10, 0.05],
                          color=INK, stroke_width=3)
        # Teal band 4-8 highlighted under the curve
        band = axes.get_area(curve, x_range=(4, 8),
                             color=TEAL, opacity=0.30)

        # Down arrows flanking the peak, crimson
        p4  = axes.c2p(4, curve_fn(4))
        p8  = axes.c2p(8, curve_fn(8))
        left_ar  = Arrow(p4 + UP * 1.3, p4 + UP * 0.15,
                         color=CRIMSON, stroke_width=3,
                         max_tip_length_to_length_ratio=0.18)
        right_ar = Arrow(p8 + UP * 1.3, p8 + UP * 0.15,
                         color=CRIMSON, stroke_width=3,
                         max_tip_length_to_length_ratio=0.18)
        left_lbl  = Text("under-kill", font=DISPLAY, font_size=14,
                         color=CRIMSON).next_to(left_ar,  UP, buff=0.05)
        right_lbl = Text("over-aggregate", font=DISPLAY, font_size=14,
                         color=CRIMSON).next_to(right_ar, UP, buff=0.05)
        sweet = Text("sweet spot", font=DISPLAY, font_size=15,
                     color=TEAL, weight=BOLD)
        sweet.move_to(axes.c2p(6, curve_fn(6)) + DOWN * 0.6)

        title = Text("DAR is an optimum, not a maximum",
                     font=DISPLAY, font_size=20, color=INK).move_to(UP * 3.15)

        self.play(FadeIn(title), run_time=0.4)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.8)
        self.play(Create(curve), run_time=1.4)
        self.play(FadeIn(band), FadeIn(sweet), run_time=0.6)
        self.play(GrowArrow(left_ar), FadeIn(left_lbl), run_time=0.5)
        self.play(GrowArrow(right_ar), FadeIn(right_lbl), run_time=0.5)
        self.wait(max(0.3, total - 4.2))


# ── B10  DAR-4 vs DAR-8 plasma at 24h ────────────────────────────────────────
class B10_ExamplePharma(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 16.3)
        title = Text("Same lab, same dose — plasma at 24 hours",
                     font=DISPLAY, font_size=18, color=INK).move_to(UP * 3.05)
        illustrative = Text("illustrative", font=MONO, font_size=13, color=INK)
        illustrative.move_to(DOWN * 3.2)

        # Two bar columns
        axis_y0 = -2.2
        max_h   = 4.2
        # DAR-4 68%
        bar4 = Rectangle(width=1.4, height=max_h * 0.68)
        bar4.set_fill(TEAL, 0.85).set_stroke(width=0, opacity=0)
        bar4.move_to([-2.4, axis_y0 + bar4.height / 2, 0])
        base4 = Line(bar4.get_left() + DOWN * 0.02,
                     bar4.get_right() + DOWN * 0.02, color=INK, stroke_width=1)
        base4.move_to([-2.4, axis_y0, 0])
        # DAR-8 11%
        bar8 = Rectangle(width=1.4, height=max_h * 0.11)
        bar8.set_fill(CRIMSON, 0.85).set_stroke(width=0, opacity=0)
        bar8.move_to([2.4, axis_y0 + bar8.height / 2, 0])
        base8 = Line(bar8.get_left() + DOWN * 0.02,
                     bar8.get_right() + DOWN * 0.02, color=INK, stroke_width=1)
        base8.move_to([2.4, axis_y0, 0])

        # Category labels
        cat4 = Text("DAR-4", font=MONO, font_size=22, color=TEAL, weight=BOLD)
        cat4.move_to([-2.4, axis_y0 - 0.35, 0])
        cat8 = Text("DAR-8", font=MONO, font_size=22, color=CRIMSON, weight=BOLD)
        cat8.move_to([2.4, axis_y0 - 0.35, 0])

        # Number labels on top of bars
        pct4 = Text("68%", font=MONO, font_size=32, color=TEAL, weight=BOLD)
        pct4.next_to(bar4, UP, buff=0.10)
        pct8 = Text("11%", font=MONO, font_size=32, color=CRIMSON, weight=BOLD)
        pct8.next_to(bar8, UP, buff=0.10)
        cap4 = Text("plasma peak", font=DISPLAY, font_size=12, color=INK)
        cap4.next_to(pct4, UP, buff=0.08)
        cap8 = Text("plasma peak", font=DISPLAY, font_size=12, color=INK)
        cap8.next_to(pct8, UP, buff=0.08)

        time_lbl = Text("24 h", font=MONO, font_size=18, color=INK, weight=BOLD)
        time_lbl.move_to(UP * 2.4)

        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(time_lbl), run_time=0.3)
        self.play(Create(base4), Create(base8), run_time=0.4)
        self.play(FadeIn(cat4), FadeIn(cat8), run_time=0.4)
        self.play(GrowFromEdge(bar4, DOWN), GrowFromEdge(bar8, DOWN), run_time=1.2)
        self.play(FadeIn(pct4), FadeIn(pct8), run_time=0.5)
        self.play(FadeIn(cap4), FadeIn(cap8), FadeIn(illustrative), run_time=0.4)
        self.wait(max(0.3, total - 3.6))


# ── B11  Quote card — tumor drug at 72h, "0.3" highlighted GOLD ──────────────
class B11_TumorQuote(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B11", 18.28)
        header = Text("72 hours", font=MONO, font_size=18, color=INK, weight=BOLD)
        header.move_to(UP * 3.0)

        line1 = Text("DAR-4:  2.4 μg/g  tumor", font=MONO,
                     font_size=32, color=TEAL, weight=BOLD)
        line1.move_to(UP * 1.1)

        # DAR-8 line rendered as three Text objects so the "0.3" can be highlighted.
        # Wider buff on the arrange so the GOLD highlight box does not collide
        # with the surrounding "DAR-8:" prefix or "μg/g tumor" suffix (Gate V fix 2026-08-28).
        prefix = Text("DAR-8:",    font=MONO, font_size=32, color=CRIMSON, weight=BOLD)
        num    = Text("0.3",       font=MONO, font_size=32, color=CRIMSON, weight=BOLD)
        suffix = Text("μg/g tumor", font=MONO, font_size=32, color=CRIMSON, weight=BOLD)
        line2 = VGroup(prefix, num, suffix).arrange(RIGHT, buff=0.55, aligned_edge=DOWN)
        line2.move_to(DOWN * 0.2)

        highlight = Rectangle(width=num.width + 0.30, height=num.height + 0.16)
        highlight.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        highlight.move_to(num)

        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=INK, stroke_width=0.7)
        rule.move_to(DOWN * 1.3)

        attribution = Text(
            "— illustrative example (same antibody, same payload, same dose)",
            font=SERIF, font_size=17, color=INK, slant=ITALIC)
        attribution.move_to(DOWN * 1.8)

        caption = Text(
            "Higher payload per molecule → less drug at the tumor.",
            font=SERIF, font_size=18, color=INK, slant=ITALIC)
        caption.move_to(DOWN * 2.7)

        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(line1), run_time=0.6)
        self.play(FadeIn(prefix), FadeIn(suffix), run_time=0.5)
        self.play(FadeIn(highlight), FadeIn(num), run_time=0.6)
        self.play(Create(rule), FadeIn(attribution), run_time=0.6)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(max(0.3, total - 3.7))


# ── Batch render helper ──────────────────────────────────────────────────────
SCENES = [
    ("B02_LoadingLogic",    "B02"),
    ("B04_DARScale",        "B04"),
    ("B05_UnderKill",       "B05"),
    ("B06_HydrophobicLoad", "B06"),
    ("B07_ClearanceTrap",   "B07"),
    ("B09_OptimumCurve",    "B09"),
    ("B10_ExamplePharma",   "B10"),
    ("B11_TumorQuote",      "B11"),
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
        result = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  FAIL: {result.stderr[-800:]}")
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
