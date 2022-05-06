from multiprocessing.sharedctypes import Value
from manim import *

class PolarConic(Scene):
    def construct(self):
        e = ValueTracker(2.0)
        d = ValueTracker(-1.0)

        plane = PolarPlane(radius_max=3).add_coordinates()
        
        focus = Dot(point=plane.get_origin(), radius=0.1, color=GREEN)
        f_label = always_redraw(lambda : MathTex(r"F", ).set_color(GREEN).next_to(focus,DOWN+LEFT,buff=0.))
        
        directrix = always_redraw(
            lambda : plane.plot_line_graph(
                [d.get_value(), d.get_value()],
                [np.sqrt(9.0-d.get_value()**2), -np.sqrt(9.0-d.get_value()**2)],
                line_color=RED,
                add_vertex_dots=False
            )
        )

        d_center = always_redraw(lambda : Dot(directrix.get_center(), radius=0.01,color=RED))
        #d_dist = always_redraw(lambda : BraceBetweenPoints(plane.get_origin(), [d.get_value(),0,0],color=RED) if d.get_value() >= 0 else BraceBetweenPoints([d.get_value(),0,0],plane.get_origin(),color=RED))
        d_label = always_redraw(lambda : MathTex(r"D",).set_color(RED).next_to(d_center,LEFT+DOWN,buff=0.1))
        
        pt = ValueTracker(2*PI/3)

        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1-e.get_value()*np.cos(t))
        
        p = always_redraw(lambda : Dot(plane.pr2pt(r(pt.get_value()),pt.get_value()), color=ORANGE))
        p_label = always_redraw(lambda : MathTex(r"P", ).set_color(YELLOW).next_to(p, UP + RIGHT,buff=0.))
        self.play(LaggedStart(
            Create(plane),
            Create(focus),
            Create(f_label),
            Create(directrix),
            Create(d_center),
            Create(d_label),
            lag_ratio=0.5
            )
        )

        fp_line = always_redraw(lambda : Line(p,focus))
        fp_brace = always_redraw(lambda : BraceBetweenPoints(fp_line.get_end(), fp_line.get_start()))
        
        dp_line = always_redraw(lambda : Line(directrix.get_center()+[0,r(pt.get_value())*np.sin(pt.get_value()),0],p))
        dp_brace = always_redraw(lambda : BraceBetweenPoints(dp_line.get_end(), dp_line.get_start()))
        
        self.wait(1)

        self.play(d.animate.set_value(0), d.animate.set_value(1))
        self.play(d.animate.set_value(-0.01), d.animate.set_value(-1))
        self.wait(1)

        self.play(LaggedStart(
            Create(p),
            Create(p_label),
            lag_ratio=0.5
        ))

        self.play(
            #FadeOut(p_label),
            FadeOut(f_label),
            FadeOut(d_label),
            Create(fp_line),
            Create(dp_line),
            #Create(fp_brace),
            #Create(dp_brace),
        )
        self.wait(0.5)

        self.play(pt.animate.set_value(np.arccos(1/e.get_value()+d.get_value()/3)))
        
        plot1_t = ValueTracker(np.arccos(1/e.get_value()+d.get_value()/3))
        plot1 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[np.arccos(1/e.get_value()+d.get_value()/3),plot1_t.get_value()],
                color = YELLOW
            )
        )

        plot2_t = ValueTracker(-np.arccos(1/e.get_value()-d.get_value()/3))
        plot2 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[-np.arccos(1/e.get_value()-d.get_value()/3),plot2_t.get_value()],
                color = YELLOW
            )
        )

        self.add(plot1,plot2)
        self.play(
            plot1_t.animate.set_value(2*PI-np.arccos(1/e.get_value()+d.get_value()/3)),
            plot2_t.animate.set_value(np.arccos(1/e.get_value()-d.get_value()/3)),
            pt.animate.set_value(2*PI-np.arccos(1/e.get_value()+d.get_value()/3))
        )

        self.wait(1)
        