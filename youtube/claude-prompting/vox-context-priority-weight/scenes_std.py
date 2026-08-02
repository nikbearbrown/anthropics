from manim import *
import numpy as np
import math

BG    = "#FFFFFF"
INK   = "#2A1A0E"
TERRA = "#C8102E"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B03_VoxContextPriority(Scene):
    """Beat B03 — SHOW: concept illustration card. Narration: The output follows the brand guide. It is predominantly blue. The hard constrain"""
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
        if "The output follows the brand guide":
            line1 = Text("The output follows the brand guide", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It is predominantly blue":
            line2 = Text("It is predominantly blue", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The hard constraint - nothing blue - was in the unlabeled br":
            line3 = Text("The hard constraint - nothing blue - was in the unlabeled br", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The output follows the brand guide":
            uline = Line(LEFT * min(4.0, len("The output follows the brand guide") * 0.18), RIGHT * min(4.0, len("The output follows the brand guide") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 7.00))


class Scene_B04_VoxContextPriority(Scene):
    """Beat B04 — SHOW: concept illustration card. Narration: Without source labels, Claude treats all pasted documents as a single undifferen"""
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
        if "Without source labels, Claude treats all pasted documents as":
            line1 = Text("Without source labels, Claude treats all pasted documents as", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "It cannot determine which source is authoritative or current":
            line2 = Text("It cannot determine which source is authoritative or current", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "So it weights them by what it can see: length, formality, st":
            line3 = Text("So it weights them by what it can see: length, formality, st", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Without source labels, Claude treats all pasted documents as":
            uline = Line(LEFT * min(4.0, len("Without source labels, Claude treats all pasted documents as") * 0.18), RIGHT * min(4.0, len("Without source labels, Claude treats all pasted documents as") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B05_VoxContextPriority(Scene):
    """Beat B05 — SHOW: concept illustration card. Narration: The brand guide is 15 pages — long and formally structured. The competitor analy"""
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
        if "The brand guide is 15 pages - long and formally structured":
            line1 = Text("The brand guide is 15 pages - long and formally structured", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "The competitor analysis is 6 pages":
            line2 = Text("The competitor analysis is 6 pages", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "The brief is 1 page, labeled FYI, informal":
            line3 = Text("The brief is 1 page, labeled FYI, informal", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The brand guide is 15 pages - long and formally structured":
            uline = Line(LEFT * min(4.0, len("The brand guide is 15 pages - long and formally structured") * 0.18), RIGHT * min(4.0, len("The brand guide is 15 pages - long and formally structured") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B06_VoxContextPriority(Scene):
    """Beat B06 — SHOW: concept illustration card. Narration: The brief\'s constraint — nothing blue — gets proportional weight: roughly one fi"""
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
        if "The brief\'s constraint - nothing blue - gets proportional we":
            line1 = Text("The brief\'s constraint - nothing blue - gets proportional we", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Not because it is less important":
            line2 = Text("Not because it is less important", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Because it is shorter and less formal":
            line3 = Text("Because it is shorter and less formal", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The brief\'s constraint - nothing blue - gets proportional we":
            uline = Line(LEFT * min(4.0, len("The brief\'s constraint - nothing blue - gets proportional we") * 0.18), RIGHT * min(4.0, len("The brief\'s constraint - nothing blue - gets proportional we") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B07_VoxContextPriority(Scene):
    """Beat B07 — SHOW: concept illustration card. Narration: Adding more unlabeled documents makes this worse, not better. Each new document """
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
        if "Adding more unlabeled documents makes this worse, not better":
            line1 = Text("Adding more unlabeled documents makes this worse, not better", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Each new document adds noise and potentially buries the info":
            line2 = Text("Each new document adds noise and potentially buries the info", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "More is not more here - it is dilution":
            line3 = Text("More is not more here - it is dilution", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "Adding more unlabeled documents makes this worse, not better":
            uline = Line(LEFT * min(4.0, len("Adding more unlabeled documents makes this worse, not better") * 0.18), RIGHT * min(4.0, len("Adding more unlabeled documents makes this worse, not better") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B08_VoxContextPriority(Scene):
    """Beat B08 — SHOW: concept illustration card. Narration: The fix is label and prune. Label each source before it appears — tell Claude wh"""
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
        if "The fix is label and prune":
            line1 = Text("The fix is label and prune", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Label each source before it appears - tell Claude what it is":
            line2 = Text("Label each source before it appears - tell Claude what it is", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Then prune to what the task actually draws on":
            line3 = Text("Then prune to what the task actually draws on", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "The fix is label and prune":
            uline = Line(LEFT * min(4.0, len("The fix is label and prune") * 0.18), RIGHT * min(4.0, len("The fix is label and prune") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B09_VoxContextPriority(Scene):
    """Beat B09 — SHOW: concept illustration card. Narration: With labels, Keiko assigns the priority order she actually intends. Claude treat"""
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
        if "With labels, Keiko assigns the priority order she actually i":
            line1 = Text("With labels, Keiko assigns the priority order she actually i", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Claude treats the brief as binding - nothing blue is now a h":
            line2 = Text("Claude treats the brief as binding - nothing blue is now a h", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "With labels, Keiko assigns the priority order she actually i":
            uline = Line(LEFT * min(4.0, len("With labels, Keiko assigns the priority order she actually i") * 0.18), RIGHT * min(4.0, len("With labels, Keiko assigns the priority order she actually i") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 9.00))


class Scene_B10_VoxContextPriority(Scene):
    """Beat B10 — SHOW: concept illustration card. Narration: This applies to any multi-document paste. Meeting notes plus a policy document p"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE IMPLICATION":
            act = Text("THE IMPLICATION", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "This applies to any multi-document paste":
            line1 = Text("This applies to any multi-document paste", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Meeting notes plus a policy document plus an email thread: w":
            line2 = Text("Meeting notes plus a policy document plus an email thread: w", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "With labels that say \'the email overrides the policy on the ":
            line3 = Text("With labels that say \'the email overrides the policy on the ", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "This applies to any multi-document paste":
            uline = Line(LEFT * min(4.0, len("This applies to any multi-document paste") * 0.18), RIGHT * min(4.0, len("This applies to any multi-document paste") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))


class Scene_B11_VoxContextPriority(Scene):
    """Beat B11 — SHOW: concept illustration card. Narration: A school administrator pastes a 20-page district handbook, a 3-page teacher memo"""
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
        if "A school administrator pastes a 20-page district handbook, a":
            line1 = Text("A school administrator pastes a 20-page district handbook, a", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "She asks Claude to summarize the current policy":
            line2 = Text("She asks Claude to summarize the current policy", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Claude summarizes the handbook":
            line3 = Text("Claude summarizes the handbook", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "A school administrator pastes a 20-page district handbook, a":
            uline = Line(LEFT * min(4.0, len("A school administrator pastes a 20-page district handbook, a") * 0.18), RIGHT * min(4.0, len("A school administrator pastes a 20-page district handbook, a") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 11.00))


class Scene_B12_VoxContextPriority(Scene):
    """Beat B12 — SHOW: concept illustration card. Narration: She adds two labels: handbook — background. Principal email — binding override o"""
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
        if "She adds two labels: handbook - background":
            line1 = Text("She adds two labels: handbook - background", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Principal email - binding override on section 4":
            line2 = Text("Principal email - binding override on section 4", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "Now Claude weights the email appropriately":
            line3 = Text("Now Claude weights the email appropriately", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "She adds two labels: handbook - background":
            uline = Line(LEFT * min(4.0, len("She adds two labels: handbook - background") * 0.18), RIGHT * min(4.0, len("She adds two labels: handbook - background") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 10.00))


class Scene_B13_VoxContextPriority(Scene):
    """Beat B13 — SHOW: layer stack diagram. Narration: Before pasting multiple documents: label each one. Use three categories: primary"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "THE PRACTICE":
            act = Text("THE PRACTICE", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        layers_text = [t for t in ["Before pasting multiple documents: label each one", "Use three categories: primary - use this as the binding sour", "Then prune each to what the task actually needs"] if t]
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


class Scene_B14_VoxContextPriority(Scene):
    """Beat B14 — SHOW: concept illustration card. Narration: More unlabeled context gives Claude more to weight incorrectly. Label your sourc"""
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        font = "EB Garamond"

        if "RECAP":
            act = Text("RECAP", font_size=24, color="#2A1A0E", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Spark line — terracotta accent
        spark = Line(LEFT * 0.6, RIGHT * 0.6, color="#C8102E", stroke_width=3)
        spark.shift(UP * 1.2)
        self.play(Create(spark), run_time=0.2)

        # Primary concept text
        if "More unlabeled context gives Claude more to weight incorrect":
            line1 = Text("More unlabeled context gives Claude more to weight incorrect", font_size=36, color="#2A1A0E", font=font)
            line1.scale(min(1.0, 13.0 / max(0.1, line1.width)))
            line1.shift(UP * 0.3)
            self.play(Write(line1), run_time=0.5)

        if "Label your sources - and the priority order you assign is th":
            line2 = Text("Label your sources - and the priority order you assign is th", font_size=28, color="#2A1A0E", font=font)
            line2.scale(min(1.0, 13.0 / max(0.1, line2.width)))
            line2.shift(DOWN * 0.6)
            self.play(Write(line2), run_time=0.4)

        if "":
            line3 = Text("", font_size=22, color="#2A1A0E", font=font)
            line3.scale(min(1.0, 13.0 / max(0.1, line3.width)))
            line3.shift(DOWN * 1.4)
            self.play(FadeIn(line3), run_time=0.3)

        # Terracotta underline on key term
        if "More unlabeled context gives Claude more to weight incorrect":
            uline = Line(LEFT * min(4.0, len("More unlabeled context gives Claude more to weight incorrect") * 0.18), RIGHT * min(4.0, len("More unlabeled context gives Claude more to weight incorrect") * 0.18),
                         color="#C8102E", stroke_width=2)
            uline.shift(UP * 0.1)
            self.play(Create(uline), run_time=0.3)

        self.wait(max(0.01, 8.00))
