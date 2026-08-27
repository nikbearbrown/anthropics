from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_ClaudeLiamInstalling(Scene):
    """Beat B02 — SHOW: bar/proportion chart. Narration: Click install. It downloads, activates, and it\'s ready — no setup wizard, no con"""
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

        lbl1 = Text("Click install"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("It downloads, activates, and it\'s ready - no setup wizard, n"[:30] if "It downloads, activates, and it\'s ready - no setup wizard, n" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "If you\'ve ever added an app from a store, you already have t":
            note = Text("If you\'ve ever added an app from a store, you already have t"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.40))


class Scene_B07_ClaudeLiamInstalling(Scene):
    """Beat B07 — SHOW: bar/proportion chart. Narration: The pattern never changes: Claude asks, you answer, the plugin calibrates. Ask a"""
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

        lbl1 = Text("The pattern never changes: Claude asks, you answer, the plug"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Ask again, answer again, it tightens"[:30] if "Ask again, answer again, it tightens" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "It\'s the same loop whether you spend two questions or twenty":
            note = Text("It\'s the same loop whether you spend two questions or twenty"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.70))


class Scene_B18_ClaudeLiamInstalling(Scene):
    """Beat B18 — SHOW: bar/proportion chart. Narration: Want Claude to focus? Disable a plugin without removing it — your customization """
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT V":
            act = Text("ACT V", font_size=24, color="#3D3929", font=font)
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

        lbl1 = Text("Want Claude to focus? Disable a plugin without removing it -"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Flip it back on when you need it"[:30] if "Flip it back on when you need it" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "Nothing you taught it is lost":
            note = Text("Nothing you taught it is lost"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.00))


class Scene_B14_ClaudeLiamInstalling(Scene):
    """Beat B14 — SHOW: two-up comparison (self-contained vs connected plugin).
    Narration: Some plugins are self-contained — the productivity plugin works out of
    the box, connected to nothing. Others get dramatically more useful the moment you
    plug them into the tools you already run."""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
        act.to_edge(UP, buff=0.3)
        self.play(FadeIn(act), run_time=0.3)

        # Left box — self-contained plugin
        lbox = Rectangle(width=3.0, height=1.8, color="#3D3929", stroke_width=3)
        lbox.move_to([-2.8, 0.2, 0])
        ltitle = Text("Productivity Plugin", font_size=20, color="#3D3929", font=font)
        ltitle.move_to(lbox.get_center() + UP * 0.3)
        ltag = Text("Self-Contained", font_size=17, color="#3D3929", font=font)
        ltag.move_to(lbox.get_center() + DOWN * 0.3)
        lcap = Text("works out of the box", font_size=16, color="#3D3929", font=font)
        lcap.next_to(lbox, DOWN, buff=0.25)

        # Right box — connected plugin (starts same style)
        rbox = Rectangle(width=3.0, height=1.8, color="#3D3929", stroke_width=3)
        rbox.move_to([0.8, 0.2, 0])
        rtitle = Text("Sales Plugin", font_size=20, color="#3D3929", font=font)
        rtitle.move_to(rbox.get_center() + UP * 0.3)
        rtag = Text("+ Your Tools", font_size=17, color="#3D3929", font=font)
        rtag.move_to(rbox.get_center() + DOWN * 0.3)

        self.play(Create(lbox), Create(rbox), run_time=0.5)
        self.play(FadeIn(ltitle), FadeIn(rtitle), run_time=0.4)
        self.play(FadeIn(ltag), FadeIn(rtag), FadeIn(lcap), run_time=0.4)

        self.wait(0.8)

        # Draw connection lines from right box to external tools
        rright = rbox.get_right()

        crm = Rectangle(width=1.3, height=0.55, color="#D97757", stroke_width=2)
        crm.move_to([3.8, 1.0, 0])
        crm_lbl = Text("CRM", font_size=18, color="#D97757", font=font)
        crm_lbl.move_to(crm.get_center())
        crm_line = Line(rright + UP * 0.35, crm.get_left(), color="#D97757", stroke_width=2)

        db = Rectangle(width=1.3, height=0.55, color="#D97757", stroke_width=2)
        db.move_to([3.8, 0.1, 0])
        db_lbl = Text("Database", font_size=18, color="#D97757", font=font)
        db_lbl.move_to(db.get_center())
        db_line = Line(rright, db.get_left(), color="#D97757", stroke_width=2)

        chat = Rectangle(width=1.3, height=0.55, color="#D97757", stroke_width=2)
        chat.move_to([3.8, -0.8, 0])
        chat_lbl = Text("History", font_size=18, color="#D97757", font=font)
        chat_lbl.move_to(chat.get_center())
        chat_line = Line(rright + DOWN * 0.35, chat.get_left(), color="#D97757", stroke_width=2)

        self.play(Create(crm_line), Create(crm), FadeIn(crm_lbl), run_time=0.5)
        self.play(Create(db_line), Create(db), FadeIn(db_lbl), run_time=0.5)
        self.play(Create(chat_line), Create(chat), FadeIn(chat_lbl), run_time=0.5)

        # Brighten right box to terracotta
        rbox_hl = Rectangle(width=3.0, height=1.8, color="#D97757", stroke_width=3)
        rbox_hl.move_to([0.8, 0.2, 0])
        rcap = Text("dramatically more useful", font_size=16, color="#D97757", font=font)
        rcap.next_to(rbox, DOWN, buff=0.25)

        self.play(Transform(rbox, rbox_hl), FadeIn(rcap), run_time=0.5)

        self.wait(max(0.01, 5.86))
