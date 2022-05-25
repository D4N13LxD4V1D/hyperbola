from manim import *

class PolarConic(Scene):
    def construct(self):
        eq1 = MathTex("e=r:D")
        eq2 = MathTex("e=\\frac{r}{D}")
        eq3 = MathTex("eD=r")
        eq4 = MathTex("r=e","D")

        self.play(Write(eq1))
        # self.wait(1)

        self.play(TransformMatchingShapes(eq1,eq2))
        # self.wait(1)
 
        self.play(TransformMatchingShapes(eq2, eq3))
        # self.wait(1)

        self.play(TransformMatchingShapes(eq3, eq4))
        # self.wait(1)

        plane = PolarPlane(radius_max=3).add_coordinates().shift(LEFT*2)
        
        e_var = Variable(1, "e")
        e = e_var.tracker
        d_var = Variable(-1,"d")
        d = d_var.tracker

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
        #d_dist = always_redraw(
        # lambda : BraceBetweenPoints(plane.get_origin(), [d.get_value(),0,0],color=RED) 
        # if d.get_value() >= 0 
        # else BraceBetweenPoints([d.get_value(),0,0],plane.get_origin(),color=RED))
        d_label = always_redraw(lambda : MathTex(r"D",).set_color(RED).next_to(d_center,LEFT+DOWN,buff=0.1))
        
        pt_var = Variable(PI/3, "\theta")
        pt = pt_var.tracker

        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1-e.get_value()*np.cos(t))
        
        p = always_redraw(lambda : Dot(plane.pr2pt(r(pt.get_value()),pt.get_value()), color=ORANGE))
        p_label = always_redraw(lambda : MathTex(r"P", ).set_color(YELLOW).next_to(p, UP + RIGHT,buff=0.))
        self.play(LaggedStart(
            eq4.animate.shift(RIGHT*3),
            Create(plane),
            Create(focus),
            Create(f_label),
            Create(directrix),
            Create(d_center),
            Create(d_label),
            lag_ratio=0.5
            )
        )
        self.wait(1)

        fp_line = always_redraw(lambda : Line(p,focus))
        fp_brace = always_redraw(lambda : BraceBetweenPoints(fp_line.get_end(), fp_line.get_start()))
        fp_label = always_redraw(lambda : MathTex("r").next_to(fp_brace))
        
        dp_line = always_redraw(lambda : Line(directrix.get_center()+[0,r(pt.get_value())*np.sin(pt.get_value()),0],p))
        dp_brace = always_redraw(lambda : BraceBetweenPoints(dp_line.get_end(), dp_line.get_start()))
        dp_label = always_redraw(lambda : MathTex("D").next_to(dp_brace,UP))

        # self.play(d.animate.set_value(0), d.animate.set_value(1))
        # self.play(d.animate.set_value(-0.01), d.animate.set_value(-1))
        # self.wait(1)

        # self.play(Flash(focus))
        # self.wait(1)

        dp_brace_1 = BraceBetweenPoints(
            plane.get_center()+[0,r(pt.get_value())*np.sin(pt.get_value()),0],
            directrix.get_center()+[0,r(pt.get_value())*np.sin(pt.get_value()),0],
        )
        dp_label_1 = always_redraw(lambda : MathTex("d").next_to(dp_brace_1,UP))
        
        dp_brace_2 = BraceBetweenPoints(
            plane.get_center()+[r(pt.get_value())*np.cos(pt.get_value()), r(pt.get_value())*np.sin(pt.get_value()),0],
            plane.get_center()+[0,r(pt.get_value())*np.sin(pt.get_value()),0],
        )
        dp_label_2 = always_redraw(lambda : MathTex("x").next_to(dp_brace_2,UP))

        dp_brace_low = BraceBetweenPoints(
            directrix.get_center(),
            plane.get_center(),
        )
        dp_label_low = always_redraw(lambda : MathTex("d").next_to(dp_brace_low,DOWN))

        # self.play(
        #     Create(dp_brace_low),
        #     Create(dp_label_low),
        # )
        # self.wait()

        self.play(
            FadeOut(dp_brace_low),
            FadeOut(dp_label_low),
        )
        self.wait()

        self.play(LaggedStart(
            Create(p),
            Create(p_label),
            lag_ratio=0.5
        ))

        self.play(
            Create(fp_line),
            Create(fp_brace),
            Create(fp_label),
        )
        self.wait(0.5)

        self.play(
            Create(dp_line),
            Create(dp_brace),
            Create(dp_label),
        )
        self.wait(0.5)

        eq5 = MathTex("r=e","(d+x)").align_to(eq4,LEFT)

        self.play(
            FadeOut(dp_brace),
            FadeOut(dp_label),
            TransformMatchingShapes(eq4, eq5),
            Create(dp_brace_1),
            Create(dp_label_1),
            Create(dp_brace_2),
            Create(dp_label_2),
        )
        self.wait(0.5)

        eq6 = MathTex("r=e(d+r\\cos\\theta)").align_to(eq5,LEFT)
        dp_label_3 = MathTex("r\\cos\\theta").next_to(dp_brace_2,UP)
        
        self.play(
            TransformMatchingShapes(eq5, eq6),
            TransformMatchingShapes(dp_label_2, dp_label_3),
        )
        self.wait(0.5)

        eq7 = MathTex("r=ed+er\\cos\\theta").align_to(eq6,LEFT)
        eq8 = MathTex("r-er\\cos\\theta=ed").align_to(eq7,LEFT)
        eq9 = MathTex("r(1-e\\cos\\theta)=ed").align_to(eq8,LEFT)
        eq10 = MathTex("r=\\frac{ed}{1-e\\cos\\theta}").align_to(eq9,LEFT)
        eq11 = MathTex("r=\\frac{1}{1-\\cos\\theta}").align_to(eq10,LEFT)

        self.play(TransformMatchingShapes(eq6,eq7))
        # self.wait(1)

        self.play(TransformMatchingShapes(eq7, eq8))
        # self.wait(1)

        self.play(TransformMatchingShapes(eq8, eq9))
        # self.wait(1)

        self.play(TransformMatchingShapes(eq9, eq10))
        # self.wait(1)
        
        # self.play(TransformMatchingShapes(eq10, eq11))
        # self.wait(1)

        d2t = ValueTracker(-1)
        d2 = always_redraw(
            lambda : plane.plot_line_graph(
                [d2t.get_value(), d2t.get_value()],
                [np.sqrt(9.0-d2t.get_value()**2), -np.sqrt(9.0-d2t.get_value()**2)],
                line_color=RED,
                add_vertex_dots=False
            )
        )

        self.play(
            Create(d2),
            FadeOut(p_label),
            FadeOut(f_label),
            FadeOut(d_label),
            FadeOut(fp_line),
            FadeOut(fp_brace),
            FadeOut(fp_label),
            FadeOut(dp_line),
            FadeOut(dp_brace_1),
            FadeOut(dp_label_1),
            FadeOut(dp_brace_2),
            FadeOut(dp_label_3),
        )

        self.play(pt.animate.set_value(np.arccos(1/e.get_value()+d.get_value()/3)))
        
        plot1_t = ValueTracker(np.arccos(1/e.get_value()+d.get_value()/3))
        plot1 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[np.arccos(1/e.get_value()+d.get_value()/3),plot1_t.get_value()],
                color = YELLOW
            )
        )

        # plot2_t = ValueTracker(-np.arccos(1/e.get_value()-d.get_value()/3))
        # plot2 = always_redraw(
        #    lambda : ParametricFunction(
        #        lambda t : plane.polar_to_point(r(t),t),
        #        t_range=[plot2_t.get_value(),-np.arccos(1/e.get_value()-d.get_value()/3)],
        #        color = YELLOW
        #    )
        # )

        self.add(
            plot1,
            # plot2
        )

        self.play(
            FadeOut(directrix),
            plot1_t.animate.set_value(2*PI-np.arccos(1/e.get_value()+d.get_value()/3)),
            # plot2_t.animate.set_value(np.arccos(1/e.get_value()-d.get_value()/3)),
            pt.animate.set_value(2*PI-np.arccos(1/e.get_value()+d.get_value()/3))
        )

        self.wait(1)

        self.play(
            FadeOut(p)
        )
        self.wait()

        eq12 = MathTex("r=\\frac{ed}{1+e\\cos\\theta}").align_to(eq10,LEFT)
        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1+e.get_value()*np.cos(t))
        plot3 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[-np.arccos(-2/3),np.arccos(-2/3)],
                color = YELLOW
            )
        )
        self.play(
            TransformMatchingShapes(eq10, eq12),
            ReplacementTransform(plot1,plot3, path_arc=PI),
            d2t.animate.set_value(1)
        )
        self.wait()

        eq13 = MathTex("r=\\frac{ed}{1+e\\sin\\theta}").align_to(eq12,LEFT)
        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1+e.get_value()*np.sin(t))
        plot4 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[np.arcsin(-2/3),PI-np.arcsin(-2/3)],
                color = YELLOW
            )
        )
        d3t = ValueTracker(1)
        d3 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(d3t.get_value()/np.sin(t),t),
                t_range=[np.arcsin(np.abs(d3t.get_value())/3),PI-np.arcsin(np.abs(d3t.get_value())/3)],
                color = RED
            )
        )
        self.play(
            TransformMatchingShapes(eq12, eq13),
            ReplacementTransform(plot3,plot4, path_arc=PI),
            ReplacementTransform(d2,d3, path_arc=PI),
        )
        self.wait()

        eq14 = MathTex("r=\\frac{ed}{1-e\\sin\\theta}").align_to(eq13,LEFT)
        def r(t):
            return e.get_value()*np.abs(d.get_value())/(1-e.get_value()*np.sin(t))
        plot5 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(r(t),t),
                t_range=[-PI-np.arcsin(2/3),np.arcsin(2/3)],
                color = YELLOW
            )
        )
        self.play(
            TransformMatchingShapes(eq13,eq14),
            ReplacementTransform(plot4,plot5, path_arc=PI),
            d3t.animate.set_value(-1)
        )
        self.wait()
