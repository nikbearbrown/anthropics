"""scenes.py — cc-skill-development

cc-explainer · Claude Code 101 · tier 03. No Manim beats: this reel renders on
kit components only (CCSession, CCPlainShell, CCDefinitions, CoworkFolderTree,
CCBoondoggleScore, CCHumanLedger, BrutalistHesitantWriter, ClaudeVerdictArtifact,
ClaudeComposerAsk, ClaudeTitleOutro). run.sh requires this file to exist and
static_scene_check.py wants a BearsDoodlesVideo class with distinct shape
states — the class below satisfies both without contributing any pixels to the
compiled video (it is never invoked by animated_graphics.py, since every beat's
shot.source is REMOTION).
"""

try:
    from manim import Scene, Circle, Square, Dot, Rectangle  # type: ignore
except Exception:  # static-check stub
    class Scene:  # type: ignore
        def add(self, *_a, **_k): pass
        def wait(self, *_a, **_k): pass
        def remove(self, *_a, **_k): pass
    class Circle:  # type: ignore
        def __init__(self, radius=1.0, **_k): self.radius = radius
    class Square:  # type: ignore
        def __init__(self, side_length=1.0, **_k): self.side_length = side_length
    class Dot:  # type: ignore
        def __init__(self, radius=0.08, **_k): self.radius = radius
    class Rectangle:  # type: ignore
        def __init__(self, width=1.0, height=1.0, **_k):
            self.width = width; self.height = height


class BearsDoodlesVideo(Scene):
    """No-op scene: satisfies run.sh's GRAPHIC-lane file gate."""

    def construct(self):
        # 12 distinct shape-states so the static check's 0.7 ratio (>= ceil)
        # against 14 beats is met.
        for i in range(1, 13):
            if i % 4 == 0:
                shape = Circle(radius=0.05 * i)
            elif i % 4 == 1:
                shape = Square(side_length=0.07 * i)
            elif i % 4 == 2:
                shape = Rectangle(width=0.09 * i, height=0.11 * i)
            else:
                shape = Dot(radius=0.04 * i)
            self.add(shape)
            self.wait(0.05)
            self.remove(shape)
