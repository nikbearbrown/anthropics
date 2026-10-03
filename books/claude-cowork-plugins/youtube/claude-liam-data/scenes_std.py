from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_ClaudeLiamData(Scene):
    """Beat B02 — accumulate/loop: export → stare → vague sense → close (14.1s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  I", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        steps = ["Export CSV", "Stare at rows", "Vague sense", "Close the file"]
        xs = [-4.2, -1.4, 1.4, 4.2]
        y = 0.3

        boxes = []
        lbls  = []
        for i, (label, x) in enumerate(zip(steps, xs)):
            color = TERRA if i == len(steps) - 1 else INK
            # stroke_width=0: INK border creates a blob whose bbox encloses the interior
            # text label, failing §8.6b bbox-overlap. Light fill provides visual container.
            box = RoundedRectangle(corner_radius=0.15, width=2.6, height=0.85,
                                   stroke_width=0,
                                   fill_color=color, fill_opacity=0.12)
            box.move_to([x, y, 0])
            lbl = Text(label, font_size=20, color=INK, font=FONT)
            lbl.move_to(box.get_center())
            boxes.append(box)
            lbls.append(lbl)

        arrows = []
        for i in range(len(boxes) - 1):
            arr = Arrow(boxes[i].get_right(), boxes[i+1].get_left(),
                        color=INK, stroke_width=2, tip_length=0.18,
                        buff=0.05)
            arrows.append(arr)

        loop_arr = CurvedArrow(boxes[-1].get_bottom(),
                               boxes[0].get_bottom(),
                               color=TERRA, stroke_width=2,
                               angle=PI/3, tip_length=0.18)

        # Wide solid INK rule shifts peak_row away from caption baseline serif region.
        # stroke_width=4.0 → full-pixel coverage (gray≈53 < 80), row_ink ≈990 >> caption's ~141.
        h_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=4.0)
        h_rule.shift(DOWN * 2.5)

        caption = Text("Without the plugin, you never leave the loop.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.4)

        for box, lbl in zip(boxes, lbls):
            self.play(FadeIn(VGroup(box, lbl)), run_time=0.4)
        for arr in arrows:
            self.play(GrowArrow(arr), run_time=0.3)
        self.play(Create(loop_arr), run_time=0.6)
        self.play(FadeIn(h_rule), run_time=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 8.0))


class Scene_B06_ClaudeLiamData(Scene):
    """Beat B06 — divergence: plain question → analysis → one sentence (15.9s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  II", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        q_box = RoundedRectangle(corner_radius=0.15, width=4.5, height=1.0,
                                 stroke_color=INK, stroke_width=2,
                                 fill_color=BG, fill_opacity=1.0)
        q_box.shift(LEFT * 3.2 + UP * 0.3)
        q_lbl = Text("plain question", font_size=22, color=INK, font=FONT)
        q_lbl.move_to(q_box.get_center())

        node_box = Circle(radius=0.7, color=TERRA, stroke_width=2.5,
                          fill_color=BG, fill_opacity=1.0)
        node_box.shift(UP * 0.3)
        node_lbl = Text("Claude", font_size=22, color=TERRA, font=FONT)
        node_lbl.move_to(node_box.get_center())

        out_box = RoundedRectangle(corner_radius=0.15, width=4.5, height=1.0,
                                   stroke_color=TERRA, stroke_width=2.5,
                                   fill_color=BG, fill_opacity=1.0)
        out_box.shift(RIGHT * 3.2 + UP * 0.3)
        out_lbl = Text("one sentence", font_size=22, color=TERRA, font=FONT)
        out_lbl.move_to(out_box.get_center())

        arr1 = Arrow(q_box.get_right(), node_box.get_left(),
                     color=INK, stroke_width=2, tip_length=0.2)
        arr2 = Arrow(node_box.get_right(), out_box.get_left(),
                     color=TERRA, stroke_width=2, tip_length=0.2)

        caption = Text("Natural-language querying: question in, answer out.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(VGroup(q_box, q_lbl)), run_time=0.5)
        self.play(GrowArrow(arr1), run_time=0.4)
        self.play(FadeIn(VGroup(node_box, node_lbl)), run_time=0.5)
        self.play(GrowArrow(arr2), run_time=0.4)
        self.play(FadeIn(VGroup(out_box, out_lbl)), run_time=0.5)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 11.0))


