from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


class Scene_B02_ClaudeLiamEnterprise(Scene):
    """Beat B02 — SHOW: bar/proportion chart. Narration: The trouble is the knowledge is scattered. A drive here, a wiki page there, a sh"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT I":
            # Double space "ACT  I": Pango swallows the single-space advance
            # at this boundary (rendered "ACTI") — see books-level memory note.
            act = Text("ACT  I", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.7)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        # Qualitative contrast: searching by filename misses most of what the
        # company knows; searching by content reaches it. Short category
        # labels only — the generator's narration-fragment labels collided
        # mid-frame and truncated mid-word.
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 30)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("by filename", font_size=22, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("by content", font_size=22, color="#D97757", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if True:
            note = Text("File search matches names — the knowledge lives in the content.",
                        font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 12.50))


class Scene_B04_ClaudeLiamEnterprise(Scene):
    """Beat B04 — names lie: filename search misses content. 14.5s — v2 INK text"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B04 · Names lie.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        # File box labeled Q3-notes
        file_box = Rectangle(width=2.4, height=1.2, color="#3D3929", stroke_width=2,
                             fill_color="#F2F0E9", fill_opacity=1).move_to(LEFT*3.5)
        file_label = Text("Q3-notes.txt", font_size=22, color="#3D3929", font=font).move_to(file_box.get_center())
        self.play(Create(file_box), Write(file_label), run_time=0.5)

        # Query label — INK on cream (WCAG 4.5:1); shapes keep terracotta accent
        query = Text("\"payment processor\"", font_size=28, color="#3D3929", font=font).move_to(RIGHT*2.5 + UP*0.5)
        self.play(Write(query), run_time=0.5)

        # Arrow sweeping toward file — misses (terracotta shape accent, not text)
        arrow = Arrow(start=RIGHT*2.3 + UP*0.3, end=LEFT*2.5 + UP*0.3,
                      color="#D97757", stroke_width=3, buff=0.1)
        self.play(Create(arrow), run_time=0.6)

        # X mark — no hit
        x_line1 = Line(LEFT*2.7 + UP*0.8, LEFT*1.3 + DOWN*0.2, color="#D97757", stroke_width=4)
        x_line2 = Line(LEFT*1.3 + UP*0.8, LEFT*2.7 + DOWN*0.2, color="#D97757", stroke_width=4)
        no_hit = Text("no match", font_size=24, color="#3D3929", font=font).move_to(DOWN*1.0)
        self.play(Create(x_line1), Create(x_line2), run_time=0.4)
        self.play(Write(no_hit), run_time=0.4)

        note = Text("The name and the content have nothing to do with each other.", font_size=20, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.30))


class Scene_B08_ClaudeLiamEnterprise(Scene):
    """Beat B08 — graveyard revived: dormant archive becomes living resource. 11.7s"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B08 · Graveyard, revived.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        cols, rows = 6, 3
        boxes = VGroup()
        for r in range(rows):
            for c in range(cols):
                rect = Rectangle(width=1.4, height=0.7, color="#8A8888", stroke_width=1.5,
                                 fill_color="#DDDBD3", fill_opacity=0.9)
                rect.move_to(RIGHT*(c*1.6 - 3.9) + UP*(0.9 - r*1.0))
                boxes.add(rect)
        self.play(FadeIn(boxes), run_time=0.4)

        dead_label = Text("dormant archive", font_size=22, color="#8A8888", font=font).move_to(DOWN*2.0)
        self.play(Write(dead_label), run_time=0.3)

        # Light up row by row
        for r in range(rows):
            row_boxes = VGroup(*[boxes[r*cols + c] for c in range(cols)])
            self.play(
                *[b.animate.set_fill("#D97757", opacity=0.65).set_stroke(color="#3D3929") for b in row_boxes],
                run_time=0.45
            )

        self.play(FadeOut(dead_label), run_time=0.2)
        live_label = Text("living resource", font_size=22, color="#3D3929", font=font).move_to(DOWN*2.0)
        self.play(Write(live_label), run_time=0.3)

        self.wait(max(0.01, 8.20))


class Scene_B10_ClaudeLiamEnterprise(Scene):
    """Beat B10 — divergence: generic vs grounded. 10.7s — v2 INK labels no-ligature"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B10 · Grounded, not generic.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        origin = LEFT*3.0 + DOWN*0.3

        # Generic arrow — drifts wide and up
        arrow_generic = Arrow(start=origin, end=RIGHT*1.5 + UP*1.8, color="#AAAAAA", stroke_width=3, buff=0)
        lbl_generic = Text("Generic best practice", font_size=20, color="#AAAAAA", font=font,
                           disable_ligatures=True)
        lbl_generic.next_to(arrow_generic.get_end(), RIGHT, buff=0.15)

        # Grounded arrow — lands on target; INK text for WCAG contrast
        arrow_grounded = Arrow(start=origin, end=RIGHT*1.5 + DOWN*0.3, color="#D97757", stroke_width=4, buff=0)
        lbl_grounded = Text("Grounded in your history", font_size=20, color="#3D3929", font=font,
                            disable_ligatures=True)
        lbl_grounded.next_to(arrow_grounded.get_end(), RIGHT, buff=0.15)

        target = Dot(radius=0.18, color="#3D3929").move_to(RIGHT*1.5 + DOWN*0.3)

        self.play(Create(arrow_generic), Write(lbl_generic), run_time=0.7)
        self.play(Create(arrow_grounded), Create(target), Write(lbl_grounded), run_time=0.7)

        note = Text("Your numbers. Your decisions. Your history.", font_size=22, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 7.50))


