"""
scenes.py — hai-vox-isotope-swap
Manim scenes for the six GRAPHIC beats: B03 LesionMap, B05 NaiveLoop,
B07 IsotopeSwap, B08 BindingLogic, B10 ScanPredicts, B11 Example.
Palette: humanitarians (newsprint cream + teal target-positive + crimson target-negative).
"""
from manim import *

GROUND    = "#F3EBDD"
INK       = "#2F2A26"
TEAL      = "#1F6F5C"   # target-expressed / imaging-lit / respond
CRIMSON   = "#BF3339"   # PSMA-negative / dark / no response
SLATE_COL = "#3E5559"
GOLD      = "#F5D061"

config.background_color = GROUND
config.pixel_width  = 1920
config.pixel_height = 1080
config.frame_rate   = 24

SANS  = "Inter"
SERIF = "EB Garamond"


def ink_text(s, size=36, weight=NORMAL, color=INK, font=SANS):
    slant = "ITALIC" if weight == ITALIC else "NORMAL"
    w = weight if weight != ITALIC else NORMAL
    return Text(s, font=font, font_size=size, weight=w, slant=slant, color=color,
                disable_ligatures=True)


class B03_LesionMap(Scene):
    """Six lesions on a body outline — four teal (bright), two crimson (dark). ~7s"""

    def construct(self):
        title = ink_text("PSMA PET scan — six lesions", 40, BOLD).to_edge(UP, buff=0.6)
        # simplified torso silhouette
        torso = RoundedRectangle(
            corner_radius=0.6, width=4.0, height=6.0,
            stroke_color=INK, stroke_width=3, fill_color=GROUND, fill_opacity=1
        ).shift(DOWN * 0.3)
        # six lesion positions in the torso
        positions = [
            LEFT * 0.8 + UP * 1.6,
            RIGHT * 0.9 + UP * 0.8,
            LEFT * 1.1 + UP * 0.1,
            RIGHT * 0.7 + DOWN * 0.6,
            LEFT * 0.6 + DOWN * 1.4,      # dark
            RIGHT * 1.0 + DOWN * 1.9,     # dark (the largest)
        ]
        colors = [TEAL, TEAL, TEAL, TEAL, CRIMSON, CRIMSON]
        radii = [0.16, 0.20, 0.15, 0.18, 0.28, 0.34]
        lesions = VGroup(*[
            Circle(radius=r, color=c, fill_color=c, fill_opacity=0.9, stroke_width=2)
            .move_to(torso.get_center() + p)
            for p, c, r in zip(positions, colors, radii)
        ])
        pos_label = ink_text("PSMA-positive: 4", 26, color=TEAL).to_edge(LEFT, buff=0.6).shift(DOWN * 0.2)
        neg_label = ink_text("PSMA-negative: 2", 26, color=CRIMSON).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.2)

        self.play(Write(title), run_time=0.9)
        self.play(Create(torso), run_time=1.0)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in lesions], lag_ratio=0.15), run_time=2.1)
        self.play(FadeIn(pos_label), FadeIn(neg_label), run_time=0.6)
        self.wait(2.5)


class B05_NaiveLoop(Scene):
    """Two-box direct arrow: DIAGNOSIS → TREAT. The naive loop. ~12.5s"""

    def construct(self):
        title = ink_text("The naive loop", 40, BOLD).to_edge(UP, buff=0.6)
        box_dx = ink_text("DIAGNOSIS", 28, BOLD, font=SANS)
        sub_dx = ink_text("prostate cancer", 22, color=SLATE_COL, font=SERIF)
        dx_group = VGroup(box_dx, sub_dx).arrange(DOWN, buff=0.15)
        rect_dx = SurroundingRectangle(dx_group, buff=0.35, color=INK, stroke_width=3)
        dx = VGroup(rect_dx, dx_group).move_to(LEFT * 3.2 + DOWN * 0.2)

        box_tr = ink_text("TREAT", 28, BOLD, font=SANS)
        sub_tr = ink_text("with the drug", 22, color=SLATE_COL, font=SERIF)
        tr_group = VGroup(box_tr, sub_tr).arrange(DOWN, buff=0.15)
        rect_tr = SurroundingRectangle(tr_group, buff=0.35, color=INK, stroke_width=3)
        tr = VGroup(rect_tr, tr_group).move_to(RIGHT * 3.2 + DOWN * 0.2)

        arrow = Arrow(rect_dx.get_right(), rect_tr.get_left(), color=INK,
                      stroke_width=4, buff=0.15, max_tip_length_to_length_ratio=0.06)

        caption = ink_text("Simple. Satisfying. Wrong.", 28, ITALIC,
                           color=CRIMSON, font=SERIF).to_edge(DOWN, buff=0.8)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(dx), run_time=0.9)
        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(FadeIn(tr), run_time=0.9)
        self.wait(1.8)
        self.play(FadeIn(caption), run_time=0.7)
        self.wait(6.5)


