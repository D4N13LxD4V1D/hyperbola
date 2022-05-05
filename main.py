from manim import *

class PolarConic(Scene):
    def construct(self):
        e = ValueTracker(0.01)

        dtx = ValueTracker(1.0)
        ecc = ValueTracker(2.0)

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        hyperbola = always_redraw(
            lambda : ParametricFunction(
                lambda t : plane.polar_to_point(dtx.get_value()*ecc.get_value()/(1-ecc.get_value()*np.cos(t)), t), 
                t_range = [0, e.get_value()], 
                color=GREEN, 
                use_smoothing=False, 
                discontinuities = [PI/3, 5*PI/3], 
                dt = 0.1
            )
        )
        hdot = always_redraw(
            lambda : Dot(
                fill_color=GREEN,
                fill_opacity=0.8
            ).scale(1.2).move_to(hyperbola.get_end())
        )

        axes = Axes(
            x_range=[0, 8, 1],
            x_length=4,
            y_range=[-3,3,1],
            y_length=3
        ).shift(RIGHT*4)
        axes.add_coordinates()
        graph = always_redraw(
            lambda : axes.plot(
                lambda x : dtx.get_value()*ecc.get_value()/(1-ecc.get_value()*np.cos(x)),
                x_range = [0, e.get_value()],
                color = GREEN,
                use_smoothing=False, 
                discontinuities = [PI/3, 5*PI/3], 
                dt = 0.1
            )
        )
        gdot = always_redraw(
            lambda : Dot(
                fill_color=GREEN,
                fill_opacity=0.8
            ).scale(1.2).move_to(graph.get_end())
        )

        title = MathTex(r"r=\frac{2}{1-2\cos\theta}", color=GREEN).next_to(axes,UP,buff=0.2)
        
        self.play(
            LaggedStart(
                Write(plane), Create(axes), Write(title),
                run_time=3,
                lag_ratio=0.5
            )
        )
        
        self.add(hyperbola,graph,hdot,gdot)
        self.play(
            e.animate.set_value(2*PI), run_time=2, rate_func=linear
        )
        self.play(ecc.animate.set_value(0), run_time=2, rate_func=linear)
        self.play(ecc.animate.set_value(1), run_time=2, rate_func=linear)
        self.play(ecc.animate.set_value(2), run_time=2, rate_func=linear)
        self.wait(0.1)