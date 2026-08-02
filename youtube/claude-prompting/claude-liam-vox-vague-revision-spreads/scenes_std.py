from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_ClaudeLiamVox(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: Maya asked Claude to make the press release more concise. Nothing else. Claude c"""
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
        if "Maya asked Claude to make the press release more concise":
            line1 = Text("Maya asked Claude to make the press release more concise", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Nothing else":
            line2 = Text("Nothing else", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude changed four elements she never touched":
            line3 = Text("Claude changed four elements she never touched", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Maya asked Claude to make the press release more concise":
            uline = Line(LEFT * min(4.0, len("Maya asked Claude to make the press release more concise") * 0.18), RIGHT * min(4.0, len("Maya asked Claude to make the press release more concise") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_ClaudeLiamVox(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: A revision request without named targets treats the entire output as revision-el"""
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
        if "A revision request without named targets treats the entire o":
            line1 = Text("A revision request without named targets treats the entire o", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\'More concise\' is a goal, not a target":
            line2 = Text("\'More concise\' is a goal, not a target", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude identifies every element that could plausibly serve t":
            line3 = Text("Claude identifies every element that could plausibly serve t", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A revision request without named targets treats the entire o":
            uline = Line(LEFT * min(4.0, len("A revision request without named targets treats the entire o") * 0.18), RIGHT * min(4.0, len("A revision request without named targets treats the entire o") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B05_ClaudeLiamVox(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: The output is not a set of independent elements. Changing one affects the others"""
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
        if "The output is not a set of independent elements":
            line1 = Text("The output is not a set of independent elements", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Changing one affects the others":
            line2 = Text("Changing one affects the others", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Remove a paragraph for conciseness - the CEO quote no longer":
            line3 = Text("Remove a paragraph for conciseness - the CEO quote no longer", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The output is not a set of independent elements":
            uline = Line(LEFT * min(4.0, len("The output is not a set of independent elements") * 0.18), RIGHT * min(4.0, len("The output is not a set of independent elements") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B06_ClaudeLiamVox(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: What Claude needs is not just the change. It needs the wall around what must not"""
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
        if "What Claude needs is not just the change":
            line1 = Text("What Claude needs is not just the change", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It needs the wall around what must not be touched":
            line2 = Text("It needs the wall around what must not be touched", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "A revision prompt has two parts: the target and the freeze l":
            line3 = Text("A revision prompt has two parts: the target and the freeze l", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "What Claude needs is not just the change":
            uline = Line(LEFT * min(4.0, len("What Claude needs is not just the change") * 0.18), RIGHT * min(4.0, len("What Claude needs is not just the change") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_ClaudeLiamVox(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Revision drift is not a model failure. It is a specification failure. The work o"""
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
        if "Revision drift is not a model failure":
            line1 = Text("Revision drift is not a model failure", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It is a specification failure":
            line2 = Text("It is a specification failure", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The work order was incomplete":
            line3 = Text("The work order was incomplete", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Revision drift is not a model failure":
            uline = Line(LEFT * min(4.0, len("Revision drift is not a model failure") * 0.18), RIGHT * min(4.0, len("Revision drift is not a model failure") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B08_ClaudeLiamVox(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: The fix: name the target and name the freeze. \'Shorten the methodology section o"""
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
        if "The fix: name the target and name the freeze":
            line1 = Text("The fix: name the target and name the freeze", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\'Shorten the methodology section only":
            line2 = Text("\'Shorten the methodology section only", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Do not touch the CEO quote, the impact paragraph, or the ope":
            line3 = Text("Do not touch the CEO quote, the impact paragraph, or the ope", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The fix: name the target and name the freeze":
            uline = Line(LEFT * min(4.0, len("The fix: name the target and name the freeze") * 0.18), RIGHT * min(4.0, len("The fix: name the target and name the freeze") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B09_ClaudeLiamVox(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: This applies to any revision. \'Make it clearer\' gives Claude the whole document."""
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
        if "This applies to any revision":
            line1 = Text("This applies to any revision", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "\'Make it clearer\' gives Claude the whole document":
            line2 = Text("\'Make it clearer\' gives Claude the whole document", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "\'Make it warmer\' gives Claude the whole document":
            line3 = Text("\'Make it warmer\' gives Claude the whole document", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "This applies to any revision":
            uline = Line(LEFT * min(4.0, len("This applies to any revision") * 0.18), RIGHT * min(4.0, len("This applies to any revision") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B10_ClaudeLiamVox(Scene):
    """Beat B10 — SHOW: layer stack diagram. Narration: A nonprofit director asks Claude to make a grant proposal \'more engaging.\' Claud"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["A nonprofit director asks Claude to make a grant proposal \'m", "\' Claude rewrites three paragraphs, adds a narrative hook, s", "The funder required measurable outcomes"] if t]
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

        self.wait(max(0.01, 11.00))


class Scene_B11_ClaudeLiamVox(Scene):
    """Beat B11 — SHOW: layer stack diagram. Narration: Targeted revision: \'Make the opening paragraph more engaging. Do not change the """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "THE EXAMPLE":
            act = Text("THE EXAMPLE", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["Targeted revision: \'Make the opening paragraph more engaging", "Do not change the measurable outcomes section, the data in s", "\' Claude rewrites the opening"] if t]
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


class Scene_B12_ClaudeLiamVox(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: The practice: before every revision request, name three things. The specific cha"""
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
        if "The practice: before every revision request, name three thin":
            line1 = Text("The practice: before every revision request, name three thin", font_size=36, color="#3D3929", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The specific change target":
            line2 = Text("The specific change target", font_size=28, color="#3D3929", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The elements frozen - must not change":
            line3 = Text("The elements frozen - must not change", font_size=22, color="#3D3929", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The practice: before every revision request, name three thin":
            uline = Line(LEFT * min(4.0, len("The practice: before every revision request, name three thin") * 0.18), RIGHT * min(4.0, len("The practice: before every revision request, name three thin") * 0.18),
                         color="#D97757", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B13_ClaudeLiamVox(Scene):
    """Beat B13 — SHOW: cycle / feedback loop. Narration: A vague revision gives Claude the whole document. Name the target. Freeze what m"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "RECAP":
            act = Text("RECAP", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        import numpy as np
        stages = [t for t in ["A vague revision gives Claude the whole document", "Name the target", "Freeze what must survive"] if t]
        if not stages:
            stages = ["Input", "Process", "Output"]
        n = len(stages)
        radius = 2.5
        colors = ["#3D3929", "#D97757"] + ["#3D3929"] * 10

        nodes = []
        for i, lbl in enumerate(stages):
            angle = np.pi / 2 - 2 * np.pi * i / n
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            circle = Circle(radius=0.55, color=colors[i % 2], stroke_width=2.5,
                            fill_color="#F2F0E9", fill_opacity=1)
            circle.move_to(pos)
            txt = Text(lbl[:20], font_size=18, color="#3D3929", font=font)
            txt.scale(min(1.0, 0.9 / max(0.1, txt.width)))
            txt.move_to(circle)
            grp = VGroup(circle, txt)
            nodes.append((grp, pos))
            self.play(FadeIn(grp), run_time=0.4)

        # Draw curved arrows between nodes
        for i in range(n):
            start_pos = nodes[i][1]
            end_pos = nodes[(i + 1) % n][1]
            arr = CurvedArrow(start_pos, end_pos, color="#D97757", stroke_width=2.5,
                              angle=-np.pi / 6)
            self.play(Create(arr), run_time=0.4)

        self.wait(max(0.01, 8.00))
