# -*- coding: utf-8 -*-
# Auto-built Manim scenes for the 20 cancer-biology plates.
# Each class Plate01..Plate20 animates the SAME geometry the SVG plate uses.
#   Render one:  manim -ql manim_plates.py Plate06
#   Render all:  for i in 01..20: manim -ql manim_plates.py Plate$i
from manim import Scene, config
from plates_gen import PLATES, make_construct

config.background_color = "#FFFFFF"

for _num, _slug, _fn in PLATES:
    _W, _H, _recs = _fn()
    globals()[f"Plate{_num}"] = type(f"Plate{_num}", (Scene,), {"construct": make_construct(_recs, _W, _H)})
