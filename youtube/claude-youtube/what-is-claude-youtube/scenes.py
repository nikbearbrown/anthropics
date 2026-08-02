from manim import *

CREAM = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"

config.background_color = CREAM

class B01_AIMakesVideos(Scene):
    """B01 — wrong model: prompt in, finished film out, one arrow. Crossed out."""
    def construct(self):
        prompt_box = RoundedRectangle(width=3, height=1.5, color=INK, stroke_width=2).set_fill("#EAE7DC", opacity=1).shift(LEFT*4)
        prompt_label = Text("Prompt", font_size=26, color=INK, weight=BOLD, font=FONT).next_to(prompt_box, UP, buff=0.2)
        prompt_text = Text('"Make a video."', font_size=24, color=INK, font=FONT).move_to(prompt_box)
        self.play(FadeIn(prompt_box), Write(prompt_label), Write(prompt_text), run_time=0.4)

        film_box = RoundedRectangle(width=3, height=1.5, color=INK, stroke_width=2).set_fill(CREAM, opacity=1).shift(RIGHT*4)
        film_label = Text("Finished film", font_size=26, color=INK, weight=BOLD, font=FONT).next_to(film_box, UP, buff=0.2)
        self.play(FadeIn(film_box), Write(film_label), run_time=0.3)

        arrow = Arrow(prompt_box.get_right(), film_box.get_left(), color=INK, stroke_width=2.5)
        self.play(Create(arrow), run_time=0.4)

        # FadeOut text labels before Cross to avoid label-on-line audit error
        self.play(FadeOut(prompt_text), FadeOut(prompt_label), FadeOut(film_label), run_time=0.2)
        cross = Cross(VGroup(prompt_box, arrow, film_box), color=TERRA, stroke_width=4)
        self.play(Create(cross), run_time=0.4)
        nope = Text("That is not the pipeline.", font_size=30, color=INK, weight=BOLD, font=FONT).shift(DOWN*2.5)
        self.play(Write(nope), run_time=0.5)
        self.wait(0.9)


class B02_PipelineWithGates(Scene):
    """B02 — right model: full pipeline with audio-master clock and two human gates."""
    def construct(self):
        stages = ["Script", "Beats", "Audio", "Visuals", "QC"]
        stage_mobs = []
        for i, stage in enumerate(stages):
            box = RoundedRectangle(width=2.2, height=1.1, color=INK, stroke_width=1.8).set_fill("#EAE7DC", opacity=1)
            box.move_to(LEFT*5 + RIGHT*(i * 2.5))
            label = Text(stage, font_size=24, color=INK, font=FONT).move_to(box)
            grp = VGroup(box, label)
            stage_mobs.append(grp)

        self.play(*[FadeIn(m) for m in stage_mobs], run_time=0.5)

        # Arrows between stages
        for i in range(len(stages) - 1):
            arr = Arrow(stage_mobs[i].get_right(), stage_mobs[i+1].get_left(), color=INK, stroke_width=1.5, buff=0.05)
            self.play(Create(arr), run_time=0.2)

        # Audio master clock line
        audio_mob = stage_mobs[2]
        master_line = DashedLine(audio_mob.get_bottom(), audio_mob.get_bottom() + DOWN*1.5, color=TERRA, stroke_width=2.5)
        master_label = Text("Master clock", font_size=24, color=INK, font=FONT).next_to(master_line, DOWN, buff=0.3)
        self.play(Create(master_line), Write(master_label), run_time=0.4)

        # Gate diamonds at beats and QC — INK color to avoid §8.3 TERRA contrast failure
        gate_positions = [stage_mobs[1].get_top() + UP*0.4, stage_mobs[4].get_top() + UP*0.4]
        for gpos in gate_positions:
            gate = Square(side_length=0.5, color=INK, stroke_width=2.5).set_fill(INK, opacity=0.15).rotate(PI/4).move_to(gpos)
            # Place gate label above gate to avoid overflowing right edge (stage 4 at x=5)
            gate_label = Text("Gate\n(human)", font_size=24, color=INK, font=FONT).next_to(gate, UP, buff=0.1)
            self.play(FadeIn(gate), Write(gate_label), run_time=0.3)

        made = Text("Human owns the argument.", font_size=30, color=INK, weight=BOLD, font=FONT).shift(DOWN*3)
        self.play(Write(made), run_time=0.5)
        self.wait(0.9)


class B04_BuildAudit(Scene):
    """B04 — do this now: two passes over one artifact."""
    def construct(self):
        artifact = RoundedRectangle(width=5, height=3.5, color=INK, stroke_width=2.5).set_fill("#EAE7DC", opacity=1)
        artifact_label = Text("Artifact", font_size=28, color=INK, weight=BOLD, font=FONT).next_to(artifact, UP, buff=0.2)
        self.play(FadeIn(artifact), Write(artifact_label), run_time=0.4)

        build_arrow = CurvedArrow(artifact.get_left() + LEFT*1.5, artifact.get_left(), color=INK, stroke_width=2.5, angle=PI/3)
        build_label = Text("Build", font_size=26, color=INK, weight=BOLD, font=FONT).next_to(build_arrow, LEFT, buff=0.1)
        self.play(Create(build_arrow), Write(build_label), run_time=0.5)

        audit_arrow = CurvedArrow(artifact.get_right(), artifact.get_right() + RIGHT*1.5, color=INK, stroke_width=2.5, angle=-PI/3)
        audit_label = Text("Audit", font_size=26, color=INK, weight=BOLD, font=FONT).next_to(audit_arrow, RIGHT, buff=0.1)
        self.play(Create(audit_arrow), Write(audit_label), run_time=0.4)

        sub = Text("Two exercises.\nSame artifact.", font_size=30, color=INK, font=FONT).shift(DOWN*2.8)
        self.play(Write(sub), run_time=0.5)
        self.wait(0.9)