class B07_IsotopeSwap(Scene):
    """Same molecule, isotope chip swaps Ga-68 → Lu-177. ~18s"""

    def construct(self):
        title = ink_text("One molecule. Two isotopes.", 42, BOLD).to_edge(UP, buff=0.6)

        molecule_label = ink_text("PSMA-targeting molecule", 22,
                                  color=SLATE_COL, font=SERIF)
        molecule = Circle(radius=0.9, color=INK, stroke_width=4,
                          fill_color=GROUND, fill_opacity=1)
        mol_group = VGroup(molecule, molecule_label.next_to(molecule, DOWN, buff=0.25))

        chip_ga = RoundedRectangle(corner_radius=0.15, width=1.6, height=0.7,
                                    stroke_color=TEAL, stroke_width=3,
                                    fill_color=TEAL, fill_opacity=0.15)
        ga_text = ink_text("Ga-68", 28, BOLD, color=TEAL).move_to(chip_ga)
        chip_ga_grp = VGroup(chip_ga, ga_text).next_to(molecule, UP, buff=0.4)

        role_ga = ink_text("PET IMAGING PROBE", 24, BOLD, color=TEAL)\
            .next_to(chip_ga_grp, UP, buff=0.4)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(mol_group), run_time=1.0)
        self.play(FadeIn(chip_ga_grp), FadeIn(role_ga), run_time=1.0)
        self.wait(2.5)

        chip_lu = RoundedRectangle(corner_radius=0.15, width=1.6, height=0.7,
                                    stroke_color=CRIMSON, stroke_width=3,
                                    fill_color=CRIMSON, fill_opacity=0.15)
        lu_text = ink_text("Lu-177", 28, BOLD, color=CRIMSON).move_to(chip_lu)
        chip_lu_grp = VGroup(chip_lu, lu_text).next_to(molecule, UP, buff=0.4)

        role_lu = ink_text("THERAPEUTIC DRUG", 24, BOLD, color=CRIMSON)\
            .next_to(chip_lu_grp, UP, buff=0.4)

        self.play(
            Transform(chip_ga_grp, chip_lu_grp),
            Transform(role_ga, role_lu),
            run_time=1.4,
        )
        self.wait(2.0)

        caption = ink_text("The targeting biology does not change.",
                           28, ITALIC, font=SERIF).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(caption), run_time=0.8)
        self.wait(7.5)