class Scene_B16_ClaudeLiamEnterprise(Scene):
    """Beat B16 — accumulate: proposals + emails + notes + past work → one briefing. 12.4s"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        # Em-dash instead of interpunct — the midpoint dot renders < 14px floor
        title = Text("B16 — Walk in prepared.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        inputs = ["Proposals", "Emails", "Notes", "Past work"]
        positions = [UL*1.8, UR*1.8, DL*1.5, DR*1.5]
        origin = ORIGIN

        src_boxes, src_labels, arrows = [], [], []
        for label, pos in zip(inputs, positions):
            box = Rectangle(width=2.0, height=0.65, color="#3D3929", stroke_width=1.5,
                            fill_color="#F2F0E9", fill_opacity=1).move_to(pos)
            lbl = Text(label, font_size=26, color="#3D3929", font=font).move_to(pos)
            arr = Arrow(start=pos, end=origin + pos*0.12, color="#8A8888", stroke_width=2, buff=0.35)
            src_boxes.append(box); src_labels.append(lbl); arrows.append(arr)

        dest = Rectangle(width=2.6, height=0.8, color="#D97757", stroke_width=2.5,
                         fill_color="#FFF8F5", fill_opacity=1).move_to(origin)
        dest_lbl = Text("One briefing", font_size=28, color="#3D3929", font=font, weight=BOLD).move_to(origin)

        for box, lbl in zip(src_boxes, src_labels):
            self.play(Create(box), Write(lbl), run_time=0.35)

        self.play(*[Create(a) for a in arrows], run_time=0.5)
        self.play(Create(dest), Write(dest_lbl), run_time=0.5)

        self.wait(max(0.01, 8.70))


class Scene_B18_ClaudeLiamEnterprise(Scene):
    """Beat B18 — boundary: search stops at your existing access. 13.4s — v2 no-ligature"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B18 — Your access only.", font_size=26, color="#3D3929", font=font,
                     disable_ligatures=True)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        # Expanding circle from center, stopped at boundary ring
        center = DOWN*0.2
        search_dot = Dot(radius=0.12, color="#D97757").move_to(center)
        self.play(FadeIn(search_dot), run_time=0.2)

        boundary_ring = Circle(radius=2.8, color="#3D3929", stroke_width=3).move_to(center)
        boundary_label = Text("Your existing access", font_size=20, color="#3D3929", font=font,
                              disable_ligatures=True)
        boundary_label.next_to(boundary_ring, UP, buff=0.15)

        # Expanding wave — stops at boundary
        wave = Circle(radius=0.12, color="#D97757", stroke_width=2.5, fill_opacity=0).move_to(center)
        self.play(wave.animate.scale(23.3), run_time=1.0)  # 0.12 * 23.3 ≈ 2.8
        self.play(FadeOut(wave), Create(boundary_ring), Write(boundary_label), run_time=0.6)

        inside_label = Text("your search", font_size=22, color="#D97757", font=font,
                            disable_ligatures=True).move_to(center + UP*0.8)
        self.play(FadeIn(inside_label), run_time=0.3)

        note = Text("It can't reach a document you couldn't open yourself.", font_size=20,
                    color="#3D3929", font=font, disable_ligatures=True)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 9.70))


