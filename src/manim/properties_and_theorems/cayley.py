from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math


class Cayley1(Scene):
    def construct(self):
        G = MathTex(r'G').scale(2)
        group_def = MathTex(r'G = \left(', r'\{g_1, g_2, ...\}', r',', r'*', r'\right)').scale(2)

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
            group_def[1].animate.set_color(BLUE),
            group_def[3].animate.set_color(RED)
        )

        g = MathTex(r'g').scale(2).set_color(BLUE)

        self.play(
            ReplacementTransform(group_def[1].copy(), g)
        )

        self.wait(2)

        Tg = MathTex(r'T', r'_g').scale(2)
        Tg[1].set_color(BLUE)

        self.play(
            ReplacementTransform(g, Tg[1])
        )

        self.play(
            Write(Tg[0])
        )

        self.wait(2)

        Tg_map = MathTex(r'T', r'_g', r': G \rightarrow G').scale(2)
        Tg_map[1].set_color(BLUE)

        self.play(
            Transform(Tg, Tg_map[:2])
        )
        self.remove(Tg_map[:2])
        self.play(
            Write(Tg_map[2:])
        )

        self.wait(2)

        self.play(
            Unwrite(Tg_map[2:])
        )

        Tg_func = MathTex(r'T', r'_g', r'(', r'x', r') =',  r'g', r'*', r'x').scale(2)
        Tg_func[1].set_color(BLUE)
        Tg_func[5].set_color(BLUE)
        Tg_func[6].set_color(RED)

        self.play(
            Transform(Tg, Tg_func[:2])
        )
        self.play(
            Write(Tg_func[2:5])
        )
        self.play(
            Write(Tg_func[5], run_time=0.5)
        )
        self.play(
            ReplacementTransform(group_def[3].copy(), Tg_func[6], run_time=0.5)
        )
        self.play(
            ReplacementTransform(Tg_func[3].copy(), Tg_func[7], run_time=0.5)
        )

        self.wait(2)

        self.remove(Tg)
        Tg_func.generate_target()
        Tg_func.target.move_to(UP * 3 + RIGHT * 4)
        Tg_func.target.scale(0.5)
        self.play(
            MoveToTarget(Tg_func)
        )

        divider = Line(array([-10, 0, 0]), array([10, 0, 0]), color=YELLOW)
        divider.move_to(UP*2.5)

        self.play(
            Create(divider)
        )
        self.wait(2)

        Tg_comp = MathTex(r'(', r'T', r'_g', r'\circ', r'T', r'_{g^{-1}}', r')').scale(2)
        Tg_comp[2].set_color(BLUE)
        Tg_comp[5].set_color(BLUE)

        self.play(
            Write(Tg_comp[1], run_time=0.5)
        )
        self.play(
            ReplacementTransform(group_def[1].copy(), Tg_comp[2], run_time=0.5)
        )
        self.play(
            Write(Tg_comp[3:5], run_time=0.5)
        )
        self.play(
            ReplacementTransform(group_def[1].copy(), Tg_comp[5], run_time=0.5)
        )
        self.play(
            Write(Tg_comp[0]),
            Write(Tg_comp[6])
        )

        Tg_comp2 = MathTex(r'(', r'T', r'_g', r'\circ', r'T', r'_{g^{-1}}', r')', r'(', r'x', r')').scale(2)
        Tg_comp2[2].set_color(BLUE)
        Tg_comp2[5].set_color(BLUE)

        self.play(
            Transform(Tg_comp, Tg_comp2[:7])
        )
        self.play(
            Write(Tg_comp2[7:])
        )
        self.remove(Tg_comp)

        Tg_comp3 = MathTex(r'T', r'_g', r'(', r'T', r'_{g^{-1}}', r'(', r'x', r')', r')').scale(2)
        Tg_comp3[1].set_color(BLUE)
        Tg_comp3[4].set_color(BLUE)

        self.play(
            ReplacementTransform(Tg_comp2, Tg_comp3)
        )

        self.wait(2)

        Tg_comp_def = MathTex(r'T', r'_g', r'(', r'T', r'_{g^{-1}}', r'(', r'x', r')', r')', r'=', r'g', r'*', r'(', r'g^{-1}', r'*', r'x', r')').scale(2)
        Tg_comp_def[1].set_color(BLUE)
        Tg_comp_def[4].set_color(BLUE)
        Tg_comp_def[10].set_color(BLUE)
        Tg_comp_def[13].set_color(BLUE)
        Tg_comp_def[11].set_color(RED)
        Tg_comp_def[14].set_color(RED)

        self.play(
            ReplacementTransform(Tg_comp3, Tg_comp_def[:9])
        )
        self.play(
            Write(Tg_comp_def[9:])
        )
        self.remove(Tg_comp3)

        Tg_comp_def2 = MathTex(r'T', r'_g', r'(', r'T', r'_{g^{-1}}', r'(', r'x', r')', r')', r'=', r'(', r'g', r'*', r'g^{-1}', r')', r'*', r'x').scale(2)
        Tg_comp_def2[1].set_color(BLUE)
        Tg_comp_def2[4].set_color(BLUE)
        Tg_comp_def2[11].set_color(BLUE)
        Tg_comp_def2[13].set_color(BLUE)
        Tg_comp_def2[12].set_color(RED)
        Tg_comp_def2[15].set_color(RED)

        self.play(
            ReplacementTransform(Tg_comp_def, Tg_comp_def2)
        )

        Tg_comp_def3 = MathTex(r'T', r'_g', r'(', r'T', r'_{g^{-1}}', r'(', r'x', r')', r')', r'=', r'x').scale(2)
        Tg_comp_def3[1].set_color(BLUE)
        Tg_comp_def3[4].set_color(BLUE)

        self.wait(2)

        self.play(
            FadeOut(Tg_comp_def2[10:16], run_time=0.5),
            ReplacementTransform(Tg_comp_def2[:10], Tg_comp_def3[:10]),
            ReplacementTransform(Tg_comp_def2[-1], Tg_comp_def3[-1])
        )
        self.remove(Tg_comp_def2)

        Tg_inv = MathTex(r'(', r'T', r'_g', r')', r'^{-1}', r'=', r'T', r'_{g^{-1}}').scale(2)
        Tg_inv[2].set_color(BLUE)
        Tg_inv[7].set_color(BLUE)

        self.wait(2)

        self.play(
            ReplacementTransform(Tg_comp_def3, Tg_inv)
        )

        self.wait(2)


