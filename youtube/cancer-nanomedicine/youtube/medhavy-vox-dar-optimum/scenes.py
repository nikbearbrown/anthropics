"""scenes.py — Manim graphics for medhavy-vox-dar-optimum.

Medhavy/vox palette (per beat_sheet.metadata):
  ground  #F3EBDD  cream
  ink     #2F2A26  charcoal serif type
  teal    #1F6F5C  optimal / survives in blood / reaches tumor
  crimson #BF3339  overloaded / cleared fast / kills healthy tissue
  gold    #F5D061  highlighter (unused here)

Editorial flat diagrams. Serif labels. Hairline strokes. No gradients,
no glow. TEAL = good, CRIMSON = failure. Numbers are illustrative
(matches the beat sheet's own DAR disclaimer).

Render one:
    manim -ql --fps 24 scenes.py B02_LoadingLogic
Render all:
    python3 render_scenes.py
"""
from manim import *

GROUND  = "#F3EBDD"
INK     = "#2F2A26"
TEAL    = "#1F6F5C"
CRIMSON = "#BF3339"
SOFT    = "#8A8575"

config.background_color = GROUND

SERIF = "EB Garamond"
MONO  = "Menlo"


def _serif(text, size=32, color=INK, weight=NORMAL, slant=NORMAL):
    return Text(text, font=SERIF, color=color, font_size=size,
                weight=weight, slant=slant)


def _mono(text, size=24, color=INK):
    return Text(text, font=MONO, color=color, font_size=size)


def _label(text, size=22, color=SOFT):
    return _serif(text, size=size, color=color, slant=ITALIC)


def _antibody(center=ORIGIN, color=INK, stroke=3.6):
    """A minimal Y-shaped antibody: stem down + two upper arms."""
    stem = Line(center + DOWN * 1.1, center, color=color, stroke_width=stroke)
    arm_l = Line(center, center + LEFT * 0.9 + UP * 0.9,
                 color=color, stroke_width=stroke)
    arm_r = Line(center, center + RIGHT * 0.9 + UP * 0.9,
                 color=color, stroke_width=stroke)
    return VGroup(stem, arm_l, arm_r)


def _payload(pos, color=TEAL, r=0.14):
    return Dot(point=pos, color=color, radius=r)


# ── B02 ──────────────────────────────────────────────────────────────────
class B02_LoadingLogic(Scene):
    """Antibody + payload accumulation 1 → 4 → 8 (teal). ~18s."""

    def construct(self):
        title = _serif("antibody + payload", size=34, color=INK).to_edge(UP, buff=0.6)
        ab = _antibody(center=ORIGIN + DOWN * 0.4, color=INK)

        counter = _mono("count: 0", size=30, color=INK).to_edge(DOWN, buff=0.9)

        # eight payload anchor positions, distributed along the two arms
        arm_l_dir = (LEFT * 0.9 + UP * 0.9)
        arm_r_dir = (RIGHT * 0.9 + UP * 0.9)
        center = ORIGIN + DOWN * 0.4
        anchors = []
        for t in (0.35, 0.60, 0.85, 1.05):
            anchors.append(center + arm_l_dir * t + (UP * 0.18))
        for t in (0.35, 0.60, 0.85, 1.05):
            anchors.append(center + arm_r_dir * t + (UP * 0.18))

        self.play(FadeIn(title, run_time=0.6))
        self.play(FadeIn(ab, run_time=0.8))
        self.play(FadeIn(counter, run_time=0.4))
        self.wait(0.6)

        dots = []
        # first four
        for i, a in enumerate(anchors[:4]):
            d = _payload(a, color=TEAL, r=0.16)
            new_counter = _mono(f"count: {i+1}", size=30, color=INK).move_to(counter)
            self.play(FadeIn(d, scale=0.6, run_time=0.35),
                      Transform(counter, new_counter, run_time=0.35))
            dots.append(d)
        self.wait(1.2)
        # next four
        for i, a in enumerate(anchors[4:]):
            d = _payload(a, color=TEAL, r=0.16)
            new_counter = _mono(f"count: {i+5}", size=30, color=INK).move_to(counter)
            self.play(FadeIn(d, scale=0.6, run_time=0.35),
                      Transform(counter, new_counter, run_time=0.35))
            dots.append(d)
        cue = _label("the naive picture: more payload = more kill", size=24).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(cue, run_time=0.6))
        self.wait(6.0)


