from manim import *
from itertools import permutations
from typing import Iterable, List
from numpy import arange
from math import factorial
from permutation_group_definition import write_group_defs

class SymmetricalGroup(Scene):
    def construct(self):
        bottom_rows = list(permutations("123"))
        bmatrices: List[str] = []
        for row in bottom_rows:
            matrix = r"\begin{bmatrix}"\
                r"1 & 2 & 3 \\" +\
                " & ".join(row) + r" \\"\
                r"\end{bmatrix}"
            bmatrices.append(matrix)


        write_group_defs(self, "Symmetric Group", r"S_3", bmatrices, r"\circ", math_font_size=36, read_time=4.0)

class ShowAllBijections(Scene): 
    @staticmethod
    def _cycle_from_permutation(perm: Iterable[int]) -> List[List[int]]:
        # horribly inefficient. bite me.
        cycles: List[Dict[int, None]] = []
        for old, new in enumerate(perm):
            if old == new:
                cycles.append({old: None})
                continue

            target_lst = None
            for lst in cycles:
                if old in lst:
                    target_lst = lst
                    break
            
            if target_lst is None:
                cycles.append({old: None})
                target_lst = cycles[-1]
            
            while new != old:
                target_lst[new] = None
                new = perm[new]
        
        return [list(d.keys()) for d in cycles]

    def construct(self):

        N = 4
        if (N % 2 == 0):
            hrange = arange(-N / 2, N / 2, 1.0) + 0.5
        else:
            hrange = arange(-(N // 2), N // 2 + 1, 1.0)
        CELL_SIZE = 1.0
        HORIZ_DIST = 1
        l_row = VGroup(*[
            Square(CELL_SIZE).shift(HORIZ_DIST * LEFT,  i * CELL_SIZE * UP).set_stroke(width=1.0)
            for i in hrange
        ])
        r_row = VGroup(*[
            Square(CELL_SIZE).shift(HORIZ_DIST * RIGHT, i * CELL_SIZE * UP).set_stroke(width=1.0)
            for i in hrange
        ])
        assert len(l_row) == len(r_row) == N, (len(l_row), len(r_row), N, hrange)
        self.play(Create(l_row), Create(r_row))

        self.wait(0.5)

        

        for i, permutation in enumerate(permutations(range(N), N)):
            arrows = VGroup(*[
                Arrow(l_row[old_idx].get_center(), r_row[new_idx].get_center(), stroke_width=1.0, buff=0, tip_length=0.1) 
                for old_idx, new_idx in enumerate(permutation)
            ])

            cycles: List[List[int]] = ShowAllBijections._cycle_from_permutation(permutation)
            cycles_str = ''.join([f"({' '.join([str(n + 1) for n in cycle])})" for cycle in cycles])
            text = Text(cycles_str).shift(3 * UP)

            if i == 0:
                self.play(Write(text))
                self.play(Create(arrows), run_time=0.50)
            else:
                self.add_foreground_mobject(text)
                self.add_foreground_mobject(arrows)
                self.wait(0.20)
            if i != factorial(N) - 1:
                self.wait(0.5)
                self.remove(text)
                self.remove(arrows)
        
        self.play(Uncreate(text))
        self.play(Uncreate(arrows))
        self.play(Uncreate(l_row), Uncreate(r_row))
        self.wait(0.5)