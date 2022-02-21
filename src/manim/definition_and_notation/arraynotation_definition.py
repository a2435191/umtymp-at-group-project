from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math

class ArrayNotationDef(Scene):
    def construct(self):
        define = MathTex(r'''\pi = \begin{bmatrix}
        g_1 & g_2 & g_3 & \cdots & g_n\\
        \pi(g_1) & \pi(g_2) & \pi(g_3) & \cdots & \pi(g_n)
        \end{bmatrix}''')

        self.play(
            Write(define)
        )

        self.wait(2)

        self.play(
            Unwrite(define)
        )