# ── B04 ──────────────────────────────────────────────────────────────────
class B04_DARScale(Scene):
    """Number line 0-10; teal bracket at 4-8 labelled 'clinical ADCs'. ~16s."""

    def construct(self):
        left  = LEFT * 5.2
        right = RIGHT * 5.2
        axis = Line(left, right, color=INK, stroke_width=2.4)

        ticks = VGroup()
        labels = VGroup()
        for n in range(0, 11):
            x = left + (right - left) * (n / 10.0)
            tk = Line(x + UP * 0.10, x + DOWN * 0.10, color=INK, stroke_width=2.0)
            ticks.add(tk)
            lbl = _mono(str(n), size=22, color=INK).next_to(x, DOWN, buff=0.25)
            labels.add(lbl)

        axis_title = _serif("DAR — drug-to-antibody ratio",
                            size=30, color=INK).to_edge(UP, buff=0.9)

        # teal bracket over 4..8
        x4 = left + (right - left) * 0.40
        x8 = left + (right - left) * 0.80
        bracket_bar = Line(x4 + UP * 0.9, x8 + UP * 0.9,
                           color=TEAL, stroke_width=6.0)
        bracket_l = Line(x4 + UP * 0.9, x4 + UP * 0.55,
                         color=TEAL, stroke_width=6.0)
        bracket_r = Line(x8 + UP * 0.9, x8 + UP * 0.55,
                         color=TEAL, stroke_width=6.0)
        bracket = VGroup(bracket_bar, bracket_l, bracket_r)
        bracket_lbl = _serif("clinical ADCs (4–8)", size=28, color=TEAL).move_to(
            (x4 + x8) / 2 + UP * 1.4)

        # crimson arrows on both sides pointing outward
        arrow_l = Arrow(x4 + DOWN * 1.2, x4 + LEFT * 1.6 + DOWN * 1.2,
                        color=CRIMSON, buff=0.05, stroke_width=6, tip_length=0.24)
        arrow_r = Arrow(x8 + DOWN * 1.2, x8 + RIGHT * 1.6 + DOWN * 1.2,
                        color=CRIMSON, buff=0.05, stroke_width=6, tip_length=0.24)
        under_lbl = _serif("under-kill", size=26, color=CRIMSON).next_to(arrow_l, DOWN, buff=0.15)
        over_lbl  = _serif("over-aggregate", size=26, color=CRIMSON).next_to(arrow_r, DOWN, buff=0.15)

        self.play(FadeIn(axis_title, run_time=0.6))
        self.play(Create(axis, run_time=1.0),
                  LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.05, run_time=1.2),
                  LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.05, run_time=1.2))
        self.play(GrowFromCenter(bracket, run_time=1.0),
                  FadeIn(bracket_lbl, run_time=0.6))
        self.wait(1.2)
        self.play(GrowArrow(arrow_l, run_time=0.6),
                  FadeIn(under_lbl, run_time=0.6),
                  GrowArrow(arrow_r, run_time=0.6),
                  FadeIn(over_lbl, run_time=0.6))
        self.wait(6.5)