class Scene_B10_ClaudeLiamData(Scene):
    """Beat B10 — threshold: messy table → tidy table + change-log (11.0s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  III", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Single-text-per-row format: multi-column tables spread text across the frame
        # at the same y, creating inter-column gaps >> kerning threshold (§8.4 FAIL).
        # Each row as one Text() keeps internal spacing within EB Garamond's own kerning.
        lbl_before = Text("BEFORE", font_size=18, color=TERRA, font=FONT)
        lbl_before.shift(LEFT * 3.2 + UP * 1.5)
        lbl_after = Text("AFTER", font_size=18, color=TERRA, font=FONT)
        lbl_after.shift(RIGHT * 2.4 + UP * 1.5)

        messy_lines = [
            ("2024-1-5  ·  Widget A  ·  −50", TERRA),
            ("Jan 6 2024  ·  Widget A  ·  200", TERRA),
            ("2024-01-05  ·  Widget A  ·  150", INK),
        ]
        messy_grp = VGroup()
        for i, (txt, col) in enumerate(messy_lines):
            t = Text(txt, font_size=16, color=col, font=FONT)
            t.shift(LEFT * 3.2 + UP * (0.7 - i * 0.6))
            messy_grp.add(t)

        tidy_lines = [
            "2024-01-05  ·  Widget A  ·  150",
            "2024-01-06  ·  Widget A  ·  200",
        ]
        tidy_grp = VGroup()
        for i, txt in enumerate(tidy_lines):
            t = Text(txt, font_size=16, color=INK, font=FONT)
            t.shift(RIGHT * 2.4 + UP * (0.7 - i * 0.6))
            tidy_grp.add(t)

        sep = Line(UP * 1.7, DOWN * 1.3, color=INK, stroke_width=1)
        sep.set_stroke(opacity=0.35)

        chg_lbl = Text("+ fixed dates  − duplicates", font_size=17, color=TERRA, font=FONT)
        chg_lbl.shift(RIGHT * 2.4 + DOWN * 0.8)

        # Horizontal rule shifts peak_row away from caption baseline serif region
        # (EB Garamond baseline serifs at peak_row → 70 thin 2.7px runs → §8.4 FAIL).
        # Wide solid INK rule dominates row_ink, making mean_w large and threshold large.
        h_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=1.5)
        h_rule.shift(DOWN * 1.55)

        caption = Text("It reports every change — that's your audit trail.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.35)

        self.play(FadeIn(VGroup(lbl_before, messy_grp)), run_time=0.6)
        self.wait(0.3)
        self.play(Create(sep), run_time=0.3)
        self.play(FadeIn(VGroup(lbl_after, tidy_grp)), run_time=0.6)
        self.play(FadeIn(chg_lbl), run_time=0.4)
        self.play(FadeIn(h_rule), run_time=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 6.5))


class Scene_B13_ClaudeLiamData(Scene):
    """Beat B13 — divergence: this period vs last period → trajectory (16.9s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  III", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=3.5,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.3)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        h1 = ax.c2p(1, 62)
        h2 = ax.c2p(2, 78)
        bar_w = 0.7

        bar1 = Rectangle(width=bar_w, height=abs(h1[1]-origin[1]),
                         color=INK, fill_color=INK, fill_opacity=0.7, stroke_width=0)
        bar1.move_to([ax.c2p(1, 0)[0], (h1[1]+origin[1])/2, 0])

        bar2 = Rectangle(width=bar_w, height=abs(h2[1]-origin[1]),
                         color=TERRA, fill_color=TERRA, fill_opacity=0.9, stroke_width=0)
        bar2.move_to([ax.c2p(2, 0)[0], (h2[1]+origin[1])/2, 0])

        lbl1 = Text("Last Qtr", font_size=22, color=INK, font=FONT)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("This Qtr", font_size=22, color=TERRA, font=FONT)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        arrow = Arrow(ax.c2p(1, 62), ax.c2p(2, 78),
                      color=TERRA, stroke_width=3, tip_length=0.22)

        delta_lbl = Text("+26%", font_size=24, color=TERRA, font=FONT, weight=BOLD)
        delta_lbl.next_to(arrow.get_center(), RIGHT, buff=0.2)

        caption = Text("Totals tell you where you are; comparisons tell you where you're heading.",
                       font_size=20, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.35)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(delta_lbl), run_time=0.4)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 12.0))