class Scene_B19_ClaudeLiamEnterprise(Scene):
    """Beat B19 — flow-accumulate: sources flow into indexed store. 14.5s — v2 no-ligature INK"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B19 — Connect, then index.", font_size=26, color="#3D3929", font=font,
                     disable_ligatures=True)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        sources = ["Drive", "Wiki", "Chat", "Folders"]
        src_positions = [UL*1.6, UR*1.6, DL*1.4, DR*1.4]
        dest_pos = ORIGIN

        dest_box = Rectangle(width=2.8, height=1.0, color="#D97757", stroke_width=2.5,
                             fill_color="#FFF8F5", fill_opacity=1).move_to(dest_pos)
        dest_lbl = Text("Indexed store", font_size=24, color="#3D3929", font=font,
                        weight=BOLD, disable_ligatures=True).move_to(dest_pos)

        src_dots, arrows = [], []
        for label, pos in zip(sources, src_positions):
            dot = Dot(radius=0.15, color="#3D3929").move_to(pos)
            lbl = Text(label, font_size=20, color="#3D3929", font=font,
                       disable_ligatures=True).next_to(dot, UP*0.6, buff=0.1)
            arr = Arrow(start=pos, end=dest_pos + pos*0.18, color="#8A8888", stroke_width=2, buff=0.35)
            self.play(FadeIn(dot), Write(lbl), run_time=0.3)
            src_dots.append(dot)
            arrows.append(arr)

        self.play(*[Create(a) for a in arrows], run_time=0.5)
        self.play(Create(dest_box), Write(dest_lbl), run_time=0.5)

        # Dots streaming into dest
        for dot in src_dots:
            small = Dot(radius=0.08, color="#D97757").move_to(dot.get_center())
            self.play(small.animate.move_to(dest_pos), run_time=0.3)
            self.remove(small)

        query_lbl = Text("now searchable", font_size=20, color="#3D3929", font=font,
                         disable_ligatures=True).to_edge(DOWN, buff=0.4)
        self.play(Write(query_lbl), run_time=0.4)

        self.wait(max(0.01, 9.50))


class Scene_B22_ClaudeLiamEnterprise(Scene):
    """Beat B22 — branch-merge: 3 documents → 1 synthesized answer. 12.8s"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B22 · Combine, don't list.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        doc_positions = [LEFT*3.5 + UP*1.5, LEFT*3.5, LEFT*3.5 + DOWN*1.5]
        doc_boxes, doc_labels = [], []
        for i, pos in enumerate(doc_positions):
            box = Rectangle(width=2.0, height=0.7, color="#3D3929", stroke_width=1.5,
                            fill_color="#F2F0E9", fill_opacity=1).move_to(pos)
            lbl = Text(f"Doc {i+1}", font_size=20, color="#3D3929", font=font).move_to(pos)
            doc_boxes.append(box); doc_labels.append(lbl)
            self.play(Create(box), Write(lbl), run_time=0.3)

        dest_pos = RIGHT*2.5
        arrows = [Arrow(start=pos, end=dest_pos, color="#D97757", stroke_width=2.5, buff=0.35)
                  for pos in doc_positions]
        self.play(*[Create(a) for a in arrows], run_time=0.6)

        dest_box = Rectangle(width=2.6, height=0.9, color="#D97757", stroke_width=2.5,
                             fill_color="#FFF8F5", fill_opacity=1).move_to(dest_pos)
        dest_lbl = Text("One answer", font_size=26, color="#D97757", font=font, weight=BOLD).move_to(dest_pos)
        self.play(Create(dest_box), Write(dest_lbl), run_time=0.5)

        note = Text("File search hands you files. This combines them.", font_size=20, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.50))


class Scene_B05_ClaudeLiamEnterprise(Scene):
    """Beat B05 — content search: file opens, query lands on matching line inside. 10.7s"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        title = Text("B05 · It reads inside.", font_size=26, color="#3D3929", font=font)
        title.to_edge(UP, buff=0.7)
        self.play(FadeIn(title), run_time=0.3)

        file_border = Rectangle(width=5.0, height=3.0, color="#3D3929", stroke_width=2,
                                fill_color="#F2F0E9", fill_opacity=1).move_to(LEFT*0.5)
        file_header = Text("Q3-notes.txt", font_size=20, color="#3D3929", font=font)
        file_header.move_to(LEFT*0.5 + UP*1.85)

        lines_text = [
            "Revenue forecast for Q3...",
            "Vendor: payment processor review",
            "Action items from last week",
        ]
        line_mobs = []
        for i, lt in enumerate(lines_text):
            lm = Text(lt, font_size=17, color="#3D3929", font=font)
            lm.move_to(LEFT*0.5 + UP*(0.7 - i*0.65))
            line_mobs.append(lm)

        self.play(Create(file_border), Write(file_header), run_time=0.5)
        for lm in line_mobs:
            self.play(FadeIn(lm), run_time=0.22)

        query = Text('"payment processor"', font_size=22, color="#D97757", font=font)
        query.move_to(RIGHT*3.5 + UP*0.5)
        self.play(Write(query), run_time=0.4)

        highlight = Rectangle(width=4.5, height=0.44, color="#D97757", stroke_width=0,
                              fill_color="#D97757", fill_opacity=0.25)
        highlight.move_to(line_mobs[1].get_center())
        self.play(Create(highlight), run_time=0.4)

        note = Text("Matches content, not filename.", font_size=20, color="#3D3929", font=font)
        note.to_edge(DOWN, buff=0.4)
        self.play(Write(note), run_time=0.4)

        self.wait(max(0.01, 5.60))


class Scene_B09_ClaudeLiamEnterprise(Scene):
    """Beat B09 — SHOW: bar/proportion chart. Narration: It goes one step further. When the plugin finds the relevant document, it can pu"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT III":
            act = Text("ACT  III", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.7)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        # Contrast the answer WITHOUT the document in context vs WITH it.
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 30)
        pt2 = ax.c2p(2, 75)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("generic answer", font_size=22, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.25)
        lbl2 = Text("grounded answer", font_size=22, color="#D97757", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.25)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if True:
            note = Text("Pull the document into context — the answer cites your own work.",
                        font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 11.10))
