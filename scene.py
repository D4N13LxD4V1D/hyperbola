from manim import *

class PolarConic(Scene):
    def construct(self):
        e = ValueTracker(0.01)

        plane = PolarPlane(radius_max=5).add_coordinates()

        self.play(LaggedStart(Write(plane)))