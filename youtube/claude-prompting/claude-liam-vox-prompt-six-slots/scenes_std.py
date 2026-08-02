from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_ClaudeLiamVox(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: She asked for an improved introduction. She got a polished rewrite — optimized f"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE QUESTION":
            act = Text("THE QUESTION", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "She asked for an improved introduction":
            line1 = Text("She asked for an improved introduction", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "She got a polished rewrite - optimized for the wrong audienc":
            line2 = Text("She got a polished rewrite - optimized for the wrong audienc", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Why did a well-meaning improvement produce the wrong output?":
            line3 = Text("Why did a well-meaning improvement produce the wrong output?", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "She asked for an improved introduction":
            uline = Line(LEFT * min(4.0, len("She asked for an improved introduction") * 0.18), RIGHT * min(4.0, len("She asked for an improved introduction") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_ClaudeLiamVox(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: A prompt is a specification. It covers six slots: task, context, sources, constr"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A prompt is a specification":
            line1 = Text("A prompt is a specification", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It covers six slots: task, context, sources, constraints, fo":
            line2 = Text("It covers six slots: task, context, sources, constraints, fo", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "\'Improve this\' answers exactly none of them - so Claude supp":
            line3 = Text("\'Improve this\' answers exactly none of them - so Claude supp", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A prompt is a specification":
            uline = Line(LEFT * min(4.0, len("A prompt is a specification") * 0.18), RIGHT * min(4.0, len("A prompt is a specification") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B05_ClaudeLiamVox(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: The guesses are plausible. Task: make it clearer. Context: general academic read"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The guesses are plausible":
            line1 = Text("The guesses are plausible", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Task: make it clearer":
            line2 = Text("Task: make it clearer", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Context: general academic reader":
            line3 = Text("Context: general academic reader", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The guesses are plausible":
            uline = Line(LEFT * min(4.0, len("The guesses are plausible") * 0.18), RIGHT * min(4.0, len("The guesses are plausible") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B06_ClaudeLiamVox(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: The slot that matters most: context. Dr. Osei\'s actual context: a specialist com"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The slot that matters most: context":
            line1 = Text("The slot that matters most: context", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Osei\'s actual context: a specialist committee that already k":
            line2 = Text("Osei\'s actual context: a specialist committee that already k", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "General-audience framing is exactly wrong":
            line3 = Text("General-audience framing is exactly wrong", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The slot that matters most: context":
            uline = Line(LEFT * min(4.0, len("The slot that matters most: context") * 0.18), RIGHT * min(4.0, len("The slot that matters most: context") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_ClaudeLiamVox(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: The same input — the same raw text — produces two different outputs depending on"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The same input - the same raw text - produces two different ":
            line1 = Text("The same input - the same raw text - produces two different ", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The text is not the specification":
            line2 = Text("The text is not the specification", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The slots are the specification":
            line3 = Text("The slots are the specification", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The same input - the same raw text - produces two different ":
            uline = Line(LEFT * min(4.0, len("The same input - the same raw text - produces two different ") * 0.18), RIGHT * min(4.0, len("The same input - the same raw text - produces two different ") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B08_ClaudeLiamVox(Scene):
    """Beat B08 — SHOW: bar/proportion chart. Narration: Each slot you fill removes a generic guess. Fill all six and Claude\'s guesses go"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Each slot you fill removes a generic guess"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Fill all six and Claude\'s guesses go to zero - the output is"[:30] if "Fill all six and Claude\'s guesses go to zero - the output is" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.00))


class Scene_B09_ClaudeLiamVox(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: Dr. Osei fills the slots: task — tighten the gap statement. Context — specialist"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Osei fills the slots: task - tighten the gap statement":
            line1 = Text("Osei fills the slots: task - tighten the gap statement", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Context - specialist review committee":
            line2 = Text("Context - specialist review committee", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Sources - only use evidence already in the text":
            line3 = Text("Sources - only use evidence already in the text", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Osei fills the slots: task - tighten the gap statement":
            uline = Line(LEFT * min(4.0, len("Osei fills the slots: task - tighten the gap statement") * 0.18), RIGHT * min(4.0, len("Osei fills the slots: task - tighten the gap statement") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B10_ClaudeLiamVox(Scene):
    """Beat B10 — SHOW: concept illustration card. Narration: The six slots apply to every request. Not just editing. Summarize this. Analyze """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE IMPLICATION":
            act = Text("THE IMPLICATION", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The six slots apply to every request":
            line1 = Text("The six slots apply to every request", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Not just editing":
            line2 = Text("Not just editing", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Summarize this":
            line3 = Text("Summarize this", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The six slots apply to every request":
            uline = Line(LEFT * min(4.0, len("The six slots apply to every request") * 0.18), RIGHT * min(4.0, len("The six slots apply to every request") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B11_ClaudeLiamVox(Scene):
    """Beat B11 — SHOW: concept illustration card. Narration: Jamie asks Claude to analyze this dataset. No context, no constraints, no format"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Jamie asks Claude to analyze this dataset":
            line1 = Text("Jamie asks Claude to analyze this dataset", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "No context, no constraints, no format":
            line2 = Text("No context, no constraints, no format", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude produces a summary of descriptive statistics - which ":
            line3 = Text("Claude produces a summary of descriptive statistics - which ", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Jamie asks Claude to analyze this dataset":
            uline = Line(LEFT * min(4.0, len("Jamie asks Claude to analyze this dataset") * 0.18), RIGHT * min(4.0, len("Jamie asks Claude to analyze this dataset") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B12_ClaudeLiamVox(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: Jamie fills the task slot: identify outliers, flag any value more than three sta"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Jamie fills the task slot: identify outliers, flag any value":
            line1 = Text("Jamie fills the task slot: identify outliers, flag any value", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "One slot filled, five still open":
            line2 = Text("One slot filled, five still open", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "But the one that mattered most - what kind of analysis - is ":
            line3 = Text("But the one that mattered most - what kind of analysis - is ", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Jamie fills the task slot: identify outliers, flag any value":
            uline = Line(LEFT * min(4.0, len("Jamie fills the task slot: identify outliers, flag any value") * 0.18), RIGHT * min(4.0, len("Jamie fills the task slot: identify outliers, flag any value") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B13_ClaudeLiamVox(Scene):
    """Beat B13 — SHOW: concept illustration card. Narration: Before you submit a vague request, spend thirty seconds on each slot. Task: what"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE PRACTICE":
            act = Text("THE PRACTICE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Before you submit a vague request, spend thirty seconds on e":
            line1 = Text("Before you submit a vague request, spend thirty seconds on e", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Task: what specific verb? Context: who reads this, in what s":
            line2 = Text("Task: what specific verb? Context: who reads this, in what s", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Before you submit a vague request, spend thirty seconds on e":
            uline = Line(LEFT * min(4.0, len("Before you submit a vague request, spend thirty seconds on e") * 0.18), RIGHT * min(4.0, len("Before you submit a vague request, spend thirty seconds on e") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B14_ClaudeLiamVox(Scene):
    """Beat B14 — SHOW: concept illustration card. Narration: A prompt is a specification covering six slots. Leave them empty and Claude gues"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "RECAP":
            act = Text("RECAP", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#D97757", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "A prompt is a specification covering six slots":
            line1 = Text("A prompt is a specification covering six slots", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Leave them empty and Claude guesses":
            line2 = Text("Leave them empty and Claude guesses", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Fill them and Claude has something to aim at":
            line3 = Text("Fill them and Claude has something to aim at", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A prompt is a specification covering six slots":
            uline = Line(LEFT * min(4.0, len("A prompt is a specification covering six slots") * 0.18), RIGHT * min(4.0, len("A prompt is a specification covering six slots") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))
