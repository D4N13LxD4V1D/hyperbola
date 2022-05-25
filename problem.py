from manim import *

class Problem(Scene):
    def construct(self):
        self.next_section("problem1", skip_animations=True)
        problem = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item a polar equation of the hyperbola"
            "\\item the vertices"
            "\\item the center"
            "\\item an equation of the directrix corresponding to\\\\"
            "the focus at the pole"
            "\\item sketch the hyperbola."
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7)

        self.play(
            Write(problem)
        )
        self.wait()

        problem1 = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item a polar equation of the hyperbola"
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7).align_to(problem, UP)

        self.play(
            TransformMatchingShapes(problem, problem1,path_arc=PI/2)
        )
        self.wait()

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.scale(.5).shift(DOWN*1.75+LEFT*2)
        f = always_redraw(
            lambda : Dot(
                plane.get_origin(),
                color=GREEN
            )
        )
        dt = ValueTracker(-2)
        d = always_redraw(
            lambda : ParametricFunction(
                lambda t: plane.polar_to_point(dt.get_value()/np.cos(t),t),
                t_range = [np.arccos(dt.get_value()/3),2*PI-np.arccos(dt.get_value()/3)],
                color=RED
            )
        )
        self.play(
            Create(plane),
            Create(f),
            Create(d)
        )
        self.wait()

        self.play(
            Flash(f),
            dt.animate.set_value(-.5)
        )
        self.wait()
        
        self.play(
            dt.animate.set_value(-2)
        )

        # self.next_section("sdas", skip_animations=False)

        eq1 = MathTex("r=\\frac{ed}{1-e\cos\\theta}").next_to(plane,RIGHT,buff=0.5)
        self.play(
            Write(eq1)
        )
        self.wait()


        eq2a = MathTex("r=\\frac{2d}{1-2\\cos\\theta}").next_to(eq1).align_to(eq1, LEFT)
        self.play(
            TransformMatchingShapes(eq1, eq2a, path_arc=PI/2)
        )
        self.wait()


        p = always_redraw(
            lambda : Dot(
                plane.polar_to_point(1,2*PI/3),
                color=YELLOW
            )
        )

        self.play(
            Create(p)
        )
        self.wait()

        eq2 = MathTex("1=\\frac{2d}{1-2\\cos(\\frac{2\\pi}{3})}").next_to(eq2a).align_to(eq2a, LEFT)
        self.play(
            Flash(p),
            TransformMatchingShapes(eq2a, eq2, path_arc=PI/2)
        )
        self.wait()

        # self.next_section("sdas", skip_animations=True)

        eq3 = MathTex("1=\\frac{2d}{1-2(-\\frac{1}{2})}").next_to(eq2).align_to(eq2, LEFT)
        self.play(
            TransformMatchingShapes(eq2, eq3, path_arc=PI/2)
        )
        self.wait()

        eq4 = MathTex("1=\\frac{2d}{1-(-1)}").next_to(eq3).align_to(eq3, LEFT)
        self.play(
            TransformMatchingShapes(eq3, eq4, path_arc=PI/2)
        )
        self.wait()

        eq5 = MathTex("1=\\frac{2d}{2}").next_to(eq4).align_to(eq4, LEFT)
        self.play(
            TransformMatchingShapes(eq4, eq5, path_arc=PI/2)
        )
        self.wait()

        eq6 = MathTex("1=d").next_to(eq5).align_to(eq5, LEFT)
        self.play(
            TransformMatchingShapes(eq5, eq6, path_arc=PI/2)
        )
        self.wait()

        eq7 = MathTex("d=1").next_to(eq6).align_to(eq6, LEFT)
        self.play(
            dt.animate.set_value(-1),
            TransformMatchingShapes(eq6, eq7, path_arc=PI/2)
        )
        self.wait()

        eq1.next_to(eq7,UP,buff=0.2).align_to(eq7, LEFT)
        self.play(
            Write(eq1)
        )
        self.wait()

        eq2 = MathTex("r=\\frac{2d}{1-2\\cos\\theta}").next_to(eq1).align_to(eq1, LEFT)
        self.play(
            TransformMatchingShapes(eq1, eq2, path_arc=PI/2)
        )
        self.wait()

        eq8 = MathTex("r=\\frac{2(1)}{1-2\\cos(\\theta)}").next_to(eq2).align_to(eq2, LEFT)
        self.play(
            Wiggle(d),
            TransformMatchingShapes(eq2, eq8, path_arc=PI/2)
        )
        self.wait()
        
        eq8b = MathTex("r=\\frac{2}{1-2\\cos(\\theta)}").next_to(eq8).align_to(eq8, LEFT)
        self.play(
            TransformMatchingShapes(eq8, eq8b, path_arc=PI/2)
        )
        
        self.play(
            TransformMatchingShapes(eq7, eq8b, path_arc=PI/2)
        )
        self.wait()

        self.play(
            eq8b.animate.next_to(plane,RIGHT,buff=0.5)
        )
        self.wait()

        eq9 = MathTex("r=\\frac{2}{1-2\\cos(\\theta)\\neq0}").next_to(eq8b).align_to(eq8b, LEFT)
        self.play(
            TransformMatchingShapes(eq8b, eq9, path_arc=PI/2)
        )
        self.wait()

        eq10 = MathTex("1-2\\cos(\\theta)\\neq0").next_to(eq9).align_to(eq9, LEFT)
        self.play(
            TransformMatchingShapes(eq9, eq10, path_arc=PI/2)
        )
        self.wait()

        eq11 = MathTex("-2\\cos(\\theta)\\neq-1").next_to(eq10).align_to(eq10, LEFT)
        self.play(
            TransformMatchingShapes(eq10, eq11, path_arc=PI/2)
        )
        self.wait()

        eq12 = MathTex("\\cos(\\theta)\\neq\\frac{-1}{-2}").next_to(eq11).align_to(eq11, LEFT)
        self.play(
            TransformMatchingShapes(eq11, eq12, path_arc=PI/2)
        )
        self.wait()
        
        eq13 = MathTex("\\cos(\\theta)\\neq\\frac{1}{2}").next_to(eq12).align_to(eq12, LEFT)
        self.play(
            TransformMatchingShapes(eq12, eq13, path_arc=PI/2)
        )
        self.wait()
        
        eq14 = MathTex("\\theta\\neq\\cos^{-1}\\left(\\frac{1}{2}\\right)").next_to(eq13).align_to(eq13, LEFT)
        self.play(
            TransformMatchingShapes(eq13, eq14, path_arc=PI/2)
        )
        self.wait()
        
        eq15 = MathTex("\\theta\\neq\\left\\{\\frac{\\pi}{3},\\ \\frac{5\pi}{3}\\right\\}").next_to(eq14).align_to(eq14, LEFT)
        self.play(
            TransformMatchingShapes(eq14, eq15, path_arc=PI/2)
        )
        self.wait()

        eq16 = MathTex("r=\\frac{2}{1-2\\cos(\\theta)}\\text{, where } \\theta\\neq\\left\\{\\frac{\\pi}{3},\\ \\frac{5\pi}{3}\\right\\}").next_to(plane).align_to(plane, LEFT)
        self.play(
            FadeOut(plane),
            FadeOut(p),
            FadeOut(d),
            FadeOut(f),
            TransformMatchingShapes(eq15, eq16, path_arc=PI/2)
        )
        self.wait()

        h = ValueTracker(0)
        a1 = always_redraw(
            lambda : plane.plot(
                lambda x : np.tan(PI/3)*(x-h.get_value()),
                x_range=[
                    (6*h.get_value()-np.sqrt(-12*h.get_value()*h.get_value()+576))/8,
                    (6*h.get_value()+np.sqrt(-12*h.get_value()*h.get_value()+576))/8
                ]
            ).scale_to_fit_height(plane.height-1)
        )
        a2 = always_redraw(
            lambda : plane.plot(
                lambda x : np.tan(5*PI/3)*(x-h.get_value()),
                x_range=[
                    (6*h.get_value()-np.sqrt(-12*h.get_value()*h.get_value()+576))/8,
                    (6*h.get_value()+np.sqrt(-12*h.get_value()*h.get_value()+576))/8
                ]
            ).scale_to_fit_height(plane.height-1)
        )
        eq17 = MathTex("r=\\frac{2}{1-2\\cos(\\theta)}").next_to(plane,RIGHT,buff=0.5)
        self.play(
            Create(plane),
            Create(p),
            Create(d),
            Create(f),
            Create(a1),
            Create(a2),
            TransformMatchingShapes(eq16, eq17, path_arc=PI/2)
        )
        self.wait()
        
        self.play(h.animate.set_value(-1))
        self.wait()
        self.play(h.animate.set_value(1))
        self.wait()
        self.play(h.animate.set_value(0))
        self.wait()
        self.play(FadeOut(a1),FadeOut(a2))
        self.wait()

        self.next_section("problem2", skip_animations=True)
        problem2 = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item[2.] the vertices"
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7).align_to(problem, UP)

        self.play(
            TransformMatchingShapes(problem1, problem2, path_arc=PI/2)
        )
        self.wait()

        v1_eq1 = MathTex("r=\\frac{2}{1-2\\cos(\\theta)}").next_to(plane,RIGHT,buff=0.5).shift(UP)
        v2_eq1 = MathTex("r=\\frac{2}{1-2\\cos(\\theta)}").next_to(plane,RIGHT,buff=0.5).shift(DOWN)

        self.play(
            TransformMatchingShapes(eq17, v1_eq1),
            Write(v2_eq1)
        )
        self.wait()

        v1_eq2 = MathTex("r=\\frac{2}{1-2\\cos(0)}").next_to(v1_eq1).align_to(v1_eq1, LEFT)
        v2_eq2 = MathTex("r=\\frac{2}{1-2\\cos(\\pi)}").next_to(v2_eq1).align_to(v2_eq1, LEFT)
        self.play(
            TransformMatchingShapes(v1_eq1, v1_eq2),
            TransformMatchingShapes(v2_eq1, v2_eq2),
        )
        self.wait()

        v1_eq3 = MathTex("r=\\frac{2}{1-2(1)}").next_to(v1_eq2).align_to(v1_eq2, LEFT)
        v2_eq3 = MathTex("r=\\frac{2}{1-2(-1)}").next_to(v2_eq2).align_to(v2_eq2, LEFT)
        self.play(
            TransformMatchingShapes(v1_eq2, v1_eq3),
            TransformMatchingShapes(v2_eq2, v2_eq3),
        )
        self.wait()

        v1_eq4 = MathTex("r=\\frac{2}{1-2}").next_to(v1_eq3).align_to(v1_eq3, LEFT)
        v2_eq4 = MathTex("r=\\frac{2}{1+2}").next_to(v2_eq3).align_to(v2_eq3, LEFT)
        self.play(
            TransformMatchingShapes(v1_eq3, v1_eq4),
            TransformMatchingShapes(v2_eq3, v2_eq4),
        )
        self.wait()

        v1_eq5 = MathTex("r=\\frac{2}{-1}").next_to(v1_eq4).align_to(v1_eq4, LEFT)
        v2_eq5 = MathTex("r=\\frac{2}{3}").next_to(v2_eq4).align_to(v2_eq4, LEFT)
        self.play(
            TransformMatchingShapes(v1_eq4, v1_eq5),
            TransformMatchingShapes(v2_eq4, v2_eq5),
        )
        self.wait()

        v1_eq6 = MathTex("r=-2").next_to(v1_eq5).align_to(v1_eq5, LEFT)
        v2_eq6 = MathTex("r=\\frac{2}{3}").next_to(v2_eq5).align_to(v2_eq5, LEFT)
        self.play(
            TransformMatchingShapes(v1_eq5, v1_eq6),
            TransformMatchingShapes(v2_eq5, v2_eq6),
        )
        self.wait()

        vertices = MathTex("\\text{Vertices: } (-2,\\ 0),\\ \\left(\\frac{2}{3},\\ \\pi\\right)").scale(.7).next_to(plane,RIGHT,buff=0.5)
        v1 = always_redraw(
            lambda : Dot (
                plane.polar_to_point(-2, 0),
                color=YELLOW
            )
        )
        v2 = always_redraw(
            lambda : Dot(
                plane.polar_to_point(2/3, PI),
                color=YELLOW
            )
        ) 
        self.play(
            Unwrite(v1_eq6),
            Unwrite(v2_eq6),
            Write(vertices),
            Create(v1),
            Create(v2)
        )
        self.wait()

        self.next_section("problem3", skip_animations=True)
        problem3 = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item[3.] the center"
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7).align_to(problem, UP)

        self.play(
            TransformMatchingShapes(problem2, problem3, path_arc=PI/2)
        )
        self.wait()

        self.play(
            vertices.animate.shift(UP),
            plane.animate.shift(LEFT*2)
        )
        self.wait()

        center1 = MathTex("\\text{Center: } \\left(\\frac{x_1+x_2}{2},\\ \\frac{y_1+y_2}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            Write(center1)
        )
        self.wait()

        center2 = MathTex("\\text{Center: } \\left(\\frac{r_1\\cos\\theta_1+r_2\\cos\\theta_2}{2},\\ \\frac{r_1\\sin\\theta_1+r_2\\sin\\theta_2}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center1, center2)
        )
        self.wait()

        center3 = MathTex("\\text{Center: } \\left(\\frac{(-2)\\cos(0)+\\left(\\frac{2}{3}\\right)\\cos(\\pi)}{2},\\ \\frac{(-1)\\sin(0)+\\left(\\frac{2}{3}\\right)\\sin(\\pi)}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center2, center3)
        )
        self.wait()

        center4 = MathTex("\\text{Center: } \\left(\\frac{(-2)(1)+\\left(\\frac{2}{3}\\right)(-1)}{2},\\ \\frac{(-1)(0)+\\left(\\frac{2}{3}\\right)(0)}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center3, center4)
        )
        self.wait()

        center5 = MathTex("\\text{Center: } \\left(\\frac{-2-\\left(\\frac{2}{3}\\right)}{2},\\ \\frac{0+0}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center4, center5)
        )
        self.wait()

        center6 = MathTex("\\text{Center: } \\left(\\frac{-\\left(\\frac{8}{3}\\right)}{2},\\ \\frac{0}{2}\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center5, center6)
        )
        self.wait()

        center7 = MathTex("\\text{Center: } \\left(-\\frac{4}{3},\\ 0\\right)").scale(.7).next_to(vertices,DOWN,buff=0.5)
        self.play(
            TransformMatchingShapes(center6, center7)
        )
        self.wait()

        c = always_redraw(
            lambda : Dot(
                plane.polar_to_point(-4/3, 0),
                color=BLUE
            )
        )
        self.play(
            Create(c),
        )
        self.wait()

        self.play(
            plane.animate.shift(RIGHT*2)
        )
        self.wait()

        self.next_section("problem4", skip_animations=True)
        problem4 = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item[4.] an equation of the directrix corresponding to\\\\"
            "the focus at the pole"
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7).align_to(problem, UP).shift(UP*0.5)

        self.play(
            Unwrite(vertices),
            Unwrite(center7),
            TransformMatchingShapes(problem3, problem4, path_arc=PI/2)
        )
        self.wait()

        self.play(
            Flash(f)
        )
        self.wait()

        self.play(
            Wiggle(d)
        )
        self.wait()

        d1 = MathTex("\\text{Directrix: } x=-1").next_to(plane,RIGHT,buff=0.5).scale(.7)
        self.play(
            Write(d1)
        )
        self.wait()

        d2 = MathTex("\\text{Directrix: } r\\cos\\theta=-1").next_to(plane,RIGHT,buff=0.5).scale(.7)
        self.play(
            TransformMatchingShapes(d1, d2)
        )
        self.wait()

        d3 = MathTex("\\text{Directrix: } r=-\\frac{1}{\\cos\\theta}").next_to(plane,RIGHT,buff=0.5).scale(.7)
        self.play(
            TransformMatchingShapes(d2, d3)
        )
        self.wait()

        self.next_section("problem5", skip_animations=False)
        problem5 = MathTex(
            "\\end{align*} The polar axis and its extension are along the\\\\"
            "principal axis of a hyperbola having a focus\\\\"
            "at the pole. The corresponding directrix is to\\\\"
            "the left of the focus. If the hyperbola contains\\\\"
            "the points $(1,\\ 2\\pi/3)$, $e=2$, find\\begin{enumerate}"
            "\\item[5. ] sketch the hyperbola."
            "\\end{enumerate}"
            "\\begin{align*}"
        ).scale(0.7).align_to(problem4, UP)

        self.play(
            Unwrite(d3),
            TransformMatchingShapes(problem4, problem5, path_arc=PI/2)
        )
        self.wait()

        self.play(
            plane.animate.next_to(problem5, DOWN, buff=0.5)
        )
        self.wait()

        self.play(
            Flash(c)
        )
        self.wait()

        self.play(
            Flash(v1)
        )
        self.wait()

        self.play(
            Flash(v2)
        )
        self.wait()

        h = ValueTracker(0)
        a1 = always_redraw(
            lambda : plane.plot(
                lambda x : np.tan(PI/3)*(x-h.get_value()),
                x_range=[
                    (6*h.get_value()-np.sqrt(-12*h.get_value()*h.get_value()+576))/8,
                    (6*h.get_value()+np.sqrt(-12*h.get_value()*h.get_value()+576))/8
                ]
            ).scale_to_fit_height(plane.height-1)
        )
        a2 = always_redraw(
            lambda : plane.plot(
                lambda x : np.tan(5*PI/3)*(x-h.get_value()),
                x_range=[
                    (6*h.get_value()-np.sqrt(-12*h.get_value()*h.get_value()+576))/8,
                    (6*h.get_value()+np.sqrt(-12*h.get_value()*h.get_value()+576))/8
                ]
            ).scale_to_fit_height(plane.height-1)
        )
        
        self.play(
            Create(a1)
        )
        self.wait()

        self.play(
            Create(a2)
        )
        self.wait()

        self.play(
            h.animate.set_value(-4/3)
        )
        self.wait()

        ct = ValueTracker(np.arccos(1/6))
        curve = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(2/(1-2*np.cos(t)), t), 
                t_range = [np.arccos(1/6), ct.get_value()], 
                color=YELLOW, 
                use_smoothing=False, 
                discontinuities = [PI/3,5*PI/3], 
                dt = 0.1
            )
        )
        self.add(
            curve
        )
        self.wait()

        self.play(
            ct.animate.set_value(np.arccos(-1/6)+PI)
        )
        self.wait(.2)
        
        ct2 = ValueTracker(5.7)
        curve2 = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(2/(1-2*np.cos(t)), t), 
                t_range = [5.7, ct2.get_value()], 
                color=YELLOW, 
                use_smoothing=False, 
                discontinuities = [PI/3,5*PI/3], 
                dt = 0.1
            )
        )
        self.add(
            curve2
        )
        self.wait()

        self.play(
            ct2.animate.set_value(2*PI+.583)
        )
        self.wait()