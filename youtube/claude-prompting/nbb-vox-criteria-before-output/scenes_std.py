from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_NbbVoxCriteria(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The foundation scores it: clarity 9 out of 10. Equity lens: 4 out of 10. Measura"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE QUESTION":
            act = Text("THE QUESTION", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The foundation scores it: clarity 9 out of 10":
            line1 = Text("The foundation scores it: clarity 9 out of 10", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Equity lens: 4 out of 10":
            line2 = Text("Equity lens: 4 out of 10", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Measurable outcomes: 3 out of 10":
            line3 = Text("Measurable outcomes: 3 out of 10", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The foundation scores it: clarity 9 out of 10":
            uline = Line(LEFT * min(4.0, len("The foundation scores it: clarity 9 out of 10") * 0.18), RIGHT * min(4.0, len("The foundation scores it: clarity 9 out of 10") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_NbbVoxCriteria(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: Fluency and correctness are independent. An output can be clear, complete-lookin"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Fluency and correctness are independent":
            line1 = Text("Fluency and correctness are independent", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "An output can be clear, complete-looking, and well-structure":
            line2 = Text("An output can be clear, complete-looking, and well-structure", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude produces fluent text optimized for what it has":
            line3 = Text("Claude produces fluent text optimized for what it has", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Fluency and correctness are independent":
            uline = Line(LEFT * min(4.0, len("Fluency and correctness are independent") * 0.18), RIGHT * min(4.0, len("Fluency and correctness are independent") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B05_NbbVoxCriteria(Scene):
    """Beat B05 — SHOW: layer stack diagram. Narration: The reviewer\'s rubric existed. The funder always evaluates equity lens and measu"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["The reviewer\'s rubric existed", "The funder always evaluates equity lens and measurable outco", "Nadia knew this at some level"] if t]
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
                             color="#2A1A0E", stroke_width=2,
                             fill_color="#C8102E" if i == 0 else "#2A1A0E",
                             fill_opacity=0.12 + i * 0.06)
            box.move_to(UP * y)
            txt = Text(lbl[:60], font_size=24, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
            txt.move_to(box)
            self.play(FadeIn(box), Write(txt), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B06_NbbVoxCriteria(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: The mechanism is simple. Claude\'s output is optimized against whatever criteria """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "The mechanism is simple":
            line1 = Text("The mechanism is simple", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Claude\'s output is optimized against whatever criteria it ha":
            line2 = Text("Claude\'s output is optimized against whatever criteria it ha", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Give it no criteria - it optimizes for fluency, generic comp":
            line3 = Text("Give it no criteria - it optimizes for fluency, generic comp", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The mechanism is simple":
            uline = Line(LEFT * min(4.0, len("The mechanism is simple") * 0.18), RIGHT * min(4.0, len("The mechanism is simple") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_NbbVoxCriteria(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Writing criteria before generating forces you to articulate what success means. """
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Writing criteria before generating forces you to articulate ":
            line1 = Text("Writing criteria before generating forces you to articulate ", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "That articulation is the information the prompt actually req":
            line2 = Text("That articulation is the information the prompt actually req", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The criteria don\'t just improve the output - they reveal req":
            line3 = Text("The criteria don\'t just improve the output - they reveal req", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Writing criteria before generating forces you to articulate ":
            uline = Line(LEFT * min(4.0, len("Writing criteria before generating forces you to articulate ") * 0.18), RIGHT * min(4.0, len("Writing criteria before generating forces you to articulate ") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B08_NbbVoxCriteria(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Criteria also give you a review checklist. Instead of reading for general impres"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Criteria also give you a review checklist":
            line1 = Text("Criteria also give you a review checklist", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Instead of reading for general impressiveness - which is how":
            line2 = Text("Instead of reading for general impressiveness - which is how", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Criteria also give you a review checklist":
            uline = Line(LEFT * min(4.0, len("Criteria also give you a review checklist") * 0.18), RIGHT * min(4.0, len("Criteria also give you a review checklist") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B09_NbbVoxCriteria(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: Nadia rewrites: the output must address equity explicitly, name three measurable"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE MECHANISM":
            act = Text("THE MECHANISM", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Nadia rewrites: the output must address equity explicitly, n":
            line1 = Text("Nadia rewrites: the output must address equity explicitly, n", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Now Claude has targets":
            line2 = Text("Now Claude has targets", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Now Nadia has a checklist":
            line3 = Text("Now Nadia has a checklist", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Nadia rewrites: the output must address equity explicitly, n":
            uline = Line(LEFT * min(4.0, len("Nadia rewrites: the output must address equity explicitly, n") * 0.18), RIGHT * min(4.0, len("Nadia rewrites: the output must address equity explicitly, n") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B10_NbbVoxCriteria(Scene):
    """Beat B10 — SHOW: layer stack diagram. Narration: The act of writing criteria before prompting is how you discover what you actual"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE IMPLICATION":
            act = Text("THE IMPLICATION", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["The act of writing criteria before prompting is how you disc", "Grant writers who write acceptance criteria learn something ", "Analysts who write failure criteria learn something about wh"] if t]
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
                             color="#2A1A0E", stroke_width=2,
                             fill_color="#C8102E" if i == 0 else "#2A1A0E",
                             fill_opacity=0.12 + i * 0.06)
            box.move_to(UP * y)
            txt = Text(lbl[:60], font_size=24, color="#2A1A0E", font=font)
            txt.scale(min(1.0, (layer_w - 1.0) / max(0.1, txt.width)))
            txt.move_to(box)
            self.play(FadeIn(box), Write(txt), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B11_NbbVoxCriteria(Scene):
    """Beat B11 — SHOW: concept illustration card. Narration: Project manager Li asks Claude for a status report. She gets 800 polished words."""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Project manager Li asks Claude for a status report":
            line1 = Text("Project manager Li asks Claude for a status report", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "She gets 800 polished words":
            line2 = Text("She gets 800 polished words", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Her director asks: did it cover risk items? She checks - the":
            line3 = Text("Her director asks: did it cover risk items? She checks - the", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Project manager Li asks Claude for a status report":
            uline = Line(LEFT * min(4.0, len("Project manager Li asks Claude for a status report") * 0.18), RIGHT * min(4.0, len("Project manager Li asks Claude for a status report") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B12_NbbVoxCriteria(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: Li adds three criteria: the report must name each flagged risk, state its curren"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "Li adds three criteria: the report must name each flagged ri":
            line1 = Text("Li adds three criteria: the report must name each flagged ri", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The next output: 800 words covering exactly those":
            line2 = Text("The next output: 800 words covering exactly those", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Polished and correct this time - because she specified what ":
            line3 = Text("Polished and correct this time - because she specified what ", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Li adds three criteria: the report must name each flagged ri":
            uline = Line(LEFT * min(4.0, len("Li adds three criteria: the report must name each flagged ri") * 0.18), RIGHT * min(4.0, len("Li adds three criteria: the report must name each flagged ri") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B13_NbbVoxCriteria(Scene):
    """Beat B13 — SHOW: two-column comparison. Narration: Before writing any prompt, ask two questions: what does good look like? And what"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PRACTICE":
            act = Text("THE PRACTICE", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Left column
        left_box = RoundedRectangle(width=5.5, height=3.5, color="#2A1A0E", stroke_width=2,
                                     fill_color="#FFFFFF", fill_opacity=1).shift(LEFT * 3.2)
        left_text = Text("Before writing any prompt, ask two questions: what does good"[:50], font_size=22, color="#2A1A0E", font=font)
        left_text.scale(min(1.0, 5.0 / max(0.1, left_text.width)))
        left_text.move_to(left_box)

        # Right column
        right_box = RoundedRectangle(width=5.5, height=3.5, color="#C8102E", stroke_width=2,
                                      fill_color="#FFFFFF", fill_opacity=1).shift(RIGHT * 3.2)
        right_text = Text("Those answers are the criteria - and the criteria are the ac"[:50] if "Those answers are the criteria - and the criteria are the ac" else "Result", font_size=22, color="#2A1A0E", font=font)
        right_text.scale(min(1.0, 5.0 / max(0.1, right_text.width)))
        right_text.move_to(right_box)

        # Divider
        divider = Line(UP * 2, DOWN * 2, color="#2A1A0E", stroke_width=1.5)

        self.play(FadeIn(left_box), FadeIn(right_box), Create(divider), run_time=0.5)
        self.play(Write(left_text), Write(right_text), run_time=0.8)

        if "":
            note = Text(""[:60], font_size=20, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.3)
            self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.01, 9.00))


class Scene_B14_NbbVoxCriteria(Scene):
    """Beat B14 — SHOW: bar/proportion chart. Narration: Fluency and correctness are independent. Write what good looks like before you g"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "RECAP":
            act = Text("RECAP", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#2A1A0E", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#2A1A0E", fill_color="#2A1A0E", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#C8102E", fill_color="#C8102E", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Fluency and correctness are independent"[:30], font_size=20, color="#2A1A0E", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Write what good looks like before you generate - and correct"[:30] if "Write what good looks like before you generate - and correct" else "Comparison", font_size=20, color="#2A1A0E", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#2A1A0E", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.00))
