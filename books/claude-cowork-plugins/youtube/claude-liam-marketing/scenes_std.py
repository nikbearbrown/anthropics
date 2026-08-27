from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_ClaudeLiamMarketing(Scene):
    """Beat B02 — SHOW: bar/proportion chart. Narration: Most tools stop at \'write me a blog post.\' The marketing plugin can draft — but """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT I":
            act = Text("ACT I", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Most tools stop at \'write me a blog post"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("\' The marketing plugin can draft - but the point is that it "[:30] if "\' The marketing plugin can draft - but the point is that it " else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "It understands strategy, not just content generation":
            note = Text("It understands strategy, not just content generation"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.10))


class Scene_B06_ClaudeLiamMarketing(Scene):
    """Beat B06 — SHOW: bar/proportion chart. Narration: Campaign planning runs from the initial brief to channel strategy. Tell it what """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Campaign planning runs from the initial brief to channel str"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Tell it what you\'re launching, who you\'re reaching, and what"[:30] if "Tell it what you\'re launching, who you\'re reaching, and what" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.40))


class Scene_B13_ClaudeLiamMarketing(Scene):
    """Beat B13 — SHOW: bar/proportion chart. Narration: Fifteen minutes of this changes the output. Content comes back closer to your vo"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT III":
            act = Text("ACT III", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Fifteen minutes of this changes the output"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Content comes back closer to your voice, ideas grounded in y"[:30] if "Content comes back closer to your voice, ideas grounded in y" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Eighty-percent-right on the first draft beats fifty-percent-":
            note = Text("Eighty-percent-right on the first draft beats fifty-percent-"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.40))


class Scene_B09_ClaudeLiamMarketing(Scene):
    """Beat B09 — SHOW: scattered tiles snap to one aligned grid under 'voice' rule."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT II", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        import random
        random.seed(42)
        positions_scattered = [
            np.array([random.uniform(-4.5, 4.5), random.uniform(-2.0, 1.8), 0])
            for _ in range(9)
        ]
        tiles_scattered = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=0.8, height=0.6,
                             stroke_color=INK, stroke_width=2,
                             fill_color=INK, fill_opacity=0.15)
            .move_to(pos)
            for pos in positions_scattered
        ])
        self.play(FadeIn(tiles_scattered), run_time=0.6)
        self.wait(0.4)

        cols, rows = 3, 3
        gap_x, gap_y = 1.4, 1.0
        grid_origin = np.array([-(cols - 1) * gap_x / 2, -(rows - 1) * gap_y / 2, 0])
        grid_positions = [
            grid_origin + np.array([c * gap_x, r * gap_y, 0])
            for r in range(rows) for c in range(cols)
        ]
        anims = [t.animate.move_to(grid_positions[i]) for i, t in enumerate(tiles_scattered)]
        self.play(*anims, run_time=1.0)

        tiles_scattered[4].set_fill(TERRA, opacity=0.85)
        tiles_scattered[4].set_stroke(TERRA, width=3)
        voice_label = Text("voice", font_size=26, color=TERRA, font=font)
        voice_label.move_to(grid_positions[4])
        self.play(FadeIn(voice_label), run_time=0.4)

        rule = Text("One voice, everywhere.", font_size=28, color=INK, font=font)
        rule.to_edge(DOWN, buff=0.5)
        self.play(Write(rule), run_time=0.5)
        self.wait(max(0.01, 9.00))


