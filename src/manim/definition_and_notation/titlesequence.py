from manim import *
import numpy as np
from numpy import array

class TitleSequence(Scene):
    def construct(self):
        P00T = Tex(r'P').set_stroke(width=1.5).set_fill(opacity=0)
        P00D = Dot(point=[2,-2,0], radius=rad, color=RED).set_stroke(width=4).set_fill(opacity=0)