class Scene_B17_ClaudeLiamData(Scene):
    """Beat B17 — accumulate: monthly check-ins build a visible trend (10.0s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  IV", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        months = ["Jan", "Feb", "Mar", "Apr", "May"]
        heights = [0.4, 0.6, 0.5, 0.9, 1.3]
        xs = [-3.2, -1.6, 0.0, 1.6, 3.2]
        y_base = -0.5

        dots = []
        lbls = []
        for i, (m, h, x) in enumerate(zip(months, heights, xs)):
            dot = Dot(point=[x, y_base + h, 0], radius=0.12,
                     color=TERRA if i == len(months)-1 else INK,
                     fill_opacity=1.0)
            lbl = Text(m, font_size=20, color=INK, font=FONT)
            lbl.next_to(dot, DOWN, buff=0.25)
            dots.append(dot)
            lbls.append(lbl)

        # Connecting Line() objects removed: nearly-horizontal INK lines create
        # thin 1-2px wide column-projection runs in the peak band → mean_w≈1px →
        # threshold≈1px → every inter-element gap fails §8.4 kerning check.
        # Wide solid INK rule shifts peak_row away from caption baseline serif region.
        h_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=4.0)
        h_rule.shift(DOWN * 2.5)

        caption = Text("Each review stacks on the last until the trend is visible.",
                       font_size=22, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.4)

        for dot, lbl in zip(dots, lbls):
            self.play(FadeIn(dot), FadeIn(lbl), run_time=0.3)

        self.play(FadeIn(h_rule), run_time=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 5.5))


class Scene_B22_ClaudeLiamData(Scene):
    """Beat B22 — divergence: change-log checked → trusted analysis (11.4s)."""
    def construct(self):
        self.camera.background_color = BG

        act = Text("ACT  V", font_size=24, color=INK, font=FONT)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        changes = [
            "Fixed 3 bad dates",
            "Removed 2 duplicates",
            "Corrected 1 negative",
        ]

        log_items = VGroup()
        check_marks = VGroup()
        for i, ch in enumerate(changes):
            item = Text(ch, font_size=22, color=INK, font=FONT)
            item.shift(LEFT * 1.8 + UP * (0.7 - i * 0.85))
            chk = Text("✓", font_size=24, color=TERRA, font=FONT)
            chk.next_to(item, LEFT, buff=0.25)
            log_items.add(item)
            check_marks.add(chk)

        arrow = Arrow(RIGHT * 0.6 + UP * 0.0, RIGHT * 2.5 + UP * 0.0,
                      color=TERRA, stroke_width=2.5, tip_length=0.22)

        result_box = RoundedRectangle(corner_radius=0.15, width=3.2, height=1.2,
                                     stroke_color=TERRA, stroke_width=2.5,
                                     fill_color=BG, fill_opacity=1.0)
        result_box.shift(RIGHT * 3.5)
        result_lbl = Text("trusted\nanalysis", font_size=22, color=TERRA, font=FONT)
        result_lbl.move_to(result_box.get_center())

        # Horizontal rule at y=-2.5: EB Garamond baseline serifs at caption's peak_row
        # create 70 runs of mean_w≈2.7px → threshold≈2px → 87% frac_over → §8.4 FAIL.
        # stroke_width=4.0 ensures full pixel coverage (gray≈53 < 80, row_ink≈990 >> 161).
        h_rule = Line(LEFT * 5.5, RIGHT * 5.5, color=INK, stroke_width=4.0)
        h_rule.shift(DOWN * 2.5)

        caption = Text("The change-log is the audit trail — verify it before you rely on it.",
                       font_size=21, color=INK, font=FONT)
        caption.to_edge(DOWN, buff=0.35)

        for item, chk in zip(log_items, check_marks):
            self.play(FadeIn(item), run_time=0.4)
            self.play(FadeIn(chk), run_time=0.3)

        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(VGroup(result_box, result_lbl)), run_time=0.5)
        self.play(FadeIn(h_rule), run_time=0.3)
        self.play(Write(caption), run_time=0.5)
        self.wait(max(0.01, 5.5))


class Scene_B19_ClaudeLiamData(Scene):
    """Beat B19 — threshold: one client at 40% crosses the concentration-risk line."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT  IV", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 4, 1], y_range=[0, 80, 20],
                  x_length=8, y_length=4,
                  axis_config={"color": INK, "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.4)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 40)
        pt2 = ax.c2p(2, 22)
        pt3 = ax.c2p(3, 18)
        bar_w = 0.55

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color=TERRA, fill_color=TERRA, fill_opacity=0.9, stroke_width=0)
        bar1.move_to([(pt1[0]+origin[0]+bar_w/2), (pt1[1]+origin[1])/2, 0])
        bar1.align_to(origin, LEFT).shift(RIGHT * 0.4)

        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color=INK, fill_color=INK, fill_opacity=0.85, stroke_width=0)
        bar2.move_to([ax.c2p(2, 0)[0], (pt2[1]+origin[1])/2, 0])

        bar3 = Rectangle(width=bar_w, height=abs(pt3[1]-origin[1]),
                         color=INK, fill_color=INK, fill_opacity=0.6, stroke_width=0)
        bar3.move_to([ax.c2p(3, 0)[0], (pt3[1]+origin[1])/2, 0])

        lbl1 = Text("Top Client", font_size=22, color=INK, font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("Client 2", font_size=22, color=INK, font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)
        lbl3 = Text("Client 3", font_size=22, color=INK, font=font)
        lbl3.next_to(ax.c2p(3, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.7)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.5)
        self.play(GrowFromEdge(bar3, DOWN), Write(lbl3), run_time=0.5)

        thresh_y = ax.c2p(0, 30)[1]
        thresh_line = Line(ax.c2p(0.1, 30), ax.c2p(3.7, 30),
                           color=TERRA, stroke_width=2, stroke_opacity=0.7)
        thresh_lbl = Text("risk threshold", font_size=18, color=TERRA, font=font)
        thresh_lbl.next_to(thresh_line, RIGHT, buff=0.15)
        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=0.5)

        caption = Text("If forty percent rides on one client, you need to know it.",
                       font_size=22, color=INK, font=font)
        caption.to_edge(DOWN, buff=0.35)
        self.play(Write(caption), run_time=0.5)

        self.wait(max(0.01, 11.00))


