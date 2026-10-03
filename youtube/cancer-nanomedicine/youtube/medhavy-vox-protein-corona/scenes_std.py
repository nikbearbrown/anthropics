"""scenes_std.py — GRAPHIC beats for medhavy-vox-protein-corona.

Newsprint palette (#F3EBDD ground / #2F2A26 ink / #1F6F5C teal / #BF3339 crimson / #F5D061 gold).
Scenes: B04_CoronaForms, B05_LigandMasked, B06_OpsominClearance,
        B07_TwoEnvironments, B09_FolateExample, B10_CoronaSummary

Render everything to manim/<bid>.mp4:
    python3 scenes_std.py
"""
import json
import pathlib
import subprocess
import sys

from manim import *
import numpy as np

GROUND  = "#F3EBDD"
INK     = "#2F2A26"
TEAL    = "#1F6F5C"
CRIMSON = "#BF3339"
GOLD    = "#F5D061"

DISPLAY = "Montserrat"
SERIF   = "EB Garamond"
MONO    = "PT Mono"

_SHEET = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
try:
    _data = json.load(open(_SHEET))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {}


def _bg(scene):
    scene.camera.background_color = GROUND


def _ligands(center, r_inner, r_outer, n, color, sw=3):
    """Small radiating lines: n ligands around a particle center."""
    lines = VGroup()
    for a in np.linspace(0, 2 * np.pi, n, endpoint=False):
        c, s = np.cos(a), np.sin(a)
        lines.add(Line(
            [center[0] + r_inner * c, center[1] + r_inner * s, 0],
            [center[0] + r_outer * c, center[1] + r_outer * s, 0],
            stroke_width=sw, color=color))
    return lines


class B04_CoronaForms(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B04", 17.34)
        title = Text("Protein corona forms within seconds",
                     font=SERIF, font_size=28, color=INK).move_to(UP * 3.2)
        # Central engineered particle
        particle = Circle(radius=0.75, fill_color=TEAL, fill_opacity=0.85,
                          stroke_color=INK, stroke_width=2).move_to(ORIGIN)
        lig = _ligands([0, 0, 0], 0.75, 1.05, 12, TEAL, sw=3)
        lbl_p = Text("engineered surface  +  targeting ligands", font=DISPLAY,
                     font_size=18, color=TEAL).move_to(DOWN * 1.7)
        # Corona proteins — pile onto the surface
        proteins = VGroup(*[
            Circle(radius=0.18, fill_color=CRIMSON, fill_opacity=0.80,
                   stroke_color=INK, stroke_width=0.7).move_to(
                [1.15 * np.cos(a), 1.15 * np.sin(a), 0])
            for a in np.linspace(0.15, 2 * np.pi + 0.15, 14, endpoint=False)
        ])
        outer = VGroup(*[
            Circle(radius=0.14, fill_color=CRIMSON, fill_opacity=0.65,
                   stroke_color=INK, stroke_width=0.5).move_to(
                [1.4 * np.cos(a), 1.4 * np.sin(a), 0])
            for a in np.linspace(0.30, 2 * np.pi + 0.30, 16, endpoint=False)
        ])
        lbl_c = Text("protein corona  (albumin  ·  IgG  ·  fibrinogen  ·  opsonins)",
                     font=DISPLAY, font_size=17, color=CRIMSON).move_to(DOWN * 2.6)
        clock = Text("t  <  seconds", font=MONO, font_size=18, color=GOLD).move_to(UP * 2.4)
        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(particle), Create(lig), run_time=0.9)
        self.play(FadeIn(lbl_p), run_time=0.4)
        self.play(FadeIn(clock), run_time=0.3)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in proteins], lag_ratio=0.06, run_time=1.6))
        self.play(LaggedStart(*[GrowFromCenter(p) for p in outer], lag_ratio=0.05, run_time=1.3))
        self.play(FadeIn(lbl_c), run_time=0.5)
        self.wait(max(0.5, total - 5.5))


