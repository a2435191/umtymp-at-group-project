from manim import *
from permutation_group_definition import write_group_defs

class SymmetricalGroup(Scene):
    def construct(self):
        matrix_1 = r"""\begin{bmatrix}
1 & 2 & 3 & \cdots & n \\
1 & 2 & 3 & \cdots & n \\
\end{bmatrix}"""
        matrix_2 = r"""\begin{bmatrix}
1 & 2 & 3 & \cdots & n \\
2 & 3 & 4 & \cdots & 1 \\
\end{bmatrix}"""
        matrix_3 = r"""\begin{bmatrix}
1 & 2 & 3 & \cdots & n \\
n & 1 & 2 & \cdots & n - 1 \\
\end{bmatrix}"""

        write_group_defs(self, "Symmetrical Group", r"S_n", [matrix_1, matrix_2, matrix_3], r"\circ", True, 72, 36)