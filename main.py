from manim import *

class PolarConic(Scene):

    minimum_t = 0

    def construct(self):
        def mini_t(plane,d,e,t):
            if np.abs(d*e/(1-e*np.cos(t))) > 0 and np.abs(d*e/(1-e*np.cos(t))) < 3:
                self.minimum_t=t
            
            return plane.polar_to_point(d*e/(1-e*np.cos(self.minimum_t)), self.minimum_t)
        
        e = ValueTracker(0.01)

        dtx = 1.00
        ecc = 2.00

        dtx_display = Variable(dtx, MathTex(r"d"), num_decimal_places=2)
        ecc_display = Variable(ecc, MathTex(r"e"), num_decimal_places=2)

        dtx_tracker = dtx_display.tracker
        ecc_tracker = ecc_display.tracker

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(LEFT*2)
        hyperbola = always_redraw(
            lambda : ParametricFunction(
                lambda t : mini_t(plane,dtx_tracker.get_value(),ecc_tracker.get_value(),t), 
                t_range = [0, e.get_value()], 
                color=GREEN, 
                use_smoothing=False, 
                discontinuities = [np.arccos(1/ecc_tracker.get_value()),2*PI-np.arccos(1/ecc_tracker.get_value())], 
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
                lambda x : dtx_tracker.get_value()*ecc_tracker.get_value()/(1-ecc_tracker.get_value()*np.cos(x))
                if np.abs(dtx_tracker.get_value()*ecc_tracker.get_value()/(1-ecc_tracker.get_value()*np.cos(x))) < 4
                else x,
                x_range = [0, e.get_value()],
                color = GREEN,
                use_smoothing=False, 
                discontinuities = [np.arccos(1/ecc_tracker.get_value()),2*PI-np.arccos(1/ecc_tracker.get_value())],  
                dt = 0.1
            )
        )
        gdot = always_redraw(
            lambda : Dot(
                fill_color=GREEN,
                fill_opacity=0.8
            ).scale(1.2).move_to(graph.get_end())
        )

        title = MathTex(r"r=\frac{ed}{1-e\cos\theta}", color=GREEN).next_to(axes,UP,buff=0.2)
        dtx_display.set_color(GREEN).next_to(axes, DOWN, buff = 0.2)
        ecc_display.set_color(GREEN).next_to(dtx_display, DOWN, buff = 0.2)

        self.play(
            LaggedStart(
                Write(plane),
                Create(axes),
                Write(title),
                Write(dtx_display),
                Write(ecc_display),
                run_time=3,
                lag_ratio=0.5
            )
        )
        
        self.add(hyperbola,graph,hdot,gdot)

        self.play(
            e.animate.set_value(2*PI),
            run_time=2, rate_func=linear
        )
        self.wait(1)

        self.play(
            dtx_tracker.animate.set_value(.50),
            ecc_tracker.animate.set_value(1.001),
            run_time=2, rate_func=linear)
        self.wait(1)
        
        self.play(
            dtx_tracker.animate.set_value(2.00),
            ecc_tracker.animate.set_value(0.5),
            run_time=2, rate_func=linear)
        self.wait(1)

        
        self.play(
            dtx_tracker.animate.set_value(1.00),
            ecc_tracker.animate.set_value(1.001),
            run_time=2, rate_func=linear)
        self.wait(1)

        self.play(ecc_tracker.animate.set_value(2), run_time=2, rate_func=linear)
        self.wait(1)