class B05_LigandMasked(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B05", 16.62)
        title = Text("Ligand masked — cannot bind",
                     font=SERIF, font_size=26, color=INK).move_to(UP * 3.2)
        # Particle with one visible ligand arm on the right
        particle = Circle(radius=0.65, fill_color=TEAL, fill_opacity=0.85,
                          stroke_color=INK, stroke_width=2).move_to(LEFT * 2.5)
        ligand = Line(particle.get_right(),
                      particle.get_right() + RIGHT * 0.8,
                      stroke_width=6, color=TEAL)
        ligand_tip = Dot(radius=0.10, color=TEAL).move_to(
            particle.get_right() + RIGHT * 0.85)
        lbl_lig = Text("targeting ligand", font=DISPLAY, font_size=16, color=TEAL)
        lbl_lig.next_to(particle, DOWN, buff=0.3)
        # Receptor on cell surface (right)
        cell_wall = Line(RIGHT * 3.5 + UP * 1.5, RIGHT * 3.5 + DOWN * 1.5,
                         stroke_width=3, color=INK)
        receptor = Rectangle(width=0.25, height=0.35, fill_color=INK,
                             fill_opacity=0.85, stroke_width=0).move_to(RIGHT * 3.35)
        lbl_cell = Text("cell surface  ·  receptor", font=DISPLAY,
                        font_size=15, color=INK).move_to(RIGHT * 3.5 + DOWN * 2.0)
        # Crimson corona slab that slides in and covers the ligand
        corona = Rectangle(width=0.7, height=1.6, fill_color=CRIMSON,
                           fill_opacity=0.85, stroke_color=INK, stroke_width=1)
        corona.move_to(LEFT * 2.5 + RIGHT * 0.85)
        corona.shift(UP * 4.5)   # off-screen start
        lbl_cor = Text("protein corona blocks the ligand",
                       font=DISPLAY, font_size=17, color=CRIMSON).move_to(DOWN * 2.6)
        # Blocked-attempt X mark between ligand tip and receptor
        x1 = Line([0, 0.2, 0], [0.4, -0.2, 0], color=CRIMSON, stroke_width=5)
        x2 = Line([0, -0.2, 0], [0.4, 0.2, 0], color=CRIMSON, stroke_width=5)
        cross = VGroup(x1, x2).move_to(RIGHT * 0.5)
        self.play(FadeIn(title), run_time=0.4)
        self.play(GrowFromCenter(particle), Create(cell_wall), FadeIn(receptor),
                  run_time=0.7)
        self.play(Create(ligand), FadeIn(ligand_tip), FadeIn(lbl_lig),
                  FadeIn(lbl_cell), run_time=0.8)
        self.wait(0.4)
        self.play(corona.animate.shift(DOWN * 4.5), run_time=1.1)
        self.play(FadeIn(lbl_cor), run_time=0.4)
        self.play(FadeIn(cross), run_time=0.5)
        self.wait(max(0.4, total - 4.3))


class B06_OpsominClearance(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B06", 18.45)
        title = Text("Opsonins on the corona flag the particle for clearance",
                     font=SERIF, font_size=22, color=INK).move_to(UP * 3.2)
        # Coated particle (left)
        core = Circle(radius=0.55, fill_color=TEAL, fill_opacity=0.85,
                      stroke_color=INK, stroke_width=1.5).move_to(LEFT * 3.0)
        ring = Circle(radius=0.85, fill_color=CRIMSON, fill_opacity=0.55,
                      stroke_color=INK, stroke_width=1.5).move_to(LEFT * 3.0)
        # Opsonin chip label
        chip_bg = Rectangle(width=1.8, height=0.4, fill_color=CRIMSON,
                            fill_opacity=0.9, stroke_width=0).move_to(LEFT * 3.0 + UP * 1.5)
        chip_t = Text("OPSONIN", font=DISPLAY, font_size=16, color=WHITE,
                      weight=BOLD).move_to(chip_bg.get_center())
        chip = VGroup(chip_bg, chip_t)
        chip_arrow = Arrow(chip_bg.get_bottom() + DOWN * 0.05,
                           ring.point_at_angle(np.pi / 2) + UP * 0.05,
                           color=CRIMSON, stroke_width=2, buff=0.05,
                           max_tip_length_to_length_ratio=0.2)
        # Macrophage (right)
        mac = Circle(radius=0.9, fill_color=INK, fill_opacity=0.35,
                     stroke_color=INK, stroke_width=2).move_to(RIGHT * 3.0)
        # bumpy edge (a few short lines around)
        bumps = VGroup(*[
            Line([3.0 + 0.9 * np.cos(a), 0 + 0.9 * np.sin(a), 0],
                 [3.0 + 1.05 * np.cos(a), 0 + 1.05 * np.sin(a), 0],
                 color=INK, stroke_width=2)
            for a in np.linspace(0, 2 * np.pi, 16, endpoint=False)
        ])
        lbl_mac = Text("macrophage  ·  liver / spleen", font=DISPLAY,
                       font_size=17, color=INK).move_to(RIGHT * 3.0 + DOWN * 1.8)
        # Arrow: particle → macrophage
        move_arrow = Arrow(ring.get_right() + RIGHT * 0.1,
                           mac.get_left() + LEFT * 0.1,
                           color=CRIMSON, stroke_width=4, buff=0.05)
        lbl_flag = Text("flagged for clearance", font=SERIF, font_size=20,
                        color=CRIMSON, slant=ITALIC).move_to(DOWN * 2.7)
        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(core), run_time=0.4)
        self.play(GrowFromCenter(ring), run_time=0.6)
        self.play(GrowFromCenter(mac), Create(bumps), FadeIn(lbl_mac), run_time=0.7)
        self.play(FadeIn(chip), Create(chip_arrow), run_time=0.7)
        self.play(GrowArrow(move_arrow), run_time=0.7)
        self.play(FadeIn(lbl_flag), run_time=0.5)
        self.wait(max(0.4, total - 4.1))


class B07_TwoEnvironments(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B07", 18.60)
        title = Text("Culture medium  vs  blood — two different worlds",
                     font=SERIF, font_size=24, color=INK).move_to(UP * 3.2)
        divider = DashedLine(UP * 2.6, DOWN * 3.0, color=GOLD, stroke_width=3,
                             dash_length=0.15)
        # LEFT — culture medium
        lbl_L = Text("IN CULTURE MEDIUM", font=DISPLAY, font_size=16, color=INK,
                     weight=BOLD).move_to(LEFT * 3.5 + UP * 2.2)
        p_L = Circle(radius=0.6, fill_color=TEAL, fill_opacity=0.85,
                     stroke_color=INK, stroke_width=1.5).move_to(LEFT * 4.2)
        lig_L = _ligands([-4.2, 0, 0], 0.6, 0.85, 10, TEAL, sw=3)
        # Receptor on the right side of the left panel
        rec_L = Rectangle(width=0.22, height=0.35, fill_color=INK,
                          fill_opacity=0.85, stroke_width=0).move_to(LEFT * 2.0)
        bond_L = Line(LEFT * 3.5, LEFT * 2.15, color=TEAL, stroke_width=3)
        lbl_bind_L = Text("binds", font=DISPLAY, font_size=17, color=TEAL,
                          weight=BOLD).move_to(LEFT * 3.2 + DOWN * 1.8)
        # RIGHT — blood
        lbl_R = Text("IN BLOOD", font=DISPLAY, font_size=16, color=INK,
                     weight=BOLD).move_to(RIGHT * 3.5 + UP * 2.2)
        p_R = Circle(radius=0.6, fill_color=TEAL, fill_opacity=0.85,
                     stroke_color=INK, stroke_width=1.5).move_to(RIGHT * 3.5)
        cor_R = Circle(radius=0.95, fill_color=CRIMSON, fill_opacity=0.7,
                       stroke_color=INK, stroke_width=1.5).move_to(RIGHT * 3.5)
        arrow_R = Arrow(RIGHT * 4.4, RIGHT * 5.6, color=CRIMSON, stroke_width=3, buff=0.05)
        lbl_liver = Text("→ liver", font=DISPLAY, font_size=17, color=CRIMSON,
                         weight=BOLD).move_to(RIGHT * 5.5 + DOWN * 0.4)
        lbl_bur_R = Text("ligand buried", font=DISPLAY, font_size=17, color=CRIMSON,
                         weight=BOLD).move_to(RIGHT * 3.5 + DOWN * 1.8)
        self.play(FadeIn(title), Create(divider), run_time=0.6)
        self.play(FadeIn(lbl_L), FadeIn(lbl_R), run_time=0.4)
        self.play(GrowFromCenter(p_L), GrowFromCenter(p_R), run_time=0.6)
        self.play(Create(lig_L), run_time=0.5)
        self.play(FadeIn(rec_L), Create(bond_L), FadeIn(lbl_bind_L), run_time=0.7)
        self.play(GrowFromCenter(cor_R), run_time=0.8)
        self.play(GrowArrow(arrow_R), FadeIn(lbl_liver), FadeIn(lbl_bur_R), run_time=0.7)
        self.wait(max(0.4, total - 4.3))


class B09_FolateExample(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B09", 22.19)
        title = Text("Folate-targeted particle — culture vs blood",
                     font=SERIF, font_size=24, color=INK).move_to(UP * 3.2)
        subtitle = Text("illustrative numbers", font=DISPLAY, font_size=14,
                        color=INK, slant=ITALIC).move_to(UP * 2.6)
        # Left column: CULTURE — one bar
        col_L_lbl = Text("IN CULTURE", font=DISPLAY, font_size=16, color=INK,
                         weight=BOLD).move_to(LEFT * 3.8 + UP * 1.8)
        bar_L = Rectangle(width=0.9, height=3.0, fill_color=TEAL,
                          fill_opacity=0.85, stroke_color=INK, stroke_width=1)
        bar_L.move_to(LEFT * 3.8 + DOWN * 0.5)
        pct_L = Text("87%", font=DISPLAY, font_size=32, color=TEAL,
                     weight=BOLD).next_to(bar_L, UP, buff=0.15)
        cap_L = Text("binding on cancer cells", font=DISPLAY, font_size=13,
                     color=INK).next_to(bar_L, DOWN, buff=0.25)
        # Right column: BLOOD — two bars (liver 72%, tumor 3%)
        col_R_lbl = Text("IN BLOOD (mouse)", font=DISPLAY, font_size=16, color=INK,
                         weight=BOLD).move_to(RIGHT * 2.5 + UP * 1.8)
        bar_liv = Rectangle(width=0.9, height=2.5, fill_color=CRIMSON,
                            fill_opacity=0.85, stroke_color=INK, stroke_width=1)
        bar_liv.move_to(RIGHT * 1.5 + DOWN * 0.75)
        pct_liv = Text("72%", font=DISPLAY, font_size=28, color=CRIMSON,
                       weight=BOLD).next_to(bar_liv, UP, buff=0.15)
        cap_liv = Text("liver at 4h", font=DISPLAY, font_size=13,
                       color=INK).next_to(bar_liv, DOWN, buff=0.25)
        bar_tum = Rectangle(width=0.9, height=0.10, fill_color=TEAL,
                            fill_opacity=0.85, stroke_color=INK, stroke_width=1)
        bar_tum.move_to(RIGHT * 3.5 + DOWN * 1.95)
        pct_tum = Text("3%", font=DISPLAY, font_size=28, color=TEAL,
                       weight=BOLD).next_to(bar_tum, UP, buff=0.15)
        cap_tum = Text("tumor", font=DISPLAY, font_size=13,
                       color=INK).next_to(bar_tum, DOWN, buff=0.25)
        footer = Text("ligands intact — corona is in the way",
                      font=SERIF, font_size=18, color=CRIMSON,
                      slant=ITALIC).move_to(DOWN * 3.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.5)
        self.play(FadeIn(col_L_lbl), FadeIn(col_R_lbl), run_time=0.5)
        self.play(GrowFromEdge(bar_L, DOWN), run_time=0.9)
        self.play(FadeIn(pct_L), FadeIn(cap_L), run_time=0.4)
        self.play(GrowFromEdge(bar_liv, DOWN), run_time=0.9)
        self.play(FadeIn(pct_liv), FadeIn(cap_liv), run_time=0.4)
        self.play(GrowFromEdge(bar_tum, DOWN), run_time=0.6)
        self.play(FadeIn(pct_tum), FadeIn(cap_tum), run_time=0.4)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(max(0.5, total - 5.5))


class B10_CoronaSummary(Scene):
    def construct(self):
        _bg(self)
        total = DUR.get("B10", 16.51)
        title = Text("The body sees the corona, not your particle",
                     font=SERIF, font_size=24, color=INK).move_to(UP * 3.2)
        # Fully-coated particle
        core = Circle(radius=0.7, fill_color=TEAL, fill_opacity=0.85,
                      stroke_color=INK, stroke_width=1.5).move_to(ORIGIN)
        lig = _ligands([0, 0, 0], 0.70, 0.95, 12, TEAL, sw=2.5)
        corona = Circle(radius=1.15, fill_color=CRIMSON, fill_opacity=0.65,
                        stroke_color=INK, stroke_width=1.5).move_to(ORIGIN)
        # Editor's-pen ring around corona (gold)
        ring = Circle(radius=1.32, fill_opacity=0, stroke_color=GOLD,
                      stroke_width=6).move_to(ORIGIN)
        # Two annotations
        lbl_lig = Text("targeting ligands  —  buried", font=DISPLAY,
                       font_size=17, color=TEAL,
                       weight=BOLD).move_to(LEFT * 3.8 + UP * 0.5)
        arr_lig = Arrow(lbl_lig.get_right() + RIGHT * 0.1,
                        core.get_left() + LEFT * 0.05,
                        color=TEAL, stroke_width=2, buff=0.05,
                        max_tip_length_to_length_ratio=0.15)
        lbl_cor = Text("protein corona  —  seconds", font=DISPLAY,
                       font_size=17, color=CRIMSON,
                       weight=BOLD).move_to(RIGHT * 3.8 + DOWN * 0.5)
        arr_cor = Arrow(lbl_cor.get_left() + LEFT * 0.1,
                        corona.get_right() + RIGHT * 0.05,
                        color=CRIMSON, stroke_width=2, buff=0.05,
                        max_tip_length_to_length_ratio=0.15)
        footer = Text("months of engineering  ·  undone in seconds",
                      font=SERIF, font_size=20, color=INK,
                      slant=ITALIC).move_to(DOWN * 2.9)
        self.play(FadeIn(title), run_time=0.5)
        self.play(GrowFromCenter(core), Create(lig), run_time=0.7)
        self.play(GrowFromCenter(corona), run_time=0.8)
        self.play(FadeIn(lbl_lig), GrowArrow(arr_lig), run_time=0.6)
        self.play(FadeIn(lbl_cor), GrowArrow(arr_cor), run_time=0.6)
        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(footer), run_time=0.6)
        self.wait(max(0.4, total - 4.6))


SCENES = [
    ("B04_CoronaForms",       "B04"),
    ("B05_LigandMasked",      "B05"),
    ("B06_OpsominClearance",  "B06"),
    ("B07_TwoEnvironments",   "B07"),
    ("B09_FolateExample",     "B09"),
    ("B10_CoronaSummary",     "B10"),
]

if __name__ == "__main__":
    import shutil
    reel = pathlib.Path(__file__).resolve().parent
    manim_dir = reel / "manim"
    manim_dir.mkdir(exist_ok=True)
    failed = []
    for scene_cls, bid in SCENES:
        print(f"[render] {scene_cls} -> manim/{bid}.mp4", flush=True)
        r = subprocess.run(
            [sys.executable, "-m", "manim", "-qh", "--fps", "24",
             "-r", "1920,1080", str(reel / "scenes_std.py"), scene_cls],
            cwd=str(reel), capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"  FAIL: {r.stderr[-500:]}")
            failed.append(scene_cls); continue
        src = reel / "media" / "videos" / "scenes_std" / "1080p24" / f"{scene_cls}.mp4"
        dst = manim_dir / f"{bid}.mp4"
        if src.exists():
            shutil.copy2(src, dst)
            print(f"  OK -> {dst}")
        else:
            print(f"  ERROR: {src} not found")
            failed.append(scene_cls)
    if failed:
        print(f"\nFailed: {failed}"); sys.exit(1)
    print(f"\nAll {len(SCENES)} scenes rendered")
