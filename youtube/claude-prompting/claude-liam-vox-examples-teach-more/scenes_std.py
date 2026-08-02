from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_ClaudeLiamVox(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: She wanted Claude to copy the paragraph structure. Instead it copied the casual """
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
        if "She wanted Claude to copy the paragraph structure":
            line1 = Text("She wanted Claude to copy the paragraph structure", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Instead it copied the casual register, hedging language, and":
            line2 = Text("Instead it copied the casual register, hedging language, and", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Why did the example teach more than she intended?":
            line3 = Text("Why did the example teach more than she intended?", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "She wanted Claude to copy the paragraph structure":
            uline = Line(LEFT * min(4.0, len("She wanted Claude to copy the paragraph structure") * 0.18), RIGHT * min(4.0, len("She wanted Claude to copy the paragraph structure") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_ClaudeLiamVox(Scene):
    """Beat B04 — SHOW: bar/proportion chart. Narration: Instructions in prompts are explicit — they describe what you want. But an examp"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE PROBLEM":
            act = Text("THE PROBLEM", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Instructions in prompts are explicit - they describe what yo"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("But an example is an instruction in disguise"[:30] if "But an example is an instruction in disguise" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "It teaches by demonstration across every feature it contains":
            note = Text("It teaches by demonstration across every feature it contains"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B05_ClaudeLiamVox(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: A memo has observable features. Structure: topics in paragraphs. Register: casua"""
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
        if "A memo has observable features":
            line1 = Text("A memo has observable features", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Structure: topics in paragraphs":
            line2 = Text("Structure: topics in paragraphs", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Register: casual, hedged":
            line3 = Text("Register: casual, hedged", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A memo has observable features":
            uline = Line(LEFT * min(4.0, len("A memo has observable features") * 0.18), RIGHT * min(4.0, len("A memo has observable features") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B06_ClaudeLiamVox(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: Claude pattern-matches across all of them at once. It cannot know which features"""
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
        if "Claude pattern-matches across all of them at once":
            line1 = Text("Claude pattern-matches across all of them at once", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It cannot know which features you consider essential and whi":
            line2 = Text("It cannot know which features you consider essential and whi", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "So it treats the example as a complete specification - and l":
            line3 = Text("So it treats the example as a complete specification - and l", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Claude pattern-matches across all of them at once":
            uline = Line(LEFT * min(4.0, len("Claude pattern-matches across all of them at once") * 0.18), RIGHT * min(4.0, len("Claude pattern-matches across all of them at once") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_ClaudeLiamVox(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Structure passes through. But so does register, sentence length, hedging density"""
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
        if "Structure passes through":
            line1 = Text("Structure passes through", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "But so does register, sentence length, hedging density, and ":
            line2 = Text("But so does register, sentence length, hedging density, and ", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The board report returns sounding like the memo - because it":
            line3 = Text("The board report returns sounding like the memo - because it", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Structure passes through":
            uline = Line(LEFT * min(4.0, len("Structure passes through") * 0.18), RIGHT * min(4.0, len("Structure passes through") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B08_ClaudeLiamVox(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: Annotation changes this. You tell Claude which features to copy — and which to i"""
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
        if "Annotation changes this":
            line1 = Text("Annotation changes this", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "You tell Claude which features to copy - and which to ignore":
            line2 = Text("You tell Claude which features to copy - and which to ignore", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The example stays; the specification narrows it":
            line3 = Text("The example stays; the specification narrows it", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Annotation changes this":
            uline = Line(LEFT * min(4.0, len("Annotation changes this") * 0.18), RIGHT * min(4.0, len("Annotation changes this") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B09_ClaudeLiamVox(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: Priya adds three lines to her prompt: copy the paragraph-per-topic structure. No"""
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
        if "Priya adds three lines to her prompt: copy the paragraph-per":
            line1 = Text("Priya adds three lines to her prompt: copy the paragraph-per", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Not the casual tone":
            line2 = Text("Not the casual tone", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Not the hedging language":
            line3 = Text("Not the hedging language", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Priya adds three lines to her prompt: copy the paragraph-per":
            uline = Line(LEFT * min(4.0, len("Priya adds three lines to her prompt: copy the paragraph-per") * 0.18), RIGHT * min(4.0, len("Priya adds three lines to her prompt: copy the paragraph-per") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B10_ClaudeLiamVox(Scene):
    """Beat B10 — SHOW: concept illustration card. Narration: This holds for any example — a quote you liked, a competitor\'s press release, a """
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
        if "This holds for any example - a quote you liked, a competitor":
            line1 = Text("This holds for any example - a quote you liked, a competitor", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Each contains dozens of features":
            line2 = Text("Each contains dozens of features", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Without annotation, all of them teach":
            line3 = Text("Without annotation, all of them teach", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "This holds for any example - a quote you liked, a competitor":
            uline = Line(LEFT * min(4.0, len("This holds for any example - a quote you liked, a competitor") * 0.18), RIGHT * min(4.0, len("This holds for any example - a quote you liked, a competitor") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B11_ClaudeLiamVox(Scene):
    """Beat B11 — SHOW: concept illustration card. Narration: Marco writes a product blog post. He pastes a competitor\'s post he admires and a"""
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
        if "Marco writes a product blog post":
            line1 = Text("Marco writes a product blog post", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "He pastes a competitor\'s post he admires and asks Claude to ":
            line2 = Text("He pastes a competitor\'s post he admires and asks Claude to ", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The output is punchy, short-sentenced, and uses three exclam":
            line3 = Text("The output is punchy, short-sentenced, and uses three exclam", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Marco writes a product blog post":
            uline = Line(LEFT * min(4.0, len("Marco writes a product blog post") * 0.18), RIGHT * min(4.0, len("Marco writes a product blog post") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B12_ClaudeLiamVox(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: He adds one line: copy the punchy short sentences. Not the exclamation points — """
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
        if "He adds one line: copy the punchy short sentences":
            line1 = Text("He adds one line: copy the punchy short sentences", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Not the exclamation points - we never use those":
            line2 = Text("Not the exclamation points - we never use those", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Next output: punchy, short, zero exclamation points":
            line3 = Text("Next output: punchy, short, zero exclamation points", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "He adds one line: copy the punchy short sentences":
            uline = Line(LEFT * min(4.0, len("He adds one line: copy the punchy short sentences") * 0.18), RIGHT * min(4.0, len("He adds one line: copy the punchy short sentences") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B13_ClaudeLiamVox(Scene):
    """Beat B13 — SHOW: concept illustration card. Narration: The practice: before you paste any example, write two sentences. Which features """
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
        if "The practice: before you paste any example, write two senten":
            line1 = Text("The practice: before you paste any example, write two senten", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Which features should Claude copy? Which should it ignore? T":
            line2 = Text("Which features should Claude copy? Which should it ignore? T", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The practice: before you paste any example, write two senten":
            uline = Line(LEFT * min(4.0, len("The practice: before you paste any example, write two senten") * 0.18), RIGHT * min(4.0, len("The practice: before you paste any example, write two senten") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B14_ClaudeLiamVox(Scene):
    """Beat B14 — SHOW: concept illustration card. Narration: An unannotated example teaches every feature it contains. Label which to copy, w"""
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
        if "An unannotated example teaches every feature it contains":
            line1 = Text("An unannotated example teaches every feature it contains", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Label which to copy, which to skip - and your example become":
            line2 = Text("Label which to copy, which to skip - and your example become", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "An unannotated example teaches every feature it contains":
            uline = Line(LEFT * min(4.0, len("An unannotated example teaches every feature it contains") * 0.18), RIGHT * min(4.0, len("An unannotated example teaches every feature it contains") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))
