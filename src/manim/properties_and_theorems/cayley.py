from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math

class Cayley(Scene):
    def construct(self):
        G = MathTex(r'G').scale(2)
        group_def = MathTex(r'G = \left(\{', r'g_1', r', g_2, ...\}, *\right)').scale(2)

        self.play(
            Write(G)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(G, group_def)
        )

        self.wait(2)

        group_def.generate_target()
        group_def.target.scale(0.5)
        group_def.target.move_to(UP*3 + LEFT*4)

        self.play(
            MoveToTarget(group_def)
        )

        self.play(
            group_def[1].animate.set_color(BLUE)
        )

        g = MathTex(r'g').scale(2).set_color(BLUE)

        self.play(
            ReplacementTransform(group_def[1].copy(), g)
        )

        self.wait(2)

        Tg = MathTex(r'T', r'_g')
        Tg[1].set_color(BLUE)

        self.play(
            ReplacementTransform(g, Tg[1]),
            Write(Tg[0])
        )

        self.wait(2)

        Tg_map = MathTex(r'T', r'_g', r': G \rightarrow G')
        Tg_map[1].set_color(BLUE)

        self.play(
            ReplacementTransform(Tg, Tg_map[:2])
        )
        self.play(
            Write(Tg_map[2:])
        )

        self.wait(2)

        Tg.generate_target()
        Tg.target.move_to(array([0, 0, 0]))

        self.play(
            Unwrite(Tg_map[2:])
        )
        self.play(
            MoveToTarget(Tg)
        )

        Tg_func = MathTex(r'T', r'_g', r'(x) = g * x')
        Tg_func[1].set_color(BLUE)

        self.play(
            ReplacementTransform(Tg, Tg_func[:2])
        )
        self.play(
            Write(Tg_map[2:])
        )
