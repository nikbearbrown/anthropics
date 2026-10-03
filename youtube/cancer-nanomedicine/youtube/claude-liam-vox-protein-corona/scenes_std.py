"""scenes_std.py — GRAPHIC beats for claude-liam-vox-protein-corona.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Color law: TEAL = engineered particle surface / targeting ligands (the thing you built).
           CRIMSON = protein corona / masking / liver clearance (the thing the body sees).
           GOLD = the moment / editor's-pen highlight. Never swap mid-film.

Scenes: B04_CoronaForms, B05_LigandMasked, B06_OpsominClearance,
        B07_TwoEnvironments, B09_FolateExample

Run all:
  python3 scenes_std.py
"""
import json
import math
import pathlib
import subprocess
import sys

from manim import *

GROUND   = "#F3EBDD"
INK      = "#2F2A26"
TEAL     = "#1F6F5C"
CRIMSON  = "#BF3339"
GOLD     = "#F5D061"
SLATE    = "#3E5559"
HAIRLINE = "#D4D4D4"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"

_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 12.0 for i in range(1, 18)}


class LabelChip(VGroup):
    def __init__(self, text, accent=CRIMSON, size=15):
        super().__init__()
        t = Text(text.upper(), font=DISPLAY, color=WHITE, font_size=int(size))
        bg = Rectangle(width=t.width + 0.3, height=t.height + 0.18)
        bg.set_fill(accent, 0.92).set_stroke(width=0, opacity=0)
        bg.move_to(t)
        self.add(bg, t)


def _bg(scene):
    scene.camera.background_color = GROUND


