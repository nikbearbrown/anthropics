from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_PasteLoop(Scene):
    """B01 — wrong model: same instruction block pasted again and again."""
    def construct(self):
        # Reduced height (1.4) so 3 blocks fit within ±3.4 safe area
        block_template = RoundedRectangle(width=6, height=1.4, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1)
        clock = Text("Week 1", font_size=26, color=INK, font=FONT).to_corner(UR, buff=1.2)
        self.play(FadeIn(clock), run_time=0.3)

        # Centers: 2.1, 0.5, -1.1 → tops: 3.1, 1.2, -0.4 → bottoms: 1.1, -0.2, -1.8; all within ±3.4
        positions = [UP*2.1, UP*0.5, DOWN*1.1]
        week_labels = ["Week 1", "Week 2", "Week 3"]
        for i, (pos, week) in enumerate(zip(positions, week_labels)):
            b = block_template.copy().move_to(pos)
            t = Text("Instructions...\n(400 words)", font_size=26, color=INK, font=FONT).move_to(b)
            copy_label = Text("copy-paste", font_size=24, color=INK, font=FONT).next_to(b, RIGHT, buff=0.25)
            new_clock = Text(week, font_size=26, color=INK, font=FONT).to_corner(UR, buff=1.2)
            self.play(FadeIn(b), Write(t), FadeIn(copy_label),
                      Transform(clock, new_clock), run_time=0.55)
            self.wait(0.15)

        waste = Text("Same instructions. Every time.", font_size=34, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.4)
        self.play(Write(waste), run_time=0.6)
        self.wait(0.8)


class B02_SkillLoad(Scene):
    """B02 — right model: SKILL.md opens and only the relevant parts flow to work surface."""
    def construct(self):
        skill_file = RoundedRectangle(width=3.2, height=4.2, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1).shift(LEFT*4)
        skill_label = Text("SKILL.md", font_size=28, color=INK, weight=BOLD, font=FONT).next_to(skill_file, UP, buff=0.25)
        task_box = RoundedRectangle(width=3, height=1, color=INK, stroke_width=2).set_fill(CREAM, opacity=0).shift(UP*2.5)
        task_label = Text("Task arrives", font_size=24, color=INK, font=FONT).move_to(task_box)
        work_surface = RoundedRectangle(width=5, height=3, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(RIGHT*3)
        ws_label = Text("Work surface", font_size=24, color=INK, font=FONT).next_to(work_surface, UP, buff=0.2)

        self.play(FadeIn(skill_file), Write(skill_label), run_time=0.4)
        self.play(FadeIn(task_box), Write(task_label), run_time=0.4)
        self.play(FadeIn(work_surface), Write(ws_label), run_time=0.4)

        asset_lines = [
            Text("Instructions", font_size=22, color=INK, font=FONT).move_to(skill_file.get_center() + UP*0.9),
            Text("Assets", font_size=22, color=INK, font=FONT).move_to(skill_file.get_center()),
            Text("Scripts", font_size=22, color=INK, font=FONT).move_to(skill_file.get_center() + DOWN*0.9),
        ]
        for a in asset_lines:
            self.play(FadeIn(a), run_time=0.25)

        relevant = asset_lines[0].copy()
        arrow = Arrow(skill_file.get_right(), work_surface.get_left(), color=TERRA, stroke_width=2)
        self.play(Create(arrow), relevant.animate.move_to(work_surface.get_center()), run_time=0.7)
        self.play(FadeOut(asset_lines[1]), FadeOut(asset_lines[2]), run_time=0.3)

        loaded = Text("Loaded when relevant.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.5)
        self.play(Write(loaded), run_time=0.6)
        self.wait(0.8)


class B04_DescartesChecklist(Scene):
    """B04 — do this now: Descartes move produces a checklist, not a feeling."""
    def construct(self):
        claim = RoundedRectangle(width=5, height=0.9, color=INK, stroke_width=2.5).set_fill(CREAM, opacity=0).shift(UP*3.0)
        claim_text = Text("My skill works.", font_size=26, color=INK, weight=BOLD, font=FONT).move_to(claim)
        self.play(FadeIn(claim), Write(claim_text), run_time=0.5)

        descartes = Text("What must be true for this to fail?", font_size=22, color=INK, font=FONT).shift(UP*1.9)
        self.play(Write(descartes), run_time=0.4)

        branches = [
            "Instructions unambiguous?",
            "Assets present?",
            "Description triggers correctly?",
            "Edge cases handled?",
        ]
        # Nodes: centers at 0.35, -0.55, -1.45, -2.35 — all within safe area
        for i, branch in enumerate(branches):
            node = RoundedRectangle(width=5.5, height=0.7, color=INK, stroke_width=1.5).set_fill("#EAE7DC", opacity=1)
            node.shift(UP*0.35 + DOWN*(i * 0.9))
            node_text = Text(branch, font_size=22, color=INK, font=FONT).move_to(node)
            tick = Dot(color=INK, radius=0.12).next_to(node, LEFT, buff=0.2)
            self.play(FadeIn(node), Write(node_text), FadeIn(tick), run_time=0.35)

        # Verdict well below last node (node 3 bottom ≈ -2.7), safely above ±3.4 floor
        result = Text("Checklist, not a feeling.", font_size=32, color=INK, weight=BOLD, font=FONT).shift(DOWN*3.2)
        self.play(Write(result), run_time=0.6)
        self.wait(0.6)