class B08_BindingLogic(Scene):
    """Two tumor cells: left binds (teal receptors), right misses (no receptors). ~15s"""

    def construct(self):
        title = ink_text("PSMA present → drug binds. Absent → drug misses.",
                         34, BOLD).to_edge(UP, buff=0.6)

        # LEFT cell — PSMA-positive
        cell_l = Circle(radius=1.5, color=TEAL, stroke_width=4,
                        fill_color=TEAL, fill_opacity=0.10).shift(LEFT * 3.5 + DOWN * 0.4)
        receptors_l = VGroup(*[
            Line(cell_l.get_center() + 1.5 * np.array([np.cos(a), np.sin(a), 0]),
                 cell_l.get_center() + 1.9 * np.array([np.cos(a), np.sin(a), 0]),
                 color=TEAL, stroke_width=5)
            for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)
        ])
        drug_l = Triangle(color=INK, fill_color=INK, fill_opacity=1)\
            .scale(0.20).move_to(cell_l.get_center() + RIGHT * 2.4)
        label_l = ink_text("PSMA-positive: drug binds", 22, color=TEAL, font=SERIF)\
            .next_to(cell_l, DOWN, buff=0.5)

        # RIGHT cell — PSMA-negative
        cell_r = Circle(radius=1.5, color=CRIMSON, stroke_width=4,
                        fill_color=CRIMSON, fill_opacity=0.08).shift(RIGHT * 3.5 + DOWN * 0.4)
        cross = VGroup(
            Line(cell_r.get_center() + UP * 0.4 + LEFT * 0.4,
                 cell_r.get_center() + DOWN * 0.4 + RIGHT * 0.4,
                 color=CRIMSON, stroke_width=6),
            Line(cell_r.get_center() + UP * 0.4 + RIGHT * 0.4,
                 cell_r.get_center() + DOWN * 0.4 + LEFT * 0.4,
                 color=CRIMSON, stroke_width=6),
        )
        drug_r = Triangle(color=INK, fill_color=INK, fill_opacity=1)\
            .scale(0.20).move_to(cell_r.get_center() + RIGHT * 2.4)
        label_r = ink_text("PSMA-negative: drug misses", 22, color=CRIMSON, font=SERIF)\
            .next_to(cell_r, DOWN, buff=0.5)

        self.play(Write(title), run_time=1.0)
        self.play(FadeIn(cell_l), Create(receptors_l),
                  FadeIn(cell_r), Create(cross), run_time=1.4)
        self.play(FadeIn(label_l), FadeIn(label_r), run_time=0.6)
        self.play(FadeIn(drug_l), FadeIn(drug_r), run_time=0.6)
        # Drug on the left docks (moves in), drug on the right passes through
        self.play(
            drug_l.animate.move_to(cell_l.get_center() + RIGHT * 1.55),
            drug_r.animate.move_to(cell_r.get_center() + LEFT * 2.4),
            run_time=1.8,
        )
        self.wait(9.5)


class B10_ScanPredicts(Scene):
    """Decision split: BRIGHT on PET → TREAT vs DARK → DO NOT TREAT. ~11.4s"""

    def construct(self):
        title = ink_text("The scan encodes the decision.", 40, BOLD)\
            .to_edge(UP, buff=0.6)

        # LEFT branch — BRIGHT / TREAT
        bright = ink_text("BRIGHT on PET", 28, BOLD, color=TEAL)
        r_bright = SurroundingRectangle(bright, buff=0.25, color=TEAL, stroke_width=3)
        bright_grp = VGroup(r_bright, bright).shift(LEFT * 3.3 + UP * 0.6)

        treat = ink_text("TREATS TARGET", 26, BOLD, color=TEAL)
        r_treat = SurroundingRectangle(treat, buff=0.25, color=TEAL, stroke_width=3,
                                        corner_radius=0.15)
        treat_grp = VGroup(r_treat, treat).shift(LEFT * 3.3 + DOWN * 1.8)
        arrow_l = Arrow(r_bright.get_bottom(), r_treat.get_top(), color=TEAL,
                        stroke_width=4, buff=0.15, max_tip_length_to_length_ratio=0.08)

        # RIGHT branch — DARK / CANNOT BIND
        dark = ink_text("DARK on PET", 28, BOLD, color=CRIMSON)
        r_dark = SurroundingRectangle(dark, buff=0.25, color=CRIMSON, stroke_width=3)
        dark_grp = VGroup(r_dark, dark).shift(RIGHT * 3.3 + UP * 0.6)

        no_treat = ink_text("CANNOT BIND", 26, BOLD, color=CRIMSON)
        r_no = SurroundingRectangle(no_treat, buff=0.25, color=CRIMSON, stroke_width=3,
                                     corner_radius=0.15)
        no_grp = VGroup(r_no, no_treat).shift(RIGHT * 3.3 + DOWN * 1.8)
        arrow_r = Arrow(r_dark.get_bottom(), r_no.get_top(), color=CRIMSON,
                        stroke_width=4, buff=0.15, max_tip_length_to_length_ratio=0.08)

        caption = ink_text("THE SCAN DECIDES", 28, BOLD, color=INK, font=SANS)\
            .to_edge(DOWN, buff=0.7)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(bright_grp), FadeIn(dark_grp), run_time=0.9)
        self.play(GrowArrow(arrow_l), GrowArrow(arrow_r), run_time=0.8)
        self.play(FadeIn(treat_grp), FadeIn(no_grp), run_time=0.8)
        self.play(Write(caption), run_time=0.8)
        self.wait(6.4)