# ── B06 ──────────────────────────────────────────────────────────────────
class B06_HydrophobicLoad(Scene):
    """Antibody loaded past 4 with crimson payload → aggregate cluster. ~17.5s."""

    def construct(self):
        title = _serif("hydrophobic overload → aggregation",
                       size=32, color=INK).to_edge(UP, buff=0.6)

        # centered antibody
        ab_center = ORIGIN + LEFT * 3.0 + DOWN * 0.3
        ab = _antibody(center=ab_center, color=TEAL)

        arm_l_dir = (LEFT * 0.9 + UP * 0.9)
        arm_r_dir = (RIGHT * 0.9 + UP * 0.9)
        anchors = []
        for t in (0.35, 0.60, 0.85, 1.05):
            anchors.append(ab_center + arm_l_dir * t + UP * 0.18)
        for t in (0.35, 0.60, 0.85, 1.05):
            anchors.append(ab_center + arm_r_dir * t + UP * 0.18)

        self.play(FadeIn(title, run_time=0.6))
        self.play(FadeIn(ab, run_time=0.8))
        self.wait(0.4)

        # first four (still ok — teal)
        first_dots = VGroup(*[_payload(a, color=TEAL, r=0.16) for a in anchors[:4]])
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in first_dots],
                              lag_ratio=0.15, run_time=1.2))
        cue_ok = _label("safe load", size=22, color=TEAL).next_to(ab, UP, buff=0.25)
        self.play(FadeIn(cue_ok, run_time=0.4))
        self.wait(0.6)

        # next four turn crimson (overload)
        over_dots = VGroup(*[_payload(a, color=CRIMSON, r=0.18) for a in anchors[4:]])
        cue_bad = _label("greasy · sticky · aggregates",
                         size=22, color=CRIMSON).next_to(ab, UP, buff=0.25)
        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in over_dots],
                              lag_ratio=0.15, run_time=1.4),
                  Transform(cue_ok, cue_bad, run_time=1.4))
        self.wait(0.8)

        # aggregation cluster on the right
        cluster_center = RIGHT * 3.4 + DOWN * 0.3
        cluster = VGroup()
        pts = [(-0.5, 0.4), (-0.1, 0.6), (0.4, 0.35), (0.6, -0.05),
               (0.35, -0.45), (-0.15, -0.6), (-0.5, -0.15), (0.1, 0.05)]
        for (dx, dy) in pts:
            cluster.add(Dot(cluster_center + RIGHT * dx + UP * dy,
                            color=CRIMSON, radius=0.19))

        arrow = Arrow(ab_center + RIGHT * 1.7, cluster_center + LEFT * 0.9,
                      color=CRIMSON, buff=0.1, stroke_width=6, tip_length=0.28)
        agg_lbl = _serif("aggregate", size=26, color=CRIMSON).next_to(
            VGroup(*cluster), DOWN, buff=0.35)

        self.play(GrowArrow(arrow, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in cluster],
                              lag_ratio=0.08, run_time=1.4),
                  FadeIn(agg_lbl, run_time=0.6))
        self.wait(6.0)


