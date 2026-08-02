from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_OutcomeBeforeTopic(Scene):
    """Beat B01 — SHOW: concept illustration card. Narration: Two teachers ask Claude for the same lesson. One gets a list of activities that """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Two teachers ask Claude for the same lesson":
            line1 = Text("Two teachers ask Claude for the same lesson", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "One gets a list of activities that cover the topic":
            line2 = Text("One gets a list of activities that cover the topic", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The other gets a lesson that fixes the misconception her stu":
            line3 = Text("The other gets a lesson that fixes the misconception her stu", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Two teachers ask Claude for the same lesson":
            uline = Line(LEFT * min(4.0, len("Two teachers ask Claude for the same lesson") * 0.18), RIGHT * min(4.0, len("Two teachers ask Claude for the same lesson") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B03_OutcomeBeforeTopic(Scene):
    """Beat B03 — SHOW: two-column comparison. Narration: Two prompts. Same topic. Same lesson request. The outputs diverge completely. Th"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#3D3929", stroke_width=2,
                                     fill_color="#F2F0E9", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("Two prompts"[:50], font_size=22, color="#3D3929", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#D97757", stroke_width=2,
                                      fill_color="#F2F0E9", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("Same topic"[:50] if "Same topic" else "Result", font_size=22, color="#3D3929", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#3D3929", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "Same lesson request":
            note = Text("Same lesson request"[:60], font_size=20, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 9.00))


class Scene_B04_OutcomeBeforeTopic(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: Here is how most teachers think about lesson-planning prompts. Describe the topi"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Here is how most teachers think about lesson-planning prompt":
            line1 = Text("Here is how most teachers think about lesson-planning prompt", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Describe the topic well":
            line2 = Text("Describe the topic well", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude knows photosynthesis":
            line3 = Text("Claude knows photosynthesis", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Here is how most teachers think about lesson-planning prompt":
            uline = Line(LEFT * min(4.0, len("Here is how most teachers think about lesson-planning prompt") * 0.18), RIGHT * min(4.0, len("Here is how most teachers think about lesson-planning prompt") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B05_OutcomeBeforeTopic(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: But Claude does not know your learning target. It knows what you asked for. Topi"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "But Claude does not know your learning target":
            line1 = Text("But Claude does not know your learning target", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It knows what you asked for":
            line2 = Text("It knows what you asked for", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Topic coverage is not the same as learning design":
            line3 = Text("Topic coverage is not the same as learning design", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "But Claude does not know your learning target":
            uline = Line(LEFT * min(4.0, len("But Claude does not know your learning target") * 0.18), RIGHT * min(4.0, len("But Claude does not know your learning target") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B06_OutcomeBeforeTopic(Scene):
    """Beat B06 — SHOW: pipeline / handoff flow. Narration: Claude is an activity generator. Left to itself, it gives you activities. It doe"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Act label at top
        if "":
            act = Text("", font_size=24, color="#3D3929", font=font, slant=NORMAL)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Build pipeline boxes that reveal left-to-right
        stages = []
        labels_text = [t for t in ["Claude is an activity generator", "Left to itself, it gives you activities", "It does not know where your class is in the sequence, what s"] if t]
        if not labels_text:
            labels_text = ["Input", "Process", "Output"]

        n = len(labels_text)
        spacing = 8.0 / n
        start_x = -(n - 1) * spacing / 2

        boxes = VGroup()
        arrows = VGroup()
        box_mobs = []
        for i, lbl in enumerate(labels_text):
            box = RoundedRectangle(width=spacing * 0.85, height=1.6,
                                   color="#3D3929", stroke_width=2,
                                   fill_color="#F2F0E9", fill_opacity=1)
            box.move_to(RIGHT * (start_x + i * spacing))
            txt = Text(lbl, font_size=20, color="#3D3929", font=font)
            txt.scale(min(1.0, (spacing * 0.8 - 0.3) / max(0.1, txt.width)))
            txt.move_to(box)
            grp = VGroup(box, txt)
            box_mobs.append(grp)
            boxes.add(grp)
            if i > 0:
                arr = Arrow(box_mobs[i-1].get_right(), box.get_left(),
                            buff=0.1, color="#D97757", stroke_width=3,
                            max_tip_length_to_length_ratio=0.15)
                arrows.add(arr)

        # Reveal stages with arrows
        for i, mob in enumerate(box_mobs):
            self.play(FadeIn(mob), run_time=0.5)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_OutcomeBeforeTopic(Scene):
    """Beat B07 — SHOW: bar/proportion chart. Narration: Prompt A: Give me a lesson on fractions. Prompt B: Sixth-grade lesson on dividin"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Prompt A: Give me a lesson on fractions"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Prompt B: Sixth-grade lesson on dividing fractions"[:30] if "Prompt B: Sixth-grade lesson on dividing fractions" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Students believe dividing always makes things smaller - need":
            note = Text("Students believe dividing always makes things smaller - need"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.00))


class Scene_B08_OutcomeBeforeTopic(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Prompt A produces three definitional exercises. Prompt B produces a prediction e"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Prompt A produces three definitional exercises":
            line1 = Text("Prompt A produces three definitional exercises", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Prompt B produces a prediction exercise that forces students":
            line2 = Text("Prompt B produces a prediction exercise that forces students", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Prompt A produces three definitional exercises":
            uline = Line(LEFT * min(4.0, len("Prompt A produces three definitional exercises") * 0.18), RIGHT * min(4.0, len("Prompt A produces three definitional exercises") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B09_OutcomeBeforeTopic(Scene):
    """Beat B09 — SHOW: layer stack diagram. Narration: Every piece of information in the outcome-anchored prompt — the grade level, the"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["Every piece of information in the outcome-anchored prompt - ", "He just had not written it down before opening Claude", ""] if t]
        if not layers_text:
            layers_text = ["Layer 1", "Layer 2", "Layer 3"]

        n = len(layers_text)
        layer_h = 1.2
        layer_w = 9.0
        start_y = (n - 1) * layer_h / 2

        for i, lbl in enumerate(reversed(layers_text)):
            y = start_y - i * layer_h
            alpha = 0.3 + i * 0.2
            box = Rectangle(width=layer_w, height=layer_h * 0.85,
                             color="#3D3929", stroke_width=2,
                             fill_color="#D97757" if i == 0 else "#3D3929",
                             fill_opacity=0.12 + i * 0.06)
            box.move_to(UP * y)
            txt = Text(lbl[:60], font_size=24, color="#3D3929", font=font)
            txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
            txt.move_to(box)
            self.play(FadeIn(box), Write(txt), run_time=0.5)

        self.wait(max(0.01, 10.00))


class Scene_B10_OutcomeBeforeTopic(Scene):
    """Beat B10 — SHOW: concept illustration card. Narration: What changes when Claude knows the target? The warm-up surfaces the misconceptio"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "What changes when Claude knows the target? The warm-up surfa":
            line1 = Text("What changes when Claude knows the target? The warm-up surfa", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The activities build toward the connection he specified":
            line2 = Text("The activities build toward the connection he specified", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The formative check matches his evidence definition":
            line3 = Text("The formative check matches his evidence definition", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "What changes when Claude knows the target? The warm-up surfa":
            uline = Line(LEFT * min(4.0, len("What changes when Claude knows the target? The warm-up surfa") * 0.18), RIGHT * min(4.0, len("What changes when Claude knows the target? The warm-up surfa") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B11_OutcomeBeforeTopic(Scene):
    """Beat B11 — SHOW: bar/proportion chart. Narration: The practice: before you open Claude, write one sentence — what will students be"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("The practice: before you open Claude, write one sentence - w"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("A performance"[:30] if "A performance" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Students will explain why six divided by one-half equals twe":
            note = Text("Students will explain why six divided by one-half equals twe"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.00))


class Scene_B12_OutcomeBeforeTopic(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: Claude cannot write your learning outcome for you. You know the class. You know """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Claude cannot write your learning outcome for you":
            line1 = Text("Claude cannot write your learning outcome for you", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "You know the class":
            line2 = Text("You know the class", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "You know the misconception":
            line3 = Text("You know the misconception", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Claude cannot write your learning outcome for you":
            uline = Line(LEFT * min(4.0, len("Claude cannot write your learning outcome for you") * 0.18), RIGHT * min(4.0, len("Claude cannot write your learning outcome for you") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B13_OutcomeBeforeTopic(Scene):
    """Beat B13 — SHOW: concept illustration card. Narration: Topic coverage is not learning design. Outcome before topic — every time."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "":
            act = Text("", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Topic coverage is not learning design":
            line1 = Text("Topic coverage is not learning design", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Outcome before topic - every time":
            line2 = Text("Outcome before topic - every time", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Topic coverage is not learning design":
            uline = Line(LEFT * min(4.0, len("Topic coverage is not learning design") * 0.18), RIGHT * min(4.0, len("Topic coverage is not learning design") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))
