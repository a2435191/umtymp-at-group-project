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
        self.play(
            Unwrite(Tg_inv)
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
        self.play(
            Unwrite(vg)
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

        H = MathTex(r'H', r'=', r'\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\}').scale(2)
        H[4].set_color(BLUE)
        H[6].set_color(BLUE)

        self.play(
            Write(H)
        )
        self.wait(2)

        group_def.generate_target()
        group_def.target.shift(0.25*LEFT)

        H.generate_target()
        H.target.scale(0.5)
        H.target.next_to(group_def.target, 4*RIGHT)

        Tg_func.generate_target()
        Tg_func.target.next_to(H.target, 4*RIGHT)

        self.play(
            MoveToTarget(H),
            MoveToTarget(group_def),
            MoveToTarget(Tg_func)
        )

        props = BulletedList('associativity', 'existence of identity element', r'existence of inverse elements\phantom{y}', r'closure\phantom{y}')
        label = Tex('Under composition, $H$ satisfies\ldots')
        props.shift(DOWN)
        label.next_to(props, 2*UP)
        props.shift(2*LEFT)

        self.play(
            Write(label)
        )
        self.play(
            Write(props)
        )
        self.wait(2)

        check = MathTex(r'\checkmark').set_color(GREEN)
        checks = VGroup()
        for i in range(4):
            checks.add(check.copy())
            checks[i].next_to(props[i], RIGHT)

        identity = MathTex(r'e_H=T', r'_e')
        identity[1].set_color(BLUE)
        identity.next_to(checks[-3], RIGHT)

        inverse = MathTex(r'(T', r'_g', r')^{-1}=T', r'_{g^{-1}}')
        inverse[1].set_color(BLUE)
        inverse[3].set_color(BLUE)
        inverse.next_to(checks[-2], RIGHT)

        closure = MathTex(r'T', r'_a', r'\circ', r'T', r'_b', r'=', r'T', r'_{a', r'*', r'b}')
        closure[1].set_color(BLUE)
        closure[4].set_color(BLUE)
        closure[7].set_color(BLUE)
        closure[8].set_color(RED)
        closure[9].set_color(BLUE)
        closure.next_to(checks[-1], RIGHT)

        extra = [None, identity, inverse, closure]

        for i in range(4):
            self.play(
                Write(checks[i])
            )
            if extra[i] is not None:
                self.play(
                    Write(extra[i])
                )
            self.wait(1)

        self.wait(2)

        H_group = MathTex(r'H', r'=', r'(\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\},\circ)')
        H_group.move_to(H)
        H_group[4].set_color(BLUE)
        H_group[6].set_color(BLUE)

        self.play(
            ReplacementTransform(H, H_group)
        )

        self.wait(2)
        self.play(
            *[Unwrite(check) for check in checks],
            *[Unwrite(ex) for ex in extra if ex is not None],
            Unwrite(label),
            Unwrite(props)
        )
        self.wait(2)


class Cayley4(Scene):
    def construct(self):
        group_def = MathTex(r'G = \left(', r'\{g_1, g_2, ...\}', r',', r'*', r'\right)')
        group_def[1].set_color(BLUE)
        group_def[3].set_color(RED)
        group_def.move_to(UP * 3 + LEFT * 4.25)

        H = MathTex(r'H', r'=', r'\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\}')
        H[4].set_color(BLUE)
        H[6].set_color(BLUE)
        H.next_to(group_def, 4*RIGHT)

        Tg_func = MathTex(r'T', r'_g', r'(', r'x', r') =', r'g', r'*', r'x')
        Tg_func[1].set_color(BLUE)
        Tg_func[5].set_color(BLUE)
        Tg_func[6].set_color(RED)
        Tg_func.next_to(H, 4*RIGHT)

        H_group = MathTex(r'H', r'=', r'(\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\},\circ)')
        H_group[4].set_color(BLUE)
        H_group[6].set_color(BLUE)
        H_group.move_to(H)

        divider = Line(array([-10, 0, 0]), array([10, 0, 0]), color=YELLOW)
        divider.move_to(UP * 2.5)

        self.add(group_def, H_group, Tg_func, divider)

        phi_map = MathTex(r'\varphi', r': G \rightarrow H').scale(2)
        phi_map[0].set_color(GOLD)

        self.play(
            Write(phi_map)
        )

        self.wait(2)

        self.play(
            Unwrite(phi_map[1:])
        )

        phi_func = MathTex(r'\varphi', r'(', r'g', r')', r'=', r'T', r'_g').scale(2)
        phi_func[0].set_color(GOLD)
        phi_func[2].set_color(BLUE)
        phi_func[-1].set_color(BLUE)

        self.play(
            Transform(phi_map[0], phi_func[0])
        )
        self.play(
            Write(phi_func[1:])
        )
        self.wait(2)

        self.remove(phi_map[0])

        phi_func.generate_target()
        phi_func.target.scale(0.5)
        phi_func.target.shift(UP*2)
        phi_func.target.align_to(group_def, LEFT)

        self.play(
            MoveToTarget(phi_func)
        )

        self.wait(2)

        homo = MathTex(r'\varphi', '(', 'a', ')\circ', r'\varphi', '(', 'b', ')').scale(2)
        homo[0].set_color(GOLD)
        homo[2].set_color(BLUE)
        homo[4].set_color(GOLD)
        homo[6].set_color(BLUE)

        homo_full = MathTex(r'\varphi', '(', 'a', r')\circ', r'\varphi', '(', 'b', ')', '=', 'T', '_a', r'\circ', 'T', '_b').scale(2)
        homo_full[0].set_color(GOLD)
        homo_full[2].set_color(BLUE)
        homo_full[4].set_color(GOLD)
        homo_full[6].set_color(BLUE)
        homo_full[10].set_color(BLUE)
        homo_full[13].set_color(BLUE)

        homo_simp = MathTex(r'\varphi', '(', 'a', ')\circ', r'\varphi', '(', 'b', ')', '=', 'T', '_{a', '*', 'b}').scale(2)
        homo_simp[0].set_color(GOLD)
        homo_simp[2].set_color(BLUE)
        homo_simp[4].set_color(GOLD)
        homo_simp[6].set_color(BLUE)
        homo_simp[10].set_color(BLUE)
        homo_simp[11].set_color(RED)
        homo_simp[12].set_color(BLUE)

        homo_homo = MathTex(r'\varphi', '(', 'a', ')\circ', r'\varphi', '(', 'b', ')', '=', r'\varphi', '(', 'a', '*', 'b', ')').scale(2)
        homo_homo[0].set_color(GOLD)
        homo_homo[2].set_color(BLUE)
        homo_homo[4].set_color(GOLD)
        homo_homo[6].set_color(BLUE)
        homo_homo[9].set_color(GOLD)
        homo_homo[11].set_color(BLUE)
        homo_homo[12].set_color(RED)
        homo_homo[13].set_color(BLUE)

        self.play(
            Write(homo)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(homo, homo_full[:8])
        )
        self.remove(homo)
        self.play(
            Write(homo_full[8:])
        )

        self.wait(2)

        self.play(
            Unwrite(homo_full[9:])
        )
        self.play(
            ReplacementTransform(homo_full[:9], homo_simp[:9])
        )
        self.remove(homo_full)
        self.play(
            Write(homo_simp[9:])
        )

        self.wait(2)

        self.play(
            Unwrite(homo_simp[9:])
        )
        self.play(
            ReplacementTransform(homo_simp[:9], homo_homo[:9])
        )
        self.remove(homo_simp)
        self.play(
            Write(homo_homo[9:])
        )

        self.wait(2)

        self.play(
            Unwrite(homo_homo[1:])
        )
        conc = Tex(r'$\varphi$', ' is a homomorphism!').scale(2)
        conc[0].set_color(GOLD)

        self.play(
            ReplacementTransform(homo_homo[0], conc[0])
        )
        self.play(
            Write(conc[1:])
        )

        self.wait(2)

        self.remove(homo_homo[0])
        self.play(
            Unwrite(conc)
        )

        self.wait(2)


class Cayley5(Scene):
    def construct(self):
        group_def = MathTex(r'G = \left(', r'\{g_1, g_2, ...\}', r',', r'*', r'\right)')
        group_def[1].set_color(BLUE)
        group_def[3].set_color(RED)
        group_def.move_to(UP * 3 + LEFT * 4.25)

        H = MathTex(r'H', r'=', r'\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\}')
        H[4].set_color(BLUE)
        H[6].set_color(BLUE)
        H.next_to(group_def, 4 * RIGHT)

        Tg_func = MathTex(r'T', r'_g', r'(', r'x', r') =', r'g', r'*', r'x')
        Tg_func[1].set_color(BLUE)
        Tg_func[5].set_color(BLUE)
        Tg_func[6].set_color(RED)
        Tg_func.next_to(H, 4 * RIGHT)

        H_group = MathTex(r'H', r'=', r'(\{', r'T', r'_g', r'\, | \,', r'g', r'\in', r'G', r'\},\circ)')
        H_group[4].set_color(BLUE)
        H_group[6].set_color(BLUE)
        H_group.move_to(H)

        phi_func = MathTex(r'\varphi', r'(', r'g', r')', r'=', r'T', r'_g')
        phi_func[0].set_color(GOLD)
        phi_func[2].set_color(BLUE)
        phi_func[-1].set_color(BLUE)
        phi_func.shift(UP * 2)
        phi_func.align_to(group_def, LEFT)

        divider = Line(array([-10, 0, 0]), array([10, 0, 0]), color=YELLOW)
        divider.move_to(UP * 2.5)

        self.add(group_def, H_group, Tg_func, phi_func, divider)

        inj1 = MathTex(r'\varphi', r'(', r'a', r')', r'=', r'\varphi', '(', 'b', ')').scale(2)
        inj1[0].set_color(GOLD)
        inj1[2].set_color(BLUE)
        inj1[5].set_color(GOLD)
        inj1[7].set_color(BLUE)

        inj2 = MathTex(r'T', r'_a', r'=', r'T', '_b').scale(2)
        inj2[1].set_color(BLUE)
        inj2[4].set_color(BLUE)

        inj3 = MathTex(r'T', r'_a', r'(x)', r'=', r'T', '_b', r'(x)').scale(2)
        inj3[1].set_color(BLUE)
        inj3[5].set_color(BLUE)

        inj4 = MathTex(r'a', r'*', r'x', r'=', r'b', '*', r'x').scale(2)
        inj4[0].set_color(BLUE)
        inj4[1].set_color(RED)
        inj4[4].set_color(BLUE)
        inj4[5].set_color(RED)

        inj5 = MathTex(r'a', r'=', r'b').scale(2)
        inj5[0].set_color(BLUE)
        inj5[2].set_color(BLUE)

        inj = Tex(r'$\varphi$', r' is injective\ldots')
        inj[0].set_color(GOLD)
        surj = Tex(r'$\varphi$', r' is surjective because it is defined as a function.')
        surj[0].set_color(GOLD)

        self.play(
            Write(surj)
        )

        self.wait(2)

        self.play(
            Unwrite(surj)
        )

        self.wait(2)

        self.play(
            Write(inj)
        )

        self.wait(2)

        self.play(
            Unwrite(inj)
        )

        self.wait(2)

        self.play(
            Write(inj1)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(inj1, inj2)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(inj2, inj3)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(inj3, inj4)
        )

        self.wait(2)

        self.play(
            ReplacementTransform(inj4, inj5)
        )

        self.wait(2)

        self.play(
            Unwrite(inj5)
        )

        self.wait(2)

        conc = MathTex(r'G \approx H').scale(2)

        self.play(
            Write(conc)
        )

        self.wait(2)

        self.play(
            Unwrite(conc)
        )

        self.wait(2)


class CayleyIntro(Scene):
    def construct(self):
        title = Tex('Cayley\'s Theorem').scale(3)
        title.shift(UP)
        line = Line(6*LEFT, 6*RIGHT)
        line.next_to(title, DOWN)
        desc = Tex(r'Every group is isomorphic to some permutation group.')
        desc.next_to(line, DOWN*2)

        self.play(
            Write(title),
            Create(line)
        )
        self.wait(2)

        self.play(
            Write(desc)
        )

        self.wait(2)

        self.play(
            Unwrite(title),
            Unwrite(desc),
            Uncreate(line)
        )

        self.wait(2)