from manim import *

class PermutationGroupDefinition(Scene):
    def construct(self):
        tex_start = r"""$G = \Bigg(\bigg\{$"""
        matrix_one = r"""$\begin{bmatrix}
    1 & 2 & 3 \\
    1 & 2 & 3
\end{bmatrix}$"""
        matrix_two = r"""$\begin{bmatrix}
    1 & 2 & 3 \\
    1 & 3 & 2
\end{bmatrix}$"""
        matrix_three = r"""$\begin{bmatrix}
    1 & 2 & 3 \\
    2 & 1 & 3
\end{bmatrix}$"""
        after_matrices = r"""$\;\ldots\bigg\},\;$"""
        circ = r"""$\circ$"""
        tex_end = r"""$\Bigg)$"""



        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}")
        tex = Tex(
            tex_start, 
            matrix_one, ",", 
            matrix_two, ",", 
            matrix_three, after_matrices,
            circ, tex_end, 
            tex_template=template, font_size=50)

        tex.set_color_by_tex("bmatrix", RED)
        tex.set_color_by_tex("circ", BLUE)
        
        self.play(Write(tex))
        self.wait()
        self.play(Unwrite(tex))
        self.wait(0.5)

