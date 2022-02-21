from manim import *

class Theorem1Intro(Scene):
    def construct(self):
        title = Tex("Non-trivial symmetric groups are non-Abelian", font_size=22).scale(3)
        
        title.shift(UP)
        line = Line(6*LEFT, 6*RIGHT)
        line.next_to(title, DOWN)
        desc = Tex(r'For all $n :n > 2$, $S_n$ is non-Abelian.', font_size=72)
        desc.next_to(line, DOWN*2)

        self.play(
            Write(title),
            Create(line)
        )

        self.wait()

        self.play(
            Write(desc)
        )

        self.wait(2)
        
    
        self.play(
            Unwrite(title),
            Unwrite(desc),
            Uncreate(line)
        )

        self.wait()

class Theorem1Proof(Scene):
    def construct(self):
        desc = Tex(r'For all $n :n > 2$, $S_n$ is non-Abelian.', font_size=72).shift(UP * 3)
        
        line = Line(6*LEFT, 6*RIGHT).next_to(desc, DOWN)

        self.play(FadeIn(desc, line))
        self.wait()

        base_case = Tex(r"Base case", r": $S_3$ is non-Abelian.", tex_environment=None)\
            .next_to(line, DOWN, aligned_edge=LEFT)
        
        base_case_pf_header = Tex(r"\textit{Proof: }", tex_environment=None)\
            .next_to(base_case, DOWN, aligned_edge=LEFT)

        self.play(Write(base_case))
        self.play(Write(base_case_pf_header))

        CMAP = {
            r"a": BLUE, 
            r"b": RED, 
            r"1": YELLOW, r"2": YELLOW, r"3": YELLOW
        }
        base_case_pf_defs = MathTex(
            r"a = (12)(3)\text{, }b = (13)(2)", substrings_to_isolate="ab"
        ).set_color_by_tex_to_color_map({"a": BLUE, "b": RED})
        
        base_case_pf_ab = MathTex(
            r"ab &= a(b(123))\\",
            r"&=a(321)\\",
            r"&=231",
            substrings_to_isolate=list(CMAP.keys())
        )\
            .set_color_by_tex_to_color_map(CMAP)\
            .next_to(base_case_pf_defs, DOWN)\
            .shift(LEFT * 2)

        base_case_pf_ba = MathTex(
            r"ba &= b(a(123))\\",
            r"&=b(213)\\",
            r"&=312",
            substrings_to_isolate=list(CMAP.keys())
        )\
            .set_color_by_tex_to_color_map(CMAP)\
            .next_to(base_case_pf_defs, DOWN)\
            .shift(RIGHT * 2)
        self.play(Write(base_case_pf_defs))
        self.play(
            Write(base_case_pf_ab),
            Write(base_case_pf_ba)
        )

        self.wait(4)

        induction_step = Tex(r"Induction steps: assume $S_k$ is non-Abelian and prove $S_{k+1}$ is non-Abelian.", font_size=36)\
            .next_to(line, DOWN, aligned_edge=LEFT)

        self.play(
            ReplacementTransform(base_case, induction_step),
            FadeOut(base_case_pf_ab, base_case_pf_ba, base_case_pf_header, base_case_pf_defs)
        )

        induction_a_def = Tex(
            r"$a_k$", r"""$ = \begin{bmatrix}
1 & 2 & 3 & \cdots & k \\
3 & 2 & k - 4 & \cdots & 7
\end{bmatrix}$"""
        ).set_color_by_tex(r"a_k", BLUE).shift(3 * LEFT)
        induction_b_def = Tex(
            r"$b_k$", r"""$ = \begin{bmatrix}
1 & 2 & 3 & \cdots & k \\
2 & 1 & 6 & \cdots & k
\end{bmatrix}$"""
        ).set_color_by_tex(r"b_k", RED).shift(3 * RIGHT)

        self.play(
            FadeIn(induction_a_def, induction_b_def)
        )

        non_abelian = MathTex(*(r"a_k b_k \neq b_k a_k".split())).next_to(induction_step, DOWN)
        non_abelian[0].set_color(BLUE)
        non_abelian[4].set_color(BLUE)
        non_abelian[1].set_color(RED)
        non_abelian[3].set_color(RED)

        self.play(
            Write(non_abelian)
        )
        self.wait()

        induction_a_next = Tex(
            r"$a_{k+1}$", r" $=$ ", r"$a_k$", r"$+ \begin{bmatrix} k + 1 \\ k + 1\end{bmatrix}$"
        ).set_color_by_tex(r"$a_{k+1}$", BLUE).move_to(induction_a_def, LEFT).shift(2 * DOWN)
        induction_b_next = Tex(
            r"$b_{k+1}$", r" $=$ ", r"$b_k$", r"$+ \begin{bmatrix} k + 1 \\ k + 1\end{bmatrix}$"
        ).set_color_by_tex(r"$b_{k+1}$", RED).move_to(induction_b_def, LEFT).shift(2 * DOWN)

        self.play(Write(induction_a_next), Write(induction_b_next))

        self.play(
            induction_b_next.animate.move_to(induction_a_next, LEFT),
            induction_a_next.animate.move_to(induction_a_def, LEFT),
            FadeOut(induction_a_def, induction_b_def, non_abelian)
        )

        induction_a_expanded = MathTex(
            r" = f: f(x) = \begin{cases}" +
            r"k + 1 & \text{if } x = k + 1\\ "+
            r"a_k(x) & \text{otherwise}"+
            r"\end{cases}")\
            .next_to(induction_a_next)
        induction_b_expanded = MathTex(
            r" = f: f(x) = \begin{cases}" +
            r"k + 1 & \text{if } x = k + 1 \\"+
            r"b_k(x) & \text{otherwise}"+
            r"\end{cases}")\
            .next_to(induction_b_next)
        

        self.play(Write(induction_a_expanded), Write(induction_b_expanded))
        self.wait(3)

        self.play(
            Unwrite(induction_a_expanded), 
            Unwrite(induction_b_expanded),
            Unwrite(induction_a_next),
            Unwrite(induction_b_next)
        )

        induction_next_choose = Tex(r"Choose $x \neq k + 1: a_k(x)b_k(x) \neq b_k(x)a_k(x)$.").move_to(induction_a_next, LEFT).shift(UP)
        self.play(Write(induction_next_choose))

        induction_final_a = MathTex(r"a_{k+1}(x) = ", r"\begin{cases}k + 1 & \text{if } x = k + 1 \\ a_k(x) & \text{otherwise}\end{cases}")\
            .next_to(induction_next_choose, DOWN, aligned_edge=LEFT)
        induction_final_b = MathTex(r"b_{k+1}(x) = ", r"\begin{cases}k + 1 & \text{if } x = k + 1 \\ b_k(x) & \text{otherwise}\end{cases}")\
            .next_to(induction_final_a, DOWN, aligned_edge=LEFT)

        self.play(Write(induction_final_a), Write(induction_final_b))

        induction_final_a_highlight = Rectangle(YELLOW, fill_opacity=0.5, height=0.6, width=3.8)\
            .next_to(induction_final_a[0])\
            .shift(DOWN * 0.4, RIGHT * 0.3)
        induction_final_b_highlight = induction_final_a_highlight.copy()\
            .shift(induction_final_b.get_center() - induction_final_a.get_center())
        self.play(Create(induction_final_a_highlight), Create(induction_final_b_highlight))
        self.wait(0.5)
        self.play(Uncreate(induction_final_a_highlight), Uncreate(induction_final_b_highlight))

        induction_final_a_replacement = MathTex(r"a_k(x)").next_to(induction_final_a[0])
        induction_final_b_replacement = MathTex(r"b_k(x)").next_to(induction_final_b[0])
        self.play(
            ReplacementTransform(induction_final_a[1], induction_final_a_replacement),
            ReplacementTransform(induction_final_b[1], induction_final_b_replacement)
        )
        self.wait(3)

        penultimate_result = MathTex(r"a_{k+1}(x)b_{k+1}(x) \neq b_{k+1}(x)a_{k+1}(x),", font_size=44)\
            .next_to(induction_final_a, DOWN, aligned_edge=LEFT)\
            .set_y(0.5 * (induction_final_a.get_y() + induction_final_b.get_y()))
        
        self.play(
            FadeOut(induction_final_a_replacement, induction_final_b_replacement),
            ReplacementTransform(induction_final_a[0], penultimate_result),
            AnimationGroup(
                Transform(induction_final_b[0], penultimate_result),
                FadeOut(induction_final_b[0])
            )
        )
        self.wait(1)

        conclusion_sentence = Tex(r"so $S_{k+1}$ is non-Abelian. \qedsymbol", 
            tex_template=TexTemplate(preamble=r"\usepackage{amsthm}"), font_size=44)\
            .next_to(penultimate_result, RIGHT)
        
        self.play(
            Write(conclusion_sentence)
        )
        self.wait(2)

        self.play(
            Unwrite(conclusion_sentence),
            Unwrite(penultimate_result),
            Unwrite(induction_next_choose),
            FadeOut(
                induction_step,
                line,
                desc
            )
        )
        self.wait()


        
        

    
        
