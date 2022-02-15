from manim import *
import numpy as np
import math
from typing import List
from copy import deepcopy
from itertools import permutations

class ArrayNotation(Scene):
    def construct(self):
        CIRCLE_COLORS = ['#0000FF', '#FF0000', '#FFFF00']
        POSITIONS = [3 * LEFT, 0, 3 * RIGHT]


        big_circles = VGroup(*[Circle(0.5, color, fill_opacity=0.75).shift(pos) 
            for color, pos in zip(CIRCLE_COLORS, POSITIONS)])
        big_circles_text = VGroup(*[Tex(str(i + 1)).shift(pos) # separate so that we can use Create/Write separately
            for i, pos in enumerate(POSITIONS)])

        self.play(Create(big_circles), Write(big_circles_text))
        self.wait(2)

        self.remove(big_circles, big_circles_text)
        big_circles.add(*big_circles_text) # so that text moves with circles
        
        
        V_SPACING, H_SPACING = 2, 5
        INTERNAL_V_SPACING = 0.75
        
        MY_UP = UP * V_SPACING
        MY_DN = DOWN * V_SPACING
        MY_LF = LEFT * H_SPACING
        MY_RT = RIGHT * H_SPACING
        center_coordinates = [
            MY_UP + MY_LF, MY_UP, MY_UP + MY_RT,
            MY_DN + MY_LF, MY_DN, MY_DN + MY_RT,
        ]

        top_circles = [big_circles.copy().scale(0.5).move_to(coord + INTERNAL_V_SPACING * UP).space_out_submobjects(0.75) 
            for coord in center_coordinates]
        btm_circles = [circle.copy().shift(2 * INTERNAL_V_SPACING * DOWN)
            for circle in top_circles]
        arrows: List[VGroup] = []
        for top_vgroup, btm_vgroup in zip(top_circles, btm_circles):
            arrow_group = VGroup(*[Arrow(top, btm) for top, btm in zip(top_vgroup, btm_vgroup) 
                if isinstance(top, Circle) and isinstance(btm, Circle)])
            arrows.append(arrow_group)


        self.play(*[ReplacementTransform(big_circles.copy(), circle) 
            for circle in top_circles])
        
        self.wait(1)

        self.play(*[ReplacementTransform(top_circle_group.copy(), btm_circle_group)
            for top_circle_group, btm_circle_group in zip(top_circles, btm_circles)])
        self.play(*[AnimationGroup(*[Create(arrow) for arrow in arrow_group]) 
            for arrow_group in arrows])
        
        self.wait()

        all_permutations = list(permutations([1, 2, 3], 3))
        internal_rotation_anims: List[AnimationGroup] = []
        for i, permutation in enumerate(all_permutations):
            btm_group = btm_circles[i]
            
            for old, new in enumerate(permutation):
                internal_rotation_anims.append(AnimationGroup(
                    btm_group[old].animate.move_to(btm_group[new - 1]),
                    btm_group[old + 3].animate.move_to(btm_group[new - 1 + 3]) # text
                ))
        self.play(*internal_rotation_anims)
            
        self.wait()

        uncreate_anims: List[Uncreate] = []
        for circle_group in top_circles + btm_circles:
            uncreate_anims += [Uncreate(circle_group[i]) for i in range(3)]
        for arrow_group in arrows:
            uncreate_anims += [Uncreate(arrow) for arrow in arrow_group]
        self.play(AnimationGroup(*uncreate_anims))
        self.wait()

        top_text = [VGroup(circle_group[3:6]) for circle_group in top_circles]
        btm_text = [VGroup(circle_group[3:6]) for circle_group in btm_circles]
        
        self.play(AnimationGroup(
            *[text.animate.shift(DOWN * INTERNAL_V_SPACING * 0.5) for text in top_text],
            *[text.animate.shift(UP   * INTERNAL_V_SPACING * 0.5) for text in btm_text]
        ))
        self.wait()

        l_bracket = Tex(r"\Bigg[")
        r_bracket = Tex(r"\Bigg]")

        self.play(AnimationGroup(
            *[Write(l_bracket.copy().move_to(text).shift(1.6 * LEFT  + 0.5 * INTERNAL_V_SPACING * DOWN)) for text in top_text],
            *[Write(r_bracket.copy().move_to(text).shift(1.6 * RIGHT + 0.5 * INTERNAL_V_SPACING * DOWN)) for text in top_text]
        ))
        self.wait()
        
        

        