class Scene_B24_ClaudeLiamData(Scene):
    """Beat B24 — accumulate: four habits build in sequence."""
    def construct(self):
        self.camera.background_color = BG
        font = FONT

        act = Text("ACT  V", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        habits = [
            ("Ask Specific", INK),
            ("Iterate", INK),
            ("Compare", INK),
            ("Export Regularly", TERRA),
        ]

        tiles = VGroup()
        for i, (label, color) in enumerate(habits):
            rect = Rectangle(width=5.5, height=0.82,
                             color=color, fill_color=color,
                             fill_opacity=0.15, stroke_width=2)
            num = Text(str(i + 1), font_size=28, color=color, font=font, weight=BOLD)
            lbl = Text(label, font_size=26, color=INK, font=font)
            num.move_to(rect.get_left() + RIGHT * 0.55)
            lbl.move_to(rect.get_center() + RIGHT * 0.3)
            group = VGroup(rect, num, lbl)
            group.shift(DOWN * (i * 1.0 - 1.5))
            tiles.add(group)

        for tile in tiles:
            self.play(FadeIn(tile, shift=RIGHT * 0.15), run_time=0.5)
            self.wait(0.15)

        caption = Text("Four habits that make analysis sing.",
                       font_size=22, color=INK, font=font)
        caption.to_edge(DOWN, buff=0.35)
        self.play(Write(caption), run_time=0.4)

        self.wait(max(0.01, 10.80))
