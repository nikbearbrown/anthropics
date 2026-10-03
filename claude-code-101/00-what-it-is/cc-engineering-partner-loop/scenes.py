"""scenes.py — cc-engineering-partner-loop

No reel-local Manim scenes. The film is 100% CC-kit Remotion:
- CCSession (B00–B04, B06)
- CCPlainShell (B05, BSHOW)
- BrutalistHesitantWriter (BIDEA)
- CCDefinitions (BDEFS)
- FlowDiagram (BFLOW)
- CCBoondoggleScore (BCND)
- CCHumanLedger (BHMN)
- ClaudeVerdictArtifact (BVDT)
- ClaudeComposerAsk (BHTF)
- ClaudeTitleOutro (BOUT)

The Scene stub below exists only because the pipeline's static_scene_check.py
looks for a `BearsDoodlesVideo` class in every reel's scenes.py — for
Manim-free reels there is nothing for it to check, so construct() is a no-op.
"""

from manim import Scene


class BearsDoodlesVideo(Scene):
    def construct(self):
        pass
