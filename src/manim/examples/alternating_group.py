from manim import *
from permutation_group_definition import write_group_defs

class AlternatingGroup(Scene):
    def construct(self):
        write_group_defs(self, "Alternating Group", r"A_3", 
            [r"x \in S_3 \text{ if $x$ can be written as a composition of an even number of cycles of length $2$}"],
            "\circ", math_font_size=32, read_time=7
        )