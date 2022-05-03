from manim import *

class PolarConic(Scene):
    def construct(self):
        formulae = MathTex(r"r=ed", font_size=96)
        self.add(formulae)