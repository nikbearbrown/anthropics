"""scenes.py — cc-writing-rules

No reel-local Manim scenes. Every beat renders on the CC kit
(CCSession / CCPlainShell / CCDefinitions / CCBoondoggleScore / CCHumanLedger)
or a shared bookend (BrutalistHesitantWriter / ClaudeVerdictArtifact /
ClaudeComposerAsk / ClaudeTitleOutro). run.sh still expects this file
present with a BearsDoodlesVideo class the static-scene check can import;
the construct is empty on purpose — nothing here composes to a Manim frame.
"""
from manim import Scene


class BearsDoodlesVideo(Scene):
    def construct(self):
        pass
