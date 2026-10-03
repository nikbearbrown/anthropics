from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B01_ClaudeLiamTroubleshooting(Scene):
    """Beat B01 — frustration → abandonment. Diagnose stays in the game."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 75)
        pt2 = ax.c2p(2, 25)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Diagnose", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Abandon", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Diagnosing is how you stay in the game.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 10.10))


class Scene_B06_ClaudeLiamTroubleshooting(Scene):
    """Beat B06 — broad default vs your context. Context sharpens output."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 35)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Broad default", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Your context", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Feed the plugin your context and the output sharpens past generic.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.80))


class Scene_B07_ClaudeLiamTroubleshooting(Scene):
    """Beat B07 — big scope vs narrow scope. Narrow scope cuts latency."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  II", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 35)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Everything", font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("One slice", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        note = Text("Scope to one date range or folder and latency drops with it.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.40))


class Scene_B02_ClaudeLiamTroubleshooting(Scene):
    """Beat B02 — the interface shifts; the concept underneath holds."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        surface_bg = Rectangle(width=9.0, height=1.3, color="#3D3929",
                               stroke_width=2, fill_opacity=0.0).shift(UP*1.2)
        surface_label_a = Text("interface — buttons — menus", font_size=30,
                               color="#3D3929", font=font).move_to(surface_bg.get_center())
        surface_label_b = Text("interface — new labels — new panels", font_size=30,
                               color="#3D3929", font=font).move_to(surface_bg.get_center())
        surface_label_c = Text("interface — redesigned — again", font_size=30,
                               color="#3D3929", font=font).move_to(surface_bg.get_center())
        surface_tag = Text("SURFACE (changes)", font_size=26,
                           color="#D97757", font=font)
        surface_tag.next_to(surface_bg, UP, buff=0.15).align_to(surface_bg, LEFT)

        base_bg = Rectangle(width=9.0, height=1.3, color="#D97757",
                            stroke_width=3, fill_color="#D97757",
                            fill_opacity=0.12).shift(DOWN*1.2)
        base_label = Text("concept — what the plugin is for", font_size=32,
                          color="#3D3929", font=font).move_to(base_bg.get_center())
        base_tag = Text("BEDROCK (persists)", font_size=26,
                        color="#3D3929", font=font)
        base_tag.next_to(base_bg, DOWN, buff=0.15).align_to(base_bg, LEFT)

        self.play(Create(surface_bg), FadeIn(surface_tag), FadeIn(surface_label_a), run_time=0.6)
        self.play(Create(base_bg), FadeIn(base_tag), FadeIn(base_label), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(surface_label_a), FadeIn(surface_label_b), run_time=0.6)
        self.wait(1.4)
        self.play(FadeOut(surface_label_b), FadeIn(surface_label_c), run_time=0.6)

        note = Text("Troubleshoot from the bedrock", font_size=28,
                    color="#3D3929", font=font).to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.6)

        self.wait(max(0.01, 6.4))


class Scene_B10_ClaudeLiamTroubleshooting(Scene):
    """Beat B10 — four steps light in sequence."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  III", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        steps = [
            ("1", "Active?"),
            ("2", "Authorized?"),
            ("3", "Simpler?"),
            ("4", "Restart?"),
        ]
        cards = []
        checks = []
        row_y = 0.2
        x_positions = [-4.8, -1.6, 1.6, 4.8]
        for (num, label), x in zip(steps, x_positions):
            box = Rectangle(width=2.8, height=1.8, color="#3D3929",
                            stroke_width=2, fill_color="#F2F0E9", fill_opacity=1.0)
            box.move_to([x, row_y, 0])
            n = Text(num, font_size=44, color="#D97757", font=font).move_to(box.get_center()+UP*0.40)
            lbl = Text(label, font_size=32, color="#3D3929", font=font).move_to(box.get_center()+DOWN*0.40)
            grp = VGroup(box, n, lbl)
            cards.append(grp)
            check = Text("✓", font_size=32, color="#D97757", font=font)
            check.next_to(box, DOWN, buff=0.25)
            checks.append(check)

        self.play(*[FadeIn(c) for c in cards], run_time=0.6)
        for i, check in enumerate(checks):
            self.play(FadeIn(check), run_time=0.4)
            self.wait(1.2)

        note = Text("Most trouble dies in these four", font_size=28,
                    color="#3D3929", font=font).to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.6)

        self.wait(max(0.01, 3.2))


class Scene_B13_ClaudeLiamTroubleshooting(Scene):
    """Beat B13 — interface labels churn; the concept line runs flat."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT  IV", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        axis = Line([-6, 0, 0], [6, 0, 0], color="#3D3929", stroke_width=2)
        self.play(Create(axis), run_time=0.4)

        tick_positions = [-4.5, -1.5, 1.5, 4.5]
        tick_labels = ["v1.2", "v1.4", "v1.7", "v2.0"]
        interface_labels = ["Plugins", "Extensions", "Add-ons", "Integrations"]

        tick_group = VGroup()
        label_group = VGroup()
        for x, tk, il in zip(tick_positions, tick_labels, interface_labels):
            tick = Line([x, -0.15, 0], [x, 0.15, 0], color="#3D3929", stroke_width=2)
            date = Text(tk, font_size=16, color="#3D3929", font=font)
            date.next_to(tick, DOWN, buff=0.2)
            lbl = Text(il, font_size=22, color="#D97757", font=font)
            lbl.next_to(tick, UP, buff=0.4)
            tick_group.add(tick, date)
            label_group.add(lbl)

        self.play(Create(tick_group), run_time=0.6)
        for lbl in label_group:
            self.play(FadeIn(lbl, shift=UP*0.2), run_time=0.5)
            self.wait(0.6)

        concept = Line([-5.5, -1.6, 0], [5.5, -1.6, 0], color="#3D3929", stroke_width=4)
        concept_lbl = Text("the concept — troubleshoot from here", font_size=22,
                           color="#3D3929", font=font)
        concept_lbl.next_to(concept, DOWN, buff=0.25)
        self.play(Create(concept), FadeIn(concept_lbl), run_time=0.7)

        self.wait(max(0.01, 3.6))
