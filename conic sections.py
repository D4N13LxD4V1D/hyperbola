from manim import *

class AllConics(Scene):
    def construct(self):
        et = ValueTracker(0.5)
        e = always_redraw(
            lambda : MathTex(
                "e={{r}}:{{D}}=" + str(np.round(et.get_value(), decimals=2)),
            ).shift(RIGHT*3)
            .set_color_by_tex("r", color=GREEN)
            .set_color_by_tex("D", color=RED)
        )

        plane = PolarPlane(radius_max=10).add_coordinates().shift(LEFT*2)
        dt = ValueTracker(-2)
        d = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(dt.get_value()/np.cos(t), t),
                t_range=[-2*PI, 2*PI],
                color=RED
            )
        )
        o = Dot(
            plane.get_origin(),
            color=GREEN
        )
        plot = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(et.get_value()*np.abs(dt.get_value())/(1-et.get_value()*np.cos(t)),t),
                t_range=[0,2*PI],
                use_smoothing=False, 
                discontinuities = [np.arccos(1/et.get_value()),2*PI-np.arccos(1/et.get_value())], 
                dt = 0.1,
                color = YELLOW
            )
        )
        
        pt = ValueTracker(PI/4)
        self.add(pt)
        p = always_redraw(
            lambda : Dot(
                plot.get_point_from_function(pt.get_value()),
                color = YELLOW
            )
        )

        self.play(
            Create(plot)
        )
        self.wait()

        self.play(
            Create(p),
        )
        self.wait()

        self.play(
            LaggedStart(
                Create(d),
                Create(o),
            )
        )
        self.wait()

        r = always_redraw(
            lambda : Line(
                o,
                p,
                color=GREEN
            )
        )

        D = always_redraw(
            lambda : Line(
                p,
                [d.get_x(), p.get_y(),0],
                color=RED
            )
        )

        self.play(
            Create(r),
            Create(D),
        )
        self.wait()

        self.play(
            Write(e)
        )
        self.wait()

        pt.add_updater(lambda m, dt: m.increment_value(np.sin(4*dt)/6))
        self.wait()

        self.play(
            et.animate.set_value(.999)
        )
        self.wait()

        self.play(
            et.animate.set_value(2)
        )
        self.wait()

        self.play(
            FadeOut(p),
            FadeOut(r),
            FadeOut(D),
            FadeOut(d),
            FadeOut(o),
            FadeOut(plot),
            FadeOut(e),
        )
        self.wait()