class Scene_B11_ClaudeLiamMarketing(Scene):
    """Beat B11 — SHOW: broad vague blob narrows to a sharp specific audience point."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT III", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        blob = Ellipse(width=7.0, height=3.0, stroke_color=INK,
                       stroke_width=2.5, fill_color=INK, fill_opacity=0.12)
        blob.shift(UP * 0.3)
        vague_lbl = Text("professionals", font_size=30, color=INK, font=font)
        vague_lbl.move_to(blob)
        self.play(GrowFromCenter(blob), Write(vague_lbl), run_time=0.8)
        self.wait(0.3)

        narrow_blob = Ellipse(width=1.2, height=2.8, stroke_color=TERRA,
                              stroke_width=3, fill_color=TERRA, fill_opacity=0.20)
        narrow_blob.shift(RIGHT * 1.5 + UP * 0.3)
        specific_txt = Text("small-business owners\nconsidering AI tools", font_size=19,
                            color=INK, font=font)
        specific_txt.next_to(narrow_blob, LEFT, buff=0.3)
        self.play(
            Transform(blob, narrow_blob),
            FadeOut(vague_lbl),
            run_time=1.0,
        )
        self.play(Write(specific_txt), run_time=0.7)

        note = Text("Narrow beats vague.", font_size=28, color=INK, font=font)
        note.to_edge(DOWN, buff=0.5)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.01, 7.50))


class Scene_B17_ClaudeLiamMarketing(Scene):
    """Beat B17 — SHOW: one document fans out into 7 content formats."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT IV", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        src_box = RoundedRectangle(corner_radius=0.15, width=2.2, height=0.9,
                                   stroke_color=INK, stroke_width=2,
                                   fill_color=INK, fill_opacity=0.12)
        src_box.shift(LEFT * 3.5)
        src_lbl = Text("one blog post", font_size=22, color=INK, font=font)
        src_lbl.move_to(src_box)
        self.play(Create(src_box), Write(src_lbl), run_time=0.5)

        outputs = ["social x1", "social x2", "social x3",
                   "social x4", "social x5", "newsletter", "video script"]
        y_positions = np.linspace(2.5, -2.5, len(outputs))
        for i, (label, y) in enumerate(zip(outputs, y_positions)):
            pos = np.array([2.8, y, 0])
            is_accent = i >= 5
            box = RoundedRectangle(corner_radius=0.1, width=1.9, height=0.55,
                                   stroke_color=TERRA if is_accent else INK, stroke_width=2,
                                   fill_color=TERRA if is_accent else INK,
                                   fill_opacity=0.10)
            box.move_to(pos)
            lbl = Text(label, font_size=18, color=INK, font=font)
            lbl.move_to(pos)
            arr = Arrow(src_box.get_right(), pos + LEFT * 0.95,
                        buff=0, color=INK, stroke_width=2, tip_length=0.15)
            self.play(GrowArrow(arr), Create(box), Write(lbl), run_time=0.22)

        note = Text("One source, many cuts.", font_size=26, color=INK, font=font)
        note.to_edge(DOWN, buff=0.35)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.01, 8.50))


class Scene_B22_ClaudeLiamMarketing(Scene):
    """Beat B22 — SHOW: one headline fans out into five angle variants."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT V", font_size=24, color=INK, font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        src_box = RoundedRectangle(corner_radius=0.15, width=2.2, height=0.9,
                                   stroke_color=INK, stroke_width=2,
                                   fill_color=INK, fill_opacity=0.12)
        src_box.shift(LEFT * 3.5)
        src_lbl = Text("one headline", font_size=22, color=INK, font=font)
        src_lbl.move_to(src_box)
        self.play(Create(src_box), Write(src_lbl), run_time=0.5)

        angle_labels = ["angle 1", "angle 2", "angle 3", "angle 4", "angle 5"]
        y_positions = np.linspace(2.0, -2.0, 5)
        for i, (label, y) in enumerate(zip(angle_labels, y_positions)):
            pos = np.array([2.8, y, 0])
            is_accent = i == 2
            box = RoundedRectangle(corner_radius=0.12, width=1.8, height=0.65,
                                   stroke_color=TERRA if is_accent else INK,
                                   stroke_width=3 if is_accent else 2,
                                   fill_color=TERRA if is_accent else INK,
                                   fill_opacity=0.15 if is_accent else 0.08)
            box.move_to(pos)
            lbl = Text(label, font_size=20, color=TERRA if is_accent else INK, font=font)
            lbl.move_to(pos)
            arr = Arrow(src_box.get_right(), pos + LEFT * 0.9,
                        buff=0, color=TERRA if is_accent else INK,
                        stroke_width=2, tip_length=0.15)
            self.play(GrowArrow(arr), Create(box), Write(lbl), run_time=0.35)

        note = Text("Options, not answers.", font_size=26, color=INK, font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.01, 9.00))