# ── B07 ──────────────────────────────────────────────────────────────────
class B07_ClearanceTrap(Scene):
    """Blood vessel: teal DAR-4 flows through, crimson DAR-8 pulled aside. ~15s."""

    def construct(self):
        title = _serif("liver / immune clearance",
                       size=32, color=INK).to_edge(UP, buff=0.6)

        # blood vessel channel: two parallel horizontal lines
        top = Line(LEFT * 5.5 + UP * 0.6, RIGHT * 5.5 + UP * 0.6,
                   color=INK, stroke_width=2.2)
        bot = Line(LEFT * 5.5 + DOWN * 0.6, RIGHT * 5.5 + DOWN * 0.6,
                   color=INK, stroke_width=2.2)
        channel = VGroup(top, bot)
        channel_lbl = _label("blood", size=22).next_to(top, UP, buff=0.15).align_to(top, LEFT)

        # cleared box (crimson) below-right
        cleared_box = RoundedRectangle(width=3.6, height=1.4, corner_radius=0.15,
                                       stroke_color=CRIMSON, stroke_width=3.2,
                                       fill_color=GROUND, fill_opacity=1.0)
        cleared_box.move_to(RIGHT * 3.6 + DOWN * 2.3)
        cleared_lbl = _serif("liver / immune", size=26, color=CRIMSON).move_to(cleared_box)

        # clock
        clock_lbl = _mono("t: hours, not days", size=24, color=SOFT).to_edge(DOWN, buff=0.3)

        # 3 teal DAR-4 particles that will flow left→right
        teal_pts = [_payload(LEFT * 5.2 + UP * 0.15 + LEFT * i * 0.6, color=TEAL, r=0.17)
                    for i in range(3)]
        # 2 crimson DAR-8 aggregates that will divert down-right
        crim_pts = [_payload(LEFT * 4.2 + DOWN * 0.15 + LEFT * i * 0.7, color=CRIMSON, r=0.19)
                    for i in range(2)]

        self.play(FadeIn(title, run_time=0.5))
        self.play(Create(channel, run_time=0.9), FadeIn(channel_lbl, run_time=0.5))
        self.play(FadeIn(cleared_box, run_time=0.5), FadeIn(cleared_lbl, run_time=0.5))
        self.play(FadeIn(clock_lbl, run_time=0.4))

        # teal DAR-4 stream flows through unimpeded
        for dot in teal_pts:
            self.add(dot)
        self.play(*[dot.animate.shift(RIGHT * 10.4) for dot in teal_pts],
                  run_time=2.2)

        # crimson DAR-8 diverts to cleared box
        for dot in crim_pts:
            self.add(dot)
        # move first partway, then down into cleared box
        cleared_target_l = cleared_box.get_left() + RIGHT * 0.6
        cleared_target_r = cleared_box.get_left() + RIGHT * 1.2
        self.play(crim_pts[0].animate.move_to(cleared_target_l),
                  crim_pts[1].animate.move_to(cleared_target_r),
                  run_time=1.8)

        tag = _serif("DAR-8 cleared", size=24, color=CRIMSON).next_to(
            cleared_box, UP, buff=0.2)
        self.play(FadeIn(tag, run_time=0.6))
        self.wait(4.6)


# ── B09 ──────────────────────────────────────────────────────────────────
class B09_OptimumCurve(Scene):
    """DAR vs tumor delivery: rises, peaks 4-8 (teal band), falls to crimson. ~17.5s."""

    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1], y_range=[0, 1.05, 0.25],
            x_length=10.0, y_length=4.4,
            axis_config={"color": INK, "stroke_width": 2.0,
                         "include_tip": False,
                         "font_size": 22},
            x_axis_config={"numbers_to_include": [0, 2, 4, 6, 8, 10]},
            y_axis_config={"include_numbers": False},
        )
        axes.to_edge(DOWN, buff=1.0)

        x_lbl = _serif("DAR", size=26, color=INK).next_to(axes.x_axis, DOWN, buff=0.35)
        y_lbl = _serif("tumor delivery", size=26, color=INK).next_to(
            axes.y_axis, LEFT, buff=0.35).rotate(PI / 2)
        y_lbl.next_to(axes.y_axis, LEFT, buff=0.3)

        title = _serif("DAR is an optimum, not a maximum",
                       size=32, color=INK).to_edge(UP, buff=0.5)

        def curve_fn(x):
            # smooth hump peaking around x=6, small at x=0, near-zero at x>=10
            import math
            peak = 6.0
            width = 2.6
            base = 0.08
            return base + (1.0 - base) * math.exp(-((x - peak) ** 2) / (2 * width ** 2))

        curve = axes.plot(curve_fn, x_range=[0.2, 9.8],
                          color=INK, stroke_width=3.6)

        # teal band across 4-8
        band = Polygon(
            axes.c2p(4, 0), axes.c2p(8, 0),
            axes.c2p(8, 1.02), axes.c2p(4, 1.02),
            fill_color=TEAL, fill_opacity=0.16, stroke_width=0,
        )
        band_lbl = _serif("sweet spot (4–8)", size=24, color=TEAL).move_to(
            axes.c2p(6, 1.08))

        # crimson arrows down at both ends
        under_arrow = Arrow(axes.c2p(1.2, 0.7), axes.c2p(1.2, 0.15),
                            color=CRIMSON, buff=0.05, stroke_width=6, tip_length=0.24)
        under_lbl = _serif("under-kill", size=22, color=CRIMSON).next_to(
            under_arrow, RIGHT, buff=0.15)
        over_arrow = Arrow(axes.c2p(9.2, 0.7), axes.c2p(9.2, 0.15),
                           color=CRIMSON, buff=0.05, stroke_width=6, tip_length=0.24)
        over_lbl = _serif("over-aggregate", size=22, color=CRIMSON).next_to(
            over_arrow, LEFT, buff=0.15)

        self.play(FadeIn(title, run_time=0.5))
        self.play(Create(axes, run_time=1.2),
                  FadeIn(x_lbl, run_time=0.4),
                  FadeIn(y_lbl, run_time=0.4))
        self.play(FadeIn(band, run_time=0.6), FadeIn(band_lbl, run_time=0.4))
        self.play(Create(curve, run_time=2.0))
        self.wait(0.6)
        self.play(GrowArrow(under_arrow, run_time=0.6), FadeIn(under_lbl, run_time=0.4),
                  GrowArrow(over_arrow, run_time=0.6), FadeIn(over_lbl, run_time=0.4))
        self.wait(8.6)