class B11_Example(Scene):
    """Before/after: 4 teal shrink −60%, 2 crimson grow +40%. Illustrative. ~22.5s"""

    def construct(self):
        title = ink_text("Worked example — six lesions, day 90", 36, BOLD)\
            .to_edge(UP, buff=0.5)

        # Column headers
        hdr_before = ink_text("BEFORE TREATMENT", 24, BOLD).shift(LEFT * 3.5 + UP * 1.9)
        hdr_after = ink_text("DAY 90", 24, BOLD).shift(RIGHT * 3.5 + UP * 1.9)

        # BEFORE — 6 lesions all at their starting sizes
        positions_before = [
            LEFT * 4.5 + UP * 0.8, LEFT * 3.5 + UP * 0.2, LEFT * 2.5 + UP * 0.8,
            LEFT * 4.5 + DOWN * 0.7, LEFT * 3.0 + DOWN * 1.3, LEFT * 2.4 + DOWN * 0.3,
        ]
        radii_before = [0.28, 0.28, 0.28, 0.28, 0.34, 0.34]
        colors_before = [TEAL, TEAL, TEAL, TEAL, CRIMSON, CRIMSON]
        lesions_before = VGroup(*[
            Circle(radius=r, color=c, fill_color=c, fill_opacity=0.9, stroke_width=2)
            .move_to(p)
            for p, r, c in zip(positions_before, radii_before, colors_before)
        ])

        # AFTER — teal lesions 40% of size (shrank 60%), crimson lesions 140% (grew 40%)
        positions_after = [
            RIGHT * 2.5 + UP * 0.8, RIGHT * 3.5 + UP * 0.2, RIGHT * 4.5 + UP * 0.8,
            RIGHT * 2.5 + DOWN * 0.7, RIGHT * 4.0 + DOWN * 1.3, RIGHT * 4.6 + DOWN * 0.3,
        ]
        radii_after = [0.28 * 0.4, 0.28 * 0.4, 0.28 * 0.4, 0.28 * 0.4, 0.34 * 1.4, 0.34 * 1.4]
        colors_after = [TEAL, TEAL, TEAL, TEAL, CRIMSON, CRIMSON]
        lesions_after = VGroup(*[
            Circle(radius=r, color=c, fill_color=c, fill_opacity=0.9, stroke_width=2)
            .move_to(p)
            for p, r, c in zip(positions_after, radii_after, colors_after)
        ])

        chip_shrink = ink_text("-60%", 32, BOLD, color=TEAL)\
            .shift(RIGHT * 3.4 + DOWN * 2.2)
        chip_grow = ink_text("+40%", 32, BOLD, color=CRIMSON)\
            .shift(RIGHT * 4.6 + DOWN * 2.2)

        illustrative = ink_text("illustrative", 18, ITALIC,
                                color=SLATE_COL, font=SERIF)\
            .to_edge(DOWN, buff=0.4).to_edge(RIGHT, buff=0.5)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(hdr_before), FadeIn(hdr_after), run_time=0.7)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in lesions_before],
                              lag_ratio=0.1), run_time=1.6)
        self.wait(1.5)
        self.play(TransformFromCopy(lesions_before, lesions_after), run_time=2.2)
        self.play(FadeIn(chip_shrink), FadeIn(chip_grow), run_time=0.7)
        self.play(FadeIn(illustrative), run_time=0.4)
        self.wait(14.0)
