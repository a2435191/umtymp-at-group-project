# NOTE:UNUSED

from manim import *
from util_write_group_defs import write_group_defs

class PermutationGroupDefinition(Scene):
    def construct(self):
        matrix_one = r"""\begin{bmatrix}
    1 & 2 & 3 \\
    1 & 2 & 3
\end{bmatrix}"""
        matrix_two = r"""\begin{bmatrix}
    1 & 2 & 3 \\
    1 & 3 & 2
\end{bmatrix}"""
        matrix_three = r"""\begin{bmatrix}
    1 & 2 & 3 \\
    2 & 1 & 3
\end{bmatrix}"""


        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{amsmath}")
        
        write_group_defs(self, "Permutation Group", "G", 
            [matrix_one, matrix_two, matrix_three], r"\circ", 72, 50, tex_template=template)

