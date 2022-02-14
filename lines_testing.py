from manim import *
import numpy as np
import math

class Lines(Scene):
    def construct(self):
        # After creating the RubiksCube, it may be necessary to scale it to
        # comfortably see the cube in the camera's frame
        path = Line(start=[0, 0, 0], end=[0, 1, 0], stroke_color='#FFFFFF')
        path.add_line_to(np.array([1, 1, 0]))
        path.add_line_to(np.array([2, 2, 0]))
        path.add_tip()

        self.play(
            Create(path)
        )