class Cayley2(Scene):
    def construct(self):
        group_def = MathTex(r'G = \left(', r'\{g_1, g_2, ...\}', r',', r'*', r'\right)')
        group_def[1].set_color(BLUE)
        group_def[3].set_color(RED)
        group_def.move_to(UP*3 + LEFT*4)

        Tg_func = MathTex(r'T', r'_g', r'(', r'x', r') =', r'g', r'*', r'x')
        Tg_func[1].set_color(BLUE)
        Tg_func[5].set_color(BLUE)
        Tg_func[6].set_color(RED)
        Tg_func.move_to(UP*3 + RIGHT*4)

        divider = Line(array([-10, 0, 0]), array([10, 0, 0]), color=YELLOW)
        divider.move_to(UP * 2.5)

        self.add(group_def, Tg_func, divider)

        prop1 = MathTex(r'T', r'_g', r'\text{ is\ldots}')
        prop1[1].set_color(BLUE)
        prop2 = Tex(r'bijective (well-defined inverse)')
        prop3 = Tex(r'a self-mapping of the set of elements in $G$')
        prop4 = Tex(r'\vdots')
        prop5 = Tex(r'permutation!')
        prop1.shift(UP*1)

        print(prop1)

        vg = VGroup(prop1, prop2, prop3, prop4, prop5)
        for i in range(4):
            vg[i+1].next_to(vg[i], DOWN)

        self.play(
            Write(vg[0])
        )
        self.play(
            Write(vg[1])
        )
        self.play(
            Write(vg[2])
        )
        self.play(
            Write(vg[3])
        )
        self.play(
            Write(vg[4])
        )

        self.wait(2)


class Cayley3(Scene):
    def construct(self):
        group_def = MathTex(r'G = \left(', r'\{g_1, g_2, ...\}', r',', r'*', r'\right)')
        group_def[1].set_color(BLUE)
        group_def[3].set_color(RED)
        group_def.move_to(UP * 3 + LEFT * 4)

        Tg_func = MathTex(r'T', r'_g', r'(', r'x', r') =', r'g', r'*', r'x')
        Tg_func[1].set_color(BLUE)
        Tg_func[5].set_color(BLUE)
        Tg_func[6].set_color(RED)
        Tg_func.move_to(UP * 3 + RIGHT * 4)

        divider = Line(array([-10, 0, 0]), array([10, 0, 0]), color=YELLOW)
        divider.move_to(UP * 2.5)

        self.add(group_def, Tg_func, divider)