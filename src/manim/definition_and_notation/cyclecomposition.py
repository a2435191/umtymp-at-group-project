from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math


class CycleComp(Scene):
    def construct(self):
        l_string = '(12)(3)(45)'
        circle = r'\circ'
        r_string = '(153)(24)'
        comp = MathTex(*l_string, circle, *r_string).scale(2)
        comp2 = MathTex(*l_string, *r_string).scale(2)

        self.play(
            Write(comp)
        )
        self.wait(2)
        self.play(
            Unwrite(comp[11])
        )
        self.play(
            ReplacementTransform(comp[:11], comp2[:11]),
            ReplacementTransform(comp[12:], comp2[11:])
        )
        self.remove(comp)

        self.wait(2)

        comp2.generate_target()
        comp2.target.move_to(UP*3)

        self.play(
            MoveToTarget(comp2)
        )

        c1 = MathTex(r'1', r'\rightarrow 5', r'\rightarrow 4').scale(2)
        c2 = MathTex(r'2', r'\rightarrow 4', r'\rightarrow 5').scale(2)
        c3 = MathTex(r'3', r'\rightarrow 1', r'\rightarrow 2').scale(2)
        c4 = MathTex(r'4', r'\rightarrow 2', r'\rightarrow 1').scale(2)
        c5 = MathTex(r'5', r'\rightarrow 3', r'\rightarrow 3').scale(2)

        result = MathTex('=(', *'14)(253)').scale(2).shift(3*DOWN)

        cs = [c1, c2, c3, c4, c5]
        nums = [comp2[17:19], comp2[12:15], comp2[8:10], comp2[5:6], comp2[1:3]]
        orders = [[1, 2], [0, 2], [1, 4], [0, 4], [1, 3]]
        results = [result[0:3], result[3:4], result[4:7], result[7:8], result[8:9]]

        ks = [0, 3, 1, 4, 2]

        for k in range(5):
            i = ks[k]
            order = orders[i]
            c = cs[i]
            unders = [Underline(num).set_color(BLUE) for num in nums]
            self.play(
                Write(c[0])
            )
            for j in range(5):
                num = nums[j]
                under = unders[j]
                self.play(
                    num.animate.set_color(BLUE),
                    Write(under)
                )
                if j in order:
                    self.play(
                        Write(
                            c[order.index(j) + 1]
                        )
                    )
                self.play(
                    num.animate.set_color(WHITE),
                    Unwrite(under)
                )
            self.play(
                Write(results[k])
            )
            self.play(
                Unwrite(c)
            )
        self.wait(2)

        self.play(
            comp2.animate.shift(DOWN*2),
            result.animate.shift(UP*2)
        )