# ── B04 Corona forms — proteins pile onto the particle ─────────────────────
class B04_CoronaForms(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B04", 14.17)
        title = Text("Protein corona forms", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        title.move_to(UP * 3.0)
        # teal nanoparticle
        particle = Circle(radius=1.2).set_fill(TEAL, 0.85).set_stroke(TEAL, 2.5)
        particle.move_to(ORIGIN + DOWN * 0.1)
        # small teal targeting ligands on the perimeter
        ligands = VGroup()
        for angle_deg in range(0, 360, 30):
            a = math.radians(angle_deg)
            end = particle.get_center() + [math.cos(a) * 1.5, math.sin(a) * 1.5, 0]
            base = particle.get_center() + [math.cos(a) * 1.15, math.sin(a) * 1.15, 0]
            arm = Line(base, end, stroke_width=2.5, color=TEAL)
            tip = Dot(radius=0.06, color=TEAL).move_to(end)
            ligands.add(arm, tip)
        # crimson protein blobs that will pile on
        proteins = VGroup()
        for angle_deg in range(15, 360, 20):
            a = math.radians(angle_deg)
            r = 1.55 + (0.15 * ((angle_deg // 20) % 3))
            pos = particle.get_center() + [math.cos(a) * r, math.sin(a) * r, 0]
            p = Ellipse(width=0.32, height=0.22).set_fill(CRIMSON, 0.88).set_stroke(width=0)
            p.rotate(a)
            p.move_to(pos)
            proteins.add(p)
        chip = LabelChip("within seconds", accent=GOLD, size=15)
        chip.submobjects[1].set_color(INK)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(particle), run_time=0.6)
        self.play(Create(ligands), run_time=0.9)
        self.play(FadeIn(proteins, shift=UP * 0.05), run_time=1.6)
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(max(0.3, total - 3.9))


# ── B05 Ligand masked — protein covers the targeting arm ───────────────────
class B05_LigandMasked(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 14.14)
        title = Text("Ligand masked", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        title.move_to(UP * 3.0)
        # left: particle with one extended ligand
        particle = Circle(radius=0.95).set_fill(TEAL, 0.85).set_stroke(TEAL, 2.5)
        particle.move_to(LEFT * 3.0)
        arm = Line(particle.get_center() + RIGHT * 0.95,
                   particle.get_center() + RIGHT * 2.4,
                   stroke_width=4, color=TEAL)
        tip = Dot(radius=0.14, color=TEAL).move_to(particle.get_center() + RIGHT * 2.4)
        # right: receptor on a cell membrane
        cell = Rectangle(width=1.4, height=3.2).set_fill(SLATE, 0.12).set_stroke(INK, 2)
        cell.move_to(RIGHT * 3.5)
        receptor = Arc(radius=0.35, start_angle=PI/2, angle=-PI,
                       color=INK, stroke_width=3)
        receptor.move_to(RIGHT * 2.85)
        rec_lbl = Text("receptor", font=DISPLAY, color=INK, font_size=14)
        rec_lbl.next_to(cell, UP, buff=0.15)
        # crimson protein block that slides in and covers the ligand
        block = Rectangle(width=1.1, height=1.0).set_fill(CRIMSON, 0.9).set_stroke(width=0)
        block.move_to(particle.get_center() + RIGHT * 1.75)
        block.set_opacity(0)
        chip = LabelChip("ligand buried — cannot bind", accent=CRIMSON, size=15)
        chip.move_to(DOWN * 3.0)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(particle), Create(arm), FadeIn(tip), run_time=0.7)
        self.play(FadeIn(cell), Create(receptor), FadeIn(rec_lbl), run_time=0.7)
        self.wait(0.6)
        self.play(block.animate.set_opacity(0.92), run_time=1.0)
        self.play(FadeIn(chip), run_time=0.5)
        self.wait(max(0.3, total - 3.9))


# ── B06 Opsonin flags particle for liver clearance ─────────────────────────
class B06_OpsominClearance(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 14.59)
        title = Text("Opsonins flag the particle", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        title.move_to(UP * 3.0)
        # coated particle at left — full crimson corona
        core = Circle(radius=0.8).set_fill(TEAL, 0.85).set_stroke(TEAL, 2)
        core.move_to(LEFT * 3.6)
        coat = Annulus(inner_radius=0.85, outer_radius=1.2, color=CRIMSON,
                        fill_opacity=0.85, stroke_width=0)
        coat.move_to(core.get_center())
        opsonin_lbl = LabelChip("opsonin", accent=CRIMSON, size=13)
        opsonin_lbl.next_to(coat, UP, buff=0.25)
        # arrow crimson pointing right
        arrow = Arrow(LEFT * 2.0, RIGHT * 1.0, color=CRIMSON, buff=0.05, stroke_width=6)
        arrow.move_to(LEFT * 0.5)
        # macrophage on right — kidney-shape circle
        macro = Circle(radius=1.1).set_fill(SLATE, 0.20).set_stroke(INK, 2)
        macro.move_to(RIGHT * 3.4)
        # small bumps for macrophage character
        for angle_deg in (30, 90, 150, 210, 270, 330):
            a = math.radians(angle_deg)
            bump = Circle(radius=0.18).set_fill(SLATE, 0.20).set_stroke(INK, 2)
            bump.move_to(macro.get_center() + [math.cos(a) * 1.05, math.sin(a) * 1.05, 0])
            macro.add(bump)
        macro_lbl = Text("liver macrophage", font=DISPLAY, color=INK, font_size=15)
        macro_lbl.next_to(macro, DOWN, buff=0.25)
        chip = LabelChip("flagged for clearance", accent=CRIMSON, size=15)
        chip.move_to(DOWN * 3.15)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(core), run_time=0.4)
        self.play(FadeIn(coat), run_time=0.5)
        self.play(FadeIn(opsonin_lbl), run_time=0.4)
        self.play(FadeIn(macro), FadeIn(macro_lbl), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.play(FadeIn(chip), run_time=0.4)
        self.wait(max(0.3, total - 4.0))


# ── B07 Two environments — culture medium vs blood ─────────────────────────
class B07_TwoEnvironments(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 15.15)
        title = Text("Culture medium vs blood", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        title.move_to(UP * 3.15)
        # left panel: culture medium
        left = Rectangle(width=5.6, height=4.0).set_fill(TEAL, 0.06).set_stroke(TEAL, 1.6)
        left.move_to(LEFT * 3.2 + DOWN * 0.2)
        left_hdr = LabelChip("culture medium", accent=TEAL, size=15)
        left_hdr.move_to(left.get_top() + DOWN * 0.32)
        # naked particle + ligand binding a receptor
        p1 = Circle(radius=0.55).set_fill(TEAL, 0.85).set_stroke(TEAL, 2)
        p1.move_to(left.get_center() + LEFT * 1.2 + DOWN * 0.2)
        arm1 = Line(p1.get_center() + RIGHT * 0.55, p1.get_center() + RIGHT * 1.5,
                    stroke_width=3, color=TEAL)
        tip1 = Dot(radius=0.10, color=TEAL).move_to(p1.get_center() + RIGHT * 1.5)
        cell1 = Rectangle(width=0.55, height=1.7).set_fill(SLATE, 0.12).set_stroke(INK, 2)
        cell1.move_to(left.get_center() + RIGHT * 1.5 + DOWN * 0.2)
        rec1 = Arc(radius=0.22, start_angle=PI/2, angle=-PI, color=INK, stroke_width=3)
        rec1.move_to(cell1.get_left() + RIGHT * 0.1)
        chk_l = LabelChip("binds", accent=TEAL, size=13)
        chk_l.move_to(left.get_bottom() + UP * 0.4)
        # right panel: blood
        right = Rectangle(width=5.6, height=4.0).set_fill(CRIMSON, 0.06).set_stroke(CRIMSON, 1.6)
        right.move_to(RIGHT * 3.2 + DOWN * 0.2)
        right_hdr = LabelChip("blood", accent=CRIMSON, size=15)
        right_hdr.move_to(right.get_top() + DOWN * 0.32)
        # coated particle heading to a liver macrophage
        core2 = Circle(radius=0.4).set_fill(TEAL, 0.85).set_stroke(TEAL, 2)
        core2.move_to(right.get_center() + LEFT * 1.4 + DOWN * 0.2)
        coat2 = Annulus(inner_radius=0.45, outer_radius=0.65, color=CRIMSON,
                        fill_opacity=0.85, stroke_width=0)
        coat2.move_to(core2.get_center())
        arrow2 = Arrow(right.get_center() + LEFT * 0.5 + DOWN * 0.2,
                       right.get_center() + RIGHT * 1.1 + DOWN * 0.2,
                       color=CRIMSON, buff=0.05, stroke_width=5)
        liver = Circle(radius=0.5).set_fill(SLATE, 0.20).set_stroke(INK, 2)
        liver.move_to(right.get_center() + RIGHT * 1.55 + DOWN * 0.2)
        liver_lbl = Text("liver", font=DISPLAY, color=INK, font_size=13)
        liver_lbl.next_to(liver, DOWN, buff=0.12)
        chk_r = LabelChip("buried — liver", accent=CRIMSON, size=13)
        chk_r.move_to(right.get_bottom() + UP * 0.4)
        # gold divider
        div = Line(UP * 2.8, DOWN * 2.8, stroke_width=3, color=GOLD)
        div.move_to(ORIGIN + DOWN * 0.2)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(left), FadeIn(right), run_time=0.5)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(FadeIn(div), run_time=0.3)
        self.play(GrowFromCenter(p1), Create(arm1), FadeIn(tip1),
                  FadeIn(cell1), Create(rec1), run_time=1.0)
        self.play(FadeIn(chk_l), run_time=0.4)
        self.play(GrowFromCenter(core2), FadeIn(coat2), run_time=0.7)
        self.play(FadeIn(liver), FadeIn(liver_lbl), run_time=0.4)
        self.play(GrowArrow(arrow2), run_time=0.6)
        self.play(FadeIn(chk_r), run_time=0.4)
        self.wait(max(0.3, total - 5.1))


# ── B09 Folate example — culture 87% vs blood 3% at tumor ─────────────────
class B09_FolateExample(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 22.31)
        title = Text("Folate-targeted particle", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        title.move_to(UP * 3.2)
        # left column: IN CULTURE — one teal bar 87%
        left_hdr = LabelChip("in culture", accent=TEAL, size=14)
        left_hdr.move_to(LEFT * 3.5 + UP * 2.4)
        cul_bar_h = 3.5 * 0.87
        cul_bar = Rectangle(width=1.2, height=cul_bar_h).set_fill(TEAL, 0.85).set_stroke(width=0)
        cul_axis_base = LEFT * 3.5 + DOWN * 1.8
        cul_bar.move_to(cul_axis_base + UP * (cul_bar_h / 2))
        cul_num = Text("87%", font=DISPLAY, color=TEAL, font_size=26, weight=BOLD)
        cul_num.next_to(cul_bar, UP, buff=0.15)
        cul_lbl = Text("binds folate receptor", font=DISPLAY, color=INK, font_size=13)
        cul_lbl.next_to(cul_bar, DOWN, buff=0.2)
        # right column: IN BLOOD — crimson 72% liver, teal 3% tumor
        right_hdr = LabelChip("in blood (4 h post-inject)", accent=CRIMSON, size=14)
        right_hdr.move_to(RIGHT * 3.0 + UP * 2.4)
        liv_bar_h = 3.5 * 0.72
        liv_bar = Rectangle(width=1.0, height=liv_bar_h).set_fill(CRIMSON, 0.85).set_stroke(width=0)
        liv_base = RIGHT * 1.7 + DOWN * 1.8
        liv_bar.move_to(liv_base + UP * (liv_bar_h / 2))
        liv_num = Text("72%", font=DISPLAY, color=CRIMSON, font_size=22, weight=BOLD)
        liv_num.next_to(liv_bar, UP, buff=0.15)
        liv_lbl = Text("liver", font=DISPLAY, color=INK, font_size=13)
        liv_lbl.next_to(liv_bar, DOWN, buff=0.2)
        tum_bar_h = 3.5 * 0.03
        tum_bar = Rectangle(width=1.0, height=max(tum_bar_h, 0.08)).set_fill(TEAL, 0.85).set_stroke(width=0)
        tum_base = RIGHT * 4.2 + DOWN * 1.8
        tum_bar.move_to(tum_base + UP * (max(tum_bar_h, 0.08) / 2))
        tum_num = Text("3%", font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
        tum_num.next_to(tum_bar, UP, buff=0.15)
        tum_lbl = Text("tumor", font=DISPLAY, color=INK, font_size=13)
        tum_lbl.next_to(tum_bar, DOWN, buff=0.2)
        # baseline axis
        axis_l = Line(LEFT * 4.2 + DOWN * 1.8, LEFT * 2.8 + DOWN * 1.8,
                      stroke_width=1.5, color=INK)
        axis_r = Line(RIGHT * 1.0 + DOWN * 1.8, RIGHT * 5.0 + DOWN * 1.8,
                      stroke_width=1.5, color=INK)
        # illustrative footer
        foot = Text("illustrative numbers — mechanism, not measurement",
                    font=SERIF, color=INK, font_size=15, slant=ITALIC)
        foot.move_to(DOWN * 3.1)
        self.play(FadeIn(title), run_time=0.4)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.4)
        self.play(Create(axis_l), Create(axis_r), run_time=0.5)
        self.play(GrowFromEdge(cul_bar, DOWN), run_time=0.9)
        self.play(FadeIn(cul_num), FadeIn(cul_lbl), run_time=0.5)
        self.wait(0.4)
        self.play(GrowFromEdge(liv_bar, DOWN), run_time=0.9)
        self.play(FadeIn(liv_num), FadeIn(liv_lbl), run_time=0.5)
        self.play(GrowFromEdge(tum_bar, DOWN), run_time=0.7)
        self.play(FadeIn(tum_num), FadeIn(tum_lbl), run_time=0.5)
        self.play(FadeIn(foot), run_time=0.6)
        self.wait(max(0.3, total - 6.4))


# ── B10 Corona summary — recap with editor's ring on the coat ──────────────
class B10_CoronaSummary(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 12.86)
        title = Text("Months of engineering, seconds of corona",
                     font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        title.move_to(UP * 3.0)
        # fully-coated particle
        core = Circle(radius=1.0).set_fill(TEAL, 0.85).set_stroke(TEAL, 2.5)
        core.move_to(ORIGIN + DOWN * 0.1)
        # small buried ligand dots on the teal core
        ligand_dots = VGroup()
        for angle_deg in range(0, 360, 45):
            a = math.radians(angle_deg)
            d = Dot(radius=0.09, color=TEAL).move_to(
                core.get_center() + [math.cos(a) * 0.95, math.sin(a) * 0.95, 0])
            ligand_dots.add(d)
        coat = Annulus(inner_radius=1.05, outer_radius=1.5, color=CRIMSON,
                        fill_opacity=0.85, stroke_width=0)
        coat.move_to(core.get_center())
        # editor's ring on the corona layer (drawn on cue "seconds")
        ring = Circle(radius=1.65).set_stroke(GOLD, 5).set_fill(opacity=0)
        ring.move_to(core.get_center())
        # two labels with arrows
        lbl_teal = Text("targeting ligands — buried",
                        font=SERIF, color=TEAL, font_size=18, slant=ITALIC)
        lbl_teal.move_to(LEFT * 3.5 + DOWN * 0.1)
        arr_teal = Arrow(lbl_teal.get_right() + RIGHT * 0.1,
                         core.get_left() + RIGHT * 0.1,
                         color=TEAL, buff=0.05, stroke_width=3)
        lbl_crim = Text("protein corona — seconds",
                        font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        lbl_crim.move_to(RIGHT * 3.5 + DOWN * 0.1)
        arr_crim = Arrow(lbl_crim.get_left() + LEFT * 0.1,
                         core.get_right() + LEFT * 0.1 + RIGHT * 0.4,
                         color=CRIMSON, buff=0.05, stroke_width=3)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(core), run_time=0.5)
        self.play(FadeIn(ligand_dots), run_time=0.5)
        self.play(FadeIn(coat), run_time=0.7)
        self.play(FadeIn(lbl_teal), GrowArrow(arr_teal), run_time=0.7)
        self.play(FadeIn(lbl_crim), GrowArrow(arr_crim), run_time=0.7)
        self.play(Create(ring), run_time=0.9)
        self.wait(max(0.3, total - 4.4))


SCENES = [
    ("B04_CoronaForms",     "B04"),
    ("B05_LigandMasked",    "B05"),
    ("B06_OpsominClearance","B06"),
    ("B07_TwoEnvironments", "B07"),
    ("B09_FolateExample",   "B09"),
    ("B10_CoronaSummary",   "B10"),
]

if __name__ == "__main__":
    reel = pathlib.Path(__file__).resolve().parent
    manim_dir = reel / "manim"
    manim_dir.mkdir(exist_ok=True)
    failed = []
    for scene_cls, bid in SCENES:
        print(f"[render] {scene_cls} -> manim/{bid}.mp4")
        out_dir = reel / "media" / "videos" / "scenes_std" / "1080p24"
        mp4_src = out_dir / f"{scene_cls}.mp4"
        mp4_dst = manim_dir / f"{bid}.mp4"
        result = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  FAIL: {result.stderr[-500:]}")
            failed.append(scene_cls)
            continue
        if mp4_src.exists():
            import shutil
            shutil.copy2(mp4_src, mp4_dst)
            print(f"  OK -> {mp4_dst}")
        else:
            print(f"  ERROR: output not found at {mp4_src}")
            failed.append(scene_cls)
    if failed:
        print(f"\nFailed scenes: {failed}")
        sys.exit(1)
    print(f"\nAll {len(SCENES)} scenes rendered to manim/")
