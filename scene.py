from multiprocessing.sharedctypes import Value
from manim import *

class PolarConic(Scene):
    def construct(self):
        e = ValueTracker(2.0)
        d = ValueTracker(-1.0)

        plane = PolarPlane(radius_max=3).add_coordinates()
        focus = Dot(point=plane.get_origin(), radius=0.1, color=RED)
        directrix = always_redraw(
            lambda : plane.plot_line_graph(
                [d.get_value(), d.get_value()],
                [np.sqrt(9.0-d.get_value()**2), -np.sqrt(9.0-d.get_value()**2)],
                line_color=RED,
                add_vertex_dots=False
            )
        )

        d_dist = always_redraw(lambda : BraceBetweenPoints(plane.get_origin(), [d.get_value(),0,0],color=RED) if d.get_value() >= 0 else BraceBetweenPoints([d.get_value(),0,0],plane.get_origin(),color=RED))
        d_label = always_redraw(lambda : MathTex(r"d",).set_color(RED).next_to(d_dist,DOWN,buff=0.2))
        
        pt = ValueTracker(2*PI/3)

        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1-e.get_value()*np.cos(t))
        
        p = always_redraw(lambda : Dot(plane.pr2pt(r(pt.get_value()),pt.get_value()), color=GREEN))
        
        self.play(LaggedStart(
            Create(plane),
            Create(focus),
            Create(directrix),
            Create(d_dist),
            Create(d_label),
            lag_ratio=0.5
            )
        )
        
        self.wait(1)

        self.play(d.animate.set_value(0), d.animate.set_value(1))
        self.play(d.animate.set_value(-0.01), d.animate.set_value(-1))
        self.wait(1)

        self.play(Create(p))
        