# ── B10 ──────────────────────────────────────────────────────────────────
class B10_ExamplePharma(Scene):
    """DAR-4 vs DAR-8 plasma at 24h: teal 68% vs crimson 11% bars. ~18.5s."""

    def construct(self):
        title = _serif("plasma at 24 hours (illustrative)",
                       size=30, color=INK).to_edge(UP, buff=0.6)

        # baseline at y=-2.0
        base_y = -2.0
        left_x = -2.6
        right_x = 2.6

        baseline = Line(LEFT * 5.4 + UP * base_y, RIGHT * 5.4 + UP * base_y,
                        color=INK, stroke_width=2.0)

        # bar heights: 68% and 11% of 4.0 units
        h_left = 4.0 * 0.68
        h_right = 4.0 * 0.11
        bar_w = 1.6

        bar_left = Rectangle(width=bar_w, height=h_left,
                             fill_color=TEAL, fill_opacity=0.85,
                             stroke_color=TEAL, stroke_width=2.0)
        bar_left.move_to(RIGHT * left_x + UP * (base_y + h_left / 2))

        bar_right = Rectangle(width=bar_w, height=h_right,
                              fill_color=CRIMSON, fill_opacity=0.85,
                              stroke_color=CRIMSON, stroke_width=2.0)
        bar_right.move_to(RIGHT * right_x + UP * (base_y + h_right / 2))

        # value labels above each bar
        val_left = _serif("68%", size=44, color=TEAL, weight=BOLD).next_to(
            bar_left, UP, buff=0.20)
        val_right = _serif("11%", size=44, color=CRIMSON, weight=BOLD).next_to(
            bar_right, UP, buff=0.20)

        # category labels below each bar
        cat_left = _serif("DAR-4", size=32, color=INK).next_to(bar_left, DOWN, buff=0.30)
        cat_right = _serif("DAR-8", size=32, color=INK).next_to(bar_right, DOWN, buff=0.30)

        illus_lbl = _mono("illustrative — same antibody, same payload, same dose",
                          size=20, color=SOFT).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(title, run_time=0.5))
        self.play(FadeIn(cat_left, run_time=0.4),
                  FadeIn(cat_right, run_time=0.4),
                  Create(baseline, run_time=0.6))
        self.play(GrowFromEdge(bar_left, DOWN, run_time=1.2),
                  FadeIn(val_left, run_time=0.6))
        self.wait(0.8)
        self.play(GrowFromEdge(bar_right, DOWN, run_time=1.2),
                  FadeIn(val_right, run_time=0.6))
        self.play(FadeIn(illus_lbl, run_time=0.5))
        self.wait(9.2)
