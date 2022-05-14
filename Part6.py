from manim import *

class Part6(Scene):
    def construct(self):
        defn = MarkupText(
            "A hyperbola is an open plane curve generated\n"
            "by a set of points in which each of it is the\n"
            "difference of the distances from two fixed\n"
            "points is a constant.",
            justify=True,
        ).scale(0.7)

        self.play(Write(defn), run_time=3)
        self.wait(2)
        self.play(Unwrite(defn))
        self.wait()
        
        plane = PolarPlane().shift(RIGHT*4)

        f1 = Dot(plane.coords_to_point(0, 0), color=RED)
        f1n = MathTex("G").set_color(RED).next_to(f1, UP + RIGHT)

        f2 = Dot(plane.c2p(-8,0), color=BLUE)
        f2n = MathTex("F").set_color(BLUE).next_to(f2, UP + LEFT)

        pt = ValueTracker(PI-.6)
        p1 = always_redraw(
            lambda : Dot(
                plane.polar_to_point(6/(1-2*np.cos(pt.get_value())), pt.get_value()),
                color = YELLOW
            )
        )
        p1n = always_redraw(
            lambda : MathTex("P").set_color(YELLOW).next_to(p1, UP + RIGHT)
        )
        
        p2 = always_redraw(
            lambda : Dot(
                plane.polar_to_point(6/(1-2*np.cos(pt.get_value()-PI+.4)), pt.get_value()-PI+.4),
                color = YELLOW
            )
        )

        curve = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(6/(1-2*np.cos(t)), t), 
                t_range = [0, 2*PI], 
                color=GREEN, 
                use_smoothing=False, 
                discontinuities = [np.arccos(1/2),2*PI-np.arccos(1/2)], 
                dt = 0.1
            )
        )

        l1 = always_redraw(
            lambda : Line(
                f1,
                p1,
                color = RED
            )
        )
        l2 = always_redraw(
            lambda : Line(
                f2,
                p1,
                color = BLUE
            )
        )

        self.play(
            Create(f1),
            Create(f2),
            Create(f1n),
            Create(f2n),
        )

        self.play(
            Create(curve),
            Create(p1),
            Create(p1n)
        )

        self.play(
            Create(l1),
            Create(l2)
        )


        l1b = always_redraw(
            lambda : BraceLabel(l1, "|\overline{GP}|="+str(np.round(l1.get_arc_length(), decimals=2)))
        )
        l2b = always_redraw(
            lambda : BraceLabel(l2, "|\overline{FP}|="+str(np.round(l2.get_arc_length(), decimals=2))).align_to(l1b, DOWN)
        )

        diff = always_redraw(
            lambda : MathTex(
                "|\overline{FP}-\overline{GP}|=" + str(np.round(np.abs(l1.get_arc_length()-l2.get_arc_length()), decimals=2))
                if np.round(np.abs(l1.get_arc_length()-l2.get_arc_length()), decimals=2) < 3.95 else
                "|\overline{FP}-\overline{GP}|=4.00"
            ).shift(DOWN*3)
        )

        self.play(
            Create(l1b),
            Create(l2b),
            Create(diff)
        )

        self.play(
            pt.animate.set_value(PI+.6),
            run_time=2
        )
        self.wait()

        pt.set_value(-.2)

        self.play(
            p1.animate.move_to(p2),
            run_time=2
        )
        
        self.play(
            pt.animate.set_value(.2),
            run_time=2
        )
        self.wait()

        stdtitle = Text("Standard Form of Hyperbola",).shift(UP*2.5)

        stdform = MathTex(
            "{ {(y-k)^2}\over{a^2} } - { {(x-h)^2}\over{b^2} } = 1 &\\text{ : transverse axis is vertical} \\\\"
            "{ {(x-h)^2}\over{a^2} } - { {(y-k)^2}\over{b^2} } = 1 &\\text{ : transverse axis is horizontal}"
        )

        self.play(
            FadeOut(
                f1, f2, f1n, f2n, p1, p1n, l1, l2, l1b, l2b, curve
            ),
            Write(stdtitle),
            TransformMatchingShapes(diff, stdform)
        )
        self.wait()

        self.play(
            Circumscribe(stdform[0][3]),
            Circumscribe(stdform[0][13]),
            Circumscribe(stdform[0][49]),
            Circumscribe(stdform[0][59]),
        )
        self.wait()